# standard.md — what the files in this repository have to look like

This repository is not documentation. It is read at runtime by every installed copy of
v2rayV, over `raw.githubusercontent.com` and its CDN mirrors, on networks that are actively
trying to block it. A line that does not parse is not a typo — it is a six-second timeout on
someone's phone, or a source that silently never contributes anything.

**Nothing here is maintained by hand any more.** `harvest.py` rebuilds both lists once a
day inside GitHub Actions and commits the result. Editing `subs/all.txt` or
`proxies/all.txt` directly works until the next run overwrites it; the way to change what
they contain is to change the inputs or the rules below.

| File | What it is | Who writes it |
|---|---|---|
| `subs/all.txt` | Links to *other people's* subscription lists, best first | `harvest.py`, daily |
| `proxies/all.txt` | Proxies that can reach GitHub when GitHub is blocked | `harvest.py`, daily |
| `app/notice.json` | The one message slot on the dashboard | a human, rarely |
| `rapo.txt` | Repositories to mine for subscription links | `harvest.py search`, and by hand |
| `proxies/sources.txt` | Proxy lists to mine | by hand |
| `proxies/PROMPT.md` | The consumer's contract for the proxy file | the author of the consumer |
| `subs/status.json`, `proxies/status.json` | Every link's history: when it was last alive, last changed, how it scored | `harvest.py` |
| `subs/STATUS.md`, `proxies/STATUS.md` | The same thing, readable, with dates | `harvest.py` |
| `subs/retired.txt`, `proxies/retired.txt` | What left the lists, when, and why | `harvest.py` |

The rules below are not conventions. They are what the parsers in
`V2rayNG/app/src/main/java/com/v2ray/ang/automode/` actually accept, and nothing here should
change without changing those.

---

## 1. `subs/all.txt` — the catalog

**One subscription link per line.** These are links to lists of servers, never servers
themselves. The distinction matters: the import stage deliberately strips bare subscription
URLs out of any body it fetches, so a `vless://` URI in this file is dropped, and a file of
nothing but server URIs would be detected as "not a catalog after all" and added as a
single ordinary source instead.

### What a line must satisfy

Extraction is `Regex("https?://[^\\s,;'\"]+")` over the whole file, so a URL is found even
when it shares a line with a label. Each match then has to survive `normalizeUrl`:

- **Scheme is `http://` or `https://`.** Anything else is dropped. Prefer `https`.
- **Trailing `.`, `,`, `;`, `)`, `]` are trimmed** before anything else.
- **No `<` or `>` anywhere, and no `YOUR_USERNAME` / `YOUR_REPOSITORY`.** Template rows such
  as `.../countries/<CODE>.sub.txt` are rejected whole, on purpose — truncating them at the
  bracket would leave a valid-looking but useless directory URL.
- **`github.com/.../blob/...` is rewritten to the raw host automatically.** `harvest.py`
  does the rewrite itself and stores the raw form.
- **It must parse as a URI with a non-empty host.** This is weaker than it looks — a
  concatenation accident such as `https://githuhttps://github.com/...` gets this far.

### What earns a place in the file

A link is written only after it has been fetched and shown to carry at least
`--min-configs` (default 5) config URIs, counted in the first 64 KB. Base64 bodies are
decoded before counting. Clash YAML, HTML error pages and READMEs are recognised and left
out.

### The order is a measurement, and it matters

Entries are sorted by a score in 0–100:

```
0.34·reach + 0.20·freshness + 0.14·clean + 0.12·speed + 0.12·volume + 0.08·modern
```

- **reach** — the share of a random sample of its servers that completed a TCP handshake.
- **freshness** — days since the file's *decoded* contents last changed. Re-encoding the
  same servers daily does not count as a change.
- **clean** — half how little the list repeats itself, half how little it repeats everyone
  else. A list handing out the same servers as twenty other lists scores badly.
- **speed** — median handshake time, 1.0 at 60 ms, 0 at 2 s. **Deliberately a small
  weight.** Ranking servers by ping has measured *worse than random* on this project: the
  fastest responders were CDN edges fronting dead hosts. It is a tiebreak, not the ranking.
- **volume** — configs carried, saturating at 300.
- **modern** — reality, TLS, hysteria2, TUIC over bare VMess.

Order is not cosmetic here. `AutoModeSourceManager.selectSources` gives the first two
never-tried links a guaranteed slot every run, so the top of this file is what a fresh
install tries first.

### Retirement at 12 days

**A link leaves this file when it has gone 12 days without carrying configs, or 12 days
without its contents changing.** A newly discovered link is immune until it has been
watched that long — "unchanged for twelve days" is a claim about observation, and on day
one there is none.

This overrides the older rule that nothing was ever removed. It is a deliberate trade: the
app's own health record (five dead runs, then auto-disable, then a resurrection probe every
fifth run) still protects against a link being dropped for one bad day, and everything
removed is written to `subs/retired.txt` with its date and reason, so a source that comes
back is recognised rather than rediscovered as a stranger.

---

## 2. `proxies/all.txt` — the way out

