# Proxy status

Generated 2026-09-26T22:11:31Z by `harvest.py`.

- **2075** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4495** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39797** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 158/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2266 |
| http | 2216 |
| socks4 | 13 |

| country | entries |
|---|---|
| NL | 2012 |
| ID | 535 |
| ?? | 484 |
| US | 138 |
| CN | 123 |
| RU | 83 |
| CO | 74 |
| PH | 70 |
| MX | 68 |
| DE | 57 |
| IN | 53 |
| BD | 51 |
| BR | 51 |
| VE | 45 |
| EC | 37 |
| VN | 34 |
| SG | 33 |
| EG | 32 |
| FR | 27 |
| TR | 27 |
| DO | 26 |
| JP | 25 |
| PK | 23 |
| AR | 20 |
| KH | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-09-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 50 | 50 | 23 | 2026-09-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-09-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 129 | 129 | 48 | 2026-09-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 143 | 143 | 39 | 2026-09-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 74 | 2026-09-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 156 | 156 | 45 | 2026-09-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 173 | 173 | 61 | 2026-09-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 375 | 375 | 153 | 2026-09-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 462 | 462 | 130 | 2026-09-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-09-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1125 | 2026-09-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1585 | 2026-09-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1948 | 1944 | 263 | 2026-09-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2810 | 2808 | 747 | 2026-09-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3169 | 3167 | 2203 | 2026-09-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3725 | 3723 | 667 | 2026-09-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 24948 | 24948 | 12213 | 2026-09-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 32506 | 32505 | 2780 | 2026-09-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1111 | 81 | 94/95 |
| http://190.97.236.128:999 | VE | 720 | 52 | 83/85 |
| http://190.97.236.129:999 | VE | 645 | 52 | 83/85 |
| http://95.3.69.222:8080 | TR | 1336 | 50 | 92/95 |
| http://38.51.207.104:8080 | VE | 558 | 28 | 35/36 |
| http://193.104.179.115:3128 | UZ | 1174 | 25 | 43/60 |
| http://190.0.246.213:4040 | CO | 450 | 24 | 53/60 |
| http://213.111.146.36:18080 | NL | 477 | 24 | 27/32 |
| http://153.51.201.35:999 | VE | 762 | 22 | 22/22 |
| http://144.124.251.24:10007 | NL | 693 | 19 | 26/44 |
| http://144.124.251.24:10008 | NL | 1121 | 19 | 22/26 |
| http://144.124.251.24:10104 | NL | 890 | 19 | 22/27 |
| http://144.124.251.24:10176 | NL | 662 | 19 | 26/43 |
| http://144.124.251.24:10185 | NL | 694 | 19 | 23/27 |
| http://144.124.251.24:10216 | NL | 726 | 19 | 27/44 |
| http://144.124.251.24:10226 | NL | 2056 | 19 | 21/26 |
| http://144.124.251.24:10333 | NL | 1313 | 19 | 25/44 |
| http://144.124.251.24:10346 | NL | 747 | 19 | 23/27 |
| http://144.124.251.24:10366 | NL | 723 | 19 | 24/41 |
| http://144.124.251.24:10372 | NL | 692 | 19 | 26/39 |
| http://144.124.251.24:10431 | NL | 699 | 19 | 28/43 |
| http://144.124.251.24:10453 | NL | 2519 | 19 | 25/32 |
| http://144.124.251.24:10551 | NL | 650 | 19 | 27/43 |
| http://144.124.251.24:10574 | NL | 806 | 19 | 27/44 |
| http://144.124.251.24:10771 | NL | 631 | 19 | 22/27 |
| http://144.124.251.24:10953 | NL | 779 | 19 | 23/27 |
| http://144.124.251.24:11011 | NL | 622 | 19 | 23/27 |
| http://144.124.251.24:11265 | NL | 718 | 19 | 26/43 |
| http://144.124.251.24:11266 | NL | 622 | 19 | 23/27 |
| http://144.124.251.24:11274 | NL | 753 | 19 | 26/43 |
| http://144.124.251.24:11480 | NL | 621 | 19 | 21/27 |
| http://144.124.251.24:11491 | NL | 671 | 19 | 26/43 |
| socks5://83.147.217.103:1080 | US | 133 | 18 | 18/18 |
| http://144.124.251.24:10801 | NL | 2494 | 17 | 23/43 |
| socks5://185.87.255.54:1080 | GB | 641 | 16 | 16/16 |
| socks5://101.36.104.239:10808 | JP | 1778 | 16 | 79/95 |
| http://190.0.246.211:4040 | CO | 746 | 15 | 82/95 |
| http://167.172.76.176:9090 | SG | 1165 | 15 | 37/56 |
| http://144.124.251.24:10261 | NL | 751 | 14 | 22/27 |
| socks5://101.36.104.46:10808 | JP | 2199 | 14 | 85/95 |
| http://154.59.56.76:999 | VE | 2085 | 13 | 44/55 |
| http://144.124.251.24:10084 | NL | 639 | 12 | 22/27 |
| http://144.124.251.24:10088 | NL | 673 | 12 | 21/27 |
| http://144.124.251.24:10412 | NL | 1539 | 12 | 22/27 |
| http://144.124.251.24:10471 | NL | 697 | 12 | 26/42 |
| http://144.124.251.24:10566 | NL | 799 | 12 | 23/28 |
| http://144.124.251.24:10605 | NL | 623 | 12 | 22/27 |
| http://144.124.251.24:10610 | NL | 774 | 12 | 22/27 |
| http://144.124.251.24:10631 | NL | 553 | 12 | 22/27 |
| http://144.124.251.24:10658 | NL | 589 | 12 | 22/27 |
| http://144.124.251.24:10689 | NL | 4013 | 12 | 23/31 |
| http://144.124.251.24:10800 | NL | 656 | 12 | 22/27 |
| http://144.124.251.24:10811 | NL | 655 | 12 | 22/27 |
| http://144.124.251.24:10818 | NL | 580 | 12 | 19/27 |
| http://144.124.251.24:11450 | NL | 929 | 12 | 20/27 |
| http://34.43.46.91:80 | US | 448 | 12 | 91/95 |
| http://190.0.246.210:4040 | CO | 788 | 11 | 83/94 |
| http://103.237.102.191:11111 | DE | 749 | 11 | 89/95 |
| http://154.59.56.73:999 | VE | 2474 | 11 | 54/67 |
| http://190.97.236.130:999 | VE | 653 | 11 | 21/24 |
| http://200.229.65.172:3128 | BR | 3329 | 10 | 10/10 |
| http://18.157.123.132:3128 | DE | 517 | 10 | 42/56 |
| http://3.216.199.128:3128 | US | 105 | 10 | 10/10 |
| http://107.167.18.122:443 | US | 324 | 10 | 45/47 |
| socks5://109.205.182.143:1088 | FR | 1563 | 10 | 10/10 |
| socks5://144.91.121.61:1088 | FR | 1561 | 9 | 81/95 |
| http://34.43.46.91:443 | US | 544 | 8 | 89/95 |
| http://123.121.132.32:8888 | CN | 1425 | 7 | 25/56 |
| http://134.199.191.115:3128 | DE | 561 | 7 | 7/7 |
| http://189.51.168.165:999 | MX | 972 | 7 | 7/7 |
| http://144.124.251.24:10000 | NL | 622 | 7 | 26/41 |
| http://144.124.251.24:10187 | NL | 629 | 7 | 22/41 |
| http://144.124.251.24:10230 | NL | 716 | 7 | 25/42 |
| http://144.124.251.24:10829 | NL | 1777 | 7 | 21/27 |
| http://144.124.251.24:11108 | NL | 729 | 7 | 23/42 |
| http://144.124.251.24:11124 | NL | 728 | 7 | 24/44 |
| http://144.124.251.24:11180 | NL | 749 | 7 | 21/26 |
| socks5://23.239.30.204:1088 | US | 5393 | 7 | 7/7 |
| http://101.251.204.174:8080 | CN | 1984 | 6 | 43/81 |
| http://222.128.173.231:8888 | CN | 1445 | 6 | 28/63 |
| http://149.130.173.58:9443 | CO | 395 | 6 | 6/6 |
| http://91.134.141.4:3128 | FR | 996 | 6 | 50/56 |
| http://43.173.120.13:8899 | US | 771 | 6 | 6/6 |
| http://161.22.39.58:999 | VE | 676 | 6 | 6/6 |
| http://201.71.2.25:999 | VE | 4748 | 6 | 34/82 |
| socks5://45.151.102.248:10808 | RU | 846 | 6 | 6/6 |
| socks5://45.61.129.165:9050 | US | 2473 | 6 | 76/95 |
| http://187.102.219.42:999 | AR | 1090 | 5 | 47/90 |
| http://103.82.246.27:6080 | ID | 4585 | 5 | 11/21 |
| http://144.124.251.24:10485 | NL | 1078 | 5 | 19/27 |
| http://128.199.121.61:9090 | SG | 1195 | 5 | 13/15 |
| http://146.190.80.158:9090 | SG | 1198 | 5 | 17/21 |
| http://3.212.18.54:3128 | ?? | 195 | 5 | 5/5 |
| socks5://49.13.22.249:10806 | DE | 5358 | 5 | 10/17 |
| socks5://43.167.166.56:1080 | JP | 971 | 5 | 6/7 |
| socks5://171.25.158.95:1080 | SE | 2122 | 5 | 6/10 |
| http://168.194.34.196:9001 | AR | 1125 | 4 | 28/93 |
| http://36.137.204.11:8002 | CN | 3650 | 4 | 7/11 |
| http://47.121.139.13:3128 | CN | 5145 | 4 | 46/94 |
| http://123.119.25.143:8888 | CN | 7536 | 4 | 24/60 |
