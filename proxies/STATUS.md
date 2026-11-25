# Proxy status

Generated 2026-11-25T22:26:42Z by `harvest.py`.

- **1514** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3169** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25693** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 147/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2768 |
| socks5 | 395 |
| socks4 | 6 |

| country | entries |
|---|---|
| ID | 872 |
| NL | 196 |
| PH | 161 |
| MX | 129 |
| CO | 122 |
| US | 110 |
| CN | 97 |
| BR | 89 |
| VE | 89 |
| TR | 85 |
| IN | 81 |
| RU | 79 |
| BD | 69 |
| CH | 68 |
| TH | 67 |
| DO | 50 |
| EC | 48 |
| AR | 47 |
| ZA | 38 |
| EG | 34 |
| PK | 34 |
| SG | 32 |
| VN | 32 |
| DE | 31 |
| PE | 31 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-11-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 33 | 2026-11-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 57 | 2026-11-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 162 | 162 | 51 | 2026-11-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 205 | 205 | 18 | 2026-11-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 227 | 227 | 22 | 2026-11-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 398 | 398 | 262 | 2026-11-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 459 | 459 | 116 | 2026-11-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1487 | 1487 | 146 | 2026-11-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1519 | 1519 | 271 | 2026-11-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1124 | 2026-11-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2359 | 2359 | 250 | 2026-11-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2711 | 2711 | 693 | 2026-11-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2992 | 2992 | 1812 | 2026-11-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5736 | 5736 | 4509 | 2026-11-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12960 | 12960 | 2094 | 2026-11-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 752 | 84 | 194/213 |
| http://130.110.103.245:3128 | SA | 1166 | 59 | 195/213 |
| http://141.94.22.37:3128 | FR | 499 | 25 | 28/29 |
| http://45.155.226.177:3128 | HK | 465 | 22 | 27/29 |
| http://4.144.146.21:80 | SG | 1151 | 20 | 96/105 |
| http://34.43.46.91:80 | US | 307 | 18 | 206/213 |
| http://189.51.168.164:999 | MX | 1430 | 17 | 45/49 |
| http://20.98.234.24:8080 | US | 78 | 17 | 17/17 |
| socks5://69.55.49.177:38182 | US | 1136 | 17 | 57/68 |
| http://103.237.102.191:11111 | DE | 554 | 16 | 200/213 |
| http://45.186.6.104:3128 | EC | 2586 | 15 | 181/191 |
| http://103.133.26.50:8080 | ID | 1508 | 15 | 79/114 |
| http://103.133.26.73:3128 | ID | 1599 | 15 | 103/191 |
| http://147.161.246.34:80 | CH | 6601 | 13 | 13/13 |
| http://146.190.80.158:9090 | SG | 1171 | 12 | 101/139 |
| http://45.135.95.185:3128 | RU | 6955 | 11 | 11/11 |
| http://128.199.113.85:9090 | SG | 1151 | 11 | 31/44 |
| socks5://123.58.219.171:10808 | HK | 2205 | 11 | 155/213 |
| http://190.123.83.137:999 | AR | 1639 | 10 | 43/50 |
| http://144.124.251.24:10801 | NL | 505 | 10 | 80/161 |
| http://144.124.251.24:11180 | NL | 818 | 10 | 92/144 |
| http://103.163.80.181:8085 | ID | 1547 | 9 | 9/9 |
| http://50.238.106.26:3128 | US | 970 | 9 | 9/9 |
| http://158.247.125.5:9443 | CO | 439 | 8 | 8/8 |
| http://34.43.46.91:443 | US | 649 | 8 | 197/213 |
| http://216.125.18.67:3128 | US | 585 | 8 | 8/8 |
| http://103.120.76.34:8085 | ID | 6212 | 7 | 19/94 |
| http://103.125.15.45:8181 | ID | 2465 | 7 | 8/9 |
| http://193.124.33.31:2052 | RU | 828 | 7 | 7/7 |
| http://103.21.150.15:3128 | VN | 1314 | 7 | 9/25 |
| http://185.191.239.248:3128 | CH | 1030 | 6 | 149/212 |
| http://177.234.217.93:999 | EC | 5539 | 6 | 51/72 |
| http://45.136.253.145:3128 | TH | 1266 | 6 | 11/17 |
| socks5://209.50.255.91:1080 | US | 1337 | 6 | 65/130 |
| http://102.244.78.61:8082 | CM | 1239 | 5 | 79/102 |
| http://102.244.78.61:8083 | CM | 1187 | 5 | 79/101 |
| http://102.244.78.61:8087 | CM | 1201 | 5 | 76/103 |
| http://45.65.138.48:999 | CO | 1375 | 5 | 110/213 |
| http://177.234.217.89:999 | EC | 1692 | 5 | 24/38 |
| http://52.128.238.98:18080 | HK | 422 | 5 | 22/28 |
| http://157.66.16.45:7789 | ID | 4870 | 5 | 10/33 |
| http://31.130.153.132:3128 | KZ | 2520 | 5 | 5/5 |
| http://189.51.168.165:999 | MX | 1897 | 5 | 112/125 |
| http://144.124.251.24:10372 | NL | 582 | 5 | 94/157 |
| http://119.94.185.43:8082 | PH | 3509 | 5 | 11/13 |
| http://13.215.184.250:3128 | SG | 3290 | 5 | 43/99 |
| http://13.59.11.63:3128 | US | 6812 | 5 | 5/5 |
| http://129.153.97.250:9443 | US | 3433 | 5 | 5/5 |
| http://154.59.56.78:999 | VE | 6043 | 5 | 115/169 |
| http://103.81.86.170:8888 | VN | 2726 | 5 | 5/5 |
| socks5://59.11.209.162:1080 | KR | 1210 | 5 | 5/5 |
| socks5://45.141.177.0:1080 | SE | 835 | 5 | 5/5 |
| http://177.130.25.76:8080 | BR | 5202 | 4 | 27/96 |
| http://201.28.86.18:61804 | BR | 3385 | 4 | 26/34 |
| http://190.12.150.244:999 | EC | 2496 | 4 | 155/209 |
| http://41.159.154.43:3128 | GA | 5704 | 4 | 8/19 |
| http://103.106.115.118:8097 | ID | 2349 | 4 | 10/17 |
| http://103.131.18.82:8011 | ID | 7368 | 4 | 35/146 |
| http://160.20.39.23:8090 | ID | 4581 | 4 | 44/188 |
| http://102.0.21.136:8080 | KE | 2072 | 4 | 9/23 |
| http://144.124.251.24:10261 | NL | 528 | 4 | 86/145 |
| http://200.106.124.127:999 | PE | 5309 | 4 | 4/4 |
| http://103.25.220.246:8086 | PH | 1376 | 4 | 35/114 |
| http://119.93.199.43:3128 | PH | 5614 | 4 | 12/30 |
| http://128.199.116.219:9090 | SG | 1162 | 4 | 102/132 |
| http://194.124.37.119:8080 | TR | 1858 | 4 | 13/42 |
| http://38.172.181.51:999 | VE | 3707 | 4 | 4/4 |
| http://185.226.194.24:999 | VE | 6483 | 4 | 40/134 |
| socks4://185.247.141.86:1080 | FI | 931 | 4 | 4/4 |
| socks5://79.98.32.62:1080 | TR | 1351 | 4 | 5/6 |
| http://66.186.199.33:8080 | AL | 2631 | 3 | 12/51 |
| http://27.147.169.75:12051 | BD | 3557 | 3 | 16/33 |
| http://103.150.166.160:8090 | BD | 3406 | 3 | 32/175 |
| http://147.161.246.34:12421 | CH | 7271 | 3 | 3/3 |
| http://111.192.28.24:8888 | CN | 1674 | 3 | 19/35 |
| http://114.244.211.247:8888 | CN | 4651 | 3 | 7/9 |
| http://114.245.152.162:8888 | CN | 1828 | 3 | 3/3 |
| http://114.246.197.205:8888 | CN | 2696 | 3 | 7/9 |
| http://114.249.228.162:8888 | CN | 3889 | 3 | 3/3 |
| http://114.249.233.219:8888 | CN | 3779 | 3 | 4/6 |
| http://123.113.149.18:8888 | CN | 1728 | 3 | 3/3 |
| http://123.121.120.25:8888 | CN | 1989 | 3 | 7/9 |
| http://222.128.174.236:8888 | CN | 3109 | 3 | 12/17 |
| http://45.65.137.218:999 | CO | 2272 | 3 | 90/178 |
| http://45.167.125.217:999 | CO | 2122 | 3 | 24/89 |
| http://186.96.111.214:999 | CO | 3534 | 3 | 103/202 |
| http://190.60.61.54:999 | CO | 6013 | 3 | 14/42 |
| http://38.50.165.123:999 | DO | 1986 | 3 | 54/198 |
| http://177.234.217.235:999 | EC | 7557 | 3 | 100/182 |
| http://197.164.101.14:1976 | EG | 1135 | 3 | 64/185 |
| http://197.164.101.14:1981 | EG | 3122 | 3 | 53/183 |
| http://173.212.207.102:1214 | FR | 587 | 3 | 3/3 |
| http://18.175.170.244:23666 | GB | 2243 | 3 | 45/125 |
| http://103.145.34.133:1111 | ID | 3554 | 3 | 36/204 |
| http://103.153.63.115:8080 | ID | 3696 | 3 | 12/45 |
| http://103.166.124.227:8080 | ID | 7515 | 3 | 33/146 |
| http://103.171.245.124:8090 | ID | 4785 | 3 | 13/50 |
| http://103.173.162.237:8818 | ID | 2217 | 3 | 22/103 |
| http://103.174.237.190:3125 | ID | 3890 | 3 | 40/195 |
| http://103.178.3.0:8080 | ID | 7735 | 3 | 3/3 |
