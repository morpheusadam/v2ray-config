# Proxy status

Generated 2026-09-11T21:54:05Z by `harvest.py`.

- **827** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1651** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **17024** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 124/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1222 |
| socks5 | 418 |
| socks4 | 11 |

| country | entries |
|---|---|
| ID | 326 |
| NL | 191 |
| CN | 103 |
| US | 102 |
| CO | 63 |
| PH | 62 |
| MX | 60 |
| RU | 60 |
| BD | 57 |
| VE | 41 |
| BR | 40 |
| VN | 38 |
| DE | 35 |
| IN | 34 |
| EC | 28 |
| EG | 27 |
| DO | 26 |
| FR | 26 |
| KH | 25 |
| SG | 23 |
| HK | 21 |
| AR | 20 |
| TR | 18 |
| TH | 17 |
| CL | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-09-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 64 | 64 | 36 | 2026-09-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 108 | 108 | 48 | 2026-09-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-09-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 150 | 150 | 44 | 2026-09-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 159 | 159 | 45 | 2026-09-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 173 | 173 | 43 | 2026-09-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 223 | 223 | 70 | 2026-09-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 251 | 251 | 157 | 2026-09-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 417 | 417 | 125 | 2026-09-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-09-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-09-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-09-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1599 | 2026-09-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2007 | 2004 | 846 | 2026-09-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2013 | 2011 | 331 | 2026-09-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2276 | 2274 | 681 | 2026-09-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2348 | 2348 | 1699 | 2026-09-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2562 | 2560 | 2015 | 2026-09-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 498 | 57 | 62/65 |
| http://34.43.46.91:80 | US | 357 | 57 | 62/65 |
| http://95.211.174.135:3128 | NL | 1884 | 51 | 64/65 |
| http://185.200.188.234:10001 | RU | 1692 | 51 | 64/65 |
| http://130.110.103.245:3128 | SA | 1641 | 51 | 63/65 |
| http://1.231.81.166:3128 | KR | 2638 | 30 | 62/65 |
| http://189.51.168.164:999 | MX | 435 | 30 | 30/30 |
| http://176.111.37.5:39811 | HK | 747 | 25 | 59/65 |
| http://181.78.23.187:999 | CO | 659 | 22 | 32/34 |
| http://181.78.74.252:999 | CO | 815 | 22 | 54/56 |
| http://181.78.74.253:999 | CO | 743 | 22 | 54/56 |
| http://190.97.236.128:999 | VE | 892 | 22 | 53/55 |
| http://190.97.236.129:999 | VE | 837 | 22 | 53/55 |
| http://176.111.37.216:39811 | HK | 961 | 20 | 53/65 |
| http://5.129.254.49:8888 | RU | 1538 | 20 | 20/20 |
| http://5.129.254.51:8888 | RU | 2155 | 20 | 20/20 |
| http://5.129.254.70:8888 | RU | 1442 | 20 | 20/20 |
| http://95.3.69.222:8080 | TR | 2084 | 20 | 62/65 |
| http://5.129.254.60:8888 | RU | 1294 | 19 | 19/19 |
| http://5.129.254.5:8888 | RU | 1308 | 18 | 19/20 |
| http://190.97.241.106:999 | VE | 1792 | 17 | 26/49 |
| http://5.129.254.154:8888 | RU | 2814 | 16 | 16/16 |
| socks5://108.174.152.80:1080 | MX | 2120 | 14 | 14/14 |
| http://45.186.6.104:3128 | EC | 685 | 13 | 42/43 |
| http://43.99.60.244:8089 | HK | 1426 | 13 | 14/15 |
| http://52.21.158.119:3128 | US | 4552 | 13 | 17/18 |
| http://190.0.246.211:4040 | CO | 1579 | 12 | 56/65 |
| http://103.157.200.126:3128 | PK | 1346 | 12 | 18/42 |
| http://34.88.38.81:9443 | FI | 698 | 10 | 21/30 |
| http://37.59.125.131:8888 | FR | 2273 | 10 | 51/65 |
| http://107.167.18.122:443 | US | 2428 | 10 | 16/17 |
| http://103.237.102.191:11111 | DE | 1022 | 9 | 61/65 |
| socks5://83.147.216.208:1080 | FI | 1151 | 9 | 15/33 |
| http://61.91.162.126:8080 | TH | 1896 | 8 | 8/8 |
| http://103.10.231.189:8080 | TH | 1734 | 8 | 33/50 |
| http://167.233.169.253:1084 | DE | 4724 | 7 | 13/14 |
| http://201.71.2.26:999 | VE | 2460 | 7 | 21/58 |
| socks5://144.91.111.48:1088 | FR | 2282 | 7 | 35/65 |
| socks5://101.36.104.46:10808 | JP | 6511 | 7 | 58/65 |
| socks5://45.32.160.61:1088 | US | 1427 | 7 | 17/18 |
| http://108.61.213.218:80 | AU | 1289 | 6 | 6/6 |
| http://184.75.221.82:3118 | CA | 203 | 6 | 27/30 |
| http://113.45.195.147:3128 | CN | 1990 | 6 | 19/30 |
| http://45.65.138.48:999 | CO | 7780 | 6 | 22/65 |
| http://41.33.219.140:1981 | EG | 4037 | 6 | 19/47 |
| http://5.129.254.129:8888 | RU | 4338 | 6 | 25/26 |
| http://38.51.207.104:8080 | VE | 1539 | 6 | 6/6 |
| http://154.59.56.72:999 | VE | 2613 | 6 | 17/24 |
| socks5://5.45.119.70:1080 | EE | 1822 | 6 | 33/63 |
| socks5://144.91.121.61:1088 | FR | 2197 | 6 | 56/65 |
| http://120.232.115.170:17981 | CN | 1775 | 5 | 45/64 |
| http://41.33.245.139:1981 | EG | 1082 | 5 | 7/8 |
| http://103.130.61.61:8081 | ID | 3132 | 5 | 53/65 |
| http://197.224.185.3:3128 | MU | 1134 | 5 | 30/33 |
| http://201.71.2.24:999 | VE | 4974 | 5 | 16/53 |
| http://201.71.2.25:999 | VE | 4851 | 5 | 12/52 |
| socks5://118.179.93.24:9090 | BD | 2368 | 5 | 9/13 |
| socks5://141.148.158.143:1080 | US | 5622 | 5 | 34/64 |
| http://119.188.131.55:17981 | CN | 2405 | 4 | 25/65 |
| http://91.134.141.4:3128 | FR | 647 | 4 | 24/26 |
| http://103.147.134.33:8082 | ID | 3822 | 4 | 7/20 |
| http://103.173.138.35:8080 | ID | 3696 | 4 | 4/4 |
| http://168.144.117.43:3129 | IN | 1499 | 4 | 10/15 |
| http://157.85.111.64:3128 | TH | 1253 | 4 | 27/33 |
| http://38.172.160.16:999 | VE | 3793 | 4 | 11/16 |
| http://154.59.56.76:999 | VE | 2397 | 4 | 20/25 |
| socks5://31.211.142.115:8192 | BG | 1434 | 4 | 13/63 |
| socks5://43.156.84.41:10808 | SG | 2592 | 4 | 4/4 |
| socks5://144.24.47.42:1080 | US | 3492 | 4 | 31/61 |
| http://114.244.223.68:8888 | CN | 1970 | 3 | 17/28 |
| http://122.246.3.12:17981 | CN | 1674 | 3 | 28/59 |
| http://123.113.148.188:8888 | CN | 4077 | 3 | 8/20 |
| http://123.121.209.108:8888 | CN | 7269 | 3 | 8/15 |
| http://123.121.210.208:8888 | CN | 7083 | 3 | 8/17 |
| http://177.234.217.237:999 | EC | 7489 | 3 | 13/38 |
| http://194.163.175.167:40001 | FR | 7047 | 3 | 7/12 |
| http://103.147.134.75:8082 | ID | 7330 | 3 | 6/11 |
| http://205.164.192.115:999 | MX | 7140 | 3 | 38/63 |
| http://91.233.223.147:3128 | RU | 1086 | 3 | 10/39 |
| http://159.223.41.216:9090 | SG | 1182 | 3 | 15/25 |
| http://167.172.76.176:9090 | SG | 6060 | 3 | 12/26 |
| http://70.61.188.34:3128 | US | 2472 | 3 | 8/24 |
| http://154.59.56.74:999 | VE | 2550 | 3 | 18/28 |
| http://201.71.2.27:999 | VE | 2063 | 3 | 19/63 |
| socks5://186.26.95.249:61445 | BR | 1791 | 3 | 18/49 |
| socks5://51.178.49.241:1088 | FR | 972 | 3 | 21/26 |
| socks5://144.126.197.184:1088 | GB | 2968 | 3 | 16/21 |
| socks5://103.66.46.54:69 | ID | 4029 | 3 | 7/19 |
| socks5://103.165.128.75:1080 | ID | 2757 | 3 | 13/50 |
| socks5://144.24.111.128:1088 | IN | 2573 | 3 | 49/65 |
| socks5://103.75.118.84:1080 | JP | 4019 | 3 | 43/60 |
| socks5://5.130.50.118:1080 | RU | 1253 | 3 | 11/38 |
| socks5://178.150.77.204:10801 | UA | 7210 | 3 | 21/43 |
| http://109.236.45.95:8989 | AL | 5338 | 2 | 18/61 |
| http://186.22.246.60:3128 | AR | 1276 | 2 | 7/23 |
| http://182.160.110.154:9898 | BD | 7287 | 2 | 8/53 |
| http://185.191.239.248:3128 | CH | 2368 | 2 | 49/64 |
| http://38.7.195.52:999 | CL | 4665 | 2 | 18/47 |
| http://8.138.217.152:21001 | CN | 3331 | 2 | 42/65 |
| http://39.106.165.196:8080 | CN | 2001 | 2 | 31/61 |
