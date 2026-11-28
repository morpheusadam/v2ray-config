# Proxy status

Generated 2026-11-28T02:09:15Z by `harvest.py`.

- **1454** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3523** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25103** endpoints on record
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
| http | 3097 |
| socks5 | 411 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 928 |
| ?? | 361 |
| NL | 165 |
| PH | 162 |
| MX | 140 |
| CO | 133 |
| US | 103 |
| BR | 94 |
| TR | 90 |
| IN | 88 |
| VE | 88 |
| CN | 85 |
| TH | 84 |
| RU | 74 |
| BD | 60 |
| EC | 51 |
| AR | 45 |
| PK | 43 |
| DO | 41 |
| DE | 35 |
| EG | 33 |
| VN | 31 |
| PE | 29 |
| ZA | 29 |
| CH | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 4 | 2026-11-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-28 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 124 | 124 | 23 | 2026-11-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 40 | 2026-11-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 56 | 2026-11-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 163 | 163 | 15 | 2026-11-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 219 | 219 | 18 | 2026-11-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 313 | 313 | 81 | 2026-11-28 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 499 | 499 | 336 | 2026-11-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1191 | 1191 | 188 | 2026-11-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-11-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-28 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1929 | 1929 | 0 | 2026-11-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2186 | 2186 | 210 | 2026-11-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2451 | 2451 | 697 | 2026-11-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2525 | 2525 | 1522 | 2026-11-28 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5797 | 5797 | 4667 | 2026-11-28 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11749 | 11749 | 2213 | 2026-11-28 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1007 | 89 | 199/218 |
| http://130.110.103.245:3128 | SA | 1286 | 64 | 200/218 |
| http://45.155.226.177:3128 | HK | 937 | 27 | 32/34 |
| http://4.144.146.21:80 | SG | 858 | 25 | 101/110 |
| http://34.43.46.91:80 | US | 426 | 23 | 211/218 |
| http://189.51.168.164:999 | MX | 1724 | 22 | 50/54 |
| http://20.98.234.24:8080 | US | 404 | 22 | 22/22 |
| socks5://69.55.49.177:38182 | US | 677 | 22 | 62/73 |
| http://103.237.102.191:11111 | DE | 928 | 21 | 205/218 |
| http://45.186.6.104:3128 | EC | 935 | 20 | 186/196 |
| http://103.133.26.50:8080 | ID | 1149 | 20 | 84/119 |
| http://103.133.26.73:3128 | ID | 1206 | 20 | 108/196 |
| http://45.135.95.185:3128 | RU | 1422 | 16 | 16/16 |
| http://128.199.113.85:9090 | SG | 860 | 16 | 36/49 |
| socks5://123.58.219.171:10808 | HK | 1885 | 16 | 160/218 |
| http://103.163.80.181:8085 | ID | 1170 | 14 | 14/14 |
| http://50.238.106.26:3128 | US | 397 | 14 | 14/14 |
| http://158.247.125.5:9443 | CO | 702 | 13 | 13/13 |
| http://34.43.46.91:443 | US | 417 | 13 | 202/218 |
| http://216.125.18.67:3128 | US | 700 | 13 | 13/13 |
| http://185.191.239.248:3128 | CH | 2353 | 11 | 154/217 |
| http://45.136.253.145:3128 | TH | 973 | 11 | 16/22 |
| http://102.244.78.61:8083 | CM | 1419 | 10 | 84/106 |
| http://45.65.138.48:999 | CO | 1575 | 10 | 115/218 |
| http://177.234.217.89:999 | EC | 3298 | 10 | 29/43 |
| http://129.153.97.250:9443 | US | 313 | 10 | 10/10 |
| http://154.59.56.78:999 | VE | 2658 | 10 | 120/174 |
| http://103.81.86.170:8888 | VN | 2585 | 10 | 10/10 |
| socks5://59.11.209.162:1080 | KR | 1045 | 10 | 10/10 |
| http://190.12.150.244:999 | EC | 5561 | 9 | 160/214 |
| http://128.199.116.219:9090 | SG | 863 | 9 | 107/137 |
| http://45.65.137.218:999 | CO | 839 | 8 | 95/183 |
| http://197.164.101.14:1981 | EG | 1324 | 8 | 58/188 |
| http://173.212.207.102:1214 | FR | 801 | 8 | 8/8 |
| http://123.115.143.194:8888 | CN | 1326 | 7 | 11/17 |
| http://197.164.101.11:1981 | EG | 1270 | 7 | 16/35 |
| http://213.131.85.28:1976 | EG | 1219 | 7 | 22/32 |
| http://187.102.219.42:999 | AR | 1299 | 6 | 125/213 |
| http://114.249.219.234:8888 | CN | 1367 | 6 | 10/14 |
| http://41.65.55.27:1981 | EG | 1966 | 6 | 61/158 |
| http://41.196.16.231:1976 | EG | 1261 | 6 | 10/45 |
| http://45.245.208.180:8080 | EG | 1340 | 6 | 65/91 |
| http://81.10.102.153:8080 | EG | 1450 | 6 | 6/6 |
| http://198.244.254.77:3128 | GB | 7779 | 6 | 82/102 |
| http://103.172.70.27:9090 | ID | 4595 | 6 | 12/32 |
| http://202.154.241.199:808 | PK | 5366 | 6 | 13/39 |
| http://81.27.101.176:443 | PL | 886 | 6 | 6/6 |
| http://81.27.101.176:80 | PL | 897 | 6 | 6/6 |
| http://128.199.121.61:9090 | SG | 854 | 6 | 108/138 |
| http://195.158.8.123:3128 | UZ | 3835 | 6 | 141/216 |
| http://154.59.56.74:999 | VE | 2509 | 6 | 124/181 |
| socks5://103.13.19.219:10808 | JP | 1280 | 6 | 26/35 |
| socks5://193.218.118.128:1080 | UA | 3944 | 6 | 54/74 |
| socks5://172.104.210.252:1080 | US | 454 | 6 | 6/6 |
| http://16.51.5.77:16637 | AU | 3675 | 5 | 47/158 |
| http://123.115.226.82:8888 | CN | 3718 | 5 | 63/164 |
| http://123.121.113.161:8888 | CN | 1561 | 5 | 25/43 |
| http://123.121.140.72:8888 | CN | 5330 | 5 | 42/70 |
| http://38.226.242.71:8080 | ID | 5070 | 5 | 49/157 |
| http://103.133.26.72:8080 | ID | 1933 | 5 | 91/144 |
| http://163.227.248.81:8818 | ID | 4919 | 5 | 37/190 |
| http://102.68.76.247:5566 | KE | 1995 | 5 | 70/171 |
| http://185.238.236.226:58080 | PL | 2737 | 5 | 74/140 |
| http://116.204.166.151:8080 | TR | 6699 | 5 | 42/173 |
| http://114.249.208.204:8888 | ?? | 7990 | 5 | 5/5 |
| socks5://78.142.217.197:1080 | DE | 929 | 5 | 11/14 |
| socks5://95.31.115.101:9150 | RU | 2005 | 5 | 27/38 |
| http://114.249.208.179:8888 | CN | 2246 | 4 | 5/6 |
| http://222.128.174.236:8888 | CN | 1878 | 4 | 16/22 |
| http://45.185.163.111:999 | EC | 1558 | 4 | 24/38 |
| http://177.234.217.93:999 | EC | 4654 | 4 | 55/77 |
| http://45.240.232.61:8080 | EG | 1489 | 4 | 90/198 |
| http://34.96.238.40:8080 | HK | 845 | 4 | 22/149 |
| http://103.61.234.186:8180 | ID | 1671 | 4 | 98/215 |
| http://103.86.117.23:8080 | ID | 6632 | 4 | 44/138 |
| http://103.156.248.100:3128 | ID | 7089 | 4 | 7/31 |
| http://110.232.78.195:8080 | ID | 3264 | 4 | 39/180 |
| http://175.184.236.12:1111 | ID | 4096 | 4 | 30/178 |
| http://51.17.99.116:37158 | IL | 1519 | 4 | 39/104 |
| http://43.216.197.62:26130 | MY | 2276 | 4 | 58/186 |
| http://119.93.207.214:8082 | PH | 6694 | 4 | 57/210 |
| http://122.52.157.209:8081 | PH | 6295 | 4 | 47/164 |
| http://185.238.238.21:58080 | PL | 6647 | 4 | 66/182 |
| http://185.238.238.49:58080 | PL | 1967 | 4 | 88/212 |
| http://167.99.74.174:9090 | SG | 878 | 4 | 121/178 |
| http://24.153.226.234:8056 | US | 2870 | 4 | 39/167 |
| http://154.59.56.73:999 | VE | 2431 | 4 | 132/190 |
| http://181.233.161.50:999 | VE | 3765 | 4 | 54/196 |
| http://20.235.56.94:8080 | ?? | 1070 | 4 | 4/4 |
| http://27.49.76.149:8082 | ?? | 3345 | 4 | 4/4 |
| http://111.119.162.248:10912 | ?? | 5489 | 4 | 4/4 |
| http://111.119.162.248:10931 | ?? | 5372 | 4 | 4/4 |
| http://178.185.231.196:3128 | ?? | 1277 | 4 | 4/4 |
| socks4://111.119.162.248:10925 | ?? | 5218 | 4 | 4/4 |
| socks5://202.40.190.74:1080 | BD | 1931 | 4 | 38/216 |
| socks5://171.25.158.95:1080 | SE | 1772 | 4 | 97/133 |
| http://45.187.105.196:8080 | BR | 2310 | 3 | 34/167 |
| http://186.26.92.233:58339 | BR | 5485 | 3 | 8/46 |
| http://16.52.81.236:30468 | CA | 4052 | 3 | 30/130 |
| http://35.183.78.223:58093 | CA | 1106 | 3 | 43/116 |
