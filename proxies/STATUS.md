# Proxy status

Generated 2026-09-01T22:00:06Z by `harvest.py`.

- **845** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1795** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15779** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 170/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1493 |
| socks5 | 282 |
| socks4 | 20 |

| country | entries |
|---|---|
| ID | 302 |
| US | 174 |
| CN | 77 |
| MX | 72 |
| DE | 58 |
| BD | 53 |
| CO | 50 |
| JP | 49 |
| IN | 48 |
| NL | 48 |
| RU | 46 |
| FR | 45 |
| SG | 43 |
| BR | 42 |
| PH | 41 |
| VE | 38 |
| AU | 37 |
| HK | 35 |
| CA | 34 |
| KR | 32 |
| TH | 28 |
| EC | 26 |
| VN | 26 |
| SE | 23 |
| GB | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 48 | 48 | 25 | 2026-09-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 65 | 65 | 20 | 2026-09-01 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 102 | 102 | 4 | 2026-09-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 115 | 115 | 28 | 2026-09-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 118 | 118 | 48 | 2026-09-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 125 | 125 | 43 | 2026-09-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-09-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 174 | 174 | 36 | 2026-09-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-01 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-09-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 769 | 769 | 528 | 2026-09-01 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1395 | 1391 | 356 | 2026-09-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-09-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1606 | 2026-09-01 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2266 | 2266 | 1722 | 2026-09-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2325 | 2323 | 185 | 2026-09-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2756 | 2754 | 669 | 2026-09-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2908 | 2906 | 2236 | 2026-09-01 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 600 | 37 | 42/45 |
| http://34.43.46.91:80 | US | 613 | 37 | 42/45 |
| http://95.211.174.135:3128 | NL | 1128 | 31 | 44/45 |
| http://204.76.203.9:3128 | NL | 2096 | 31 | 44/45 |
| http://204.76.203.9:8080 | NL | 1864 | 31 | 37/38 |
| http://185.200.188.234:10001 | RU | 2070 | 31 | 44/45 |
| http://130.110.103.245:3128 | SA | 2411 | 31 | 43/45 |
| http://199.7.149.96:3128 | US | 357 | 24 | 24/24 |
| http://45.186.6.104:3128 | EC | 851 | 23 | 23/23 |
| http://64.112.184.210:3128 | US | 774 | 23 | 44/45 |
| http://103.211.103.170:3128 | HK | 2680 | 17 | 17/17 |
| http://202.28.194.139:31280 | TH | 2604 | 17 | 43/45 |
| http://87.251.77.29:3128 | DE | 1110 | 16 | 42/45 |
| http://68.178.174.239:3128 | US | 1144 | 13 | 13/13 |
| http://68.178.174.239:8888 | US | 1146 | 13 | 13/13 |
| http://184.75.221.82:3118 | CA | 353 | 10 | 10/10 |
| http://190.0.246.213:4040 | CO | 1364 | 10 | 10/10 |
| http://1.231.81.166:3128 | KR | 1631 | 10 | 42/45 |
| http://189.51.168.164:999 | MX | 991 | 10 | 10/10 |
| socks5://47.250.211.53:1080 | MY | 1698 | 10 | 26/45 |
| socks5://85.209.156.148:1080 | US | 5313 | 9 | 13/16 |
| socks5://193.25.215.182:22222 | US | 628 | 8 | 41/45 |
| http://3.211.120.181:443 | US | 397 | 7 | 7/7 |
| http://18.157.123.132:3128 | DE | 815 | 6 | 6/6 |
| http://116.202.172.187:11000 | DE | 862 | 6 | 6/6 |
| http://91.134.141.4:3128 | FR | 1154 | 6 | 6/6 |
| http://173.212.240.48:8888 | FR | 3578 | 6 | 6/6 |
| http://5.129.254.129:8888 | RU | 5578 | 6 | 6/6 |
| http://103.10.231.189:8080 | TH | 1260 | 6 | 19/30 |
| socks5://51.178.49.241:1088 | FR | 945 | 6 | 6/6 |
| socks5://95.81.103.220:1080 | NL | 1065 | 6 | 6/6 |
| socks5://171.25.158.95:1080 | SE | 2750 | 6 | 22/44 |
| http://40.176.90.140:3128 | CA | 2379 | 5 | 5/5 |
| http://139.159.97.82:10900 | CN | 2508 | 5 | 10/14 |
| http://190.0.246.210:4040 | CO | 1816 | 5 | 40/44 |
| http://176.111.37.5:39811 | HK | 2345 | 5 | 39/45 |
| http://16.79.110.168:3128 | ID | 5591 | 5 | 5/5 |
| http://43.218.128.7:49180 | ID | 3205 | 5 | 5/5 |
| http://108.136.182.225:8070 | ID | 2414 | 5 | 5/5 |
| http://43.201.254.87:37803 | KR | 2634 | 5 | 5/5 |
| http://205.164.192.115:999 | MX | 3967 | 5 | 24/43 |
| http://43.216.195.95:3128 | MY | 3269 | 5 | 5/5 |
| http://47.81.56.193:8888 | TH | 1470 | 5 | 27/45 |
| http://44.200.234.67:17046 | US | 4271 | 5 | 5/5 |
| http://14.251.13.20:8080 | VN | 1169 | 5 | 16/17 |
| http://13.244.61.193:31142 | ZA | 4825 | 5 | 8/12 |
| socks4://194.31.108.109:2080 | IR | 4384 | 5 | 5/5 |
| socks5://78.159.131.108:1082 | AL | 3028 | 5 | 16/44 |
| http://40.177.104.199:48086 | CA | 1503 | 4 | 7/12 |
| http://39.106.170.168:8080 | CN | 1184 | 4 | 15/43 |
| http://3.127.27.51:29198 | DE | 5035 | 4 | 11/41 |
| http://186.33.45.218:999 | EC | 5530 | 4 | 21/34 |
| http://41.33.219.140:1981 | EG | 5416 | 4 | 9/27 |
| http://34.88.38.81:9443 | FI | 972 | 4 | 5/10 |
| http://18.175.218.194:3128 | GB | 4002 | 4 | 5/9 |
| http://51.17.209.199:4040 | IL | 2418 | 4 | 4/4 |
| http://20.61.126.88:3128 | NL | 1857 | 4 | 8/9 |
| http://47.129.239.222:54001 | SG | 3446 | 4 | 5/9 |
| http://16.28.66.143:2020 | ZA | 2404 | 4 | 4/4 |
| socks5://103.174.122.197:8199 | ID | 2615 | 4 | 13/45 |
| socks5://13.215.27.14:1080 | SG | 1061 | 4 | 20/37 |
| socks5://45.61.188.134:44499 | US | 1215 | 4 | 7/12 |
| http://16.26.99.200:46516 | AU | 3945 | 3 | 6/17 |
| http://16.50.56.246:18379 | AU | 2449 | 3 | 3/3 |
| http://16.50.56.246:9991 | AU | 2437 | 3 | 3/3 |
| http://16.174.6.134:3128 | CA | 4675 | 3 | 3/3 |
| http://40.176.84.249:40807 | CA | 4866 | 3 | 3/3 |
| http://115.231.181.40:8128 | CN | 4060 | 3 | 23/44 |
| http://219.142.66.245:9090 | CN | 1711 | 3 | 14/20 |
| http://190.0.246.211:4040 | CO | 3434 | 3 | 39/45 |
| http://18.157.159.247:9002 | DE | 2546 | 3 | 7/12 |
| http://35.159.62.164:37226 | DE | 1777 | 3 | 3/3 |
| http://63.179.134.206:56179 | DE | 2069 | 3 | 12/45 |
| http://103.237.102.191:11111 | DE | 1493 | 3 | 43/45 |
| http://13.36.211.95:44085 | FR | 4538 | 3 | 4/5 |
| http://15.188.238.238:59093 | FR | 2063 | 3 | 3/3 |
| http://15.237.108.20:8072 | FR | 923 | 3 | 4/5 |
| http://37.59.125.131:8888 | FR | 1913 | 3 | 32/45 |
| http://35.176.250.70:5566 | GB | 1120 | 3 | 3/3 |
| http://43.218.124.29:38951 | ID | 6294 | 3 | 4/9 |
| http://103.176.97.57:8082 | ID | 1536 | 3 | 15/34 |
| http://168.144.84.188:3129 | IN | 1485 | 3 | 3/3 |
| http://43.202.0.209:6808 | KR | 3246 | 3 | 5/9 |
| http://212.154.169.90:3128 | KZ | 1403 | 3 | 19/24 |
| http://43.217.201.189:10756 | MY | 3244 | 3 | 4/5 |
| http://194.87.35.27:8080 | NL | 1874 | 3 | 3/3 |
| http://13.212.157.123:8000 | SG | 2886 | 3 | 3/3 |
| http://3.92.47.79:10801 | US | 1365 | 3 | 4/5 |
| http://3.231.160.150:7089 | US | 2343 | 3 | 4/9 |
| http://154.59.56.73:999 | VE | 5765 | 3 | 14/17 |
| http://190.97.241.106:999 | VE | 3442 | 3 | 7/29 |
| http://15.240.165.254:8832 | ZA | 2554 | 3 | 4/5 |
| socks5://38.49.210.79:40000 | CA | 952 | 3 | 17/45 |
| socks5://103.142.255.33:69 | ID | 6637 | 3 | 13/38 |
| socks5://101.36.104.46:10808 | JP | 1486 | 3 | 41/45 |
| socks5://5.255.117.250:1080 | NL | 952 | 3 | 9/30 |
| socks5://89.189.132.154:1080 | RU | 2659 | 3 | 12/36 |
| socks5://67.210.146.50:11080 | US | 843 | 3 | 11/41 |
| http://16.51.148.102:8181 | AU | 5614 | 2 | 11/17 |
| http://113.11.120.105:30226 | BD | 3583 | 2 | 10/44 |
