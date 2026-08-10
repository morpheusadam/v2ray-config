#!/usr/bin/env python3
"""
harvest.py — the machine that maintains this repository.

Two files here are read at runtime by every installed copy of v2rayV: `subs/all.txt`, the
catalog of subscription links, and `proxies/all.txt`, the proxies it uses to reach GitHub
from a network that blocks it. Both rot fast. This script keeps them true, once a day,
from inside GitHub Actions:

    crawl     search GitHub for repositories and lists nobody has told us about
    collect   read every known source and pull out every candidate link
    prove     fetch each one and see whether it really carries working configs
    rank      score what survived, best first
    prune     retire anything that has not changed or answered in 12 days
    write     rewrite both files, sorted, with their headers intact

Ranking is the point of the whole thing, so it is worth stating what it measures. For a
subscription: how many of its servers actually accept a TCP connection, how fast they
answer, how recently the file changed, how many configs it carries, how few of them are
duplicates of everyone else's, and whether it uses protocols worth having. For a proxy:
whether a real request completes through it, how long that took, and how many days running
it has managed that. Neither score is a guess about a server's throughput — it is what can
be measured from a runner in a few seconds, which is reachability and latency.

Usage:

    python harvest.py daily                  everything, which is what CI runs
    python harvest.py subs run               subscriptions only
    python harvest.py proxies run            proxies only
    python harvest.py subs search            look for new repositories on GitHub
    python harvest.py subs status            print the current standings

Standard library only. `GITHUB_TOKEN` in the environment is optional and only raises API
rate limits — GitHub Actions provides one for free.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import ipaddress
import json
import math
import os
import random
import re
import socket
import ssl
import statistics
import struct
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

REPOS_FILE = HERE / "rapo.txt"
SUBS_FILE = HERE / "subs" / "all.txt"
SUBS_CANDIDATES = HERE / "subs" / "candidates.txt"
SUBS_STATUS = HERE / "subs" / "status.json"
SUBS_REPORT = HERE / "subs" / "STATUS.md"
SUBS_RETIRED = HERE / "subs" / "retired.txt"

PROXY_FILE = HERE / "proxies" / "all.txt"
PROXY_SOURCES = HERE / "proxies" / "sources.txt"
PROXY_STATUS = HERE / "proxies" / "status.json"
PROXY_REPORT = HERE / "proxies" / "STATUS.md"
PROXY_RETIRED = HERE / "proxies" / "retired.txt"

CACHE_DIR = HERE / ".cache"

USER_AGENT = "v2ray-config-harvest/2.0 (+https://github.com/morpheusadam/v2ray-config)"

# A window this size tells a subscription from a script and keeps a ten-million-line list
# from being downloaded just to classify it. Config counts are therefore "within the first
# window", not totals — which is all the ranking needs, and is fair across sources.
PROBE_BYTES = 64 * 1024

# The rule the owner set: anything that has not changed, or has not answered, for this
# long leaves the file. See `prune_stale`.
MAX_STALE_DAYS = 12

# The proxy test is the app's own job, done exactly: a TLS tunnel to the raw host and
# sixteen bytes of the subscription list back out of it. See proxies/PROMPT.md §3 — a proxy
# that passes a generic liveness check and then refuses CONNECT, or sits somewhere that
# cannot itself reach GitHub, is the single most common false positive in a naive checker.
PROXY_TARGET_HOST = "raw.githubusercontent.com"
PROXY_TARGET_PATH = "/morpheusadam/v2ray-config/main/subs/all.txt"
PROXY_DEADLINE = 8.0        # the app's own probe read timeout; slower is failure, not slow
PROXY_CONNECT_TIMEOUT = 6.0

# Public proxies flap. The app waits five dead runs before disabling a subscription source
# and this file follows the same instinct: three consecutive failures, then out.
PROXY_FAILURES_BEFORE_DROP = 3


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def days_since(value: str | None) -> float | None:
    stamp = parse_iso(value)
    if stamp is None:
        return None
    return (datetime.now(timezone.utc) - stamp).total_seconds() / 86400.0


def log(message: str = "") -> None:
    print(message, flush=True)


# =========================================================================== http


@dataclass
class Response:
    url: str
    status: int
    body: bytes
    headers: dict

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300

    def text(self) -> str:
        return self.body.decode("utf-8", errors="ignore")


def http_get(url: str, *, max_bytes: int | None = None, timeout: int = 25,
             headers: dict | None = None) -> Response | None:
    """A GET that never raises. None means there was no answer at all."""
    request_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if max_bytes:
        # Advisory only: a server that ignores it just sends more, and the read caps it.
        request_headers["Range"] = f"bytes=0-{max_bytes - 1}"
    if headers:
        request_headers.update(headers)

    request = urllib.request.Request(url, headers=request_headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(max_bytes) if max_bytes else response.read()
            return Response(url, response.status, body, dict(response.headers))
    except urllib.error.HTTPError as e:
        try:
            body = e.read(max_bytes or 4096)
        except Exception:
            body = b""
        return Response(url, e.code, body, dict(e.headers or {}))
    except Exception:
        return None


def github_api(path: str, *, timeout: int = 25) -> tuple[int, object]:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = http_get(f"https://api.github.com{path}", timeout=timeout, headers=headers)
    if response is None:
        return 0, None
    try:
        return response.status, json.loads(response.text())
    except Exception:
        return response.status, None


def has_token() -> bool:
    return bool(os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"))


# ============================================================================ urls

URL_RE = re.compile(r"""https?://[^\s'"`<>\\\[\](){}|,;]+""")
TRAILING_JUNK = ".,;:!?'\"`)]}>*_"

DEAD_HOSTS = (
    "shields.io", "img.shields.io", "badgen.net", "camo.githubusercontent.com",
    "user-images.githubusercontent.com", "private-user-images.githubusercontent.com",
    "avatars.githubusercontent.com", "opencollective.com", "t.me", "telegram.me",
    "telegram.org", "twitter.com", "x.com", "youtube.com", "youtu.be", "discord.gg",
    "discord.com", "instagram.com", "facebook.com", "linkedin.com", "reddit.com",
    "stackoverflow.com", "wikipedia.org", "google.com", "gstatic.com", "apache.org",
    "opensource.org", "creativecommons.org", "python.org", "pypi.org", "npmjs.com",
    "nodejs.org", "docker.com", "hub.docker.com", "letsencrypt.org", "cloudflare.com",
    "developer.mozilla.org", "gnu.org", "choosealicense.com", "api.github.com",
    "docs.github.com", "gitter.im", "patreon.com", "buymeacoffee.com", "ko-fi.com",
    "paypal.me", "star-history.com", "hits.dwyl.com", "visitor-badge.laobi.icu",
)

MEDIA_SUFFIXES = (
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico", ".mp4", ".webm",
    ".mp3", ".zip", ".tar", ".gz", ".7z", ".rar", ".exe", ".apk", ".dmg", ".deb", ".rpm",
    ".pdf", ".ttf", ".woff", ".woff2", ".css", ".dat", ".db",
)
CODE_SUFFIXES = (".py", ".go", ".rs", ".java", ".kt", ".sh", ".ps1", ".php", ".rb", ".md")

NOISE_PATH_HINTS = (
    "/blob/", "/tree/", "/issues", "/pulls", "/releases", "/actions", "/stargazers",
    "/watchers", "/network/", "/graphs/", "/wiki", "/security", "/discussions",
    "requirements.txt", "license", "changelog", "contributing", "code_of_conduct",
    ".github/", "/workflows/", "package.json", "go.mod", "cargo.toml",
)


def normalize_url(raw: str) -> str | None:
    """
    The rules `AutoModeSourceManager.normalizeUrl` applies on the phone, plus the rewrites
    that turn a human-facing GitHub link into the raw file behind it.

    Anything this returns survives the app's own parser. That is the point: a link the app
    would silently drop must never reach `subs/all.txt`.
    """
    url = (raw or "").strip().rstrip(TRAILING_JUNK)
    if not url or not url.lower().startswith(("http://", "https://")):
        return None

    lowered = url.lower()
    # Placeholder rows are rejected whole, not truncated: ".../<CODE>.sub.txt" cut at the
    # bracket becomes a valid-looking directory URL that returns nothing.
    if "<" in url or ">" in url or "{" in url or "}" in url:
        return None
    if "your_username" in lowered or "your_repository" in lowered:
        return None

    if url.startswith("https://github.com/") and "/blob/" in url:
        url = url.replace("https://github.com/", "https://raw.githubusercontent.com/", 1)
        url = url.replace("/blob/", "/", 1)
    elif url.startswith("https://github.com/") and "/raw/" in url:
        url = url.replace("https://github.com/", "https://raw.githubusercontent.com/", 1)
        url = url.replace("/raw/", "/", 1)

    # jsdelivr mirrors the same bytes, but the raw host is what the app's mirror ladder
    # expands from, so the canonical form is the one worth storing.
    jsdelivr = re.match(r"^https://cdn\.jsdelivr\.net/gh/([^/@]+)/([^/@]+)@([^/]+)/(.+)$", url)
    if jsdelivr:
        user, repo, ref, path = jsdelivr.groups()
        url = f"https://raw.githubusercontent.com/{user}/{repo}/{ref}/{path}"

    url = url.split("?raw=true")[0]

    try:
        if not urllib.parse.urlsplit(url).hostname:
            return None
    except Exception:
        return None
    return url


