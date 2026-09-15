# Proxy status

Generated 2026-09-15T17:33:15Z by `harvest.py`.

- **1085** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1781** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **21686** endpoints on record
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
| socks5 | 892 |
| http | 880 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 709 |
| ID | 191 |
| CN | 82 |
| US | 74 |
| RU | 60 |
| VN | 53 |
| CO | 47 |
| BD | 41 |
| MX | 40 |
| DE | 34 |
| SG | 32 |
| VE | 31 |
| PH | 28 |
| BR | 24 |
| EC | 24 |
| FR | 24 |
| IN | 22 |
| EG | 21 |
| HK | 17 |
| FI | 15 |
| JP | 13 |
| AR | 12 |
| KH | 11 |
| TH | 10 |
| DO | 9 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-09-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 55 | 55 | 15 | 2026-09-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 62 | 62 | 37 | 2026-09-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-09-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 151 | 151 | 68 | 2026-09-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 312 | 312 | 88 | 2026-09-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 338 | 338 | 124 | 2026-09-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 519 | 519 | 370 | 2026-09-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-09-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-09-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 634 | 634 | 124 | 2026-09-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-09-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1652 | 1648 | 367 | 2026-09-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-09-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2277 | 2275 | 521 | 2026-09-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2414 | 2412 | 712 | 2026-09-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2546 | 2544 | 1993 | 2026-09-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5913 | 5913 | 3861 | 2026-09-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11654 | 11653 | 2177 | 2026-09-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1526 | 64 | 69/72 |
| http://34.43.46.91:80 | US | 1580 | 64 | 69/72 |
| http://95.211.174.135:3128 | NL | 1620 | 58 | 71/72 |
| http://185.200.188.234:10001 | RU | 4832 | 58 | 71/72 |
| http://130.110.103.245:3128 | SA | 3094 | 58 | 70/72 |
| http://1.231.81.166:3128 | KR | 2713 | 37 | 69/72 |
| http://176.111.37.5:39811 | HK | 2748 | 32 | 66/72 |
| http://181.78.23.187:999 | CO | 769 | 29 | 39/41 |
| http://181.78.74.252:999 | CO | 1283 | 29 | 61/63 |
| http://181.78.74.253:999 | CO | 1100 | 29 | 61/63 |
| http://190.97.236.128:999 | VE | 1251 | 29 | 60/62 |
| http://190.97.236.129:999 | VE | 1019 | 29 | 60/62 |
| http://95.3.69.222:8080 | TR | 3032 | 27 | 69/72 |
| http://190.97.241.106:999 | VE | 2283 | 24 | 33/56 |
| http://45.186.6.104:3128 | EC | 865 | 20 | 49/50 |
| socks5://107.167.18.122:443 | US | 379 | 17 | 23/24 |
| http://103.237.102.191:11111 | DE | 2103 | 16 | 68/72 |
| socks5://83.147.216.208:1080 | FI | 1179 | 16 | 22/40 |
| socks5://144.91.111.48:1088 | FR | 3352 | 14 | 42/72 |
| http://184.75.221.82:3118 | CA | 1265 | 13 | 34/37 |
| socks5://144.91.121.61:1088 | FR | 4004 | 13 | 63/72 |
| http://91.134.141.4:3128 | FR | 779 | 11 | 31/33 |
| http://186.5.94.206:999 | EC | 1387 | 9 | 32/34 |
| http://107.150.41.226:18080 | US | 458 | 9 | 9/9 |
| http://14.251.13.20:8080 | VN | 1254 | 9 | 42/44 |
| socks5://213.199.47.140:1080 | FR | 6279 | 9 | 31/38 |
| socks5://161.35.90.93:1083 | NL | 2378 | 8 | 37/70 |
| http://114.236.137.41:21000 | CN | 2587 | 7 | 50/72 |
| http://45.240.232.61:8080 | EG | 3446 | 7 | 20/52 |
| http://195.158.8.123:3128 | UZ | 2482 | 7 | 48/70 |
| socks5://191.223.220.23:1080 | JP | 1116 | 7 | 19/69 |
| http://8.138.217.152:21001 | CN | 4007 | 6 | 48/72 |
| http://103.177.118.145:8118 | BD | 1680 | 5 | 49/53 |
| http://190.0.246.210:4040 | CO | 1381 | 5 | 62/71 |
| http://186.33.45.219:999 | EC | 2200 | 5 | 35/61 |
| http://65.109.217.164:3128 | FI | 1889 | 5 | 5/5 |
| http://84.8.216.230:2001 | MA | 3711 | 5 | 5/5 |
| http://43.156.199.63:8080 | SG | 2634 | 5 | 6/7 |
| http://202.28.194.139:31280 | TH | 3410 | 5 | 65/72 |
| http://38.51.207.104:8080 | VE | 5905 | 5 | 12/13 |
| http://210.211.113.34:80 | VN | 7776 | 5 | 37/44 |
| socks5://91.107.179.68:10809 | DE | 1054 | 5 | 5/5 |
| http://45.65.138.48:999 | CO | 5258 | 4 | 27/72 |
| http://172.104.56.95:8888 | SG | 1621 | 4 | 4/4 |
| http://210.211.113.33:80 | VN | 2458 | 4 | 22/42 |
| socks4://58.187.104.62:1111 | VN | 6695 | 4 | 4/4 |
| socks4://58.187.104.62:1117 | VN | 2588 | 4 | 4/4 |
| socks5://103.210.161.8:1080 | CN | 4192 | 4 | 34/45 |
| socks5://109.123.251.109:1080 | FR | 7756 | 4 | 35/72 |
| socks5://45.74.31.42:12636 | NL | 6081 | 4 | 4/4 |
| socks5://161.35.90.93:1082 | NL | 4960 | 4 | 36/72 |
| socks5://58.187.104.62:1083 | VN | 3561 | 4 | 4/4 |
| socks5://103.162.30.189:10808 | VN | 3086 | 4 | 6/7 |
| socks5://160.22.17.4:9988 | VN | 2047 | 4 | 29/68 |
| http://187.102.219.42:999 | AR | 1618 | 3 | 34/67 |
| http://185.191.239.248:3128 | CH | 2547 | 3 | 54/71 |
| http://61.149.134.158:8888 | CN | 7155 | 3 | 14/37 |
| http://114.254.48.165:8888 | CN | 2934 | 3 | 15/37 |
| http://123.121.122.28:8888 | CN | 1190 | 3 | 15/21 |
| http://221.221.162.189:8888 | CN | 6584 | 3 | 13/40 |
| http://222.128.168.101:8888 | CN | 7522 | 3 | 11/36 |
| http://222.128.171.2:8888 | CN | 6948 | 3 | 13/24 |
| http://190.12.150.244:999 | EC | 3249 | 3 | 43/68 |
| http://34.88.38.81:9443 | FI | 1087 | 3 | 24/37 |
| http://35.228.49.168:9443 | FI | 778 | 3 | 5/9 |
| http://194.163.175.167:40000 | FR | 5286 | 3 | 22/37 |
| http://176.111.37.216:39811 | HK | 4356 | 3 | 59/72 |
| http://117.236.124.166:3128 | IN | 2865 | 3 | 47/72 |
| http://212.154.169.90:3128 | KZ | 1190 | 3 | 35/51 |
| http://197.224.185.3:3128 | MU | 2354 | 3 | 36/40 |
| http://189.51.168.164:999 | MX | 624 | 3 | 36/37 |
| http://45.132.252.25:49156 | RU | 1335 | 3 | 3/3 |
| http://43.128.76.140:8080 | SG | 2755 | 3 | 4/5 |
| http://43.153.123.79:80 | US | 3764 | 3 | 3/3 |
| http://69.87.216.54:7989 | US | 269 | 3 | 12/17 |
| http://38.172.160.16:999 | VE | 5226 | 3 | 14/23 |
| http://42.96.18.62:1311 | VN | 1916 | 3 | 49/71 |
| http://58.187.104.62:2088 | VN | 2813 | 3 | 3/3 |
| http://210.211.113.37:80 | VN | 5341 | 3 | 28/44 |
| socks4://58.187.104.62:1085 | VN | 3324 | 3 | 3/3 |
| socks5://27.131.14.9:1088 | BD | 4005 | 3 | 22/71 |
| socks5://5.75.133.113:10811 | DE | 1321 | 3 | 23/43 |
| socks5://49.13.22.249:10801 | DE | 2219 | 3 | 26/41 |
| socks5://147.45.66.116:1082 | DE | 5291 | 3 | 25/71 |
| socks5://45.74.31.42:21911 | NL | 3189 | 3 | 3/3 |
| socks5://45.74.31.42:22732 | NL | 6510 | 3 | 3/3 |
| socks5://161.35.90.93:1081 | NL | 5282 | 3 | 34/72 |
| http://149.54.16.170:8080 | AF | 6831 | 2 | 5/14 |
| http://108.61.213.218:80 | AU | 1252 | 2 | 10/13 |
| http://103.251.232.40:8090 | BD | 4284 | 2 | 8/38 |
| http://38.7.195.53:999 | CL | 2703 | 2 | 20/71 |
| http://36.155.23.163:10808 | CN | 7209 | 2 | 4/9 |
| http://39.106.165.196:8080 | CN | 2028 | 2 | 35/68 |
| http://39.106.170.168:8080 | CN | 1694 | 2 | 34/70 |
| http://111.192.19.39:8888 | CN | 1968 | 2 | 18/36 |
| http://113.45.195.147:3128 | CN | 2446 | 2 | 24/37 |
| http://114.244.223.68:8888 | CN | 1584 | 2 | 21/35 |
| http://115.231.181.40:8128 | CN | 2057 | 2 | 30/71 |
| http://123.119.178.176:8888 | CN | 3088 | 2 | 16/37 |
| http://123.121.114.234:8888 | CN | 2921 | 2 | 12/31 |
