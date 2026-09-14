# Proxy status

Generated 2026-09-14T22:44:14Z by `harvest.py`.

- **733** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1432** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **20224** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 186/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 913 |
| socks5 | 509 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 327 |
| ID | 199 |
| US | 90 |
| CN | 78 |
| RU | 54 |
| CO | 47 |
| MX | 44 |
| VN | 44 |
| BD | 38 |
| DE | 37 |
| PH | 33 |
| SG | 33 |
| VE | 32 |
| BR | 30 |
| FR | 25 |
| EG | 23 |
| EC | 22 |
| IN | 22 |
| KH | 17 |
| AR | 12 |
| FI | 12 |
| HK | 12 |
| TH | 11 |
| IR | 10 |
| TR | 10 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-09-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 48 | 48 | 11 | 2026-09-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 58 | 58 | 30 | 2026-09-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 146 | 146 | 39 | 2026-09-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 83 | 2026-09-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 177 | 177 | 99 | 2026-09-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 185 | 185 | 72 | 2026-09-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 283 | 283 | 137 | 2026-09-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 398 | 398 | 142 | 2026-09-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-09-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-09-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-09-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-09-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1978 | 1974 | 232 | 2026-09-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2452 | 2450 | 276 | 2026-09-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2861 | 2859 | 715 | 2026-09-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2967 | 2965 | 2257 | 2026-09-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4176 | 4176 | 2867 | 2026-09-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10468 | 10467 | 2249 | 2026-09-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 368 | 63 | 68/71 |
| http://34.43.46.91:80 | US | 467 | 63 | 68/71 |
| http://95.211.174.135:3128 | NL | 1045 | 57 | 70/71 |
| http://185.200.188.234:10001 | RU | 1808 | 57 | 70/71 |
| http://130.110.103.245:3128 | SA | 1269 | 57 | 69/71 |
| http://1.231.81.166:3128 | KR | 1413 | 36 | 68/71 |
| http://176.111.37.5:39811 | HK | 1007 | 31 | 65/71 |
| http://181.78.23.187:999 | CO | 736 | 28 | 38/40 |
| http://181.78.74.252:999 | CO | 839 | 28 | 60/62 |
| http://181.78.74.253:999 | CO | 783 | 28 | 60/62 |
| http://190.97.236.128:999 | VE | 775 | 28 | 59/61 |
| http://190.97.236.129:999 | VE | 775 | 28 | 59/61 |
| http://95.3.69.222:8080 | TR | 1580 | 26 | 68/71 |
| http://190.97.241.106:999 | VE | 4540 | 23 | 32/55 |
| http://45.186.6.104:3128 | EC | 838 | 19 | 48/49 |
| http://107.167.18.122:443 | US | 3407 | 16 | 22/23 |
| http://103.237.102.191:11111 | DE | 795 | 15 | 67/71 |
| socks5://83.147.216.208:1080 | FI | 6086 | 15 | 21/39 |
| socks5://144.91.111.48:1088 | FR | 2003 | 13 | 41/71 |
| http://184.75.221.82:3118 | CA | 1421 | 12 | 33/36 |
| socks5://144.91.121.61:1088 | FR | 6963 | 12 | 62/71 |
| http://91.134.141.4:3128 | FR | 636 | 10 | 30/32 |
| socks5://51.178.49.241:1088 | FR | 4342 | 9 | 27/32 |
| http://186.5.94.206:999 | EC | 3930 | 8 | 31/33 |
| http://107.150.41.226:18080 | US | 376 | 8 | 8/8 |
| http://14.251.13.20:8080 | VN | 1235 | 8 | 41/43 |
| socks5://213.199.47.140:1080 | FR | 5170 | 8 | 30/37 |
| socks5://43.135.176.121:1080 | US | 2201 | 8 | 23/26 |
| http://165.154.162.73:8888 | US | 4697 | 7 | 41/71 |
| socks5://161.35.90.93:1083 | NL | 6554 | 7 | 36/69 |
| http://114.236.137.41:21000 | CN | 1721 | 6 | 49/71 |
| http://45.240.232.61:8080 | EG | 4671 | 6 | 19/51 |
| http://124.156.194.52:8081 | SG | 3810 | 6 | 6/6 |
| http://195.158.8.123:3128 | UZ | 5027 | 6 | 47/69 |
| socks5://191.223.220.23:1080 | JP | 1015 | 6 | 18/68 |
| http://8.138.217.152:21001 | CN | 2824 | 5 | 47/71 |
| http://103.177.118.145:8118 | BD | 5192 | 4 | 48/52 |
| http://114.254.49.43:8888 | CN | 1359 | 4 | 11/18 |
| http://190.0.246.210:4040 | CO | 2045 | 4 | 61/70 |
| http://186.33.45.219:999 | EC | 5738 | 4 | 34/60 |
| http://65.109.217.164:3128 | FI | 766 | 4 | 4/4 |
| http://84.8.216.230:2001 | MA | 723 | 4 | 4/4 |
| http://144.124.251.24:10230 | NL | 5161 | 4 | 7/18 |
| http://144.124.251.24:10453 | NL | 2346 | 4 | 5/8 |
| http://144.124.251.24:10566 | NL | 3720 | 4 | 4/4 |
| http://144.124.251.24:11124 | NL | 3645 | 4 | 6/20 |
| http://43.156.199.63:8080 | SG | 1814 | 4 | 5/6 |
| http://202.28.194.139:31280 | TH | 2135 | 4 | 64/71 |
| http://38.51.207.104:8080 | VE | 4723 | 4 | 11/12 |
| http://200.59.191.27:999 | VE | 3220 | 4 | 41/66 |
| http://210.211.113.34:80 | VN | 4408 | 4 | 36/43 |
| socks5://91.107.179.68:10809 | DE | 1426 | 4 | 4/4 |
| socks5://144.24.111.128:1088 | IN | 1619 | 4 | 54/71 |
| socks5://45.61.129.165:9050 | US | 2096 | 4 | 59/71 |
| socks5://118.70.82.27:1083 | VN | 1695 | 4 | 4/4 |
| http://45.65.138.48:999 | CO | 5007 | 3 | 26/71 |
| http://41.196.16.229:1976 | EG | 1139 | 3 | 3/3 |
| http://144.124.251.24:10000 | NL | 1014 | 3 | 7/17 |
| http://144.124.251.24:10007 | NL | 2229 | 3 | 6/20 |
| http://144.124.251.24:10082 | NL | 4395 | 3 | 6/19 |
| http://144.124.251.24:10084 | NL | 7156 | 3 | 3/3 |
| http://144.124.251.24:10088 | NL | 5094 | 3 | 3/3 |
| http://144.124.251.24:10185 | NL | 5244 | 3 | 3/3 |
| http://144.124.251.24:10187 | NL | 2461 | 3 | 4/17 |
| http://144.124.251.24:10216 | NL | 6357 | 3 | 7/20 |
| http://144.124.251.24:10261 | NL | 3454 | 3 | 3/3 |
| http://144.124.251.24:10299 | NL | 7715 | 3 | 3/3 |
| http://144.124.251.24:10333 | NL | 5492 | 3 | 5/20 |
| http://144.124.251.24:10337 | NL | 3609 | 3 | 3/3 |
| http://144.124.251.24:10346 | NL | 5116 | 3 | 3/3 |
| http://144.124.251.24:10366 | NL | 3651 | 3 | 4/17 |
| http://144.124.251.24:10412 | NL | 4852 | 3 | 3/3 |
| http://144.124.251.24:10431 | NL | 4592 | 3 | 8/19 |
| http://144.124.251.24:10471 | NL | 7935 | 3 | 7/18 |
| http://144.124.251.24:10485 | NL | 4334 | 3 | 3/3 |
| http://144.124.251.24:10574 | NL | 4704 | 3 | 7/20 |
| http://144.124.251.24:10601 | NL | 5287 | 3 | 4/18 |
| http://144.124.251.24:10605 | NL | 2211 | 3 | 3/3 |
| http://144.124.251.24:10610 | NL | 3516 | 3 | 3/3 |
| http://144.124.251.24:10631 | NL | 6103 | 3 | 3/3 |
| http://144.124.251.24:10658 | NL | 3851 | 3 | 3/3 |
| http://144.124.251.24:10689 | NL | 2274 | 3 | 4/7 |
| http://144.124.251.24:10800 | NL | 3152 | 3 | 3/3 |
| http://144.124.251.24:10811 | NL | 3119 | 3 | 3/3 |
| http://144.124.251.24:10829 | NL | 3134 | 3 | 3/3 |
| http://144.124.251.24:10953 | NL | 3227 | 3 | 3/3 |
| http://144.124.251.24:11011 | NL | 2480 | 3 | 3/3 |
| http://144.124.251.24:11108 | NL | 3635 | 3 | 4/18 |
| http://144.124.251.24:11265 | NL | 6790 | 3 | 6/19 |
| http://144.124.251.24:11266 | NL | 2064 | 3 | 3/3 |
| http://144.124.251.24:11274 | NL | 7068 | 3 | 6/19 |
| http://144.124.251.24:11491 | NL | 2591 | 3 | 6/19 |
| http://119.93.83.106:8082 | PH | 6929 | 3 | 3/3 |
| http://167.99.74.174:9090 | SG | 1088 | 3 | 16/31 |
| http://172.104.56.95:8888 | SG | 1435 | 3 | 3/3 |
| http://47.81.56.193:8888 | TH | 1597 | 3 | 41/71 |
| http://43.109.48.179:9999 | VN | 1493 | 3 | 21/69 |
| http://210.211.113.33:80 | VN | 3792 | 3 | 21/41 |
| socks4://58.187.104.62:1111 | VN | 1950 | 3 | 3/3 |
| socks5://103.210.161.8:1080 | CN | 1700 | 3 | 33/44 |
