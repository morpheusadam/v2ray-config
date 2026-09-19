# Proxy status

Generated 2026-09-19T16:26:10Z by `harvest.py`.

- **1610** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2824** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **28949** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 161/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1448 |
| http | 1371 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 1230 |
| ID | 337 |
| US | 116 |
| CN | 96 |
| RU | 78 |
| PH | 65 |
| DE | 63 |
| MX | 60 |
| SG | 56 |
| CO | 49 |
| BD | 46 |
| VE | 46 |
| VN | 39 |
| IN | 36 |
| TH | 36 |
| EG | 32 |
| BR | 30 |
| FR | 29 |
| HK | 28 |
| DO | 24 |
| EC | 24 |
| AR | 20 |
| TR | 20 |
| FI | 18 |
| CL | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-09-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 45 | 45 | 21 | 2026-09-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 54 | 54 | 23 | 2026-09-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 63 | 63 | 10 | 2026-09-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-09-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 109 | 109 | 41 | 2026-09-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 91 | 2026-09-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 213 | 213 | 70 | 2026-09-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 258 | 258 | 162 | 2026-09-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 428 | 428 | 81 | 2026-09-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-09-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-09-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1612 | 2026-09-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1932 | 1928 | 538 | 2026-09-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2095 | 2094 | 725 | 2026-09-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2203 | 2202 | 1656 | 2026-09-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2598 | 2597 | 862 | 2026-09-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 13776 | 13776 | 8197 | 2026-09-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 19219 | 19218 | 2285 | 2026-09-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 2080 | 72 | 77/80 |
| http://34.43.46.91:80 | US | 1293 | 72 | 77/80 |
| http://95.211.174.135:3128 | NL | 1807 | 66 | 79/80 |
| http://185.200.188.234:10001 | RU | 2804 | 66 | 79/80 |
| http://130.110.103.245:3128 | SA | 2069 | 66 | 78/80 |
| http://1.231.81.166:3128 | KR | 2913 | 45 | 77/80 |
| http://190.97.236.128:999 | VE | 1955 | 37 | 68/70 |
| http://190.97.236.129:999 | VE | 815 | 37 | 68/70 |
| http://95.3.69.222:8080 | TR | 1810 | 35 | 77/80 |
| socks5://107.167.18.122:443 | US | 1353 | 25 | 31/32 |
| socks5://83.147.216.208:1080 | FI | 1070 | 24 | 30/48 |
| http://184.75.221.82:3118 | CA | 219 | 21 | 42/45 |
| http://91.134.141.4:3128 | FR | 652 | 19 | 39/41 |
| http://186.5.94.206:999 | EC | 2356 | 17 | 40/42 |
| http://107.150.41.226:18080 | US | 207 | 17 | 17/17 |
| http://186.33.45.219:999 | EC | 2040 | 13 | 43/69 |
| http://38.51.207.104:8080 | VE | 615 | 13 | 20/21 |
| http://197.224.185.3:3128 | MU | 1802 | 11 | 44/48 |
| http://189.51.168.164:999 | MX | 492 | 11 | 44/45 |
| http://45.132.252.25:49156 | RU | 910 | 11 | 11/11 |
| http://5.129.254.5:8888 | RU | 1177 | 10 | 33/35 |
| http://5.129.254.49:8888 | RU | 1045 | 10 | 34/35 |
| http://5.129.254.51:8888 | RU | 1099 | 10 | 34/35 |
| http://5.129.254.60:8888 | RU | 1081 | 10 | 33/34 |
| http://5.129.254.70:8888 | RU | 1127 | 10 | 34/35 |
| http://5.129.254.129:8888 | RU | 1089 | 10 | 39/41 |
| http://5.129.254.154:8888 | RU | 1111 | 10 | 30/31 |
| http://193.104.179.115:3128 | UZ | 1523 | 10 | 28/45 |
| http://120.232.115.170:17981 | CN | 2201 | 9 | 58/79 |
| http://190.0.246.213:4040 | CO | 679 | 9 | 38/45 |
| http://213.111.146.36:18080 | NL | 1557 | 9 | 12/17 |
| http://157.85.108.47:3128 | TH | 1206 | 9 | 37/48 |
| socks5://101.36.104.46:10808 | JP | 2411 | 9 | 71/80 |
| socks5://121.169.46.116:1090 | KR | 4559 | 8 | 53/80 |
| http://45.186.6.104:3128 | EC | 738 | 7 | 56/58 |
| http://77.73.68.222:65000 | RU | 1034 | 7 | 7/7 |
| http://61.91.162.126:8080 | TH | 1378 | 7 | 20/23 |
| http://103.10.231.189:8080 | TH | 1606 | 7 | 45/65 |
| http://153.51.201.35:999 | VE | 848 | 7 | 7/7 |
| http://154.3.76.14:999 | VE | 688 | 7 | 24/33 |
| http://210.211.113.33:80 | VN | 2288 | 7 | 29/50 |
| http://8.138.217.152:21001 | CN | 7416 | 6 | 55/80 |
| http://36.155.23.163:10808 | CN | 1096 | 6 | 11/17 |
| http://123.121.123.216:8888 | CN | 1694 | 6 | 15/40 |
| http://176.111.37.216:39811 | HK | 1839 | 6 | 66/80 |
| http://38.194.246.34:999 | MX | 6715 | 6 | 43/71 |
| http://152.42.177.32:8888 | SG | 1054 | 6 | 22/40 |
| http://201.71.2.24:999 | VE | 2142 | 6 | 25/68 |
| http://201.71.2.25:999 | VE | 5005 | 6 | 21/67 |
| http://201.71.2.27:999 | VE | 4661 | 6 | 27/78 |
| http://18.157.123.132:3128 | DE | 640 | 5 | 29/41 |
| http://177.234.217.237:999 | EC | 3045 | 5 | 22/53 |
| http://41.33.245.138:1981 | EG | 3536 | 5 | 6/10 |
| http://203.177.217.222:8082 | PH | 7195 | 5 | 14/25 |
| http://124.156.194.52:8081 | SG | 3123 | 5 | 12/15 |
| http://190.97.229.118:999 | VE | 6614 | 5 | 35/70 |
| http://190.97.241.106:999 | VE | 3591 | 5 | 40/64 |
| http://103.102.131.30:3128 | VN | 4744 | 5 | 5/5 |
| socks5://45.74.31.41:15538 | NL | 2946 | 5 | 5/5 |
| socks5://193.233.223.47:1080 | RU | 3228 | 5 | 5/5 |
| socks5://162.120.16.210:1080 | US | 317 | 5 | 14/28 |
| http://103.106.119.217:8080 | BD | 5503 | 4 | 4/4 |
| http://103.177.118.145:8118 | BD | 3693 | 4 | 56/61 |
| http://38.7.195.51:999 | CL | 3912 | 4 | 23/71 |
| http://2.27.63.250:8118 | DE | 707 | 4 | 15/30 |
| http://103.237.102.191:11111 | DE | 1587 | 4 | 75/80 |
| http://177.234.217.235:999 | EC | 5041 | 4 | 28/49 |
| http://37.59.125.131:8888 | FR | 7104 | 4 | 63/80 |
| http://176.111.37.5:39811 | HK | 1342 | 4 | 73/80 |
| http://103.53.79.198:8050 | ID | 2473 | 4 | 6/18 |
| http://205.164.192.115:999 | MX | 5770 | 4 | 49/78 |
| http://144.124.251.24:10000 | NL | 3189 | 4 | 12/26 |
| http://144.124.251.24:10007 | NL | 3337 | 4 | 11/29 |
| http://144.124.251.24:10008 | NL | 719 | 4 | 7/11 |
| http://144.124.251.24:10084 | NL | 4198 | 4 | 8/12 |
| http://144.124.251.24:10104 | NL | 2322 | 4 | 7/12 |
| http://144.124.251.24:10176 | NL | 2492 | 4 | 11/28 |
| http://144.124.251.24:10185 | NL | 2167 | 4 | 8/12 |
| http://144.124.251.24:10216 | NL | 2572 | 4 | 12/29 |
| http://144.124.251.24:10226 | NL | 1002 | 4 | 6/11 |
| http://144.124.251.24:10261 | NL | 2049 | 4 | 8/12 |
| http://144.124.251.24:10299 | NL | 1199 | 4 | 8/12 |
| http://144.124.251.24:10333 | NL | 1314 | 4 | 10/29 |
| http://144.124.251.24:10337 | NL | 1577 | 4 | 8/12 |
| http://144.124.251.24:10346 | NL | 2382 | 4 | 8/12 |
| http://144.124.251.24:10366 | NL | 2025 | 4 | 9/26 |
| http://144.124.251.24:10372 | NL | 2820 | 4 | 11/24 |
| http://144.124.251.24:10412 | NL | 2223 | 4 | 8/12 |
| http://144.124.251.24:10431 | NL | 966 | 4 | 13/28 |
| http://144.124.251.24:10453 | NL | 2328 | 4 | 10/17 |
| http://144.124.251.24:10471 | NL | 992 | 4 | 12/27 |
| http://144.124.251.24:10485 | NL | 2284 | 4 | 7/12 |
| http://144.124.251.24:10551 | NL | 3005 | 4 | 12/28 |
| http://144.124.251.24:10566 | NL | 1886 | 4 | 9/13 |
| http://144.124.251.24:10574 | NL | 945 | 4 | 12/29 |
| http://144.124.251.24:10601 | NL | 2107 | 4 | 9/27 |
| http://144.124.251.24:10605 | NL | 1142 | 4 | 8/12 |
| http://144.124.251.24:10610 | NL | 1039 | 4 | 8/12 |
| http://144.124.251.24:10628 | NL | 4826 | 4 | 7/12 |
| http://144.124.251.24:10631 | NL | 1323 | 4 | 8/12 |