Governed by [`proxies/PROMPT.md`](proxies/PROMPT.md), written by the author of the code
that reads it. That document wins over this one wherever they disagree. The short version:

### What the file is for

The app downloads it, shuffles it, and races entries until **one** can fetch sixteen bytes
from GitHub. One success is a total success. What matters is not the count of entries but
the **density** — of 600 drawn at random, how many work right now. That number is measured
on every run and written into the file's header.

### What "validated" means

Not a TCP connect. Not a generic liveness check. The entry must open a TLS tunnel to
`raw.githubusercontent.com:443` **addressed by name**, send `Range: bytes=0-15`, and get
back 206 or 200 with a non-empty body, all inside eight seconds. Consequences:

- **SOCKS5** must accept address type `0x03` (domain name).
- **SOCKS4** must be **SOCKS4a** — a plain SOCKS4 server cannot carry a hostname and is
  useless here.
- **HTTP** must allow `CONNECT` to 443. Proxies that allow only `GET` are the commonest
  false positive in a naive checker, and there are a lot of them.

### Format

```
scheme://host:port | country | ms | days-alive
```

Everything after the first `/`, `|` or space is discarded by the parser, so the metadata is
free. The scheme is **always** written: a labelled entry costs the app one handshake, a bare
`host:port` costs up to three, at six seconds each.

- Recognised schemes: `http`, `https`, `socks4`, `socks4a`, `socks5`, `socks5h`, `socks`.
- Host may contain only letters, digits, `.` and `-`. **IPv6 is silently dropped by the
  parser**, so it is never emitted. Private, loopback, reserved and CGNAT ranges are
  filtered before any probe.
- Deduplicated by `host:port`, first occurrence wins.

### Order does not matter, and is not a ranking

The app shuffles before taking its 600, so sorting by latency is wasted work. Entries are
grouped by protocol and country and then by address, to make the daily diff readable.

### Retirement

An entry leaves after **3 consecutive failed runs** — public proxies flap, and one bad
check is not evidence. Its record is kept for 12 days after that in case it returns.

### Size

Under 1 MB, and the run warns if it is not. A copy ships inside the APK, so its size is paid
by every install, and it is downloaded on a phone before the VPN is up. If quality forces a
choice between more entries and fewer better ones, **fewer better ones** — density is the
only number that matters.

---

## 3. `app/notice.json`

Documented separately and completely in [app/README.md](app/README.md). Its normal state is
`"notice": null`, it is polled every six hours, and `maxVersionCode` is the field that
decides whether an update card follows people onto the version it told them to install.

`harvest.py` never touches it.

---

## 4. The daily job

`.github/workflows/daily.yml` runs at 03:20 UTC and commits whatever changed:

```
python harvest.py daily --refresh --tree --pages 3 --max-stale-days 12
```

Stages, in order: search GitHub for repositories nobody has listed yet → read every
repository in `rapo.txt` and collect candidate links → fetch each candidate and measure the
servers inside it → rank, retire, rewrite `subs/all.txt` → then the whole proxy pass.

Each stage runs on its own too, which is how to debug one:

```
python harvest.py subs search       # find new repositories
python harvest.py subs collect      # gather candidate links
python harvest.py subs prove        # fetch and measure
python harvest.py subs write        # rank, retire, rewrite
python harvest.py subs status       # print the standings
python harvest.py proxies run       # collect, prove, rewrite
python harvest.py proxies write     # rewrite from yesterday's measurements, no probing
```

`subs write` and `proxies write` re-derive their file from `status.json` without touching
the network, so a changed weight or threshold can be tried in a second instead of costing
a full re-probe to find out whether it was the right change.

`GITHUB_TOKEN` is optional and only raises API rate limits — Actions supplies one. Without
it, search falls back to ten requests a minute and the tree scan to sixty an hour, and both
degrade to "did fewer" rather than failing.

---

## 5. The bundled snapshots

`subs/all.txt` and `proxies/all.txt` also ship inside the APK, as

```
V2rayNG/app/src/main/assets/automode_subs.txt
V2rayNG/app/src/main/assets/automode_proxies.txt
```

They break a circular bootstrap — the proxy list needed to reach a blocked host lives on
that blocked host — and they are the only rung of the route ladder that cannot fail.

**Refresh both at every release.** They are copies taken by hand, they go stale between
releases, and a stale snapshot is the difference between a first run working and not
working on a blocked network. Fresh network data is merged *ahead* of the bundled copy
rather than replacing it, so staleness degrades gracefully — but only if there was a route
to the network at all, which is precisely the case they exist to cover.

---

## 6. Before committing by hand

Rarely necessary now, but when it is:

1. New rows in `rapo.txt` are `https://github.com/owner/repo`, one per line, nothing else.
2. New rows in `proxies/sources.txt` return `host:port` lines. Anything else is ignored
   silently, which looks the same as a source that went dead.
3. `subs/all.txt` and `proxies/all.txt` are outputs — change the inputs instead.
4. The two `assets/automode_*.txt` copies match, if a release is going out.
5. `app/notice.json` is `null` unless there is something genuinely worth a person's
   attention — the slot lives inside a VPN app on someone's phone and spends goodwill every
   time it is used.
