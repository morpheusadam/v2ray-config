# Proxy status

Generated 2026-09-17T17:44:19Z by `harvest.py`.

- **1473** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2333** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25389** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 124/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1344 |
| socks5 | 986 |
| socks4 | 3 |

| country | entries |
|---|---|
| NL | 755 |
| ID | 334 |
| CN | 117 |
| US | 97 |
| RU | 71 |
| MX | 67 |
| PH | 67 |
| CO | 63 |
| BD | 49 |
| SG | 49 |
| VE | 44 |
| DE | 40 |
| BR | 36 |
| VN | 36 |
| IN | 33 |
| FR | 32 |
| EC | 31 |
| EG | 29 |
| JP | 29 |
| TH | 22 |
| HK | 19 |
| DO | 18 |
| FI | 18 |
| AR | 16 |
| PK | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 28 | 28 | 15 | 2026-09-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 60 | 60 | 27 | 2026-09-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 95 | 95 | 27 | 2026-09-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 99 | 99 | 25 | 2026-09-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-09-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 202 | 202 | 40 | 2026-09-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 204 | 204 | 76 | 2026-09-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 436 | 436 | 255 | 2026-09-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-09-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-09-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1151 | 2026-09-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1607 | 2026-09-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1905 | 1901 | 487 | 2026-09-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1905 | 1903 | 742 | 2026-09-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2194 | 2192 | 1646 | 2026-09-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2205 | 2203 | 747 | 2026-09-17 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 10296 | 10296 | 6315 | 2026-09-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 16203 | 16202 | 2526 | 2026-09-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 898 | 68 | 73/76 |
| http://34.43.46.91:80 | US | 805 | 68 | 73/76 |
| http://95.211.174.135:3128 | NL | 1442 | 62 | 75/76 |
| http://185.200.188.234:10001 | RU | 1479 | 62 | 75/76 |
| http://130.110.103.245:3128 | SA | 1687 | 62 | 74/76 |
| http://1.231.81.166:3128 | KR | 928 | 41 | 73/76 |
| http://190.97.236.128:999 | VE | 1924 | 33 | 64/66 |
| http://190.97.236.129:999 | VE | 895 | 33 | 64/66 |
| http://95.3.69.222:8080 | TR | 1528 | 31 | 73/76 |
| socks5://107.167.18.122:443 | US | 1159 | 21 | 27/28 |
| socks5://83.147.216.208:1080 | FI | 1421 | 20 | 26/44 |
| http://184.75.221.82:3118 | CA | 2264 | 17 | 38/41 |
| socks5://144.91.121.61:1088 | FR | 2100 | 17 | 67/76 |
| http://91.134.141.4:3128 | FR | 788 | 15 | 35/37 |
| http://186.5.94.206:999 | EC | 1046 | 13 | 36/38 |
| http://107.150.41.226:18080 | US | 464 | 13 | 13/13 |
| socks5://213.199.47.140:1080 | FR | 7346 | 13 | 35/42 |
| http://190.0.246.210:4040 | CO | 832 | 9 | 66/75 |
| http://186.33.45.219:999 | EC | 861 | 9 | 39/65 |
| http://43.156.199.63:8080 | SG | 2179 | 9 | 10/11 |
| http://38.51.207.104:8080 | VE | 2776 | 9 | 16/17 |
| socks5://103.162.30.189:10808 | VN | 2292 | 8 | 10/11 |
| socks5://160.22.17.4:9988 | VN | 1387 | 8 | 33/72 |
| http://34.88.38.81:9443 | FI | 910 | 7 | 28/41 |
| http://35.228.49.168:9443 | FI | 948 | 7 | 9/13 |
| http://197.224.185.3:3128 | MU | 1324 | 7 | 40/44 |
| http://189.51.168.164:999 | MX | 1596 | 7 | 40/41 |
| http://45.132.252.25:49156 | RU | 1120 | 7 | 7/7 |
| http://115.231.181.40:8128 | CN | 1873 | 6 | 34/75 |
| http://5.129.254.5:8888 | RU | 1437 | 6 | 29/31 |
| http://5.129.254.49:8888 | RU | 1730 | 6 | 30/31 |
| http://5.129.254.51:8888 | RU | 1702 | 6 | 30/31 |
| http://5.129.254.60:8888 | RU | 1514 | 6 | 29/30 |
| http://5.129.254.70:8888 | RU | 2296 | 6 | 30/31 |
| http://5.129.254.129:8888 | RU | 1520 | 6 | 35/37 |
| http://5.129.254.154:8888 | RU | 1371 | 6 | 26/27 |
| http://193.104.179.115:3128 | UZ | 1588 | 6 | 24/41 |
| socks5://57.128.231.218:1004 | PL | 1452 | 6 | 7/10 |
| socks5://45.32.160.61:1088 | US | 458 | 6 | 27/29 |
| http://185.195.71.218:18080 | CH | 1291 | 5 | 7/13 |
| http://47.121.139.13:3128 | CN | 1746 | 5 | 36/75 |
| http://120.232.115.170:17981 | CN | 1494 | 5 | 54/75 |
| http://190.0.246.211:4040 | CO | 901 | 5 | 64/76 |
| http://190.0.246.213:4040 | CO | 692 | 5 | 34/41 |
| http://213.111.146.36:18080 | NL | 2002 | 5 | 8/13 |
| http://157.85.108.47:3128 | TH | 1074 | 5 | 33/44 |
| socks5://101.36.104.46:10808 | JP | 1611 | 5 | 67/76 |
| socks5://95.220.142.90:1080 | RU | 4847 | 5 | 5/5 |
| socks5://144.24.47.42:1080 | US | 223 | 5 | 40/72 |
| socks5://193.25.215.182:22222 | US | 692 | 5 | 70/76 |
| http://114.249.237.87:8888 | CN | 1228 | 4 | 21/40 |
| http://123.121.211.160:8888 | CN | 1310 | 4 | 9/22 |
| http://221.221.159.97:8888 | CN | 1207 | 4 | 11/29 |
| http://167.172.76.176:9090 | SG | 902 | 4 | 19/37 |
| http://154.59.56.78:999 | VE | 2224 | 4 | 20/32 |
| http://163.181.207.169:9999 | VN | 1256 | 4 | 23/74 |
| socks5://135.125.232.151:1080 | DE | 994 | 4 | 6/7 |
| socks5://123.58.219.171:10808 | HK | 5387 | 4 | 61/76 |
| socks5://202.62.52.20:1080 | KH | 4834 | 4 | 18/43 |
| socks5://121.169.46.116:1090 | KR | 2675 | 4 | 49/76 |
| socks5://43.135.176.121:1080 | US | 399 | 4 | 27/31 |
| socks5://45.61.129.165:9050 | US | 1462 | 4 | 63/76 |
| http://39.106.170.168:8080 | CN | 1675 | 3 | 37/74 |
| http://122.246.3.12:17981 | CN | 2248 | 3 | 34/70 |
| http://38.75.82.217:999 | DO | 5197 | 3 | 3/3 |
| http://45.186.6.104:3128 | EC | 790 | 3 | 52/54 |
| http://186.33.45.220:999 | EC | 2929 | 3 | 21/45 |
| http://84.36.141.180:1981 | EG | 1217 | 3 | 9/27 |
| http://117.236.124.166:3128 | IN | 1474 | 3 | 50/76 |
| http://194.31.108.109:2080 | IR | 3476 | 3 | 22/36 |
| http://212.154.169.90:3128 | KZ | 1418 | 3 | 38/55 |
| http://103.25.220.250:8083 | PH | 6952 | 3 | 10/65 |
| http://77.73.68.222:65000 | RU | 1173 | 3 | 3/3 |
| http://124.156.194.52:8080 | SG | 2198 | 3 | 6/9 |
| http://128.199.254.13:9090 | SG | 905 | 3 | 4/5 |
| http://129.226.206.61:80 | SG | 889 | 3 | 20/68 |
| http://61.91.162.126:8080 | TH | 1194 | 3 | 16/19 |
| http://103.10.231.189:8080 | TH | 1448 | 3 | 41/61 |
| http://153.51.201.35:999 | VE | 898 | 3 | 3/3 |
| http://154.3.76.14:999 | VE | 781 | 3 | 20/29 |
| http://186.167.113.97:999 | VE | 3015 | 3 | 3/3 |
| http://200.59.191.27:999 | VE | 2161 | 3 | 44/71 |
| http://163.181.207.213:9999 | VN | 1303 | 3 | 14/33 |
| http://210.211.113.33:80 | VN | 3140 | 3 | 25/46 |
| http://210.211.113.35:80 | VN | 3170 | 3 | 24/48 |
| socks5://103.210.161.8:1080 | CN | 1001 | 3 | 37/49 |
| socks5://49.13.22.249:10802 | DE | 6955 | 3 | 3/3 |
| socks5://43.230.193.154:1080 | KH | 3885 | 3 | 19/74 |
| socks5://45.74.31.25:6178 | NL | 3079 | 3 | 3/3 |
| socks5://45.74.31.40:12951 | NL | 7814 | 3 | 3/3 |
| socks5://45.74.31.40:17113 | NL | 6781 | 3 | 3/3 |
| socks5://147.45.234.180:1080 | NL | 4035 | 3 | 5/22 |
| socks5://62.113.112.246:10808 | RU | 1757 | 3 | 3/3 |
| socks5://5.161.115.244:1080 | US | 449 | 3 | 3/3 |
| socks5://135.148.120.20:1080 | US | 704 | 3 | 3/3 |
| http://45.232.0.2:8080 | AR | 5728 | 2 | 21/74 |
| http://187.102.219.42:999 | AR | 1299 | 2 | 36/71 |
| http://8.138.217.152:21001 | CN | 2914 | 2 | 51/76 |
| http://101.251.204.174:8080 | CN | 1750 | 2 | 30/62 |
| http://114.249.209.219:8888 | CN | 1166 | 2 | 17/34 |
