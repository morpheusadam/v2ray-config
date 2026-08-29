# Proxy status

Generated 2026-08-29T17:17:23Z by `harvest.py`.

- **627** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1541** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14796** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 140/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1329 |
| socks5 | 197 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 298 |
| US | 128 |
| CN | 102 |
| CO | 64 |
| BR | 49 |
| DE | 47 |
| MX | 46 |
| PH | 46 |
| TH | 40 |
| VE | 39 |
| FR | 38 |
| IN | 38 |
| RU | 38 |
| EC | 36 |
| NL | 35 |
| TR | 32 |
| BD | 31 |
| JP | 24 |
| SG | 23 |
| AU | 21 |
| HK | 21 |
| VN | 20 |
| DO | 18 |
| CL | 15 |
| KH | 14 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 46 | 46 | 16 | 2026-08-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 75 | 75 | 34 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 76 | 76 | 12 | 2026-08-29 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 105 | 105 | 18 | 2026-08-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 120 | 120 | 56 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 131 | 131 | 31 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 146 | 146 | 65 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 211 | 211 | 42 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-29 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 493 | 493 | 243 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1150 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1604 | 2026-08-29 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1895 | 1891 | 435 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1936 | 1934 | 234 | 2026-08-29 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2173 | 2173 | 1656 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2350 | 2348 | 643 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2777 | 2775 | 2133 | 2026-08-29 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 883 | 35 | 37/38 |
| http://34.43.46.91:443 | US | 425 | 30 | 35/38 |
| http://34.43.46.91:80 | US | 658 | 30 | 35/38 |
| http://103.237.102.191:11111 | DE | 694 | 24 | 37/38 |
| http://95.211.174.135:3128 | NL | 700 | 24 | 37/38 |
| http://204.76.203.9:3128 | NL | 722 | 24 | 37/38 |
| http://204.76.203.9:8080 | NL | 510 | 24 | 30/31 |
| http://185.200.188.234:10001 | RU | 6662 | 24 | 37/38 |
| http://130.110.103.245:3128 | SA | 1091 | 24 | 36/38 |
| http://95.3.69.222:8080 | TR | 1090 | 24 | 37/38 |
| http://199.7.149.90:3128 | US | 20 | 21 | 21/21 |
| http://199.7.149.96:3128 | US | 15 | 17 | 17/17 |
| http://45.186.6.104:3128 | EC | 702 | 16 | 16/16 |
| http://64.112.184.210:3128 | US | 126 | 16 | 37/38 |
| http://190.0.246.210:4040 | CO | 6796 | 14 | 34/37 |
| http://103.130.61.61:8081 | ID | 1724 | 13 | 33/38 |
| http://42.96.18.62:1311 | VN | 1809 | 12 | 27/37 |
| socks5://144.91.121.61:1088 | FR | 5961 | 12 | 36/38 |
| http://176.111.37.5:39811 | HK | 2332 | 11 | 33/38 |
| http://190.0.246.211:4040 | CO | 6404 | 10 | 33/38 |
| http://103.211.103.170:3128 | HK | 3134 | 10 | 10/10 |
| http://202.28.194.139:31280 | TH | 2183 | 10 | 36/38 |
| http://14.251.13.20:8080 | VN | 1365 | 10 | 10/10 |
| socks5://101.36.104.46:10808 | JP | 2925 | 10 | 35/38 |
| socks5://45.61.129.165:9050 | US | 3961 | 10 | 30/38 |
| http://87.251.77.29:3128 | DE | 588 | 9 | 35/38 |
| socks5://45.194.33.12:30001 | HK | 1463 | 9 | 27/34 |
| socks5://45.194.33.12:30002 | HK | 1386 | 9 | 11/12 |
| http://103.177.118.145:8118 | BD | 6632 | 8 | 18/19 |
| http://114.236.137.41:21000 | CN | 4695 | 8 | 26/38 |
| http://81.19.210.10:80 | GB | 434 | 8 | 8/8 |
| socks5://45.144.54.40:1080 | DE | 4972 | 7 | 29/38 |
| http://87.237.15.238:7080 | BE | 4650 | 6 | 6/6 |
| http://197.224.185.3:3128 | MU | 1738 | 6 | 6/6 |
| http://175.136.239.173:8181 | MY | 7371 | 6 | 30/38 |
| http://157.85.105.217:3128 | TH | 3387 | 6 | 6/6 |
| http://157.85.108.68:3128 | TH | 1343 | 6 | 6/6 |
| http://157.85.111.64:3128 | TH | 4417 | 6 | 6/6 |
| http://68.178.174.239:3128 | US | 1403 | 6 | 6/6 |
| http://68.178.174.239:8888 | US | 1417 | 6 | 6/6 |
| http://209.174.97.162:5999 | US | 1238 | 6 | 6/6 |
| http://8.138.217.152:21001 | CN | 1968 | 5 | 25/38 |
| http://181.78.23.187:999 | CO | 726 | 5 | 6/7 |
| http://181.78.74.252:999 | CO | 727 | 5 | 28/29 |
| http://181.78.74.253:999 | CO | 784 | 5 | 28/29 |
| http://190.97.236.128:999 | VE | 677 | 5 | 27/28 |
| http://190.97.236.129:999 | VE | 2639 | 5 | 27/28 |
| http://210.211.113.34:80 | VN | 3110 | 5 | 9/10 |
| socks5://113.249.111.67:1080 | CN | 3099 | 5 | 5/5 |
| socks5://45.12.18.106:1080 | RU | 1077 | 5 | 5/5 |
| socks5://84.8.102.52:1080 | SA | 1359 | 5 | 5/5 |
| socks5://171.25.158.95:1080 | SE | 4317 | 5 | 16/37 |
| http://152.53.136.178:10000 | DE | 2161 | 4 | 9/13 |
| http://41.196.16.233:1976 | EG | 5009 | 4 | 9/16 |
| http://212.154.169.90:3128 | KZ | 1152 | 4 | 14/17 |
| socks5://5.75.133.113:10811 | DE | 1729 | 4 | 6/9 |
| socks5://213.199.47.140:1080 | FR | 1615 | 4 | 4/4 |
| http://87.237.15.239:7080 | BE | 529 | 3 | 3/3 |
| http://184.75.221.82:3118 | CA | 159 | 3 | 3/3 |
| http://111.200.191.214:8888 | CN | 7736 | 3 | 3/3 |
| http://114.248.86.121:8888 | CN | 2225 | 3 | 3/3 |
| http://114.248.179.223:8888 | CN | 1853 | 3 | 5/6 |
| http://114.249.213.204:8888 | CN | 7000 | 3 | 3/3 |
| http://114.250.195.182:8888 | CN | 6913 | 3 | 3/3 |
| http://114.254.48.165:8888 | CN | 5969 | 3 | 3/3 |
| http://120.232.115.170:17981 | CN | 1758 | 3 | 22/37 |
| http://123.115.212.50:8888 | CN | 1918 | 3 | 3/3 |
| http://123.119.178.176:8888 | CN | 2101 | 3 | 3/3 |
| http://123.121.112.4:8888 | CN | 2615 | 3 | 3/3 |
| http://123.121.115.239:8888 | CN | 5215 | 3 | 3/3 |
| http://123.121.121.123:8888 | CN | 3022 | 3 | 3/3 |
| http://123.121.141.57:8888 | CN | 3034 | 3 | 3/3 |
| http://123.121.209.61:8888 | CN | 6930 | 3 | 3/3 |
| http://221.221.166.95:8888 | CN | 1946 | 3 | 3/3 |
| http://190.0.246.213:4040 | CO | 1570 | 3 | 3/3 |
| http://130.61.112.125:443 | DE | 516 | 3 | 3/3 |
| http://194.163.175.167:40000 | FR | 792 | 3 | 3/3 |
| http://103.155.198.138:3125 | ID | 2544 | 3 | 7/28 |
| http://103.180.118.150:8080 | ID | 6742 | 3 | 8/23 |
| http://1.231.81.166:3128 | KR | 1252 | 3 | 35/38 |
| http://38.210.179.8:999 | MX | 3318 | 3 | 8/20 |
| http://45.188.167.25:999 | MX | 6678 | 3 | 3/3 |
| http://189.51.168.164:999 | MX | 366 | 3 | 3/3 |
| http://175.136.239.174:8181 | MY | 3974 | 3 | 24/38 |
| http://43.128.73.106:80 | SG | 1360 | 3 | 10/33 |
| http://43.156.227.68:80 | SG | 1146 | 3 | 3/3 |
| http://43.160.242.118:3128 | SG | 4837 | 3 | 28/35 |
| http://159.223.52.199:3128 | SG | 3448 | 3 | 7/24 |
| http://157.85.97.203:3128 | TH | 1344 | 3 | 3/3 |
| http://157.85.97.204:3128 | TH | 1338 | 3 | 3/3 |
| http://157.85.97.242:3128 | TH | 1318 | 3 | 3/3 |
| http://157.85.105.218:3128 | TH | 1316 | 3 | 3/3 |
| http://157.85.105.220:3128 | TH | 1573 | 3 | 3/3 |
| http://157.85.108.50:3128 | TH | 1349 | 3 | 3/3 |
| http://157.85.108.69:3128 | TH | 1328 | 3 | 3/3 |
| http://157.85.108.135:3128 | TH | 1333 | 3 | 3/3 |
| http://122.116.180.77:8080 | TW | 3491 | 3 | 8/34 |
| http://35.94.193.222:5001 | US | 2752 | 3 | 3/3 |
| http://43.153.54.58:3128 | US | 5845 | 3 | 5/10 |
| http://45.59.100.205:3128 | US | 240 | 3 | 3/3 |
