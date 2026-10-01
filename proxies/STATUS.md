# Proxy status

Generated 2026-10-01T23:24:05Z by `harvest.py`.

- **2543** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5304** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39629** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 128/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2950 |
| http | 2346 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 2727 |
| ID | 624 |
| ?? | 355 |
| US | 128 |
| PH | 93 |
| CN | 87 |
| MX | 82 |
| CO | 71 |
| RU | 71 |
| IN | 66 |
| BR | 64 |
| DE | 53 |
| BD | 50 |
| EC | 50 |
| VE | 50 |
| SG | 40 |
| TR | 39 |
| AR | 34 |
| CA | 30 |
| HK | 29 |
| JP | 29 |
| VN | 27 |
| DO | 26 |
| EG | 26 |
| PK | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-10-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 88 | 88 | 19 | 2026-10-01 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-10-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 110 | 110 | 57 | 2026-10-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 127 | 127 | 44 | 2026-10-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 149 | 149 | 47 | 2026-10-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 83 | 2026-10-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 328 | 328 | 171 | 2026-10-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 348 | 348 | 98 | 2026-10-01 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 514 | 514 | 257 | 2026-10-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-10-01 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1200 | 1196 | 167 | 2026-10-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-10-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-10-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2368 | 2366 | 715 | 2026-10-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2480 | 2478 | 1741 | 2026-10-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3727 | 3725 | 1082 | 2026-10-01 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 36015 | 36015 | 20348 | 2026-10-01 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 42047 | 42046 | 2240 | 2026-10-01 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1424 | 91 | 104/105 |
| http://95.3.69.222:8080 | TR | 1264 | 60 | 102/105 |
| http://190.0.246.213:4040 | CO | 498 | 34 | 63/70 |
| http://213.111.146.36:18080 | NL | 471 | 34 | 37/42 |
| http://190.0.246.211:4040 | CO | 1073 | 25 | 92/105 |
| http://34.43.46.91:80 | US | 694 | 22 | 101/105 |
| http://190.0.246.210:4040 | CO | 801 | 21 | 93/104 |
| http://103.237.102.191:11111 | DE | 1121 | 21 | 99/105 |
| http://18.157.123.132:3128 | DE | 599 | 20 | 52/66 |
| socks5://144.91.121.61:1088 | FR | 1641 | 19 | 91/105 |
| http://34.43.46.91:443 | US | 386 | 18 | 99/105 |
| http://149.130.173.58:9443 | CO | 387 | 16 | 16/16 |
| http://43.173.120.13:8899 | US | 859 | 16 | 16/16 |
| http://185.195.71.218:18080 | CH | 615 | 13 | 33/42 |
| http://186.5.94.206:999 | EC | 939 | 13 | 64/67 |
| http://37.59.125.131:8888 | FR | 4284 | 13 | 84/105 |
| http://107.150.41.226:18080 | US | 380 | 13 | 41/42 |
| http://197.224.185.3:3128 | MU | 1515 | 11 | 67/73 |
| http://45.186.6.104:3128 | EC | 645 | 10 | 78/83 |
| http://185.191.239.248:3128 | CH | 1353 | 9 | 75/104 |
| socks5://101.36.104.239:10808 | JP | 2401 | 9 | 88/105 |
| http://34.88.38.81:9443 | FI | 584 | 8 | 48/70 |
| http://35.228.49.168:9443 | FI | 587 | 8 | 29/42 |
| http://195.158.8.123:3128 | UZ | 2819 | 8 | 69/103 |
| http://190.97.229.118:999 | VE | 6738 | 8 | 52/95 |
| http://190.97.241.106:999 | VE | 1520 | 8 | 61/89 |
| http://222.128.172.158:8888 | CN | 2503 | 7 | 33/70 |
| http://47.81.56.193:8888 | TH | 2192 | 7 | 65/105 |
| socks5://144.91.111.48:1088 | FR | 2001 | 7 | 68/105 |
| socks5://45.61.129.165:9050 | US | 2496 | 7 | 85/105 |
| http://123.121.121.123:8888 | CN | 1980 | 6 | 36/70 |
| http://35.78.212.217:32053 | JP | 3434 | 6 | 26/87 |
| http://5.129.254.5:8888 | RU | 892 | 6 | 51/60 |
| http://5.129.254.49:8888 | RU | 973 | 6 | 52/60 |
| http://5.129.254.51:8888 | RU | 925 | 6 | 52/60 |
| http://5.129.254.60:8888 | RU | 914 | 6 | 51/59 |
| http://5.129.254.70:8888 | RU | 961 | 6 | 52/60 |
| http://5.129.254.129:8888 | RU | 993 | 6 | 57/66 |
| http://5.129.254.154:8888 | RU | 969 | 6 | 48/56 |
| http://104.248.151.93:9090 | SG | 1196 | 6 | 6/6 |
| http://128.199.116.219:9090 | SG | 1762 | 6 | 20/24 |
| http://154.59.56.78:999 | VE | 1458 | 6 | 41/61 |
| socks5://45.155.71.236:1080 | AT | 718 | 6 | 8/10 |
| http://15.229.149.81:3128 | BR | 2389 | 5 | 10/15 |
| http://190.12.150.244:999 | EC | 7461 | 5 | 71/101 |
| http://159.223.41.216:9090 | SG | 1166 | 5 | 44/65 |
| http://18.190.253.157:5051 | US | 1096 | 5 | 6/17 |
| http://165.154.162.73:8888 | US | 826 | 5 | 61/105 |
| http://38.51.207.104:8080 | VE | 565 | 5 | 44/46 |
| http://154.59.56.74:999 | VE | 2810 | 5 | 47/68 |
| http://210.211.113.33:80 | VN | 6297 | 5 | 47/75 |
| http://89.36.160.2:3128 | ?? | 579 | 5 | 5/5 |
| http://203.175.102.67:3125 | ?? | 2368 | 5 | 5/5 |
| socks5://45.74.31.40:4281 | NL | 4446 | 5 | 5/5 |
| socks5://185.50.202.185:1080 | ?? | 1965 | 5 | 5/5 |
| socks5://212.77.75.25:1088 | ?? | 845 | 5 | 5/5 |
| http://3.26.199.107:1234 | AU | 3229 | 4 | 7/18 |
| http://54.206.129.120:41345 | AU | 3893 | 4 | 20/83 |
| http://38.7.195.51:999 | CL | 3495 | 4 | 35/96 |
| http://119.188.131.55:17981 | CN | 6590 | 4 | 48/105 |
| http://122.246.3.12:17981 | CN | 1763 | 4 | 46/99 |
| http://31.31.74.185:9898 | CZ | 616 | 4 | 22/26 |
| http://177.53.215.196:1812 | EC | 1522 | 4 | 7/20 |
| http://177.234.221.197:999 | EC | 1449 | 4 | 7/10 |
| http://41.33.60.42:8081 | EG | 2394 | 4 | 33/103 |
| http://160.22.217.93:8082 | ID | 3671 | 4 | 17/47 |
| http://223.25.106.206:8181 | ID | 1770 | 4 | 6/18 |
| http://168.144.121.183:3129 | IN | 1363 | 4 | 27/56 |
| http://178.92.72.194:8080 | IN | 1058 | 4 | 6/12 |
| http://144.124.251.24:10000 | NL | 530 | 4 | 32/51 |
| http://144.124.251.24:10007 | NL | 964 | 4 | 32/54 |
| http://144.124.251.24:10008 | NL | 485 | 4 | 28/36 |
| http://144.124.251.24:10082 | NL | 1173 | 4 | 29/53 |
| http://144.124.251.24:10088 | NL | 511 | 4 | 27/37 |
| http://144.124.251.24:10104 | NL | 533 | 4 | 28/37 |
| http://144.124.251.24:10176 | NL | 657 | 4 | 32/53 |
| http://144.124.251.24:10185 | NL | 538 | 4 | 29/37 |
| http://144.124.251.24:10187 | NL | 1204 | 4 | 28/51 |
| http://144.124.251.24:10216 | NL | 471 | 4 | 33/54 |
| http://144.124.251.24:10226 | NL | 536 | 4 | 27/36 |
| http://144.124.251.24:10230 | NL | 603 | 4 | 31/52 |
| http://144.124.251.24:10261 | NL | 5157 | 4 | 28/37 |
| http://144.124.251.24:10299 | NL | 480 | 4 | 27/37 |
| http://144.124.251.24:10333 | NL | 529 | 4 | 31/54 |
| http://144.124.251.24:10346 | NL | 563 | 4 | 29/37 |
| http://144.124.251.24:10372 | NL | 565 | 4 | 32/49 |
| http://144.124.251.24:10412 | NL | 553 | 4 | 28/37 |
| http://144.124.251.24:10431 | NL | 508 | 4 | 34/53 |
| http://144.124.251.24:10453 | NL | 2370 | 4 | 31/42 |
| http://144.124.251.24:10471 | NL | 588 | 4 | 32/52 |
| http://144.124.251.24:10485 | NL | 1237 | 4 | 25/37 |
| http://144.124.251.24:10551 | NL | 469 | 4 | 33/53 |
| http://144.124.251.24:10566 | NL | 514 | 4 | 29/38 |
| http://144.124.251.24:10574 | NL | 494 | 4 | 33/54 |
| http://144.124.251.24:10601 | NL | 507 | 4 | 26/52 |
| http://144.124.251.24:10605 | NL | 713 | 4 | 28/37 |
| http://144.124.251.24:10610 | NL | 502 | 4 | 28/37 |
| http://144.124.251.24:10628 | NL | 539 | 4 | 26/37 |
| http://144.124.251.24:10631 | NL | 513 | 4 | 28/37 |
| http://144.124.251.24:10658 | NL | 512 | 4 | 28/37 |
