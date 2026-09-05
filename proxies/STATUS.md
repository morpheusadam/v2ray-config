# Proxy status

Generated 2026-09-05T15:53:50Z by `harvest.py`.

- **593** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1753** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16059** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 133/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1423 |
| socks5 | 318 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 272 |
| US | 166 |
| CN | 118 |
| RU | 69 |
| MX | 66 |
| BD | 58 |
| IN | 54 |
| NL | 53 |
| PH | 52 |
| FR | 50 |
| CO | 44 |
| DE | 44 |
| VE | 43 |
| HK | 42 |
| SG | 41 |
| JP | 39 |
| BR | 37 |
| VN | 36 |
| EC | 28 |
| TH | 28 |
| CA | 25 |
| KH | 24 |
| EG | 23 |
| FI | 23 |
| IE | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 2 | 2026-09-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 47 | 47 | 30 | 2026-09-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 50 | 50 | 12 | 2026-09-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 98 | 98 | 20 | 2026-09-05 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 130 | 130 | 63 | 2026-09-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 67 | 2026-09-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 230 | 230 | 52 | 2026-09-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 235 | 235 | 19 | 2026-09-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 334 | 334 | 116 | 2026-09-05 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 461 | 461 | 183 | 2026-09-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-09-05 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1440 | 1436 | 363 | 2026-09-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1123 | 2026-09-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1601 | 2026-09-05 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2282 | 2282 | 1636 | 2026-09-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2372 | 2370 | 190 | 2026-09-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2836 | 2834 | 713 | 2026-09-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2966 | 2964 | 2247 | 2026-09-05 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 378 | 44 | 49/52 |
| http://34.43.46.91:80 | US | 251 | 44 | 49/52 |
| http://95.211.174.135:3128 | NL | 959 | 38 | 51/52 |
| http://204.76.203.9:3128 | NL | 930 | 38 | 51/52 |
| http://204.76.203.9:8080 | NL | 648 | 38 | 44/45 |
| http://185.200.188.234:10001 | RU | 1195 | 38 | 51/52 |
| http://130.110.103.245:3128 | SA | 1294 | 38 | 50/52 |
| http://199.7.149.96:3128 | US | 154 | 31 | 31/31 |
| http://64.112.184.210:3128 | US | 197 | 30 | 51/52 |
| http://103.211.103.170:3128 | HK | 2500 | 24 | 24/24 |
| http://68.178.174.239:3128 | US | 1029 | 20 | 20/20 |
| http://68.178.174.239:8888 | US | 1032 | 20 | 20/20 |
| http://1.231.81.166:3128 | KR | 990 | 17 | 49/52 |
| http://189.51.168.164:999 | MX | 2277 | 17 | 17/17 |
| socks5://193.25.215.182:22222 | US | 813 | 15 | 48/52 |
| http://116.202.172.187:11000 | DE | 1550 | 13 | 13/13 |
| http://91.134.141.4:3128 | FR | 725 | 13 | 13/13 |
| http://173.212.240.48:8888 | FR | 1026 | 13 | 13/13 |
| http://5.129.254.129:8888 | RU | 1286 | 13 | 13/13 |
| socks5://171.25.158.95:1080 | SE | 7335 | 13 | 29/51 |
| http://176.111.37.5:39811 | HK | 2197 | 12 | 46/52 |
| http://14.251.13.20:8080 | VN | 1291 | 12 | 23/24 |
| http://37.59.125.131:8888 | FR | 2295 | 10 | 39/52 |
| http://154.59.56.73:999 | VE | 2168 | 10 | 21/24 |
| socks5://101.36.104.46:10808 | JP | 1231 | 10 | 48/52 |
| socks5://5.255.117.250:1080 | NL | 3841 | 10 | 16/37 |
| http://120.232.115.170:17981 | CN | 1859 | 9 | 34/51 |
| http://181.78.23.187:999 | CO | 773 | 9 | 19/21 |
| http://181.78.74.252:999 | CO | 796 | 9 | 41/43 |
| http://181.78.74.253:999 | CO | 837 | 9 | 41/43 |
| http://190.97.236.128:999 | VE | 674 | 9 | 40/42 |
| http://190.97.236.129:999 | VE | 676 | 9 | 40/42 |
| http://103.177.118.145:8118 | BD | 1724 | 8 | 31/33 |
| http://186.5.94.206:999 | EC | 7710 | 8 | 13/14 |
| http://197.164.101.13:1981 | EG | 1996 | 8 | 13/41 |
| http://175.136.239.173:8181 | MY | 7849 | 8 | 41/52 |
| socks5://101.36.104.239:10808 | JP | 2146 | 8 | 43/52 |
| socks5://5.255.117.127:1080 | NL | 726 | 8 | 15/28 |
| socks5://147.45.60.124:1082 | US | 5378 | 8 | 28/52 |
| http://114.236.137.41:21000 | CN | 2731 | 7 | 36/52 |
| http://176.111.37.216:39811 | HK | 2600 | 7 | 40/52 |
| http://197.224.185.3:3128 | MU | 1180 | 7 | 18/20 |
| http://5.129.254.49:8888 | RU | 1127 | 7 | 7/7 |
| http://5.129.254.51:8888 | RU | 1092 | 7 | 7/7 |
| http://5.129.254.70:8888 | RU | 1076 | 7 | 7/7 |
| http://157.85.97.240:3128 | TH | 1200 | 7 | 14/20 |
| http://157.85.111.64:3128 | TH | 1246 | 7 | 18/20 |
| http://95.3.69.222:8080 | TR | 1386 | 7 | 49/52 |
| socks4://45.61.129.165:9050 | US | 2044 | 7 | 43/52 |
| socks5://79.137.79.217:2080 | FR | 754 | 7 | 7/7 |
| socks5://121.169.46.116:1090 | KR | 1400 | 7 | 35/52 |
| socks5://165.22.63.133:1080 | SG | 1237 | 7 | 8/9 |
| socks5://188.166.217.100:1080 | SG | 1254 | 7 | 7/7 |
| socks5://116.241.240.176:11080 | TW | 1137 | 7 | 8/9 |
| socks5://43.135.176.121:1080 | US | 777 | 7 | 7/7 |
| http://111.192.19.39:8888 | CN | 1323 | 6 | 8/16 |
| http://38.211.76.177:999 | CO | 764 | 6 | 7/10 |
| http://175.136.239.174:8181 | MY | 6783 | 6 | 34/52 |
| http://5.129.254.60:8888 | RU | 1208 | 6 | 6/6 |
| http://157.85.97.204:3128 | TH | 3245 | 6 | 14/17 |
| socks5://161.35.90.93:1083 | NL | 1361 | 6 | 24/50 |
| socks5://143.198.205.96:1080 | SG | 1323 | 6 | 6/6 |
| http://184.75.221.82:3118 | CA | 5406 | 5 | 16/17 |
| http://114.254.48.23:8888 | CN | 1549 | 5 | 5/5 |
| http://190.0.246.211:4040 | CO | 4869 | 5 | 44/52 |
| http://103.237.102.191:11111 | DE | 798 | 5 | 49/52 |
| http://65.1.240.131:3001 | IN | 1202 | 5 | 5/5 |
| http://5.129.254.5:8888 | RU | 1069 | 5 | 6/7 |
| http://202.28.194.139:31280 | TH | 2175 | 5 | 49/52 |
| http://193.104.179.115:3128 | UZ | 1738 | 5 | 7/17 |
| http://195.158.8.123:3128 | UZ | 2689 | 5 | 33/50 |
| socks5://144.91.111.48:1088 | FR | 2740 | 5 | 24/52 |
| socks5://213.199.47.140:1080 | FR | 1154 | 5 | 15/18 |
| socks5://144.24.111.128:1088 | IN | 1594 | 5 | 40/52 |
| socks5://193.233.218.121:1080 | RU | 2129 | 5 | 6/7 |
| socks5://143.198.93.65:1080 | SG | 1261 | 5 | 5/5 |
| socks5://159.223.86.111:1080 | SG | 1243 | 5 | 5/5 |
| socks5://45.32.160.61:1088 | US | 449 | 5 | 5/5 |
| socks5://154.12.242.0:1080 | US | 814 | 5 | 5/5 |
| socks5://185.222.138.237:1080 | XK | 1054 | 5 | 5/5 |
| http://111.192.25.85:8888 | CN | 6695 | 4 | 8/17 |
| http://123.119.176.120:8888 | CN | 3514 | 4 | 8/17 |
| http://200.10.31.45:8081 | CO | 6498 | 4 | 19/49 |
| http://167.233.89.17:1084 | DE | 5437 | 4 | 4/4 |
| http://167.233.148.141:1083 | DE | 1216 | 4 | 4/4 |
| http://167.233.169.253:1083 | DE | 4270 | 4 | 4/4 |
| http://186.33.45.218:999 | EC | 2285 | 4 | 26/41 |
| http://178.236.16.4:8888 | KZ | 1072 | 4 | 4/4 |
| http://116.204.182.120:80 | TH | 1252 | 4 | 4/4 |
| http://107.167.18.122:443 | US | 324 | 4 | 4/4 |
| http://154.59.56.76:999 | VE | 2368 | 4 | 9/12 |
| http://190.97.241.106:999 | VE | 4510 | 4 | 13/36 |
| http://210.211.113.37:80 | VN | 6442 | 4 | 16/24 |
| socks5://103.210.161.8:1080 | CN | 1241 | 4 | 17/25 |
| socks5://45.95.233.128:1082 | FR | 2012 | 4 | 22/51 |
| socks5://123.58.219.171:10808 | HK | 2695 | 4 | 43/52 |
| socks5://5.255.123.162:1080 | NL | 4840 | 4 | 14/35 |
| socks5://160.22.17.4:9988 | VN | 1608 | 4 | 21/48 |
| http://103.161.69.252:2698 | BD | 5274 | 3 | 20/52 |
| http://34.34.190.145:8080 | BE | 809 | 3 | 3/3 |
