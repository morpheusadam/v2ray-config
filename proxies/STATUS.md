# Proxy status

Generated 2026-08-18T19:55:01Z by `harvest.py`.

- **750** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1367** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13364** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 139/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1096 |
| socks5 | 247 |
| socks4 | 24 |

| country | entries |
|---|---|
| ID | 317 |
| US | 97 |
| CO | 63 |
| RU | 59 |
| PH | 58 |
| CN | 49 |
| MX | 43 |
| BD | 42 |
| TR | 38 |
| BR | 37 |
| VE | 33 |
| FR | 31 |
| DE | 28 |
| SG | 27 |
| NL | 26 |
| VN | 24 |
| EC | 22 |
| HK | 21 |
| JP | 21 |
| IN | 19 |
| KH | 19 |
| TH | 15 |
| AR | 14 |
| CL | 13 |
| DO | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 4 | 2026-08-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 82 | 82 | 49 | 2026-08-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 96 | 96 | 10 | 2026-08-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 130 | 130 | 72 | 2026-08-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 132 | 132 | 54 | 2026-08-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 97 | 2026-08-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 154 | 154 | 26 | 2026-08-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 170 | 170 | 12 | 2026-08-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 295 | 295 | 121 | 2026-08-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 404 | 404 | 180 | 2026-08-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-08-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-08-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1119 | 2026-08-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1613 | 2026-08-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1847 | 1845 | 165 | 2026-08-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1947 | 1943 | 466 | 2026-08-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2359 | 2357 | 677 | 2026-08-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2503 | 2501 | 2028 | 2026-08-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2686 | 2686 | 2150 | 2026-08-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1790 | 17 | 17/17 |
| http://64.112.184.210:3128 | US | 1514 | 17 | 17/17 |
| socks5://69.55.49.177:38182 | US | 1989 | 17 | 17/17 |
| http://181.39.25.196:8118 | EC | 1983 | 14 | 16/17 |
| http://190.0.246.210:4040 | CO | 674 | 13 | 15/16 |
| http://34.43.46.91:443 | US | 2083 | 9 | 14/17 |
| http://34.43.46.91:80 | US | 1298 | 9 | 14/17 |
| http://181.78.74.252:999 | CO | 878 | 8 | 8/8 |
| http://181.78.74.253:999 | CO | 814 | 8 | 8/8 |
| http://157.230.178.216:40000 | US | 3434 | 8 | 15/16 |
| http://190.97.236.128:999 | VE | 1911 | 7 | 7/7 |
| http://190.97.236.129:999 | VE | 1932 | 7 | 7/7 |
| http://186.33.45.219:999 | EC | 3261 | 6 | 6/6 |
| http://213.136.77.119:8888 | FR | 2195 | 5 | 5/5 |
| http://190.12.150.244:999 | EC | 6659 | 4 | 9/13 |
| http://49.51.253.118:8888 | US | 2720 | 4 | 4/4 |
| socks4://163.192.14.135:50161 | US | 1939 | 4 | 10/16 |
| socks5://147.45.60.250:1082 | US | 1206 | 4 | 7/17 |
| http://8.138.217.152:21001 | CN | 2482 | 3 | 10/17 |
| http://47.107.82.96:30051 | CN | 1837 | 3 | 8/10 |
| http://101.251.204.174:8080 | CN | 2916 | 3 | 3/3 |
| http://120.24.202.132:19000 | CN | 7628 | 3 | 6/11 |
| http://223.85.21.195:8080 | CN | 4759 | 3 | 8/15 |
| http://45.179.200.38:999 | CO | 6037 | 3 | 3/3 |
| http://103.237.102.191:11111 | DE | 1309 | 3 | 16/17 |
| http://80.78.128.94:8080 | ES | 1601 | 3 | 4/6 |
| http://37.59.125.131:8888 | FR | 1265 | 3 | 14/17 |
| http://191.44.125.11:8080 | FR | 3639 | 3 | 4/15 |
| http://212.58.132.5:8888 | GB | 1382 | 3 | 12/16 |
| http://176.111.37.5:39811 | HK | 1550 | 3 | 16/17 |
| http://176.111.37.216:39811 | HK | 2236 | 3 | 15/17 |
| http://103.61.16.92:8080 | ID | 2429 | 3 | 6/14 |
| http://103.110.100.25:1111 | ID | 5382 | 3 | 6/15 |
| http://103.147.134.114:8082 | ID | 6694 | 3 | 3/3 |
| http://103.172.42.193:1111 | ID | 4753 | 3 | 6/14 |
| http://103.172.70.203:8080 | ID | 3862 | 3 | 3/3 |
| http://103.176.96.32:8082 | ID | 6498 | 3 | 4/10 |
| http://103.176.97.57:8082 | ID | 3473 | 3 | 5/6 |
| http://103.178.3.140:8818 | ID | 3824 | 3 | 4/6 |
| http://103.236.143.55:8080 | ID | 3563 | 3 | 5/10 |
| http://117.236.124.166:3128 | IN | 2458 | 3 | 10/17 |
| http://1.231.81.166:3128 | KR | 1376 | 3 | 16/17 |
| http://94.131.92.155:3128 | KZ | 1381 | 3 | 9/15 |
| http://175.136.239.173:8181 | MY | 2519 | 3 | 13/17 |
| http://175.143.76.177:8181 | MY | 2828 | 3 | 14/17 |
| http://95.211.174.135:3128 | NL | 2975 | 3 | 16/17 |
| http://204.76.203.9:3128 | NL | 1266 | 3 | 16/17 |
| http://204.76.203.9:8080 | NL | 692 | 3 | 9/10 |
| http://161.49.90.70:1337 | PH | 5247 | 3 | 3/3 |
| http://185.141.26.131:3128 | RO | 656 | 3 | 3/3 |
| http://85.193.65.88:8888 | RU | 1572 | 3 | 6/7 |
| http://185.200.188.234:10001 | RU | 2355 | 3 | 16/17 |
| http://130.110.103.245:3128 | SA | 2699 | 3 | 15/17 |
| http://202.28.194.139:31280 | TH | 2958 | 3 | 16/17 |
| http://95.3.69.222:8080 | TR | 3871 | 3 | 16/17 |
| http://34.69.61.247:80 | US | 241 | 3 | 10/16 |
| http://45.66.249.187:3128 | US | 406 | 3 | 7/8 |
| http://45.66.249.187:8080 | US | 603 | 3 | 9/12 |
| http://45.66.249.187:8181 | US | 377 | 3 | 7/8 |
| http://42.96.18.62:1311 | VN | 1896 | 3 | 11/16 |
| socks4://45.61.129.165:9050 | US | 4185 | 3 | 14/17 |
| socks5://45.144.54.40:1080 | DE | 2874 | 3 | 11/17 |
| socks5://109.123.251.109:1080 | FR | 1181 | 3 | 8/17 |
| socks5://144.91.111.48:1088 | FR | 2668 | 3 | 14/17 |
| socks5://144.91.121.61:1088 | FR | 2665 | 3 | 16/17 |
| socks5://150.241.91.238:7777 | FR | 905 | 3 | 3/3 |
| socks5://212.58.132.5:1080 | GB | 2102 | 3 | 16/17 |
| socks5://45.194.33.12:30001 | HK | 1577 | 3 | 11/13 |
| socks5://152.32.168.221:10808 | HK | 7419 | 3 | 5/6 |
| socks5://144.24.111.128:1088 | IN | 2468 | 3 | 12/17 |
| socks5://85.198.82.207:1080 | RU | 5608 | 3 | 4/6 |
| socks5://178.128.82.131:10808 | SG | 4235 | 3 | 8/17 |
| socks5://43.130.38.45:51029 | US | 5799 | 3 | 5/15 |
| socks5://43.162.94.99:1080 | US | 5371 | 3 | 13/17 |
| socks5://193.25.215.182:22222 | US | 1965 | 3 | 16/17 |
| http://109.236.45.95:8989 | AL | 5303 | 2 | 4/13 |
| http://170.168.102.55:3128 | AM | 4841 | 2 | 3/8 |
| http://186.123.26.22:8080 | AR | 3214 | 2 | 2/2 |
| http://103.161.69.252:2698 | BD | 2280 | 2 | 7/17 |
| http://113.11.126.238:30226 | BD | 4773 | 2 | 5/16 |
| http://45.227.195.121:8082 | BR | 5357 | 2 | 2/2 |
| http://138.122.140.194:3128 | BR | 1367 | 2 | 4/11 |
| http://47.110.226.74:19991 | CN | 5571 | 2 | 6/15 |
| http://111.230.27.213:3128 | CN | 2977 | 2 | 9/17 |
| http://114.236.137.41:21000 | CN | 4612 | 2 | 11/17 |
| http://116.62.60.22:3128 | CN | 4046 | 2 | 2/2 |
| http://120.232.115.170:17981 | CN | 1480 | 2 | 7/16 |
| http://161.18.226.135:8080 | CO | 3300 | 2 | 3/13 |
| http://87.251.77.29:3128 | DE | 1559 | 2 | 15/17 |
| http://38.50.165.123:999 | DO | 6854 | 2 | 2/2 |
| http://38.255.121.1:999 | DO | 601 | 2 | 3/5 |
| http://41.128.90.50:1976 | EG | 4140 | 2 | 2/2 |
| http://41.196.16.233:1981 | EG | 1369 | 2 | 2/2 |
| http://13.38.217.179:29788 | FR | 3986 | 2 | 3/16 |
| http://43.99.100.108:3128 | HK | 1231 | 2 | 14/17 |
| http://41.216.186.74:8080 | ID | 5563 | 2 | 4/6 |
| http://45.198.10.43:8080 | ID | 3530 | 2 | 3/7 |
| http://45.198.32.207:8080 | ID | 5384 | 2 | 3/6 |
| http://45.198.33.147:8080 | ID | 3244 | 2 | 4/14 |
| http://103.50.25.13:8888 | ID | 6954 | 2 | 2/2 |
