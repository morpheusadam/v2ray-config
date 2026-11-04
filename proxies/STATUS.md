# Proxy status

Generated 2026-11-04T00:11:34Z by `harvest.py`.

- **3983** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35250** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 209/600 (35%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3331 |
| socks5 | 2647 |
| socks4 | 22 |

| country | entries |
|---|---|
| NL | 2465 |
| ID | 1047 |
| CO | 175 |
| PH | 162 |
| US | 156 |
| MX | 138 |
| TH | 117 |
| VE | 102 |
| BR | 99 |
| TR | 93 |
| IN | 81 |
| VN | 81 |
| RU | 79 |
| CN | 73 |
| BD | 72 |
| DO | 71 |
| EC | 71 |
| AR | 67 |
| DE | 55 |
| PE | 50 |
| EG | 45 |
| ZA | 44 |
| CL | 35 |
| SG | 34 |
| PK | 33 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-11-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 45 | 2026-11-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 69 | 2026-11-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 242 | 242 | 61 | 2026-11-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 242 | 242 | 72 | 2026-11-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 304 | 304 | 189 | 2026-11-04 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-11-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 777 | 777 | 266 | 2026-11-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1226 | 1226 | 291 | 2026-11-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1119 | 2026-11-04 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1630 | 1630 | 139 | 2026-11-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1653 | 1653 | 642 | 2026-11-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2640 | 2640 | 667 | 2026-11-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3105 | 3105 | 1824 | 2026-11-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3815 | 3815 | 886 | 2026-11-04 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4976 | 4976 | 3712 | 2026-11-04 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11678 | 11677 | 2583 | 2026-11-04 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 501 | 81 | 81/81 |
| http://103.237.102.191:11111 | DE | 695 | 57 | 163/170 |
| http://103.133.26.73:3128 | ID | 1465 | 46 | 66/148 |
| http://176.111.37.5:39811 | HK | 812 | 41 | 151/170 |
| http://34.43.46.91:80 | US | 610 | 40 | 164/170 |
| http://4.144.146.21:80 | SG | 1036 | 38 | 55/62 |
| http://176.111.37.216:39811 | HK | 925 | 33 | 142/170 |
| http://34.43.46.91:443 | US | 374 | 19 | 159/170 |
| http://167.172.76.176:9090 | SG | 1037 | 17 | 94/131 |
| socks5://101.36.104.239:10808 | JP | 3431 | 17 | 146/170 |
| http://130.110.103.245:3128 | SA | 1372 | 16 | 152/170 |
| socks5://193.25.215.182:22222 | US | 798 | 16 | 143/170 |
| http://103.133.26.72:8080 | ID | 2298 | 13 | 50/96 |
| http://45.189.57.114:3129 | EC | 791 | 12 | 12/12 |
| http://154.59.56.78:999 | VE | 5805 | 12 | 89/126 |
| http://102.244.78.61:8085 | CM | 1336 | 11 | 48/60 |
| http://102.244.78.61:8087 | CM | 1319 | 11 | 47/60 |
| http://102.244.78.61:8090 | CM | 1353 | 10 | 48/62 |
| http://130.127.204.197:8080 | US | 265 | 10 | 10/10 |
| http://38.172.160.16:999 | VE | 3695 | 10 | 73/121 |
| http://45.65.224.74:999 | AR | 5109 | 9 | 28/35 |
| http://123.200.8.170:10000 | BD | 2369 | 9 | 76/168 |
| http://102.244.78.61:8082 | CM | 1354 | 9 | 48/59 |
| http://190.12.150.244:999 | EC | 1223 | 9 | 122/166 |
| http://154.59.56.72:999 | VE | 3898 | 9 | 96/129 |
| socks5://69.55.49.177:38182 | US | 363 | 9 | 24/25 |
| http://186.96.111.214:999 | CO | 1495 | 8 | 78/159 |
| http://195.226.213.251:8888 | UA | 6270 | 8 | 68/164 |
| http://165.154.162.73:8888 | US | 1006 | 8 | 113/170 |
| socks5://45.61.129.165:9050 | US | 5556 | 8 | 129/170 |
| http://190.123.83.137:999 | AR | 1195 | 7 | 7/7 |
| http://190.0.246.213:4040 | CO | 602 | 7 | 125/135 |
| http://43.155.62.157:443 | HK | 2064 | 7 | 63/73 |
| http://160.22.207.95:8082 | ID | 3308 | 7 | 41/148 |
| http://189.51.168.165:999 | MX | 484 | 7 | 76/82 |
| http://154.59.56.74:999 | VE | 5003 | 7 | 90/133 |
| socks5://101.36.104.46:10808 | JP | 4915 | 7 | 146/170 |
| http://128.201.30.222:8666 | BR | 3089 | 6 | 9/16 |
| http://8.243.167.51:999 | CO | 7809 | 6 | 16/57 |
| http://45.65.137.218:999 | CO | 2511 | 6 | 58/135 |
| http://131.221.40.131:4040 | CO | 598 | 6 | 8/9 |
| http://177.234.217.83:999 | EC | 1550 | 6 | 13/17 |
| http://177.234.217.92:999 | EC | 2656 | 6 | 14/19 |
| http://37.187.109.70:10111 | FR | 2580 | 6 | 59/170 |
| http://103.133.26.119:8080 | ID | 1970 | 6 | 49/80 |
| http://103.155.196.83:8082 | ID | 6519 | 6 | 35/83 |
| http://160.19.146.221:2022 | ID | 3145 | 6 | 39/135 |
| http://160.22.45.114:8080 | ID | 4881 | 6 | 18/29 |
| http://202.47.185.153:8090 | ID | 3210 | 6 | 28/125 |
| http://140.238.32.108:3128 | JP | 901 | 6 | 95/169 |
| http://82.152.138.127:999 | MX | 311 | 6 | 46/132 |
| http://189.51.168.164:999 | MX | 538 | 6 | 6/6 |
| http://38.172.130.175:999 | PE | 6257 | 6 | 23/56 |
| http://152.42.170.187:9090 | SG | 1058 | 6 | 6/6 |
| http://49.229.100.235:8080 | TH | 1423 | 6 | 78/118 |
| http://171.100.254.137:8080 | TH | 1384 | 6 | 6/6 |
| http://23.94.68.53:3128 | US | 2616 | 6 | 6/6 |
| socks5://176.124.206.150:8443 | FI | 1373 | 6 | 6/6 |
| socks5://8.219.122.8:9999 | SG | 3145 | 6 | 26/60 |
| http://187.102.219.64:999 | AR | 1296 | 5 | 67/109 |
| http://185.191.239.248:3128 | CH | 960 | 5 | 121/169 |
| http://186.67.94.10:999 | CL | 6223 | 5 | 31/165 |
| http://102.244.78.61:8080 | CM | 1296 | 5 | 48/59 |
| http://102.244.78.61:8084 | CM | 1330 | 5 | 46/58 |
| http://114.244.221.178:8888 | CN | 2167 | 5 | 48/93 |
| http://38.95.88.126:999 | DO | 6050 | 5 | 23/121 |
| http://41.33.245.139:1976 | EG | 1094 | 5 | 8/9 |
| http://43.161.254.16:3128 | HK | 2360 | 5 | 7/10 |
| http://103.130.61.61:8081 | ID | 1460 | 5 | 139/170 |
| http://103.172.42.123:1111 | ID | 3275 | 5 | 30/168 |
| http://103.193.145.51:8080 | ID | 4099 | 5 | 5/5 |
| http://161.248.176.2:8080 | IN | 5446 | 5 | 24/99 |
| http://187.251.224.167:8081 | MX | 1089 | 5 | 42/130 |
| http://49.149.24.144:8082 | PH | 5341 | 5 | 6/9 |
| http://119.93.207.214:8082 | PH | 1822 | 5 | 37/162 |
| http://128.199.116.219:9090 | SG | 1044 | 5 | 70/89 |
| http://61.91.162.126:8080 | TH | 1386 | 5 | 83/113 |
| http://103.10.231.189:8080 | TH | 1631 | 5 | 110/155 |
| http://38.63.98.55:999 | VE | 2449 | 5 | 14/34 |
| http://38.172.181.0:999 | VE | 4040 | 5 | 37/77 |
| http://154.59.56.76:999 | VE | 4607 | 5 | 93/130 |
| socks5://84.200.89.140:1080 | DE | 1466 | 5 | 5/5 |
| socks5://195.201.246.53:1086 | DE | 1772 | 5 | 5/5 |
| socks5://103.191.218.119:69 | ID | 3656 | 5 | 43/156 |
| http://45.65.224.125:999 | AR | 4105 | 4 | 22/32 |
| http://181.209.109.173:3128 | AR | 5580 | 4 | 4/4 |
| http://103.134.56.148:8080 | BD | 3072 | 4 | 35/112 |
| http://184.75.221.82:3118 | CA | 243 | 4 | 117/135 |
| http://192.18.158.84:3128 | CA | 3318 | 4 | 4/4 |
| http://102.244.78.61:8081 | CM | 1351 | 4 | 45/56 |
| http://27.185.218.213:17981 | CN | 1750 | 4 | 66/170 |
| http://123.121.122.142:8888 | CN | 2827 | 4 | 9/16 |
| http://45.65.138.48:999 | CO | 2352 | 4 | 75/170 |
| http://190.0.246.210:4040 | CO | 800 | 4 | 155/169 |
| http://190.144.238.66:8080 | CO | 2355 | 4 | 25/120 |
| http://167.233.243.116:3128 | DE | 757 | 4 | 4/4 |
| http://167.233.243.116:3129 | DE | 714 | 4 | 4/4 |
| http://38.50.165.126:999 | DO | 4200 | 4 | 25/93 |
| http://177.234.217.93:999 | EC | 1704 | 4 | 18/29 |
| http://41.33.89.100:1976 | EG | 4119 | 4 | 10/32 |
