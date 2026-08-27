# Proxy status

Generated 2026-08-27T22:55:29Z by `harvest.py`.

- **791** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1612** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13829** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 163/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1299 |
| socks5 | 300 |
| socks4 | 13 |

| country | entries |
|---|---|
| ID | 338 |
| US | 77 |
| PH | 75 |
| CO | 70 |
| CN | 58 |
| RU | 56 |
| BD | 53 |
| IN | 49 |
| MX | 48 |
| NL | 48 |
| DE | 46 |
| FR | 41 |
| BR | 38 |
| VE | 36 |
| VN | 36 |
| SG | 32 |
| HK | 31 |
| TR | 31 |
| EC | 28 |
| JP | 27 |
| AR | 21 |
| CL | 20 |
| TH | 20 |
| DO | 18 |
| KH | 18 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 3 | 3 | 0 | 2026-08-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 45 | 45 | 17 | 2026-08-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 64 | 64 | 39 | 2026-08-27 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-08-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 101 | 101 | 26 | 2026-08-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 140 | 140 | 24 | 2026-08-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 61 | 2026-08-27 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 157 | 157 | 59 | 2026-08-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 161 | 161 | 80 | 2026-08-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 222 | 222 | 44 | 2026-08-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 321 | 321 | 137 | 2026-08-27 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-08-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-08-27 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1277 | 1273 | 301 | 2026-08-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1455 | 1453 | 216 | 2026-08-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-08-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1608 | 2026-08-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1911 | 1909 | 691 | 2026-08-27 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2106 | 2106 | 1644 | 2026-08-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2217 | 2215 | 1716 | 2026-08-27 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 3369 | 31 | 33/34 |
| http://34.43.46.91:443 | US | 421 | 26 | 31/34 |
| http://34.43.46.91:80 | US | 1286 | 26 | 31/34 |
| http://103.237.102.191:11111 | DE | 2130 | 20 | 33/34 |
| http://95.211.174.135:3128 | NL | 1442 | 20 | 33/34 |
| http://204.76.203.9:3128 | NL | 1621 | 20 | 33/34 |
| http://204.76.203.9:8080 | NL | 663 | 20 | 26/27 |
| http://185.200.188.234:10001 | RU | 2664 | 20 | 33/34 |
| http://130.110.103.245:3128 | SA | 2550 | 20 | 32/34 |
| http://95.3.69.222:8080 | TR | 2607 | 20 | 33/34 |
| http://199.7.149.90:3128 | US | 218 | 17 | 17/17 |
| http://199.7.149.96:3128 | US | 234 | 13 | 13/13 |
| http://45.186.6.104:3128 | EC | 784 | 12 | 12/12 |
| http://64.112.184.210:3128 | US | 405 | 12 | 33/34 |
| socks5://123.58.219.171:10808 | HK | 2606 | 12 | 28/34 |
| socks5://43.162.94.99:1080 | US | 3910 | 11 | 27/34 |
| http://190.0.246.210:4040 | CO | 710 | 10 | 30/33 |
| http://47.81.56.193:8888 | TH | 3744 | 10 | 18/34 |
| http://103.130.61.61:8081 | ID | 2780 | 9 | 29/34 |
| http://42.96.18.62:1311 | VN | 1758 | 8 | 23/33 |
| socks5://144.91.121.61:1088 | FR | 4777 | 8 | 32/34 |
| socks5://101.36.104.239:10808 | JP | 2231 | 8 | 28/34 |
| socks5://67.207.92.87:1088 | US | 486 | 8 | 19/33 |
| socks5://193.25.215.182:22222 | US | 1210 | 8 | 31/34 |
| http://176.111.37.5:39811 | HK | 2277 | 7 | 29/34 |
| socks5://152.89.104.11:1080 | DE | 902 | 7 | 12/34 |
| socks5://152.32.168.221:10808 | HK | 4967 | 7 | 17/23 |
| http://179.41.11.138:8080 | AR | 855 | 6 | 6/6 |
| http://185.191.239.248:3128 | CH | 1009 | 6 | 23/33 |
| http://190.0.246.211:4040 | CO | 2628 | 6 | 29/34 |
| http://103.211.103.170:3128 | HK | 576 | 6 | 6/6 |
| http://202.28.194.139:31280 | TH | 3764 | 6 | 32/34 |
| http://154.59.56.73:999 | VE | 5947 | 6 | 6/6 |
| http://14.251.13.20:8080 | VN | 1186 | 6 | 6/6 |
| socks4://45.61.129.165:9050 | US | 3060 | 6 | 26/34 |
| socks5://101.36.104.46:10808 | JP | 1905 | 6 | 31/34 |
| socks5://43.164.3.124:1080 | TH | 1410 | 6 | 23/33 |
| http://87.251.77.29:3128 | DE | 1033 | 5 | 31/34 |
| http://153.80.240.37:8080 | NL | 888 | 5 | 23/34 |
| http://103.218.122.183:8080 | VN | 1291 | 5 | 5/5 |
| socks5://45.194.33.12:30001 | HK | 2478 | 5 | 23/30 |
| socks5://45.194.33.12:30002 | HK | 2181 | 5 | 7/8 |
| http://103.177.118.145:8118 | BD | 1601 | 4 | 14/15 |
| http://114.236.137.41:21000 | CN | 2299 | 4 | 22/34 |
| http://81.19.210.10:80 | GB | 590 | 4 | 4/4 |
| http://18.60.247.31:16583 | IN | 5410 | 4 | 5/11 |
| http://43.206.240.252:32840 | JP | 2222 | 4 | 9/18 |
| http://38.194.246.34:999 | MX | 6476 | 4 | 15/25 |
| http://175.143.76.177:8181 | MY | 1926 | 4 | 24/34 |
| http://43.98.172.166:3128 | SG | 1255 | 4 | 4/4 |
| http://43.156.236.238:80 | SG | 1316 | 4 | 15/32 |
| http://43.160.242.118:3128 | SG | 1031 | 4 | 25/31 |
| http://165.99.14.18:2222 | VN | 3223 | 4 | 4/4 |
| socks5://51.222.104.72:1080 | CA | 6056 | 4 | 15/34 |
| socks5://5.45.119.70:1080 | EE | 1349 | 4 | 14/32 |
| http://119.188.131.55:17981 | CN | 3316 | 3 | 14/34 |
| http://219.142.66.245:9090 | CN | 1665 | 3 | 7/9 |
| http://186.33.45.218:999 | EC | 5764 | 3 | 14/23 |
| http://2.26.68.16:80 | FI | 4333 | 3 | 5/11 |
| http://37.59.125.131:8888 | FR | 2008 | 3 | 25/34 |
| http://176.111.37.216:39811 | HK | 1804 | 3 | 29/34 |
| http://103.61.234.186:8180 | ID | 1878 | 3 | 16/31 |
| http://103.172.42.47:1111 | ID | 1411 | 3 | 9/32 |
| http://121.101.131.128:8091 | ID | 1544 | 3 | 7/23 |
| http://182.253.62.26:8080 | ID | 6934 | 3 | 3/3 |
| http://185.28.155.163:1433 | IL | 850 | 3 | 3/3 |
| http://45.43.60.220:8080 | JP | 7336 | 3 | 21/33 |
| http://175.136.239.174:8181 | MY | 2702 | 3 | 21/34 |
| http://175.139.255.25:8181 | MY | 1733 | 3 | 26/34 |
| http://222.127.241.158:8082 | PH | 5730 | 3 | 8/28 |
| http://13.53.139.178:14452 | SE | 3004 | 3 | 6/25 |
| http://43.156.114.4:80 | SG | 1429 | 3 | 14/30 |
| http://43.163.112.8:80 | SG | 1024 | 3 | 15/31 |
| http://34.94.46.8:80 | US | 260 | 3 | 21/32 |
| http://190.97.238.14:999 | VE | 7773 | 3 | 3/3 |
| socks4://103.73.67.219:10800 | HK | 3783 | 3 | 3/3 |
| socks5://45.144.54.40:1080 | DE | 3174 | 3 | 25/34 |
| socks5://47.245.165.201:1080 | DE | 933 | 3 | 7/30 |
| socks5://81.0.49.104:18500 | ES | 2194 | 3 | 11/31 |
| socks5://185.185.80.58:1088 | FR | 1004 | 3 | 22/33 |
| socks5://144.24.111.128:1088 | IN | 3163 | 3 | 26/34 |
| socks5://103.75.118.84:1080 | JP | 2285 | 3 | 22/29 |
| socks5://45.95.202.92:10808 | RU | 1645 | 3 | 7/12 |
| socks5://107.191.44.214:1081 | US | 3230 | 3 | 19/34 |
| socks5://192.163.200.82:17071 | US | 4612 | 3 | 7/25 |
| http://170.168.102.55:3128 | AM | 6460 | 2 | 11/25 |
| http://38.156.71.1:999 | AR | 1418 | 2 | 3/7 |
| http://138.117.13.65:999 | AR | 1632 | 2 | 7/30 |
| http://15.135.215.62:7028 | AU | 3024 | 2 | 5/14 |
| http://16.26.143.154:59988 | AU | 6913 | 2 | 3/6 |
| http://16.51.62.173:35842 | AU | 2253 | 2 | 7/18 |
| http://16.51.148.102:4153 | AU | 2811 | 2 | 2/2 |
| http://16.51.148.102:8181 | AU | 6080 | 2 | 5/6 |
| http://54.206.129.120:41345 | AU | 2564 | 2 | 4/12 |
| http://54.253.167.61:48854 | AU | 2977 | 2 | 5/28 |
| http://54.253.167.61:9927 | AU | 3825 | 2 | 5/28 |
| http://103.142.69.62:8080 | BD | 4420 | 2 | 9/32 |
| http://175.29.127.158:2525 | BD | 2591 | 2 | 9/33 |
| http://87.237.15.238:7080 | BE | 636 | 2 | 2/2 |
| http://15.229.231.89:3080 | BR | 2134 | 2 | 4/26 |
