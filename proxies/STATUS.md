# Proxy status

Generated 2026-08-30T22:03:11Z by `harvest.py`.

- **1272** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1977** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15314** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 160/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1733 |
| socks5 | 232 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 405 |
| US | 166 |
| CN | 115 |
| CO | 76 |
| MX | 71 |
| DE | 64 |
| PH | 64 |
| BD | 54 |
| IN | 54 |
| BR | 46 |
| FR | 46 |
| VE | 43 |
| VN | 41 |
| HK | 39 |
| EC | 38 |
| TH | 37 |
| NL | 36 |
| RU | 35 |
| SG | 32 |
| JP | 30 |
| AU | 26 |
| CA | 24 |
| TR | 22 |
| GB | 21 |
| KH | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 2 | 2026-08-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 60 | 60 | 34 | 2026-08-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 82 | 82 | 34 | 2026-08-30 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-08-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 125 | 125 | 31 | 2026-08-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 147 | 147 | 76 | 2026-08-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 148 | 148 | 50 | 2026-08-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 149 | 149 | 35 | 2026-08-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 157 | 157 | 71 | 2026-08-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-30 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 257 | 257 | 83 | 2026-08-30 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-08-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-08-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 951 | 951 | 618 | 2026-08-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1145 | 2026-08-30 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1751 | 1748 | 218 | 2026-08-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1605 | 2026-08-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2074 | 2072 | 405 | 2026-08-30 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2225 | 2225 | 1663 | 2026-08-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2289 | 2287 | 664 | 2026-08-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2656 | 2654 | 2018 | 2026-08-30 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1032 | 38 | 40/41 |
| http://34.43.46.91:443 | US | 774 | 33 | 38/41 |
| http://34.43.46.91:80 | US | 991 | 33 | 38/41 |
| http://103.237.102.191:11111 | DE | 707 | 27 | 40/41 |
| http://95.211.174.135:3128 | NL | 1125 | 27 | 40/41 |
| http://204.76.203.9:3128 | NL | 1199 | 27 | 40/41 |
| http://204.76.203.9:8080 | NL | 502 | 27 | 33/34 |
| http://185.200.188.234:10001 | RU | 4159 | 27 | 40/41 |
| http://130.110.103.245:3128 | SA | 1356 | 27 | 39/41 |
| http://95.3.69.222:8080 | TR | 1882 | 27 | 40/41 |
| http://199.7.149.96:3128 | US | 36 | 20 | 20/20 |
| http://45.186.6.104:3128 | EC | 721 | 19 | 19/19 |
| http://64.112.184.210:3128 | US | 659 | 19 | 40/41 |
| http://42.96.18.62:1311 | VN | 2105 | 15 | 30/40 |
| socks5://144.91.121.61:1088 | FR | 1329 | 15 | 39/41 |
| http://190.0.246.211:4040 | CO | 622 | 13 | 36/41 |
| http://103.211.103.170:3128 | HK | 458 | 13 | 13/13 |
| http://202.28.194.139:31280 | TH | 1909 | 13 | 39/41 |
| socks4://45.61.129.165:9050 | US | 2667 | 13 | 33/41 |
| socks5://101.36.104.46:10808 | JP | 1470 | 13 | 38/41 |
| http://87.251.77.29:3128 | DE | 1162 | 12 | 38/41 |
| socks5://45.194.33.12:30001 | HK | 1465 | 12 | 30/37 |
| socks5://45.194.33.12:30002 | HK | 1415 | 12 | 14/15 |
| http://103.177.118.145:8118 | BD | 4683 | 11 | 21/22 |
| http://87.237.15.238:7080 | BE | 4624 | 9 | 9/9 |
| http://197.224.185.3:3128 | MU | 1742 | 9 | 9/9 |
| http://175.136.239.173:8181 | MY | 6000 | 9 | 33/41 |
| http://157.85.111.64:3128 | TH | 1615 | 9 | 9/9 |
| http://68.178.174.239:3128 | US | 1412 | 9 | 9/9 |
| http://68.178.174.239:8888 | US | 1416 | 9 | 9/9 |
| http://209.174.97.162:5999 | US | 214 | 9 | 9/9 |
| http://8.138.217.152:21001 | CN | 3346 | 8 | 28/41 |
| http://181.78.23.187:999 | CO | 680 | 8 | 9/10 |
| http://181.78.74.252:999 | CO | 666 | 8 | 31/32 |
| http://181.78.74.253:999 | CO | 661 | 8 | 31/32 |
| http://190.97.236.128:999 | VE | 602 | 8 | 30/31 |
| http://190.97.236.129:999 | VE | 597 | 8 | 30/31 |
| socks5://45.12.18.106:1080 | RU | 952 | 8 | 8/8 |
| socks5://84.8.102.52:1080 | SA | 1175 | 8 | 8/8 |
| socks5://213.199.47.140:1080 | FR | 3257 | 7 | 7/7 |
| http://87.237.15.239:7080 | BE | 553 | 6 | 6/6 |
| http://184.75.221.82:3118 | CA | 187 | 6 | 6/6 |
| http://120.232.115.170:17981 | CN | 2013 | 6 | 25/40 |
| http://123.121.115.239:8888 | CN | 1903 | 6 | 6/6 |
| http://123.121.121.123:8888 | CN | 3958 | 6 | 6/6 |
| http://190.0.246.213:4040 | CO | 2644 | 6 | 6/6 |
| http://130.61.112.125:443 | DE | 986 | 6 | 6/6 |
| http://194.163.175.167:40000 | FR | 525 | 6 | 6/6 |
| http://1.231.81.166:3128 | KR | 1215 | 6 | 38/41 |
| http://189.51.168.164:999 | MX | 378 | 6 | 6/6 |
| http://175.136.239.174:8181 | MY | 3262 | 6 | 27/41 |
| http://43.156.227.68:80 | SG | 1154 | 6 | 6/6 |
| http://43.160.242.118:3128 | SG | 1164 | 6 | 31/38 |
| http://157.85.97.203:3128 | TH | 1360 | 6 | 6/6 |
| http://157.85.97.204:3128 | TH | 1358 | 6 | 6/6 |
| http://157.85.97.242:3128 | TH | 1321 | 6 | 6/6 |
| http://157.85.105.218:3128 | TH | 1325 | 6 | 6/6 |
| http://157.85.105.220:3128 | TH | 1325 | 6 | 6/6 |
| http://157.85.108.50:3128 | TH | 1575 | 6 | 6/6 |
| http://45.59.100.205:3128 | US | 269 | 6 | 6/6 |
| socks4://158.220.99.85:4545 | FR | 3251 | 6 | 6/6 |
| socks5://47.250.211.53:1080 | MY | 1917 | 6 | 22/41 |
| socks5://185.118.143.141:1080 | TR | 4344 | 6 | 11/13 |
| http://111.192.21.92:8888 | CN | 1245 | 5 | 5/5 |
| http://84.36.141.180:1976 | EG | 1997 | 5 | 14/27 |
| http://82.64.186.155:8080 | FR | 2731 | 5 | 5/5 |
| socks5://101.36.104.239:10808 | JP | 1799 | 5 | 34/41 |
| socks5://85.209.156.148:1080 | US | 1887 | 5 | 9/12 |
| http://193.233.232.49:3131 | AT | 541 | 4 | 4/4 |
| http://103.141.174.38:11411 | BD | 4332 | 4 | 11/25 |
| http://114.244.223.68:8888 | CN | 1248 | 4 | 4/4 |
| http://221.221.165.188:8888 | CN | 1262 | 4 | 5/6 |
| http://128.140.113.110:8081 | DE | 1775 | 4 | 4/4 |
| http://85.193.65.88:8888 | RU | 1287 | 4 | 12/31 |
| socks5://121.169.46.116:1090 | KR | 1394 | 4 | 27/41 |
| socks5://109.200.111.171:1080 | RU | 4913 | 4 | 17/40 |
| socks5://193.25.215.182:22222 | US | 901 | 4 | 37/41 |
| http://179.41.11.138:8080 | AR | 771 | 3 | 12/13 |
| http://181.10.138.226:8083 | AR | 7126 | 3 | 3/3 |
| http://185.191.239.248:3128 | CH | 993 | 3 | 29/40 |
| http://47.107.82.96:30051 | CN | 5978 | 3 | 23/34 |
| http://101.251.204.174:8080 | CN | 4449 | 3 | 13/27 |
| http://111.230.27.213:3128 | CN | 5633 | 3 | 17/41 |
| http://114.249.218.6:8888 | CN | 1288 | 3 | 4/6 |
| http://114.249.220.157:8888 | CN | 1550 | 3 | 5/6 |
| http://123.115.233.96:8888 | CN | 1578 | 3 | 5/6 |
| http://123.121.129.198:8888 | CN | 1603 | 3 | 5/6 |
| http://219.142.66.245:9090 | CN | 1749 | 3 | 11/16 |
| http://190.60.42.141:555 | CO | 5767 | 3 | 3/3 |
| http://45.71.186.213:999 | EC | 5225 | 3 | 11/25 |
| http://177.234.217.235:999 | EC | 7550 | 3 | 5/10 |
| http://186.5.94.206:999 | EC | 761 | 3 | 3/3 |
| http://186.33.45.219:999 | EC | 2492 | 3 | 22/30 |
| http://45.240.232.61:8080 | EG | 945 | 3 | 8/21 |
| http://47.57.69.227:3128 | HK | 3337 | 3 | 11/13 |
| http://36.93.56.58:8080 | ID | 7859 | 3 | 8/35 |
| http://38.188.63.147:8080 | ID | 6653 | 3 | 4/6 |
| http://45.123.143.10:8080 | ID | 4161 | 3 | 10/37 |
| http://45.198.20.166:8080 | ID | 7812 | 3 | 10/35 |
| http://140.245.238.56:53 | IN | 5352 | 3 | 10/37 |
