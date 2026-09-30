# Proxy status

Generated 2026-09-30T23:11:38Z by `harvest.py`.

- **3290** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5193** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39719** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 187/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2599 |
| http | 2591 |
| socks4 | 3 |

| country | entries |
|---|---|
| NL | 2415 |
| ID | 707 |
| ?? | 324 |
| US | 134 |
| CN | 106 |
| PH | 105 |
| MX | 85 |
| RU | 78 |
| CO | 77 |
| IN | 76 |
| BR | 61 |
| VE | 61 |
| EC | 58 |
| BD | 56 |
| DE | 53 |
| TR | 47 |
| SG | 43 |
| AR | 41 |
| VN | 39 |
| FR | 32 |
| DO | 31 |
| CA | 29 |
| JP | 28 |
| TH | 28 |
| HK | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 3 | 3 | 1 | 2026-09-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 122 | 122 | 66 | 2026-09-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 57 | 2026-09-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 88 | 2026-09-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 331 | 331 | 89 | 2026-09-30 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 442 | 442 | 197 | 2026-09-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 533 | 533 | 208 | 2026-09-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-09-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 669 | 669 | 291 | 2026-09-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1182 | 1182 | 213 | 2026-09-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-09-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-09-30 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1985 | 1985 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2818 | 2818 | 719 | 2026-09-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3340 | 3340 | 2124 | 2026-09-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3670 | 3670 | 789 | 2026-09-30 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 33465 | 33465 | 18519 | 2026-09-30 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 41300 | 41300 | 2529 | 2026-09-30 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1084 | 89 | 102/103 |
| http://95.3.69.222:8080 | TR | 1811 | 58 | 100/103 |
| http://190.0.246.213:4040 | CO | 634 | 32 | 61/68 |
| http://213.111.146.36:18080 | NL | 642 | 32 | 35/40 |
| http://190.0.246.211:4040 | CO | 1162 | 23 | 90/103 |
| http://34.43.46.91:80 | US | 620 | 20 | 99/103 |
| http://190.0.246.210:4040 | CO | 928 | 19 | 91/102 |
| http://103.237.102.191:11111 | DE | 963 | 19 | 97/103 |
| http://18.157.123.132:3128 | DE | 737 | 18 | 50/64 |
| socks5://144.91.121.61:1088 | FR | 1873 | 17 | 89/103 |
| http://34.43.46.91:443 | US | 622 | 16 | 97/103 |
| http://149.130.173.58:9443 | CO | 494 | 14 | 14/14 |
| http://43.173.120.13:8899 | US | 172 | 14 | 14/14 |
| http://185.195.71.218:18080 | CH | 1129 | 11 | 31/40 |
| http://103.119.19.218:3128 | CZ | 748 | 11 | 15/16 |
| http://186.5.94.206:999 | EC | 1319 | 11 | 62/65 |
| http://37.59.125.131:8888 | FR | 1365 | 11 | 82/103 |
| http://107.150.41.226:18080 | US | 354 | 11 | 39/40 |
| http://172.236.242.244:3128 | US | 263 | 11 | 11/11 |
| socks5://154.201.71.12:2080 | HK | 1266 | 10 | 11/12 |
| http://197.224.185.3:3128 | MU | 4630 | 9 | 65/71 |
| http://184.75.221.82:3118 | CA | 316 | 8 | 60/68 |
| http://144.76.61.252:3128 | DE | 5888 | 8 | 14/16 |
| http://45.186.6.104:3128 | EC | 785 | 8 | 76/81 |
| socks5://5.75.133.113:10801 | DE | 1250 | 8 | 41/69 |
| http://185.191.239.248:3128 | CH | 2792 | 7 | 73/102 |
| http://123.121.122.28:8888 | CN | 1255 | 7 | 32/52 |
| http://123.121.208.55:8888 | CN | 3626 | 7 | 22/56 |
| http://153.51.241.50:999 | MX | 1766 | 7 | 54/100 |
| http://49.229.100.235:8080 | TH | 1334 | 7 | 27/51 |
| socks5://101.36.104.239:10808 | JP | 2110 | 7 | 86/103 |
| http://129.212.171.38:3128 | DE | 2045 | 6 | 6/6 |
| http://134.199.191.115:3128 | DE | 5518 | 6 | 14/15 |
| http://34.88.38.81:9443 | FI | 952 | 6 | 46/68 |
| http://35.228.49.168:9443 | FI | 813 | 6 | 27/40 |
| http://43.155.62.157:443 | HK | 888 | 6 | 6/6 |
| http://176.111.37.216:39811 | HK | 1397 | 6 | 84/103 |
| http://136.114.233.244:3128 | US | 871 | 6 | 7/8 |
| http://195.158.8.123:3128 | UZ | 2106 | 6 | 67/101 |
| http://190.97.229.118:999 | VE | 7291 | 6 | 50/93 |
| http://190.97.241.106:999 | VE | 3791 | 6 | 59/87 |
| socks5://109.123.251.109:1080 | FR | 1869 | 6 | 58/103 |
| http://114.252.15.106:8888 | CN | 1266 | 5 | 32/56 |
| http://123.119.179.34:8888 | CN | 1246 | 5 | 25/65 |
| http://123.121.208.63:8888 | CN | 1243 | 5 | 25/49 |
| http://222.128.172.158:8888 | CN | 6352 | 5 | 31/68 |
| http://45.71.186.213:999 | EC | 3170 | 5 | 32/87 |
| http://103.113.26.7:8080 | ID | 6614 | 5 | 7/16 |
| http://185.238.236.226:58080 | PL | 1135 | 5 | 12/25 |
| http://56.228.13.15:443 | SE | 1294 | 5 | 11/17 |
| http://47.81.56.193:8888 | TH | 2338 | 5 | 63/103 |
| http://38.172.160.16:999 | VE | 808 | 5 | 32/54 |
| socks5://144.91.111.48:1088 | FR | 1899 | 5 | 66/103 |
| socks5://45.74.31.47:4769 | NL | 6686 | 5 | 5/5 |
| socks5://45.74.31.50:4726 | NL | 3820 | 5 | 5/5 |
| socks5://45.74.31.50:5349 | NL | 1846 | 5 | 5/5 |
| socks5://45.61.129.165:9050 | US | 1879 | 5 | 83/103 |
| socks5://67.207.92.87:1088 | US | 668 | 5 | 57/102 |
| socks5://129.153.11.56:1080 | US | 313 | 5 | 7/8 |
| socks5://160.187.0.89:1080 | VN | 1444 | 5 | 12/16 |
| http://123.115.226.82:8888 | CN | 1231 | 4 | 18/49 |
| http://123.121.121.123:8888 | CN | 1288 | 4 | 34/68 |
| http://123.121.211.160:8888 | CN | 1254 | 4 | 26/49 |
| http://67.207.72.60:3128 | DE | 2552 | 4 | 13/18 |
| http://154.236.179.229:1981 | EG | 2567 | 4 | 11/21 |
| http://213.131.85.28:1981 | EG | 1096 | 4 | 4/4 |
| http://37.59.138.176:8080 | ES | 4550 | 4 | 11/45 |
| http://103.156.16.241:8081 | ID | 4400 | 4 | 10/23 |
| http://103.169.130.130:8080 | ID | 1466 | 4 | 6/16 |
| http://144.79.241.254:3128 | ID | 3340 | 4 | 4/4 |
| http://175.111.96.154:3128 | ID | 1915 | 4 | 7/16 |
| http://203.175.103.169:8080 | ID | 4436 | 4 | 6/16 |
| http://35.78.212.217:32053 | JP | 4978 | 4 | 24/85 |
| http://38.56.111.104:999 | PE | 1957 | 4 | 4/4 |
| http://203.177.217.222:8082 | PH | 5450 | 4 | 25/48 |
| http://185.238.238.169:58080 | PL | 1652 | 4 | 13/25 |
| http://5.129.254.5:8888 | RU | 1264 | 4 | 49/58 |
| http://5.129.254.49:8888 | RU | 1285 | 4 | 50/58 |
| http://5.129.254.51:8888 | RU | 1302 | 4 | 50/58 |
| http://5.129.254.60:8888 | RU | 1180 | 4 | 49/57 |
| http://5.129.254.70:8888 | RU | 1192 | 4 | 50/58 |
| http://5.129.254.129:8888 | RU | 1220 | 4 | 55/64 |
| http://5.129.254.154:8888 | RU | 1200 | 4 | 46/54 |
| http://195.19.217.200:3128 | RU | 3685 | 4 | 19/29 |
| http://104.248.151.93:9090 | SG | 962 | 4 | 4/4 |
| http://128.199.116.219:9090 | SG | 1793 | 4 | 18/22 |
| http://167.99.74.174:9090 | SG | 963 | 4 | 40/63 |
| http://201.4.69.164:8080 | SY | 1276 | 4 | 7/16 |
| http://13.59.172.95:3128 | US | 389 | 4 | 4/4 |
| http://172.210.12.8:3128 | US | 307 | 4 | 17/39 |
| http://154.59.56.78:999 | VE | 3011 | 4 | 39/59 |
| http://210.211.113.34:80 | VN | 4562 | 4 | 52/75 |
| socks5://45.155.71.236:1080 | AT | 3389 | 4 | 6/8 |
| socks5://45.74.31.47:5222 | NL | 7727 | 4 | 4/4 |
| socks5://45.74.31.47:6738 | NL | 4954 | 4 | 9/30 |
| socks5://45.74.31.50:5623 | NL | 5146 | 4 | 4/4 |
| socks5://78.85.193.226:1080 | RU | 6978 | 4 | 4/4 |
| http://168.194.34.196:9001 | AR | 1673 | 3 | 33/101 |
| http://54.206.129.120:40000 | AU | 3098 | 3 | 15/63 |
| http://15.229.149.81:1080 | BR | 2035 | 3 | 4/5 |
