# Proxy status

Generated 2026-09-10T21:52:42Z by `harvest.py`.

- **839** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2227** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16447** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 183/600 (30%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1915 |
| socks5 | 293 |
| socks4 | 19 |

| country | entries |
|---|---|
| ID | 521 |
| US | 136 |
| CO | 102 |
| MX | 99 |
| CN | 90 |
| PH | 84 |
| BD | 77 |
| NL | 71 |
| RU | 64 |
| BR | 60 |
| IN | 58 |
| VE | 53 |
| DE | 52 |
| EC | 40 |
| FR | 38 |
| HK | 37 |
| VN | 35 |
| SG | 34 |
| TR | 31 |
| DO | 29 |
| JP | 28 |
| AR | 27 |
| TH | 27 |
| CL | 23 |
| EG | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 88 | 88 | 37 | 2026-09-10 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 107 | 107 | 23 | 2026-09-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 130 | 130 | 69 | 2026-09-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 146 | 146 | 39 | 2026-09-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-09-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 264 | 264 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 283 | 283 | 62 | 2026-09-10 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 567 | 567 | 190 | 2026-09-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 589 | 589 | 261 | 2026-09-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-09-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1124 | 2026-09-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-09-10 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1968 | 1964 | 466 | 2026-09-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2237 | 2235 | 201 | 2026-09-10 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2572 | 2572 | 1459 | 2026-09-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2694 | 2692 | 732 | 2026-09-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3054 | 3052 | 2315 | 2026-09-10 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1961 | 55 | 60/63 |
| http://34.43.46.91:80 | US | 1954 | 55 | 60/63 |
| http://95.211.174.135:3128 | NL | 1374 | 49 | 62/63 |
| http://185.200.188.234:10001 | RU | 1186 | 49 | 62/63 |
| http://130.110.103.245:3128 | SA | 1347 | 49 | 61/63 |
| http://64.112.184.210:3128 | US | 1405 | 41 | 62/63 |
| http://1.231.81.166:3128 | KR | 1178 | 28 | 60/63 |
| http://189.51.168.164:999 | MX | 466 | 28 | 28/28 |
| socks5://193.25.215.182:22222 | US | 1902 | 26 | 59/63 |
| http://176.111.37.5:39811 | HK | 1384 | 23 | 57/63 |
| http://181.78.23.187:999 | CO | 814 | 20 | 30/32 |
| http://181.78.74.252:999 | CO | 762 | 20 | 52/54 |
| http://181.78.74.253:999 | CO | 736 | 20 | 52/54 |
| http://190.97.236.128:999 | VE | 744 | 20 | 51/53 |
| http://190.97.236.129:999 | VE | 677 | 20 | 51/53 |
| http://103.177.118.145:8118 | BD | 2671 | 19 | 42/44 |
| http://176.111.37.216:39811 | HK | 1340 | 18 | 51/63 |
| http://5.129.254.49:8888 | RU | 1263 | 18 | 18/18 |
| http://5.129.254.51:8888 | RU | 1200 | 18 | 18/18 |
| http://5.129.254.70:8888 | RU | 1243 | 18 | 18/18 |
| http://95.3.69.222:8080 | TR | 1694 | 18 | 60/63 |
| http://5.129.254.60:8888 | RU | 1195 | 17 | 17/17 |
| http://5.129.254.5:8888 | RU | 1216 | 16 | 17/18 |
| http://190.97.241.106:999 | VE | 3935 | 15 | 24/47 |
| http://5.129.254.154:8888 | RU | 1121 | 14 | 14/14 |
| socks5://108.174.152.80:1080 | MX | 409 | 12 | 12/12 |
| http://45.186.6.104:3128 | EC | 812 | 11 | 40/41 |
| http://43.99.60.244:8089 | HK | 1060 | 11 | 12/13 |
| http://52.21.158.119:3128 | US | 215 | 11 | 15/16 |
| socks5://58.187.162.191:1083 | VN | 2505 | 11 | 11/11 |
| http://190.0.246.211:4040 | CO | 1603 | 10 | 54/63 |
| http://103.157.200.126:3128 | PK | 2360 | 10 | 16/40 |
| http://213.131.85.29:1981 | EG | 1045 | 8 | 8/8 |
| http://34.88.38.81:9443 | FI | 708 | 8 | 19/28 |
| http://37.59.125.131:8888 | FR | 2811 | 8 | 49/63 |
| http://107.167.18.122:443 | US | 1387 | 8 | 14/15 |
| http://210.211.113.34:80 | VN | 2534 | 8 | 30/35 |
| socks5://147.45.60.139:1082 | US | 3308 | 8 | 35/54 |
| http://103.237.102.191:11111 | DE | 1176 | 7 | 59/63 |
| socks5://83.147.216.208:1080 | FI | 1480 | 7 | 13/31 |
| http://61.91.162.126:8080 | TH | 1366 | 6 | 6/6 |
| http://103.10.231.189:8080 | TH | 1473 | 6 | 31/48 |
| http://69.87.216.54:7989 | US | 224 | 6 | 7/8 |
| http://190.0.246.213:4040 | CO | 3453 | 5 | 25/28 |
| http://167.233.169.253:1084 | DE | 5602 | 5 | 11/12 |
| http://38.44.17.142:999 | DO | 2402 | 5 | 29/56 |
| http://213.131.85.29:1976 | EG | 1027 | 5 | 7/8 |
| http://43.156.236.238:80 | SG | 1036 | 5 | 28/61 |
| http://195.158.22.212:3128 | UZ | 1902 | 5 | 8/22 |
| http://201.71.2.26:999 | VE | 5356 | 5 | 19/56 |
| socks5://81.0.49.104:18500 | ES | 3513 | 5 | 22/60 |
| socks5://85.117.248.36:1080 | ES | 3146 | 5 | 9/48 |
| socks5://144.91.111.48:1088 | FR | 5340 | 5 | 33/63 |
| socks5://101.36.104.46:10808 | JP | 3540 | 5 | 56/63 |
| socks5://203.189.150.44:1080 | KH | 3138 | 5 | 23/63 |
| socks5://45.32.160.61:1088 | US | 424 | 5 | 15/16 |
| http://108.61.213.218:80 | AU | 1926 | 4 | 4/4 |
| http://184.75.221.82:3118 | CA | 236 | 4 | 25/28 |
| http://113.45.195.147:3128 | CN | 1593 | 4 | 17/28 |
| http://45.65.138.48:999 | CO | 7940 | 4 | 20/63 |
| http://41.33.219.140:1981 | EG | 7900 | 4 | 17/45 |
| http://144.79.75.222:8080 | ID | 5550 | 4 | 9/45 |
| http://5.129.254.129:8888 | RU | 2299 | 4 | 23/24 |
| http://193.104.179.115:3128 | UZ | 1752 | 4 | 16/28 |
| http://38.51.207.104:8080 | VE | 671 | 4 | 4/4 |
| http://154.59.56.72:999 | VE | 1952 | 4 | 15/22 |
| http://154.59.56.73:999 | VE | 6763 | 4 | 31/35 |
| http://103.218.122.183:8080 | VN | 1364 | 4 | 18/34 |
| http://116.104.54.38:2080 | VN | 1880 | 4 | 4/4 |
| http://210.211.113.33:80 | VN | 2654 | 4 | 18/33 |
| socks5://5.45.119.70:1080 | EE | 2520 | 4 | 31/61 |
| socks5://144.91.121.61:1088 | FR | 3483 | 4 | 54/63 |
| socks5://101.36.104.239:10808 | JP | 1297 | 4 | 52/63 |
| socks5://195.114.7.6:1080 | UA | 6804 | 4 | 14/43 |
| socks5://178.130.47.21:1082 | US | 4461 | 4 | 30/62 |
| http://182.160.124.174:9669 | BD | 5430 | 3 | 13/62 |
| http://45.175.44.4:80 | BR | 5868 | 3 | 8/60 |
| http://138.122.140.194:3128 | BR | 5340 | 3 | 19/57 |
| http://186.67.94.10:999 | CL | 7411 | 3 | 8/58 |
| http://111.200.188.89:8888 | CN | 2996 | 3 | 12/25 |
| http://120.232.115.170:17981 | CN | 1615 | 3 | 43/62 |
| http://221.221.154.122:8888 | CN | 1345 | 3 | 7/16 |
| http://45.172.218.67:3028 | CO | 4527 | 3 | 27/53 |
| http://179.1.221.26:3128 | CO | 678 | 3 | 3/3 |
| http://190.0.246.210:4040 | CO | 3440 | 3 | 55/62 |
| http://167.233.169.253:1082 | DE | 2582 | 3 | 10/12 |
| http://177.234.217.88:999 | EC | 4883 | 3 | 17/55 |
| http://41.33.245.139:1976 | EG | 3172 | 3 | 5/8 |
| http://41.33.245.139:1981 | EG | 1087 | 3 | 5/6 |
| http://197.164.101.13:1976 | EG | 7177 | 3 | 7/16 |
| http://103.130.61.61:8081 | ID | 4918 | 3 | 51/63 |
| http://103.156.233.137:8080 | ID | 6801 | 3 | 9/51 |
| http://115.178.53.114:8080 | ID | 6138 | 3 | 11/59 |
| http://49.156.44.115:8080 | KH | 5251 | 3 | 8/29 |
| http://197.224.185.3:3128 | MU | 1890 | 3 | 28/31 |
| http://38.194.246.34:999 | MX | 7311 | 3 | 31/54 |
| http://93.180.134.36:3128 | TR | 5685 | 3 | 3/3 |
| http://195.62.50.2:8080 | TR | 4422 | 3 | 7/12 |
| http://154.3.76.14:999 | VE | 2732 | 3 | 11/16 |
| http://190.97.226.89:999 | VE | 5645 | 3 | 10/36 |
