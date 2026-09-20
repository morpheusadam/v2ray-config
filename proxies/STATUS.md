# Proxy status

Generated 2026-09-20T16:55:57Z by `harvest.py`.

- **2076** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3309** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **31684** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 169/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1740 |
| http | 1560 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1524 |
| ID | 450 |
| CN | 111 |
| US | 105 |
| PH | 76 |
| RU | 70 |
| SG | 63 |
| DE | 61 |
| MX | 59 |
| CO | 58 |
| VE | 52 |
| BD | 43 |
| IN | 38 |
| TR | 37 |
| BR | 36 |
| VN | 36 |
| TH | 33 |
| EC | 32 |
| PK | 32 |
| EG | 30 |
| DO | 27 |
| FR | 24 |
| AR | 22 |
| CL | 22 |
| HK | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-09-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 55 | 55 | 15 | 2026-09-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 92 | 92 | 39 | 2026-09-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 95 | 95 | 51 | 2026-09-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 86 | 2026-09-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 167 | 167 | 54 | 2026-09-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 281 | 281 | 80 | 2026-09-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 493 | 493 | 214 | 2026-09-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-09-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 648 | 648 | 181 | 2026-09-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1142 | 2026-09-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1603 | 2026-09-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1871 | 1867 | 444 | 2026-09-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2420 | 2418 | 720 | 2026-09-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2819 | 2817 | 1998 | 2026-09-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3130 | 3128 | 956 | 2026-09-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 15901 | 15901 | 9067 | 2026-09-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 22566 | 22565 | 2522 | 2026-09-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 660 | 74 | 79/82 |
| http://34.43.46.91:80 | US | 671 | 74 | 79/82 |
| http://95.211.174.135:3128 | NL | 1093 | 68 | 81/82 |
| http://185.200.188.234:10001 | RU | 1271 | 68 | 81/82 |
| http://130.110.103.245:3128 | SA | 1572 | 68 | 80/82 |
| http://1.231.81.166:3128 | KR | 1141 | 47 | 79/82 |
| http://190.97.236.128:999 | VE | 1986 | 39 | 70/72 |
| http://190.97.236.129:999 | VE | 932 | 39 | 70/72 |
| http://95.3.69.222:8080 | TR | 1635 | 37 | 79/82 |
| http://107.167.18.122:443 | US | 86 | 27 | 33/34 |
| http://184.75.221.82:3118 | CA | 339 | 23 | 44/47 |
| http://91.134.141.4:3128 | FR | 797 | 21 | 41/43 |
| http://186.5.94.206:999 | EC | 4093 | 19 | 42/44 |
| http://107.150.41.226:18080 | US | 394 | 19 | 19/19 |
| http://38.51.207.104:8080 | VE | 771 | 15 | 22/23 |
| http://197.224.185.3:3128 | MU | 2301 | 13 | 46/50 |
| http://189.51.168.164:999 | MX | 4208 | 13 | 46/47 |
| http://45.132.252.25:49156 | RU | 1061 | 13 | 13/13 |
| http://193.104.179.115:3128 | UZ | 1476 | 12 | 30/47 |
| http://120.232.115.170:17981 | CN | 2950 | 11 | 60/81 |
| http://190.0.246.213:4040 | CO | 707 | 11 | 40/47 |
| http://213.111.146.36:18080 | NL | 742 | 11 | 14/19 |
| http://45.186.6.104:3128 | EC | 873 | 9 | 58/60 |
| http://61.91.162.126:8080 | TH | 1574 | 9 | 22/25 |
| http://103.10.231.189:8080 | TH | 1700 | 9 | 47/67 |
| http://153.51.201.35:999 | VE | 974 | 9 | 9/9 |
| http://8.138.217.152:21001 | CN | 3442 | 8 | 57/82 |
| http://123.121.123.216:8888 | CN | 1552 | 8 | 17/42 |
| http://176.111.37.216:39811 | HK | 1068 | 8 | 68/82 |
| http://152.42.177.32:8888 | SG | 1094 | 8 | 24/42 |
| http://201.71.2.25:999 | VE | 2528 | 8 | 23/69 |
| http://201.71.2.27:999 | VE | 4714 | 8 | 29/80 |
| socks5://36.155.23.163:10808 | CN | 1371 | 8 | 13/19 |
| http://177.234.217.237:999 | EC | 4535 | 7 | 24/55 |
| http://190.97.229.118:999 | VE | 7087 | 7 | 37/72 |
| http://190.97.241.106:999 | VE | 7191 | 7 | 42/66 |
| socks5://193.233.223.47:1080 | RU | 5555 | 7 | 7/7 |
| http://103.237.102.191:11111 | DE | 1059 | 6 | 77/82 |
| http://177.234.217.235:999 | EC | 5795 | 6 | 30/51 |
| http://37.59.125.131:8888 | FR | 1365 | 6 | 65/82 |
| http://176.111.37.5:39811 | HK | 1091 | 6 | 75/82 |
| http://205.164.192.115:999 | MX | 3362 | 6 | 51/80 |
| http://144.124.251.24:10000 | NL | 871 | 6 | 14/28 |
| http://144.124.251.24:10007 | NL | 1198 | 6 | 13/31 |
| http://144.124.251.24:10008 | NL | 1364 | 6 | 9/13 |
| http://144.124.251.24:10084 | NL | 973 | 6 | 10/14 |
| http://144.124.251.24:10104 | NL | 1193 | 6 | 9/14 |
| http://144.124.251.24:10176 | NL | 952 | 6 | 13/30 |
| http://144.124.251.24:10185 | NL | 1115 | 6 | 10/14 |
| http://144.124.251.24:10216 | NL | 957 | 6 | 14/31 |
| http://144.124.251.24:10226 | NL | 849 | 6 | 8/13 |
| http://144.124.251.24:10299 | NL | 914 | 6 | 10/14 |
| http://144.124.251.24:10333 | NL | 4537 | 6 | 12/31 |
| http://144.124.251.24:10337 | NL | 986 | 6 | 10/14 |
| http://144.124.251.24:10346 | NL | 989 | 6 | 10/14 |
| http://144.124.251.24:10366 | NL | 769 | 6 | 11/28 |
| http://144.124.251.24:10372 | NL | 813 | 6 | 13/26 |
| http://144.124.251.24:10412 | NL | 1045 | 6 | 10/14 |
| http://144.124.251.24:10431 | NL | 997 | 6 | 15/30 |
| http://144.124.251.24:10453 | NL | 803 | 6 | 12/19 |
| http://144.124.251.24:10471 | NL | 807 | 6 | 14/29 |
| http://144.124.251.24:10485 | NL | 1156 | 6 | 9/14 |
| http://144.124.251.24:10551 | NL | 823 | 6 | 14/30 |
| http://144.124.251.24:10566 | NL | 956 | 6 | 11/15 |
| http://144.124.251.24:10574 | NL | 798 | 6 | 14/31 |
| http://144.124.251.24:10605 | NL | 971 | 6 | 10/14 |
| http://144.124.251.24:10610 | NL | 1059 | 6 | 10/14 |
| http://144.124.251.24:10628 | NL | 1084 | 6 | 9/14 |
| http://144.124.251.24:10631 | NL | 977 | 6 | 10/14 |
| http://144.124.251.24:10658 | NL | 1020 | 6 | 10/14 |
| http://144.124.251.24:10689 | NL | 1018 | 6 | 11/18 |
| http://144.124.251.24:10771 | NL | 1083 | 6 | 9/14 |
| http://144.124.251.24:10800 | NL | 1041 | 6 | 10/14 |
| http://144.124.251.24:10811 | NL | 977 | 6 | 10/14 |
| http://144.124.251.24:10829 | NL | 924 | 6 | 9/14 |
| http://144.124.251.24:10953 | NL | 989 | 6 | 10/14 |
| http://144.124.251.24:11011 | NL | 1096 | 6 | 10/14 |
| http://144.124.251.24:11108 | NL | 984 | 6 | 11/29 |
| http://144.124.251.24:11124 | NL | 924 | 6 | 13/31 |
| http://144.124.251.24:11180 | NL | 841 | 6 | 9/13 |
| http://144.124.251.24:11265 | NL | 811 | 6 | 13/30 |
| http://144.124.251.24:11266 | NL | 1076 | 6 | 10/14 |
| http://144.124.251.24:11274 | NL | 870 | 6 | 13/30 |
| http://144.124.251.24:11480 | NL | 932 | 6 | 8/14 |
| http://144.124.251.24:11491 | NL | 812 | 6 | 13/30 |
| http://195.19.217.200:3128 | RU | 2410 | 6 | 7/8 |
| http://43.128.76.140:8081 | SG | 5047 | 6 | 11/12 |
| http://43.156.174.122:8080 | SG | 5148 | 6 | 6/6 |
| http://167.99.74.174:9090 | SG | 887 | 6 | 25/42 |
| socks5://144.24.111.128:1088 | IN | 1568 | 6 | 63/82 |
| socks5://161.35.90.93:1082 | NL | 2532 | 6 | 44/82 |
| http://103.61.234.186:8180 | ID | 7523 | 5 | 35/79 |
| http://103.130.61.61:8081 | ID | 1980 | 5 | 65/82 |
| http://157.85.111.64:3128 | TH | 4125 | 5 | 37/50 |
| socks5://45.32.160.61:1088 | US | 428 | 5 | 32/35 |
| socks5://83.147.217.103:1080 | US | 467 | 5 | 5/5 |
| http://41.196.16.230:1976 | EG | 1285 | 4 | 6/7 |
| http://41.196.16.230:1981 | EG | 1235 | 4 | 5/6 |
| http://62.193.104.26:1981 | EG | 3961 | 4 | 6/10 |
| http://154.236.168.162:1981 | EG | 5026 | 4 | 7/24 |
