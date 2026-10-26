# Proxy status

Generated 2026-10-26T23:19:08Z by `harvest.py`.

- **2914** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4276** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39649** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 156/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2442 |
| http | 1826 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 2251 |
| ID | 552 |
| US | 95 |
| CO | 88 |
| PH | 82 |
| RU | 78 |
| MX | 71 |
| ?? | 69 |
| CN | 61 |
| BD | 60 |
| BR | 58 |
| VE | 51 |
| TH | 47 |
| VN | 47 |
| EC | 45 |
| IN | 36 |
| AR | 35 |
| SG | 30 |
| DE | 29 |
| TR | 29 |
| DO | 28 |
| JP | 25 |
| EG | 24 |
| PK | 21 |
| HK | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-10-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 128 | 128 | 2 | 2026-10-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 134 | 134 | 79 | 2026-10-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 139 | 139 | 49 | 2026-10-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 88 | 2026-10-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 154 | 154 | 44 | 2026-10-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 291 | 291 | 141 | 2026-10-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 350 | 350 | 142 | 2026-10-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 672 | 672 | 337 | 2026-10-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1124 | 2026-10-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1733 | 1729 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-10-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2324 | 2322 | 784 | 2026-10-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2622 | 2620 | 1795 | 2026-10-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3318 | 3316 | 1112 | 2026-10-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 79332 | 79332 | 64754 | 2026-10-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 84959 | 84958 | 2238 | 2026-10-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1012 | 74 | 141/154 |
| http://149.130.173.58:9443 | CO | 601 | 65 | 65/65 |
| http://190.0.246.213:4040 | CO | 615 | 48 | 111/119 |
| http://103.237.102.191:11111 | DE | 955 | 41 | 147/154 |
| http://45.186.6.104:3128 | EC | 783 | 35 | 125/132 |
| http://103.133.26.72:8080 | ID | 1243 | 30 | 35/80 |
| http://103.133.26.73:3128 | ID | 1328 | 30 | 50/132 |
| http://103.133.26.119:8080 | ID | 1616 | 30 | 34/64 |
| http://176.111.37.5:39811 | HK | 1091 | 25 | 135/154 |
| http://34.43.46.91:80 | US | 492 | 24 | 148/154 |
| socks5://43.245.199.34:1080 | HK | 1233 | 23 | 23/23 |
| http://4.144.146.21:80 | SG | 995 | 22 | 39/46 |
| http://190.0.246.210:4040 | CO | 820 | 21 | 140/153 |
| http://43.155.62.157:443 | HK | 1054 | 21 | 49/57 |
| http://102.244.78.61:8081 | CM | 1363 | 20 | 33/40 |
| http://186.5.94.206:999 | EC | 1038 | 19 | 107/116 |
| http://184.75.221.82:3118 | CA | 472 | 18 | 105/119 |
| http://189.51.168.165:999 | MX | 476 | 18 | 61/66 |
| http://176.111.37.216:39811 | HK | 943 | 17 | 126/154 |
| http://103.130.61.61:8081 | ID | 5465 | 16 | 124/154 |
| http://185.191.239.248:3128 | CH | 1224 | 14 | 110/153 |
| http://103.133.26.50:8080 | ID | 1298 | 14 | 33/55 |
| socks5://129.146.121.2:10808 | US | 1138 | 11 | 11/11 |
| http://181.78.195.136:999 | EC | 833 | 10 | 10/10 |
| http://103.130.61.60:8081 | ID | 3898 | 10 | 10/10 |
| http://162.214.159.94:3128 | US | 127 | 10 | 10/10 |
| http://123.121.132.234:8888 | CN | 1229 | 9 | 13/15 |
| http://146.190.80.158:9090 | SG | 946 | 9 | 58/80 |
| socks5://67.207.92.87:1088 | US | 581 | 9 | 95/153 |
| socks5://69.55.49.177:38182 | US | 552 | 9 | 9/9 |
| http://5.129.254.5:8888 | RU | 2342 | 8 | 93/109 |
| http://5.129.254.49:8888 | RU | 1355 | 8 | 94/109 |
| http://5.129.254.51:8888 | RU | 1833 | 8 | 94/109 |
| http://5.129.254.60:8888 | RU | 1310 | 8 | 93/108 |
| http://5.129.254.70:8888 | RU | 2313 | 8 | 94/109 |
| http://5.129.254.129:8888 | RU | 1270 | 8 | 99/115 |
| http://5.129.254.154:8888 | RU | 3295 | 8 | 90/105 |
| http://5.129.254.215:8888 | RU | 1367 | 8 | 43/51 |
| http://5.129.254.243:8888 | RU | 1268 | 8 | 43/50 |
| http://147.45.164.178:8888 | RU | 1478 | 8 | 23/28 |
| http://64.118.155.2:22222 | US | 274 | 8 | 8/8 |
| socks5://101.36.104.46:10808 | JP | 1438 | 8 | 133/154 |
| http://15.229.149.81:3128 | BR | 3156 | 7 | 35/64 |
| http://89.167.124.218:8888 | DE | 988 | 7 | 7/7 |
| http://45.65.224.74:999 | AR | 1113 | 6 | 14/19 |
| http://102.244.78.61:8080 | CM | 1433 | 6 | 35/43 |
| http://102.244.78.61:8082 | CM | 1457 | 6 | 35/43 |
| http://102.244.78.61:8083 | CM | 1331 | 6 | 35/42 |
| http://102.244.78.61:8084 | CM | 1358 | 6 | 33/42 |
| http://102.244.78.61:8085 | CM | 1383 | 6 | 33/44 |
| http://102.244.78.61:8086 | CM | 1365 | 6 | 34/42 |
| http://102.244.78.61:8087 | CM | 1394 | 6 | 32/44 |
| http://102.244.78.61:8088 | CM | 1340 | 6 | 34/42 |
| http://102.244.78.61:8089 | CM | 1391 | 6 | 33/42 |
| http://102.244.78.61:8090 | CM | 1402 | 6 | 35/46 |
| http://103.119.19.218:3128 | CZ | 804 | 6 | 54/67 |
| socks5://47.87.97.94:1080 | TH | 1378 | 6 | 26/30 |
| http://15.217.214.40:36960 | ES | 4682 | 5 | 5/5 |
| http://43.202.114.177:7428 | KR | 3205 | 5 | 28/68 |
| http://38.194.246.34:999 | MX | 4111 | 5 | 85/145 |
| http://154.59.56.78:999 | VE | 2911 | 5 | 76/110 |
| http://187.102.219.42:999 | AR | 1213 | 4 | 83/149 |
| http://51.85.44.162:8089 | IL | 1827 | 4 | 4/4 |
| http://157.120.37.23:3128 | JP | 1613 | 4 | 8/10 |
| http://185.238.238.165:58080 | PL | 1152 | 4 | 19/44 |
| http://159.223.41.216:9090 | SG | 947 | 4 | 81/114 |
| http://49.229.100.235:8080 | TH | 1305 | 4 | 66/102 |
| http://61.91.162.126:8080 | TH | 1302 | 4 | 73/97 |
| http://103.10.231.189:8080 | TH | 1861 | 4 | 100/139 |
| socks5://107.191.47.162:1081 | FR | 804 | 4 | 4/4 |
| socks5://47.238.126.208:1080 | HK | 1048 | 4 | 30/59 |
| socks5://103.38.82.221:5555 | HK | 1178 | 4 | 9/30 |
| socks5://45.74.31.40:4863 | NL | 4343 | 4 | 5/9 |
| socks5://45.74.31.41:5560 | NL | 6418 | 4 | 13/54 |
| socks5://45.74.31.42:5793 | NL | 2514 | 4 | 4/4 |
| socks5://51.15.20.32:1088 | NL | 1042 | 4 | 15/18 |
| socks5://47.251.127.154:1080 | US | 5790 | 4 | 32/107 |
| socks5://166.1.90.114:1090 | US | 481 | 4 | 10/13 |
| http://16.26.208.68:18596 | AU | 3178 | 3 | 41/119 |
| http://16.26.208.68:9005 | AU | 6538 | 3 | 5/13 |
| http://179.43.10.233:8874 | BR | 6140 | 3 | 22/146 |
| http://35.183.29.62:8181 | CA | 2405 | 3 | 27/122 |
| http://45.161.112.227:999 | CL | 2842 | 3 | 41/147 |
| http://47.110.226.74:19991 | CN | 5819 | 3 | 62/152 |
| http://122.246.3.12:17981 | CN | 1726 | 3 | 67/148 |
| http://45.65.137.218:999 | CO | 3111 | 3 | 47/119 |
| http://179.1.221.26:3128 | CO | 1526 | 3 | 31/94 |
| http://45.71.186.211:999 | EC | 5403 | 3 | 46/107 |
| http://177.234.217.235:999 | EC | 2794 | 3 | 56/123 |
| http://190.12.150.244:999 | EC | 1691 | 3 | 108/150 |
| http://43.99.60.244:8089 | HK | 914 | 3 | 56/104 |
| http://112.121.173.84:808 | HK | 2970 | 3 | 5/6 |
| http://36.50.56.105:8818 | ID | 3967 | 3 | 24/150 |
| http://36.64.193.226:8080 | ID | 5920 | 3 | 25/149 |
| http://103.55.225.54:8080 | ID | 7257 | 3 | 20/114 |
| http://103.144.54.71:8082 | ID | 3747 | 3 | 32/90 |
| http://103.147.134.33:8082 | ID | 3762 | 3 | 28/109 |
| http://103.147.134.116:8082 | ID | 4601 | 3 | 36/113 |
| http://103.171.12.2:8080 | IN | 7594 | 3 | 21/117 |
| http://46.209.30.11:8080 | IR | 1898 | 3 | 15/17 |
