# Proxy status

Generated 2026-09-04T21:47:42Z by `harvest.py`.

- **1180** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2117** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16295** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 165/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1785 |
| socks5 | 317 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 363 |
| US | 215 |
| CN | 126 |
| MX | 82 |
| RU | 63 |
| BD | 59 |
| IN | 59 |
| PH | 59 |
| CO | 57 |
| FR | 57 |
| NL | 56 |
| JP | 54 |
| SG | 53 |
| BR | 48 |
| HK | 48 |
| VE | 48 |
| DE | 43 |
| CA | 39 |
| TH | 37 |
| VN | 37 |
| EC | 34 |
| KH | 24 |
| EG | 23 |
| IE | 23 |
| SE | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 3 | 3 | 1 | 2026-09-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 54 | 54 | 26 | 2026-09-04 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 105 | 105 | 37 | 2026-09-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 132 | 132 | 67 | 2026-09-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-09-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 157 | 157 | 46 | 2026-09-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 192 | 192 | 14 | 2026-09-04 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 205 | 205 | 32 | 2026-09-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 307 | 307 | 109 | 2026-09-04 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-09-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 796 | 796 | 471 | 2026-09-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-09-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1601 | 2026-09-04 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1988 | 1985 | 316 | 2026-09-04 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2305 | 2305 | 1686 | 2026-09-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2335 | 2333 | 168 | 2026-09-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2803 | 2801 | 714 | 2026-09-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2976 | 2974 | 2271 | 2026-09-04 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 750 | 43 | 48/51 |
| http://34.43.46.91:80 | US | 582 | 43 | 48/51 |
| http://95.211.174.135:3128 | NL | 876 | 37 | 50/51 |
| http://204.76.203.9:3128 | NL | 723 | 37 | 50/51 |
| http://204.76.203.9:8080 | NL | 522 | 37 | 43/44 |
| http://185.200.188.234:10001 | RU | 1033 | 37 | 50/51 |
| http://130.110.103.245:3128 | SA | 1030 | 37 | 49/51 |
| http://199.7.149.96:3128 | US | 26 | 30 | 30/30 |
| http://45.186.6.104:3128 | EC | 787 | 29 | 29/29 |
| http://64.112.184.210:3128 | US | 394 | 29 | 50/51 |
| http://103.211.103.170:3128 | HK | 489 | 23 | 23/23 |
| http://68.178.174.239:3128 | US | 1169 | 19 | 19/19 |
| http://68.178.174.239:8888 | US | 1188 | 19 | 19/19 |
| http://1.231.81.166:3128 | KR | 1306 | 16 | 48/51 |
| http://189.51.168.164:999 | MX | 5743 | 16 | 16/16 |
| socks5://193.25.215.182:22222 | US | 1142 | 14 | 47/51 |
| http://116.202.172.187:11000 | DE | 581 | 12 | 12/12 |
| http://91.134.141.4:3128 | FR | 477 | 12 | 12/12 |
| http://173.212.240.48:8888 | FR | 588 | 12 | 12/12 |
| http://5.129.254.129:8888 | RU | 4061 | 12 | 12/12 |
| socks5://171.25.158.95:1080 | SE | 2049 | 12 | 28/50 |
| http://176.111.37.5:39811 | HK | 787 | 11 | 45/51 |
| http://14.251.13.20:8080 | VN | 1387 | 11 | 22/23 |
| http://34.88.38.81:9443 | FI | 620 | 10 | 11/16 |
| http://37.59.125.131:8888 | FR | 3794 | 9 | 38/51 |
| http://154.59.56.73:999 | VE | 5793 | 9 | 20/23 |
| socks5://101.36.104.46:10808 | JP | 1370 | 9 | 47/51 |
| socks5://5.255.117.250:1080 | NL | 876 | 9 | 15/36 |
| http://120.232.115.170:17981 | CN | 1962 | 8 | 33/50 |
| http://181.78.23.187:999 | CO | 708 | 8 | 18/20 |
| http://181.78.74.252:999 | CO | 703 | 8 | 40/42 |
| http://181.78.74.253:999 | CO | 825 | 8 | 40/42 |
| http://190.97.236.128:999 | VE | 595 | 8 | 39/41 |
| http://190.97.236.129:999 | VE | 600 | 8 | 39/41 |
| http://103.177.118.145:8118 | BD | 3577 | 7 | 30/32 |
| http://186.5.94.206:999 | EC | 4900 | 7 | 12/13 |
| http://197.164.101.13:1981 | EG | 6007 | 7 | 12/40 |
| http://175.136.239.173:8181 | MY | 3410 | 7 | 40/51 |
| socks5://101.36.104.239:10808 | JP | 1228 | 7 | 42/51 |
| socks5://5.255.99.75:1080 | NL | 576 | 7 | 11/26 |
| socks5://5.255.117.127:1080 | NL | 590 | 7 | 14/27 |
| socks5://147.45.60.124:1082 | US | 1527 | 7 | 27/51 |
| socks5://178.130.47.21:1082 | US | 4509 | 7 | 23/50 |
| http://187.102.219.42:999 | AR | 5171 | 6 | 25/46 |
| http://114.236.137.41:21000 | CN | 1803 | 6 | 35/51 |
| http://123.57.213.24:3539 | CN | 1702 | 6 | 25/50 |
| http://194.163.175.167:40000 | FR | 645 | 6 | 15/16 |
| http://176.111.37.216:39811 | HK | 714 | 6 | 39/51 |
| http://197.224.185.3:3128 | MU | 1856 | 6 | 17/19 |
| http://5.129.254.49:8888 | RU | 1184 | 6 | 6/6 |
| http://5.129.254.51:8888 | RU | 2831 | 6 | 6/6 |
| http://5.129.254.70:8888 | RU | 1012 | 6 | 6/6 |
| http://85.193.65.88:8888 | RU | 1476 | 6 | 20/41 |
| http://157.85.97.240:3128 | TH | 1338 | 6 | 13/19 |
| http://157.85.111.64:3128 | TH | 1340 | 6 | 17/19 |
| http://95.3.69.222:8080 | TR | 1709 | 6 | 48/51 |
| http://44.204.11.88:44218 | US | 2232 | 6 | 7/9 |
| socks4://45.61.129.165:9050 | US | 3612 | 6 | 42/51 |
| socks5://79.137.79.217:2080 | FR | 583 | 6 | 6/6 |
| socks5://121.169.46.116:1090 | KR | 6080 | 6 | 34/51 |
| socks5://165.22.63.133:1080 | SG | 1422 | 6 | 7/8 |
| socks5://188.166.217.100:1080 | SG | 1396 | 6 | 6/6 |
| socks5://116.241.240.176:11080 | TW | 1389 | 6 | 7/8 |
| socks5://43.135.176.121:1080 | US | 1269 | 6 | 6/6 |
| http://111.192.19.39:8888 | CN | 1246 | 5 | 7/15 |
| http://38.211.76.177:999 | CO | 3669 | 5 | 6/9 |
| http://45.172.218.67:3028 | CO | 6346 | 5 | 22/41 |
| http://190.0.246.210:4040 | CO | 3254 | 5 | 45/50 |
| http://154.90.48.209:9090 | ID | 1813 | 5 | 8/10 |
| http://175.136.239.174:8181 | MY | 2526 | 5 | 33/51 |
| http://119.95.176.156:8082 | PH | 1465 | 5 | 5/5 |
| http://5.129.254.60:8888 | RU | 2080 | 5 | 5/5 |
| http://43.160.242.118:3128 | SG | 4140 | 5 | 39/48 |
| http://157.85.97.204:3128 | TH | 1313 | 5 | 13/16 |
| http://20.127.100.54:8080 | US | 7733 | 5 | 5/5 |
| socks4://51.159.149.245:80 | FR | 2374 | 5 | 5/5 |
| socks5://144.91.121.61:1088 | FR | 1805 | 5 | 46/51 |
| socks5://161.35.90.93:1082 | NL | 3929 | 5 | 26/51 |
| socks5://161.35.90.93:1083 | NL | 1591 | 5 | 23/49 |
| socks5://143.198.205.96:1080 | SG | 1388 | 5 | 5/5 |
| socks5://3.84.72.152:5555 | US | 169 | 5 | 5/5 |
| socks5://85.209.156.148:1080 | US | 5916 | 5 | 18/22 |
| http://184.75.221.82:3118 | CA | 238 | 4 | 15/16 |
| http://114.249.213.204:8888 | CN | 6051 | 4 | 10/16 |
| http://114.252.13.139:8888 | CN | 3296 | 4 | 4/4 |
| http://114.252.15.106:8888 | CN | 2881 | 4 | 4/4 |
| http://114.254.48.23:8888 | CN | 1562 | 4 | 4/4 |
| http://120.26.171.55:25125 | CN | 7744 | 4 | 21/49 |
| http://139.159.97.82:10900 | CN | 1495 | 4 | 14/20 |
| http://221.221.150.139:8888 | CN | 3112 | 4 | 6/10 |
| http://221.221.153.111:8888 | CN | 1604 | 4 | 7/15 |
| http://190.0.246.211:4040 | CO | 4498 | 4 | 43/51 |
| http://103.237.102.191:11111 | DE | 739 | 4 | 48/51 |
| http://103.130.61.61:8081 | ID | 7731 | 4 | 41/51 |
| http://14.139.235.82:3128 | IN | 2451 | 4 | 31/51 |
| http://65.1.240.131:3001 | IN | 1049 | 4 | 4/4 |
| http://5.129.228.92:443 | NL | 493 | 4 | 27/36 |
| http://5.129.254.5:8888 | RU | 2092 | 4 | 5/6 |
| http://202.28.194.139:31280 | TH | 2237 | 4 | 48/51 |
| http://52.21.158.119:3128 | US | 115 | 4 | 4/4 |
