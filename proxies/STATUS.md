# Proxy status

Generated 2026-09-16T17:38:55Z by `harvest.py`.

- **1354** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2132** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **23954** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 148/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1115 |
| http | 1006 |
| socks4 | 11 |

| country | entries |
|---|---|
| NL | 918 |
| ID | 224 |
| CN | 90 |
| RU | 72 |
| US | 66 |
| VN | 57 |
| BD | 51 |
| CO | 50 |
| MX | 46 |
| DE | 38 |
| SG | 38 |
| PH | 34 |
| VE | 31 |
| FR | 30 |
| IN | 29 |
| EG | 25 |
| BR | 23 |
| EC | 23 |
| FI | 18 |
| CA | 17 |
| JP | 17 |
| HK | 16 |
| KH | 15 |
| TH | 15 |
| CL | 14 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 63 | 63 | 35 | 2026-09-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 68 | 68 | 30 | 2026-09-16 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 125 | 125 | 41 | 2026-09-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 136 | 136 | 43 | 2026-09-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-09-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 157 | 157 | 52 | 2026-09-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 368 | 368 | 107 | 2026-09-16 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 547 | 547 | 443 | 2026-09-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-09-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-09-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1598 | 2026-09-16 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1957 | 1953 | 454 | 2026-09-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2341 | 2339 | 701 | 2026-09-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2428 | 2426 | 1937 | 2026-09-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2475 | 2473 | 699 | 2026-09-16 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 8503 | 8503 | 5595 | 2026-09-16 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 13935 | 13934 | 2115 | 2026-09-16 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1554 | 66 | 71/74 |
| http://34.43.46.91:80 | US | 1734 | 66 | 71/74 |
| http://95.211.174.135:3128 | NL | 922 | 60 | 73/74 |
| http://185.200.188.234:10001 | RU | 2817 | 60 | 73/74 |
| http://130.110.103.245:3128 | SA | 1447 | 60 | 72/74 |
| http://1.231.81.166:3128 | KR | 1240 | 39 | 71/74 |
| http://176.111.37.5:39811 | HK | 2050 | 34 | 68/74 |
| http://190.97.236.128:999 | VE | 1779 | 31 | 62/64 |
| http://190.97.236.129:999 | VE | 1819 | 31 | 62/64 |
| http://95.3.69.222:8080 | TR | 1326 | 29 | 71/74 |
| http://190.97.241.106:999 | VE | 1650 | 26 | 35/58 |
| socks5://107.167.18.122:443 | US | 1399 | 19 | 25/26 |
| http://103.237.102.191:11111 | DE | 995 | 18 | 70/74 |
| socks5://83.147.216.208:1080 | FI | 2063 | 18 | 24/42 |
| socks5://144.91.111.48:1088 | FR | 1620 | 16 | 44/74 |
| http://184.75.221.82:3118 | CA | 319 | 15 | 36/39 |
| socks5://144.91.121.61:1088 | FR | 5443 | 15 | 65/74 |
| http://91.134.141.4:3128 | FR | 652 | 13 | 33/35 |
| http://186.5.94.206:999 | EC | 1988 | 11 | 34/36 |
| http://107.150.41.226:18080 | US | 6511 | 11 | 11/11 |
| socks5://213.199.47.140:1080 | FR | 2226 | 11 | 33/40 |
| http://103.177.118.145:8118 | BD | 4015 | 7 | 51/55 |
| http://190.0.246.210:4040 | CO | 5181 | 7 | 64/73 |
| http://186.33.45.219:999 | EC | 1816 | 7 | 37/63 |
| http://84.8.216.230:2001 | MA | 2811 | 7 | 7/7 |
| http://43.156.199.63:8080 | SG | 2005 | 7 | 8/9 |
| http://38.51.207.104:8080 | VE | 774 | 7 | 14/15 |
| http://172.104.56.95:8888 | SG | 3041 | 6 | 6/6 |
| socks5://109.123.251.109:1080 | FR | 3457 | 6 | 37/74 |
| socks5://161.35.90.93:1082 | NL | 2419 | 6 | 38/74 |
| socks5://103.162.30.189:10808 | VN | 3573 | 6 | 8/9 |
| socks5://160.22.17.4:9988 | VN | 1553 | 6 | 31/70 |
| http://34.88.38.81:9443 | FI | 970 | 5 | 26/39 |
| http://35.228.49.168:9443 | FI | 807 | 5 | 7/11 |
| http://197.224.185.3:3128 | MU | 1869 | 5 | 38/42 |
| http://189.51.168.164:999 | MX | 1526 | 5 | 38/39 |
| http://45.132.252.25:49156 | RU | 1709 | 5 | 5/5 |
| http://210.211.113.37:80 | VN | 2871 | 5 | 30/46 |
| http://108.61.213.218:80 | AU | 1096 | 4 | 12/15 |
| http://39.106.165.196:8080 | CN | 1824 | 4 | 37/70 |
| http://113.45.195.147:3128 | CN | 2163 | 4 | 26/39 |
| http://115.231.181.40:8128 | CN | 5065 | 4 | 32/73 |
| http://41.128.90.53:1976 | EG | 1194 | 4 | 4/4 |
| http://103.155.198.138:3125 | ID | 6904 | 4 | 16/64 |
| http://153.80.240.2:1080 | NL | 1919 | 4 | 4/4 |
| http://5.129.254.5:8888 | RU | 1202 | 4 | 27/29 |
| http://5.129.254.49:8888 | RU | 1174 | 4 | 28/29 |
| http://5.129.254.51:8888 | RU | 1252 | 4 | 28/29 |
| http://5.129.254.60:8888 | RU | 1192 | 4 | 27/28 |
| http://5.129.254.70:8888 | RU | 1316 | 4 | 28/29 |
| http://5.129.254.129:8888 | RU | 1868 | 4 | 33/35 |
| http://5.129.254.154:8888 | RU | 1395 | 4 | 24/25 |
| http://43.128.76.140:8081 | SG | 1219 | 4 | 4/4 |
| http://193.104.179.115:3128 | UZ | 1299 | 4 | 22/39 |
| http://154.59.56.74:999 | VE | 4221 | 4 | 25/37 |
| socks5://65.21.252.66:10811 | FI | 1000 | 4 | 31/62 |
| socks5://57.128.231.218:1004 | PL | 4096 | 4 | 5/8 |
| socks5://45.32.160.61:1088 | US | 387 | 4 | 25/27 |
| http://83.143.24.66:80 | BW | 7563 | 3 | 6/20 |
| http://185.195.71.218:18080 | CH | 2134 | 3 | 5/11 |
| http://47.121.139.13:3128 | CN | 2011 | 3 | 34/73 |
| http://61.149.132.196:8888 | CN | 2314 | 3 | 7/19 |
| http://61.149.135.125:8888 | CN | 7917 | 3 | 15/34 |
| http://111.230.27.213:3128 | CN | 3352 | 3 | 29/74 |
| http://120.232.115.170:17981 | CN | 1940 | 3 | 52/73 |
| http://123.121.208.55:8888 | CN | 5253 | 3 | 9/27 |
| http://190.0.246.211:4040 | CO | 4069 | 3 | 62/74 |
| http://190.0.246.213:4040 | CO | 593 | 3 | 32/39 |
| http://18.157.123.132:3128 | DE | 665 | 3 | 24/35 |
| http://177.234.217.83:999 | EC | 4640 | 3 | 21/69 |
| http://181.188.203.112:999 | EC | 7978 | 3 | 20/66 |
| http://37.59.125.131:8888 | FR | 4699 | 3 | 58/74 |
| http://103.169.254.75:6080 | ID | 3634 | 3 | 9/62 |
| http://163.223.150.82:8080 | ID | 5500 | 3 | 10/62 |
| http://213.111.146.36:18080 | NL | 4556 | 3 | 6/11 |
| http://43.156.153.104:8080 | SG | 4113 | 3 | 3/3 |
| http://157.85.108.47:3128 | TH | 1205 | 3 | 31/42 |
| http://47.254.36.25:11080 | US | 6094 | 3 | 6/16 |
| http://190.89.29.110:999 | VE | 3085 | 3 | 12/52 |
| http://190.97.236.130:999 | VE | 782 | 3 | 3/3 |
| socks5://49.13.22.249:10811 | DE | 7433 | 3 | 24/46 |
| socks5://193.233.139.106:1080 | FI | 2650 | 3 | 17/32 |
| socks5://157.173.115.35:1081 | FR | 3197 | 3 | 3/3 |
| socks5://101.36.104.46:10808 | JP | 3780 | 3 | 65/74 |
| socks5://103.75.118.84:1080 | JP | 2087 | 3 | 51/69 |
| socks5://45.74.31.40:10509 | NL | 4892 | 3 | 3/3 |
| socks5://45.74.31.40:12735 | NL | 4020 | 3 | 3/3 |
| socks5://45.74.31.40:31246 | NL | 4608 | 3 | 3/3 |
| socks5://45.74.31.40:9971 | NL | 4779 | 3 | 3/3 |
| socks5://45.74.31.41:12122 | NL | 4937 | 3 | 3/3 |
| socks5://45.74.31.41:12670 | NL | 4802 | 3 | 3/3 |
| socks5://45.74.31.41:16321 | NL | 4137 | 3 | 3/3 |
| socks5://45.74.31.41:4444 | NL | 6744 | 3 | 3/3 |
| socks5://95.220.142.90:1080 | RU | 4268 | 3 | 3/3 |
| socks5://144.24.47.42:1080 | US | 704 | 3 | 38/70 |
| socks5://193.25.215.182:22222 | US | 1320 | 3 | 68/74 |
| http://27.147.153.179:8158 | BD | 5565 | 2 | 2/2 |
| http://190.181.22.106:8080 | BO | 4074 | 2 | 5/26 |
| http://144.217.82.40:8089 | CA | 4271 | 2 | 8/10 |
| http://147.182.156.27:8080 | CA | 184 | 2 | 2/2 |
