# Proxy status

Generated 2026-09-04T17:01:03Z by `harvest.py`.

- **878** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1840** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16310** endpoints on record
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
| http | 1507 |
| socks5 | 321 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 284 |
| US | 191 |
| CN | 122 |
| NL | 64 |
| MX | 61 |
| SG | 57 |
| RU | 56 |
| BD | 52 |
| FR | 50 |
| CO | 47 |
| JP | 45 |
| HK | 44 |
| DE | 42 |
| IN | 39 |
| VN | 38 |
| BR | 36 |
| PH | 35 |
| TH | 33 |
| EG | 32 |
| CA | 30 |
| VE | 29 |
| AU | 28 |
| EC | 24 |
| KR | 24 |
| KH | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 2 | 2026-09-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 62 | 62 | 31 | 2026-09-04 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 117 | 117 | 19 | 2026-09-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 137 | 137 | 48 | 2026-09-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 70 | 2026-09-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 158 | 158 | 76 | 2026-09-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 206 | 206 | 26 | 2026-09-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 241 | 241 | 49 | 2026-09-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-04 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 407 | 407 | 160 | 2026-09-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 598 | 598 | 297 | 2026-09-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-09-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1129 | 2026-09-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1598 | 2026-09-04 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2000 | 1996 | 507 | 2026-09-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2349 | 2347 | 173 | 2026-09-04 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2411 | 2411 | 1664 | 2026-09-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2831 | 2829 | 689 | 2026-09-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3087 | 3085 | 2340 | 2026-09-04 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 570 | 42 | 47/50 |
| http://34.43.46.91:80 | US | 697 | 42 | 47/50 |
| http://95.211.174.135:3128 | NL | 1356 | 36 | 49/50 |
| http://204.76.203.9:3128 | NL | 1072 | 36 | 49/50 |
| http://204.76.203.9:8080 | NL | 809 | 36 | 42/43 |
| http://185.200.188.234:10001 | RU | 1608 | 36 | 49/50 |
| http://130.110.103.245:3128 | SA | 1449 | 36 | 48/50 |
| http://199.7.149.96:3128 | US | 393 | 29 | 29/29 |
| http://45.186.6.104:3128 | EC | 892 | 28 | 28/28 |
| http://64.112.184.210:3128 | US | 545 | 28 | 49/50 |
| http://103.211.103.170:3128 | HK | 1903 | 22 | 22/22 |
| http://68.178.174.239:3128 | US | 893 | 18 | 18/18 |
| http://68.178.174.239:8888 | US | 1147 | 18 | 18/18 |
| http://190.0.246.213:4040 | CO | 762 | 15 | 15/15 |
| http://1.231.81.166:3128 | KR | 1282 | 15 | 47/50 |
| http://189.51.168.164:999 | MX | 561 | 15 | 15/15 |
| socks5://193.25.215.182:22222 | US | 3569 | 13 | 46/50 |
| http://116.202.172.187:11000 | DE | 970 | 11 | 11/11 |
| http://91.134.141.4:3128 | FR | 802 | 11 | 11/11 |
| http://173.212.240.48:8888 | FR | 1062 | 11 | 11/11 |
| http://5.129.254.129:8888 | RU | 1324 | 11 | 11/11 |
| socks5://171.25.158.95:1080 | SE | 6490 | 11 | 27/49 |
| http://176.111.37.5:39811 | HK | 1481 | 10 | 44/50 |
| http://14.251.13.20:8080 | VN | 1055 | 10 | 21/22 |
| http://34.88.38.81:9443 | FI | 925 | 9 | 10/15 |
| http://16.174.6.134:3128 | CA | 4812 | 8 | 8/8 |
| http://37.59.125.131:8888 | FR | 3863 | 8 | 37/50 |
| http://154.59.56.73:999 | VE | 7380 | 8 | 19/22 |
| socks5://101.36.104.46:10808 | JP | 2286 | 8 | 46/50 |
| socks5://5.255.117.250:1080 | NL | 6100 | 8 | 14/35 |
| http://120.232.115.170:17981 | CN | 2229 | 7 | 32/49 |
| http://181.78.23.187:999 | CO | 863 | 7 | 17/19 |
| http://181.78.74.252:999 | CO | 873 | 7 | 39/41 |
| http://181.78.74.253:999 | CO | 855 | 7 | 39/41 |
| http://190.97.236.128:999 | VE | 786 | 7 | 38/40 |
| http://190.97.236.129:999 | VE | 866 | 7 | 38/40 |
| socks5://49.13.22.249:10801 | DE | 1826 | 7 | 12/19 |
| http://103.177.118.145:8118 | BD | 2472 | 6 | 29/31 |
| http://186.5.94.206:999 | EC | 2056 | 6 | 11/12 |
| http://197.164.101.13:1981 | EG | 1721 | 6 | 11/39 |
| http://175.136.239.173:8181 | MY | 2711 | 6 | 39/50 |
| http://85.198.100.232:13100 | RU | 1136 | 6 | 6/6 |
| socks5://5.75.133.113:10801 | DE | 6776 | 6 | 11/16 |
| socks5://101.36.104.239:10808 | JP | 1982 | 6 | 41/50 |
| socks5://5.255.99.75:1080 | NL | 1978 | 6 | 10/25 |
| socks5://5.255.117.127:1080 | NL | 962 | 6 | 13/26 |
| socks5://147.45.60.124:1082 | US | 717 | 6 | 26/50 |
| socks5://178.130.47.21:1082 | US | 2482 | 6 | 22/49 |
| http://187.102.219.42:999 | AR | 1260 | 5 | 24/45 |
| http://111.192.21.92:8888 | CN | 7264 | 5 | 12/14 |
| http://114.236.137.41:21000 | CN | 2053 | 5 | 34/50 |
| http://123.57.213.24:3539 | CN | 1493 | 5 | 24/49 |
| http://123.121.121.123:8888 | CN | 1566 | 5 | 13/15 |
| http://194.163.175.167:40000 | FR | 1249 | 5 | 14/15 |
| http://176.111.37.216:39811 | HK | 1261 | 5 | 38/50 |
| http://140.238.32.108:3128 | JP | 1916 | 5 | 23/49 |
| http://197.224.185.3:3128 | MU | 2146 | 5 | 16/18 |
| http://5.129.254.49:8888 | RU | 1373 | 5 | 5/5 |
| http://5.129.254.51:8888 | RU | 1384 | 5 | 5/5 |
| http://5.129.254.70:8888 | RU | 1266 | 5 | 5/5 |
| http://85.193.65.88:8888 | RU | 1779 | 5 | 19/40 |
| http://51.21.132.197:3128 | SE | 1410 | 5 | 8/10 |
| http://157.85.97.240:3128 | TH | 4149 | 5 | 12/18 |
| http://157.85.108.47:3128 | TH | 3111 | 5 | 13/18 |
| http://157.85.111.64:3128 | TH | 1054 | 5 | 16/18 |
| http://95.3.69.222:8080 | TR | 1569 | 5 | 47/50 |
| http://44.204.11.88:44218 | US | 1115 | 5 | 6/8 |
| socks5://45.95.233.88:1082 | FR | 1107 | 5 | 25/47 |
| socks5://79.137.79.217:2080 | FR | 1089 | 5 | 5/5 |
| socks5://80.72.180.122:1080 | KG | 3111 | 5 | 17/48 |
| socks5://121.169.46.116:1090 | KR | 1478 | 5 | 33/50 |
| socks5://165.22.63.133:1080 | SG | 1093 | 5 | 6/7 |
| socks5://188.166.217.100:1080 | SG | 1086 | 5 | 5/5 |
| socks5://116.241.240.176:11080 | TW | 3126 | 5 | 6/7 |
| socks5://43.135.176.121:1080 | US | 1271 | 5 | 5/5 |
| socks5://45.61.129.165:9050 | US | 2886 | 5 | 41/50 |
| http://111.192.19.39:8888 | CN | 1214 | 4 | 6/14 |
| http://119.188.131.55:17981 | CN | 2311 | 4 | 19/50 |
| http://38.211.76.177:999 | CO | 6168 | 4 | 5/8 |
| http://45.172.218.67:3028 | CO | 5141 | 4 | 21/40 |
| http://190.0.246.210:4040 | CO | 851 | 4 | 44/49 |
| http://154.90.48.209:9090 | ID | 1996 | 4 | 7/9 |
| http://175.136.239.174:8181 | MY | 2499 | 4 | 32/50 |
| http://119.95.176.156:8082 | PH | 1203 | 4 | 4/4 |
| http://5.129.254.60:8888 | RU | 1378 | 4 | 4/4 |
| http://109.94.1.23:4050 | RU | 2626 | 4 | 35/50 |
| http://43.160.242.118:3128 | SG | 1763 | 4 | 38/47 |
| http://157.85.97.204:3128 | TH | 1049 | 4 | 12/15 |
| http://20.127.100.54:8080 | US | 5355 | 4 | 4/4 |
| socks4://51.159.149.245:80 | FR | 7922 | 4 | 4/4 |
| socks5://51.178.49.241:1088 | FR | 6563 | 4 | 10/11 |
| socks5://144.91.121.61:1088 | FR | 1891 | 4 | 45/50 |
| socks5://152.70.107.226:1080 | JP | 914 | 4 | 10/47 |
| socks5://161.35.90.93:1082 | NL | 2403 | 4 | 25/50 |
| socks5://161.35.90.93:1083 | NL | 1264 | 4 | 22/48 |
| socks5://109.111.79.212:1080 | RU | 1657 | 4 | 11/28 |
| socks5://143.198.205.96:1080 | SG | 1081 | 4 | 4/4 |
| socks5://3.84.72.152:5555 | US | 516 | 4 | 4/4 |
| socks5://85.209.156.148:1080 | US | 4941 | 4 | 17/21 |
| http://16.174.83.123:3128 | CA | 2823 | 3 | 8/10 |
