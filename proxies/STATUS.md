# Proxy status

Generated 2026-09-25T17:52:57Z by `harvest.py`.

- **1725** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3717** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **37386** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 141/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1879 |
| http | 1835 |
| socks4 | 3 |

| country | entries |
|---|---|
| NL | 1656 |
| ID | 456 |
| ?? | 164 |
| US | 155 |
| CN | 109 |
| RU | 89 |
| MX | 73 |
| CO | 65 |
| BD | 58 |
| BR | 57 |
| DE | 49 |
| IN | 47 |
| PH | 47 |
| VE | 46 |
| VN | 38 |
| JP | 34 |
| SG | 32 |
| EC | 31 |
| EG | 29 |
| DO | 28 |
| FR | 25 |
| PK | 23 |
| TH | 23 |
| AR | 20 |
| HK | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 2 | 2026-09-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 17 | 17 | 4 | 2026-09-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 73 | 73 | 30 | 2026-09-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 138 | 138 | 41 | 2026-09-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 143 | 143 | 49 | 2026-09-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-09-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 193 | 193 | 60 | 2026-09-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 361 | 361 | 149 | 2026-09-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-09-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 585 | 585 | 159 | 2026-09-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-09-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-09-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-09-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1900 | 1896 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2704 | 2702 | 650 | 2026-09-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2847 | 2845 | 2068 | 2026-09-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2931 | 2929 | 517 | 2026-09-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 21290 | 21290 | 10905 | 2026-09-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 28111 | 28110 | 3326 | 2026-09-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 768 | 78 | 91/92 |
| http://130.110.103.245:3128 | SA | 7901 | 78 | 90/92 |
| http://1.231.81.166:3128 | KR | 1429 | 57 | 89/92 |
| http://190.97.236.128:999 | VE | 749 | 49 | 80/82 |
| http://190.97.236.129:999 | VE | 764 | 49 | 80/82 |
| http://95.3.69.222:8080 | TR | 1280 | 47 | 89/92 |
| http://38.51.207.104:8080 | VE | 1509 | 25 | 32/33 |
| http://193.104.179.115:3128 | UZ | 1148 | 22 | 40/57 |
| http://190.0.246.213:4040 | CO | 560 | 21 | 50/57 |
| http://213.111.146.36:18080 | NL | 486 | 21 | 24/29 |
| http://153.51.201.35:999 | VE | 684 | 19 | 19/19 |
| http://144.124.251.24:10007 | NL | 610 | 16 | 23/41 |
| http://144.124.251.24:10008 | NL | 598 | 16 | 19/23 |
| http://144.124.251.24:10104 | NL | 590 | 16 | 19/24 |
| http://144.124.251.24:10176 | NL | 971 | 16 | 23/40 |
| http://144.124.251.24:10185 | NL | 718 | 16 | 20/24 |
| http://144.124.251.24:10216 | NL | 620 | 16 | 24/41 |
| http://144.124.251.24:10226 | NL | 639 | 16 | 18/23 |
| http://144.124.251.24:10333 | NL | 658 | 16 | 22/41 |
| http://144.124.251.24:10346 | NL | 584 | 16 | 20/24 |
| http://144.124.251.24:10366 | NL | 653 | 16 | 21/38 |
| http://144.124.251.24:10372 | NL | 548 | 16 | 23/36 |
| http://144.124.251.24:10431 | NL | 591 | 16 | 25/40 |
| http://144.124.251.24:10453 | NL | 3110 | 16 | 22/29 |
| http://144.124.251.24:10551 | NL | 636 | 16 | 24/40 |
| http://144.124.251.24:10574 | NL | 611 | 16 | 24/41 |
| http://144.124.251.24:10771 | NL | 594 | 16 | 19/24 |
| http://144.124.251.24:10953 | NL | 539 | 16 | 20/24 |
| http://144.124.251.24:11011 | NL | 569 | 16 | 20/24 |
| http://144.124.251.24:11265 | NL | 584 | 16 | 23/40 |
| http://144.124.251.24:11266 | NL | 617 | 16 | 20/24 |
| http://144.124.251.24:11274 | NL | 570 | 16 | 23/40 |
| http://144.124.251.24:11480 | NL | 552 | 16 | 18/24 |
| http://144.124.251.24:11491 | NL | 590 | 16 | 23/40 |
| socks5://83.147.217.103:1080 | US | 110 | 15 | 15/15 |
| http://144.124.251.24:10801 | NL | 958 | 14 | 20/40 |
| socks5://213.199.47.140:1080 | FR | 5219 | 14 | 50/58 |
| socks5://185.87.255.54:1080 | GB | 682 | 13 | 13/13 |
| socks5://101.36.104.239:10808 | JP | 2005 | 13 | 76/92 |
| http://190.0.246.211:4040 | CO | 763 | 12 | 79/92 |
| http://144.124.251.24:10082 | NL | 599 | 12 | 22/40 |
| http://167.172.76.176:9090 | SG | 1170 | 12 | 34/53 |
| socks5://103.75.118.84:1080 | JP | 3465 | 12 | 66/87 |
| http://144.124.251.24:10261 | NL | 579 | 11 | 19/24 |
| http://128.199.116.219:9090 | SG | 1272 | 11 | 11/11 |
| socks5://101.36.104.46:10808 | JP | 1450 | 11 | 82/92 |
| http://213.32.70.99:3128 | FR | 2006 | 10 | 10/10 |
| http://154.59.56.76:999 | VE | 4732 | 10 | 41/52 |
| http://181.119.224.25:8080 | EC | 730 | 9 | 9/9 |
| http://197.224.185.3:3128 | MU | 1761 | 9 | 55/60 |
| http://144.124.251.24:10084 | NL | 553 | 9 | 19/24 |
| http://144.124.251.24:10088 | NL | 554 | 9 | 18/24 |
| http://144.124.251.24:10412 | NL | 551 | 9 | 19/24 |
| http://144.124.251.24:10471 | NL | 708 | 9 | 23/39 |
| http://144.124.251.24:10566 | NL | 525 | 9 | 20/25 |
| http://144.124.251.24:10605 | NL | 600 | 9 | 19/24 |
| http://144.124.251.24:10610 | NL | 588 | 9 | 19/24 |
| http://144.124.251.24:10631 | NL | 774 | 9 | 19/24 |
| http://144.124.251.24:10658 | NL | 566 | 9 | 19/24 |
| http://144.124.251.24:10689 | NL | 586 | 9 | 20/28 |
| http://144.124.251.24:10800 | NL | 1194 | 9 | 19/24 |
| http://144.124.251.24:10811 | NL | 530 | 9 | 19/24 |
| http://144.124.251.24:10818 | NL | 623 | 9 | 16/24 |
| http://144.124.251.24:11450 | NL | 551 | 9 | 17/24 |
| http://34.43.46.91:80 | US | 314 | 9 | 88/92 |
| http://190.0.246.210:4040 | CO | 1560 | 8 | 80/91 |
| http://103.237.102.191:11111 | DE | 737 | 8 | 86/92 |
| http://35.78.212.217:32053 | JP | 2445 | 8 | 18/74 |
| http://154.59.56.72:999 | VE | 5282 | 8 | 34/51 |
| http://154.59.56.73:999 | VE | 1511 | 8 | 51/64 |
| http://190.97.236.130:999 | VE | 6902 | 8 | 18/21 |
| http://200.229.65.172:3128 | BR | 6058 | 7 | 7/7 |
| http://38.7.195.50:999 | CL | 7369 | 7 | 26/51 |
| http://18.157.123.132:3128 | DE | 523 | 7 | 39/53 |
| http://103.130.61.61:8081 | ID | 6131 | 7 | 74/92 |
| http://3.216.199.128:3128 | US | 63 | 7 | 7/7 |
| http://107.167.18.122:443 | US | 327 | 7 | 42/44 |
| socks5://109.205.182.143:1088 | FR | 581 | 7 | 7/7 |
| http://114.252.12.211:8888 | CN | 2334 | 6 | 28/57 |
| http://120.232.115.57:17981 | CN | 7003 | 6 | 13/17 |
| http://222.128.172.158:8888 | CN | 2074 | 6 | 23/57 |
| http://34.88.38.81:9443 | FI | 747 | 6 | 39/57 |
| http://35.228.49.168:9443 | FI | 585 | 6 | 20/29 |
| http://140.238.32.108:3128 | JP | 1560 | 6 | 43/91 |
| http://190.89.29.110:999 | VE | 3305 | 6 | 21/70 |
| socks5://144.91.121.61:1088 | FR | 7653 | 6 | 78/92 |
| socks5://67.207.92.87:1088 | US | 883 | 6 | 49/91 |
| http://45.186.6.104:3128 | EC | 668 | 5 | 67/70 |
| http://91.233.223.147:3128 | RU | 2939 | 5 | 19/66 |
| http://34.43.46.91:443 | US | 330 | 5 | 86/92 |
| socks5://185.87.255.47:1080 | GB | 583 | 5 | 10/11 |
| socks5://103.88.234.239:40002 | MX | 524 | 5 | 11/15 |
| socks5://45.74.31.40:10065 | NL | 3491 | 5 | 5/5 |
| http://111.192.16.130:8888 | CN | 1623 | 4 | 27/57 |
| http://111.196.26.27:8888 | CN | 1399 | 4 | 7/14 |
| http://114.244.217.102:8888 | CN | 2246 | 4 | 9/15 |
| http://123.115.226.82:8888 | CN | 3701 | 4 | 13/38 |
| http://123.121.132.32:8888 | CN | 7396 | 4 | 22/53 |
| http://125.33.195.27:8888 | CN | 2024 | 4 | 16/38 |
| http://222.128.171.2:8888 | CN | 4603 | 4 | 24/44 |
