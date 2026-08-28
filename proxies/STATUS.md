# Proxy status

Generated 2026-08-28T23:02:56Z by `harvest.py`.

- **884** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1639** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14024** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 164/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1327 |
| socks5 | 296 |
| socks4 | 16 |

| country | entries |
|---|---|
| ID | 310 |
| CN | 120 |
| US | 85 |
| CO | 69 |
| MX | 54 |
| BD | 53 |
| DE | 53 |
| PH | 51 |
| IN | 47 |
| RU | 47 |
| FR | 45 |
| BR | 41 |
| EC | 35 |
| TH | 35 |
| NL | 34 |
| TR | 34 |
| VE | 34 |
| VN | 29 |
| HK | 28 |
| JP | 27 |
| SG | 25 |
| DO | 22 |
| AU | 21 |
| ZA | 20 |
| FI | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 2 | 2 | 1 | 2026-08-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 70 | 70 | 38 | 2026-08-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 72 | 72 | 32 | 2026-08-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 93 | 93 | 29 | 2026-08-28 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-08-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 112 | 112 | 28 | 2026-08-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-08-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 162 | 162 | 53 | 2026-08-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 184 | 184 | 47 | 2026-08-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 196 | 196 | 33 | 2026-08-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-28 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 492 | 492 | 248 | 2026-08-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-08-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-08-28 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1288 | 1284 | 465 | 2026-08-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1444 | 1442 | 169 | 2026-08-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1148 | 2026-08-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1607 | 2026-08-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1890 | 1888 | 626 | 2026-08-28 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2119 | 2119 | 1659 | 2026-08-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2251 | 2249 | 1720 | 2026-08-28 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 954 | 33 | 35/36 |
| http://34.43.46.91:443 | US | 424 | 28 | 33/36 |
| http://34.43.46.91:80 | US | 385 | 28 | 33/36 |
| http://103.237.102.191:11111 | DE | 883 | 22 | 35/36 |
| http://95.211.174.135:3128 | NL | 1235 | 22 | 35/36 |
| http://204.76.203.9:3128 | NL | 944 | 22 | 35/36 |
| http://204.76.203.9:8080 | NL | 730 | 22 | 28/29 |
| http://185.200.188.234:10001 | RU | 1130 | 22 | 35/36 |
| http://130.110.103.245:3128 | SA | 1433 | 22 | 34/36 |
| http://95.3.69.222:8080 | TR | 1452 | 22 | 35/36 |
| http://199.7.149.90:3128 | US | 343 | 19 | 19/19 |
| http://199.7.149.96:3128 | US | 343 | 15 | 15/15 |
| http://45.186.6.104:3128 | EC | 701 | 14 | 14/14 |
| http://64.112.184.210:3128 | US | 379 | 14 | 35/36 |
| socks5://123.58.219.171:10808 | HK | 1835 | 14 | 30/36 |
| http://190.0.246.210:4040 | CO | 625 | 12 | 32/35 |
| http://47.81.56.193:8888 | TH | 1657 | 12 | 20/36 |
| http://103.130.61.61:8081 | ID | 2815 | 11 | 31/36 |
| http://42.96.18.62:1311 | VN | 1693 | 10 | 25/35 |
| socks5://144.91.121.61:1088 | FR | 1708 | 10 | 34/36 |
| socks5://67.207.92.87:1088 | US | 772 | 10 | 21/35 |
| socks5://193.25.215.182:22222 | US | 443 | 10 | 33/36 |
| http://176.111.37.5:39811 | HK | 1016 | 9 | 31/36 |
| socks5://152.32.168.221:10808 | HK | 1503 | 9 | 19/25 |
| http://179.41.11.138:8080 | AR | 859 | 8 | 8/8 |
| http://185.191.239.248:3128 | CH | 887 | 8 | 25/35 |
| http://190.0.246.211:4040 | CO | 832 | 8 | 31/36 |
| http://103.211.103.170:3128 | HK | 739 | 8 | 8/8 |
| http://202.28.194.139:31280 | TH | 2755 | 8 | 34/36 |
| http://154.59.56.73:999 | VE | 2432 | 8 | 8/8 |
| http://14.251.13.20:8080 | VN | 1197 | 8 | 8/8 |
| socks5://101.36.104.46:10808 | JP | 1468 | 8 | 33/36 |
| socks5://45.61.129.165:9050 | US | 2242 | 8 | 28/36 |
| http://87.251.77.29:3128 | DE | 1058 | 7 | 33/36 |
| http://103.218.122.183:8080 | VN | 1183 | 7 | 7/7 |
| socks5://45.194.33.12:30001 | HK | 1310 | 7 | 25/32 |
| socks5://45.194.33.12:30002 | HK | 1219 | 7 | 9/10 |
| http://103.177.118.145:8118 | BD | 1491 | 6 | 16/17 |
| http://114.236.137.41:21000 | CN | 1709 | 6 | 24/36 |
| http://81.19.210.10:80 | GB | 911 | 6 | 6/6 |
| http://175.143.76.177:8181 | MY | 3153 | 6 | 26/36 |
| http://43.98.172.166:3128 | SG | 2582 | 6 | 6/6 |
| socks5://5.45.119.70:1080 | EE | 1182 | 6 | 16/34 |
| http://186.33.45.218:999 | EC | 6244 | 5 | 16/25 |
| http://176.111.37.216:39811 | HK | 915 | 5 | 31/36 |
| http://185.28.155.163:1433 | IL | 1143 | 5 | 5/5 |
| http://175.139.255.25:8181 | MY | 3861 | 5 | 28/36 |
| http://43.156.114.4:80 | SG | 1153 | 5 | 16/32 |
| socks5://45.144.54.40:1080 | DE | 1039 | 5 | 27/36 |
| socks5://144.24.111.128:1088 | IN | 1771 | 5 | 28/36 |
| socks5://103.75.118.84:1080 | JP | 2336 | 5 | 24/31 |
| socks5://192.163.200.82:17071 | US | 2450 | 5 | 9/27 |
| http://138.117.13.65:999 | AR | 3469 | 4 | 9/32 |
| http://15.135.215.62:7028 | AU | 4193 | 4 | 7/16 |
| http://54.206.129.120:41345 | AU | 4226 | 4 | 6/14 |
| http://87.237.15.238:7080 | BE | 733 | 4 | 4/4 |
| http://16.52.81.236:34947 | CA | 1198 | 4 | 7/28 |
| http://16.174.124.173:425 | CA | 2325 | 4 | 4/4 |
| http://35.183.127.162:40229 | CA | 1200 | 4 | 6/16 |
| http://40.177.99.164:31822 | CA | 2809 | 4 | 9/36 |
| http://47.121.139.13:3128 | CN | 2929 | 4 | 14/35 |
| http://114.94.148.37:18080 | CN | 968 | 4 | 20/35 |
| http://114.245.165.34:8888 | CN | 3597 | 4 | 4/4 |
| http://222.128.173.231:8888 | CN | 3926 | 4 | 4/4 |
| http://190.60.61.51:999 | CO | 4271 | 4 | 6/8 |
| http://86.53.111.249:8080 | DE | 1861 | 4 | 8/19 |
| http://51.92.173.133:1090 | ES | 4967 | 4 | 5/14 |
| http://81.168.119.85:5443 | GB | 859 | 4 | 11/24 |
| http://103.158.210.80:8082 | ID | 4417 | 4 | 6/26 |
| http://182.253.40.39:8080 | ID | 4353 | 4 | 5/13 |
| http://13.126.183.60:48293 | IN | 3577 | 4 | 4/4 |
| http://43.200.174.95:6906 | KR | 4979 | 4 | 4/4 |
| http://197.224.185.3:3128 | MU | 2051 | 4 | 4/4 |
| http://103.88.234.239:40013 | MX | 570 | 4 | 6/7 |
| http://175.136.239.173:8181 | MY | 3163 | 4 | 28/36 |
| http://91.233.223.147:3128 | RU | 1175 | 4 | 5/10 |
| http://13.51.196.44:25499 | SE | 2320 | 4 | 8/30 |
| http://13.212.26.15:5910 | SG | 2754 | 4 | 9/30 |
| http://157.85.97.240:3128 | TH | 1116 | 4 | 4/4 |
| http://157.85.105.217:3128 | TH | 2158 | 4 | 4/4 |
| http://157.85.108.47:3128 | TH | 1315 | 4 | 4/4 |
| http://157.85.108.62:3128 | TH | 1294 | 4 | 4/4 |
| http://157.85.108.68:3128 | TH | 1119 | 4 | 4/4 |
| http://157.85.111.64:3128 | TH | 1121 | 4 | 4/4 |
| http://18.222.132.180:54474 | US | 1590 | 4 | 8/30 |
| http://34.207.102.197:20297 | US | 957 | 4 | 5/14 |
| http://68.178.174.239:3128 | US | 957 | 4 | 4/4 |
| http://68.178.174.239:8888 | US | 967 | 4 | 4/4 |
| http://209.174.97.162:5999 | US | 404 | 4 | 4/4 |
| socks5://31.25.236.95:1080 | DE | 4987 | 4 | 8/20 |
| socks5://77.239.106.24:1080 | DE | 2917 | 4 | 16/21 |
| socks5://195.135.255.98:1080 | LV | 2195 | 4 | 13/36 |
| http://16.26.154.68:53546 | AU | 3307 | 3 | 10/32 |
| http://143.0.203.173:8080 | BR | 7574 | 3 | 7/26 |
| http://181.191.14.5:8080 | BR | 3863 | 3 | 7/26 |
| http://8.138.217.152:21001 | CN | 4310 | 3 | 23/36 |
| http://111.230.27.213:3128 | CN | 3601 | 3 | 14/36 |
| http://115.231.181.40:8128 | CN | 2524 | 3 | 19/35 |
| http://38.10.240.130:3128 | CO | 7009 | 3 | 8/34 |
| http://181.78.23.187:999 | CO | 777 | 3 | 4/5 |
