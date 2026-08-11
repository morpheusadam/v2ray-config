# Proxy status

Generated 2026-08-11T14:25:22Z by `harvest.py`.

- **394** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **394** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **10659** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 155/394 (39%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 244 |
| socks5 | 144 |
| socks4 | 6 |

| country | entries |
|---|---|
| US | 56 |
| ID | 54 |
| NL | 20 |
| RU | 20 |
| BD | 18 |
| FR | 17 |
| VN | 17 |
| CN | 15 |
| PH | 15 |
| CO | 12 |
| JP | 11 |
| DE | 10 |
| HK | 10 |
| BR | 9 |
| KH | 8 |
| IN | 7 |
| SG | 7 |
| TH | 7 |
| MX | 6 |
| GB | 5 |
| MY | 5 |
| TR | 5 |
| FI | 4 |
| IT | 4 |
| KR | 4 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 7 | 2026-08-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 70 | 70 | 61 | 2026-08-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 85 | 2026-08-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 105 | 105 | 50 | 2026-08-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 115 | 115 | 33 | 2026-08-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 138 | 138 | 24 | 2026-08-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 90 | 2026-08-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 157 | 157 | 107 | 2026-08-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 177 | 177 | 71 | 2026-08-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 213 | 213 | 77 | 2026-08-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 345 | 345 | 248 | 2026-08-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 537 | 2026-08-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-08-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-08-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1641 | 2026-08-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1854 | 1850 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1984 | 1982 | 245 | 2026-08-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2416 | 2414 | 733 | 2026-08-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2546 | 2546 | 2050 | 2026-08-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2589 | 2587 | 2485 | 2026-08-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://186.10.150.112:8080 | CL | 5487 | 2 | 2/2 |
| http://8.138.217.152:21001 | CN | 5330 | 2 | 2/2 |
| http://114.236.137.41:21000 | CN | 6676 | 2 | 2/2 |
| http://119.188.131.55:17981 | CN | 1739 | 2 | 2/2 |
| http://190.0.246.211:4040 | CO | 3457 | 2 | 2/2 |
| http://87.251.77.29:3128 | DE | 1022 | 2 | 2/2 |
| http://103.237.102.191:11111 | DE | 942 | 2 | 2/2 |
| http://181.39.25.196:8118 | EC | 1393 | 2 | 2/2 |
| http://37.59.125.131:8888 | FR | 1476 | 2 | 2/2 |
| http://37.187.109.70:10111 | FR | 3648 | 2 | 2/2 |
| http://169.58.85.194:8080 | FR | 1386 | 2 | 2/2 |
| http://18.170.25.193:53656 | GB | 3212 | 2 | 2/2 |
| http://82.102.11.164:3460 | GB | 6078 | 2 | 2/2 |
| http://43.99.100.108:3128 | HK | 1312 | 2 | 2/2 |
| http://172.110.220.36:3128 | HK | 945 | 2 | 2/2 |
| http://176.111.37.5:39811 | HK | 1112 | 2 | 2/2 |
| http://176.111.37.216:39811 | HK | 1491 | 2 | 2/2 |
| http://103.130.61.61:8081 | ID | 3477 | 2 | 2/2 |
| http://103.135.48.30:8089 | ID | 4162 | 2 | 2/2 |
| http://103.156.248.60:8080 | ID | 5111 | 2 | 2/2 |
| http://110.76.147.26:1111 | ID | 5079 | 2 | 2/2 |
| http://146.196.40.165:8080 | ID | 4459 | 2 | 2/2 |
| http://14.139.235.82:3128 | IN | 2099 | 2 | 2/2 |
| http://5.200.72.62:3128 | IR | 2989 | 2 | 2/2 |
| http://178.252.180.59:10909 | IR | 1993 | 2 | 2/2 |
| http://185.191.106.0:8081 | IT | 6629 | 2 | 2/2 |
| http://188.217.172.202:8080 | IT | 4337 | 2 | 2/2 |
| http://1.231.81.166:3128 | KR | 1186 | 2 | 2/2 |
| http://175.136.239.173:8181 | MY | 2747 | 2 | 2/2 |
| http://175.136.239.174:8181 | MY | 2732 | 2 | 2/2 |
| http://175.139.255.25:8181 | MY | 3888 | 2 | 2/2 |
| http://175.143.76.177:8181 | MY | 4676 | 2 | 2/2 |
| http://88.210.11.216:8989 | NL | 1305 | 2 | 2/2 |
| http://89.251.21.4:8080 | NL | 5970 | 2 | 2/2 |
| http://95.211.64.139:8888 | NL | 1379 | 2 | 2/2 |
| http://95.211.64.139:8889 | NL | 1054 | 2 | 2/2 |
| http://95.211.174.135:3128 | NL | 1090 | 2 | 2/2 |
| http://144.178.199.118:8443 | NL | 943 | 2 | 2/2 |
| http://147.45.166.120:3333 | NL | 2365 | 2 | 2/2 |
| http://195.133.14.222:49152 | NL | 956 | 2 | 2/2 |
| http://204.76.203.9:3128 | NL | 982 | 2 | 2/2 |
| http://109.94.1.23:4050 | RU | 3079 | 2 | 2/2 |
| http://185.200.188.234:10001 | RU | 1656 | 2 | 2/2 |
| http://130.110.103.245:3128 | SA | 2023 | 2 | 2/2 |
| http://143.198.87.117:8888 | SG | 1208 | 2 | 2/2 |
| http://152.42.167.241:3128 | SG | 1436 | 2 | 2/2 |
| http://47.81.56.193:8888 | TH | 1483 | 2 | 2/2 |
| http://202.28.194.139:31280 | TH | 2240 | 2 | 2/2 |
| http://95.3.69.222:8080 | TR | 1515 | 2 | 2/2 |
| http://34.43.46.91:443 | US | 456 | 2 | 2/2 |
| http://34.43.46.91:80 | US | 401 | 2 | 2/2 |
| http://43.153.82.179:8888 | US | 4131 | 2 | 2/2 |
| http://64.112.184.210:3128 | US | 1956 | 2 | 2/2 |
| http://216.106.182.177:3128 | US | 565 | 2 | 2/2 |
| http://38.76.9.0:999 | VE | 1675 | 2 | 2/2 |
| http://113.160.132.26:8080 | VN | 1499 | 2 | 2/2 |
| socks4://119.28.64.217:50161 | HK | 4313 | 2 | 2/2 |
| socks4://185.171.83.65:49153 | NL | 2205 | 2 | 2/2 |
| socks4://216.106.179.216:49430 | US | 3425 | 2 | 2/2 |
| socks5://152.69.167.87:1080 | AU | 7367 | 2 | 2/2 |
| socks5://103.151.74.29:2025 | BD | 7185 | 2 | 2/2 |
| socks5://144.22.165.206:1088 | BR | 2779 | 2 | 2/2 |
| socks5://38.49.210.79:40000 | CA | 2841 | 2 | 2/2 |
| socks5://51.222.104.72:1080 | CA | 3555 | 2 | 2/2 |
| socks5://45.144.54.40:1080 | DE | 1648 | 2 | 2/2 |
| socks5://66.163.118.99:10006 | ES | 1054 | 2 | 2/2 |
| socks5://51.159.97.242:10006 | FR | 6032 | 2 | 2/2 |
| socks5://109.123.251.109:1080 | FR | 3002 | 2 | 2/2 |
| socks5://109.172.55.177:1082 | FR | 2019 | 2 | 2/2 |
| socks5://144.91.111.48:1088 | FR | 2719 | 2 | 2/2 |
| socks5://144.91.121.61:1088 | FR | 1611 | 2 | 2/2 |
| socks5://194.163.174.78:1085 | FR | 4391 | 2 | 2/2 |
| socks5://212.58.132.5:1080 | GB | 2020 | 2 | 2/2 |
| socks5://38.76.215.92:1080 | HK | 4448 | 2 | 2/2 |
| socks5://123.58.219.171:10808 | HK | 1434 | 2 | 2/2 |
| socks5://165.154.20.187:10808 | HK | 2672 | 2 | 2/2 |
| socks5://103.174.122.197:8199 | ID | 3014 | 2 | 2/2 |
| socks5://202.43.165.140:10802 | ID | 6584 | 2 | 2/2 |
| socks5://144.24.111.128:1088 | IN | 1957 | 2 | 2/2 |
| socks5://66.163.119.55:10006 | IT | 2362 | 2 | 2/2 |
| socks5://149.62.186.244:1080 | IT | 4622 | 2 | 2/2 |
| socks5://101.36.104.46:10808 | JP | 2162 | 2 | 2/2 |
| socks5://101.36.104.239:10808 | JP | 1773 | 2 | 2/2 |
| socks5://202.62.62.113:1080 | KH | 2030 | 2 | 2/2 |
| socks5://121.169.46.116:1090 | KR | 1760 | 2 | 2/2 |
| socks5://195.135.255.98:1080 | LV | 7236 | 2 | 2/2 |
| socks5://47.250.211.53:1080 | MY | 1622 | 2 | 2/2 |
| socks5://5.230.201.154:1080 | NL | 1755 | 2 | 2/2 |
| socks5://45.137.43.0:1081 | PL | 2236 | 2 | 2/2 |
| socks5://151.115.99.193:10006 | PL | 1811 | 2 | 2/2 |
| socks5://193.233.218.213:1080 | RU | 1355 | 2 | 2/2 |
| socks5://43.134.58.45:1080 | SG | 2323 | 2 | 2/2 |
| socks5://43.156.84.41:10808 | SG | 6893 | 2 | 2/2 |
| socks5://43.163.122.46:8080 | SG | 1454 | 2 | 2/2 |
| socks5://5.78.44.212:1080 | US | 4361 | 2 | 2/2 |
| socks5://43.162.94.99:1080 | US | 2623 | 2 | 2/2 |
| socks5://47.85.195.135:1080 | US | 5803 | 2 | 2/2 |
| socks5://47.251.127.154:1080 | US | 660 | 2 | 2/2 |
| socks5://69.55.49.177:38182 | US | 769 | 2 | 2/2 |
| socks5://107.191.44.214:1081 | US | 3427 | 2 | 2/2 |
