# Proxy status

Generated 2026-09-02T17:08:55Z by `harvest.py`.

- **1203** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1881** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15635** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 196/600 (33%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1586 |
| socks5 | 280 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 378 |
| US | 148 |
| CN | 77 |
| CO | 67 |
| MX | 66 |
| RU | 58 |
| DE | 57 |
| BD | 56 |
| NL | 53 |
| PH | 52 |
| FR | 45 |
| VE | 45 |
| BR | 41 |
| TH | 40 |
| SG | 39 |
| EC | 36 |
| IN | 33 |
| AU | 32 |
| CA | 29 |
| HK | 27 |
| JP | 27 |
| VN | 27 |
| GB | 25 |
| ZA | 24 |
| KR | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-09-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 88 | 88 | 12 | 2026-09-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 93 | 93 | 44 | 2026-09-02 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-02 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 117 | 117 | 26 | 2026-09-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 118 | 118 | 45 | 2026-09-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 126 | 126 | 56 | 2026-09-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-09-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 182 | 182 | 37 | 2026-09-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 262 | 262 | 115 | 2026-09-02 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-09-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 637 | 637 | 343 | 2026-09-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1144 | 2026-09-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-09-02 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 1939 | 1939 | 1512 | 2026-09-02 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2017 | 2013 | 336 | 2026-09-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2303 | 2301 | 171 | 2026-09-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2833 | 2831 | 705 | 2026-09-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3051 | 3049 | 2276 | 2026-09-02 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 888 | 38 | 43/46 |
| http://34.43.46.91:80 | US | 902 | 38 | 43/46 |
| http://95.211.174.135:3128 | NL | 1312 | 32 | 45/46 |
| http://204.76.203.9:3128 | NL | 1362 | 32 | 45/46 |
| http://204.76.203.9:8080 | NL | 537 | 32 | 38/39 |
| http://185.200.188.234:10001 | RU | 1186 | 32 | 45/46 |
| http://130.110.103.245:3128 | SA | 1449 | 32 | 44/46 |
| http://199.7.149.96:3128 | US | 26 | 25 | 25/25 |
| http://45.186.6.104:3128 | EC | 650 | 24 | 24/24 |
| http://64.112.184.210:3128 | US | 254 | 24 | 45/46 |
| http://103.211.103.170:3128 | HK | 3257 | 18 | 18/18 |
| http://202.28.194.139:31280 | TH | 2046 | 18 | 44/46 |
| http://87.251.77.29:3128 | DE | 913 | 17 | 43/46 |
| http://68.178.174.239:3128 | US | 1170 | 14 | 14/14 |
| http://68.178.174.239:8888 | US | 1170 | 14 | 14/14 |
| http://184.75.221.82:3118 | CA | 138 | 11 | 11/11 |
| http://190.0.246.213:4040 | CO | 1702 | 11 | 11/11 |
| http://1.231.81.166:3128 | KR | 1518 | 11 | 43/46 |
| http://189.51.168.164:999 | MX | 364 | 11 | 11/11 |
| socks5://47.250.211.53:1080 | MY | 2068 | 11 | 27/46 |
| socks5://193.25.215.182:22222 | US | 1238 | 9 | 42/46 |
| http://3.211.120.181:443 | US | 85 | 8 | 8/8 |
| http://18.157.123.132:3128 | DE | 528 | 7 | 7/7 |
| http://116.202.172.187:11000 | DE | 587 | 7 | 7/7 |
| http://91.134.141.4:3128 | FR | 490 | 7 | 7/7 |
| http://173.212.240.48:8888 | FR | 674 | 7 | 7/7 |
| http://5.129.254.129:8888 | RU | 1049 | 7 | 7/7 |
| http://103.10.231.189:8080 | TH | 1580 | 7 | 20/31 |
| socks5://95.81.103.220:1080 | NL | 690 | 7 | 7/7 |
| socks5://171.25.158.95:1080 | SE | 6441 | 7 | 23/45 |
| http://176.111.37.5:39811 | HK | 1117 | 6 | 40/46 |
| http://16.79.110.168:3128 | ID | 3546 | 6 | 6/6 |
| http://108.136.182.225:8070 | ID | 2747 | 6 | 6/6 |
| http://47.81.56.193:8888 | TH | 1861 | 6 | 28/46 |
| http://14.251.13.20:8080 | VN | 1438 | 6 | 17/18 |
| socks5://78.159.131.108:1082 | AL | 1665 | 6 | 17/45 |
| http://40.177.104.199:48086 | CA | 3433 | 5 | 8/13 |
| http://39.106.170.168:8080 | CN | 2064 | 5 | 16/44 |
| http://34.88.38.81:9443 | FI | 614 | 5 | 6/11 |
| http://47.129.239.222:54001 | SG | 2754 | 5 | 6/10 |
| socks5://45.61.188.134:44499 | US | 1607 | 5 | 8/13 |
| http://16.50.56.246:18379 | AU | 2563 | 4 | 4/4 |
| http://16.50.56.246:9991 | AU | 2610 | 4 | 4/4 |
| http://16.174.6.134:3128 | CA | 2344 | 4 | 4/4 |
| http://35.159.62.164:37226 | DE | 1611 | 4 | 4/4 |
| http://63.179.134.206:56179 | DE | 3040 | 4 | 13/46 |
| http://103.237.102.191:11111 | DE | 1245 | 4 | 44/46 |
| http://13.36.211.95:44085 | FR | 1407 | 4 | 5/6 |
| http://15.237.108.20:8072 | FR | 766 | 4 | 5/6 |
| http://37.59.125.131:8888 | FR | 1144 | 4 | 33/46 |
| http://35.176.250.70:5566 | GB | 3737 | 4 | 4/4 |
| http://103.176.97.57:8082 | ID | 5578 | 4 | 16/35 |
| http://168.144.84.188:3129 | IN | 1287 | 4 | 4/4 |
| http://212.154.169.90:3128 | KZ | 1152 | 4 | 20/25 |
| http://3.92.47.79:10801 | US | 2837 | 4 | 5/6 |
| http://154.59.56.73:999 | VE | 3045 | 4 | 15/18 |
| http://190.97.241.106:999 | VE | 691 | 4 | 8/30 |
| socks5://101.36.104.46:10808 | JP | 1960 | 4 | 42/46 |
| socks5://5.255.117.250:1080 | NL | 592 | 4 | 10/31 |
| socks5://67.210.146.50:11080 | US | 4554 | 4 | 12/42 |
| http://40.176.175.23:26204 | CA | 1614 | 3 | 10/32 |
| http://40.177.104.199:22203 | CA | 1706 | 3 | 5/6 |
| http://8.138.217.152:21001 | CN | 3864 | 3 | 32/46 |
| http://120.26.171.55:25125 | CN | 1854 | 3 | 17/44 |
| http://120.232.115.170:17981 | CN | 1946 | 3 | 28/45 |
| http://181.78.10.110:999 | CO | 2754 | 3 | 15/42 |
| http://181.78.23.187:999 | CO | 665 | 3 | 13/15 |
| http://181.78.74.252:999 | CO | 715 | 3 | 35/37 |
| http://181.78.74.253:999 | CO | 700 | 3 | 35/37 |
| http://164.92.182.55:8080 | DE | 1745 | 3 | 4/5 |
| http://177.234.217.235:999 | EC | 5688 | 3 | 9/15 |
| http://196.204.3.21:1981 | EG | 1075 | 3 | 5/25 |
| http://15.232.45.244:3127 | ID | 2476 | 3 | 5/6 |
| http://51.84.101.19:80 | IL | 4635 | 3 | 11/38 |
| http://117.236.124.166:3128 | IN | 1746 | 3 | 28/46 |
| http://175.143.76.177:8181 | MY | 2780 | 3 | 34/46 |
| http://111.119.162.248:10916 | PK | 5392 | 3 | 5/30 |
| http://185.238.238.93:58080 | PL | 5964 | 3 | 12/42 |
| http://13.51.44.23:9103 | SE | 986 | 3 | 4/5 |
| http://35.94.193.222:5001 | US | 2847 | 3 | 8/11 |
| http://154.59.56.76:999 | VE | 2963 | 3 | 4/6 |
| http://190.97.236.128:999 | VE | 597 | 3 | 34/36 |
| http://190.97.236.129:999 | VE | 591 | 3 | 34/36 |
| http://190.97.238.14:999 | VE | 4620 | 3 | 10/15 |
| http://200.59.191.27:999 | VE | 3437 | 3 | 24/41 |
| http://210.211.113.36:80 | VN | 5252 | 3 | 11/17 |
| socks5://49.13.22.249:10801 | DE | 1139 | 3 | 8/15 |
| socks5://43.164.136.189:1080 | KR | 1259 | 3 | 25/46 |
| socks5://5.255.123.162:1080 | NL | 5716 | 3 | 9/29 |
| socks5://93.87.38.20:1090 | RS | 807 | 3 | 3/3 |
| socks5://165.22.243.171:1080 | SG | 1457 | 3 | 3/3 |
| http://15.220.121.140:3128 | AR | 768 | 2 | 2/2 |
| http://3.26.152.74:12708 | AU | 2829 | 2 | 2/2 |
| http://3.26.152.74:50741 | AU | 4604 | 2 | 3/4 |
| http://13.239.253.213:3128 | AU | 3144 | 2 | 3/11 |
| http://13.239.253.213:52317 | AU | 3469 | 2 | 3/6 |
| http://15.135.238.248:18057 | AU | 3509 | 2 | 3/4 |
| http://16.26.154.68:53546 | AU | 3086 | 2 | 15/42 |
| http://16.50.48.241:59412 | AU | 3551 | 2 | 2/2 |
| http://52.62.103.7:22986 | AU | 2797 | 2 | 4/10 |
