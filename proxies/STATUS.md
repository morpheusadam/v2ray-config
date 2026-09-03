# Proxy status

Generated 2026-09-03T21:52:34Z by `harvest.py`.

- **1154** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2049** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16396** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 251/600 (42%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1754 |
| socks5 | 278 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 348 |
| US | 187 |
| CN | 126 |
| MX | 80 |
| CO | 69 |
| BD | 58 |
| RU | 58 |
| FR | 55 |
| PH | 51 |
| SG | 49 |
| DE | 47 |
| IN | 47 |
| JP | 45 |
| HK | 43 |
| NL | 43 |
| VE | 42 |
| BR | 40 |
| CA | 38 |
| EC | 34 |
| TH | 34 |
| VN | 30 |
| AU | 29 |
| KR | 29 |
| EG | 28 |
| DO | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-09-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 88 | 88 | 41 | 2026-09-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 90 | 90 | 45 | 2026-09-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 98 | 98 | 13 | 2026-09-03 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 107 | 107 | 35 | 2026-09-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 116 | 116 | 4 | 2026-09-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 143 | 143 | 44 | 2026-09-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-09-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 178 | 178 | 31 | 2026-09-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-03 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1056 | 1056 | 649 | 2026-09-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-09-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1600 | 2026-09-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1850 | 1848 | 169 | 2026-09-03 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2004 | 2000 | 742 | 2026-09-03 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2215 | 2215 | 1680 | 2026-09-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2361 | 2359 | 747 | 2026-09-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2774 | 2772 | 2055 | 2026-09-03 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1717 | 41 | 46/49 |
| http://34.43.46.91:80 | US | 1044 | 41 | 46/49 |
| http://95.211.174.135:3128 | NL | 1874 | 35 | 48/49 |
| http://204.76.203.9:3128 | NL | 2137 | 35 | 48/49 |
| http://204.76.203.9:8080 | NL | 666 | 35 | 41/42 |
| http://185.200.188.234:10001 | RU | 2669 | 35 | 48/49 |
| http://130.110.103.245:3128 | SA | 2478 | 35 | 47/49 |
| http://199.7.149.96:3128 | US | 151 | 28 | 28/28 |
| http://45.186.6.104:3128 | EC | 862 | 27 | 27/27 |
| http://64.112.184.210:3128 | US | 755 | 27 | 48/49 |
| http://103.211.103.170:3128 | HK | 584 | 21 | 21/21 |
| http://68.178.174.239:3128 | US | 1051 | 17 | 17/17 |
| http://68.178.174.239:8888 | US | 1362 | 17 | 17/17 |
| http://190.0.246.213:4040 | CO | 923 | 14 | 14/14 |
| http://1.231.81.166:3128 | KR | 1559 | 14 | 46/49 |
| http://189.51.168.164:999 | MX | 516 | 14 | 14/14 |
| socks5://47.250.211.53:1080 | MY | 1972 | 14 | 30/49 |
| socks5://193.25.215.182:22222 | US | 1444 | 12 | 45/49 |
| http://116.202.172.187:11000 | DE | 720 | 10 | 10/10 |
| http://91.134.141.4:3128 | FR | 614 | 10 | 10/10 |
| http://173.212.240.48:8888 | FR | 742 | 10 | 10/10 |
| http://5.129.254.129:8888 | RU | 1296 | 10 | 10/10 |
| socks5://171.25.158.95:1080 | SE | 5145 | 10 | 26/48 |
| http://176.111.37.5:39811 | HK | 1502 | 9 | 43/49 |
| http://47.81.56.193:8888 | TH | 1503 | 9 | 31/49 |
| http://14.251.13.20:8080 | VN | 1321 | 9 | 20/21 |
| http://40.177.104.199:48086 | CA | 1876 | 8 | 11/16 |
| http://34.88.38.81:9443 | FI | 860 | 8 | 9/14 |
| http://16.174.6.134:3128 | CA | 2819 | 7 | 7/7 |
| http://37.59.125.131:8888 | FR | 1803 | 7 | 36/49 |
| http://154.59.56.73:999 | VE | 5171 | 7 | 18/21 |
| socks5://101.36.104.46:10808 | JP | 2783 | 7 | 45/49 |
| socks5://5.255.117.250:1080 | NL | 3864 | 7 | 13/34 |
| http://40.177.104.199:22203 | CA | 5238 | 6 | 8/9 |
| http://120.232.115.170:17981 | CN | 1540 | 6 | 31/48 |
| http://181.78.23.187:999 | CO | 855 | 6 | 16/18 |
| http://181.78.74.252:999 | CO | 786 | 6 | 38/40 |
| http://181.78.74.253:999 | CO | 828 | 6 | 38/40 |
| http://175.143.76.177:8181 | MY | 4322 | 6 | 37/49 |
| http://190.97.236.128:999 | VE | 738 | 6 | 37/39 |
| http://190.97.236.129:999 | VE | 716 | 6 | 37/39 |
| socks5://49.13.22.249:10801 | DE | 7135 | 6 | 11/18 |
| http://103.177.118.145:8118 | BD | 1594 | 5 | 28/30 |
| http://123.121.122.126:8888 | CN | 4474 | 5 | 12/17 |
| http://217.76.245.80:999 | DO | 842 | 5 | 5/5 |
| http://186.5.94.206:999 | EC | 5533 | 5 | 10/11 |
| http://190.12.150.244:999 | EC | 2910 | 5 | 30/45 |
| http://197.164.101.13:1981 | EG | 5459 | 5 | 10/38 |
| http://175.136.239.173:8181 | MY | 4556 | 5 | 38/49 |
| http://85.198.100.232:13100 | RU | 1075 | 5 | 5/5 |
| http://154.59.56.72:999 | VE | 1955 | 5 | 6/8 |
| http://154.59.56.74:999 | VE | 1882 | 5 | 7/12 |
| socks5://5.75.133.113:10801 | DE | 2089 | 5 | 10/15 |
| socks5://5.75.133.113:10811 | DE | 1767 | 5 | 13/20 |
| socks5://144.126.197.184:1088 | GB | 5115 | 5 | 5/5 |
| socks5://101.36.104.239:10808 | JP | 1808 | 5 | 40/49 |
| socks5://5.255.99.75:1080 | NL | 4859 | 5 | 9/24 |
| socks5://5.255.117.127:1080 | NL | 743 | 5 | 12/25 |
| socks5://147.45.60.124:1082 | US | 3776 | 5 | 25/49 |
| socks5://178.130.47.21:1082 | US | 529 | 5 | 21/48 |
| http://187.102.219.42:999 | AR | 5290 | 4 | 23/44 |
| http://62.60.239.29:3128 | AT | 1115 | 4 | 4/4 |
| http://16.26.180.163:8083 | AU | 6484 | 4 | 8/9 |
| http://111.192.21.92:8888 | CN | 5593 | 4 | 11/13 |
| http://114.236.137.41:21000 | CN | 2844 | 4 | 33/49 |
| http://114.245.149.247:8888 | CN | 1740 | 4 | 5/7 |
| http://123.57.213.24:3539 | CN | 1398 | 4 | 23/48 |
| http://123.121.121.123:8888 | CN | 2019 | 4 | 12/14 |
| http://123.121.129.198:8888 | CN | 1357 | 4 | 9/14 |
| http://123.121.131.112:8888 | CN | 1458 | 4 | 9/12 |
| http://181.39.25.196:8118 | EC | 1867 | 4 | 47/49 |
| http://181.188.203.112:999 | EC | 7903 | 4 | 14/41 |
| http://194.163.175.167:40000 | FR | 726 | 4 | 13/14 |
| http://18.170.25.193:57422 | GB | 3872 | 4 | 20/45 |
| http://45.5.116.151:8080 | GT | 834 | 4 | 4/4 |
| http://176.111.37.216:39811 | HK | 1131 | 4 | 37/49 |
| http://38.46.214.177:8085 | ID | 1689 | 4 | 11/25 |
| http://140.238.32.108:3128 | JP | 2803 | 4 | 22/48 |
| http://197.224.185.3:3128 | MU | 1149 | 4 | 15/17 |
| http://190.43.231.101:999 | PE | 5475 | 4 | 9/26 |
| http://5.129.254.49:8888 | RU | 1367 | 4 | 4/4 |
| http://5.129.254.51:8888 | RU | 1464 | 4 | 4/4 |
| http://5.129.254.70:8888 | RU | 1419 | 4 | 4/4 |
| http://85.193.65.88:8888 | RU | 1153 | 4 | 18/39 |
| http://51.21.132.197:3128 | SE | 1731 | 4 | 7/9 |
| http://157.85.97.240:3128 | TH | 1239 | 4 | 11/17 |
| http://157.85.108.47:3128 | TH | 1285 | 4 | 12/17 |
| http://157.85.111.64:3128 | TH | 1248 | 4 | 15/17 |
| http://95.3.69.222:8080 | TR | 1938 | 4 | 46/49 |
| http://3.92.47.79:9002 | US | 1591 | 4 | 10/16 |
| http://34.223.251.103:1001 | US | 788 | 4 | 4/4 |
| http://34.223.252.220:1001 | US | 879 | 4 | 4/4 |
| http://44.204.11.88:44218 | US | 1531 | 4 | 5/7 |
| http://42.96.18.62:1311 | VN | 3776 | 4 | 36/48 |
| socks4://45.61.129.165:9050 | US | 3338 | 4 | 40/49 |
| socks5://45.95.233.88:1082 | FR | 1839 | 4 | 24/46 |
| socks5://79.137.79.217:2080 | FR | 1302 | 4 | 4/4 |
| socks5://80.72.180.122:1080 | KG | 6886 | 4 | 16/47 |
| socks5://121.169.46.116:1090 | KR | 2624 | 4 | 32/49 |
| socks5://165.22.63.133:1080 | SG | 1656 | 4 | 5/6 |
