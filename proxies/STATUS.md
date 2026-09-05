# Proxy status

Generated 2026-09-05T21:41:01Z by `harvest.py`.

- **571** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1587** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15769** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 158/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1264 |
| socks5 | 314 |
| socks4 | 9 |

| country | entries |
|---|---|
| ID | 260 |
| US | 151 |
| CN | 123 |
| RU | 69 |
| NL | 65 |
| BD | 52 |
| MX | 51 |
| PH | 44 |
| IN | 43 |
| SG | 41 |
| DE | 40 |
| FR | 40 |
| VE | 39 |
| CO | 38 |
| HK | 36 |
| VN | 36 |
| BR | 34 |
| EC | 28 |
| TH | 27 |
| FI | 24 |
| JP | 24 |
| AR | 19 |
| KH | 19 |
| CA | 17 |
| DO | 15 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-09-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 59 | 59 | 35 | 2026-09-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 83 | 83 | 32 | 2026-09-05 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-09-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 113 | 113 | 22 | 2026-09-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 145 | 145 | 83 | 2026-09-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-09-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 207 | 207 | 34 | 2026-09-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 234 | 234 | 20 | 2026-09-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-05 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 410 | 410 | 153 | 2026-09-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 496 | 496 | 214 | 2026-09-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1124 | 2026-09-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1601 | 2026-09-05 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1810 | 1810 | 477 | 2026-09-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1842 | 1840 | 178 | 2026-09-05 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2211 | 2211 | 1578 | 2026-09-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2331 | 2329 | 703 | 2026-09-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2386 | 2384 | 1840 | 2026-09-05 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1117 | 45 | 50/53 |
| http://34.43.46.91:80 | US | 751 | 45 | 50/53 |
| http://95.211.174.135:3128 | NL | 1959 | 39 | 52/53 |
| http://204.76.203.9:3128 | NL | 868 | 39 | 52/53 |
| http://204.76.203.9:8080 | NL | 702 | 39 | 45/46 |
| http://185.200.188.234:10001 | RU | 1835 | 39 | 52/53 |
| http://130.110.103.245:3128 | SA | 1439 | 39 | 51/53 |
| http://199.7.149.96:3128 | US | 186 | 32 | 32/32 |
| http://64.112.184.210:3128 | US | 228 | 31 | 52/53 |
| http://103.211.103.170:3128 | HK | 1190 | 25 | 25/25 |
| http://68.178.174.239:3128 | US | 1039 | 21 | 21/21 |
| http://68.178.174.239:8888 | US | 1040 | 21 | 21/21 |
| http://1.231.81.166:3128 | KR | 2111 | 18 | 50/53 |
| http://189.51.168.164:999 | MX | 6753 | 18 | 18/18 |
| socks5://193.25.215.182:22222 | US | 1363 | 16 | 49/53 |
| http://116.202.172.187:11000 | DE | 1036 | 14 | 14/14 |
| http://91.134.141.4:3128 | FR | 774 | 14 | 14/14 |
| http://173.212.240.48:8888 | FR | 834 | 14 | 14/14 |
| http://5.129.254.129:8888 | RU | 1810 | 14 | 14/14 |
| socks5://171.25.158.95:1080 | SE | 5571 | 14 | 30/52 |
| http://176.111.37.5:39811 | HK | 1361 | 13 | 47/53 |
| http://14.251.13.20:8080 | VN | 1260 | 13 | 24/25 |
| http://37.59.125.131:8888 | FR | 4454 | 11 | 40/53 |
| http://154.59.56.73:999 | VE | 3991 | 11 | 22/25 |
| socks5://101.36.104.46:10808 | JP | 2466 | 11 | 49/53 |
| http://120.232.115.170:17981 | CN | 1604 | 10 | 35/52 |
| http://181.78.23.187:999 | CO | 764 | 10 | 20/22 |
| http://181.78.74.252:999 | CO | 787 | 10 | 42/44 |
| http://181.78.74.253:999 | CO | 791 | 10 | 42/44 |
| http://190.97.236.128:999 | VE | 1752 | 10 | 41/43 |
| http://190.97.236.129:999 | VE | 1778 | 10 | 41/43 |
| http://103.177.118.145:8118 | BD | 4755 | 9 | 32/34 |
| http://186.5.94.206:999 | EC | 6482 | 9 | 14/15 |
| http://197.164.101.13:1981 | EG | 7903 | 9 | 14/42 |
| http://175.136.239.173:8181 | MY | 3147 | 9 | 42/53 |
| socks5://101.36.104.239:10808 | JP | 2772 | 9 | 44/53 |
| socks5://5.255.117.127:1080 | NL | 754 | 9 | 16/29 |
| socks5://147.45.60.124:1082 | US | 4550 | 9 | 29/53 |
| http://114.236.137.41:21000 | CN | 2182 | 8 | 37/53 |
| http://176.111.37.216:39811 | HK | 1244 | 8 | 41/53 |
| http://197.224.185.3:3128 | MU | 2206 | 8 | 19/21 |
| http://5.129.254.49:8888 | RU | 2282 | 8 | 8/8 |
| http://5.129.254.51:8888 | RU | 1919 | 8 | 8/8 |
| http://5.129.254.70:8888 | RU | 2348 | 8 | 8/8 |
| http://157.85.97.240:3128 | TH | 1232 | 8 | 15/21 |
| http://157.85.111.64:3128 | TH | 1216 | 8 | 19/21 |
| http://95.3.69.222:8080 | TR | 2322 | 8 | 50/53 |
| socks4://45.61.129.165:9050 | US | 4402 | 8 | 44/53 |
| socks5://121.169.46.116:1090 | KR | 5493 | 8 | 36/53 |
| socks5://165.22.63.133:1080 | SG | 2384 | 8 | 9/10 |
| socks5://188.166.217.100:1080 | SG | 2068 | 8 | 8/8 |
| socks5://43.135.176.121:1080 | US | 2476 | 8 | 8/8 |
| http://111.192.19.39:8888 | CN | 1226 | 7 | 9/17 |
| http://5.129.254.60:8888 | RU | 1498 | 7 | 7/7 |
| http://157.85.97.204:3128 | TH | 1363 | 7 | 15/18 |
| socks5://143.198.205.96:1080 | SG | 1955 | 7 | 7/7 |
| http://114.254.48.23:8888 | CN | 1462 | 6 | 6/6 |
| http://103.237.102.191:11111 | DE | 854 | 6 | 50/53 |
| http://65.1.240.131:3001 | IN | 1242 | 6 | 6/6 |
| http://5.129.254.5:8888 | RU | 2263 | 6 | 7/8 |
| http://202.28.194.139:31280 | TH | 4108 | 6 | 50/53 |
| http://193.104.179.115:3128 | UZ | 2777 | 6 | 8/18 |
| socks5://144.91.111.48:1088 | FR | 2658 | 6 | 25/53 |
| socks5://213.199.47.140:1080 | FR | 6525 | 6 | 16/19 |
| socks5://144.24.111.128:1088 | IN | 1964 | 6 | 41/53 |
| socks5://193.233.218.121:1080 | RU | 2546 | 6 | 7/8 |
| socks5://143.198.93.65:1080 | SG | 1271 | 6 | 6/6 |
| socks5://159.223.86.111:1080 | SG | 1412 | 6 | 6/6 |
| socks5://45.32.160.61:1088 | US | 662 | 6 | 6/6 |
| socks5://185.222.138.237:1080 | XK | 1160 | 6 | 6/6 |
| http://111.192.25.85:8888 | CN | 1693 | 5 | 9/18 |
| http://167.233.89.17:1084 | DE | 1723 | 5 | 5/5 |
| http://167.233.148.141:1083 | DE | 1486 | 5 | 5/5 |
| http://167.233.169.253:1083 | DE | 4010 | 5 | 5/5 |
| http://186.33.45.218:999 | EC | 5401 | 5 | 27/42 |
| http://178.236.16.4:8888 | KZ | 1252 | 5 | 5/5 |
| http://107.167.18.122:443 | US | 396 | 5 | 5/5 |
| http://154.59.56.76:999 | VE | 5387 | 5 | 10/13 |
| http://190.97.241.106:999 | VE | 2823 | 5 | 14/37 |
| http://210.211.113.37:80 | VN | 1299 | 5 | 17/25 |
| socks5://103.210.161.8:1080 | CN | 1250 | 5 | 18/26 |
| socks5://123.58.219.171:10808 | HK | 1954 | 5 | 44/53 |
| socks5://160.22.17.4:9988 | VN | 1664 | 5 | 22/49 |
| http://34.34.190.145:8080 | BE | 1416 | 4 | 4/4 |
| http://185.191.239.248:3128 | CH | 2150 | 4 | 39/52 |
| http://27.185.218.213:17981 | CN | 1865 | 4 | 24/53 |
| http://39.106.170.168:8080 | CN | 1638 | 4 | 22/51 |
| http://47.110.226.74:19991 | CN | 6495 | 4 | 19/51 |
| http://114.249.210.133:8888 | CN | 3754 | 4 | 4/4 |
| http://18.157.123.132:3128 | DE | 688 | 4 | 13/14 |
| http://117.236.124.166:3128 | IN | 1740 | 4 | 33/53 |
| http://175.139.255.25:8181 | MY | 3583 | 4 | 38/53 |
| http://5.129.254.154:8888 | RU | 1374 | 4 | 4/4 |
| http://140.99.255.67:8181 | US | 588 | 4 | 4/4 |
| http://210.211.113.34:80 | VN | 3956 | 4 | 21/25 |
| socks5://38.49.210.79:40000 | CA | 2299 | 4 | 21/53 |
| socks5://47.76.175.249:1080 | HK | 1527 | 4 | 4/4 |
| socks5://72.56.76.200:1080 | NL | 1779 | 4 | 5/6 |
| socks5://157.245.159.157:1080 | SG | 1456 | 4 | 4/4 |
| socks5://107.175.194.203:40000 | US | 483 | 4 | 5/6 |
