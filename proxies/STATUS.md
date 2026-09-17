# Proxy status

Generated 2026-09-17T22:25:04Z by `harvest.py`.

- **1591** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2587** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25673** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 181/600 (30%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1608 |
| socks5 | 976 |
| socks4 | 3 |

| country | entries |
|---|---|
| NL | 772 |
| ID | 378 |
| US | 132 |
| CN | 117 |
| RU | 86 |
| MX | 69 |
| PH | 63 |
| DE | 57 |
| CO | 56 |
| SG | 52 |
| BD | 48 |
| IN | 48 |
| VE | 47 |
| FR | 40 |
| VN | 38 |
| BR | 36 |
| JP | 36 |
| EG | 34 |
| EC | 32 |
| TR | 27 |
| HK | 23 |
| DO | 21 |
| TH | 20 |
| FI | 19 |
| PK | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 1 | 2026-09-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 33 | 33 | 17 | 2026-09-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 87 | 87 | 41 | 2026-09-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 88 | 2026-09-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 177 | 177 | 42 | 2026-09-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 224 | 224 | 77 | 2026-09-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 262 | 262 | 109 | 2026-09-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 340 | 340 | 89 | 2026-09-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 377 | 377 | 178 | 2026-09-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-09-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-09-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1605 | 2026-09-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1862 | 1858 | 256 | 2026-09-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2384 | 2382 | 716 | 2026-09-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2558 | 2556 | 1838 | 2026-09-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2736 | 2734 | 646 | 2026-09-17 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 10522 | 10522 | 6322 | 2026-09-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 16729 | 16728 | 2447 | 2026-09-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1527 | 69 | 74/77 |
| http://34.43.46.91:80 | US | 1421 | 69 | 74/77 |
| http://95.211.174.135:3128 | NL | 1596 | 63 | 76/77 |
| http://185.200.188.234:10001 | RU | 2335 | 63 | 76/77 |
| http://130.110.103.245:3128 | SA | 1947 | 63 | 75/77 |
| http://1.231.81.166:3128 | KR | 1230 | 42 | 74/77 |
| http://190.97.236.128:999 | VE | 1712 | 34 | 65/67 |
| http://190.97.236.129:999 | VE | 656 | 34 | 65/67 |
| http://95.3.69.222:8080 | TR | 1999 | 32 | 74/77 |
| socks5://107.167.18.122:443 | US | 379 | 22 | 28/29 |
| socks5://83.147.216.208:1080 | FI | 863 | 21 | 27/45 |
| http://184.75.221.82:3118 | CA | 302 | 18 | 39/42 |
| http://91.134.141.4:3128 | FR | 490 | 16 | 36/38 |
| http://186.5.94.206:999 | EC | 798 | 14 | 37/39 |
| http://107.150.41.226:18080 | US | 266 | 14 | 14/14 |
| socks5://213.199.47.140:1080 | FR | 3082 | 14 | 36/43 |
| http://190.0.246.210:4040 | CO | 1149 | 10 | 67/76 |
| http://186.33.45.219:999 | EC | 3534 | 10 | 40/66 |
| http://43.156.199.63:8080 | SG | 4780 | 10 | 11/12 |
| http://38.51.207.104:8080 | VE | 1534 | 10 | 17/18 |
| socks5://103.162.30.189:10808 | VN | 5033 | 9 | 11/12 |
| http://34.88.38.81:9443 | FI | 628 | 8 | 29/42 |
| http://35.228.49.168:9443 | FI | 633 | 8 | 10/14 |
| http://197.224.185.3:3128 | MU | 1753 | 8 | 41/45 |
| http://189.51.168.164:999 | MX | 337 | 8 | 41/42 |
| http://45.132.252.25:49156 | RU | 844 | 8 | 8/8 |
| http://115.231.181.40:8128 | CN | 2357 | 7 | 35/76 |
| http://5.129.254.5:8888 | RU | 1033 | 7 | 30/32 |
| http://5.129.254.49:8888 | RU | 1231 | 7 | 31/32 |
| http://5.129.254.51:8888 | RU | 1104 | 7 | 31/32 |
| http://5.129.254.60:8888 | RU | 1054 | 7 | 30/31 |
| http://5.129.254.70:8888 | RU | 1100 | 7 | 31/32 |
| http://5.129.254.129:8888 | RU | 1040 | 7 | 36/38 |
| http://5.129.254.154:8888 | RU | 1530 | 7 | 27/28 |
| http://193.104.179.115:3128 | UZ | 1423 | 7 | 25/42 |
| socks5://57.128.231.218:1004 | PL | 882 | 7 | 8/11 |
| http://47.121.139.13:3128 | CN | 2292 | 6 | 37/76 |
| http://120.232.115.170:17981 | CN | 2047 | 6 | 55/76 |
| http://190.0.246.211:4040 | CO | 654 | 6 | 65/77 |
| http://190.0.246.213:4040 | CO | 457 | 6 | 35/42 |
| http://213.111.146.36:18080 | NL | 509 | 6 | 9/14 |
| http://157.85.108.47:3128 | TH | 1304 | 6 | 34/45 |
| socks5://101.36.104.46:10808 | JP | 2073 | 6 | 68/77 |
| socks5://144.24.47.42:1080 | US | 685 | 6 | 41/73 |
| socks5://193.25.215.182:22222 | US | 1478 | 6 | 71/77 |
| http://123.121.211.160:8888 | CN | 1535 | 5 | 10/23 |
| http://221.221.159.97:8888 | CN | 1199 | 5 | 12/30 |
| http://167.172.76.176:9090 | SG | 1161 | 5 | 20/38 |
| http://154.59.56.78:999 | VE | 2519 | 5 | 21/33 |
| socks5://135.125.232.151:1080 | DE | 609 | 5 | 7/8 |
| socks5://121.169.46.116:1090 | KR | 1232 | 5 | 50/77 |
| socks5://43.135.176.121:1080 | US | 3576 | 5 | 28/32 |
| socks5://45.61.129.165:9050 | US | 2935 | 5 | 64/77 |
| http://39.106.170.168:8080 | CN | 1721 | 4 | 38/75 |
| http://45.186.6.104:3128 | EC | 651 | 4 | 53/55 |
| http://186.33.45.220:999 | EC | 2679 | 4 | 22/46 |
| http://84.36.141.180:1981 | EG | 6278 | 4 | 10/28 |
| http://117.236.124.166:3128 | IN | 2118 | 4 | 51/77 |
| http://194.31.108.109:2080 | IR | 1196 | 4 | 23/37 |
| http://77.73.68.222:65000 | RU | 749 | 4 | 4/4 |
| http://124.156.194.52:8080 | SG | 2440 | 4 | 7/10 |
| http://128.199.254.13:9090 | SG | 1195 | 4 | 5/6 |
| http://61.91.162.126:8080 | TH | 1507 | 4 | 17/20 |
| http://103.10.231.189:8080 | TH | 1530 | 4 | 42/62 |
| http://153.51.201.35:999 | VE | 738 | 4 | 4/4 |
| http://154.3.76.14:999 | VE | 6557 | 4 | 21/30 |
| http://200.59.191.27:999 | VE | 2053 | 4 | 45/72 |
| http://210.211.113.33:80 | VN | 2572 | 4 | 26/47 |
| http://210.211.113.35:80 | VN | 3967 | 4 | 25/49 |
| socks5://62.113.112.246:10808 | RU | 976 | 4 | 4/4 |
| socks5://5.161.115.244:1080 | US | 94 | 4 | 4/4 |
| socks5://135.148.120.20:1080 | US | 315 | 4 | 4/4 |
| http://187.102.219.42:999 | AR | 5816 | 3 | 37/72 |
| http://8.138.217.152:21001 | CN | 3334 | 3 | 52/77 |
| http://114.249.210.133:8888 | CN | 6214 | 3 | 12/28 |
| http://114.249.219.180:8888 | CN | 6917 | 3 | 14/41 |
| http://114.250.195.77:8888 | CN | 1247 | 3 | 13/42 |
| http://114.252.12.211:8888 | CN | 1215 | 3 | 16/42 |
| http://114.252.15.106:8888 | CN | 1241 | 3 | 15/30 |
| http://119.188.131.55:17981 | CN | 2381 | 3 | 33/77 |
| http://123.119.25.143:8888 | CN | 3308 | 3 | 12/42 |
| http://123.119.178.176:8888 | CN | 1204 | 3 | 19/42 |
| http://123.121.113.161:8888 | CN | 1884 | 3 | 12/42 |
| http://123.121.123.216:8888 | CN | 1575 | 3 | 12/37 |
| http://221.221.156.154:8888 | CN | 6883 | 3 | 6/13 |
| http://222.128.172.158:8888 | CN | 1203 | 3 | 15/42 |
| http://38.19.43.108:999 | CO | 3613 | 3 | 5/13 |
| http://152.53.183.107:8081 | DE | 1456 | 3 | 19/30 |
| http://190.12.150.244:999 | EC | 6265 | 3 | 47/73 |
| http://41.33.219.140:1981 | EG | 1131 | 3 | 25/59 |
| http://65.109.217.164:3128 | FI | 630 | 3 | 9/10 |
| http://37.187.109.70:10111 | FR | 7893 | 3 | 30/77 |
| http://176.111.37.216:39811 | HK | 1218 | 3 | 63/77 |
| http://200.107.239.218:999 | HN | 6285 | 3 | 3/3 |
| http://103.174.122.87:3128 | ID | 7717 | 3 | 12/59 |
| http://38.194.246.34:999 | MX | 6327 | 3 | 40/68 |
| http://206.135.56.50:8080 | MX | 494 | 3 | 12/36 |
| http://124.105.40.93:8181 | PH | 6569 | 3 | 10/42 |
| http://43.156.153.104:8081 | SG | 3574 | 3 | 3/3 |
| http://152.42.177.32:8888 | SG | 1197 | 3 | 19/37 |
