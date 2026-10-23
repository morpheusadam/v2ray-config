# Proxy status

Generated 2026-10-23T22:37:18Z by `harvest.py`.

- **3095** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5396** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39844** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 205/600 (34%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2741 |
| socks5 | 2645 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 2428 |
| ID | 854 |
| PH | 154 |
| CO | 148 |
| MX | 135 |
| US | 129 |
| RU | 109 |
| VE | 88 |
| BD | 78 |
| CN | 72 |
| TR | 69 |
| BR | 67 |
| IN | 67 |
| TH | 67 |
| VN | 65 |
| EC | 63 |
| AR | 52 |
| DO | 50 |
| PK | 44 |
| SG | 44 |
| PE | 37 |
| EG | 36 |
| DE | 33 |
| SY | 30 |
| ZA | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-10-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 68 | 68 | 8 | 2026-10-23 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 68 | 2026-10-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-10-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 157 | 157 | 86 | 2026-10-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 239 | 239 | 81 | 2026-10-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-23 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 593 | 593 | 37 | 2026-10-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 596 | 596 | 217 | 2026-10-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 636 | 636 | 401 | 2026-10-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1150 | 2026-10-23 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1733 | 1729 | 372 | 2026-10-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-10-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1953 | 1951 | 740 | 2026-10-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2337 | 2335 | 824 | 2026-10-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2377 | 2375 | 1593 | 2026-10-23 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 76976 | 76976 | 63619 | 2026-10-23 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 84278 | 84277 | 2610 | 2026-10-23 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 937 | 68 | 135/148 |
| http://149.130.173.58:9443 | CO | 512 | 59 | 59/59 |
| http://190.0.246.213:4040 | CO | 746 | 42 | 105/113 |
| http://197.224.185.3:3128 | MU | 2045 | 40 | 109/116 |
| http://103.237.102.191:11111 | DE | 1083 | 35 | 141/148 |
| http://203.252.142.217:80 | KR | 1379 | 30 | 30/30 |
| http://45.186.6.104:3128 | EC | 2782 | 29 | 119/126 |
| http://103.133.26.72:8080 | ID | 1770 | 24 | 29/74 |
| http://103.133.26.73:3128 | ID | 1446 | 24 | 44/126 |
| http://103.133.26.119:8080 | ID | 1757 | 24 | 28/58 |
| http://176.111.37.5:39811 | HK | 1892 | 19 | 129/148 |
| http://34.43.46.91:80 | US | 1379 | 18 | 142/148 |
| socks5://43.245.199.34:1080 | HK | 1733 | 17 | 17/17 |
| http://4.144.146.21:80 | SG | 1364 | 16 | 33/40 |
| http://190.0.246.210:4040 | CO | 1380 | 15 | 134/147 |
| http://43.155.62.157:443 | HK | 1003 | 15 | 43/51 |
| http://102.244.78.61:8081 | CM | 1470 | 14 | 27/34 |
| http://186.5.94.206:999 | EC | 2145 | 13 | 101/110 |
| http://49.156.44.115:8080 | KH | 5502 | 13 | 44/114 |
| http://205.164.192.115:999 | MX | 5579 | 13 | 98/146 |
| socks5://103.100.158.115:10809 | JP | 964 | 13 | 28/36 |
| http://184.75.221.82:3118 | CA | 276 | 12 | 99/113 |
| http://189.51.168.165:999 | MX | 494 | 12 | 55/60 |
| http://130.110.103.245:3128 | SA | 1647 | 12 | 132/148 |
| http://176.111.37.216:39811 | HK | 1608 | 11 | 120/148 |
| http://34.88.38.81:9443 | FI | 964 | 10 | 79/113 |
| http://35.228.49.168:9443 | FI | 827 | 10 | 60/85 |
| http://103.130.61.61:8081 | ID | 3607 | 10 | 118/148 |
| http://177.234.217.88:999 | EC | 5839 | 9 | 60/140 |
| http://205.237.105.49:3129 | FR | 1687 | 9 | 18/19 |
| socks5://51.15.20.32:1088 | NL | 983 | 9 | 11/12 |
| http://185.191.239.248:3128 | CH | 1387 | 8 | 104/147 |
| http://103.133.26.50:8080 | ID | 1716 | 8 | 27/49 |
| http://186.96.111.214:999 | CO | 1763 | 7 | 63/137 |
| http://45.125.64.215:443 | HK | 1499 | 7 | 17/18 |
| http://34.43.46.91:443 | US | 1357 | 7 | 138/148 |
| http://165.154.162.73:8888 | US | 7090 | 7 | 97/148 |
| http://38.172.160.16:999 | VE | 6575 | 7 | 57/99 |
| socks5://101.36.104.239:10808 | JP | 1373 | 7 | 125/148 |
| socks5://143.198.90.221:1088 | SG | 2333 | 7 | 14/16 |
| http://81.19.210.10:80 | GB | 774 | 6 | 8/9 |
| http://45.43.60.220:8080 | JP | 3482 | 6 | 78/147 |
| http://152.42.177.32:8888 | SG | 1064 | 6 | 69/108 |
| http://103.22.181.107:3128 | TH | 1996 | 6 | 6/6 |
| http://195.142.250.34:8080 | TR | 3026 | 6 | 6/6 |
| http://144.202.78.114:1234 | US | 3527 | 6 | 6/6 |
| http://200.59.191.27:999 | VE | 1760 | 6 | 97/143 |
| socks5://121.169.46.116:1090 | KR | 2233 | 6 | 101/148 |
| http://114.248.179.223:8888 | CN | 1413 | 5 | 46/116 |
| http://45.65.138.48:999 | CO | 6540 | 5 | 60/148 |
| http://160.19.19.100:8080 | ID | 5501 | 5 | 20/79 |
| http://82.152.138.127:999 | MX | 3961 | 5 | 29/110 |
| http://148.245.75.54:999 | MX | 3438 | 5 | 14/37 |
| http://203.177.217.222:8082 | PH | 6867 | 5 | 58/93 |
| http://45.177.16.130:999 | PY | 5359 | 5 | 33/146 |
| http://88.210.37.30:3128 | US | 1083 | 5 | 5/5 |
| http://104.219.55.50:8118 | US | 914 | 5 | 6/10 |
| socks5://123.58.219.171:10808 | HK | 5018 | 5 | 117/148 |
| socks5://212.77.75.25:1088 | IT | 2129 | 5 | 40/48 |
| socks5://171.25.158.95:1080 | SE | 1424 | 5 | 54/63 |
| socks5://129.146.121.2:10808 | US | 801 | 5 | 5/5 |
| socks5://209.50.255.91:1080 | US | 914 | 5 | 33/65 |
| http://45.65.226.169:999 | AR | 3174 | 4 | 9/10 |
| http://186.38.100.130:999 | AR | 5014 | 4 | 13/23 |
| http://47.110.226.74:19991 | CN | 5441 | 4 | 58/146 |
| http://45.172.223.179:999 | CO | 4313 | 4 | 17/67 |
| http://179.1.196.133:999 | CO | 3346 | 4 | 4/4 |
| http://179.49.160.94:999 | CO | 5673 | 4 | 17/86 |
| http://38.57.65.195:999 | DO | 7088 | 4 | 10/33 |
| http://45.71.186.213:999 | EC | 6268 | 4 | 50/132 |
| http://181.78.195.136:999 | EC | 4531 | 4 | 4/4 |
| http://198.244.254.77:3128 | GB | 4691 | 4 | 29/32 |
| http://38.183.146.163:8080 | ID | 4001 | 4 | 20/121 |
| http://103.3.59.251:8080 | ID | 6772 | 4 | 20/114 |
| http://103.63.26.59:1111 | ID | 1483 | 4 | 18/49 |
| http://103.66.62.177:8080 | ID | 4222 | 4 | 14/67 |
| http://103.66.62.187:8080 | ID | 4394 | 4 | 12/41 |
| http://103.130.61.60:8081 | ID | 2550 | 4 | 4/4 |
| http://103.147.134.116:8082 | ID | 4755 | 4 | 33/107 |
| http://121.101.129.131:8080 | ID | 4530 | 4 | 6/14 |
| http://203.175.102.169:3125 | ID | 4524 | 4 | 14/56 |
| http://82.180.145.170:3129 | IN | 1580 | 4 | 19/50 |
| http://168.144.121.183:3129 | IN | 1513 | 4 | 45/99 |
| http://202.179.93.132:58080 | IN | 2760 | 4 | 21/126 |
| http://186.96.160.220:999 | MX | 3742 | 4 | 18/70 |
| http://38.172.130.175:999 | PE | 4367 | 4 | 13/34 |
| http://49.146.155.183:8082 | PH | 5867 | 4 | 21/69 |
| http://124.105.40.93:8181 | PH | 4396 | 4 | 31/113 |
| http://103.86.135.98:8080 | PK | 3580 | 4 | 8/22 |
| http://181.79.217.1:8080 | PY | 4794 | 4 | 11/29 |
| http://1.20.101.33:80 | TH | 2323 | 4 | 4/4 |
| http://162.214.159.94:3128 | US | 1504 | 4 | 4/4 |
| http://154.59.56.73:999 | VE | 7001 | 4 | 86/120 |
| http://171.245.71.144:2032 | VN | 4504 | 4 | 4/4 |
| socks5://113.249.111.67:1080 | CN | 2253 | 4 | 51/115 |
| socks5://213.199.47.140:1080 | FR | 1519 | 4 | 89/114 |
| socks5://45.74.31.46:6171 | NL | 3472 | 4 | 4/4 |
| socks5://45.74.31.46:6984 | NL | 7321 | 4 | 6/14 |
| socks5://45.74.31.47:15349 | NL | 3052 | 4 | 4/4 |
| socks5://217.71.230.103:1080 | RU | 1395 | 4 | 4/4 |
