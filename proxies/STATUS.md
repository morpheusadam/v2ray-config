# Proxy status

Generated 2026-08-12T14:26:27Z by `harvest.py`.

- **404** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **530** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11232** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 161/530 (30%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 338 |
| socks5 | 180 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 87 |
| US | 61 |
| RU | 30 |
| CN | 26 |
| NL | 26 |
| FR | 20 |
| VN | 20 |
| DE | 18 |
| SG | 18 |
| JP | 17 |
| PH | 16 |
| HK | 15 |
| BD | 13 |
| CO | 11 |
| IN | 10 |
| VE | 9 |
| BR | 8 |
| TH | 8 |
| TR | 8 |
| KH | 7 |
| KR | 7 |
| MX | 7 |
| PL | 6 |
| CL | 5 |
| FI | 5 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 3 | 2026-08-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 68 | 68 | 49 | 2026-08-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 93 | 93 | 48 | 2026-08-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 95 | 95 | 31 | 2026-08-12 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-08-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 110 | 110 | 60 | 2026-08-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 129 | 129 | 48 | 2026-08-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 130 | 130 | 14 | 2026-08-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 89 | 2026-08-12 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 159 | 159 | 40 | 2026-08-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 305 | 305 | 168 | 2026-08-12 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 164 | 2026-08-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 535 | 2026-08-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-08-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1139 | 2026-08-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1636 | 2026-08-12 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1846 | 1846 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1948 | 1948 | 195 | 2026-08-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2468 | 2468 | 716 | 2026-08-12 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2507 | 2507 | 2033 | 2026-08-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2928 | 2926 | 2645 | 2026-08-12 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://114.236.137.41:21000 | CN | 4491 | 4 | 4/4 |
| http://190.0.246.211:4040 | CO | 2722 | 4 | 4/4 |
| http://87.251.77.29:3128 | DE | 1072 | 4 | 4/4 |
| http://103.237.102.191:11111 | DE | 5818 | 4 | 4/4 |
| http://43.99.100.108:3128 | HK | 1210 | 4 | 4/4 |
| http://176.111.37.5:39811 | HK | 1209 | 4 | 4/4 |
| http://176.111.37.216:39811 | HK | 1361 | 4 | 4/4 |
| http://103.130.61.61:8081 | ID | 5612 | 4 | 4/4 |
| http://1.231.81.166:3128 | KR | 1182 | 4 | 4/4 |
| http://175.139.255.25:8181 | MY | 2601 | 4 | 4/4 |
| http://175.143.76.177:8181 | MY | 2653 | 4 | 4/4 |
| http://88.210.11.216:8989 | NL | 6249 | 4 | 4/4 |
| http://95.211.64.139:8888 | NL | 1946 | 4 | 4/4 |
| http://95.211.64.139:8889 | NL | 3863 | 4 | 4/4 |
| http://95.211.174.135:3128 | NL | 1116 | 4 | 4/4 |
| http://144.178.199.118:8443 | NL | 1098 | 4 | 4/4 |
| http://147.45.166.120:3333 | NL | 972 | 4 | 4/4 |
| http://204.76.203.9:3128 | NL | 1072 | 4 | 4/4 |
| http://109.94.1.23:4050 | RU | 4264 | 4 | 4/4 |
| http://185.200.188.234:10001 | RU | 1312 | 4 | 4/4 |
| http://143.198.87.117:8888 | SG | 4497 | 4 | 4/4 |
| http://152.42.167.241:3128 | SG | 5219 | 4 | 4/4 |
| http://47.81.56.193:8888 | TH | 1341 | 4 | 4/4 |
| http://202.28.194.139:31280 | TH | 1877 | 4 | 4/4 |
| http://95.3.69.222:8080 | TR | 1554 | 4 | 4/4 |
| http://34.43.46.91:443 | US | 541 | 4 | 4/4 |
| http://34.43.46.91:80 | US | 550 | 4 | 4/4 |
| http://43.153.82.179:8888 | US | 7972 | 4 | 4/4 |
| http://64.112.184.210:3128 | US | 1566 | 4 | 4/4 |
| socks5://144.22.165.206:1088 | BR | 4789 | 4 | 4/4 |
| socks5://45.144.54.40:1080 | DE | 1240 | 4 | 4/4 |
| socks5://66.163.118.99:10006 | ES | 1990 | 4 | 4/4 |
| socks5://144.91.121.61:1088 | FR | 1952 | 4 | 4/4 |
| socks5://212.58.132.5:1080 | GB | 1956 | 4 | 4/4 |
| socks5://123.58.219.171:10808 | HK | 1384 | 4 | 4/4 |
| socks5://66.163.119.55:10006 | IT | 2528 | 4 | 4/4 |
| socks5://149.62.186.244:1080 | IT | 4395 | 4 | 4/4 |
| socks5://101.36.104.46:10808 | JP | 1651 | 4 | 4/4 |
| socks5://101.36.104.239:10808 | JP | 1649 | 4 | 4/4 |
| socks5://193.233.218.213:1080 | RU | 4641 | 4 | 4/4 |
| socks5://43.134.58.45:1080 | SG | 2617 | 4 | 4/4 |
| socks5://43.156.84.41:10808 | SG | 1730 | 4 | 4/4 |
| socks5://43.162.94.99:1080 | US | 1166 | 4 | 4/4 |
| socks5://69.55.49.177:38182 | US | 1156 | 4 | 4/4 |
| socks5://129.151.9.55:10808 | US | 2392 | 4 | 4/4 |
| socks5://193.25.215.182:22222 | US | 725 | 4 | 4/4 |
| http://185.191.239.248:3128 | CH | 2580 | 3 | 3/3 |
| http://38.7.195.53:999 | CL | 6722 | 3 | 3/3 |
| http://177.224.225.7:3128 | MX | 1256 | 3 | 3/3 |
| http://95.211.64.139:8887 | NL | 971 | 3 | 3/3 |
| http://180.191.125.28:8081 | PH | 3080 | 3 | 3/3 |
| http://180.191.231.149:8082 | PH | 6441 | 3 | 3/3 |
| http://203.150.128.134:8080 | TH | 6982 | 3 | 3/3 |
| http://178.18.207.85:8888 | TR | 7475 | 3 | 3/3 |
| http://154.219.125.230:3128 | US | 93 | 3 | 3/3 |
| http://157.230.178.216:40000 | US | 5643 | 3 | 3/3 |
| http://162.214.74.29:3128 | US | 5317 | 3 | 3/3 |
| http://162.214.159.94:3128 | US | 4914 | 3 | 3/3 |
| http://165.22.161.41:8118 | US | 5615 | 3 | 3/3 |
| http://174.137.134.182:2999 | US | 6745 | 3 | 3/3 |
| http://163.181.207.167:9999 | VN | 1177 | 3 | 3/3 |
| socks5://192.9.171.168:1080 | AU | 5530 | 3 | 3/3 |
| socks5://134.175.238.113:1080 | CN | 2743 | 3 | 3/3 |
| socks5://212.113.99.167:10800 | DE | 1445 | 3 | 3/3 |
| socks5://185.185.80.58:1088 | FR | 3901 | 3 | 3/3 |
| socks5://144.21.39.252:1080 | NL | 3134 | 3 | 3/3 |
| socks5://91.204.178.195:1080 | RU | 4895 | 3 | 3/3 |
| socks5://171.25.158.95:1080 | SE | 2518 | 3 | 3/3 |
| socks5://45.32.160.61:1088 | US | 539 | 3 | 3/3 |
| socks5://67.207.92.87:1088 | US | 515 | 3 | 3/3 |
| socks5://141.148.158.143:1080 | US | 5276 | 3 | 3/3 |
| socks5://147.45.60.110:1082 | US | 419 | 3 | 3/3 |
| http://138.117.14.238:8090 | AR | 6540 | 2 | 2/2 |
| http://190.136.211.228:999 | AR | 6607 | 2 | 2/2 |
| http://185.32.45.61:8090 | AZ | 5650 | 2 | 2/2 |
| http://103.142.69.62:8080 | BD | 2690 | 2 | 2/2 |
| http://103.148.83.110:8889 | BD | 2510 | 2 | 2/2 |
| http://123.0.26.73:10000 | BD | 5470 | 2 | 2/2 |
| http://138.186.187.194:8080 | BR | 7873 | 2 | 2/2 |
| http://170.238.38.15:8080 | BR | 6365 | 2 | 2/2 |
| http://45.95.232.35:3128 | CH | 7763 | 2 | 2/2 |
| http://45.175.137.253:999 | CL | 4194 | 2 | 2/2 |
| http://27.185.218.213:17981 | CN | 4570 | 2 | 3/4 |
| http://47.110.226.74:19991 | CN | 6797 | 2 | 2/2 |
| http://101.206.186.99:8080 | CN | 4996 | 2 | 3/4 |
| http://111.230.27.213:3128 | CN | 6417 | 2 | 3/4 |
| http://119.91.133.30:8080 | CN | 4927 | 2 | 2/2 |
| http://122.246.3.210:17981 | CN | 6303 | 2 | 3/4 |
| http://223.85.21.195:8080 | CN | 4499 | 2 | 2/2 |
| http://190.14.240.133:999 | CO | 3965 | 2 | 2/2 |
| http://152.53.20.190:20000 | DE | 3920 | 2 | 3/4 |
| http://45.144.53.63:5050 | FI | 6679 | 2 | 2/2 |
| http://65.108.159.129:8081 | FI | 2952 | 2 | 2/2 |
| http://103.97.140.199:8080 | ID | 4958 | 2 | 2/2 |
| http://103.99.136.98:8080 | ID | 2161 | 2 | 2/2 |
| http://103.124.197.26:8090 | ID | 5970 | 2 | 2/2 |
| http://103.133.24.37:8080 | ID | 1228 | 2 | 2/2 |
| http://103.146.185.139:1111 | ID | 4350 | 2 | 2/2 |
| http://103.167.68.84:8080 | ID | 2267 | 2 | 2/2 |
| http://103.167.170.70:1111 | ID | 7208 | 2 | 2/2 |
