# Proxy status

Generated 2026-09-13T16:58:24Z by `harvest.py`.

- **827** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1757** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **17176** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 145/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1347 |
| socks5 | 396 |
| socks4 | 14 |

| country | entries |
|---|---|
| ID | 384 |
| NL | 148 |
| CN | 102 |
| US | 93 |
| CO | 71 |
| MX | 71 |
| RU | 67 |
| BD | 60 |
| PH | 59 |
| BR | 43 |
| VE | 42 |
| VN | 39 |
| SG | 35 |
| EC | 31 |
| DE | 29 |
| IN | 29 |
| EG | 27 |
| TH | 26 |
| FR | 25 |
| KH | 23 |
| CL | 22 |
| DO | 21 |
| TR | 21 |
| HK | 20 |
| AR | 18 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 58 | 58 | 35 | 2026-09-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-09-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 165 | 165 | 83 | 2026-09-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 193 | 193 | 56 | 2026-09-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 257 | 257 | 107 | 2026-09-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 258 | 258 | 112 | 2026-09-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 284 | 284 | 95 | 2026-09-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 288 | 288 | 168 | 2026-09-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 386 | 386 | 127 | 2026-09-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 534 | 2026-09-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-09-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-09-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1602 | 2026-09-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1977 | 1973 | 741 | 2026-09-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2119 | 2117 | 486 | 2026-09-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2203 | 2203 | 1582 | 2026-09-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2296 | 2294 | 699 | 2026-09-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2501 | 2499 | 1939 | 2026-09-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 2204 | 60 | 65/68 |
| http://34.43.46.91:80 | US | 2284 | 60 | 65/68 |
| http://95.211.174.135:3128 | NL | 1272 | 54 | 67/68 |
| http://185.200.188.234:10001 | RU | 1310 | 54 | 67/68 |
| http://130.110.103.245:3128 | SA | 1707 | 54 | 66/68 |
| http://1.231.81.166:3128 | KR | 982 | 33 | 65/68 |
| http://189.51.168.164:999 | MX | 558 | 33 | 33/33 |
| http://176.111.37.5:39811 | HK | 1156 | 28 | 62/68 |
| http://181.78.23.187:999 | CO | 862 | 25 | 35/37 |
| http://181.78.74.252:999 | CO | 893 | 25 | 57/59 |
| http://181.78.74.253:999 | CO | 900 | 25 | 57/59 |
| http://190.97.236.128:999 | VE | 877 | 25 | 56/58 |
| http://190.97.236.129:999 | VE | 1932 | 25 | 56/58 |
| http://176.111.37.216:39811 | HK | 1220 | 23 | 56/68 |
| http://5.129.254.49:8888 | RU | 1314 | 23 | 23/23 |
| http://5.129.254.51:8888 | RU | 1324 | 23 | 23/23 |
| http://5.129.254.70:8888 | RU | 1328 | 23 | 23/23 |
| http://95.3.69.222:8080 | TR | 1631 | 23 | 65/68 |
| http://5.129.254.60:8888 | RU | 1261 | 22 | 22/22 |
| http://5.129.254.5:8888 | RU | 1349 | 21 | 22/23 |
| http://190.97.241.106:999 | VE | 6361 | 20 | 29/52 |
| http://5.129.254.154:8888 | RU | 1375 | 19 | 19/19 |
| socks5://108.174.152.80:1080 | MX | 431 | 17 | 17/17 |
| http://45.186.6.104:3128 | EC | 896 | 16 | 45/46 |
| http://107.167.18.122:443 | US | 94 | 13 | 19/20 |
| http://103.237.102.191:11111 | DE | 987 | 12 | 64/68 |
| socks5://83.147.216.208:1080 | FI | 1183 | 12 | 18/36 |
| http://61.91.162.126:8080 | TH | 1590 | 11 | 11/11 |
| http://103.10.231.189:8080 | TH | 1235 | 11 | 36/53 |
| socks5://144.91.111.48:1088 | FR | 3915 | 10 | 38/68 |
| socks5://45.32.160.61:1088 | US | 490 | 10 | 20/21 |
| http://184.75.221.82:3118 | CA | 477 | 9 | 30/33 |
| http://113.45.195.147:3128 | CN | 4074 | 9 | 22/33 |
| http://5.129.254.129:8888 | RU | 1316 | 9 | 28/29 |
| socks5://5.45.119.70:1080 | EE | 1715 | 9 | 36/66 |
| socks5://144.91.121.61:1088 | FR | 4345 | 9 | 59/68 |
| http://103.130.61.61:8081 | ID | 3146 | 8 | 56/68 |
| http://197.224.185.3:3128 | MU | 7513 | 8 | 33/36 |
| http://91.134.141.4:3128 | FR | 819 | 7 | 27/29 |
| http://157.85.111.64:3128 | TH | 1091 | 7 | 30/36 |
| http://154.59.56.76:999 | VE | 6269 | 7 | 23/28 |
| socks5://43.156.84.41:10808 | SG | 1943 | 7 | 7/7 |
| socks5://144.24.47.42:1080 | US | 1252 | 7 | 34/64 |
| http://205.164.192.115:999 | MX | 2757 | 6 | 41/66 |
| socks5://51.178.49.241:1088 | FR | 1259 | 6 | 24/29 |
| socks5://103.75.118.84:1080 | JP | 4490 | 6 | 46/63 |
| http://186.5.94.206:999 | EC | 1487 | 5 | 28/30 |
| http://197.164.101.13:1981 | EG | 1779 | 5 | 24/57 |
| http://117.236.124.166:3128 | IN | 1594 | 5 | 44/68 |
| http://213.163.196.45:80 | SG | 1808 | 5 | 5/5 |
| http://38.172.179.192:999 | VE | 5945 | 5 | 18/62 |
| http://154.59.56.78:999 | VE | 3095 | 5 | 15/24 |
| http://14.251.13.20:8080 | VN | 1089 | 5 | 38/40 |
| socks5://118.179.195.140:9090 | BD | 4177 | 5 | 12/19 |
| socks5://213.199.47.140:1080 | FR | 5203 | 5 | 27/34 |
| socks5://123.58.219.171:10808 | HK | 3147 | 5 | 55/68 |
| socks5://45.74.31.42:14215 | NL | 2284 | 5 | 5/5 |
| socks5://213.165.38.49:1080 | NL | 2052 | 5 | 17/35 |
| socks5://43.135.176.121:1080 | US | 3037 | 5 | 20/23 |
| socks5://107.150.41.226:18080 | US | 433 | 5 | 5/5 |
| socks5://162.120.16.210:1080 | US | 1162 | 5 | 8/16 |
| http://144.217.82.40:8089 | CA | 6573 | 4 | 4/4 |
| http://123.121.122.28:8888 | CN | 1181 | 4 | 12/17 |
| http://79.32.158.19:3128 | IT | 1148 | 4 | 5/15 |
| http://165.154.162.73:8888 | US | 4635 | 4 | 38/68 |
| http://190.97.229.118:999 | VE | 3902 | 4 | 27/58 |
| socks5://161.97.114.197:1080 | FR | 4095 | 4 | 8/10 |
| socks5://47.76.175.249:1080 | HK | 1055 | 4 | 16/19 |
| socks5://101.36.104.239:10808 | JP | 1329 | 4 | 56/68 |
| socks5://161.35.90.93:1081 | NL | 6407 | 4 | 31/68 |
| socks5://161.35.90.93:1083 | NL | 1892 | 4 | 33/66 |
| http://186.216.208.98:3128 | BR | 3178 | 3 | 20/66 |
| http://47.110.226.74:19991 | CN | 4998 | 3 | 27/66 |
| http://114.236.137.41:21000 | CN | 1985 | 3 | 46/68 |
| http://190.121.157.41:999 | CO | 6086 | 3 | 6/40 |
| http://38.50.165.122:999 | DO | 7581 | 3 | 14/56 |
| http://45.240.232.61:8080 | EG | 5762 | 3 | 16/48 |
| http://156.200.116.67:8080 | EG | 4422 | 3 | 12/67 |
| http://37.187.109.70:10111 | FR | 3210 | 3 | 25/68 |
| http://102.164.252.150:8080 | GQ | 7313 | 3 | 13/27 |
| http://154.90.48.254:2024 | ID | 1743 | 3 | 3/3 |
| http://165.99.194.184:8080 | ID | 7679 | 3 | 15/66 |
| http://38.210.179.146:999 | MX | 6056 | 3 | 17/66 |
| http://148.222.153.74:999 | MX | 5630 | 3 | 13/64 |
| http://187.190.58.152:80 | MX | 2534 | 3 | 22/66 |
| http://38.158.83.161:999 | PE | 7086 | 3 | 9/56 |
| http://43.128.112.151:80 | SG | 915 | 3 | 5/7 |
| http://43.153.195.69:80 | SG | 882 | 3 | 5/8 |
| http://43.156.236.238:80 | SG | 901 | 3 | 32/66 |
| http://124.156.194.52:8081 | SG | 1988 | 3 | 3/3 |
| http://38.58.182.147:18080 | US | 4811 | 3 | 3/3 |
| http://195.158.8.123:3128 | UZ | 2720 | 3 | 44/66 |
| http://185.226.194.8:999 | VE | 6247 | 3 | 5/6 |
| http://42.116.159.52:50001 | VN | 1220 | 3 | 3/3 |
| http://163.181.207.213:9999 | VN | 1257 | 3 | 11/25 |
| socks5://123.0.24.154:9090 | BD | 3936 | 3 | 4/14 |
| socks5://5.75.133.113:10801 | DE | 5819 | 3 | 23/34 |
| socks5://65.21.252.66:10808 | FI | 1552 | 3 | 20/54 |
| socks5://54.95.120.6:1080 | JP | 703 | 3 | 3/3 |
| socks5://191.223.220.23:1080 | JP | 837 | 3 | 15/65 |