def is_plausible_sub(url: str) -> bool:
    """A pre-filter that only avoids wasting a fetch. Proof is the fetch itself."""
    lowered = url.lower()
    split = urllib.parse.urlsplit(lowered)
    host = split.hostname or ""

    if any(host == h or host.endswith("." + h) for h in DEAD_HOSTS):
        return False
    if split.path.endswith(MEDIA_SUFFIXES) or split.path.endswith(CODE_SUFFIXES):
        return False
    if any(hint in lowered for hint in NOISE_PATH_HINTS):
        return False
    # A bare repository page is a source of links, not a list of servers.
    if host == "github.com" and lowered.count("/") <= 4:
        return False
    return True


def extract_urls(text: str) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for match in URL_RE.findall(text or ""):
        url = normalize_url(match)
        if url and is_plausible_sub(url) and url not in seen:
            seen.add(url)
            found.append(url)
    return found


# ========================================================== configs and their servers

CONFIG_SCHEMES = (
    "vless://", "vmess://", "trojan://", "ss://", "ssr://", "hysteria://", "hysteria2://",
    "hy2://", "tuic://", "juicity://", "anytls://", "wireguard://", "socks://",
)

# Protocols and transports worth more than a plain VMess over TCP: they survive active
# probing, which is what decides whether a server lives more than a week.
MODERN_MARKERS = ("reality", "security=tls", "hysteria2://", "hy2://", "tuic://", "xtls",
                  "vless://", "grpc", "ws")

CONFIG_URI_RE = re.compile(
    r"(?:" + "|".join(re.escape(s) for s in CONFIG_SCHEMES) + r")[^\s\"'<>]+"
)

B64_ALPHABET = re.compile(r"^[A-Za-z0-9+/=_\-\s]+$")


def count_configs(text: str) -> tuple[int, list[str]]:
    total, protocols = 0, []
    for scheme in CONFIG_SCHEMES:
        n = text.count(scheme)
        if n:
            total += n
            protocols.append(scheme[:-3])
    return total, protocols


def try_base64(text: str, min_len: int = 64) -> str | None:
    """
    Most subscription files are one base64 blob. Decodes it when that is what this is.

    A partial download almost never ends on a 4-byte boundary, so the tail is trimmed
    rather than padded: a truncated last config costs nothing, a decode failure costs the
    whole file.
    """
    compact = re.sub(r"\s+", "", text)
    if len(compact) < min_len or not B64_ALPHABET.match(compact):
        return None
    compact = compact[: len(compact) - (len(compact) % 4)]
    for decoder in (base64.b64decode, base64.urlsafe_b64decode):
        try:
            return decoder(compact).decode("utf-8", errors="ignore")
        except (binascii.Error, ValueError):
            continue
    return None


def parse_endpoint(uri: str) -> tuple[str, int] | None:
    """
    The host and port a config actually dials.

    Every protocol here ends up as `[userinfo@]host:port` after its own preamble, except
    VMess, which is a base64 JSON object, and SSR, which is a base64 colon-separated line.
    """
    scheme, sep, rest = uri.strip().partition("://")
    if not sep:
        return None
    scheme = scheme.lower()

    if scheme == "vmess":
        decoded = try_base64(rest.split("#")[0], min_len=24)
        if not decoded:
            return None
        try:
            obj = json.loads(decoded)
        except Exception:
            return None
        host = str(obj.get("add") or obj.get("host") or "").strip()
        try:
            port = int(str(obj.get("port") or 0))
        except ValueError:
            return None
        return (host, port) if host and 0 < port < 65536 else None

    if scheme == "ssr":
        decoded = try_base64(rest.split("#")[0], min_len=16)
        if not decoded:
            return None
        parts = decoded.split(":")
        if len(parts) >= 2 and parts[1].isdigit():
            return parts[0], int(parts[1])
        return None

    body = rest.split("#")[0]
    if "@" not in body and scheme == "ss":
        # ss://base64(method:pass@host:port) — the older of the two shapes.
        decoded = try_base64(body, min_len=16)
        if not decoded or "@" not in decoded:
            return None
        body = decoded
    body = body.split("?")[0].split("/")[0]

    authority = body.rsplit("@", 1)[-1]
    bracketed = re.match(r"^\[([^\]]+)\]:(\d+)$", authority)
    if bracketed:
        return bracketed.group(1), int(bracketed.group(2))
    host, _, port = authority.rpartition(":")
    if not host or not port.isdigit():
        return None
    port_number = int(port)
    if not 0 < port_number < 65536:
        return None
    # A host has to look like one; scraped lists carry fragments that do not.
    if not re.match(r"^[A-Za-z0-9._-]+$", host):
        return None
    return host, port_number


def endpoints_of(text: str, limit: int = 400) -> list[tuple[str, int]]:
    seen: set[tuple[str, int]] = set()
    ordered: list[tuple[str, int]] = []
    for uri in CONFIG_URI_RE.findall(text):
        endpoint = parse_endpoint(uri)
        if endpoint and endpoint not in seen:
            seen.add(endpoint)
            ordered.append(endpoint)
            if len(ordered) >= limit:
                break
    return ordered


def tcp_latency(endpoint: tuple[str, int], timeout: float = 3.0) -> float | None:
    """Milliseconds to complete a TCP handshake, or None when it never completed."""
    started = time.perf_counter()
    try:
        with socket.create_connection(endpoint, timeout=timeout):
            return (time.perf_counter() - started) * 1000.0
    except Exception:
        return None


# ===================================================================== classification


@dataclass
class Verdict:
    kind: str = "other"   # configs | catalog | clash | html | empty | dead | other
    configs: int = 0
    protocols: list = field(default_factory=list)
    links: list = field(default_factory=list)
    http_status: int = 0
    bytes: int = 0
    last_modified: str = ""
    note: str = ""
    digest: str = ""
    body: str = ""       # decoded text; released once the scoring pass has read it
    markers: int = 0     # occurrences of the protocol markers worth having


def classify(response: Response | None) -> Verdict:
    if response is None:
        return Verdict(kind="dead", note="no response")
    if not response.ok and response.status != 206:
        return Verdict(kind="dead", http_status=response.status, note=f"HTTP {response.status}")

    text = response.text()
    verdict = Verdict(
        http_status=response.status,
        bytes=len(response.body),
        last_modified=response.headers.get("Last-Modified", "")
        or response.headers.get("last-modified", ""),
    )

    if not text.strip():
        verdict.kind = "empty"
        return verdict

    head = text[:2000].lower()
    if "<html" in head or "<!doctype html" in head:
        verdict.kind = "html"
        return verdict

    plain = text
    count, protocols = count_configs(text)
    if count == 0:
        decoded = try_base64(text)
        if decoded:
            count, protocols = count_configs(decoded)
            if count:
                verdict.note = "base64"
                plain = decoded

    # Two, not one: a README fragment or a rule file can mention a single URI by accident,
    # and one config is not a subscription worth carrying.
    if count >= 2:
        verdict.kind = "configs"
        verdict.configs = count
        verdict.protocols = protocols
        verdict.body = plain
        # Over the decoded text, because several sources re-encode the same servers on
        # every build and a digest of the raw bytes would call that a daily update.
        verdict.digest = hashlib.sha256(plain.encode("utf-8", "ignore")).hexdigest()[:16]
        return verdict

    if re.search(r"^\s*proxies:", text[:4000], re.M) or "proxy-groups:" in head:
        verdict.kind = "clash"
        return verdict

    links = extract_urls(text)
    if len(links) >= 3:
        verdict.kind = "catalog"
        verdict.links = links
        return verdict

    return verdict


# ========================================================================= status io


def load_json(path: Path, default: dict) -> dict:
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                for key, value in default.items():
                    data.setdefault(key, value)
                return data
        except Exception:
            log(f"{path.name} is unreadable — starting a new one")
    return dict(default)


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")


def load_subs_status() -> dict:
    return load_json(SUBS_STATUS, {"generatedAt": "", "links": {}})


def load_proxy_status() -> dict:
    return load_json(PROXY_STATUS, {"generatedAt": "", "proxies": {}})


def save_proxy_status(status: dict) -> None:
    """
    Keeps only the endpoints that have ever worked.

    This file is committed on every run, and a run probes tens of thousands of endpoints of
    which a couple of hundred succeed. Remembering the rest would add ten megabytes a day
    to the repository to record that a stranger was, once again, a stranger — and they come
    back from the sources tomorrow anyway, so nothing is actually forgotten.
    """
    kept = {name: record for name, record in status["proxies"].items()
            if record.get("successes", 0) > 0}
    dropped = len(status["proxies"]) - len(kept)
    save_json(PROXY_STATUS, {**status, "proxies": kept})
    if dropped:
        log(f"status.json: kept {len(kept)} endpoints with a history, "
            f"forgot {dropped} that never worked")


