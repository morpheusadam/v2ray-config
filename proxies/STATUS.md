# Proxy status

Generated 2026-08-28T03:51:26Z by `harvest.py`.

- **721** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1437** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14041** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 173/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1131 |
| socks5 | 291 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 272 |
| US | 80 |
| CN | 63 |
| CO | 56 |
| BD | 52 |
| PH | 51 |
| DE | 44 |
| RU | 44 |
| MX | 42 |
| IN | 41 |
| FR | 38 |
| BR | 37 |
| NL | 37 |
| VN | 33 |
| VE | 32 |
| HK | 31 |
| TR | 29 |
| EC | 27 |
| JP | 26 |
| SG | 25 |
| TH | 23 |
| FI | 21 |
| ZA | 19 |
| KH | 18 |
| AU | 17 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 3 | 2026-08-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 20 | 20 | 7 | 2026-08-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 52 | 52 | 33 | 2026-08-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 83 | 83 | 18 | 2026-08-28 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 140 | 140 | 63 | 2026-08-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-08-28 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 157 | 157 | 51 | 2026-08-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 172 | 172 | 35 | 2026-08-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 174 | 174 | 15 | 2026-08-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 227 | 227 | 85 | 2026-08-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-28 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-08-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 456 | 2026-08-28 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1388 | 1384 | 473 | 2026-08-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1421 | 1419 | 204 | 2026-08-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1142 | 2026-08-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1610 | 2026-08-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1888 | 1886 | 696 | 2026-08-28 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2106 | 2106 | 1622 | 2026-08-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2273 | 2271 | 1744 | 2026-08-28 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 877 | 32 | 34/35 |
| http://34.43.46.91:443 | US | 388 | 27 | 32/35 |
| http://34.43.46.91:80 | US | 226 | 27 | 32/35 |
| http://103.237.102.191:11111 | DE | 795 | 21 | 34/35 |
| http://95.211.174.135:3128 | NL | 812 | 21 | 34/35 |
| http://204.76.203.9:3128 | NL | 949 | 21 | 34/35 |
| http://204.76.203.9:8080 | NL | 582 | 21 | 27/28 |
| http://185.200.188.234:10001 | RU | 1154 | 21 | 34/35 |
| http://130.110.103.245:3128 | SA | 1219 | 21 | 33/35 |
| http://95.3.69.222:8080 | TR | 1324 | 21 | 34/35 |
| http://199.7.149.90:3128 | US | 98 | 18 | 18/18 |
| http://199.7.149.96:3128 | US | 95 | 14 | 14/14 |
| http://45.186.6.104:3128 | EC | 654 | 13 | 13/13 |
| http://64.112.184.210:3128 | US | 292 | 13 | 34/35 |
| socks5://123.58.219.171:10808 | HK | 1910 | 13 | 29/35 |
| http://190.0.246.210:4040 | CO | 545 | 11 | 31/34 |
| http://47.81.56.193:8888 | TH | 1749 | 11 | 19/35 |
| http://103.130.61.61:8081 | ID | 4121 | 10 | 30/35 |
| http://42.96.18.62:1311 | VN | 1884 | 9 | 24/34 |
| socks5://144.91.121.61:1088 | FR | 1674 | 9 | 33/35 |
| socks5://101.36.104.239:10808 | JP | 1914 | 9 | 29/35 |
| socks5://67.207.92.87:1088 | US | 564 | 9 | 20/34 |
| socks5://193.25.215.182:22222 | US | 1385 | 9 | 32/35 |
| http://176.111.37.5:39811 | HK | 1001 | 8 | 30/35 |
| socks5://152.89.104.11:1080 | DE | 1169 | 8 | 13/35 |
| socks5://152.32.168.221:10808 | HK | 1515 | 8 | 18/24 |
| http://179.41.11.138:8080 | AR | 851 | 7 | 7/7 |
| http://185.191.239.248:3128 | CH | 820 | 7 | 24/34 |
| http://190.0.246.211:4040 | CO | 743 | 7 | 30/35 |
| http://103.211.103.170:3128 | HK | 542 | 7 | 7/7 |
| http://202.28.194.139:31280 | TH | 2027 | 7 | 33/35 |
| http://154.59.56.73:999 | VE | 1767 | 7 | 7/7 |
| http://14.251.13.20:8080 | VN | 1343 | 7 | 7/7 |
| socks4://45.61.129.165:9050 | US | 3816 | 7 | 27/35 |
| socks5://101.36.104.46:10808 | JP | 1368 | 7 | 32/35 |
| http://87.251.77.29:3128 | DE | 660 | 6 | 32/35 |
| http://103.218.122.183:8080 | VN | 1380 | 6 | 6/6 |
| socks5://45.194.33.12:30001 | HK | 1519 | 6 | 24/31 |
| socks5://45.194.33.12:30002 | HK | 1463 | 6 | 8/9 |
| http://103.177.118.145:8118 | BD | 1552 | 5 | 15/16 |
| http://114.236.137.41:21000 | CN | 3107 | 5 | 23/35 |
| http://81.19.210.10:80 | GB | 555 | 5 | 5/5 |
| http://175.143.76.177:8181 | MY | 5293 | 5 | 25/35 |
| http://43.98.172.166:3128 | SG | 1927 | 5 | 5/5 |
| http://43.156.236.238:80 | SG | 1121 | 5 | 16/33 |
| socks5://51.222.104.72:1080 | CA | 3329 | 5 | 16/35 |
| socks5://5.45.119.70:1080 | EE | 882 | 5 | 15/33 |
| http://219.142.66.245:9090 | CN | 2489 | 4 | 8/10 |
| http://186.33.45.218:999 | EC | 1702 | 4 | 15/24 |
| http://2.26.68.16:80 | FI | 4620 | 4 | 6/12 |
| http://37.59.125.131:8888 | FR | 1169 | 4 | 26/35 |
| http://176.111.37.216:39811 | HK | 976 | 4 | 30/35 |
| http://103.61.234.186:8180 | ID | 4601 | 4 | 17/32 |
| http://185.28.155.163:1433 | IL | 1558 | 4 | 4/4 |
| http://175.139.255.25:8181 | MY | 4264 | 4 | 27/35 |
| http://222.127.241.158:8082 | PH | 5541 | 4 | 9/29 |
| http://43.156.114.4:80 | SG | 1293 | 4 | 15/31 |
| http://43.163.112.8:80 | SG | 1092 | 4 | 16/32 |
| http://34.94.46.8:80 | US | 487 | 4 | 22/33 |
| socks5://45.144.54.40:1080 | DE | 1076 | 4 | 26/35 |
| socks5://185.185.80.58:1088 | FR | 1245 | 4 | 23/34 |
| socks5://144.24.111.128:1088 | IN | 1680 | 4 | 27/35 |
| socks5://103.75.118.84:1080 | JP | 2154 | 4 | 23/30 |
| socks5://192.163.200.82:17071 | US | 1133 | 4 | 8/26 |
| http://138.117.13.65:999 | AR | 3179 | 3 | 8/31 |
| http://15.135.215.62:7028 | AU | 2486 | 3 | 6/15 |
| http://16.26.143.154:59988 | AU | 5848 | 3 | 4/7 |
| http://54.206.129.120:41345 | AU | 2362 | 3 | 5/13 |
| http://54.253.167.61:48854 | AU | 3982 | 3 | 6/29 |
| http://87.237.15.238:7080 | BE | 550 | 3 | 3/3 |
| http://15.229.231.89:3080 | BR | 3319 | 3 | 5/27 |
| http://16.52.81.236:34947 | CA | 2252 | 3 | 6/27 |
| http://16.174.124.173:425 | CA | 1326 | 3 | 3/3 |
| http://35.183.127.162:40229 | CA | 860 | 3 | 5/15 |
| http://40.177.99.164:31822 | CA | 1907 | 3 | 8/35 |
| http://47.121.139.13:3128 | CN | 1941 | 3 | 13/34 |
| http://114.94.148.37:18080 | CN | 2332 | 3 | 19/34 |
| http://114.245.165.34:8888 | CN | 4303 | 3 | 3/3 |
| http://120.24.202.132:19000 | CN | 4234 | 3 | 11/29 |
| http://123.115.232.7:8888 | CN | 3065 | 3 | 3/3 |
| http://222.128.173.231:8888 | CN | 7475 | 3 | 3/3 |
| http://45.172.218.67:3028 | CO | 2681 | 3 | 11/25 |
| http://190.60.61.51:999 | CO | 2466 | 3 | 5/7 |
| http://3.127.27.51:29198 | DE | 2954 | 3 | 7/31 |
| http://86.53.111.249:8080 | DE | 643 | 3 | 7/18 |
| http://45.70.236.194:999 | EC | 3420 | 3 | 10/31 |
| http://177.234.217.83:999 | EC | 6135 | 3 | 9/30 |
| http://51.92.173.133:1090 | ES | 2203 | 3 | 4/13 |
| http://51.92.173.133:6014 | ES | 1210 | 3 | 8/29 |
| http://144.31.185.67:8080 | FI | 4280 | 3 | 3/3 |
| http://81.168.119.85:5443 | GB | 3502 | 3 | 10/23 |
| http://18.163.182.106:21128 | HK | 3283 | 3 | 3/3 |
| http://36.90.174.236:8080 | ID | 6711 | 3 | 3/3 |
| http://103.158.210.80:8082 | ID | 2560 | 3 | 5/25 |
| http://103.171.241.254:8080 | ID | 2485 | 3 | 11/30 |
| http://108.136.140.236:37871 | ID | 3221 | 3 | 4/5 |
| http://182.253.40.39:8080 | ID | 5149 | 3 | 4/12 |
| http://108.131.109.106:48856 | IE | 910 | 3 | 5/17 |
| http://51.84.101.19:32775 | IL | 1210 | 3 | 5/7 |
| http://13.126.183.60:48293 | IN | 5604 | 3 | 3/3 |
