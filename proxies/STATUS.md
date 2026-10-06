# Proxy status

Generated 2026-10-06T19:06:17Z by `harvest.py`.

- **1306** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5171** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39642** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 70/600 (12%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3019 |
| http | 2146 |
| socks4 | 6 |

| country | entries |
|---|---|
| NL | 2686 |
| ID | 583 |
| ?? | 431 |
| US | 93 |
| PH | 89 |
| MX | 78 |
| CO | 76 |
| RU | 76 |
| CN | 71 |
| BD | 64 |
| BR | 57 |
| EC | 54 |
| IN | 54 |
| VE | 52 |
| TR | 41 |
| DE | 40 |
| SG | 34 |
| DO | 32 |
| JP | 32 |
| AR | 31 |
| EG | 28 |
| VN | 28 |
| PK | 27 |
| CA | 25 |
| CL | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 80 | 80 | 39 | 2026-10-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 99 | 99 | 34 | 2026-10-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 114 | 114 | 39 | 2026-10-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 190 | 190 | 54 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 281 | 281 | 63 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 292 | 292 | 167 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 395 | 395 | 214 | 2026-10-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-10-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1204 | 1200 | 135 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1150 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1592 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2362 | 2360 | 776 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2479 | 2477 | 1701 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4173 | 4171 | 1520 | 2026-10-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 44914 | 44914 | 27470 | 2026-10-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 50353 | 50352 | 1973 | 2026-10-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.3.69.222:8080 | TR | 1646 | 68 | 110/113 |
| http://190.0.246.211:4040 | CO | 922 | 33 | 100/113 |
| http://34.43.46.91:80 | US | 833 | 30 | 109/113 |
| http://190.0.246.210:4040 | CO | 841 | 29 | 101/112 |
| http://34.43.46.91:443 | US | 615 | 26 | 107/113 |
| http://149.130.173.58:9443 | CO | 587 | 24 | 24/24 |
| http://43.173.120.13:8899 | US | 434 | 24 | 24/24 |
| http://159.223.41.216:9090 | SG | 894 | 13 | 52/73 |
| socks5://212.77.75.25:1088 | IT | 1086 | 13 | 13/13 |
| socks5://171.25.158.95:1080 | SE | 2363 | 11 | 23/28 |
| socks5://213.199.47.140:1080 | FR | 6265 | 10 | 65/79 |
| socks5://47.238.126.208:1080 | HK | 1442 | 10 | 17/18 |
| socks5://85.209.156.148:1080 | US | 2016 | 10 | 47/84 |
| http://107.167.18.122:443 | US | 91 | 9 | 61/65 |
| socks5://79.137.198.71:7777 | NL | 1054 | 9 | 10/13 |
| socks5://83.147.217.103:1080 | US | 472 | 9 | 33/36 |
| http://184.75.221.82:3118 | CA | 367 | 8 | 69/78 |
| http://123.121.123.115:8888 | CN | 1234 | 8 | 22/37 |
| socks5://123.58.219.171:10808 | HK | 1352 | 8 | 87/113 |
| http://119.188.131.55:17981 | CN | 5942 | 7 | 55/113 |
| http://190.0.246.213:4040 | CO | 711 | 7 | 70/78 |
| http://45.245.208.181:8080 | EG | 3462 | 7 | 9/17 |
| http://144.124.251.24:10000 | NL | 1506 | 7 | 39/59 |
| http://144.124.251.24:10007 | NL | 1592 | 7 | 39/62 |
| http://144.124.251.24:10008 | NL | 1054 | 7 | 35/44 |
| http://144.124.251.24:10082 | NL | 1774 | 7 | 36/61 |
| http://144.124.251.24:10084 | NL | 2179 | 7 | 34/45 |
| http://144.124.251.24:10088 | NL | 1714 | 7 | 34/45 |
| http://144.124.251.24:10104 | NL | 2597 | 7 | 35/45 |
| http://144.124.251.24:10176 | NL | 1073 | 7 | 39/61 |
| http://144.124.251.24:10185 | NL | 1600 | 7 | 36/45 |
| http://144.124.251.24:10187 | NL | 1080 | 7 | 35/59 |
| http://144.124.251.24:10216 | NL | 924 | 7 | 40/62 |
| http://144.124.251.24:10226 | NL | 1155 | 7 | 34/44 |
| http://144.124.251.24:10230 | NL | 858 | 7 | 38/60 |
| http://144.124.251.24:10261 | NL | 1338 | 7 | 35/45 |
| http://144.124.251.24:10299 | NL | 2631 | 7 | 34/45 |
| http://144.124.251.24:10333 | NL | 924 | 7 | 38/62 |
| http://144.124.251.24:10337 | NL | 1601 | 7 | 33/45 |
| http://144.124.251.24:10346 | NL | 2285 | 7 | 36/45 |
| http://144.124.251.24:10366 | NL | 973 | 7 | 36/59 |
| http://144.124.251.24:10372 | NL | 1102 | 7 | 39/57 |
| http://144.124.251.24:10412 | NL | 3220 | 7 | 35/45 |
| http://144.124.251.24:10431 | NL | 971 | 7 | 41/61 |
| http://144.124.251.24:10453 | NL | 972 | 7 | 38/50 |
| http://144.124.251.24:10471 | NL | 988 | 7 | 39/60 |
| http://144.124.251.24:10551 | NL | 973 | 7 | 40/61 |
| http://144.124.251.24:10566 | NL | 1071 | 7 | 36/46 |
| http://144.124.251.24:10574 | NL | 967 | 7 | 40/62 |
| http://144.124.251.24:10601 | NL | 1003 | 7 | 33/60 |
| http://144.124.251.24:10605 | NL | 1046 | 7 | 35/45 |
| http://144.124.251.24:10610 | NL | 1773 | 7 | 35/45 |
| http://144.124.251.24:10628 | NL | 2475 | 7 | 33/45 |
| http://144.124.251.24:10631 | NL | 2189 | 7 | 35/45 |
| http://144.124.251.24:10658 | NL | 3043 | 7 | 35/45 |
| http://144.124.251.24:10689 | NL | 1440 | 7 | 36/49 |
| http://144.124.251.24:10771 | NL | 1055 | 7 | 35/45 |
| http://144.124.251.24:10800 | NL | 1560 | 7 | 35/45 |
| http://144.124.251.24:10801 | NL | 1468 | 7 | 36/61 |
| http://144.124.251.24:10811 | NL | 1286 | 7 | 35/45 |
| http://144.124.251.24:10818 | NL | 2207 | 7 | 32/45 |
| http://144.124.251.24:10829 | NL | 3028 | 7 | 33/45 |
| http://144.124.251.24:10953 | NL | 2008 | 7 | 36/45 |
| http://144.124.251.24:11011 | NL | 1115 | 7 | 36/45 |
| http://144.124.251.24:11108 | NL | 1111 | 7 | 36/60 |
| http://144.124.251.24:11124 | NL | 917 | 7 | 37/62 |
| http://144.124.251.24:11180 | NL | 1739 | 7 | 34/44 |
| http://144.124.251.24:11265 | NL | 1282 | 7 | 39/61 |
| http://144.124.251.24:11266 | NL | 1244 | 7 | 36/45 |
| http://144.124.251.24:11274 | NL | 1030 | 7 | 39/61 |
| http://144.124.251.24:11450 | NL | 1270 | 7 | 33/45 |
| http://144.124.251.24:11480 | NL | 1617 | 7 | 34/45 |
| http://144.124.251.24:11491 | NL | 1040 | 7 | 39/61 |
| http://154.59.56.72:999 | VE | 7932 | 7 | 50/72 |
| http://168.194.34.196:9001 | AR | 7875 | 6 | 40/111 |
| http://45.71.186.210:999 | EC | 3804 | 6 | 29/87 |
| http://190.12.150.244:999 | EC | 5571 | 6 | 78/109 |
| http://41.128.77.76:1981 | EG | 1283 | 6 | 30/67 |
| http://44.216.27.249:3128 | US | 6108 | 6 | 9/10 |
| http://200.59.191.27:999 | VE | 2527 | 6 | 71/108 |
| socks5://103.75.118.84:1080 | JP | 742 | 6 | 78/108 |
| http://45.240.232.61:8080 | EG | 6311 | 5 | 38/93 |
| http://51.170.133.249:80 | MA | 1055 | 5 | 19/36 |
| http://197.224.185.3:3128 | MU | 2123 | 5 | 74/81 |
| http://128.199.121.61:9090 | SG | 913 | 5 | 27/33 |
| http://167.172.76.176:9090 | SG | 943 | 5 | 51/74 |
| http://165.154.162.73:8888 | US | 544 | 5 | 67/113 |
| http://4.144.146.21:80 | ?? | 912 | 5 | 5/5 |
| http://38.175.202.151:443 | ?? | 5461 | 5 | 5/5 |
| http://102.244.78.61:8090 | ?? | 1622 | 5 | 5/5 |
| socks5://65.21.252.66:10805 | FI | 6268 | 5 | 17/27 |
| http://187.102.219.64:999 | AR | 5017 | 4 | 27/52 |
| http://120.232.115.170:17981 | CN | 1206 | 4 | 81/112 |
| http://186.5.94.206:999 | EC | 1580 | 4 | 69/75 |
| http://45.80.151.33:3128 | NL | 822 | 4 | 15/37 |
| http://69.87.216.54:7989 | US | 33 | 4 | 36/58 |
| http://154.59.56.74:999 | VE | 5202 | 4 | 54/76 |
| http://154.59.56.76:999 | VE | 7513 | 4 | 57/73 |
| http://154.59.56.78:999 | VE | 4582 | 4 | 48/69 |
| socks5://107.149.92.23:8443 | HK | 2786 | 4 | 8/30 |
