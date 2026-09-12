# Proxy status

Generated 2026-09-12T16:10:01Z by `harvest.py`.

- **702** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1529** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **17172** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 146/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1106 |
| socks5 | 414 |
| socks4 | 9 |

| country | entries |
|---|---|
| ID | 278 |
| NL | 157 |
| CN | 112 |
| US | 90 |
| MX | 63 |
| RU | 62 |
| CO | 56 |
| BD | 50 |
| PH | 49 |
| VE | 44 |
| VN | 42 |
| BR | 36 |
| SG | 33 |
| DE | 31 |
| EC | 27 |
| FR | 27 |
| IN | 25 |
| DO | 23 |
| EG | 21 |
| TH | 21 |
| KH | 20 |
| CL | 18 |
| HK | 17 |
| AR | 16 |
| TR | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-09-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 32 | 32 | 18 | 2026-09-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 93 | 93 | 26 | 2026-09-12 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-09-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 165 | 165 | 97 | 2026-09-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 169 | 169 | 45 | 2026-09-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 208 | 208 | 83 | 2026-09-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 263 | 263 | 153 | 2026-09-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 305 | 305 | 86 | 2026-09-12 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 342 | 342 | 152 | 2026-09-12 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 534 | 2026-09-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-09-12 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1450 | 1446 | 363 | 2026-09-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1123 | 2026-09-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1600 | 2026-09-12 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2414 | 2414 | 1671 | 2026-09-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2760 | 2758 | 553 | 2026-09-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2867 | 2865 | 717 | 2026-09-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3107 | 3105 | 2356 | 2026-09-12 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 673 | 58 | 63/66 |
| http://34.43.46.91:80 | US | 630 | 58 | 63/66 |
| http://95.211.174.135:3128 | NL | 1046 | 52 | 65/66 |
| http://185.200.188.234:10001 | RU | 1195 | 52 | 65/66 |
| http://130.110.103.245:3128 | SA | 1605 | 52 | 64/66 |
| http://1.231.81.166:3128 | KR | 956 | 31 | 63/66 |
| http://189.51.168.164:999 | MX | 1729 | 31 | 31/31 |
| http://176.111.37.5:39811 | HK | 1061 | 26 | 60/66 |
| http://181.78.23.187:999 | CO | 796 | 23 | 33/35 |
| http://181.78.74.252:999 | CO | 920 | 23 | 55/57 |
| http://181.78.74.253:999 | CO | 858 | 23 | 55/57 |
| http://190.97.236.128:999 | VE | 879 | 23 | 54/56 |
| http://190.97.236.129:999 | VE | 875 | 23 | 54/56 |
| http://176.111.37.216:39811 | HK | 1158 | 21 | 54/66 |
| http://5.129.254.49:8888 | RU | 1360 | 21 | 21/21 |
| http://5.129.254.51:8888 | RU | 2061 | 21 | 21/21 |
| http://5.129.254.70:8888 | RU | 1273 | 21 | 21/21 |
| http://95.3.69.222:8080 | TR | 1612 | 21 | 63/66 |
| http://5.129.254.60:8888 | RU | 1311 | 20 | 20/20 |
| http://5.129.254.5:8888 | RU | 1314 | 19 | 20/21 |
| http://190.97.241.106:999 | VE | 3564 | 18 | 27/50 |
| http://5.129.254.154:8888 | RU | 1364 | 17 | 17/17 |
| socks5://108.174.152.80:1080 | MX | 1467 | 15 | 15/15 |
| http://45.186.6.104:3128 | EC | 818 | 14 | 43/44 |
| http://190.0.246.211:4040 | CO | 1833 | 13 | 57/66 |
| http://37.59.125.131:8888 | FR | 3035 | 11 | 52/66 |
| http://107.167.18.122:443 | US | 89 | 11 | 17/18 |
| http://103.237.102.191:11111 | DE | 982 | 10 | 62/66 |
| socks5://83.147.216.208:1080 | FI | 1270 | 10 | 16/34 |
| http://61.91.162.126:8080 | TH | 1203 | 9 | 9/9 |
| http://103.10.231.189:8080 | TH | 1470 | 9 | 34/51 |
| http://167.233.169.253:1084 | DE | 5746 | 8 | 14/15 |
| http://201.71.2.26:999 | VE | 2239 | 8 | 22/59 |
| socks5://144.91.111.48:1088 | FR | 6373 | 8 | 36/66 |
| socks5://101.36.104.46:10808 | JP | 2500 | 8 | 59/66 |
| socks5://45.32.160.61:1088 | US | 466 | 8 | 18/19 |
| http://108.61.213.218:80 | AU | 923 | 7 | 7/7 |
| http://184.75.221.82:3118 | CA | 447 | 7 | 28/31 |
| http://113.45.195.147:3128 | CN | 1709 | 7 | 20/31 |
| http://45.65.138.48:999 | CO | 5315 | 7 | 23/66 |
| http://41.33.219.140:1981 | EG | 6015 | 7 | 20/48 |
| http://5.129.254.129:8888 | RU | 1303 | 7 | 26/27 |
| http://38.51.207.104:8080 | VE | 5305 | 7 | 7/7 |
| http://154.59.56.72:999 | VE | 6503 | 7 | 18/25 |
| socks5://5.45.119.70:1080 | EE | 1084 | 7 | 34/64 |
| socks5://144.91.121.61:1088 | FR | 2986 | 7 | 57/66 |
| http://103.130.61.61:8081 | ID | 2314 | 6 | 54/66 |
| http://197.224.185.3:3128 | MU | 2128 | 6 | 31/34 |
| http://201.71.2.24:999 | VE | 3566 | 6 | 17/54 |
| socks5://141.148.158.143:1080 | US | 3377 | 6 | 35/65 |
| http://91.134.141.4:3128 | FR | 856 | 5 | 25/27 |
| http://157.85.111.64:3128 | TH | 2097 | 5 | 28/34 |
| http://154.59.56.76:999 | VE | 4320 | 5 | 21/26 |
| socks5://31.211.142.115:8192 | BG | 6995 | 5 | 14/64 |
| socks5://43.156.84.41:10808 | SG | 1066 | 5 | 5/5 |
| socks5://144.24.47.42:1080 | US | 2255 | 5 | 32/62 |
| http://123.113.148.188:8888 | CN | 1955 | 4 | 9/21 |
| http://123.121.210.208:8888 | CN | 6209 | 4 | 9/18 |
| http://205.164.192.115:999 | MX | 6831 | 4 | 39/64 |
| http://91.233.223.147:3128 | RU | 1374 | 4 | 11/40 |
| http://159.223.41.216:9090 | SG | 4112 | 4 | 16/26 |
| http://167.172.76.176:9090 | SG | 921 | 4 | 13/27 |
| http://70.61.188.34:3128 | US | 5177 | 4 | 9/25 |
| http://154.59.56.74:999 | VE | 2357 | 4 | 19/29 |
| socks5://51.178.49.241:1088 | FR | 1711 | 4 | 22/27 |
| socks5://144.126.197.184:1088 | GB | 950 | 4 | 17/22 |
| socks5://103.165.128.75:1080 | ID | 3416 | 4 | 14/51 |
| socks5://144.24.111.128:1088 | IN | 1536 | 4 | 50/66 |
| socks5://103.75.118.84:1080 | JP | 2819 | 4 | 44/61 |
| socks5://5.130.50.118:1080 | RU | 2623 | 4 | 12/39 |
| http://109.236.45.95:8989 | AL | 2179 | 3 | 19/62 |
| http://185.191.239.248:3128 | CH | 1777 | 3 | 50/65 |
| http://47.107.107.24:80 | CN | 3533 | 3 | 20/34 |
| http://61.149.132.196:8888 | CN | 1978 | 3 | 4/11 |
| http://111.196.31.158:8888 | CN | 3404 | 3 | 8/12 |
| http://152.53.183.107:8081 | DE | 3450 | 3 | 13/19 |
| http://167.233.169.253:1083 | DE | 2541 | 3 | 16/18 |
| http://186.5.94.206:999 | EC | 1343 | 3 | 26/28 |
| http://197.164.101.13:1981 | EG | 3570 | 3 | 22/55 |
| http://197.164.101.14:1976 | EG | 3522 | 3 | 14/38 |
| http://103.176.96.225:8082 | ID | 5917 | 3 | 4/11 |
| http://103.194.46.99:8082 | ID | 7498 | 3 | 13/64 |
| http://117.236.124.166:3128 | IN | 1695 | 3 | 42/66 |
| http://160.238.65.6:3128 | NL | 3516 | 3 | 15/48 |
| http://43.156.199.63:8081 | SG | 2639 | 3 | 3/3 |
| http://213.163.196.45:80 | SG | 1896 | 3 | 3/3 |
| http://40.160.136.215:8081 | US | 3148 | 3 | 5/6 |
| http://104.218.199.249:16062 | US | 2133 | 3 | 5/9 |
| http://38.58.191.16:999 | VE | 5333 | 3 | 3/3 |
| http://38.172.179.192:999 | VE | 5161 | 3 | 16/60 |
| http://154.59.56.78:999 | VE | 5754 | 3 | 13/22 |
| http://190.97.226.44:999 | VE | 7140 | 3 | 12/62 |
| http://200.59.191.27:999 | VE | 2762 | 3 | 37/61 |
| http://14.251.13.20:8080 | VN | 1165 | 3 | 36/38 |
| socks5://118.179.195.140:9090 | BD | 3728 | 3 | 10/17 |
| socks5://177.52.25.34:1080 | BR | 6755 | 3 | 13/64 |
| socks5://103.210.161.8:1080 | CN | 1027 | 3 | 29/39 |
| socks5://193.233.139.106:1080 | FI | 1266 | 3 | 12/24 |
| socks5://109.123.251.109:1080 | FR | 3258 | 3 | 30/66 |
| socks5://213.199.47.140:1080 | FR | 2326 | 3 | 25/32 |