def append_retired(path: Path, entries: list[tuple[str, str]]) -> None:
    """
    Retirement is not deletion. A link that comes back is recognised rather than treated
    as a stranger, and the reason it left is on the record.
    """
    if not entries:
        return
    stamp = now_iso()
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if not existing:
        existing = ("# Retired by harvest.py. Kept so a source that returns is recognised\n"
                    "# rather than rediscovered as a stranger. Format: date\treason\tvalue\n\n")
    lines = [f"{stamp}\t{reason}\t{value}" for value, reason in entries]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(existing.rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")


# =========================================================================== ranking


def speed_score(latency_ms: float | None) -> float:
    """
    1.0 at 60 ms, 0.0 at 2000 ms, logarithmic in between.

    Logarithmic because the difference between 60 ms and 200 ms matters to a person and
    the difference between 1.2 s and 1.5 s does not.
    """
    if latency_ms is None or latency_ms <= 0:
        return 0.0
    if latency_ms <= 60:
        return 1.0
    if latency_ms >= 2000:
        return 0.0
    return 1.0 - math.log(latency_ms / 60.0) / math.log(2000.0 / 60.0)


def freshness_score(days: float | None) -> float:
    """Full marks for a change today, nothing left by the retirement age."""
    if days is None:
        return 0.5          # never yet observed changing — neither rewarded nor punished
    if days <= 1:
        return 1.0
    if days >= MAX_STALE_DAYS:
        return 0.0
    return 1.0 - (days - 1) / (MAX_STALE_DAYS - 1)


def volume_score(configs: int) -> float:
    """Diminishing: 300 configs in a window is as much as anyone can use."""
    if configs <= 0:
        return 0.0
    return min(1.0, math.log10(1 + configs) / math.log10(301))


# Reachability and freshness carry this, not latency. Ranking servers by ping has been
# measured on this project as *worse than random*: the fastest responders were CDN edges
# fronting dead hosts. Speed keeps a small weight because a 2-second handshake really is a
# bad sign, but it is a tiebreak, not the ranking.
SUB_WEIGHTS = {
    "reach": 0.34,      # do its servers accept a connection at all
    "fresh": 0.20,      # how recently the file changed
    "clean": 0.14,      # how little of it is duplicated, by itself or by everyone else
    "speed": 0.12,      # how fast they answer — deliberately small, see above
    "volume": 0.12,     # how much it carries
    "modern": 0.08,     # reality / tls / hysteria2 rather than bare vmess
}


def score_sub(record: dict) -> float:
    parts = {
        "reach": record.get("reachRatio", 0.0),
        "speed": speed_score(record.get("medianLatencyMs")),
        "fresh": freshness_score(days_since(record.get("lastChanged"))),
        "volume": volume_score(record.get("configs", 0)),
        "clean": record.get("cleanRatio", 0.0),
        "modern": record.get("modernRatio", 0.0),
    }
    record["scoreParts"] = {k: round(v, 3) for k, v in parts.items()}
    return round(100.0 * sum(SUB_WEIGHTS[k] * v for k, v in parts.items()), 2)


# Diagnostic only — proxies/all.txt is deliberately *not* sorted by this. The app shuffles
# before drawing its 600, so any ranking in the file is discarded, and PROMPT.md §5 is
# explicit that sorting by latency is wasted work. The score exists to answer "which of
# these is worth keeping" in the report, and there the durable signal is history, not speed:
# the payload is a few hundred kilobytes once, so a 900 ms proxy that works beats a 40 ms
# one that does not.
PROXY_WEIGHTS = {
    "streak": 0.50,     # consecutive good runs, which is the only thing that predicts tomorrow
    "uptime": 0.40,     # successes out of checks, over its whole life
    "speed": 0.10,      # a tiebreak, and nothing more
}


def score_proxy(record: dict) -> float:
    asked = max(1, record.get("checks", 0))
    parts = {
        "speed": speed_score(record.get("latencyMs")),
        "uptime": record.get("successes", 0) / asked,
        "streak": min(1.0, record.get("streak", 0) / 7.0),
    }
    record["scoreParts"] = {k: round(v, 3) for k, v in parts.items()}
    return round(100.0 * sum(PROXY_WEIGHTS[k] * v for k, v in parts.items()), 2)


def prune_stale(records: dict, *, alive_key: str, change_key: str | None,
                max_days: int) -> list[tuple[str, str]]:
    """
    Retires anything that stopped answering, or stopped changing, more than `max_days` ago.

    A newly discovered entry is immune until it has been watched for that long: "has not
    changed in twelve days" is a claim about observation, and on day one there is none.
    """
    retired: list[tuple[str, str]] = []
    for key, record in list(records.items()):
        watched = days_since(record.get("firstSeen"))
        if watched is not None and watched < max_days:
            continue

        since_alive = days_since(record.get(alive_key))
        if since_alive is None or since_alive > max_days:
            reason = (f"no configs for {since_alive:.0f}d" if since_alive is not None
                      else "never alive")
            retired.append((key, reason))
            records.pop(key, None)
            continue

        if change_key:
            since_change = days_since(record.get(change_key))
            if since_change is not None and since_change > max_days:
                retired.append((key, f"unchanged for {since_change:.0f}d"))
                records.pop(key, None)
    return retired


# ==================================================================== subs: discovery


def read_repos() -> list[str]:
    if not REPOS_FILE.exists():
        return []
    repos = []
    for line in REPOS_FILE.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^https://github\.com/([^/]+)/([^/\s]+)/?$", line.strip())
        if match:
            repos.append(f"{match.group(1)}/{match.group(2)}")
    return repos


def write_repos(repos: list[str]) -> None:
    unique = sorted(set(repos), key=str.lower)
    REPOS_FILE.write_text("\n".join(f"https://github.com/{r}" for r in unique) + "\n",
                          encoding="utf-8")


DEFAULT_QUERIES = (
    "v2ray config", "v2ray subscription", "vless subscription", "free v2ray configs",
    "xray config collector", "v2ray-configs", "vmess subscription",
    "v2ray collector telegram", "free vpn configs vless", "sing-box subscription free",
    "hysteria2 subscription", "reality config free",
)


def stage_search(args) -> int:
    """
    Asks GitHub for repositories matching the usual queries and adds the new ones.

    Unauthenticated search allows ten requests a minute, so the pause between pages is not
    politeness — without it every request after the tenth is a 403.
    """
    queries = args.query or list(DEFAULT_QUERIES)
    have = set(read_repos())
    found: set[str] = set()
    pause = 2.5 if has_token() else 7.0

    log(f"searching GitHub: {len(queries)} queries x {args.pages} pages"
        f"{' (authenticated)' if has_token() else ' (unauthenticated, and therefore slow)'}")

    for query in queries:
        for page in range(1, args.pages + 1):
            status, data = github_api(
                f"/search/repositories?q={urllib.parse.quote(query)}"
                f"&sort=updated&order=desc&per_page=100&page={page}")
            if status == 403:
                log("  rate limited — waiting 60s")
                time.sleep(60)
                continue
            if status != 200 or not isinstance(data, dict):
                log(f"  {query!r} page {page}: HTTP {status}")
                break
            items = data.get("items") or []
            for item in items:
                if item.get("full_name"):
                    found.add(item["full_name"])
            log(f"  {query!r} page {page}: {len(items)} results, {len(found)} distinct")
            if len(items) < 100:
                break
            time.sleep(pause)
        time.sleep(pause)

    new = sorted(found - have, key=str.lower)
    if new:
        write_repos(list(have | found))
        log(f"{len(new)} new repositories added to {REPOS_FILE.name}")
        for name in new[:40]:
            log(f"  {name}")
        if len(new) > 40:
            log(f"  … and {len(new) - 40} more")
    else:
        log("no new repositories")
    return len(new)


README_NAMES = ("README.md", "README.MD", "readme.md", "Readme.md", "README",
                "README.txt", "README.rst")


def fetch_readme(repo: str, *, refresh: bool = False) -> str | None:
    cache = CACHE_DIR / "readme" / (repo.replace("/", "__") + ".md")
    if cache.exists() and not refresh:
        return cache.read_text(encoding="utf-8", errors="ignore")
    for name in README_NAMES:
        response = http_get(f"https://raw.githubusercontent.com/{repo}/HEAD/{name}", timeout=25)
        if response and response.ok and response.body.strip():
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(response.text(), encoding="utf-8")
            return response.text()
    return None


# Guesses worth seven cheap GETs against the raw host when a repository has no README.
COMMON_PATHS = (
    "sub.txt", "subs.txt", "all.txt", "config.txt", "configs.txt", "mix.txt",
    "all_configs.txt", "subscription.txt", "v2ray.txt", "vless.txt", "vmess.txt",
    "trojan.txt", "ss.txt", "sub/all.txt", "sub/sub.txt", "configs/all.txt",
    "Splitted-By-Protocol/vless.txt", "Config/all.txt", "output/all.txt",
)

TREE_NAME_HINTS = ("sub", "config", "all", "mix", "vless", "vmess", "trojan",
                   "shadowsocks", "ss", "hysteria", "hy2", "tuic", "reality", "merged",
                   "output", "result", "server")


def scan_tree(repo: str, *, budget: dict) -> list[str]:
    """
    Lists a repository's files through the API and keeps the ones that look like output.

    Only reached for repositories whose README gave nothing, because without a token the
    API allows sixty calls an hour and this spends one per repository. `budget` makes a
    run degrade to "scanned fewer" instead of a wall of 403s.
    """
    if budget["left"] <= 0:
        return []

    data = None
    ref = "HEAD"
    for candidate_ref in ("HEAD", "main", "master"):
        budget["left"] -= 1
        status, payload = github_api(f"/repos/{repo}/git/trees/{candidate_ref}?recursive=1")
        if status == 403:
            budget["left"] = 0
            budget["rate_limited"] = True
            return []
        if status == 200 and isinstance(payload, dict):
            data, ref = payload, candidate_ref
            break
        if budget["left"] <= 0:
            return []
    if data is None:
        return []

    candidates = []
    for entry in data.get("tree") or []:
        if entry.get("type") != "blob":
            continue
        path = entry.get("path", "")
        lowered = path.lower()
        name = lowered.rsplit("/", 1)[-1]
        if not (name.endswith(".txt") or "." not in name):
            continue
        if any(noise in lowered for noise in ("readme", "license", "requirements", ".github/")):
            continue
        if not any(hint in lowered for hint in TREE_NAME_HINTS):
            continue
        candidates.append(path)

    # Shallow first: a root-level all.txt is the maintained file, a country split forty
    # directories down is a slice of it.
    candidates.sort(key=lambda p: (p.count("/"), len(p)))
    if len(candidates) > 40:
        log(f"    {repo}: {len(candidates)} candidate paths, keeping the 40 shallowest")
        candidates = candidates[:40]

    return [f"https://raw.githubusercontent.com/{repo}/{ref}/{urllib.parse.quote(p)}"
            for p in candidates]


def probe_common_paths(repo: str) -> list[str]:
    found = []
    for path in COMMON_PATHS:
        url = f"https://raw.githubusercontent.com/{repo}/HEAD/{path}"
        response = http_get(url, max_bytes=4096, timeout=15)
        if response and (response.ok or response.status == 206) and response.body.strip():
            found.append(url)
    return found


def read_catalog_links() -> list[str]:
    if not SUBS_FILE.exists():
        return []
    return [line.strip() for line in SUBS_FILE.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")]


def stage_collect(args) -> dict[str, str]:
    """Every candidate link, mapped to the repository that published it."""
    repos = read_repos()
    if args.limit:
        repos = repos[: args.limit]
    log(f"{len(repos)} repositories in {REPOS_FILE.name}")

    origin: dict[str, str] = {}
    # What is already in the catalog is a candidate like any other: it has to prove itself
    # every day, or the twelve-day rule will eventually retire it.
    for url in read_catalog_links():
        origin[url] = "(catalog)"

    without_readme: list[str] = []

    def one(repo: str) -> tuple[str, list[str], bool]:
        readme = fetch_readme(repo, refresh=args.refresh)
        if readme is None:
            return repo, [], False
        return repo, extract_urls(readme), True

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for index, (repo, links, had_readme) in enumerate(pool.map(one, repos), 1):
            if not had_readme:
                without_readme.append(repo)
                continue
            for url in links:
                origin.setdefault(url, repo)
            if index % 20 == 0 or index == len(repos):
                log(f"  [{index}/{len(repos)}] {len(origin)} candidates so far")

    if without_readme and not args.no_guess:
        log(f"guessing common paths for {len(without_readme)} repositories with no README")
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for repo, links in zip(without_readme, pool.map(probe_common_paths, without_readme)):
                for url in links:
                    origin.setdefault(url, repo)

    if args.tree:
        seen_repos = {r for r in origin.values()}
        empty = [r for r in repos if r not in seen_repos]
        budget = {"left": args.tree_budget, "rate_limited": False}
        log(f"scanning file trees for {len(empty)} repositories (API budget {args.tree_budget})")
        for repo in empty:
            for url in scan_tree(repo, budget=budget):
                origin.setdefault(url, repo)
            if budget["left"] <= 0:
                log("    tree budget spent"
                    + (" (GitHub rate limit — set GITHUB_TOKEN)" if budget["rate_limited"] else ""))
                break

    SUBS_CANDIDATES.parent.mkdir(parents=True, exist_ok=True)
    SUBS_CANDIDATES.write_text(
        "\n".join(f"{url}\t{repo}" for url, repo in origin.items()) + "\n", encoding="utf-8")
    log(f"{len(origin)} unique candidates written to {SUBS_CANDIDATES.name}")
    return origin


def load_candidates() -> dict[str, str]:
    if not SUBS_CANDIDATES.exists():
        return {}
    origin = {}
    for line in SUBS_CANDIDATES.read_text(encoding="utf-8").splitlines():
        if line.strip():
            url, _, repo = line.partition("\t")
            origin.setdefault(url, repo)
    return origin


# ======================================================================= subs: proving


def stage_prove(args, origin: dict[str, str] | None = None) -> dict:
    """
    Fetches every candidate, decides what it is, and measures the servers inside it.

    Measurement and classification happen in one pass because both need the body, and the
    body is the expensive part.
    """
    origin = origin if origin is not None else load_candidates()
    if not origin:
        log("no candidates — run `subs collect` first")
        return load_subs_status()

    status = load_subs_status()
    stamp = now_iso()
    pending = [u for u in origin if not args.only_new or u not in status["links"]]
    log(f"proving {len(pending)} links, {args.samples} servers sampled from each")

    endpoint_owners: dict[tuple[str, int], set[str]] = {}

    def check(url: str) -> tuple[str, Verdict, list, list]:
        verdict = classify(http_get(url, max_bytes=args.probe_bytes, timeout=args.timeout))
        if verdict.kind != "configs":
            return url, verdict, [], []
        endpoints = endpoints_of(verdict.body)
        sample = (endpoints if len(endpoints) <= args.samples
                  else random.sample(endpoints, args.samples))
        # Everything the body is needed for is extracted here, then it is dropped: holding
        # 64 KB per link across three thousand links is a quarter of a gigabyte for nothing.
        lowered = verdict.body.lower()
        verdict.markers = sum(lowered.count(m) for m in MODERN_MARKERS)
        verdict.body = ""
        return url, verdict, endpoints, sample

    alive = 0
    catalog_links: list[str] = []
    results: list[tuple[str, Verdict, list, list]] = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for index, item in enumerate(pool.map(check, pending), 1):
            url, verdict, endpoints, _ = item
            results.append(item)
            if verdict.kind == "configs":
                alive += 1
                for endpoint in endpoints:
                    endpoint_owners.setdefault(endpoint, set()).add(url)
            elif verdict.kind == "catalog":
                catalog_links.extend(verdict.links)
            if index % 100 == 0 or index == len(pending):
                log(f"  [{index}/{len(pending)}] {alive} carrying configs")

    # One level of recursion: a file that is itself a list of subscription links is the
    # same shape as subs/all.txt, and its entries are usually the good ones.
    fresh = [u for u in dict.fromkeys(catalog_links)
             if u not in origin and u not in status["links"]]
    if fresh and not args.no_recurse:
        log(f"{len(fresh)} links found inside catalogs — proving those too")
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for index, item in enumerate(pool.map(check, fresh), 1):
                url, verdict, endpoints, _ = item
                origin.setdefault(url, "(catalog)")
                results.append(item)
                if verdict.kind == "configs":
                    alive += 1
                    for endpoint in endpoints:
                        endpoint_owners.setdefault(endpoint, set()).add(url)
                if index % 100 == 0 or index == len(fresh):
                    log(f"  [{index}/{len(fresh)}] {alive} carrying configs")

    # ---- measure the servers -------------------------------------------------------
    to_probe: dict[tuple[str, int], None] = {}
    for _, verdict, _, sample in results:
        if verdict.kind == "configs":
            for endpoint in sample:
                to_probe[endpoint] = None
    log(f"probing {len(to_probe)} distinct servers over TCP")

    latency: dict[tuple[str, int], float | None] = {}
    endpoints_list = list(to_probe)
    with ThreadPoolExecutor(max_workers=args.probe_workers) as pool:
        for index, (endpoint, ms) in enumerate(
                zip(endpoints_list, pool.map(lambda e: tcp_latency(e, args.tcp_timeout),
                                             endpoints_list)), 1):
            latency[endpoint] = ms
            if index % 500 == 0 or index == len(endpoints_list):
                reached = sum(1 for v in latency.values() if v is not None)
                log(f"  [{index}/{len(endpoints_list)}] {reached} reachable")

    # ---- write it all down ---------------------------------------------------------
    for url, verdict, endpoints, sample in results:
        record = status["links"].setdefault(url, {"firstSeen": stamp})
        record.update({
            "kind": verdict.kind,
            "configs": verdict.configs,
            "protocols": verdict.protocols,
            "httpStatus": verdict.http_status,
            "bytes": verdict.bytes,
            "lastChecked": stamp,
            "repo": origin.get(url, record.get("repo", "")),
        })
        if verdict.last_modified:
            record["lastModified"] = verdict.last_modified
        if verdict.kind != "configs":
            record["score"] = 0.0
            continue

        record["lastAlive"] = stamp
        if record.get("digest") != verdict.digest:
            record["lastChanged"] = stamp
            record["changes"] = record.get("changes", 0) + 1
        record["digest"] = verdict.digest

        measured = [latency[e] for e in sample if e in latency]
        reached = [ms for ms in measured if ms is not None]
        record["sampled"] = len(measured)
        record["reachRatio"] = round(len(reached) / len(measured), 3) if measured else 0.0
        record["medianLatencyMs"] = round(statistics.median(reached), 1) if reached else None

        # Clean means two things at once: few duplicates of itself, and few servers that
        # every other list is also handing out.
        self_clean = len(endpoints) / verdict.configs if verdict.configs else 0.0
        shared = [1.0 / len(endpoint_owners.get(e, {url})) for e in endpoints] or [0.0]
        record["cleanRatio"] = round(0.5 * min(1.0, self_clean) + 0.5 * (sum(shared) / len(shared)), 3)

        record["modernRatio"] = round(min(1.0, verdict.markers / max(1, verdict.configs)), 3)

        record["score"] = score_sub(record)

    status["generatedAt"] = stamp
    save_json(SUBS_STATUS, status)
    log(f"{alive} links carry configs. status written to {SUBS_STATUS.name}")
    return status


def stage_write_subs(args, status: dict | None = None) -> int:
    """
    Rewrites `subs/all.txt`: living links only, best score first, header count corrected.

    Order is not cosmetic. `AutoModeSourceManager.selectSources` gives the first two
    never-tried links a guaranteed slot every run, so what sits at the top of this file is
    what a fresh install tries first.
    """
    status = status or load_subs_status()
    links = status.get("links", {})

    # Rescored from the stored measurements every time, so that changing a weight takes
    # effect on the next write rather than only on links measured after the change.
    for record in links.values():
        if record.get("kind") == "configs":
            record["score"] = score_sub(record)

    retired = prune_stale(links, alive_key="lastAlive", change_key="lastChanged",
                          max_days=args.max_stale_days)
    if retired:
        append_retired(SUBS_RETIRED, retired)
        log(f"retired {len(retired)} links (nothing alive or changed in "
            f"{args.max_stale_days} days) — recorded in {SUBS_RETIRED.name}")

    alive = [(url, record) for url, record in links.items()
             if record.get("kind") == "configs"
             and record.get("configs", 0) >= args.min_configs]
    alive.sort(key=lambda item: -item[1].get("score", 0.0))

    header = [
        "# Subscription sources for Auto Mode",
        "#",
        "# One link per line. Lines starting with # are ignored, so notes like this are fine.",
        "# Paste this whole file into the Auto Mode settings window, or point \"Import file\" at it.",
        "#",
        "# Maintained by harvest.py, which runs once a day on GitHub Actions. Every link here",
        "# was fetched and proved to carry configs, and a sample of its servers was dialled",
        "# over TCP. The order is that measurement, best first: how many of its servers",
        "# answered, how recently the file changed, how little of it is duplicated, how fast",
        "# it answered, how much it carries, and whether it uses protocols worth having.",
        "#",
        f"# Anything that stops answering, or stops changing, for {args.max_stale_days} days leaves this file",
        f"# and is recorded in {SUBS_RETIRED.name}.",
        "#",
        f"# {len(alive)} links, generated {now_iso()}. None of them are operated by this project.",
    ]

    SUBS_FILE.parent.mkdir(parents=True, exist_ok=True)
    SUBS_FILE.write_text("\n".join(header + [""] + [url for url, _ in alive]) + "\n",
                         encoding="utf-8")

    status["generatedAt"] = now_iso()
    save_json(SUBS_STATUS, status)
    write_subs_report(status)
    log(f"subs/all.txt: {len(alive)} links, best score "
        f"{alive[0][1].get('score', 0) if alive else 0}")
    return len(alive)


def write_subs_report(status: dict) -> None:
    links = status.get("links", {})
    alive = {u: r for u, r in links.items() if r.get("kind") == "configs"}
    by_kind = Counter(r.get("kind", "?") for r in links.values())

    lines = [
        "# Subscription status",
        "",
        f"Generated {status.get('generatedAt', '—')} by `harvest.py`.",
        "",
        f"- **{len(alive)}** links carrying configs",
        f"- **{len(links)}** links on record",
        f"- retirement age: **{MAX_STALE_DAYS} days** without a change or an answer",
        "",
        "Score, each part in 0–1:",
        "",
        "> " + " + ".join(f"{weight:.2f}·{name}" for name, weight in SUB_WEIGHTS.items()),
        "",
        "**reach** is the share of sampled servers that completed a TCP handshake;",
        "**fresh** counts days since the file's decoded contents last changed; **clean**",
        "penalises a list that repeats itself or repeats everyone else; **speed** is the",
        "median handshake time, 1.0 at 60 ms and 0 at 2 s, and is weighted low on purpose —",
        "ranking servers by ping has measured worse than random here, because the fastest",
        "responders were CDN edges fronting dead hosts; **volume** saturates at 300 configs;",
        "**modern** rewards reality, TLS, hysteria2 and TUIC over bare VMess.",
        "",
        "| kind | count |",
        "|---|---|",
    ]
    for kind, count in by_kind.most_common():
        lines.append(f"| {kind} | {count} |")

    lines += [
        "",
        "## Live subscriptions, best first",
        "",
        "| # | score | link | configs | reach | median ms | last change | repo |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for index, (url, record) in enumerate(
            sorted(alive.items(), key=lambda kv: -kv[1].get("score", 0)), 1):
        latency = record.get("medianLatencyMs")
        lines.append(
            f"| {index} | {record.get('score', 0):.1f} | {url} | {record.get('configs', 0)} | "
            f"{record.get('reachRatio', 0):.0%} | {latency if latency else '—'} | "
            f"{(record.get('lastChanged', '') or '—')[:10]} | {record.get('repo', '')} |")

    dead = [(u, r) for u, r in links.items() if r.get("kind") != "configs"]
    if dead:
        lines += [
            "",
            "## Not carrying configs",
            "",
            "| link | kind | http | last checked |",
            "|---|---|---|---|",
        ]
        for url, record in sorted(dead, key=lambda kv: kv[1].get("kind", "")):
            lines.append(f"| {url} | {record.get('kind', '?')} | {record.get('httpStatus', 0)} "
                         f"| {(record.get('lastChecked', '') or '')[:10]} |")

    SUBS_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ============================================================================ proxies

DEFAULT_PROXY_SOURCES = """\
# Where proxies/all.txt comes from. One URL per line, # for comments.
# Add your own freely — anything that returns host:port lines will do, and every entry is
# proved by an actual request before it reaches all.txt.

https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt
https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt
https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt
https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt
https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt
https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt
https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt
https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt
https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt
https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt
https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt
https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt

# Very large — roughly 290,000 lines across the three, which is more than a daily probe
# budget can prove. Uncomment only alongside a raised --max-candidates, and remember that
# density is what matters: unproved volume makes the file worse, not better.
# https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt
# https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt
# https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt
"""

PROXY_SCHEMES = {
    "http": "http", "https": "http", "socks4": "socks4", "socks4a": "socks4",
    "socks5": "socks5", "socks5h": "socks5", "socks": "socks5",
}

# The port conventions AutoModeProxy uses to guess an unlabelled entry. Only a habit, but
# a strong one, and it turns three handshakes into one.
SOCKS5_PORTS = {1080, 1081, 1085, 1088, 1090, 10808, 10809, 9050, 9150, 7890, 7891}
SOCKS4_PORTS = {4145, 5678, 9091}
HTTP_PORTS = {80, 81, 800, 801, 808, 999, 3128, 3129, 8000, 8008, 8080, 8081, 8085,
              8086, 8090, 8118, 8123, 8888, 8889, 9000, 9080}


def parse_proxy_line(raw: str) -> tuple[str, int, str] | None:
    """
    One line of a scraped proxy list, in the shapes `AutoModeProxy.parse` accepts.

    Credentials are dropped rather than carried: a public list's `host:port:user:pass` is
    as often `host:port:country:anonymity`, and an entry that needs auth we cannot verify
    is worth less than the six seconds it costs to find out.
    """
    line = (raw or "").strip()
    if not line or line.startswith(("#", "//")):
        return None

    protocol = ""
    if "://" in line:
        scheme, _, rest = line.partition("://")
        protocol = PROXY_SCHEMES.get(scheme.lower(), "")
        if not protocol:
            return None
        line = rest

    line = line.split("/")[0].split("|")[0].split(" ")[0].split("\t")[0].strip()
    if "@" in line:
        line = line.rsplit("@", 1)[-1]
    parts = line.split(":")
    if len(parts) < 2:
        return None

    host, port = parts[0].strip(), parts[1].strip()
    if not port.isdigit() or not 0 < int(port) < 65536:
        return None
    # A host has to look like one. This rejects IPv6 and the "1.2.3.4:80:80:80" nonsense.
    if not host or not re.match(r"^[A-Za-z0-9.-]+$", host):
        return None

    # Private, loopback, link-local and carrier-grade NAT space. Free either way, and it
    # removes a surprising fraction of any scraped list.
    try:
        address = ipaddress.ip_address(host)
        if (address.is_private or address.is_loopback or address.is_reserved
                or address.is_link_local or address.is_multicast
                or address in ipaddress.ip_network("100.64.0.0/10")):
            return None
    except ValueError:
        pass  # a hostname, which is fine

    if not protocol:
        port_number = int(port)
        protocol = ("socks5" if port_number in SOCKS5_PORTS else
                    "socks4" if port_number in SOCKS4_PORTS else
                    "http" if port_number in HTTP_PORTS else "")
    return host, int(port), protocol


def _recv_exactly(sock: socket.socket, count: int) -> bytes:
    buffer = b""
    while len(buffer) < count:
        piece = sock.recv(count - len(buffer))
        if not piece:
            break
        buffer += piece
    return buffer


def _handshake_http(sock: socket.socket) -> bool:
    """CONNECT to port 443. Many public HTTP proxies allow GET and refuse this."""
    sock.sendall((f"CONNECT {PROXY_TARGET_HOST}:443 HTTP/1.1\r\n"
                  f"Host: {PROXY_TARGET_HOST}:443\r\n"
                  f"User-Agent: {USER_AGENT}\r\nProxy-Connection: keep-alive\r\n\r\n").encode())
    head = b""
    while b"\r\n\r\n" not in head and len(head) < 1024:
        piece = sock.recv(256)
        if not piece:
            break
        head += piece
    return b" 200" in head[:32]


def _handshake_socks5(sock: socket.socket) -> bool:
    """
    Domain-name address type only.

    The app never resolves the destination locally — on a network that answers DNS with a
    lie, handing a proxy an IP defeats the point — so a SOCKS5 server that cannot take a
    hostname is no use here even though it works.
    """
    sock.sendall(b"\x05\x01\x00")
    greeting = _recv_exactly(sock, 2)
    if len(greeting) != 2 or greeting[0] != 5 or greeting[1] != 0:
        return False

    host_bytes = PROXY_TARGET_HOST.encode()
    sock.sendall(b"\x05\x01\x00\x03" + bytes([len(host_bytes)]) + host_bytes
                 + struct.pack(">H", 443))
    reply = _recv_exactly(sock, 4)
    if len(reply) < 4 or reply[1] != 0:
        return False
    # Consume the bound address so the stream starts clean for TLS.
    if reply[3] == 1:
        _recv_exactly(sock, 6)
    elif reply[3] == 3:
        length = _recv_exactly(sock, 1)
        _recv_exactly(sock, (length[0] if length else 0) + 2)
    elif reply[3] == 4:
        _recv_exactly(sock, 18)
    return True


def _handshake_socks4a(sock: socket.socket) -> bool:
    """
    SOCKS4a specifically: destination IP 0.0.0.1 signals "the hostname follows".

    Plain SOCKS4 cannot carry a name, so it is not a weaker version of this — it is a
    different thing that this app cannot use at all.
    """
    sock.sendall(b"\x04\x01" + struct.pack(">H", 443) + b"\x00\x00\x00\x01" + b"\x00"
                 + PROXY_TARGET_HOST.encode() + b"\x00")
    reply = _recv_exactly(sock, 8)
    return len(reply) >= 2 and reply[1] == 0x5A


def probe_proxy(host: str, port: int, protocol: str,
                deadline: float = PROXY_DEADLINE) -> tuple[str, float] | None:
    """
    The app's own probe, run against one candidate: handshake, TLS, sixteen bytes back.

    Anything short of this ships a file whose entries pass our check and fail the app's —
    which shows up in production as "no working proxy among 600 tried" while the report
    here claims forty percent healthy.

    An unlabelled entry is tried in the order its port suggests, and whichever protocol
    completes is the one recorded, because writing the scheme down is what turns three
    handshakes on the phone into one.
    """
    order = [protocol] if protocol else (
        ["socks5", "http", "socks4"] if port in SOCKS5_PORTS else
        ["socks4", "socks5", "http"] if port in SOCKS4_PORTS else
        ["http", "socks5", "socks4"])

    context = ssl.create_default_context()

    for candidate in order:
        started = time.perf_counter()

        def left() -> float:
            return deadline - (time.perf_counter() - started)

        try:
            with socket.create_connection(
                    (host, port), timeout=min(PROXY_CONNECT_TIMEOUT, deadline)) as sock:
                sock.settimeout(max(0.5, left()))

                if candidate == "http":
                    ok = _handshake_http(sock)
                elif candidate == "socks5":
                    ok = _handshake_socks5(sock)
                else:
                    ok = _handshake_socks4a(sock)
                if not ok or left() <= 0:
                    continue

                sock.settimeout(max(0.5, left()))
                with context.wrap_socket(sock, server_hostname=PROXY_TARGET_HOST) as tls:
                    tls.settimeout(max(0.5, left()))
                    tls.sendall((f"GET {PROXY_TARGET_PATH} HTTP/1.1\r\n"
                                 f"Host: {PROXY_TARGET_HOST}\r\n"
                                 f"Range: bytes=0-15\r\n"
                                 f"User-Agent: {USER_AGENT}\r\n"
                                 f"Accept: */*\r\nConnection: close\r\n\r\n").encode())

                    head = b""
                    while b"\r\n\r\n" not in head and len(head) < 4096 and left() > 0:
                        piece = tls.recv(512)
                        if not piece:
                            break
                        head += piece
                    if not (b" 206" in head[:32] or b" 200" in head[:32]):
                        continue

                    body = head.split(b"\r\n\r\n", 1)[1] if b"\r\n\r\n" in head else b""
                    if not body and left() > 0:
                        try:
                            body = tls.recv(64)
                        except Exception:
                            body = b""
                    if not body:
                        continue

                    # The deadline is a wall-clock promise, and the per-operation timeouts
                    # above cannot keep it on their own: each one is allowed a floor of half
                    # a second, so a chain of them can overrun. An entry that needed longer
                    # than the app allows is a failure, not a slow success.
                    elapsed = (time.perf_counter() - started) * 1000.0
                    if elapsed > deadline * 1000.0:
                        continue
                    return candidate, elapsed
        except Exception:
            continue
    return None


def read_proxy_sources() -> list[str]:
    if not PROXY_SOURCES.exists():
        PROXY_SOURCES.parent.mkdir(parents=True, exist_ok=True)
        PROXY_SOURCES.write_text(DEFAULT_PROXY_SOURCES, encoding="utf-8")
        log(f"wrote a starting {PROXY_SOURCES.name}")
    return [line.strip() for line in PROXY_SOURCES.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")]


def lookup_countries(hosts: list[str]) -> dict[str, str]:
    """
    Two-letter country per IP, in batches of a hundred, best effort.

    Only for the human reading the file and the diff: where a proxy sits decides whether
    an Iranian network can reach it at all, and that is the one leg this checker cannot
    test from a runner in Europe.
    """
    result: dict[str, str] = {}
    batch_size = 100
    for start in range(0, len(hosts), batch_size):
        batch = hosts[start:start + batch_size]
        payload = json.dumps([{"query": h, "fields": "status,countryCode,query"} for h in batch])
        request = urllib.request.Request(
            "http://ip-api.com/batch", data=payload.encode(),
            headers={"Content-Type": "application/json", "User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                for entry in json.loads(response.read().decode()):
                    if entry.get("status") == "success" and entry.get("query"):
                        result[entry["query"]] = entry.get("countryCode") or "??"
        except Exception:
            return result       # the free endpoint rate-limits; a partial map is fine
        time.sleep(1.5)         # 45 requests a minute is the documented ceiling
    return result


def measure_density(entries: list[tuple[str, dict]], sample_size: int,
                    workers: int) -> tuple[int, int]:
    """
    The file's only real quality score: of N drawn at random, how many work right now.

    Measured the way the app measures it — a random sample of the shipped file, not the
    entries that happened to pass during generation.
    """
    if not entries:
        return 0, 0
    sample = (entries if len(entries) <= sample_size
              else random.sample(entries, sample_size))

    def check(item) -> bool:
        name, record = item
        host, _, port = name.rpartition(":")
        return probe_proxy(host, int(port), record.get("protocol", "")) is not None

    with ThreadPoolExecutor(max_workers=workers) as pool:
        return sum(1 for ok in pool.map(check, sample) if ok), len(sample)


def stage_proxies(args) -> int:
    """
    The whole proxy side: collect, prove, retire, rewrite.

    One stage rather than four because, unlike a subscription link, a proxy is worth
    nothing between runs — the only durable state is how many days it has worked.
    """
    sources = read_proxy_sources()
    log(f"{len(sources)} proxy sources")

    status = load_proxy_status()
    stamp = now_iso()
    candidates: dict[tuple[str, int], str] = {}

    # Yesterday's winners first, and re-proved: an endpoint that has worked three days
    # running is worth more than any stranger, and its history is the only thing here
    # that cannot be rebuilt from scratch.
    for key, record in status["proxies"].items():
        host, _, port = key.rpartition(":")
        if port.isdigit():
            candidates[(host, int(port))] = record.get("protocol", "")

    # And whatever is already published, which on the first run — before any status file
    # exists — is the only record of what used to work, and must be treated as history
    # rather than thrown in with the strangers when the probe budget is capped.
    if PROXY_FILE.exists():
        for line in PROXY_FILE.read_text(encoding="utf-8").splitlines():
            parsed = parse_proxy_line(line)
            if parsed and (parsed[0], parsed[1]) not in candidates:
                candidates[(parsed[0], parsed[1])] = parsed[2]
    carried = set(candidates)
    log(f"{len(carried)} endpoints carried over from previous runs")

    def pull(url: str) -> tuple[int, list[str]]:
        response = http_get(url, timeout=args.timeout, max_bytes=8 * 1024 * 1024)
        if response is None:
            return 0, []
        if response.ok or response.status == 206:
            return response.status, response.text().splitlines()
        return response.status, []

    # A source that has moved returns 404 and yields nothing, which reads in a log exactly
    # like a source that is simply quiet today. The difference is worth shouting about:
    # three of the seeded sources had silently gone 404 before this was recorded.
    health: dict[str, dict] = status.setdefault("sources", {})
    broken: list[str] = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for url, (http_status, lines) in zip(sources, pool.map(pull, sources)):
            added = usable = 0
            for line in lines:
                parsed = parse_proxy_line(line)
                if not parsed:
                    continue
                usable += 1
                host, port, protocol = parsed
                if (host, port) not in candidates:
                    added += 1
                # A scheme from the source beats the port heuristic; never overwrite a
                # known scheme with a blank one.
                if protocol or (host, port) not in candidates:
                    candidates[(host, port)] = protocol or candidates.get((host, port), "")

            record = health.setdefault(url, {"firstSeen": stamp})
            record.update({"lastChecked": stamp, "httpStatus": http_status,
                           "lines": len(lines), "usable": usable, "new": added})
            if usable:
                record["lastYielded"] = stamp
            else:
                broken.append(url)
            log(f"  {'OK ' if usable else 'DEAD'} {added:>6} new  {url}")

    if broken:
        log(f"\n  {len(broken)} sources yielded nothing — check or replace them:")
        for url in broken:
            log(f"    HTTP {health[url]['httpStatus']}  {url}")
        log("")

    log(f"{len(candidates)} distinct endpoints to prove")

    # Carried-over endpoints keep their place at the front — they have a history, which is
    # the only thing here that predicts tomorrow. The rest is sampled rather than truncated,
    # so a cap does not silently mean "whichever source happened to load first".
    cap = args.limit or args.max_candidates
    if cap and len(candidates) > cap:
        strangers = [k for k in candidates if k not in carried]
        room = max(0, cap - len(carried))
        keep = set(random.sample(strangers, min(room, len(strangers))))
        log(f"capping at {cap}: {len(carried)} with history + {len(keep)} sampled "
            f"from {len(strangers)} strangers ({len(strangers) - len(keep)} left for tomorrow)")
        candidates = {k: v for k, v in candidates.items() if k in carried or k in keep}

    keys = list(candidates)
    working = 0
    with ThreadPoolExecutor(max_workers=args.proxy_workers) as pool:
        outcomes = pool.map(
            lambda k: probe_proxy(k[0], k[1], candidates[k], args.proxy_timeout), keys)
        for index, (key, outcome) in enumerate(zip(keys, outcomes), 1):
            name = f"{key[0]}:{key[1]}"
            record = status["proxies"].setdefault(name, {"firstSeen": stamp})
            record["checks"] = record.get("checks", 0) + 1
            record["lastChecked"] = stamp
            if outcome:
                protocol, latency = outcome
                record["protocol"] = protocol
                record["latencyMs"] = round(latency)
                record["successes"] = record.get("successes", 0) + 1
                record["streak"] = record.get("streak", 0) + 1
                record["fails"] = 0
                record["lastAlive"] = stamp
                working += 1
            else:
                record["streak"] = 0
                record["fails"] = record.get("fails", 0) + 1
            record["score"] = score_proxy(record)
            if index % 500 == 0 or index == len(keys):
                log(f"  [{index}/{len(keys)}] {working} reached GitHub")

    status["generatedAt"] = stamp
    return write_proxies(args, status, proved=working)


def write_proxies(args, status: dict | None = None, proved: int = 0) -> int:
    """
    Rewrites `proxies/all.txt` from what has already been measured.

    Separate from the probing so a change to the emit rules — the failure threshold, the
    deadline, the cap — can be applied to yesterday's measurements in a second, instead of
    costing a sixteen-minute re-probe to find out whether it was the right change.
    """
    status = status or load_proxy_status()
    stamp = status.get("generatedAt") or now_iso()

    retired = prune_stale(status["proxies"], alive_key="lastAlive", change_key=None,
                          max_days=args.max_stale_days)
    if retired:
        append_retired(PROXY_RETIRED, retired)
        log(f"retired {len(retired)} endpoints dead for {args.max_stale_days} days")

    # Emitted, not just today's winners: a proxy that flapped once today but worked
    # yesterday and the day before is still a better bet than an untested stranger.
    emitted = [(name, record) for name, record in status["proxies"].items()
               if record.get("successes", 0) > 0
               and record.get("fails", 0) < args.drop_after_failures
               and record.get("latencyMs", 0) <= args.proxy_timeout * 1000]

    countries: dict[str, str] = {}
    if args.geo and emitted:
        log(f"looking up countries for {len(emitted)} endpoints")
        countries = lookup_countries([name.rsplit(":", 1)[0] for name, _ in emitted])
        for name, record in emitted:
            code = countries.get(name.rsplit(":", 1)[0])
            if code:
                record["country"] = code

    # Sorted for a human reading the diff, never by latency: the app shuffles before
    # taking its 600, so any ranking here is discarded. Density is what matters, and
    # ordering cannot change it.
    def sort_key(item):
        name, record = item
        host = name.rsplit(":", 1)[0]
        try:
            packed = int(ipaddress.ip_address(host))
        except ValueError:
            packed = 0
        return (record.get("protocol", "zz"), record.get("country", "ZZ"), packed, name)

    emitted.sort(key=sort_key)

    if args.max_entries and len(emitted) > args.max_entries:
        log(f"capping at {args.max_entries} of {len(emitted)} — keeping the longest streaks")
        emitted.sort(key=lambda item: -item[1].get("streak", 0))
        emitted = emitted[: args.max_entries]
        emitted.sort(key=sort_key)

    if args.density and emitted:
        log(f"measuring density: {min(args.density, len(emitted))} drawn at random")
        hits, sampled = measure_density(emitted, args.density, args.proxy_workers)
        log(f"  {hits}/{sampled} reached GitHub on the second pass")
        measured_at = stamp
    else:
        # A re-emit measures nothing, so it reports the last real measurement and says
        # when that was, rather than dropping the only quality number the file has.
        previous = status.get("density", {})
        hits, sampled = previous.get("hits", 0), previous.get("sampled", 0)
        measured_at = previous.get("measuredAt", stamp)

    header = [
        "# Proxies that opened a TLS tunnel to raw.githubusercontent.com:443 and returned",
        f"# sixteen bytes of subs/all.txt, within {args.proxy_timeout:.0f} seconds. Nothing else qualifies.",
        "#",
        f"# Regenerated {stamp} · {len(emitted)} entries"
        + (f" · {proved} proved this run" if proved else ""),
    ]
    if sampled:
        header.append(f"# Density: {hits}/{sampled} of a random sample worked on re-check "
                      f"({hits / sampled:.0%}, measured {measured_at[:10]}) — the file's only "
                      f"real quality score.")
    header += [
        "#",
        "# Format: scheme://host:port | country | ms | days-alive",
        "# Everything after the first space or | is ignored by the client, so this is safe.",
        "#",
    ]

    lines = []
    for name, record in emitted:
        days = record.get("streak", 0)
        country = record.get("country", "??")
        latency = record.get("latencyMs", "?")
        lines.append(f"{record.get('protocol') or 'http'}://{name} | {country} | "
                     f"{latency}ms | {days}d")

    PROXY_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROXY_FILE.write_text("\n".join(header + [""] + lines) + "\n", encoding="utf-8")

    # Never let a re-emit, which measures nothing, overwrite a real measurement with zeros.
    if sampled:
        status["density"] = {"hits": hits, "sampled": sampled, "measuredAt": measured_at}
    save_proxy_status(status)
    write_proxy_report(status, emitted, proved, (hits, sampled))
    size_kb = PROXY_FILE.stat().st_size / 1024
    log(f"proxies/all.txt: {len(emitted)} entries, {size_kb:.0f} KB")
    if size_kb > 1024:
        log("  WARNING: over 1 MB — this file is downloaded on a phone before the VPN is up")
    return len(emitted)


def write_proxy_report(status: dict, emitted: list, proved: int,
                       density: tuple[int, int]) -> None:
    hits, sampled = density
    by_protocol = Counter(record.get("protocol", "?") for _, record in emitted)
    by_country = Counter(record.get("country", "??") for _, record in emitted)

    lines = [
        "# Proxy status",
        "",
        f"Generated {status.get('generatedAt', '—')} by `harvest.py`.",
        "",
        (f"- **{proved}** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run"
         if proved else "- re-emitted from stored measurements; nothing was probed this run"),
        f"- **{len(emitted)}** entries in `all.txt` (a proxy is kept until it fails "
        f"{PROXY_FAILURES_BEFORE_DROP} runs running)",
        f"- **{len(status.get('proxies', {}))}** endpoints on record",
        f"- retirement age: **{MAX_STALE_DAYS} days** with no successful request",
    ]
    if sampled:
        lines.append(f"- **density: {hits}/{sampled} ({hits / sampled:.0%})** — of a random "
                     f"sample of the shipped file, how many worked on a second pass")
    lines += [
        "",
        "The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206",
        "or 200, non-empty body, all inside eight seconds. A proxy that answers a generic",
        "liveness check but refuses `CONNECT` — the commonest false positive there is —",
        "fails here, which is the point.",
        "",
        "Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,",
        "so ranking is discarded; what matters is the share of the file that works, and the",
        "order is chosen to make the daily diff readable instead.",
        "",
        "| protocol | entries |",
        "|---|---|",
    ]
    for protocol, count in by_protocol.most_common():
        lines.append(f"| {protocol} | {count} |")

    if any(code != "??" for code in by_country):
        lines += ["", "| country | entries |", "|---|---|"]
        for code, count in by_country.most_common(25):
            lines.append(f"| {code} | {count} |")

    health = status.get("sources", {})
    if health:
        lines += [
            "",
            "## Sources",
            "",
            "A source that has moved returns 404 and yields nothing, which in a log looks",
            "exactly like a quiet day. Anything reading **0 usable** here is worth replacing.",
            "",
            "| source | http | lines | usable | new this run | last yielded |",
            "|---|---|---|---|---|---|",
        ]
        for url, record in sorted(health.items(), key=lambda kv: kv[1].get("usable", 0)):
            lines.append(
                f"| {url} | {record.get('httpStatus', 0)} | {record.get('lines', 0)} | "
                f"{record.get('usable', 0)} | {record.get('new', 0)} | "
                f"{(record.get('lastYielded', '') or '—')[:10]} |")

    lines += [
        "",
        "## Longest-running entries",
        "",
        "Consecutive successful runs is the only signal here that predicts tomorrow.",
        "",
        "| proxy | country | ms | streak | successes/checks |",
        "|---|---|---|---|---|",
    ]
    for name, record in sorted(emitted, key=lambda kv: -kv[1].get("streak", 0))[:100]:
        lines.append(
            f"| {record.get('protocol', '?')}://{name} | {record.get('country', '??')} | "
            f"{record.get('latencyMs', '—')} | {record.get('streak', 0)} | "
            f"{record.get('successes', 0)}/{max(1, record.get('checks', 1))} |")

    PROXY_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


# =============================================================================== cli


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--workers", type=int, default=16, help="concurrent HTTP fetches")
    parser.add_argument("--timeout", type=int, default=25, help="seconds per fetch")
    parser.add_argument("--probe-bytes", type=int, default=PROBE_BYTES,
                        help=f"bytes read from each candidate (default {PROBE_BYTES})")
    parser.add_argument("--max-stale-days", type=int, default=MAX_STALE_DAYS,
                        help=f"retirement age in days (default {MAX_STALE_DAYS})")
    parser.add_argument("--limit", type=int, default=0, help="stop after N items (testing)")


def add_collect_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--refresh", action="store_true", help="ignore the README cache")
    parser.add_argument("--no-guess", action="store_true", help="skip common-path guessing")
    parser.add_argument("--tree", action="store_true",
                        help="list files via the API when a README gives nothing")
    parser.add_argument("--tree-budget", type=int, default=50,
                        help="API calls the tree scan may spend")


def add_prove_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--only-new", action="store_true", help="skip links already on record")
    parser.add_argument("--no-recurse", action="store_true", help="do not follow catalogs")
    parser.add_argument("--samples", type=int, default=12,
                        help="servers dialled per subscription (default 12)")
    parser.add_argument("--probe-workers", type=int, default=64, help="concurrent TCP probes")
    parser.add_argument("--tcp-timeout", type=float, default=3.0, help="seconds per TCP probe")


def add_write_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--min-configs", type=int, default=5,
                        help="ignore links carrying fewer configs (default 5)")


def add_search_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--query", action="append", help="repeatable; replaces the defaults")
    parser.add_argument("--pages", type=int, default=2, help="pages of 100 per query")


def add_proxy_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--proxy-workers", type=int, default=200, help="concurrent proxy probes")
    parser.add_argument("--proxy-timeout", type=float, default=PROXY_DEADLINE,
                        help="hard deadline per proxy, in seconds — the app's own budget")
    parser.add_argument("--drop-after-failures", type=int, default=PROXY_FAILURES_BEFORE_DROP,
                        help="consecutive failures before an entry leaves all.txt")
    parser.add_argument("--max-entries", type=int, default=6000,
                        help="cap on all.txt; the file is downloaded before the VPN is up")
    parser.add_argument("--density", type=int, default=600,
                        help="re-check this many at random and report the hit rate (0 to skip)")
    parser.add_argument("--max-candidates", type=int, default=40000,
                        help="probe budget: endpoints with history first, then a random sample")
    parser.add_argument("--geo", action="store_true",
                        help="annotate entries with a country code via ip-api.com")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Maintain subs/all.txt and proxies/all.txt.",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    top = parser.add_subparsers(dest="area", required=True)

    subs = top.add_parser("subs", help="the subscription catalog").add_subparsers(
        dest="command", required=True)

    p = subs.add_parser("search", help="find new repositories on GitHub")
    add_common(p)
    add_search_flags(p)
    p = subs.add_parser("collect", help="read every repository, collect candidates")
    add_common(p)
    add_collect_flags(p)
    p = subs.add_parser("prove", help="fetch each candidate and measure its servers")
    add_common(p)
    add_prove_flags(p)
    p = subs.add_parser("write", help="rank, retire and rewrite subs/all.txt")
    add_common(p)
    add_write_flags(p)
    p = subs.add_parser("run", help="collect, prove and write")
    for add in (add_common, add_collect_flags, add_prove_flags, add_write_flags, add_search_flags):
        add(p)
    p.add_argument("--search", action="store_true", help="look for new repositories first")
    subs.add_parser("status", help="print the current standings")

    proxies = top.add_parser("proxies", help="the proxy list").add_subparsers(
        dest="command", required=True)
    p = proxies.add_parser("run", help="collect, prove and rewrite proxies/all.txt")
    add_common(p)
    add_proxy_flags(p)
    p = proxies.add_parser("write", help="rewrite proxies/all.txt from what was already measured")
    add_common(p)
    add_proxy_flags(p)

    p = top.add_parser("daily", help="everything, which is what CI runs")
    for add in (add_common, add_collect_flags, add_prove_flags, add_write_flags,
                add_search_flags, add_proxy_flags):
        add(p)
    p.add_argument("--skip-proxies", action="store_true")
    p.add_argument("--skip-subs", action="store_true")
    p.add_argument("--skip-search", action="store_true")

    args = parser.parse_args(argv)
    started = time.time()

    if args.area == "subs":
        if args.command == "search":
            stage_search(args)
        elif args.command == "collect":
            stage_collect(args)
        elif args.command == "prove":
            stage_prove(args)
        elif args.command == "write":
            stage_write_subs(args)
        elif args.command == "status":
            status = load_subs_status()
            alive = [(u, r) for u, r in status["links"].items() if r.get("kind") == "configs"]
            alive.sort(key=lambda kv: -kv[1].get("score", 0))
            log(f"{len(alive)} live of {len(status['links'])} known, "
                f"generated {status.get('generatedAt', '—')}\n")
            for index, (url, record) in enumerate(alive[:30], 1):
                log(f"{index:3}. {record.get('score', 0):5.1f}  "
                    f"{record.get('configs', 0):5} cfg  "
                    f"{record.get('reachRatio', 0):4.0%} reach  {url}")
        elif args.command == "run":
            if getattr(args, "search", False):
                stage_search(args)
            origin = stage_collect(args)
            stage_write_subs(args, stage_prove(args, origin=origin))

    elif args.area == "proxies":
        if args.command == "write":
            args.density = 0        # nothing was probed, so there is nothing to re-check
            write_proxies(args)
        else:
            stage_proxies(args)

    elif args.area == "daily":
        if not args.skip_subs:
            if not args.skip_search:
                stage_search(args)
            origin = stage_collect(args)
            stage_write_subs(args, stage_prove(args, origin=origin))
        if not args.skip_proxies:
            log("\n" + "=" * 70 + "\nproxies\n" + "=" * 70)
            stage_proxies(args)

    log(f"\ndone in {time.time() - started:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
