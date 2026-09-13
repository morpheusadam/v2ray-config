# Proxy status

Generated 2026-09-13T21:40:47Z by `harvest.py`.

- **679** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1766** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **17140** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 111/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1327 |
| socks5 | 428 |
| socks4 | 11 |

| country | entries |
|---|---|
| ID | 371 |
| NL | 231 |
| US | 95 |
| CN | 88 |
| CO | 68 |
| MX | 63 |
| RU | 63 |
| PH | 58 |
| BD | 53 |
| VN | 44 |
| BR | 43 |
| VE | 41 |
| IN | 34 |
| SG | 33 |
| DE | 32 |
| EC | 31 |
| EG | 29 |
| TH | 24 |
| FR | 23 |
| DO | 22 |
| KH | 22 |
| TR | 18 |
| AR | 17 |
| HK | 17 |
| PE | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 3 | 3 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 59 | 59 | 15 | 2026-09-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 62 | 62 | 30 | 2026-09-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 103 | 103 | 37 | 2026-09-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 109 | 109 | 61 | 2026-09-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 113 | 113 | 37 | 2026-09-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 82 | 2026-09-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 272 | 272 | 165 | 2026-09-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 325 | 325 | 153 | 2026-09-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 415 | 415 | 137 | 2026-09-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 533 | 2026-09-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-09-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1120 | 2026-09-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1602 | 2026-09-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1975 | 1971 | 314 | 2026-09-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2526 | 2526 | 1751 | 2026-09-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2647 | 2645 | 459 | 2026-09-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2822 | 2820 | 708 | 2026-09-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3006 | 3004 | 2241 | 2026-09-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 709 | 61 | 66/69 |
| http://34.43.46.91:80 | US | 826 | 61 | 66/69 |
| http://95.211.174.135:3128 | NL | 1444 | 55 | 68/69 |
| http://185.200.188.234:10001 | RU | 1089 | 55 | 68/69 |
| http://130.110.103.245:3128 | SA | 1566 | 55 | 67/69 |
| http://1.231.81.166:3128 | KR | 1554 | 34 | 66/69 |
| http://176.111.37.5:39811 | HK | 1030 | 29 | 63/69 |
| http://181.78.23.187:999 | CO | 679 | 26 | 36/38 |
| http://181.78.74.252:999 | CO | 655 | 26 | 58/60 |
| http://181.78.74.253:999 | CO | 725 | 26 | 58/60 |
| http://190.97.236.128:999 | VE | 1802 | 26 | 57/59 |
| http://190.97.236.129:999 | VE | 1780 | 26 | 57/59 |
| http://5.129.254.49:8888 | RU | 1083 | 24 | 24/24 |
| http://5.129.254.51:8888 | RU | 1085 | 24 | 24/24 |
| http://5.129.254.70:8888 | RU | 1040 | 24 | 24/24 |
| http://95.3.69.222:8080 | TR | 1478 | 24 | 66/69 |
| http://5.129.254.60:8888 | RU | 1133 | 23 | 23/23 |
| http://5.129.254.5:8888 | RU | 1003 | 22 | 23/24 |
| http://190.97.241.106:999 | VE | 4333 | 21 | 30/53 |
| http://5.129.254.154:8888 | RU | 1060 | 20 | 20/20 |
| socks5://108.174.152.80:1080 | MX | 868 | 18 | 18/18 |
| http://45.186.6.104:3128 | EC | 604 | 17 | 46/47 |
| http://107.167.18.122:443 | US | 1355 | 14 | 20/21 |
| http://103.237.102.191:11111 | DE | 844 | 13 | 65/69 |
| socks5://83.147.216.208:1080 | FI | 841 | 13 | 19/37 |
| http://61.91.162.126:8080 | TH | 1582 | 12 | 12/12 |
| http://103.10.231.189:8080 | TH | 1610 | 12 | 37/54 |
| socks5://144.91.111.48:1088 | FR | 2209 | 11 | 39/69 |
| socks5://45.32.160.61:1088 | US | 232 | 11 | 21/22 |
| http://184.75.221.82:3118 | CA | 1315 | 10 | 31/34 |
| http://5.129.254.129:8888 | RU | 1056 | 10 | 29/30 |
| socks5://144.91.121.61:1088 | FR | 3548 | 10 | 60/69 |
| http://91.134.141.4:3128 | FR | 507 | 8 | 28/30 |
| socks5://43.156.84.41:10808 | SG | 3551 | 8 | 8/8 |
| socks5://51.178.49.241:1088 | FR | 760 | 7 | 25/30 |
| socks5://103.75.118.84:1080 | JP | 1937 | 7 | 47/64 |
| http://186.5.94.206:999 | EC | 980 | 6 | 29/31 |
| http://213.163.196.45:80 | SG | 1433 | 6 | 6/6 |
| http://38.172.179.192:999 | VE | 5395 | 6 | 19/63 |
| http://154.59.56.78:999 | VE | 6295 | 6 | 16/25 |
| http://14.251.13.20:8080 | VN | 1413 | 6 | 39/41 |
| socks5://118.179.195.140:9090 | BD | 2165 | 6 | 13/20 |
| socks5://213.199.47.140:1080 | FR | 2694 | 6 | 28/35 |
| socks5://123.58.219.171:10808 | HK | 2826 | 6 | 56/69 |
| socks5://45.74.31.42:14215 | NL | 3191 | 6 | 6/6 |
| socks5://213.165.38.49:1080 | NL | 2712 | 6 | 18/36 |
| socks5://43.135.176.121:1080 | US | 527 | 6 | 21/24 |
| socks5://107.150.41.226:18080 | US | 703 | 6 | 6/6 |
| http://165.154.162.73:8888 | US | 7598 | 5 | 39/69 |
| http://190.97.229.118:999 | VE | 5257 | 5 | 28/59 |
| socks5://161.97.114.197:1080 | FR | 3695 | 5 | 9/11 |
| socks5://47.76.175.249:1080 | HK | 1970 | 5 | 17/20 |
| socks5://101.36.104.239:10808 | JP | 4605 | 5 | 57/69 |
| socks5://161.35.90.93:1083 | NL | 2493 | 5 | 34/67 |
| http://186.216.208.98:3128 | BR | 5989 | 4 | 21/67 |
| http://114.236.137.41:21000 | CN | 1812 | 4 | 47/69 |
| http://45.240.232.61:8080 | EG | 1453 | 4 | 17/49 |
| http://43.128.112.151:80 | SG | 1163 | 4 | 6/8 |
| http://43.153.195.69:80 | SG | 1197 | 4 | 6/9 |
| http://43.156.236.238:80 | SG | 1143 | 4 | 33/67 |
| http://124.156.194.52:8081 | SG | 2802 | 4 | 4/4 |
| http://195.158.8.123:3128 | UZ | 2340 | 4 | 45/67 |
| socks5://123.0.24.154:9090 | BD | 3850 | 4 | 5/15 |
| socks5://5.75.133.113:10801 | DE | 910 | 4 | 24/35 |
| socks5://54.95.120.6:1080 | JP | 1028 | 4 | 4/4 |
| socks5://191.223.220.23:1080 | JP | 1148 | 4 | 16/66 |
| socks5://5.255.103.55:1080 | NL | 2910 | 4 | 24/68 |
| socks5://185.49.110.155:1080 | RU | 1600 | 4 | 24/66 |
| socks5://213.27.29.153:51000 | RU | 3304 | 4 | 18/67 |
| socks5://193.25.215.182:22222 | US | 1640 | 4 | 64/69 |
| http://51.161.123.224:8080 | CA | 1243 | 3 | 3/3 |
| http://8.138.217.152:21001 | CN | 7097 | 3 | 45/69 |
| http://115.231.181.40:8128 | CN | 2273 | 3 | 28/68 |
| http://119.188.131.55:17981 | CN | 4961 | 3 | 28/69 |
| http://120.232.115.170:17981 | CN | 1803 | 3 | 48/68 |
| http://122.246.3.12:17981 | CN | 1620 | 3 | 31/63 |
| http://2.27.63.250:8118 | DE | 641 | 3 | 9/19 |
| http://94.43.164.242:8080 | GE | 6965 | 3 | 3/3 |
| http://154.90.48.231:9090 | ID | 1842 | 3 | 3/3 |
| http://45.43.60.220:8080 | JP | 3322 | 3 | 40/68 |
| http://45.90.236.68:3128 | NL | 1138 | 3 | 3/3 |
| http://119.95.176.156:8082 | PH | 2166 | 3 | 11/23 |
| http://46.183.134.50:8080 | RU | 6939 | 3 | 11/66 |
| http://47.84.84.1:3128 | SG | 3253 | 3 | 23/69 |
| socks5://113.249.111.67:1080 | CN | 2447 | 3 | 19/36 |
| socks5://103.163.244.106:1080 | IN | 3637 | 3 | 15/65 |
| socks5://110.235.247.206:1080 | KH | 6095 | 3 | 14/50 |
| socks5://202.79.26.242:1080 | KH | 2933 | 3 | 7/28 |
| socks5://45.74.31.42:20222 | NL | 6051 | 3 | 3/3 |
| socks5://95.81.96.158:1080 | NL | 5020 | 3 | 6/29 |
| socks5://31.41.227.175:1080 | RU | 6242 | 3 | 6/9 |
| socks5://77.110.104.9:1080 | RU | 1681 | 3 | 9/12 |
| http://165.101.26.18:8080 | AF | 7658 | 2 | 3/7 |
| http://103.177.118.145:8118 | BD | 4719 | 2 | 46/50 |
| http://182.160.124.54:12331 | BD | 6812 | 2 | 12/68 |
| http://138.122.140.194:3128 | BR | 4244 | 2 | 21/63 |
| http://179.191.229.45:8900 | BR | 3151 | 2 | 3/20 |
| http://187.19.200.217:8090 | BR | 6567 | 2 | 2/2 |
| http://38.7.195.52:999 | CL | 7367 | 2 | 20/51 |
| http://47.103.30.64:8080 | CN | 1723 | 2 | 2/2 |
