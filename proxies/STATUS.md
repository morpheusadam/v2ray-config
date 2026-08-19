# Proxy status

Generated 2026-08-19T13:48:28Z by `harvest.py`.

- **601** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1309** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13128** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 166/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1057 |
| socks5 | 232 |
| socks4 | 20 |

| country | entries |
|---|---|
| ID | 319 |
| US | 99 |
| RU | 66 |
| CO | 61 |
| PH | 58 |
| MX | 43 |
| CN | 42 |
| BD | 40 |
| BR | 38 |
| TR | 35 |
| FR | 34 |
| VE | 27 |
| DE | 26 |
| EC | 26 |
| SG | 25 |
| NL | 23 |
| HK | 19 |
| JP | 17 |
| AR | 16 |
| IN | 16 |
| VN | 16 |
| KH | 14 |
| DO | 13 |
| IR | 13 |
| KE | 12 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-08-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 74 | 74 | 39 | 2026-08-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 102 | 102 | 10 | 2026-08-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 113 | 113 | 25 | 2026-08-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 124 | 124 | 23 | 2026-08-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 134 | 134 | 59 | 2026-08-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 86 | 2026-08-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 158 | 158 | 52 | 2026-08-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 195 | 195 | 85 | 2026-08-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 419 | 419 | 189 | 2026-08-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-08-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-08-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1135 | 2026-08-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1615 | 2026-08-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1975 | 1971 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2179 | 2177 | 179 | 2026-08-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2501 | 2501 | 1912 | 2026-08-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2705 | 2703 | 708 | 2026-08-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2901 | 2899 | 2318 | 2026-08-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2422 | 18 | 18/18 |
| http://64.112.184.210:3128 | US | 139 | 18 | 18/18 |
| socks5://69.55.49.177:38182 | US | 1321 | 18 | 18/18 |
| http://181.39.25.196:8118 | EC | 766 | 15 | 17/18 |
| http://190.0.246.210:4040 | CO | 1384 | 14 | 16/17 |
| http://34.43.46.91:443 | US | 1007 | 10 | 15/18 |
| http://34.43.46.91:80 | US | 1185 | 10 | 15/18 |
| http://181.78.74.252:999 | CO | 683 | 9 | 9/9 |
| http://181.78.74.253:999 | CO | 690 | 9 | 9/9 |
| http://157.230.178.216:40000 | US | 1691 | 9 | 16/17 |
| http://190.97.236.128:999 | VE | 659 | 8 | 8/8 |
| http://190.97.236.129:999 | VE | 660 | 8 | 8/8 |
| http://213.136.77.119:8888 | FR | 809 | 6 | 6/6 |
| http://190.12.150.244:999 | EC | 6523 | 5 | 10/14 |
| http://49.51.253.118:8888 | US | 1018 | 5 | 5/5 |
| socks4://163.192.14.135:50161 | US | 6030 | 5 | 11/17 |
| http://8.138.217.152:21001 | CN | 3740 | 4 | 11/18 |
| http://47.107.82.96:30051 | CN | 2256 | 4 | 9/11 |
| http://45.179.200.38:999 | CO | 4587 | 4 | 4/4 |
| http://103.237.102.191:11111 | DE | 1116 | 4 | 17/18 |
| http://191.44.125.11:8080 | FR | 6977 | 4 | 5/16 |
| http://212.58.132.5:8888 | GB | 1330 | 4 | 13/17 |
| http://176.111.37.5:39811 | HK | 1200 | 4 | 17/18 |
| http://176.111.37.216:39811 | HK | 814 | 4 | 16/18 |
| http://103.147.134.114:8082 | ID | 3812 | 4 | 4/4 |
| http://117.236.124.166:3128 | IN | 1446 | 4 | 11/18 |
| http://1.231.81.166:3128 | KR | 1224 | 4 | 17/18 |
| http://94.131.92.155:3128 | KZ | 5201 | 4 | 10/16 |
| http://175.136.239.173:8181 | MY | 3924 | 4 | 14/18 |
| http://175.143.76.177:8181 | MY | 2777 | 4 | 15/18 |
| http://95.211.174.135:3128 | NL | 722 | 4 | 17/18 |
| http://204.76.203.9:3128 | NL | 1100 | 4 | 17/18 |
| http://204.76.203.9:8080 | NL | 537 | 4 | 10/11 |
| http://185.141.26.131:3128 | RO | 437 | 4 | 4/4 |
| http://85.193.65.88:8888 | RU | 1180 | 4 | 7/8 |
| http://185.200.188.234:10001 | RU | 1155 | 4 | 17/18 |
| http://130.110.103.245:3128 | SA | 1078 | 4 | 16/18 |
| http://202.28.194.139:31280 | TH | 1925 | 4 | 17/18 |
| http://95.3.69.222:8080 | TR | 1304 | 4 | 17/18 |
| http://34.69.61.247:80 | US | 293 | 4 | 11/17 |
| http://45.66.249.187:3128 | US | 718 | 4 | 8/9 |
| http://45.66.249.187:8080 | US | 494 | 4 | 10/13 |
| http://45.66.249.187:8181 | US | 722 | 4 | 8/9 |
| http://42.96.18.62:1311 | VN | 5102 | 4 | 12/17 |
| socks5://45.144.54.40:1080 | DE | 1475 | 4 | 12/18 |
| socks5://144.91.111.48:1088 | FR | 2085 | 4 | 15/18 |
| socks5://144.91.121.61:1088 | FR | 2134 | 4 | 17/18 |
| socks5://150.241.91.238:7777 | FR | 3588 | 4 | 4/4 |
| socks5://212.58.132.5:1080 | GB | 1720 | 4 | 17/18 |
| socks5://144.24.111.128:1088 | IN | 1606 | 4 | 13/18 |
| socks5://178.128.82.131:10808 | SG | 6148 | 4 | 9/18 |
| socks5://43.162.94.99:1080 | US | 863 | 4 | 14/18 |
| socks5://45.61.129.165:9050 | US | 6038 | 4 | 15/18 |
| http://116.62.60.22:3128 | CN | 3798 | 3 | 3/3 |
| http://120.232.115.170:17981 | CN | 2344 | 3 | 8/17 |
| http://87.251.77.29:3128 | DE | 922 | 3 | 16/18 |
| http://41.128.90.50:1976 | EG | 3997 | 3 | 3/3 |
| http://43.99.100.108:3128 | HK | 1796 | 3 | 15/18 |
| http://45.198.32.207:8080 | ID | 4563 | 3 | 4/7 |
| http://103.130.61.61:8081 | ID | 1996 | 3 | 15/18 |
| http://103.164.212.125:8080 | ID | 7489 | 3 | 4/10 |
| http://118.99.68.149:8888 | ID | 7313 | 3 | 6/17 |
| http://119.2.41.29:8080 | ID | 5026 | 3 | 4/14 |
| http://203.2.151.13:8080 | ID | 2727 | 3 | 6/11 |
| http://5.129.228.92:443 | NL | 492 | 3 | 3/3 |
| http://122.52.189.109:8080 | PH | 5738 | 3 | 4/8 |
| http://124.83.107.140:8082 | PH | 6632 | 3 | 3/3 |
| http://77.222.54.205:3128 | RU | 778 | 3 | 3/3 |
| http://95.189.35.234:81 | RU | 2670 | 3 | 9/16 |
| http://43.156.228.168:80 | SG | 1405 | 3 | 9/17 |
| http://103.10.231.189:8080 | TH | 1933 | 3 | 3/3 |
| http://216.106.179.216:49331 | US | 411 | 3 | 7/17 |
| http://216.106.182.177:3128 | US | 284 | 3 | 15/18 |
| http://43.109.48.179:9999 | VN | 1363 | 3 | 6/16 |
| socks5://147.45.221.115:1082 | AL | 3705 | 3 | 11/18 |
| socks5://103.138.145.228:1999 | BD | 5044 | 3 | 6/16 |
| socks5://119.148.20.109:22122 | BD | 5083 | 3 | 7/9 |
| socks5://77.239.106.24:1080 | DE | 1638 | 3 | 3/3 |
| socks5://159.195.49.27:1080 | DE | 612 | 3 | 11/17 |
| socks5://45.95.233.88:1082 | FR | 620 | 3 | 8/15 |
| socks5://103.111.136.82:8199 | ID | 4134 | 3 | 5/13 |
| socks5://95.31.16.116:1081 | RU | 917 | 3 | 7/9 |
| socks5://216.106.179.216:49571 | US | 2507 | 3 | 6/17 |
| http://103.185.250.142:1452 | BD | 5008 | 2 | 2/2 |
| http://187.49.176.141:8080 | BR | 2876 | 2 | 3/8 |
| http://200.95.184.50:999 | CL | 5940 | 2 | 4/10 |
| http://27.185.218.213:17981 | CN | 2692 | 2 | 9/18 |
| http://47.101.182.85:13443 | CN | 6766 | 2 | 3/4 |
| http://38.19.43.139:999 | CO | 2320 | 2 | 2/2 |
| http://64.204.90.17:999 | CO | 7063 | 2 | 3/6 |
| http://190.109.1.58:8080 | CO | 5550 | 2 | 4/13 |
| http://190.121.135.9:8080 | CO | 1724 | 2 | 2/2 |
| http://200.10.31.45:8081 | CO | 2795 | 2 | 6/15 |
| http://38.75.82.212:999 | DO | 3752 | 2 | 6/12 |
| http://45.176.99.58:999 | DO | 5301 | 2 | 8/13 |
| http://186.33.45.218:999 | EC | 4039 | 2 | 4/7 |
| http://41.65.103.190:8080 | EG | 6302 | 2 | 6/17 |
| http://65.108.159.129:8081 | FI | 2465 | 2 | 6/16 |
| http://80.241.214.192:3128 | FR | 3731 | 2 | 2/2 |
| http://85.117.62.70:8080 | GE | 2953 | 2 | 4/11 |
