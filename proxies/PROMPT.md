# Brief: maintaining `proxies/all.txt`

You are building the daily job that regenerates `proxies/all.txt` in this repository.
This document is the contract. It is written by the author of the *consumer* — the code in
v2rayV that reads this file — so the numbers and parsing rules below are taken from that
implementation rather than guessed at.

Read the job description first, because it is narrower than "collect working proxies" and
optimising for the wrong thing is the main way this fails.

---

## 1. What this file is actually for

v2rayV is an Android VPN client. On a normal network it fetches its subscription lists
straight from `raw.githubusercontent.com`. On a censored network — Iran is the case that
motivated all of this — that host is unreachable, and a run that cannot download a list
produces nothing at all.

So the app falls back to this file. It downloads it, shuffles it, and races entries until
**one** of them can fetch sixteen bytes of a file from GitHub. Then it stops and does the
rest of its work through that one.

Three consequences, and they are the whole brief:

- **One success is a total success.** The file does not need a high hit rate. It needs a
  hit rate that is not *near zero* when 600 entries are tried. Optimise for "at least a
  few of any random 600 work", not for "most entries work".
- **"Working proxy" is the wrong test.** The only property that counts is: *can this proxy
  open a TLS tunnel to `raw.githubusercontent.com:443` and return data, from outside Iran,
  in under eight seconds*. A proxy can be perfectly alive, answer any generic check, and
  still be useless here because it refuses `CONNECT`, restricts it to a whitelist, or sits
  somewhere that itself cannot reach GitHub.
- **Latency and bandwidth barely matter.** The payload is a few hundred kilobytes of text,
  once. A 900 ms proxy that works is worth more than a 40 ms one that does not.

---

## 2. The consumer's contract

These are facts about the code that reads this file, not preferences. Violating them
silently loses entries.

### 2.1 The parser

Implemented in `AutoModeProxy.parse`. One entry per line. Accepted forms:

```
socks5://1.2.3.4:1080
http://user:pass@1.2.3.4:8080
1.2.3.4:4145
1.2.3.4:8080:user:pass
```

Recognised schemes, everything else is **rejected outright**:

| written | understood as |
|---|---|
| `http`, `https` | HTTP `CONNECT` |
| `socks5`, `socks5h`, `socks` | SOCKS5 |
| `socks4`, `socks4a` | SOCKS4a |

Rules that drop a line:

- Blank, or starting with `#` or `//`. **Comments are safe** — use them for a header.
- No port, a port outside `1–65535`, or a port that is not a number.
- A host containing anything other than letters, digits, `.` and `-`.
  **This rejects every IPv6 address.** Do not emit them; they are silently discarded.
- An unrecognised scheme.

Two behaviours that are useful rather than restrictive:

- Everything after the first `/`, `|`, or space in the authority is **discarded before
  parsing**. This means you may append whatever metadata you like and the app will ignore
  it. `socks5://1.2.3.4:1080 | DE | 2026-08-11 | 412ms` parses exactly as
  `socks5://1.2.3.4:1080`. Use this — a file a human can audit costs nothing.
- Deduplication is by `host:port`, and **the first occurrence wins**. If the same endpoint
  appears twice, the later line — including its scheme — is thrown away. Never emit an
  endpoint twice; if you must, put the scheme-bearing line first.

### 2.2 Declaring the scheme is the single biggest lever you have

When a line declares its protocol, the app performs **one** handshake. When it does not,
it guesses from the port and may perform **three**, each with a six-second connect and a
six-second handshake timeout.

A bare `1.2.3.4:9999` on an unconventional port can therefore burn ~36 seconds of one of
only 24 concurrent slots, to discover nothing. The same entry written as
`socks5://1.2.3.4:9999` costs at most 12.

**Always write the scheme.** If your validator learned the protocol — and it must, to
validate at all — then write it down. Emitting bare `host:port` throws away the most
valuable thing you know.

For reference, the port heuristic used when you do not (it is a fallback, not a plan):

- SOCKS5 first: `1080 1081 1085 1088 1090 10808 10809 9050 9150 7890 7891`
- SOCKS4 first: `4145 5678 9091`
- HTTP first: `80 81 800 801 808 999 3128 3129 8000 8008 8080 8081 8085 8086 8090 8118 8123 8888 8889 9000 9080`
- anything else: SOCKS5, then HTTP, then SOCKS4

### 2.3 Protocol requirements the app imposes

The app never resolves the destination locally — on a network that answers DNS with a lie,
handing a proxy an IP defeats the point. The destination always travels **by name**. This
means:

- **SOCKS5** must accept address type `0x03` (domain name). Username/password
  (RFC 1929) is supported if the entry carries credentials; otherwise `no-auth` is offered.
- **SOCKS4** must speak **SOCKS4a** — the hostname extension, signalled with destination
  IP `0.0.0.1`. A plain SOCKS4 server that cannot do this will reject the request and the
  entry is dead as far as this app is concerned. Validate for 4a specifically, not 4.
- **HTTP** must allow `CONNECT` to port 443. Many public HTTP proxies allow only plain
  `GET`, or restrict `CONNECT` to a whitelist. These are the most common false positives
  in a naive checker and there are a lot of them.

### 2.4 Budgets

Everything the app does with this file, in numbers:

