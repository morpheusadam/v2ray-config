# Proxy status

Generated 2026-08-31T19:44:55Z by `harvest.py`.

- **984** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1948** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15657** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 142/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1685 |
| socks5 | 246 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 434 |
| US | 160 |
| CN | 118 |
| CO | 77 |
| MX | 72 |
| PH | 71 |
| BR | 59 |
| BD | 55 |
| DE | 51 |
| RU | 45 |
| VE | 44 |
| NL | 43 |
| IN | 42 |
| VN | 41 |
| FR | 40 |
| EC | 36 |
| SG | 31 |
| TH | 30 |
| HK | 28 |
| KH | 24 |
| KR | 23 |
| JP | 22 |
| TR | 21 |
| CA | 19 |
| MY | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-08-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 91 | 91 | 54 | 2026-08-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 93 | 93 | 31 | 2026-08-31 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 140 | 140 | 66 | 2026-08-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 144 | 144 | 45 | 2026-08-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 70 | 2026-08-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 184 | 184 | 49 | 2026-08-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 198 | 198 | 35 | 2026-08-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 293 | 293 | 111 | 2026-08-31 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-08-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-08-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 783 | 783 | 419 | 2026-08-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-08-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1603 | 2026-08-31 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1861 | 1857 | 468 | 2026-08-31 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2120 | 2120 | 1549 | 2026-08-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2158 | 2158 | 327 | 2026-08-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2491 | 2491 | 668 | 2026-08-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2814 | 2812 | 2181 | 2026-08-31 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1114 | 39 | 41/42 |
| http://34.43.46.91:443 | US | 681 | 34 | 39/42 |
| http://34.43.46.91:80 | US | 1453 | 34 | 39/42 |
| http://95.211.174.135:3128 | NL | 1788 | 28 | 41/42 |
| http://204.76.203.9:3128 | NL | 1009 | 28 | 41/42 |
| http://204.76.203.9:8080 | NL | 741 | 28 | 34/35 |
| http://185.200.188.234:10001 | RU | 6361 | 28 | 41/42 |
| http://130.110.103.245:3128 | SA | 1941 | 28 | 40/42 |
| http://95.3.69.222:8080 | TR | 2073 | 28 | 41/42 |
| http://199.7.149.96:3128 | US | 357 | 21 | 21/21 |
| http://45.186.6.104:3128 | EC | 699 | 20 | 20/20 |
| http://64.112.184.210:3128 | US | 483 | 20 | 41/42 |
| http://42.96.18.62:1311 | VN | 1880 | 16 | 31/41 |
| http://103.211.103.170:3128 | HK | 1484 | 14 | 14/14 |
| http://202.28.194.139:31280 | TH | 2719 | 14 | 40/42 |
| socks4://45.61.129.165:9050 | US | 2964 | 14 | 34/42 |
| http://87.251.77.29:3128 | DE | 900 | 13 | 39/42 |
| socks5://45.194.33.12:30001 | HK | 1133 | 13 | 31/38 |
| socks5://45.194.33.12:30002 | HK | 1127 | 13 | 15/16 |
| http://103.177.118.145:8118 | BD | 2563 | 12 | 22/23 |
| http://197.224.185.3:3128 | MU | 1986 | 10 | 10/10 |
| http://157.85.111.64:3128 | TH | 4197 | 10 | 10/10 |
| http://68.178.174.239:3128 | US | 964 | 10 | 10/10 |
| http://68.178.174.239:8888 | US | 958 | 10 | 10/10 |
| http://8.138.217.152:21001 | CN | 2306 | 9 | 29/42 |
| http://181.78.23.187:999 | CO | 864 | 9 | 10/11 |
| http://181.78.74.252:999 | CO | 814 | 9 | 32/33 |
| http://181.78.74.253:999 | CO | 824 | 9 | 32/33 |
| http://190.97.236.128:999 | VE | 703 | 9 | 31/32 |
| http://190.97.236.129:999 | VE | 725 | 9 | 31/32 |
| http://184.75.221.82:3118 | CA | 386 | 7 | 7/7 |
| http://123.121.121.123:8888 | CN | 3320 | 7 | 7/7 |
| http://190.0.246.213:4040 | CO | 1389 | 7 | 7/7 |
| http://130.61.112.125:443 | DE | 737 | 7 | 7/7 |
| http://194.163.175.167:40000 | FR | 1412 | 7 | 7/7 |
| http://1.231.81.166:3128 | KR | 1069 | 7 | 39/42 |
| http://189.51.168.164:999 | MX | 516 | 7 | 7/7 |
| http://43.160.242.118:3128 | SG | 1881 | 7 | 32/39 |
| http://157.85.97.204:3128 | TH | 1100 | 7 | 7/7 |
| socks4://158.220.99.85:4545 | FR | 1378 | 7 | 7/7 |
| socks5://47.250.211.53:1080 | MY | 4295 | 7 | 23/42 |
| http://111.192.21.92:8888 | CN | 2106 | 6 | 6/6 |
| socks5://85.209.156.148:1080 | US | 1802 | 6 | 10/13 |
| http://193.233.232.49:3131 | AT | 3794 | 5 | 5/5 |
| http://221.221.165.188:8888 | CN | 1257 | 5 | 6/7 |
| http://85.193.65.88:8888 | RU | 1457 | 5 | 13/32 |
| socks5://193.25.215.182:22222 | US | 603 | 5 | 38/42 |
| http://179.41.11.138:8080 | AR | 982 | 4 | 13/14 |
| http://185.191.239.248:3128 | CH | 3239 | 4 | 30/41 |
| http://101.251.204.174:8080 | CN | 1459 | 4 | 14/28 |
| http://114.249.218.6:8888 | CN | 1966 | 4 | 5/7 |
| http://177.234.217.235:999 | EC | 5883 | 4 | 6/11 |
| http://186.5.94.206:999 | EC | 4195 | 4 | 4/4 |
| http://47.57.69.227:3128 | HK | 2983 | 4 | 12/14 |
| http://38.188.63.147:8080 | ID | 2870 | 4 | 5/7 |
| http://175.143.76.177:8181 | MY | 3792 | 4 | 31/42 |
| http://3.211.120.181:443 | US | 336 | 4 | 4/4 |
| socks5://123.58.219.171:10808 | HK | 2982 | 4 | 35/42 |
| socks5://94.183.233.251:1080 | US | 4307 | 4 | 6/7 |
| http://200.115.100.33:8080 | BR | 7042 | 3 | 5/14 |
| http://170.245.50.65:8080 | CL | 6201 | 3 | 5/30 |
| http://111.192.31.242:8888 | CN | 1314 | 3 | 5/7 |
| http://114.236.137.41:21000 | CN | 3060 | 3 | 29/42 |
| http://120.26.171.55:25125 | CN | 1772 | 3 | 14/40 |
| http://123.121.122.126:8888 | CN | 1266 | 3 | 6/10 |
| http://123.121.132.32:8888 | CN | 1406 | 3 | 3/3 |
| http://45.172.218.67:3028 | CO | 4622 | 3 | 16/32 |
| http://18.157.123.132:3128 | DE | 760 | 3 | 3/3 |
| http://116.202.172.187:11000 | DE | 823 | 3 | 3/3 |
| http://38.44.17.142:999 | DO | 5041 | 3 | 18/35 |
| http://51.146.240.4:3128 | FR | 2297 | 3 | 6/8 |
| http://51.146.240.4:43 | FR | 1224 | 3 | 5/7 |
| http://91.134.141.4:3128 | FR | 761 | 3 | 3/3 |
| http://173.212.240.48:8888 | FR | 1016 | 3 | 3/3 |
| http://181.215.18.40:3128 | HK | 6574 | 3 | 9/33 |
| http://103.68.212.84:80 | ID | 1437 | 3 | 3/3 |
| http://103.122.64.163:8080 | ID | 3767 | 3 | 10/35 |
| http://103.152.21.59:3128 | ID | 3652 | 3 | 3/3 |
| http://144.79.241.253:3128 | ID | 3065 | 3 | 5/28 |
| http://210.87.92.82:8080 | ID | 1314 | 3 | 8/28 |
| http://151.185.59.40:8080 | IN | 1615 | 3 | 5/14 |
| http://43.164.136.235:3128 | KR | 2251 | 3 | 3/3 |
| http://38.123.220.105:999 | MX | 4151 | 3 | 9/38 |
| http://116.90.224.50:8080 | NP | 7471 | 3 | 10/39 |
| http://5.129.254.129:8888 | RU | 1263 | 3 | 3/3 |
| http://109.94.1.23:4050 | RU | 2262 | 3 | 30/42 |
| http://101.32.167.12:3000 | SG | 1675 | 3 | 3/3 |
| http://131.222.210.21:8080 | SY | 1489 | 3 | 8/37 |
| http://103.10.231.189:8080 | TH | 1282 | 3 | 16/27 |
| http://157.85.105.217:3128 | TH | 3139 | 3 | 9/10 |
| http://54.158.219.104:8443 | US | 4237 | 3 | 4/6 |
| http://38.252.186.112:999 | VE | 7460 | 3 | 5/8 |
| http://190.97.238.14:999 | VE | 2202 | 3 | 7/11 |
| http://190.97.238.160:999 | VE | 5031 | 3 | 8/15 |
| http://210.211.113.36:80 | VN | 2583 | 3 | 8/13 |
| socks5://119.148.7.10:22122 | BD | 5953 | 3 | 16/36 |
| socks5://45.144.54.40:1080 | DE | 4992 | 3 | 32/42 |
| socks5://51.178.49.241:1088 | FR | 1236 | 3 | 3/3 |
| socks5://103.191.218.119:69 | ID | 3591 | 3 | 10/28 |
| socks5://144.24.111.128:1088 | IN | 2668 | 3 | 32/42 |
