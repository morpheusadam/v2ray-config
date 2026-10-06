# Proxy status

Generated 2026-10-06T00:56:26Z by `harvest.py`.

- **2892** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5629** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39146** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 123/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3506 |
| http | 2115 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 3139 |
| ID | 600 |
| ?? | 449 |
| PH | 92 |
| US | 84 |
| RU | 82 |
| CO | 75 |
| MX | 70 |
| CN | 66 |
| BD | 65 |
| BR | 54 |
| EC | 52 |
| DE | 48 |
| VE | 48 |
| IN | 47 |
| TR | 42 |
| VN | 36 |
| DO | 34 |
| EG | 29 |
| CL | 28 |
| SG | 27 |
| AR | 26 |
| PK | 26 |
| TH | 26 |
| JP | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 122 | 122 | 66 | 2026-10-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 56 | 2026-10-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 89 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 221 | 221 | 80 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 259 | 259 | 69 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 354 | 354 | 174 | 2026-10-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 760 | 760 | 196 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 787 | 787 | 418 | 2026-10-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1320 | 1320 | 281 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1135 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2375 | 2375 | 758 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2614 | 2614 | 1771 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3736 | 3736 | 1220 | 2026-10-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 43878 | 43878 | 26493 | 2026-10-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 50520 | 50520 | 2415 | 2026-10-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1032 | 98 | 111/112 |
| http://95.3.69.222:8080 | TR | 1543 | 67 | 109/112 |
| http://190.0.246.211:4040 | CO | 672 | 32 | 99/112 |
| http://34.43.46.91:80 | US | 490 | 29 | 108/112 |
| http://190.0.246.210:4040 | CO | 762 | 28 | 100/111 |
| http://103.237.102.191:11111 | DE | 829 | 28 | 106/112 |
| http://34.43.46.91:443 | US | 505 | 25 | 106/112 |
| http://149.130.173.58:9443 | CO | 447 | 23 | 23/23 |
| http://43.173.120.13:8899 | US | 381 | 23 | 23/23 |
| socks5://101.36.104.239:10808 | JP | 4229 | 16 | 95/112 |
| http://159.223.41.216:9090 | SG | 1153 | 12 | 51/72 |
| socks5://212.77.75.25:1088 | IT | 705 | 12 | 12/12 |
| socks5://5.255.123.162:1080 | NL | 561 | 10 | 34/95 |
| socks5://171.25.158.95:1080 | SE | 3706 | 10 | 22/27 |
| socks5://213.199.47.140:1080 | FR | 2920 | 9 | 64/78 |
| socks5://47.238.126.208:1080 | HK | 2177 | 9 | 16/17 |
| socks5://85.209.156.148:1080 | US | 4180 | 9 | 46/83 |
| http://103.144.54.73:8082 | ID | 6658 | 8 | 32/57 |
| http://107.167.18.122:443 | US | 328 | 8 | 60/64 |
| socks5://121.169.46.116:1090 | KR | 2767 | 8 | 77/112 |
| socks5://79.137.198.71:7777 | NL | 1619 | 8 | 9/12 |
| socks5://83.147.217.103:1080 | US | 277 | 8 | 32/35 |
| http://184.75.221.82:3118 | CA | 186 | 7 | 68/77 |
| http://123.121.123.115:8888 | CN | 1581 | 7 | 21/36 |
| http://202.136.82.219:8080 | ID | 6704 | 7 | 32/110 |
| socks5://123.58.219.171:10808 | HK | 2663 | 7 | 86/112 |
| http://119.188.131.55:17981 | CN | 5863 | 6 | 54/112 |
| http://190.0.246.213:4040 | CO | 484 | 6 | 69/77 |
| http://45.245.208.181:8080 | EG | 3199 | 6 | 8/16 |
| http://144.124.251.24:10000 | NL | 2352 | 6 | 38/58 |
| http://144.124.251.24:10007 | NL | 791 | 6 | 38/61 |
| http://144.124.251.24:10008 | NL | 718 | 6 | 34/43 |
| http://144.124.251.24:10082 | NL | 1175 | 6 | 35/60 |
| http://144.124.251.24:10084 | NL | 1417 | 6 | 33/44 |
| http://144.124.251.24:10088 | NL | 772 | 6 | 33/44 |
| http://144.124.251.24:10104 | NL | 761 | 6 | 34/44 |
| http://144.124.251.24:10176 | NL | 908 | 6 | 38/60 |
| http://144.124.251.24:10185 | NL | 912 | 6 | 35/44 |
| http://144.124.251.24:10187 | NL | 2790 | 6 | 34/58 |
| http://144.124.251.24:10216 | NL | 818 | 6 | 39/61 |
| http://144.124.251.24:10226 | NL | 816 | 6 | 33/43 |
| http://144.124.251.24:10230 | NL | 3357 | 6 | 37/59 |
| http://144.124.251.24:10261 | NL | 964 | 6 | 34/44 |
| http://144.124.251.24:10299 | NL | 967 | 6 | 33/44 |
| http://144.124.251.24:10333 | NL | 972 | 6 | 37/61 |
| http://144.124.251.24:10337 | NL | 717 | 6 | 32/44 |
| http://144.124.251.24:10346 | NL | 706 | 6 | 35/44 |
| http://144.124.251.24:10366 | NL | 1357 | 6 | 35/58 |
| http://144.124.251.24:10372 | NL | 1167 | 6 | 38/56 |
| http://144.124.251.24:10412 | NL | 781 | 6 | 34/44 |
| http://144.124.251.24:10431 | NL | 1761 | 6 | 40/60 |
| http://144.124.251.24:10453 | NL | 932 | 6 | 37/49 |
| http://144.124.251.24:10471 | NL | 4883 | 6 | 38/59 |
| http://144.124.251.24:10485 | NL | 705 | 6 | 31/44 |
| http://144.124.251.24:10551 | NL | 2747 | 6 | 39/60 |
| http://144.124.251.24:10566 | NL | 678 | 6 | 35/45 |
| http://144.124.251.24:10574 | NL | 2958 | 6 | 39/61 |
| http://144.124.251.24:10601 | NL | 2892 | 6 | 32/59 |
| http://144.124.251.24:10605 | NL | 676 | 6 | 34/44 |
| http://144.124.251.24:10610 | NL | 3057 | 6 | 34/44 |
| http://144.124.251.24:10628 | NL | 925 | 6 | 32/44 |
| http://144.124.251.24:10631 | NL | 906 | 6 | 34/44 |
| http://144.124.251.24:10658 | NL | 757 | 6 | 34/44 |
| http://144.124.251.24:10689 | NL | 1361 | 6 | 35/48 |
| http://144.124.251.24:10771 | NL | 819 | 6 | 34/44 |
| http://144.124.251.24:10800 | NL | 745 | 6 | 34/44 |
| http://144.124.251.24:10801 | NL | 2841 | 6 | 35/60 |
| http://144.124.251.24:10811 | NL | 806 | 6 | 34/44 |
| http://144.124.251.24:10818 | NL | 1027 | 6 | 31/44 |
| http://144.124.251.24:10829 | NL | 705 | 6 | 32/44 |
| http://144.124.251.24:10953 | NL | 776 | 6 | 35/44 |
| http://144.124.251.24:11011 | NL | 1309 | 6 | 35/44 |
| http://144.124.251.24:11108 | NL | 2421 | 6 | 35/59 |
| http://144.124.251.24:11124 | NL | 1186 | 6 | 36/61 |
| http://144.124.251.24:11180 | NL | 759 | 6 | 33/43 |
| http://144.124.251.24:11265 | NL | 935 | 6 | 38/60 |
| http://144.124.251.24:11266 | NL | 768 | 6 | 35/44 |
| http://144.124.251.24:11274 | NL | 903 | 6 | 38/60 |
| http://144.124.251.24:11450 | NL | 779 | 6 | 32/44 |
| http://144.124.251.24:11480 | NL | 755 | 6 | 33/44 |
| http://144.124.251.24:11491 | NL | 1147 | 6 | 38/60 |
| http://154.59.56.72:999 | VE | 3285 | 6 | 49/71 |
| http://213.131.85.26:1981 | ?? | 6324 | 6 | 6/6 |
| http://168.194.34.196:9001 | AR | 2290 | 5 | 39/110 |
| http://38.7.195.50:999 | CL | 2509 | 5 | 37/71 |
| http://45.71.186.210:999 | EC | 4490 | 5 | 28/86 |
| http://190.12.150.244:999 | EC | 3151 | 5 | 77/108 |
| http://41.128.77.76:1981 | EG | 1973 | 5 | 29/66 |
| http://3.1.100.245:3128 | SG | 1189 | 5 | 18/24 |
| http://44.216.27.249:3128 | US | 83 | 5 | 8/9 |
| http://200.59.191.27:999 | VE | 3420 | 5 | 70/107 |
| http://200.128.84.82:3128 | ?? | 704 | 5 | 5/5 |
| socks5://103.75.118.84:1080 | JP | 1043 | 5 | 77/107 |
| http://38.7.195.55:999 | CL | 3183 | 4 | 35/86 |
| http://177.234.221.194:999 | EC | 3226 | 4 | 8/11 |
| http://205.235.1.34:999 | EC | 4188 | 4 | 12/21 |
| http://45.240.232.61:8080 | EG | 5101 | 4 | 37/92 |
| http://43.155.62.157:443 | HK | 1042 | 4 | 13/15 |
| http://103.156.75.41:8080 | ID | 7216 | 4 | 7/30 |
| http://51.170.133.249:80 | MA | 2554 | 4 | 18/35 |
