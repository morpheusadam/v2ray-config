# Proxy status

Generated 2026-09-01T17:21:46Z by `harvest.py`.

- **499** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1792** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15354** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 130/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1478 |
| socks5 | 291 |
| socks4 | 23 |

| country | entries |
|---|---|
| ID | 370 |
| US | 139 |
| CN | 96 |
| MX | 74 |
| CO | 62 |
| BD | 59 |
| PH | 59 |
| DE | 55 |
| NL | 53 |
| BR | 47 |
| RU | 46 |
| FR | 40 |
| VE | 40 |
| SG | 36 |
| HK | 34 |
| IN | 34 |
| KR | 32 |
| VN | 30 |
| EC | 28 |
| AU | 26 |
| KH | 25 |
| JP | 24 |
| CA | 23 |
| TH | 22 |
| GB | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 2 | 2026-09-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 56 | 56 | 24 | 2026-09-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 62 | 62 | 19 | 2026-09-01 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 103 | 103 | 22 | 2026-09-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 134 | 134 | 71 | 2026-09-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 72 | 2026-09-01 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 168 | 168 | 40 | 2026-09-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 177 | 177 | 31 | 2026-09-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 284 | 284 | 112 | 2026-09-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 314 | 314 | 120 | 2026-09-01 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-09-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-09-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1605 | 2026-09-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1927 | 1925 | 165 | 2026-09-01 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1957 | 1953 | 639 | 2026-09-01 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2043 | 2043 | 1544 | 2026-09-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2418 | 2416 | 656 | 2026-09-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2702 | 2700 | 2061 | 2026-09-01 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 2153 | 41 | 43/44 |
| http://34.43.46.91:443 | US | 3085 | 36 | 41/44 |
| http://34.43.46.91:80 | US | 3314 | 36 | 41/44 |
| http://95.211.174.135:3128 | NL | 2455 | 30 | 43/44 |
| http://204.76.203.9:3128 | NL | 1616 | 30 | 43/44 |
| http://204.76.203.9:8080 | NL | 660 | 30 | 36/37 |
| http://185.200.188.234:10001 | RU | 2485 | 30 | 43/44 |
| http://130.110.103.245:3128 | SA | 3461 | 30 | 42/44 |
| http://199.7.149.96:3128 | US | 198 | 23 | 23/23 |
| http://45.186.6.104:3128 | EC | 972 | 22 | 22/22 |
| http://64.112.184.210:3128 | US | 2308 | 22 | 43/44 |
| http://103.211.103.170:3128 | HK | 4916 | 16 | 16/16 |
| http://202.28.194.139:31280 | TH | 3430 | 16 | 42/44 |
| socks4://45.61.129.165:9050 | US | 3627 | 16 | 36/44 |
| http://87.251.77.29:3128 | DE | 1063 | 15 | 41/44 |
| http://68.178.174.239:3128 | US | 1304 | 12 | 12/12 |
| http://68.178.174.239:8888 | US | 1292 | 12 | 12/12 |
| http://184.75.221.82:3118 | CA | 273 | 9 | 9/9 |
| http://190.0.246.213:4040 | CO | 5128 | 9 | 9/9 |
| http://194.163.175.167:40000 | FR | 5769 | 9 | 9/9 |
| http://1.231.81.166:3128 | KR | 2137 | 9 | 41/44 |
| http://189.51.168.164:999 | MX | 609 | 9 | 9/9 |
| http://43.160.242.118:3128 | SG | 5225 | 9 | 34/41 |
| socks5://47.250.211.53:1080 | MY | 3279 | 9 | 25/44 |
| socks5://85.209.156.148:1080 | US | 1859 | 8 | 12/15 |
| socks5://193.25.215.182:22222 | US | 1503 | 7 | 40/44 |
| http://3.211.120.181:443 | US | 297 | 6 | 6/6 |
| socks5://94.183.233.251:1080 | US | 5075 | 6 | 8/9 |
| http://18.157.123.132:3128 | DE | 1734 | 5 | 5/5 |
| http://116.202.172.187:11000 | DE | 1415 | 5 | 5/5 |
| http://91.134.141.4:3128 | FR | 621 | 5 | 5/5 |
| http://173.212.240.48:8888 | FR | 1250 | 5 | 5/5 |
| http://5.129.254.129:8888 | RU | 1119 | 5 | 5/5 |
| http://103.10.231.189:8080 | TH | 1671 | 5 | 18/29 |
| socks5://51.178.49.241:1088 | FR | 1342 | 5 | 5/5 |
| socks5://144.24.111.128:1088 | IN | 2878 | 5 | 34/44 |
| socks5://95.81.103.220:1080 | NL | 848 | 5 | 5/5 |
| socks5://171.25.158.95:1080 | SE | 2811 | 5 | 21/43 |
| http://16.26.180.163:8083 | AU | 3680 | 4 | 4/4 |
| http://16.26.208.68:18596 | AU | 3072 | 4 | 5/9 |
| http://16.50.48.241:23482 | AU | 3260 | 4 | 4/4 |
| http://16.174.83.123:3128 | CA | 2814 | 4 | 4/4 |
| http://40.176.90.140:3128 | CA | 2093 | 4 | 4/4 |
| http://40.177.99.164:31822 | CA | 4911 | 4 | 14/44 |
| http://114.254.50.97:8888 | CN | 2154 | 4 | 7/9 |
| http://122.246.3.12:17981 | CN | 1762 | 4 | 20/38 |
| http://139.159.97.82:10900 | CN | 4451 | 4 | 9/13 |
| http://190.0.246.210:4040 | CO | 7527 | 4 | 39/43 |
| http://3.122.224.70:38675 | DE | 984 | 4 | 4/4 |
| http://63.181.83.210:4358 | DE | 4045 | 4 | 10/30 |
| http://35.180.138.2:5050 | FR | 1879 | 4 | 4/4 |
| http://52.47.115.41:7898 | FR | 4663 | 4 | 6/11 |
| http://18.170.45.5:47098 | GB | 1017 | 4 | 4/4 |
| http://176.111.37.5:39811 | HK | 3354 | 4 | 38/44 |
| http://16.79.110.168:3128 | ID | 2647 | 4 | 4/4 |
| http://43.218.128.7:49180 | ID | 5879 | 4 | 4/4 |
| http://108.136.182.225:8070 | ID | 6341 | 4 | 4/4 |
| http://51.17.130.167:11938 | IL | 3188 | 4 | 5/8 |
| http://51.17.154.141:8009 | IL | 1844 | 4 | 12/30 |
| http://43.201.254.87:37803 | KR | 3407 | 4 | 4/4 |
| http://205.164.192.115:999 | MX | 2476 | 4 | 23/42 |
| http://43.216.195.95:3128 | MY | 3995 | 4 | 4/4 |
| http://51.20.254.126:24380 | SE | 4595 | 4 | 5/8 |
| http://43.156.114.4:80 | SG | 1026 | 4 | 22/40 |
| http://47.129.166.112:38352 | SG | 2439 | 4 | 4/4 |
| http://47.81.56.193:8888 | TH | 3291 | 4 | 26/44 |
| http://3.231.160.150:56404 | US | 1149 | 4 | 4/4 |
| http://44.200.234.67:17046 | US | 2115 | 4 | 4/4 |
| http://14.251.13.20:8080 | VN | 1224 | 4 | 15/16 |
| http://13.244.61.193:31142 | ZA | 3088 | 4 | 7/11 |
| socks4://194.31.108.109:2080 | IR | 7161 | 4 | 4/4 |
| socks5://78.159.131.108:1082 | AL | 4885 | 4 | 15/43 |
| http://186.216.208.98:3128 | BR | 7164 | 3 | 12/42 |
| http://40.177.104.199:48086 | CA | 5679 | 3 | 6/11 |
| http://39.106.170.168:8080 | CN | 1803 | 3 | 14/42 |
| http://114.246.196.30:8888 | CN | 6055 | 3 | 6/8 |
| http://122.246.3.210:17981 | CN | 4476 | 3 | 15/44 |
| http://221.221.162.189:8888 | CN | 3705 | 3 | 5/12 |
| http://3.127.27.51:29198 | DE | 2674 | 3 | 10/40 |
| http://186.33.45.218:999 | EC | 7900 | 3 | 20/33 |
| http://41.33.219.140:1981 | EG | 4198 | 3 | 8/26 |
| http://34.88.38.81:9443 | FI | 1096 | 3 | 4/9 |
| http://18.175.218.194:3128 | GB | 820 | 3 | 4/8 |
| http://15.232.152.216:5961 | ID | 3192 | 3 | 3/3 |
| http://43.218.233.2:8948 | ID | 2804 | 3 | 3/3 |
| http://51.17.209.199:4040 | IL | 1998 | 3 | 3/3 |
| http://45.43.60.220:8080 | JP | 5871 | 3 | 27/43 |
| http://56.68.116.64:47651 | MY | 2378 | 3 | 11/44 |
| http://20.61.126.88:3128 | NL | 6852 | 3 | 7/8 |
| http://47.129.239.222:54001 | SG | 2506 | 3 | 4/8 |
| http://54.255.249.161:3129 | SG | 5121 | 3 | 6/12 |
| http://18.208.158.27:37926 | US | 1201 | 3 | 3/3 |
| http://13.244.61.193:80 | ZA | 2420 | 3 | 7/11 |
| http://16.28.66.143:2020 | ZA | 6268 | 3 | 3/3 |
| socks5://163.47.37.190:1080 | BD | 2893 | 3 | 13/36 |
| socks5://185.214.101.27:1080 | ES | 1246 | 3 | 4/16 |
| socks5://65.21.252.66:10801 | FI | 5848 | 3 | 16/32 |
| socks5://65.21.252.66:10811 | FI | 2833 | 3 | 18/32 |
| socks5://103.174.122.197:8199 | ID | 2002 | 3 | 12/44 |
| socks5://110.235.246.62:1080 | KH | 7353 | 3 | 14/42 |
