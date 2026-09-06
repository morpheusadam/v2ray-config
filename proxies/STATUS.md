# Proxy status

Generated 2026-09-06T16:05:17Z by `harvest.py`.

- **798** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1291** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16231** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 199/600 (33%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 940 |
| socks5 | 336 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 160 |
| US | 127 |
| CN | 119 |
| RU | 66 |
| NL | 55 |
| SG | 50 |
| DE | 49 |
| CO | 43 |
| IN | 41 |
| BD | 40 |
| VN | 37 |
| FR | 31 |
| MX | 31 |
| HK | 29 |
| PH | 28 |
| BR | 24 |
| VE | 24 |
| EC | 22 |
| PK | 22 |
| EG | 21 |
| KH | 19 |
| FI | 18 |
| TH | 17 |
| JP | 15 |
| DO | 12 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 11 | 11 | 3 | 2026-09-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 70 | 70 | 38 | 2026-09-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 116 | 116 | 19 | 2026-09-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 127 | 127 | 57 | 2026-09-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-09-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 176 | 176 | 92 | 2026-09-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 225 | 225 | 45 | 2026-09-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 269 | 269 | 19 | 2026-09-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 487 | 487 | 202 | 2026-09-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 584 | 584 | 227 | 2026-09-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1473 | 1473 | 249 | 2026-09-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-09-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1605 | 2026-09-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2383 | 2383 | 1676 | 2026-09-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2428 | 2426 | 218 | 2026-09-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2841 | 2839 | 749 | 2026-09-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2889 | 2887 | 2193 | 2026-09-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 675 | 46 | 51/54 |
| http://34.43.46.91:80 | US | 517 | 46 | 51/54 |
| http://95.211.174.135:3128 | NL | 1229 | 40 | 53/54 |
| http://185.200.188.234:10001 | RU | 2954 | 40 | 53/54 |
| http://130.110.103.245:3128 | SA | 1543 | 40 | 52/54 |
| http://199.7.149.96:3128 | US | 368 | 33 | 33/33 |
| http://64.112.184.210:3128 | US | 537 | 32 | 53/54 |
| http://103.211.103.170:3128 | HK | 2986 | 26 | 26/26 |
| http://68.178.174.239:3128 | US | 887 | 22 | 22/22 |
| http://68.178.174.239:8888 | US | 890 | 22 | 22/22 |
| http://1.231.81.166:3128 | KR | 1024 | 19 | 51/54 |
| http://189.51.168.164:999 | MX | 562 | 19 | 19/19 |
| socks5://193.25.215.182:22222 | US | 550 | 17 | 50/54 |
| http://116.202.172.187:11000 | DE | 880 | 15 | 15/15 |
| http://91.134.141.4:3128 | FR | 800 | 15 | 15/15 |
| http://173.212.240.48:8888 | FR | 2878 | 15 | 15/15 |
| http://5.129.254.129:8888 | RU | 1278 | 15 | 15/15 |
| socks5://171.25.158.95:1080 | SE | 1651 | 15 | 31/53 |
| http://176.111.37.5:39811 | HK | 1125 | 14 | 48/54 |
| http://14.251.13.20:8080 | VN | 2390 | 14 | 25/26 |
| http://37.59.125.131:8888 | FR | 1495 | 12 | 41/54 |
| http://154.59.56.73:999 | VE | 1835 | 12 | 23/26 |
| socks5://101.36.104.46:10808 | JP | 1100 | 12 | 50/54 |
| http://120.232.115.170:17981 | CN | 2205 | 11 | 36/53 |
| http://181.78.23.187:999 | CO | 984 | 11 | 21/23 |
| http://181.78.74.252:999 | CO | 950 | 11 | 43/45 |
| http://181.78.74.253:999 | CO | 984 | 11 | 43/45 |
| http://190.97.236.128:999 | VE | 796 | 11 | 42/44 |
| http://190.97.236.129:999 | VE | 808 | 11 | 42/44 |
| http://103.177.118.145:8118 | BD | 1529 | 10 | 33/35 |
| http://186.5.94.206:999 | EC | 1048 | 10 | 15/16 |
| http://197.164.101.13:1981 | EG | 5878 | 10 | 15/43 |
| http://175.136.239.173:8181 | MY | 3518 | 10 | 43/54 |
| socks5://101.36.104.239:10808 | JP | 868 | 10 | 45/54 |
| socks5://5.255.117.127:1080 | NL | 946 | 10 | 17/30 |
| socks5://147.45.60.124:1082 | US | 556 | 10 | 30/54 |
| http://176.111.37.216:39811 | HK | 956 | 9 | 42/54 |
| http://197.224.185.3:3128 | MU | 1975 | 9 | 20/22 |
| http://5.129.254.49:8888 | RU | 1364 | 9 | 9/9 |
| http://5.129.254.51:8888 | RU | 1339 | 9 | 9/9 |
| http://5.129.254.70:8888 | RU | 1312 | 9 | 9/9 |
| http://157.85.97.240:3128 | TH | 1090 | 9 | 16/22 |
| http://95.3.69.222:8080 | TR | 1590 | 9 | 51/54 |
| socks4://45.61.129.165:9050 | US | 1899 | 9 | 45/54 |
| socks5://165.22.63.133:1080 | SG | 1072 | 9 | 10/11 |
| socks5://188.166.217.100:1080 | SG | 1191 | 9 | 9/9 |
| socks5://43.135.176.121:1080 | US | 1162 | 9 | 9/9 |
| http://5.129.254.60:8888 | RU | 1300 | 8 | 8/8 |
| http://157.85.97.204:3128 | TH | 1279 | 8 | 16/19 |
| socks5://143.198.205.96:1080 | SG | 1075 | 8 | 8/8 |
| http://103.237.102.191:11111 | DE | 999 | 7 | 51/54 |
| http://65.1.240.131:3001 | IN | 1180 | 7 | 7/7 |
| http://5.129.254.5:8888 | RU | 1349 | 7 | 8/9 |
| http://202.28.194.139:31280 | TH | 1895 | 7 | 51/54 |
| http://193.104.179.115:3128 | UZ | 1734 | 7 | 9/19 |
| socks5://144.91.111.48:1088 | FR | 1225 | 7 | 26/54 |
| socks5://144.24.111.128:1088 | IN | 1753 | 7 | 42/54 |
| socks5://193.233.218.121:1080 | RU | 1492 | 7 | 8/9 |
| socks5://143.198.93.65:1080 | SG | 1082 | 7 | 7/7 |
| socks5://159.223.86.111:1080 | SG | 1080 | 7 | 7/7 |
| socks5://45.32.160.61:1088 | US | 524 | 7 | 7/7 |
| socks5://185.222.138.237:1080 | XK | 1199 | 7 | 7/7 |
| http://111.192.25.85:8888 | CN | 1224 | 6 | 10/19 |
| http://167.233.89.17:1084 | DE | 1464 | 6 | 6/6 |
| http://167.233.148.141:1083 | DE | 4616 | 6 | 6/6 |
| http://167.233.169.253:1083 | DE | 1291 | 6 | 6/6 |
| http://186.33.45.218:999 | EC | 5390 | 6 | 28/43 |
| http://107.167.18.122:443 | US | 6151 | 6 | 6/6 |
| http://190.97.241.106:999 | VE | 1106 | 6 | 15/38 |
| http://210.211.113.37:80 | VN | 2620 | 6 | 18/26 |
| socks5://103.210.161.8:1080 | CN | 1144 | 6 | 19/27 |
| socks5://123.58.219.171:10808 | HK | 1495 | 6 | 45/54 |
| http://185.191.239.248:3128 | CH | 1544 | 5 | 40/53 |
| http://39.106.170.168:8080 | CN | 1277 | 5 | 23/52 |
| http://47.110.226.74:19991 | CN | 5864 | 5 | 20/52 |
| http://18.157.123.132:3128 | DE | 816 | 5 | 14/15 |
| http://117.236.124.166:3128 | IN | 1645 | 5 | 34/54 |
| http://175.139.255.25:8181 | MY | 5798 | 5 | 39/54 |
| http://5.129.254.154:8888 | RU | 1304 | 5 | 5/5 |
| http://140.99.255.67:8181 | US | 241 | 5 | 5/5 |
| http://210.211.113.34:80 | VN | 2715 | 5 | 22/26 |
| socks5://38.49.210.79:40000 | CA | 6682 | 5 | 22/54 |
| socks5://47.76.175.249:1080 | HK | 3546 | 5 | 5/5 |
| socks5://157.245.159.157:1080 | SG | 1120 | 5 | 5/5 |
| http://38.7.195.55:999 | CL | 2425 | 4 | 11/28 |
| http://175.143.76.177:8181 | MY | 2845 | 4 | 41/54 |
| http://42.96.18.62:1311 | VN | 1366 | 4 | 40/53 |
| socks5://65.109.196.122:2091 | FI | 7137 | 4 | 7/8 |
| socks5://223.25.110.37:8199 | ID | 3702 | 4 | 15/53 |
| socks5://5.255.103.55:1080 | NL | 1633 | 4 | 15/53 |
| socks5://146.190.90.120:1080 | SG | 1160 | 4 | 5/7 |
| socks5://167.172.79.22:1080 | SG | 1083 | 4 | 5/7 |
| socks5://206.189.33.43:1080 | SG | 1078 | 4 | 5/7 |
| socks5://107.173.230.93:40000 | US | 2284 | 4 | 4/4 |
| socks5://147.45.60.246:1082 | US | 2437 | 4 | 18/53 |
| http://36.137.204.11:8001 | CN | 2999 | 3 | 4/14 |
| http://47.121.139.13:3128 | CN | 2014 | 3 | 22/53 |
| http://123.115.227.124:8888 | CN | 5466 | 3 | 7/19 |
| http://123.119.178.176:8888 | CN | 6387 | 3 | 9/19 |
| http://123.121.122.28:8888 | CN | 3274 | 3 | 3/3 |