| | value |
|---|---|
| Entries tried per run | 600, drawn at random from the whole file |
| Concurrent probes | 24, in waves of 48 |
| TCP connect timeout | 6 s |
| Handshake timeout | 6 s |
| Probe read timeout | 8 s |
| Probe request | `Range: bytes=0-15` on the subscription URL |
| Accepted result | HTTP 206 or 200, with a non-empty body |
| A winner is remembered for | 6 hours, then re-probed |

**Validate with the same budget.** An entry that needs 20 seconds is not a slow success,
it is a failure — the app will have abandoned it.

### 2.5 Ordering does not matter

The app shuffles before taking its 600. Do not spend effort sorting by quality; it is
discarded. Sort for human readability instead (by country, by protocol — whatever makes
the diff reviewable).

What *does* matter is the **density of working entries**, because the sample is random.
Two thousand entries at 1% beats twenty thousand at 0.05%.

### 2.6 Size

The file is downloaded whole, on a phone, often on a bad connection, before the VPN is up.
It is currently ~65 KB. **Keep it under about 1 MB.** If quality forces a choice between
more entries and fewer better ones, choose fewer better ones — see the density point above.

A copy of this file is also compiled into the APK as a cold-start fallback, so its size is
paid by every install.

---

## 3. What "validated" has to mean

Do not accept an entry into `all.txt` on the strength of a TCP connect, a handshake, or a
fetch of `example.com`. The check must be the real one, end to end:

1. Open a TCP socket to the proxy.
2. Perform the protocol handshake, addressing **`raw.githubusercontent.com` by name**, port 443.
3. Complete a TLS handshake through the tunnel with that hostname as SNI.
4. Send `GET /morpheusadam/v2ray-config/main/subs/all.txt HTTP/1.1` with
   `Range: bytes=0-15` and `Host: raw.githubusercontent.com`.
5. Require HTTP 206 or 200 and a non-empty body.
6. The whole thing inside 8 seconds.

Anything less and you will ship a file full of entries that pass your check and fail the
app's. That has a specific smell in production: the app reports "no working proxy among
600 tried" while your dashboard says 40% healthy.

**Also verify from a vantage point that resembles the user's**, or at least understand that
you cannot. A checker running in a European datacentre proves the proxy is reachable *from
there*. The user is in Iran. Reachability from Iran to the proxy is the leg you cannot
easily test and should be conservative about — prefer proxies in places Iranian networks
generally reach (Turkey, Germany, the Netherlands, France, the Gulf) over ones behind
national firewalls of their own.

---

## 4. Suggested shape of the job

Daily, since public proxies decay in hours to days and the app re-probes every 6 hours.

```
collect   →  dedupe  →  cheap filter  →  real validation  →  emit
```

**Collect.** Public proxy lists on GitHub, the usual aggregators, and — worth more than
any of them — the entries that worked yesterday. Keep a persistent record keyed by
`host:port`; an endpoint that has worked three days running is worth re-checking before
any stranger.

**Dedupe** by `host:port` before validating, or you pay for the same endpoint repeatedly.

**Cheap filter** before the expensive check: drop IPv6, drop private and reserved ranges
(`10/8`, `172.16/12`, `192.168/16`, `127/8`, `169.254/16`, `100.64/10`), drop hosts that
do not parse under the rules in §2.1. This costs nothing and removes a surprising fraction.

**Validate** as in §3, with high concurrency — this is I/O-bound and a few hundred workers
is reasonable — and a hard per-entry deadline. Record the protocol that succeeded.

**Emit** with the scheme written, one per line, plus a comment header. Something like:

```
# Proxies that reached raw.githubusercontent.com:443 within 8s.
# Regenerated 2026-08-11T03:00Z · 2,143 entries · checked from 3 vantage points
# Format: scheme://host:port | country | ms | days-alive
# Anything after the first space or | is ignored by the client.

socks5://1.2.3.4:1080 | DE | 412ms | 12d
http://5.6.7.8:3128 | NL | 780ms | 3d
```

---

## 5. Things that will look like improvements and are not

- **Sorting by latency.** The app shuffles. Wasted work. (And in the sibling problem of
  ranking *servers*, sorting by ping measured *worse than random* — the fastest responders
  were CDN edges fronting dead hosts. Be suspicious of latency as a proxy for quality.)
- **Adding tens of thousands of unvalidated entries.** This lowers density, which is the
  one number that matters, and inflates a file that is downloaded before the VPN is up.
- **Emitting IPv6, or `[::1]:1080` style entries.** Silently dropped by the parser.
- **Removing entries the moment they fail once.** Public proxies flap. Keep a history and
  require two or three consecutive failures before dropping, the same way the app itself
  waits five dead runs before disabling a subscription source.
- **Authenticated proxies from public lists.** Credentials in a public list are either
  fake or about to be rotated. Support the syntax, do not go looking for them.

---

## 6. How to tell whether it is working

The metric that matters is not "entries in the file" and not "percent healthy at generation
time". It is:

> Of 600 entries drawn at random, how many can fetch from GitHub *right now*?

Measure it the way the app does: sample 600 at random from the shipped file, run the §3
check, count successes. Track that number over time. If it stays comfortably above ~10,
the app will find a route on its first wave and the user waits a second. If it approaches
1–2, users on censored networks start seeing "no working proxy" and everything downstream
of it stops.

Report that number in the header comment. It is the file's only real quality score.
