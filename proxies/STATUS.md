# Proxy status

Generated 2026-09-28T23:55:43Z by `harvest.py`.

- **2313** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4036** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39789** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 175/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2281 |
| http | 1746 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 2045 |
| ?? | 372 |
| ID | 336 |
| US | 160 |
| CN | 117 |
| MX | 57 |
| IN | 56 |
| CO | 50 |
| DE | 48 |
| RU | 48 |
| VE | 45 |
| BD | 40 |
| VN | 40 |
| FR | 34 |
| PH | 34 |
| BR | 33 |
| PK | 33 |
| EC | 31 |
| HK | 29 |
| JP | 29 |
| SG | 26 |
| CA | 24 |
| DO | 22 |
| ZA | 22 |
| AU | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-09-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 84 | 84 | 39 | 2026-09-28 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-09-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 120 | 120 | 40 | 2026-09-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 121 | 121 | 56 | 2026-09-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 80 | 2026-09-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 198 | 198 | 61 | 2026-09-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 397 | 397 | 244 | 2026-09-28 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 534 | 534 | 231 | 2026-09-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 579 | 579 | 333 | 2026-09-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-09-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-09-28 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1626 | 1622 | 251 | 2026-09-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-09-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2786 | 2784 | 719 | 2026-09-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3095 | 3093 | 2165 | 2026-09-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3401 | 3399 | 650 | 2026-09-28 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 28744 | 28744 | 15111 | 2026-09-28 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 36318 | 36317 | 3128 | 2026-09-28 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 876 | 85 | 98/99 |
| http://190.97.236.128:999 | VE | 670 | 56 | 87/89 |
| http://190.97.236.129:999 | VE | 671 | 56 | 87/89 |
| http://95.3.69.222:8080 | TR | 1205 | 54 | 96/99 |
| http://38.51.207.104:8080 | VE | 913 | 32 | 39/40 |
| http://190.0.246.213:4040 | CO | 485 | 28 | 57/64 |
| http://213.111.146.36:18080 | NL | 523 | 28 | 31/36 |
| http://153.51.201.35:999 | VE | 891 | 26 | 26/26 |
| socks5://83.147.217.103:1080 | US | 166 | 22 | 22/22 |
| http://190.0.246.211:4040 | CO | 2748 | 19 | 86/99 |
| http://167.172.76.176:9090 | SG | 1163 | 19 | 41/60 |
| http://34.43.46.91:80 | US | 513 | 16 | 95/99 |
| http://190.0.246.210:4040 | CO | 2488 | 15 | 87/98 |
| http://103.237.102.191:11111 | DE | 798 | 15 | 93/99 |
| http://154.59.56.73:999 | VE | 3867 | 15 | 58/71 |
| http://18.157.123.132:3128 | DE | 514 | 14 | 46/60 |
| socks4://107.167.18.122:443 | US | 327 | 14 | 49/51 |
| socks5://144.91.121.61:1088 | FR | 1619 | 13 | 85/99 |
| http://34.43.46.91:443 | US | 432 | 12 | 93/99 |
| http://189.51.168.165:999 | MX | 1694 | 11 | 11/11 |
| http://149.130.173.58:9443 | CO | 431 | 10 | 10/10 |
| http://43.173.120.13:8899 | US | 644 | 10 | 10/10 |
| http://161.22.39.58:999 | VE | 674 | 10 | 10/10 |
| http://3.212.18.54:3128 | ?? | 566 | 9 | 9/9 |
| socks5://171.25.158.95:1080 | SE | 5965 | 9 | 10/14 |
| http://36.137.204.11:8002 | CN | 5439 | 8 | 11/15 |
| http://190.12.150.244:999 | EC | 1131 | 8 | 66/95 |
| http://185.195.71.218:18080 | CH | 1072 | 7 | 27/36 |
| http://103.119.19.218:3128 | CZ | 636 | 7 | 11/12 |
| http://186.5.94.206:999 | EC | 1816 | 7 | 58/61 |
| http://37.59.125.131:8888 | FR | 1269 | 7 | 78/99 |
| http://167.86.104.220:80 | FR | 5669 | 7 | 18/35 |
| http://3.1.100.245:3128 | SG | 7280 | 7 | 8/11 |
| http://43.159.54.178:80 | SG | 1164 | 7 | 14/19 |
| http://107.150.41.226:18080 | US | 247 | 7 | 35/36 |
| http://172.236.242.244:3128 | ?? | 369 | 7 | 7/7 |
| socks5://5.75.133.113:10802 | DE | 7122 | 7 | 19/24 |
| http://119.188.131.55:17981 | CN | 4463 | 6 | 44/99 |
| http://45.86.245.81:8080 | ?? | 800 | 6 | 6/6 |
| socks4://144.76.61.252:1080 | DE | 2112 | 6 | 9/12 |
| socks5://154.201.71.12:2080 | ?? | 4832 | 6 | 7/8 |
| http://45.232.0.2:8080 | AR | 2562 | 5 | 29/97 |
| http://113.45.195.147:3128 | CN | 3206 | 5 | 40/64 |
| http://120.232.115.57:17981 | CN | 1725 | 5 | 19/24 |
| http://123.121.210.208:8888 | CN | 1233 | 5 | 23/51 |
| http://38.211.76.203:999 | CO | 7303 | 5 | 8/17 |
| http://62.141.38.35:3128 | DE | 1116 | 5 | 7/10 |
| http://197.224.185.3:3128 | MU | 2256 | 5 | 61/67 |
| http://38.194.246.34:999 | MX | 2219 | 5 | 55/90 |
| http://128.199.254.13:9090 | SG | 1443 | 5 | 21/28 |
| http://129.226.89.151:80 | SG | 1164 | 5 | 29/46 |
| http://152.42.177.32:8888 | SG | 1151 | 5 | 36/59 |
| socks5://121.169.46.116:1090 | KR | 3141 | 5 | 66/99 |
| socks5://103.88.234.239:40002 | MX | 3082 | 5 | 17/22 |
| socks5://138.124.66.226:1080 | ?? | 636 | 5 | 5/5 |
| socks5://174.138.189.26:2001 | ?? | 537 | 5 | 5/5 |
| http://184.75.221.82:3118 | CA | 206 | 4 | 56/64 |
| http://125.33.195.27:8888 | CN | 1568 | 4 | 22/45 |
| http://144.76.61.252:3128 | DE | 3721 | 4 | 10/12 |
| http://45.186.6.104:3128 | EC | 697 | 4 | 72/77 |
| http://51.170.133.249:80 | MA | 738 | 4 | 11/22 |
| http://205.164.192.115:999 | MX | 3349 | 4 | 63/97 |
| http://24.52.147.103:5999 | ?? | 3399 | 4 | 6/7 |
| http://49.147.104.23:8082 | ?? | 1676 | 4 | 4/4 |
| socks4://185.112.83.80:1080 | ?? | 1115 | 4 | 4/4 |
| socks5://36.155.23.163:10808 | CN | 1407 | 4 | 23/36 |
| socks5://5.75.133.113:10801 | DE | 5406 | 4 | 37/65 |
| socks5://45.74.31.41:13043 | NL | 3034 | 4 | 8/21 |
| socks5://45.74.31.41:17701 | NL | 4495 | 4 | 4/4 |
| socks5://45.74.31.50:10037 | NL | 4803 | 4 | 4/4 |
| socks5://43.155.143.227:1080 | ?? | 3252 | 4 | 7/8 |
| socks5://46.39.251.233:1080 | ?? | 2637 | 4 | 5/6 |
| socks5://47.238.126.208:1080 | ?? | 1355 | 4 | 4/4 |
| http://187.102.219.34:999 | AR | 1161 | 3 | 21/50 |
| http://130.162.192.208:8080 | AU | 5427 | 3 | 12/43 |
| http://200.229.76.160:3128 | BR | 4647 | 3 | 13/19 |
| http://185.191.239.248:3128 | CH | 1105 | 3 | 69/98 |
| http://1.15.53.214:8888 | CN | 1847 | 3 | 22/93 |
| http://39.106.165.196:8080 | CN | 1573 | 3 | 49/95 |
| http://47.103.30.64:8080 | CN | 1836 | 3 | 11/32 |
| http://111.192.16.130:8888 | CN | 1842 | 3 | 31/64 |
| http://111.192.16.206:8888 | CN | 2136 | 3 | 7/21 |
| http://111.192.24.82:8888 | CN | 1530 | 3 | 5/18 |
| http://111.196.31.158:8888 | CN | 1204 | 3 | 23/45 |
| http://114.244.221.178:8888 | CN | 1985 | 3 | 12/22 |
| http://114.246.207.184:8888 | CN | 1840 | 3 | 11/21 |
| http://114.246.207.186:8888 | CN | 1711 | 3 | 9/19 |
| http://114.252.13.224:8888 | CN | 1570 | 3 | 26/63 |
| http://114.254.50.97:8888 | CN | 1222 | 3 | 33/64 |
| http://123.121.122.28:8888 | CN | 6715 | 3 | 28/48 |
| http://123.121.208.55:8888 | CN | 1533 | 3 | 18/52 |
| http://221.221.144.75:8888 | CN | 1284 | 3 | 23/61 |
| http://221.221.154.156:8888 | CN | 1323 | 3 | 19/59 |
| http://221.221.157.49:8888 | CN | 1243 | 3 | 15/51 |
| http://221.221.159.97:8888 | CN | 1231 | 3 | 22/52 |
| http://221.221.163.120:8888 | CN | 1461 | 3 | 24/52 |
| http://222.128.171.2:8888 | CN | 1250 | 3 | 28/51 |
| http://200.10.30.5:8083 | CO | 5275 | 3 | 30/88 |
| http://38.50.165.123:999 | DO | 3687 | 3 | 20/84 |
| http://38.50.165.125:999 | DO | 4282 | 3 | 15/74 |
