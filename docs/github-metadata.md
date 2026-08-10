# Repository description and topics

The README is what convinces someone who already landed here. **The description and topics
are what decides whether they land at all** — GitHub's own search weights them heavily, and
Google shows the description as the result snippet. Neither is in the repository, so neither
can be set by a commit: paste them in at *Settings → General* and via the ⚙ next to *About*
on the front page.

Topics: lowercase, hyphens, max 20 per repo, 35 characters each.

---

## morpheusadam/v2ray-config

**Description** (349 characters, under GitHub's 350 limit — leads with what people search
for, then the one claim nobody else makes):

```
Free V2Ray subscription links, rebuilt from measurement every day. VLESS, VMess, Trojan, Shadowsocks, Hysteria2, TUIC and Reality configs, plus a proxy list proved to reach GitHub from blocked networks. Every link is fetched, decoded and dialled before it is published; anything that stops changing for 12 days is retired. No signup, no tracking.
```

**Website field:** `https://raw.githubusercontent.com/morpheusadam/v2ray-config/main/subs/all.txt`

Pointing it at the subscription itself means the front page carries a one-click copy target
above the fold, which is what most visitors came for.

**Topics** (20):

```
v2ray
v2ray-config
v2ray-subscription
free-vpn
vless
vmess
trojan
shadowsocks
hysteria2
reality
xray
sing-box
subscription-link
proxy-list
socks5
free-proxy
v2rayng
clash
censorship-circumvention
iran
```

---

## morpheusadam/v2rayV

**Description:**

```
Android V2Ray/Xray client that connects itself. One press measures your line, tests servers against it, and connects on the first one fast enough for you — no picking from a list of dead servers. VLESS, Reality, VMess, Trojan, Shadowsocks, Hysteria2, TUIC. Fork of v2rayNG with Auto Mode, a censorship route ladder and a live dashboard.
```

**Website field:** `https://github.com/morpheusadam/v2ray-config`

**Topics** (20):

```
v2ray
v2rayng
android
vpn
vpn-client
xray
vless
reality
vmess
trojan
shadowsocks
hysteria2
tuic
sing-box
kotlin
android-vpn
free-vpn
censorship-circumvention
anti-dpi
auto-connect
```

---

## morpheusadam/v2rayN-Pro-Max

**Description:**

```
V2Ray/Xray client for Windows and Linux that tests and picks servers for you. One press reads your subscription links, drops what is dead, measures real throughput on what survives, and leaves the fastest servers ready to use. Xray, sing-box and mihomo cores. Fork of v2rayN with Auto Mode.
```

**Website field:** `https://github.com/morpheusadam/v2ray-config`

**Topics** (20):

```
v2ray
v2rayn
xray
windows
linux
vpn-client
vless
reality
vmess
trojan
shadowsocks
hysteria2
sing-box
mihomo
clash
free-vpn
subscription
speed-test
censorship-circumvention
dotnet
```

---

## The rest of the checklist

Things that move a repository in search and cost nothing:

- **Pin all three** to the profile, so each one lends the others credibility.
- **Link them to each other** in every README. They already do — that internal linking is
  what makes three small repositories read as one project.
- **Cut a tagged release.** GitHub ranks repositories with releases above those without, and
  a release page is a second thing for Google to index. `v2rayV` has none yet.
- **Set the social preview image** (Settings → Social preview). Without one, every share on
  Telegram, X or Discord renders as grey text; `docs/banner.svg` exported to PNG at
  1280×640 is exactly the right shape.
- **Enable Discussions** if you want the long-tail questions ("how do I import this into
  NekoBox") to become indexable pages instead of closed issues.
- **The alt text on every image is already written** for search rather than for decoration.
  Keep it that way when adding screenshots.
- **Do not stuff keywords into commit messages or file names.** GitHub search ignores them
  and it makes the repository look like spam to the people you want.
