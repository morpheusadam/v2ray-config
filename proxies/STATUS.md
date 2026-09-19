# Proxy status

Generated 2026-09-19T21:44:09Z by `harvest.py`.

- **1640** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2833** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **30171** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 186/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1562 |
| socks5 | 1267 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 1060 |
| ID | 433 |
| US | 123 |
| CN | 115 |
| PH | 72 |
| RU | 72 |
| SG | 64 |
| MX | 62 |
| DE | 60 |
| VE | 50 |
| CO | 48 |
| BD | 44 |
| IN | 40 |
| VN | 37 |
| TH | 35 |
| BR | 31 |
| EC | 29 |
| EG | 29 |
| PK | 29 |
| FR | 28 |
| AR | 26 |
| HK | 25 |
| TR | 25 |
| DO | 24 |
| CL | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-09-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 62 | 62 | 25 | 2026-09-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 71 | 71 | 31 | 2026-09-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-09-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-09-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 217 | 217 | 75 | 2026-09-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 284 | 284 | 124 | 2026-09-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 336 | 336 | 125 | 2026-09-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 520 | 520 | 286 | 2026-09-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-09-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 631 | 631 | 40 | 2026-09-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-09-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1611 | 2026-09-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1822 | 1818 | 233 | 2026-09-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2446 | 2444 | 682 | 2026-09-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2571 | 2569 | 1896 | 2026-09-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3047 | 3045 | 965 | 2026-09-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 14762 | 14762 | 8368 | 2026-09-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 21347 | 21346 | 2608 | 2026-09-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 330 | 73 | 78/81 |
| http://34.43.46.91:80 | US | 288 | 73 | 78/81 |
| http://95.211.174.135:3128 | NL | 864 | 67 | 80/81 |
| http://185.200.188.234:10001 | RU | 1182 | 67 | 80/81 |
| http://130.110.103.245:3128 | SA | 1418 | 67 | 79/81 |
| http://1.231.81.166:3128 | KR | 1202 | 46 | 78/81 |
| http://190.97.236.128:999 | VE | 1792 | 38 | 69/71 |
| http://190.97.236.129:999 | VE | 856 | 38 | 69/71 |
| http://95.3.69.222:8080 | TR | 1335 | 36 | 78/81 |
| socks5://107.167.18.122:443 | US | 363 | 26 | 32/33 |
| socks5://83.147.216.208:1080 | FI | 2122 | 25 | 31/49 |
| http://184.75.221.82:3118 | CA | 181 | 22 | 43/46 |
| http://91.134.141.4:3128 | FR | 586 | 20 | 40/42 |
| http://186.5.94.206:999 | EC | 959 | 18 | 41/43 |
| http://107.150.41.226:18080 | US | 419 | 18 | 18/18 |
| http://38.51.207.104:8080 | VE | 1552 | 14 | 21/22 |
| http://197.224.185.3:3128 | MU | 1849 | 12 | 45/49 |
| http://189.51.168.164:999 | MX | 424 | 12 | 45/46 |
| http://45.132.252.25:49156 | RU | 836 | 12 | 12/12 |
| http://193.104.179.115:3128 | UZ | 1194 | 11 | 29/46 |
| http://120.232.115.170:17981 | CN | 2059 | 10 | 59/80 |
| http://190.0.246.213:4040 | CO | 949 | 10 | 39/46 |
| http://213.111.146.36:18080 | NL | 1313 | 10 | 13/18 |
| http://157.85.108.47:3128 | TH | 1234 | 10 | 38/49 |
| http://45.186.6.104:3128 | EC | 616 | 8 | 57/59 |
| http://61.91.162.126:8080 | TH | 1474 | 8 | 21/24 |
| http://103.10.231.189:8080 | TH | 1474 | 8 | 46/66 |
| http://153.51.201.35:999 | VE | 844 | 8 | 8/8 |
| http://154.3.76.14:999 | VE | 6415 | 8 | 25/34 |
| http://210.211.113.33:80 | VN | 3984 | 8 | 30/51 |
| http://8.138.217.152:21001 | CN | 6956 | 7 | 56/81 |
| http://123.121.123.216:8888 | CN | 1762 | 7 | 16/41 |
| http://176.111.37.216:39811 | HK | 1236 | 7 | 67/81 |
| http://152.42.177.32:8888 | SG | 1083 | 7 | 23/41 |
| http://201.71.2.25:999 | VE | 5336 | 7 | 22/68 |
| http://201.71.2.27:999 | VE | 6060 | 7 | 28/79 |
| socks5://36.155.23.163:10808 | CN | 1222 | 7 | 12/18 |
| http://177.234.217.237:999 | EC | 3564 | 6 | 23/54 |
| http://203.177.217.222:8082 | PH | 2596 | 6 | 15/26 |
| http://190.97.229.118:999 | VE | 2992 | 6 | 36/71 |
| http://190.97.241.106:999 | VE | 1620 | 6 | 41/65 |
| socks5://45.74.31.41:15538 | NL | 6060 | 6 | 6/6 |
| socks5://193.233.223.47:1080 | RU | 1261 | 6 | 6/6 |
| http://38.7.195.51:999 | CL | 4269 | 5 | 24/72 |
| http://2.27.63.250:8118 | DE | 874 | 5 | 16/31 |
| http://103.237.102.191:11111 | DE | 726 | 5 | 76/81 |
| http://177.234.217.235:999 | EC | 5205 | 5 | 29/50 |
| http://37.59.125.131:8888 | FR | 2207 | 5 | 64/81 |
| http://176.111.37.5:39811 | HK | 898 | 5 | 74/81 |
| http://205.164.192.115:999 | MX | 4027 | 5 | 50/79 |
| http://144.124.251.24:10000 | NL | 1745 | 5 | 13/27 |
| http://144.124.251.24:10007 | NL | 816 | 5 | 12/30 |
| http://144.124.251.24:10008 | NL | 1607 | 5 | 8/12 |
| http://144.124.251.24:10084 | NL | 1081 | 5 | 9/13 |
| http://144.124.251.24:10104 | NL | 1452 | 5 | 8/13 |
| http://144.124.251.24:10176 | NL | 642 | 5 | 12/29 |
| http://144.124.251.24:10185 | NL | 1862 | 5 | 9/13 |
| http://144.124.251.24:10216 | NL | 2017 | 5 | 13/30 |
| http://144.124.251.24:10226 | NL | 2122 | 5 | 7/12 |
| http://144.124.251.24:10299 | NL | 1734 | 5 | 9/13 |
| http://144.124.251.24:10333 | NL | 4507 | 5 | 11/30 |
| http://144.124.251.24:10337 | NL | 1796 | 5 | 9/13 |
| http://144.124.251.24:10346 | NL | 1996 | 5 | 9/13 |
| http://144.124.251.24:10366 | NL | 752 | 5 | 10/27 |
| http://144.124.251.24:10372 | NL | 3422 | 5 | 12/25 |
| http://144.124.251.24:10412 | NL | 6664 | 5 | 9/13 |
| http://144.124.251.24:10431 | NL | 713 | 5 | 14/29 |
| http://144.124.251.24:10453 | NL | 4203 | 5 | 11/18 |
| http://144.124.251.24:10471 | NL | 1760 | 5 | 13/28 |
| http://144.124.251.24:10485 | NL | 2343 | 5 | 8/13 |
| http://144.124.251.24:10551 | NL | 658 | 5 | 13/29 |
| http://144.124.251.24:10566 | NL | 843 | 5 | 10/14 |
| http://144.124.251.24:10574 | NL | 783 | 5 | 13/30 |
| http://144.124.251.24:10601 | NL | 1315 | 5 | 10/28 |
| http://144.124.251.24:10605 | NL | 798 | 5 | 9/13 |
| http://144.124.251.24:10610 | NL | 1044 | 5 | 9/13 |
| http://144.124.251.24:10628 | NL | 963 | 5 | 8/13 |
| http://144.124.251.24:10631 | NL | 3559 | 5 | 9/13 |
| http://144.124.251.24:10658 | NL | 1883 | 5 | 9/13 |
| http://144.124.251.24:10689 | NL | 1947 | 5 | 10/17 |
| http://144.124.251.24:10771 | NL | 1421 | 5 | 8/13 |
| http://144.124.251.24:10800 | NL | 1153 | 5 | 9/13 |
| http://144.124.251.24:10811 | NL | 1865 | 5 | 9/13 |
| http://144.124.251.24:10829 | NL | 2256 | 5 | 8/13 |
| http://144.124.251.24:10953 | NL | 1637 | 5 | 9/13 |
| http://144.124.251.24:11011 | NL | 2162 | 5 | 9/13 |
| http://144.124.251.24:11108 | NL | 2138 | 5 | 10/28 |
| http://144.124.251.24:11124 | NL | 738 | 5 | 12/30 |
| http://144.124.251.24:11180 | NL | 3438 | 5 | 8/12 |
| http://144.124.251.24:11265 | NL | 678 | 5 | 12/29 |
| http://144.124.251.24:11266 | NL | 1730 | 5 | 9/13 |
| http://144.124.251.24:11274 | NL | 680 | 5 | 12/29 |
| http://144.124.251.24:11480 | NL | 1908 | 5 | 7/13 |
| http://144.124.251.24:11491 | NL | 720 | 5 | 12/29 |
| http://195.19.217.200:3128 | RU | 3560 | 5 | 6/7 |
| http://43.128.76.140:8081 | SG | 2501 | 5 | 10/11 |
| http://43.156.174.122:8080 | SG | 4313 | 5 | 5/5 |
| http://47.84.84.1:3128 | SG | 3827 | 5 | 32/81 |
| http://167.99.74.174:9090 | SG | 1094 | 5 | 24/41 |
| http://154.59.56.72:999 | VE | 3227 | 5 | 25/40 |
