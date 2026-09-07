# Proxy status

Generated 2026-09-07T18:14:27Z by `harvest.py`.

- **1605** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2196** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16065** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 155/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1818 |
| socks5 | 360 |
| socks4 | 18 |

| country | entries |
|---|---|
| ID | 548 |
| US | 129 |
| CN | 126 |
| CO | 99 |
| PH | 91 |
| RU | 80 |
| MX | 78 |
| BD | 75 |
| VE | 59 |
| SG | 55 |
| DE | 54 |
| NL | 52 |
| IN | 49 |
| BR | 48 |
| VN | 45 |
| EC | 44 |
| PK | 30 |
| FR | 29 |
| TR | 27 |
| CL | 26 |
| HK | 26 |
| DO | 24 |
| EG | 24 |
| KH | 24 |
| TH | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 33 | 33 | 17 | 2026-09-07 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 113 | 113 | 19 | 2026-09-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 63 | 2026-09-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 159 | 159 | 85 | 2026-09-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 167 | 167 | 67 | 2026-09-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 184 | 184 | 24 | 2026-09-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 203 | 203 | 20 | 2026-09-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-07 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 432 | 432 | 161 | 2026-09-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 548 | 548 | 186 | 2026-09-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-09-07 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1467 | 1463 | 220 | 2026-09-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-09-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1603 | 2026-09-07 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2167 | 2167 | 1510 | 2026-09-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2321 | 2319 | 161 | 2026-09-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2858 | 2856 | 743 | 2026-09-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2974 | 2972 | 2361 | 2026-09-07 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 539 | 48 | 53/56 |
| http://34.43.46.91:80 | US | 506 | 48 | 53/56 |
| http://95.211.174.135:3128 | NL | 1280 | 42 | 55/56 |
| http://185.200.188.234:10001 | RU | 2143 | 42 | 55/56 |
| http://130.110.103.245:3128 | SA | 1826 | 42 | 54/56 |
| http://199.7.149.96:3128 | US | 359 | 35 | 35/35 |
| http://64.112.184.210:3128 | US | 490 | 34 | 55/56 |
| http://103.211.103.170:3128 | HK | 4413 | 28 | 28/28 |
| http://68.178.174.239:3128 | US | 888 | 24 | 24/24 |
| http://68.178.174.239:8888 | US | 887 | 24 | 24/24 |
| http://1.231.81.166:3128 | KR | 1672 | 21 | 53/56 |
| http://189.51.168.164:999 | MX | 565 | 21 | 21/21 |
| socks5://193.25.215.182:22222 | US | 655 | 19 | 52/56 |
| http://116.202.172.187:11000 | DE | 2021 | 17 | 17/17 |
| http://91.134.141.4:3128 | FR | 778 | 17 | 17/17 |
| http://173.212.240.48:8888 | FR | 1117 | 17 | 17/17 |
| http://5.129.254.129:8888 | RU | 1477 | 17 | 17/17 |
| http://176.111.37.5:39811 | HK | 1488 | 16 | 50/56 |
| http://14.251.13.20:8080 | VN | 2144 | 16 | 27/28 |
| http://154.59.56.73:999 | VE | 4186 | 14 | 25/28 |
| http://120.232.115.170:17981 | CN | 1390 | 13 | 38/55 |
| http://181.78.23.187:999 | CO | 868 | 13 | 23/25 |
| http://181.78.74.252:999 | CO | 1002 | 13 | 45/47 |
| http://181.78.74.253:999 | CO | 933 | 13 | 45/47 |
| http://190.97.236.128:999 | VE | 798 | 13 | 44/46 |
| http://190.97.236.129:999 | VE | 790 | 13 | 44/46 |
| http://103.177.118.145:8118 | BD | 1464 | 12 | 35/37 |
| http://186.5.94.206:999 | EC | 1014 | 12 | 17/18 |
| socks5://147.45.60.124:1082 | US | 1913 | 12 | 32/56 |
| http://176.111.37.216:39811 | HK | 1210 | 11 | 44/56 |
| http://197.224.185.3:3128 | MU | 2031 | 11 | 22/24 |
| http://5.129.254.49:8888 | RU | 1920 | 11 | 11/11 |
| http://5.129.254.51:8888 | RU | 2314 | 11 | 11/11 |
| http://5.129.254.70:8888 | RU | 1332 | 11 | 11/11 |
| http://95.3.69.222:8080 | TR | 1820 | 11 | 53/56 |
| socks4://45.61.129.165:9050 | US | 5782 | 11 | 47/56 |
| socks5://43.135.176.121:1080 | US | 1039 | 11 | 11/11 |
| http://5.129.254.60:8888 | RU | 1349 | 10 | 10/10 |
| http://157.85.97.204:3128 | TH | 3178 | 10 | 18/21 |
| http://5.129.254.5:8888 | RU | 1338 | 9 | 10/11 |
| http://202.28.194.139:31280 | TH | 2624 | 9 | 53/56 |
| socks5://144.91.111.48:1088 | FR | 7675 | 9 | 28/56 |
| socks5://144.24.111.128:1088 | IN | 1863 | 9 | 44/56 |
| socks5://45.32.160.61:1088 | US | 497 | 9 | 9/9 |
| socks5://185.222.138.237:1080 | XK | 1193 | 9 | 9/9 |
| http://167.233.148.141:1083 | DE | 1734 | 8 | 8/8 |
| http://167.233.169.253:1083 | DE | 2038 | 8 | 8/8 |
| http://190.97.241.106:999 | VE | 2429 | 8 | 17/40 |
| socks5://103.210.161.8:1080 | CN | 4139 | 8 | 21/29 |
| http://185.191.239.248:3128 | CH | 1191 | 7 | 42/55 |
| http://117.236.124.166:3128 | IN | 2792 | 7 | 36/56 |
| http://175.139.255.25:8181 | MY | 4373 | 7 | 41/56 |
| http://5.129.254.154:8888 | RU | 1342 | 7 | 7/7 |
| http://38.7.195.55:999 | CL | 5855 | 6 | 13/30 |
| http://42.96.18.62:1311 | VN | 2718 | 6 | 42/55 |
| socks5://65.109.196.122:2091 | FI | 3901 | 6 | 9/10 |
| socks5://147.45.60.246:1082 | US | 2447 | 6 | 20/55 |
| http://123.119.178.176:8888 | CN | 1201 | 5 | 11/21 |
| http://123.121.129.198:8888 | CN | 2520 | 5 | 14/21 |
| http://221.221.163.120:8888 | CN | 1198 | 5 | 7/9 |
| http://167.233.169.253:1082 | DE | 1884 | 5 | 5/5 |
| http://167.233.169.253:1084 | DE | 1731 | 5 | 5/5 |
| http://196.61.42.26:3128 | GH | 2593 | 5 | 10/24 |
| http://168.144.84.188:3129 | IN | 1530 | 5 | 10/14 |
| http://77.235.24.145:3129 | KG | 7701 | 5 | 5/5 |
| http://157.85.108.47:3128 | TH | 1121 | 5 | 18/24 |
| http://161.35.181.96:999 | US | 505 | 5 | 5/5 |
| socks5://109.172.55.227:1082 | FR | 947 | 5 | 22/54 |
| socks5://117.244.114.54:1080 | IN | 5384 | 5 | 13/51 |
| socks5://108.174.152.80:1080 | MX | 1794 | 5 | 5/5 |
| socks5://107.181.252.58:1081 | US | 1105 | 5 | 5/5 |
| http://8.138.217.152:21001 | CN | 2920 | 4 | 37/56 |
| http://113.45.195.147:3128 | CN | 1455 | 4 | 12/21 |
| http://114.249.237.87:8888 | CN | 7529 | 4 | 11/20 |
| http://114.252.12.211:8888 | CN | 2116 | 4 | 10/21 |
| http://114.254.50.97:8888 | CN | 1226 | 4 | 15/21 |
| http://222.128.171.2:8888 | CN | 7586 | 4 | 6/8 |
| http://190.0.246.210:4040 | CO | 2193 | 4 | 49/55 |
| http://190.0.246.213:4040 | CO | 3566 | 4 | 19/21 |
| http://45.186.6.104:3128 | EC | 830 | 4 | 33/34 |
| http://197.164.101.14:1976 | EG | 1670 | 4 | 8/28 |
| http://144.31.185.62:8080 | FI | 7568 | 4 | 16/26 |
| http://43.99.60.244:8089 | HK | 909 | 4 | 5/6 |
| http://103.130.61.61:8081 | ID | 2703 | 4 | 45/56 |
| http://85.193.65.88:8888 | RU | 2082 | 4 | 24/46 |
| http://43.163.112.8:80 | SG | 890 | 4 | 29/53 |
| http://52.21.158.119:3128 | US | 379 | 4 | 8/9 |
| http://107.181.252.58:1082 | US | 1079 | 4 | 4/4 |
| http://154.3.76.14:999 | VE | 3948 | 4 | 7/9 |
| socks5://103.75.118.84:1080 | JP | 3288 | 4 | 38/51 |
| socks5://5.255.113.177:1080 | NL | 4039 | 4 | 14/55 |
| socks5://213.165.38.49:1080 | NL | 2576 | 4 | 6/23 |
| socks5://45.84.13.153:1080 | RU | 3288 | 4 | 6/37 |
| socks5://58.187.162.191:1083 | VN | 1552 | 4 | 4/4 |
| http://201.20.42.46:3127 | BR | 1834 | 3 | 14/54 |
| http://184.75.221.82:3118 | CA | 417 | 3 | 19/21 |
| http://38.7.195.50:999 | CL | 4364 | 3 | 6/15 |
| http://8.141.121.115:13126 | CN | 2476 | 3 | 6/30 |
| http://114.250.192.17:8888 | CN | 1188 | 3 | 9/21 |
| http://114.254.49.43:8888 | CN | 3284 | 3 | 3/3 |
