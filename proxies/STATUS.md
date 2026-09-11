# Proxy status

Generated 2026-09-11T17:08:41Z by `harvest.py`.

- **794** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1971** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16609** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 137/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1533 |
| socks5 | 420 |
| socks4 | 18 |

| country | entries |
|---|---|
| ID | 451 |
| NL | 182 |
| CN | 109 |
| US | 95 |
| CO | 84 |
| MX | 78 |
| BD | 76 |
| PH | 71 |
| RU | 64 |
| BR | 53 |
| VE | 52 |
| IN | 44 |
| DE | 41 |
| EC | 36 |
| VN | 36 |
| SG | 30 |
| DO | 29 |
| FR | 27 |
| KH | 24 |
| TR | 23 |
| AR | 22 |
| EG | 22 |
| TH | 20 |
| HK | 19 |
| CL | 18 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 49 | 49 | 22 | 2026-09-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 118 | 118 | 69 | 2026-09-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-09-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 179 | 179 | 66 | 2026-09-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 207 | 207 | 117 | 2026-09-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 217 | 217 | 84 | 2026-09-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 258 | 258 | 98 | 2026-09-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 273 | 273 | 111 | 2026-09-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 433 | 433 | 148 | 2026-09-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-09-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1393 | 1389 | 419 | 2026-09-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1134 | 2026-09-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1604 | 2026-09-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2040 | 2038 | 272 | 2026-09-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2308 | 2308 | 1656 | 2026-09-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2424 | 2422 | 703 | 2026-09-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2660 | 2658 | 2058 | 2026-09-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 526 | 56 | 61/64 |
| http://34.43.46.91:80 | US | 889 | 56 | 61/64 |
| http://95.211.174.135:3128 | NL | 1992 | 50 | 63/64 |
| http://185.200.188.234:10001 | RU | 1495 | 50 | 63/64 |
| http://130.110.103.245:3128 | SA | 1746 | 50 | 62/64 |
| http://1.231.81.166:3128 | KR | 1362 | 29 | 61/64 |
| http://189.51.168.164:999 | MX | 1583 | 29 | 29/29 |
| socks5://193.25.215.182:22222 | US | 1241 | 27 | 60/64 |
| http://176.111.37.5:39811 | HK | 1826 | 24 | 58/64 |
| http://181.78.23.187:999 | CO | 712 | 21 | 31/33 |
| http://181.78.74.252:999 | CO | 869 | 21 | 53/55 |
| http://181.78.74.253:999 | CO | 811 | 21 | 53/55 |
| http://190.97.236.128:999 | VE | 754 | 21 | 52/54 |
| http://190.97.236.129:999 | VE | 823 | 21 | 52/54 |
| http://103.177.118.145:8118 | BD | 2369 | 20 | 43/45 |
| http://176.111.37.216:39811 | HK | 1449 | 19 | 52/64 |
| http://5.129.254.49:8888 | RU | 1097 | 19 | 19/19 |
| http://5.129.254.51:8888 | RU | 1091 | 19 | 19/19 |
| http://5.129.254.70:8888 | RU | 1057 | 19 | 19/19 |
| http://95.3.69.222:8080 | TR | 2041 | 19 | 61/64 |
| http://5.129.254.60:8888 | RU | 1144 | 18 | 18/18 |
| http://5.129.254.5:8888 | RU | 1102 | 17 | 18/19 |
| http://190.97.241.106:999 | VE | 6736 | 16 | 25/48 |
| http://5.129.254.154:8888 | RU | 1115 | 15 | 15/15 |
| socks5://108.174.152.80:1080 | MX | 401 | 13 | 13/13 |
| http://45.186.6.104:3128 | EC | 671 | 12 | 41/42 |
| http://43.99.60.244:8089 | HK | 1040 | 12 | 13/14 |
| http://52.21.158.119:3128 | US | 230 | 12 | 16/17 |
| http://190.0.246.211:4040 | CO | 3335 | 11 | 55/64 |
| http://103.157.200.126:3128 | PK | 2398 | 11 | 17/41 |
| http://34.88.38.81:9443 | FI | 2085 | 9 | 20/29 |
| http://37.59.125.131:8888 | FR | 1956 | 9 | 50/64 |
| http://107.167.18.122:443 | US | 254 | 9 | 15/16 |
| http://210.211.113.34:80 | VN | 3489 | 9 | 31/36 |
| http://103.237.102.191:11111 | DE | 2019 | 8 | 60/64 |
| socks5://83.147.216.208:1080 | FI | 4204 | 8 | 14/32 |
| http://61.91.162.126:8080 | TH | 1365 | 7 | 7/7 |
| http://103.10.231.189:8080 | TH | 1791 | 7 | 32/49 |
| http://190.0.246.213:4040 | CO | 6168 | 6 | 26/29 |
| http://167.233.169.253:1084 | DE | 4691 | 6 | 12/13 |
| http://43.156.236.238:80 | SG | 1015 | 6 | 29/62 |
| http://201.71.2.26:999 | VE | 5802 | 6 | 20/57 |
| socks5://144.91.111.48:1088 | FR | 3829 | 6 | 34/64 |
| socks5://101.36.104.46:10808 | JP | 2362 | 6 | 57/64 |
| socks5://203.189.150.44:1080 | KH | 4847 | 6 | 24/64 |
| socks5://45.32.160.61:1088 | US | 515 | 6 | 16/17 |
| http://108.61.213.218:80 | AU | 1103 | 5 | 5/5 |
| http://184.75.221.82:3118 | CA | 309 | 5 | 26/29 |
| http://113.45.195.147:3128 | CN | 1570 | 5 | 18/29 |
| http://45.65.138.48:999 | CO | 5169 | 5 | 21/64 |
| http://41.33.219.140:1981 | EG | 4320 | 5 | 18/46 |
| http://5.129.254.129:8888 | RU | 1236 | 5 | 24/25 |
| http://38.51.207.104:8080 | VE | 6072 | 5 | 5/5 |
| http://154.59.56.72:999 | VE | 6211 | 5 | 16/23 |
| socks5://5.45.119.70:1080 | EE | 2921 | 5 | 32/62 |
| socks5://144.91.121.61:1088 | FR | 4518 | 5 | 55/64 |
| socks5://178.130.47.21:1082 | US | 524 | 5 | 31/63 |
| http://111.200.188.89:8888 | CN | 1312 | 4 | 13/26 |
| http://120.232.115.170:17981 | CN | 1610 | 4 | 44/63 |
| http://179.1.221.26:3128 | CO | 4773 | 4 | 4/4 |
| http://190.0.246.210:4040 | CO | 3040 | 4 | 56/63 |
| http://41.33.245.139:1981 | EG | 5296 | 4 | 6/7 |
| http://103.130.61.61:8081 | ID | 1533 | 4 | 52/64 |
| http://115.178.53.114:8080 | ID | 7135 | 4 | 12/60 |
| http://197.224.185.3:3128 | MU | 1847 | 4 | 29/32 |
| http://201.71.2.24:999 | VE | 4984 | 4 | 15/52 |
| http://201.71.2.25:999 | VE | 5257 | 4 | 11/51 |
| socks5://118.179.93.24:9090 | BD | 1840 | 4 | 8/12 |
| socks5://45.95.202.92:10808 | RU | 1356 | 4 | 14/42 |
| socks5://67.207.92.87:1088 | US | 471 | 4 | 34/63 |
| socks5://141.148.158.143:1080 | US | 1682 | 4 | 33/63 |
| http://177.136.86.155:999 | AR | 7113 | 3 | 6/19 |
| http://118.179.167.238:55 | BD | 4736 | 3 | 8/33 |
| http://38.7.195.50:999 | CL | 3565 | 3 | 11/23 |
| http://61.149.135.125:8888 | CN | 3715 | 3 | 10/24 |
| http://101.251.204.174:8080 | CN | 1942 | 3 | 25/50 |
| http://114.254.49.43:8888 | CN | 6031 | 3 | 7/11 |
| http://119.188.131.55:17981 | CN | 2560 | 3 | 24/64 |
| http://123.121.208.63:8888 | CN | 3210 | 3 | 5/10 |
| http://181.78.25.253:999 | CO | 6085 | 3 | 18/59 |
| http://186.180.20.18:8080 | CO | 1875 | 3 | 15/58 |
| http://190.113.249.14:88 | CR | 5595 | 3 | 13/37 |
| http://185.27.144.53:999 | DO | 2032 | 3 | 5/33 |
| http://190.12.150.244:999 | EC | 3663 | 3 | 39/60 |
| http://41.128.72.197:1976 | EG | 5059 | 3 | 5/11 |
| http://91.134.141.4:3128 | FR | 740 | 3 | 23/25 |
| http://103.147.134.33:8082 | ID | 5591 | 3 | 6/19 |
| http://103.160.205.244:8181 | ID | 5017 | 3 | 4/10 |
| http://103.167.170.70:1111 | ID | 3770 | 3 | 9/62 |
| http://103.173.138.35:8080 | ID | 5229 | 3 | 3/3 |
| http://168.144.117.43:3129 | IN | 1570 | 3 | 9/14 |
| http://120.28.139.2:8082 | PH | 7762 | 3 | 14/60 |
| http://122.3.77.27:8082 | PH | 3876 | 3 | 8/53 |
| http://185.238.238.21:58080 | PL | 2226 | 3 | 8/28 |
| http://185.238.238.141:58080 | PL | 4617 | 3 | 15/62 |
| http://43.156.227.68:80 | SG | 1217 | 3 | 19/29 |
| http://157.85.111.64:3128 | TH | 2233 | 3 | 26/32 |
| http://195.158.8.123:3128 | UZ | 3241 | 3 | 41/62 |
| http://38.172.160.16:999 | VE | 4062 | 3 | 10/15 |
| http://154.59.56.76:999 | VE | 3194 | 3 | 19/24 |
