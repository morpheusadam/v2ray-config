# Proxy status

Generated 2026-11-26T02:25:31Z by `harvest.py`.

- **1622** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3177** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25293** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 159/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2791 |
| socks5 | 380 |
| socks4 | 6 |

| country | entries |
|---|---|
| ID | 892 |
| NL | 182 |
| PH | 154 |
| CO | 133 |
| MX | 130 |
| US | 100 |
| CN | 95 |
| IN | 84 |
| TR | 83 |
| VE | 78 |
| BR | 74 |
| CH | 73 |
| RU | 72 |
| TH | 67 |
| ?? | 57 |
| EC | 56 |
| BD | 54 |
| AR | 42 |
| DO | 41 |
| PK | 35 |
| EG | 34 |
| VN | 33 |
| DE | 32 |
| ZA | 30 |
| PE | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-11-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 146 | 146 | 41 | 2026-11-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 32 | 2026-11-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 55 | 2026-11-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 196 | 196 | 30 | 2026-11-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 253 | 253 | 24 | 2026-11-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 372 | 372 | 86 | 2026-11-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 431 | 431 | 280 | 2026-11-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 444 | 2026-11-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1576 | 1576 | 226 | 2026-11-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1116 | 2026-11-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1901 | 1901 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2145 | 2145 | 209 | 2026-11-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2568 | 2568 | 710 | 2026-11-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2970 | 2970 | 1664 | 2026-11-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5753 | 5753 | 4561 | 2026-11-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 13195 | 13195 | 2066 | 2026-11-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 750 | 85 | 195/214 |
| http://130.110.103.245:3128 | SA | 972 | 60 | 196/214 |
| http://141.94.22.37:3128 | FR | 489 | 26 | 29/30 |
| http://45.155.226.177:3128 | HK | 436 | 23 | 28/30 |
| http://4.144.146.21:80 | SG | 1165 | 21 | 97/106 |
| http://34.43.46.91:80 | US | 314 | 19 | 207/214 |
| http://189.51.168.164:999 | MX | 913 | 18 | 46/50 |
| http://20.98.234.24:8080 | US | 101 | 18 | 18/18 |
| socks5://69.55.49.177:38182 | US | 371 | 18 | 58/69 |
| http://103.237.102.191:11111 | DE | 677 | 17 | 201/214 |
| http://45.186.6.104:3128 | EC | 692 | 16 | 182/192 |
| http://103.133.26.50:8080 | ID | 1517 | 16 | 80/115 |
| http://103.133.26.73:3128 | ID | 1585 | 16 | 104/192 |
| http://147.161.246.34:80 | CH | 4888 | 14 | 14/14 |
| http://146.190.80.158:9090 | SG | 1189 | 13 | 102/140 |
| http://45.135.95.185:3128 | RU | 1333 | 12 | 12/12 |
| http://128.199.113.85:9090 | SG | 1152 | 12 | 32/45 |
| socks5://123.58.219.171:10808 | HK | 1766 | 12 | 156/214 |
| http://190.123.83.137:999 | AR | 4007 | 11 | 44/51 |
| http://103.163.80.181:8085 | ID | 1520 | 10 | 10/10 |
| http://50.238.106.26:3128 | US | 139 | 10 | 10/10 |
| http://158.247.125.5:9443 | CO | 438 | 9 | 9/9 |
| http://34.43.46.91:443 | US | 331 | 9 | 198/214 |
| http://216.125.18.67:3128 | US | 1336 | 9 | 9/9 |
| http://193.124.33.31:2052 | RU | 913 | 8 | 8/8 |
| http://103.21.150.15:3128 | VN | 1221 | 8 | 10/26 |
| http://185.191.239.248:3128 | CH | 819 | 7 | 150/213 |
| http://45.136.253.145:3128 | TH | 1254 | 7 | 12/18 |
| http://102.244.78.61:8082 | CM | 1185 | 6 | 80/103 |
| http://102.244.78.61:8083 | CM | 1186 | 6 | 80/102 |
| http://102.244.78.61:8087 | CM | 1212 | 6 | 77/104 |
| http://45.65.138.48:999 | CO | 1310 | 6 | 111/214 |
| http://177.234.217.89:999 | EC | 5449 | 6 | 25/39 |
| http://52.128.238.98:18080 | HK | 429 | 6 | 23/29 |
| http://157.66.16.45:7789 | ID | 4468 | 6 | 11/34 |
| http://31.130.153.132:3128 | KZ | 1336 | 6 | 6/6 |
| http://189.51.168.165:999 | MX | 1366 | 6 | 113/126 |
| http://144.124.251.24:10372 | NL | 667 | 6 | 95/158 |
| http://13.59.11.63:3128 | US | 382 | 6 | 6/6 |
| http://129.153.97.250:9443 | US | 407 | 6 | 6/6 |
| http://154.59.56.78:999 | VE | 3399 | 6 | 116/170 |
| http://103.81.86.170:8888 | VN | 1615 | 6 | 6/6 |
| socks5://59.11.209.162:1080 | KR | 1142 | 6 | 6/6 |
| socks5://45.141.177.0:1080 | SE | 1237 | 6 | 6/6 |
| http://190.12.150.244:999 | EC | 1244 | 5 | 156/210 |
| http://102.0.21.136:8080 | KE | 5345 | 5 | 10/24 |
| http://144.124.251.24:10261 | NL | 689 | 5 | 87/146 |
| http://200.106.124.127:999 | PE | 6828 | 5 | 5/5 |
| http://119.93.199.43:3128 | PH | 1617 | 5 | 13/31 |
| http://128.199.116.219:9090 | SG | 1146 | 5 | 103/133 |
| socks4://185.247.141.86:1080 | FI | 635 | 5 | 5/5 |
| http://147.161.246.34:12421 | CH | 4488 | 4 | 4/4 |
| http://114.244.211.247:8888 | CN | 1863 | 4 | 8/10 |
| http://114.246.197.205:8888 | CN | 1631 | 4 | 8/10 |
| http://114.249.228.162:8888 | CN | 5562 | 4 | 4/4 |
| http://123.113.149.18:8888 | CN | 2323 | 4 | 4/4 |
| http://123.121.120.25:8888 | CN | 1833 | 4 | 8/10 |
| http://45.65.137.218:999 | CO | 2137 | 4 | 91/179 |
| http://186.96.111.214:999 | CO | 4863 | 4 | 104/203 |
| http://177.234.217.235:999 | EC | 1498 | 4 | 101/183 |
| http://197.164.101.14:1976 | EG | 1526 | 4 | 65/186 |
| http://197.164.101.14:1981 | EG | 1573 | 4 | 54/184 |
| http://173.212.207.102:1214 | FR | 713 | 4 | 4/4 |
| http://103.138.185.81:83 | IN | 7053 | 4 | 27/169 |
| http://189.187.131.201:999 | MX | 3239 | 4 | 4/4 |
| http://79.98.32.137:8080 | TR | 5076 | 4 | 12/53 |
| http://38.172.160.16:999 | VE | 4842 | 4 | 97/165 |
| socks5://118.179.205.174:2080 | BD | 3084 | 4 | 4/4 |
| socks5://49.13.22.249:10806 | DE | 4898 | 4 | 38/136 |
| http://181.209.125.186:999 | AR | 4394 | 3 | 9/42 |
| http://16.5.7.5:8118 | BR | 1693 | 3 | 8/13 |
| http://102.244.78.61:8080 | CM | 1183 | 3 | 82/103 |
| http://102.244.78.61:8084 | CM | 1184 | 3 | 77/102 |
| http://102.244.78.61:8085 | CM | 1229 | 3 | 79/104 |
| http://102.244.78.61:8088 | CM | 1221 | 3 | 78/102 |
| http://102.244.78.61:8089 | CM | 1213 | 3 | 79/102 |
| http://114.244.221.178:8888 | CN | 1610 | 3 | 72/137 |
| http://114.246.192.19:8888 | CN | 7343 | 3 | 4/10 |
| http://114.249.212.245:8888 | CN | 2130 | 3 | 3/3 |
| http://114.249.231.192:8888 | CN | 2808 | 3 | 6/10 |
| http://123.115.143.194:8888 | CN | 1874 | 3 | 7/13 |
| http://177.93.33.55:999 | CO | 615 | 3 | 15/35 |
| http://177.234.217.44:999 | EC | 1915 | 3 | 48/114 |
| http://197.164.101.11:1981 | EG | 1312 | 3 | 12/31 |
| http://213.131.85.28:1976 | EG | 935 | 3 | 18/28 |
| http://51.94.221.175:1857 | ES | 2725 | 3 | 49/155 |
| http://36.95.155.74:3126 | ID | 6075 | 3 | 14/44 |
| http://103.156.15.73:8080 | ID | 6480 | 3 | 43/211 |
| http://103.158.210.80:8082 | ID | 2610 | 3 | 71/204 |
| http://103.171.82.29:8080 | ID | 1447 | 3 | 8/39 |
| http://144.124.251.24:10000 | NL | 529 | 3 | 93/160 |
| http://144.124.251.24:10187 | NL | 546 | 3 | 91/160 |
| http://144.124.251.24:10747 | NL | 705 | 3 | 14/57 |
| http://144.124.251.24:11108 | NL | 679 | 3 | 84/161 |
| http://58.69.182.53:8085 | PH | 1850 | 3 | 42/177 |
| http://180.191.142.241:8081 | PH | 4600 | 3 | 19/53 |
| http://167.172.76.176:9090 | SG | 1155 | 3 | 129/175 |
| http://190.94.212.249:999 | VE | 4635 | 3 | 20/88 |
| socks5://61.247.178.146:1080 | BD | 5188 | 3 | 20/54 |
| socks5://49.13.22.249:10802 | DE | 7421 | 3 | 53/141 |
