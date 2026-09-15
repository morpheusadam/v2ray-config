# Proxy status

Generated 2026-09-15T22:25:52Z by `harvest.py`.

- **859** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1448** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **22151** endpoints on record
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
| http | 862 |
| socks5 | 571 |
| socks4 | 15 |

| country | entries |
|---|---|
| NL | 393 |
| ID | 172 |
| CN | 89 |
| US | 74 |
| RU | 62 |
| VN | 58 |
| CO | 42 |
| BD | 39 |
| DE | 38 |
| MX | 37 |
| SG | 35 |
| FR | 28 |
| BR | 26 |
| EG | 26 |
| VE | 26 |
| EC | 25 |
| PH | 21 |
| IN | 20 |
| FI | 17 |
| HK | 15 |
| KH | 13 |
| AR | 12 |
| ZA | 11 |
| CL | 10 |
| JP | 10 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-09-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 65 | 65 | 32 | 2026-09-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 113 | 113 | 39 | 2026-09-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 136 | 136 | 60 | 2026-09-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-09-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 221 | 221 | 90 | 2026-09-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 356 | 356 | 113 | 2026-09-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 366 | 366 | 149 | 2026-09-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 389 | 389 | 48 | 2026-09-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-09-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-09-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1937 | 1933 | 383 | 2026-09-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2721 | 2719 | 2079 | 2026-09-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2785 | 2783 | 714 | 2026-09-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3016 | 3014 | 623 | 2026-09-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 6508 | 6508 | 4040 | 2026-09-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12529 | 12528 | 2167 | 2026-09-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 557 | 65 | 70/73 |
| http://34.43.46.91:80 | US | 1070 | 65 | 70/73 |
| http://95.211.174.135:3128 | NL | 1348 | 59 | 72/73 |
| http://185.200.188.234:10001 | RU | 1246 | 59 | 72/73 |
| http://130.110.103.245:3128 | SA | 1336 | 59 | 71/73 |
| http://1.231.81.166:3128 | KR | 1672 | 38 | 70/73 |
| http://176.111.37.5:39811 | HK | 1170 | 33 | 67/73 |
| http://181.78.23.187:999 | CO | 617 | 30 | 40/42 |
| http://181.78.74.252:999 | CO | 679 | 30 | 62/64 |
| http://181.78.74.253:999 | CO | 682 | 30 | 62/64 |
| http://190.97.236.128:999 | VE | 1795 | 30 | 61/63 |
| http://190.97.236.129:999 | VE | 672 | 30 | 61/63 |
| http://95.3.69.222:8080 | TR | 1585 | 28 | 70/73 |
| http://190.97.241.106:999 | VE | 1628 | 25 | 34/57 |
| http://107.167.18.122:443 | US | 2397 | 18 | 24/25 |
| http://103.237.102.191:11111 | DE | 1140 | 17 | 69/73 |
| socks5://83.147.216.208:1080 | FI | 1164 | 17 | 23/41 |
| socks5://144.91.111.48:1088 | FR | 4454 | 15 | 43/73 |
| http://184.75.221.82:3118 | CA | 199 | 14 | 35/38 |
| socks5://144.91.121.61:1088 | FR | 4147 | 14 | 64/73 |
| http://91.134.141.4:3128 | FR | 495 | 12 | 32/34 |
| http://186.5.94.206:999 | EC | 813 | 10 | 33/35 |
| http://107.150.41.226:18080 | US | 286 | 10 | 10/10 |
| http://14.251.13.20:8080 | VN | 1432 | 10 | 43/45 |
| socks5://213.199.47.140:1080 | FR | 1792 | 10 | 32/39 |
| http://195.158.8.123:3128 | UZ | 1460 | 8 | 49/71 |
| http://8.138.217.152:21001 | CN | 4196 | 7 | 49/73 |
| http://103.177.118.145:8118 | BD | 1579 | 6 | 50/54 |
| http://190.0.246.210:4040 | CO | 2258 | 6 | 63/72 |
| http://186.33.45.219:999 | EC | 2694 | 6 | 36/62 |
| http://65.109.217.164:3128 | FI | 625 | 6 | 6/6 |
| http://84.8.216.230:2001 | MA | 7103 | 6 | 6/6 |
| http://43.156.199.63:8080 | SG | 3354 | 6 | 7/8 |
| http://202.28.194.139:31280 | TH | 1996 | 6 | 66/73 |
| http://38.51.207.104:8080 | VE | 3646 | 6 | 13/14 |
| http://210.211.113.34:80 | VN | 1486 | 6 | 38/45 |
| http://172.104.56.95:8888 | SG | 2317 | 5 | 5/5 |
| socks4://58.187.104.62:1083 | VN | 4016 | 5 | 5/5 |
| socks4://58.187.104.62:1111 | VN | 5353 | 5 | 5/5 |
| socks4://58.187.104.62:1117 | VN | 3710 | 5 | 5/5 |
| socks5://109.123.251.109:1080 | FR | 4110 | 5 | 36/73 |
| socks5://45.74.31.42:12636 | NL | 6891 | 5 | 5/5 |
| socks5://161.35.90.93:1082 | NL | 2318 | 5 | 37/73 |
| socks5://103.162.30.189:10808 | VN | 3504 | 5 | 7/8 |
| socks5://160.22.17.4:9988 | VN | 1763 | 5 | 30/69 |
| http://185.191.239.248:3128 | CH | 1810 | 4 | 55/72 |
| http://61.149.134.158:8888 | CN | 1567 | 4 | 15/38 |
| http://123.121.122.28:8888 | CN | 2535 | 4 | 16/22 |
| http://190.12.150.244:999 | EC | 1818 | 4 | 44/69 |
| http://34.88.38.81:9443 | FI | 626 | 4 | 25/38 |
| http://35.228.49.168:9443 | FI | 612 | 4 | 6/10 |
| http://176.111.37.216:39811 | HK | 1173 | 4 | 60/73 |
| http://197.224.185.3:3128 | MU | 1745 | 4 | 37/41 |
| http://189.51.168.164:999 | MX | 354 | 4 | 37/38 |
| http://45.132.252.25:49156 | RU | 818 | 4 | 4/4 |
| http://43.153.123.79:80 | US | 2719 | 4 | 4/4 |
| http://38.172.160.16:999 | VE | 5258 | 4 | 15/24 |
| http://58.187.104.62:2088 | VN | 2665 | 4 | 4/4 |
| http://210.211.113.37:80 | VN | 3458 | 4 | 29/45 |
| socks4://58.187.104.62:1085 | VN | 2764 | 4 | 4/4 |
| socks5://49.13.22.249:10801 | DE | 1966 | 4 | 27/42 |
| socks5://161.35.90.93:1081 | NL | 2524 | 4 | 35/73 |
| http://108.61.213.218:80 | AU | 1000 | 3 | 11/14 |
| http://36.155.23.163:10808 | CN | 1851 | 3 | 5/10 |
| http://39.106.165.196:8080 | CN | 4490 | 3 | 36/69 |
| http://113.45.195.147:3128 | CN | 1897 | 3 | 25/38 |
| http://114.244.223.68:8888 | CN | 2201 | 3 | 22/36 |
| http://115.231.181.40:8128 | CN | 1974 | 3 | 31/72 |
| http://218.93.176.70:2088 | CN | 6169 | 3 | 7/19 |
| http://200.10.31.45:8081 | CO | 3599 | 3 | 29/70 |
| http://177.234.217.237:999 | EC | 2286 | 3 | 17/46 |
| http://41.128.90.53:1976 | EG | 1671 | 3 | 3/3 |
| http://103.155.198.138:3125 | ID | 7184 | 3 | 15/63 |
| http://38.194.246.34:999 | MX | 4960 | 3 | 37/64 |
| http://187.190.58.152:80 | MX | 3369 | 3 | 25/71 |
| http://205.164.192.115:999 | MX | 3660 | 3 | 44/71 |
| http://153.80.240.2:1080 | NL | 535 | 3 | 3/3 |
| http://153.80.240.2:8080 | NL | 514 | 3 | 5/7 |
| http://5.129.254.5:8888 | RU | 1047 | 3 | 26/28 |
| http://5.129.254.49:8888 | RU | 1110 | 3 | 27/28 |
| http://5.129.254.51:8888 | RU | 1032 | 3 | 27/28 |
| http://5.129.254.60:8888 | RU | 1086 | 3 | 26/27 |
| http://5.129.254.70:8888 | RU | 1155 | 3 | 27/28 |
| http://5.129.254.129:8888 | RU | 1053 | 3 | 32/34 |
| http://5.129.254.154:8888 | RU | 1019 | 3 | 23/24 |
| http://43.128.76.140:8081 | SG | 6336 | 3 | 3/3 |
| http://47.84.84.1:3128 | SG | 1893 | 3 | 26/73 |
| http://5.161.50.82:8118 | US | 5731 | 3 | 18/72 |
| http://193.104.179.115:3128 | UZ | 1332 | 3 | 21/38 |
| http://154.59.56.74:999 | VE | 2852 | 3 | 24/36 |
| socks4://87.239.251.202:1081 | NL | 2813 | 3 | 23/71 |
| socks4://58.187.104.62:1062 | VN | 2464 | 3 | 3/3 |
| socks4://58.187.104.62:1089 | VN | 2495 | 3 | 4/5 |
| socks5://5.75.133.113:10808 | DE | 2307 | 3 | 24/46 |
| socks5://65.21.252.66:10811 | FI | 4245 | 3 | 30/61 |
| socks5://46.8.31.104:1080 | KZ | 3147 | 3 | 10/65 |
| socks5://45.74.31.40:10811 | NL | 6094 | 3 | 5/9 |
| socks5://45.74.31.42:11062 | NL | 7062 | 3 | 3/3 |
| socks5://45.74.31.42:15659 | NL | 2762 | 3 | 3/3 |
| socks5://57.128.231.218:1004 | PL | 1018 | 3 | 4/7 |
