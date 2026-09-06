# Proxy status

Generated 2026-09-06T21:42:06Z by `harvest.py`.

- **690** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1317** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16115** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 197/600 (33%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 953 |
| socks5 | 347 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 183 |
| CN | 132 |
| US | 130 |
| SG | 58 |
| RU | 57 |
| DE | 52 |
| NL | 51 |
| BD | 47 |
| CO | 45 |
| IN | 40 |
| VN | 39 |
| MX | 37 |
| VE | 29 |
| HK | 28 |
| PH | 28 |
| FR | 27 |
| EC | 23 |
| EG | 20 |
| KH | 20 |
| PK | 19 |
| BR | 18 |
| FI | 18 |
| TH | 16 |
| JP | 14 |
| AR | 11 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 62 | 62 | 30 | 2026-09-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 117 | 117 | 34 | 2026-09-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 127 | 127 | 12 | 2026-09-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 85 | 2026-09-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 160 | 160 | 76 | 2026-09-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 244 | 244 | 6 | 2026-09-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 282 | 282 | 36 | 2026-09-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 477 | 477 | 164 | 2026-09-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 494 | 494 | 190 | 2026-09-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-09-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1537 | 1533 | 240 | 2026-09-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1113 | 2026-09-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1601 | 2026-09-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2281 | 2279 | 171 | 2026-09-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2523 | 2523 | 1659 | 2026-09-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2778 | 2776 | 758 | 2026-09-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2984 | 2982 | 2267 | 2026-09-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 518 | 47 | 52/55 |
| http://34.43.46.91:80 | US | 2499 | 47 | 52/55 |
| http://95.211.174.135:3128 | NL | 950 | 41 | 54/55 |
| http://185.200.188.234:10001 | RU | 1201 | 41 | 54/55 |
| http://130.110.103.245:3128 | SA | 1385 | 41 | 53/55 |
| http://199.7.149.96:3128 | US | 176 | 34 | 34/34 |
| http://64.112.184.210:3128 | US | 421 | 33 | 54/55 |
| http://103.211.103.170:3128 | HK | 672 | 27 | 27/27 |
| http://68.178.174.239:3128 | US | 1031 | 23 | 23/23 |
| http://68.178.174.239:8888 | US | 1041 | 23 | 23/23 |
| http://1.231.81.166:3128 | KR | 1135 | 20 | 52/55 |
| http://189.51.168.164:999 | MX | 495 | 20 | 20/20 |
| socks5://193.25.215.182:22222 | US | 833 | 18 | 51/55 |
| http://116.202.172.187:11000 | DE | 879 | 16 | 16/16 |
| http://91.134.141.4:3128 | FR | 781 | 16 | 16/16 |
| http://173.212.240.48:8888 | FR | 1087 | 16 | 16/16 |
| http://5.129.254.129:8888 | RU | 1773 | 16 | 16/16 |
| socks5://171.25.158.95:1080 | SE | 4710 | 16 | 32/54 |
| http://176.111.37.5:39811 | HK | 1102 | 15 | 49/55 |
| http://14.251.13.20:8080 | VN | 1276 | 15 | 26/27 |
| http://154.59.56.73:999 | VE | 1580 | 13 | 24/27 |
| http://120.232.115.170:17981 | CN | 2238 | 12 | 37/54 |
| http://181.78.23.187:999 | CO | 782 | 12 | 22/24 |
| http://181.78.74.252:999 | CO | 783 | 12 | 44/46 |
| http://181.78.74.253:999 | CO | 845 | 12 | 44/46 |
| http://190.97.236.128:999 | VE | 683 | 12 | 43/45 |
| http://190.97.236.129:999 | VE | 753 | 12 | 43/45 |
| http://103.177.118.145:8118 | BD | 1581 | 11 | 34/36 |
| http://186.5.94.206:999 | EC | 986 | 11 | 16/17 |
| http://175.136.239.173:8181 | MY | 3472 | 11 | 44/55 |
| socks5://5.255.117.127:1080 | NL | 746 | 11 | 18/31 |
| socks5://147.45.60.124:1082 | US | 4530 | 11 | 31/55 |
| http://176.111.37.216:39811 | HK | 927 | 10 | 43/55 |
| http://197.224.185.3:3128 | MU | 1940 | 10 | 21/23 |
| http://5.129.254.49:8888 | RU | 6066 | 10 | 10/10 |
| http://5.129.254.51:8888 | RU | 2404 | 10 | 10/10 |
| http://5.129.254.70:8888 | RU | 2438 | 10 | 10/10 |
| http://95.3.69.222:8080 | TR | 1943 | 10 | 52/55 |
| socks4://45.61.129.165:9050 | US | 3274 | 10 | 46/55 |
| socks5://165.22.63.133:1080 | SG | 1280 | 10 | 11/12 |
| socks5://188.166.217.100:1080 | SG | 1442 | 10 | 10/10 |
| socks5://43.135.176.121:1080 | US | 424 | 10 | 10/10 |
| http://5.129.254.60:8888 | RU | 1293 | 9 | 9/9 |
| http://157.85.97.204:3128 | TH | 1263 | 9 | 17/20 |
| socks5://143.198.205.96:1080 | SG | 1374 | 9 | 9/9 |
| http://103.237.102.191:11111 | DE | 1883 | 8 | 52/55 |
| http://5.129.254.5:8888 | RU | 1334 | 8 | 9/10 |
| http://202.28.194.139:31280 | TH | 2288 | 8 | 52/55 |
| http://193.104.179.115:3128 | UZ | 1453 | 8 | 10/20 |
| socks5://144.91.111.48:1088 | FR | 6125 | 8 | 27/55 |
| socks5://144.24.111.128:1088 | IN | 2690 | 8 | 43/55 |
| socks5://193.233.218.121:1080 | RU | 1293 | 8 | 9/10 |
| socks5://143.198.93.65:1080 | SG | 2023 | 8 | 8/8 |
| socks5://159.223.86.111:1080 | SG | 1236 | 8 | 8/8 |
| socks5://45.32.160.61:1088 | US | 454 | 8 | 8/8 |
| socks5://185.222.138.237:1080 | XK | 1029 | 8 | 8/8 |
| http://167.233.148.141:1083 | DE | 3561 | 7 | 7/7 |
| http://167.233.169.253:1083 | DE | 1653 | 7 | 7/7 |
| http://186.33.45.218:999 | EC | 3754 | 7 | 29/44 |
| http://190.97.241.106:999 | VE | 1533 | 7 | 16/39 |
| http://210.211.113.37:80 | VN | 4861 | 7 | 19/27 |
| socks5://103.210.161.8:1080 | CN | 1720 | 7 | 20/28 |
| socks5://123.58.219.171:10808 | HK | 2041 | 7 | 46/55 |
| http://185.191.239.248:3128 | CH | 2001 | 6 | 41/54 |
| http://39.106.170.168:8080 | CN | 1837 | 6 | 24/53 |
| http://117.236.124.166:3128 | IN | 1658 | 6 | 35/55 |
| http://175.139.255.25:8181 | MY | 2107 | 6 | 40/55 |
| http://5.129.254.154:8888 | RU | 2410 | 6 | 6/6 |
| socks5://47.76.175.249:1080 | HK | 1377 | 6 | 6/6 |
| socks5://157.245.159.157:1080 | SG | 2120 | 6 | 6/6 |
| http://38.7.195.55:999 | CL | 6454 | 5 | 12/29 |
| http://42.96.18.62:1311 | VN | 1904 | 5 | 41/54 |
| socks5://65.109.196.122:2091 | FI | 1988 | 5 | 8/9 |
| socks5://223.25.110.37:8199 | ID | 3753 | 5 | 16/54 |
| socks5://5.255.103.55:1080 | NL | 2101 | 5 | 16/54 |
| socks5://146.190.90.120:1080 | SG | 1696 | 5 | 6/8 |
| socks5://167.172.79.22:1080 | SG | 1414 | 5 | 6/8 |
| socks5://206.189.33.43:1080 | SG | 1234 | 5 | 6/8 |
| socks5://147.45.60.246:1082 | US | 4455 | 5 | 19/54 |
| http://123.119.178.176:8888 | CN | 1362 | 4 | 10/20 |
| http://123.121.129.198:8888 | CN | 2153 | 4 | 13/20 |
| http://221.221.154.156:8888 | CN | 1772 | 4 | 7/15 |
| http://221.221.163.120:8888 | CN | 1689 | 4 | 6/8 |
| http://167.233.169.253:1082 | DE | 1170 | 4 | 4/4 |
| http://167.233.169.253:1084 | DE | 2650 | 4 | 4/4 |
| http://196.61.42.26:3128 | GH | 4333 | 4 | 9/23 |
| http://168.144.84.188:3129 | IN | 1485 | 4 | 9/13 |
| http://77.235.24.145:3129 | KG | 3180 | 4 | 4/4 |
| http://152.42.177.32:8888 | SG | 1063 | 4 | 10/15 |
| http://157.85.108.47:3128 | TH | 2278 | 4 | 17/23 |
| http://161.35.181.96:999 | US | 282 | 4 | 4/4 |
| http://154.59.56.74:999 | VE | 3281 | 4 | 11/18 |
| socks5://109.172.55.227:1082 | FR | 833 | 4 | 21/53 |
| socks5://117.244.114.54:1080 | IN | 4965 | 4 | 12/50 |
| socks5://108.174.152.80:1080 | MX | 510 | 4 | 4/4 |
| socks5://93.87.38.20:1090 | RS | 1975 | 4 | 10/12 |
| socks5://167.172.87.244:1080 | SG | 1349 | 4 | 5/8 |
| socks5://107.181.252.58:1081 | US | 615 | 4 | 4/4 |
| http://8.138.217.152:21001 | CN | 3475 | 3 | 36/55 |
| http://47.107.82.96:30051 | CN | 1808 | 3 | 31/48 |
