# Proxy status

Generated 2026-09-20T21:48:14Z by `harvest.py`.

- **1629** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2972** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **31713** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 159/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1562 |
| http | 1398 |
| socks4 | 12 |

| country | entries |
|---|---|
| NL | 1318 |
| ID | 363 |
| CN | 127 |
| US | 116 |
| RU | 80 |
| DE | 63 |
| SG | 61 |
| PH | 55 |
| MX | 54 |
| CO | 51 |
| VE | 45 |
| IN | 41 |
| BD | 40 |
| VN | 39 |
| BR | 33 |
| PK | 32 |
| EG | 31 |
| FR | 29 |
| DO | 28 |
| EC | 28 |
| TH | 23 |
| AR | 22 |
| FI | 21 |
| HK | 21 |
| CL | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-09-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 97 | 97 | 49 | 2026-09-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 124 | 124 | 53 | 2026-09-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 128 | 128 | 39 | 2026-09-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 148 | 148 | 44 | 2026-09-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 83 | 2026-09-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 248 | 248 | 70 | 2026-09-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 272 | 272 | 45 | 2026-09-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-09-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 586 | 586 | 260 | 2026-09-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-09-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-09-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1608 | 2026-09-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1817 | 1813 | 266 | 2026-09-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2403 | 2401 | 724 | 2026-09-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2587 | 2585 | 1862 | 2026-09-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3358 | 3356 | 923 | 2026-09-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 16401 | 16401 | 8754 | 2026-09-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 22656 | 22655 | 2399 | 2026-09-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1063 | 69 | 82/83 |
| http://185.200.188.234:10001 | RU | 1508 | 69 | 82/83 |
| http://130.110.103.245:3128 | SA | 1837 | 69 | 81/83 |
| http://1.231.81.166:3128 | KR | 1983 | 48 | 80/83 |
| http://190.97.236.128:999 | VE | 2780 | 40 | 71/73 |
| http://190.97.236.129:999 | VE | 1749 | 40 | 71/73 |
| http://95.3.69.222:8080 | TR | 1895 | 38 | 80/83 |
| socks5://107.167.18.122:443 | US | 380 | 28 | 34/35 |
| http://91.134.141.4:3128 | FR | 491 | 22 | 42/44 |
| http://186.5.94.206:999 | EC | 752 | 20 | 43/45 |
| http://107.150.41.226:18080 | US | 1341 | 20 | 20/20 |
| http://38.51.207.104:8080 | VE | 744 | 16 | 23/24 |
| http://189.51.168.164:999 | MX | 334 | 14 | 47/48 |
| http://45.132.252.25:49156 | RU | 813 | 14 | 14/14 |
| http://193.104.179.115:3128 | UZ | 1391 | 13 | 31/48 |
| http://190.0.246.213:4040 | CO | 484 | 12 | 41/48 |
| http://213.111.146.36:18080 | NL | 499 | 12 | 15/20 |
| http://45.186.6.104:3128 | EC | 584 | 10 | 59/61 |
| http://61.91.162.126:8080 | TH | 1531 | 10 | 23/26 |
| http://103.10.231.189:8080 | TH | 1929 | 10 | 48/68 |
| http://153.51.201.35:999 | VE | 678 | 10 | 10/10 |
| http://176.111.37.216:39811 | HK | 1365 | 9 | 69/83 |
| http://152.42.177.32:8888 | SG | 1176 | 9 | 25/43 |
| http://201.71.2.25:999 | VE | 564 | 9 | 24/70 |
| http://201.71.2.27:999 | VE | 709 | 9 | 30/81 |
| http://190.97.229.118:999 | VE | 2381 | 8 | 38/73 |
| http://190.97.241.106:999 | VE | 623 | 8 | 43/67 |
| socks5://193.233.223.47:1080 | RU | 1151 | 8 | 8/8 |
| http://103.237.102.191:11111 | DE | 1600 | 7 | 78/83 |
| http://37.59.125.131:8888 | FR | 2392 | 7 | 66/83 |
| http://176.111.37.5:39811 | HK | 911 | 7 | 76/83 |
| http://144.124.251.24:10000 | NL | 1506 | 7 | 15/29 |
| http://144.124.251.24:10007 | NL | 1439 | 7 | 14/32 |
| http://144.124.251.24:10008 | NL | 7046 | 7 | 10/14 |
| http://144.124.251.24:10104 | NL | 5756 | 7 | 10/15 |
| http://144.124.251.24:10176 | NL | 3451 | 7 | 14/31 |
| http://144.124.251.24:10185 | NL | 4170 | 7 | 11/15 |
| http://144.124.251.24:10216 | NL | 3300 | 7 | 15/32 |
| http://144.124.251.24:10226 | NL | 4144 | 7 | 9/14 |
| http://144.124.251.24:10333 | NL | 862 | 7 | 13/32 |
| http://144.124.251.24:10346 | NL | 5865 | 7 | 11/15 |
| http://144.124.251.24:10366 | NL | 2280 | 7 | 12/29 |
| http://144.124.251.24:10372 | NL | 955 | 7 | 14/27 |
| http://144.124.251.24:10431 | NL | 5789 | 7 | 16/31 |
| http://144.124.251.24:10453 | NL | 1544 | 7 | 13/20 |
| http://144.124.251.24:10551 | NL | 3012 | 7 | 15/31 |
| http://144.124.251.24:10574 | NL | 5044 | 7 | 15/32 |
| http://144.124.251.24:10628 | NL | 3612 | 7 | 10/15 |
| http://144.124.251.24:10771 | NL | 1934 | 7 | 10/15 |
| http://144.124.251.24:10829 | NL | 6484 | 7 | 10/15 |
| http://144.124.251.24:10953 | NL | 2507 | 7 | 11/15 |
| http://144.124.251.24:11011 | NL | 1493 | 7 | 11/15 |
| http://144.124.251.24:11108 | NL | 2528 | 7 | 12/30 |
| http://144.124.251.24:11180 | NL | 6230 | 7 | 10/14 |
| http://144.124.251.24:11265 | NL | 2389 | 7 | 14/31 |
| http://144.124.251.24:11266 | NL | 5949 | 7 | 11/15 |
| http://144.124.251.24:11274 | NL | 3372 | 7 | 14/31 |
| http://144.124.251.24:11480 | NL | 3086 | 7 | 9/15 |
| http://144.124.251.24:11491 | NL | 2379 | 7 | 14/31 |
| http://195.19.217.200:3128 | RU | 4793 | 7 | 8/9 |
| http://43.156.174.122:8080 | SG | 2254 | 7 | 7/7 |
| http://167.99.74.174:9090 | SG | 1144 | 7 | 26/43 |
| socks5://161.35.90.93:1082 | NL | 1724 | 7 | 45/83 |
| http://103.61.234.186:8180 | ID | 7727 | 6 | 36/80 |
| http://103.130.61.61:8081 | ID | 5071 | 6 | 66/83 |
| socks5://45.32.160.61:1088 | US | 201 | 6 | 33/36 |
| socks5://83.147.217.103:1080 | US | 149 | 6 | 6/6 |
| http://41.196.16.230:1981 | EG | 863 | 5 | 6/7 |
| http://62.193.104.26:1981 | EG | 2195 | 5 | 7/11 |
| http://154.236.168.162:1981 | EG | 4990 | 5 | 8/25 |
| http://103.88.234.239:40010 | MX | 521 | 5 | 7/8 |
| http://144.124.251.24:10187 | NL | 1377 | 5 | 11/29 |
| http://144.124.251.24:10230 | NL | 4889 | 5 | 14/30 |
| http://144.124.251.24:10801 | NL | 2702 | 5 | 11/31 |
| http://43.128.76.140:8080 | SG | 1137 | 5 | 12/16 |
| http://43.163.7.224:8080 | SG | 1325 | 5 | 5/5 |
| http://159.223.41.216:9090 | SG | 1176 | 5 | 27/43 |
| http://201.71.2.26:999 | VE | 559 | 5 | 34/76 |
| socks5://5.75.133.113:10802 | DE | 2448 | 5 | 6/8 |
| socks5://213.199.47.140:1080 | FR | 1126 | 5 | 41/49 |
| http://101.251.204.174:8080 | CN | 2024 | 4 | 35/69 |
| http://114.252.12.211:8888 | CN | 2076 | 4 | 21/48 |
| http://181.78.176.147:999 | CO | 3576 | 4 | 4/4 |
| http://31.31.74.185:9898 | CZ | 582 | 4 | 4/4 |
| http://64.188.71.169:3128 | DE | 561 | 4 | 4/4 |
| http://41.128.77.76:1976 | EG | 1921 | 4 | 18/49 |
| http://41.128.77.76:1981 | EG | 921 | 4 | 15/37 |
| http://197.164.101.14:1976 | EG | 3306 | 4 | 19/55 |
| http://37.187.109.70:10111 | FR | 1866 | 4 | 35/83 |
| http://168.144.117.43:3129 | IN | 1355 | 4 | 19/33 |
| http://85.133.250.27:80 | IR | 1023 | 4 | 7/8 |
| http://187.190.58.152:80 | MX | 3577 | 4 | 31/81 |
| http://43.134.16.72:8080 | SG | 2228 | 4 | 4/4 |
| http://43.134.79.76:8081 | SG | 2126 | 4 | 4/4 |
| http://43.156.199.63:8080 | SG | 1125 | 4 | 15/18 |
| http://43.159.35.15:8080 | SG | 1133 | 4 | 4/4 |
| http://146.190.80.158:9090 | SG | 1190 | 4 | 7/9 |
| http://167.172.84.23:3128 | SG | 2574 | 4 | 4/4 |
| http://210.211.113.34:80 | VN | 2989 | 4 | 43/55 |
| socks4://57.128.231.218:1001 | PL | 858 | 4 | 11/21 |
