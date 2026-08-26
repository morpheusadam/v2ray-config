# Proxy status

Generated 2026-08-26T22:29:51Z by `harvest.py`.

- **716** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1590** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14403** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 183/600 (30%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1304 |
| socks5 | 270 |
| socks4 | 16 |

| country | entries |
|---|---|
| ID | 325 |
| US | 75 |
| PH | 72 |
| CO | 66 |
| DE | 60 |
| RU | 59 |
| CN | 54 |
| BD | 51 |
| IN | 47 |
| MX | 46 |
| NL | 42 |
| BR | 41 |
| VE | 36 |
| FR | 34 |
| VN | 33 |
| EC | 32 |
| SG | 28 |
| TR | 28 |
| TH | 26 |
| AR | 22 |
| HK | 22 |
| JP | 21 |
| AU | 19 |
| CL | 19 |
| EG | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-08-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 77 | 77 | 26 | 2026-08-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 78 | 78 | 41 | 2026-08-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 93 | 93 | 42 | 2026-08-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 107 | 107 | 38 | 2026-08-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 113 | 113 | 31 | 2026-08-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 134 | 134 | 60 | 2026-08-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 149 | 149 | 43 | 2026-08-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 88 | 2026-08-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 458 | 458 | 194 | 2026-08-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-08-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-08-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-08-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1603 | 2026-08-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1858 | 1854 | 303 | 2026-08-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2136 | 2134 | 314 | 2026-08-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2257 | 2257 | 1754 | 2026-08-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2479 | 2477 | 685 | 2026-08-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2753 | 2751 | 2076 | 2026-08-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1257 | 30 | 32/33 |
| http://34.43.46.91:443 | US | 715 | 25 | 30/33 |
| http://34.43.46.91:80 | US | 750 | 25 | 30/33 |
| http://103.237.102.191:11111 | DE | 1085 | 19 | 32/33 |
| http://95.211.174.135:3128 | NL | 1265 | 19 | 32/33 |
| http://204.76.203.9:3128 | NL | 1348 | 19 | 32/33 |
| http://204.76.203.9:8080 | NL | 758 | 19 | 25/26 |
| http://185.200.188.234:10001 | RU | 1306 | 19 | 32/33 |
| http://130.110.103.245:3128 | SA | 1690 | 19 | 31/33 |
| http://95.3.69.222:8080 | TR | 1419 | 19 | 32/33 |
| http://199.7.149.90:3128 | US | 361 | 16 | 16/16 |
| http://199.7.149.96:3128 | US | 341 | 12 | 12/12 |
| http://45.186.6.104:3128 | EC | 770 | 11 | 11/11 |
| http://64.112.184.210:3128 | US | 660 | 11 | 32/33 |
| socks5://123.58.219.171:10808 | HK | 2981 | 11 | 27/33 |
| socks5://43.162.94.99:1080 | US | 606 | 10 | 26/33 |
| http://190.0.246.210:4040 | CO | 3047 | 9 | 29/32 |
| http://47.81.56.193:8888 | TH | 2579 | 9 | 17/33 |
| http://120.232.115.170:17981 | CN | 1455 | 8 | 19/32 |
| http://103.130.61.61:8081 | ID | 1418 | 8 | 28/33 |
| http://42.96.18.62:1311 | VN | 3028 | 7 | 22/32 |
| socks5://144.91.121.61:1088 | FR | 6924 | 7 | 31/33 |
| socks5://101.36.104.239:10808 | JP | 4822 | 7 | 27/33 |
| socks5://67.207.92.87:1088 | US | 497 | 7 | 18/32 |
| socks5://193.25.215.182:22222 | US | 1729 | 7 | 30/33 |
| http://176.111.37.5:39811 | HK | 1313 | 6 | 28/33 |
| http://212.154.169.90:3128 | KZ | 1371 | 6 | 10/12 |
| socks5://152.89.104.11:1080 | DE | 1100 | 6 | 11/33 |
| socks5://152.32.168.221:10808 | HK | 1351 | 6 | 16/22 |
| http://179.41.11.138:8080 | AR | 872 | 5 | 5/5 |
| http://185.191.239.248:3128 | CH | 1186 | 5 | 22/32 |
| http://190.0.246.211:4040 | CO | 2661 | 5 | 28/33 |
| http://18.170.25.193:57422 | GB | 6418 | 5 | 12/29 |
| http://103.211.103.170:3128 | HK | 1258 | 5 | 5/5 |
| http://202.28.194.139:31280 | TH | 2771 | 5 | 31/33 |
| http://154.59.56.73:999 | VE | 2995 | 5 | 5/5 |
| http://14.251.13.20:8080 | VN | 1210 | 5 | 5/5 |
| socks4://112.28.149.152:8443 | CN | 1673 | 5 | 16/33 |
| socks4://45.61.129.165:9050 | US | 2314 | 5 | 25/33 |
| socks5://101.36.104.46:10808 | JP | 1275 | 5 | 30/33 |
| socks5://43.164.3.124:1080 | TH | 3339 | 5 | 22/32 |
| socks5://185.118.143.141:1080 | TR | 7424 | 5 | 5/5 |
| http://87.251.77.29:3128 | DE | 1027 | 4 | 30/33 |
| http://152.53.136.178:10000 | DE | 2005 | 4 | 5/8 |
| http://153.80.240.37:8080 | NL | 1047 | 4 | 22/33 |
| http://95.190.193.74:3128 | RU | 1320 | 4 | 4/4 |
| http://103.218.122.183:8080 | VN | 1264 | 4 | 4/4 |
| socks5://213.136.92.91:1080 | FR | 4110 | 4 | 22/33 |
| socks5://45.194.33.12:30001 | HK | 4735 | 4 | 22/29 |
| socks5://45.194.33.12:30002 | HK | 1664 | 4 | 6/7 |
| socks5://163.53.204.178:9813 | IN | 4972 | 4 | 9/32 |
| http://103.177.118.145:8118 | BD | 1484 | 3 | 13/14 |
| http://186.216.208.98:3128 | BR | 3465 | 3 | 9/31 |
| http://114.236.137.41:21000 | CN | 1650 | 3 | 21/33 |
| http://38.44.17.142:999 | DO | 5277 | 3 | 14/26 |
| http://205.235.1.38:999 | EC | 1575 | 3 | 8/19 |
| http://13.38.27.183:9824 | FR | 2981 | 3 | 10/29 |
| http://81.19.210.10:80 | GB | 869 | 3 | 3/3 |
| http://103.134.245.127:8090 | ID | 2924 | 3 | 4/14 |
| http://163.223.116.209:8080 | ID | 6392 | 3 | 7/29 |
| http://18.60.247.31:16583 | IN | 3381 | 3 | 4/10 |
| http://43.206.240.252:32840 | JP | 2335 | 3 | 8/17 |
| http://94.131.92.155:3128 | KZ | 1230 | 3 | 20/31 |
| http://38.194.246.34:999 | MX | 2942 | 3 | 14/24 |
| http://175.143.76.177:8181 | MY | 7321 | 3 | 23/33 |
| http://115.147.58.42:5050 | PH | 5440 | 3 | 6/12 |
| http://181.94.197.37:8080 | PY | 1217 | 3 | 13/28 |
| http://43.98.172.166:3128 | SG | 2037 | 3 | 3/3 |
| http://43.134.141.85:80 | SG | 962 | 3 | 12/31 |
| http://43.156.236.238:80 | SG | 958 | 3 | 14/31 |
| http://43.160.242.118:3128 | SG | 4263 | 3 | 24/30 |
| http://43.208.237.116:33672 | TH | 2528 | 3 | 5/12 |
| http://165.99.14.18:2222 | VN | 2967 | 3 | 3/3 |
| http://165.99.14.18:2765 | VN | 6641 | 3 | 5/10 |
| http://165.99.14.18:5432 | VN | 4132 | 3 | 10/28 |
| http://165.99.14.18:5566 | VN | 7210 | 3 | 8/12 |
| http://210.211.113.33:80 | VN | 3201 | 3 | 3/3 |
| socks5://51.222.104.72:1080 | CA | 3873 | 3 | 14/33 |
| socks5://5.45.119.70:1080 | EE | 2031 | 3 | 13/31 |
| socks5://194.163.174.78:1081 | FR | 2590 | 3 | 5/19 |
| socks5://185.118.143.190:1080 | TR | 5497 | 3 | 4/6 |
| socks5://36.50.177.175:1080 | VN | 2609 | 3 | 9/32 |
| http://181.14.210.237:8080 | AR | 3600 | 2 | 7/31 |
| http://103.72.198.132:55 | BD | 3096 | 2 | 8/32 |
| http://203.112.75.210:1111 | BD | 4542 | 2 | 2/2 |
| http://179.43.10.233:8874 | BR | 5076 | 2 | 6/25 |
| http://47.103.30.64:8080 | CN | 1659 | 2 | 6/27 |
| http://119.188.131.55:17981 | CN | 2175 | 2 | 13/33 |
| http://120.26.171.55:25125 | CN | 1450 | 2 | 9/31 |
| http://219.142.66.245:9090 | CN | 4141 | 2 | 6/8 |
| http://38.19.40.9:8083 | CO | 1708 | 2 | 9/25 |
| http://38.75.82.220:999 | DO | 4693 | 2 | 7/14 |
| http://45.229.17.113:999 | EC | 5904 | 2 | 2/2 |
| http://45.236.107.106:808 | EC | 7791 | 2 | 5/32 |
| http://186.33.45.218:999 | EC | 6435 | 2 | 13/22 |
| http://186.33.45.220:999 | EC | 5996 | 2 | 2/2 |
| http://205.235.1.34:999 | EC | 4886 | 2 | 5/10 |
| http://41.128.72.196:1976 | EG | 1208 | 2 | 2/2 |
| http://197.164.101.14:1976 | EG | 3003 | 2 | 4/5 |
| http://2.26.68.16:80 | FI | 3452 | 2 | 4/10 |
