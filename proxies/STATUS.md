# Proxy status

Generated 2026-11-21T20:10:04Z by `harvest.py`.

- **2407** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4142** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **27305** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 144/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3598 |
| socks5 | 539 |
| socks4 | 5 |

| country | entries |
|---|---|
| ID | 1050 |
| ?? | 686 |
| NL | 328 |
| PH | 173 |
| CO | 159 |
| MX | 151 |
| VE | 101 |
| US | 100 |
| TR | 99 |
| BR | 93 |
| TH | 89 |
| IN | 78 |
| RU | 77 |
| EC | 63 |
| BD | 62 |
| AR | 54 |
| ZA | 46 |
| DO | 45 |
| PK | 39 |
| CN | 36 |
| PE | 34 |
| EG | 32 |
| VN | 30 |
| SG | 28 |
| DE | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 3 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 59 | 59 | 12 | 2026-11-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 104 | 104 | 18 | 2026-11-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 36 | 2026-11-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 60 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 314 | 314 | 42 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 382 | 382 | 97 | 2026-11-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 416 | 416 | 278 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 981 | 981 | 178 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1120 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2005 | 2005 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2724 | 2724 | 762 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2732 | 2732 | 429 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3186 | 3186 | 1761 | 2026-11-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5643 | 5643 | 4408 | 2026-11-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12371 | 12371 | 2228 | 2026-11-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1226 | 76 | 186/205 |
| http://130.110.103.245:3128 | SA | 1293 | 51 | 187/205 |
| http://141.94.22.37:3128 | FR | 671 | 17 | 20/21 |
| http://45.155.226.177:3128 | HK | 808 | 14 | 19/21 |
| http://4.144.146.21:80 | SG | 1041 | 12 | 88/97 |
| http://15.229.149.81:3128 | BR | 2019 | 11 | 77/115 |
| http://128.199.121.61:9090 | SG | 2842 | 11 | 98/125 |
| socks5://193.25.215.182:22222 | US | 736 | 11 | 170/205 |
| http://103.130.61.61:8081 | ID | 6152 | 10 | 170/205 |
| http://34.43.46.91:80 | US | 310 | 10 | 198/205 |
| socks5://45.61.129.165:9050 | US | 1297 | 10 | 157/205 |
| socks5://46.246.12.31:1080 | ?? | 2958 | 10 | 10/10 |
| http://15.229.149.81:1080 | BR | 1854 | 9 | 61/107 |
| http://103.176.96.225:8082 | ID | 5688 | 9 | 55/150 |
| http://189.51.168.164:999 | MX | 5188 | 9 | 37/41 |
| http://104.248.151.93:9090 | SG | 1046 | 9 | 74/106 |
| http://20.98.234.24:8080 | ?? | 227 | 9 | 9/9 |
| socks5://69.55.49.177:38182 | US | 485 | 9 | 49/60 |
| http://103.237.102.191:11111 | DE | 755 | 8 | 192/205 |
| http://201.46.86.37:8080 | MX | 1470 | 8 | 15/39 |
| http://172.235.157.127:3128 | ?? | 810 | 8 | 8/8 |
| http://45.186.6.104:3128 | EC | 601 | 7 | 173/183 |
| http://103.133.26.50:8080 | ID | 1426 | 7 | 71/106 |
| http://103.133.26.72:8080 | ID | 1343 | 7 | 79/131 |
| http://103.133.26.73:3128 | ID | 1471 | 7 | 95/183 |
| http://103.158.210.80:8082 | ID | 3795 | 7 | 66/195 |
| http://110.74.195.34:25 | KH | 3302 | 7 | 69/198 |
| http://91.134.141.4:3128 | ?? | 640 | 7 | 7/7 |
| socks5://103.119.1.160:5555 | HK | 2628 | 7 | 15/20 |
| socks5://103.124.172.134:1080 | ?? | 4549 | 7 | 7/7 |
| http://181.78.195.136:999 | EC | 1651 | 6 | 35/61 |
| http://45.245.208.180:8080 | EG | 3721 | 6 | 54/78 |
| http://103.86.117.23:8080 | ID | 2468 | 6 | 39/125 |
| http://140.238.32.108:3128 | JP | 1531 | 6 | 121/204 |
| http://185.238.238.49:58080 | PL | 1234 | 6 | 80/199 |
| http://165.154.162.73:8888 | US | 3140 | 6 | 136/205 |
| http://154.59.56.76:999 | VE | 5759 | 6 | 119/165 |
| http://217.142.139.207:8085 | ?? | 4669 | 6 | 7/8 |
| http://187.102.219.32:999 | AR | 1513 | 5 | 80/204 |
| http://200.10.30.5:8083 | CO | 2676 | 5 | 64/194 |
| http://54.36.150.233:3128 | FR | 681 | 5 | 18/27 |
| http://38.199.88.1:999 | GT | 468 | 5 | 16/25 |
| http://103.133.24.75:8080 | ID | 3272 | 5 | 21/94 |
| http://124.108.19.6:9292 | IN | 4603 | 5 | 9/31 |
| http://161.49.87.222:8095 | PH | 2386 | 5 | 27/101 |
| http://38.51.206.73:999 | VE | 4336 | 5 | 12/26 |
| http://154.59.56.72:999 | VE | 2624 | 5 | 121/164 |
| http://45.66.156.107:8081 | ?? | 217 | 5 | 5/5 |
| http://49.151.179.5:8082 | ?? | 2596 | 5 | 5/5 |
| http://114.253.7.197:8888 | ?? | 6591 | 5 | 5/5 |
| http://119.94.185.43:8082 | ?? | 5338 | 5 | 5/5 |
| http://125.25.53.180:8080 | ?? | 3426 | 5 | 5/5 |
| http://147.161.246.34:12544 | ?? | 5350 | 5 | 5/5 |
| http://147.161.246.34:80 | ?? | 5136 | 5 | 5/5 |
| socks5://209.50.255.91:1080 | US | 526 | 5 | 58/122 |
| socks5://103.248.228.166:5555 | ?? | 1228 | 5 | 7/8 |
| http://181.191.14.5:8080 | BR | 4181 | 4 | 29/195 |
| http://204.157.251.178:999 | DO | 5557 | 4 | 18/59 |
| http://177.234.217.43:999 | EC | 7137 | 4 | 65/178 |
| http://41.65.55.10:1976 | EG | 1771 | 4 | 16/64 |
| http://41.128.77.76:1981 | EG | 1133 | 4 | 73/159 |
| http://45.240.232.61:8080 | EG | 5274 | 4 | 79/185 |
| http://213.131.85.28:1976 | EG | 1112 | 4 | 12/19 |
| http://49.0.2.166:8080 | ID | 3931 | 4 | 25/88 |
| http://103.120.175.243:9191 | ID | 5100 | 4 | 13/68 |
| http://103.132.54.150:8080 | ID | 5111 | 4 | 36/139 |
| http://103.145.161.18:8080 | ID | 3018 | 4 | 8/19 |
| http://160.22.198.17:8082 | ID | 4434 | 4 | 57/197 |
| http://163.61.245.26:1452 | ID | 7212 | 4 | 13/35 |
| http://38.252.228.2:999 | MX | 6718 | 4 | 9/22 |
| http://78.14.19.3:3125 | MX | 2642 | 4 | 20/65 |
| http://189.196.45.158:999 | MX | 5730 | 4 | 24/67 |
| http://103.167.229.147:8080 | NP | 7301 | 4 | 8/20 |
| http://180.191.98.8:8080 | PH | 2535 | 4 | 11/31 |
| http://47.129.130.0:9898 | SG | 3353 | 4 | 42/122 |
| http://146.190.80.158:9090 | SG | 1050 | 4 | 93/131 |
| http://38.252.110.183:999 | VE | 5005 | 4 | 7/19 |
| http://101.96.122.196:8080 | VN | 6481 | 4 | 11/45 |
| http://20.33.10.132:80 | ZA | 6990 | 4 | 27/79 |
| http://16.5.7.5:8118 | ?? | 1842 | 4 | 4/4 |
| http://41.196.16.233:1976 | ?? | 1134 | 4 | 4/4 |
| http://102.222.240.10:9999 | ?? | 1426 | 4 | 4/4 |
| http://114.244.212.147:8888 | ?? | 4473 | 4 | 4/4 |
| http://147.161.246.34:10731 | ?? | 5022 | 4 | 4/4 |
| http://147.161.246.34:11588 | ?? | 5407 | 4 | 4/4 |
| http://147.161.246.34:12673 | ?? | 5198 | 4 | 4/4 |
| http://147.161.246.34:12720 | ?? | 5500 | 4 | 4/4 |
| socks5://101.36.104.46:10808 | JP | 1325 | 4 | 169/205 |
| socks5://101.36.104.239:10808 | JP | 1101 | 4 | 167/205 |
| http://168.194.34.196:9001 | AR | 3134 | 3 | 81/203 |
| http://187.102.219.42:999 | AR | 2747 | 3 | 113/200 |
| http://213.169.33.3:8001 | BG | 4716 | 3 | 22/121 |
| http://177.87.15.141:8080 | BR | 4142 | 3 | 11/38 |
| http://187.103.105.20:8085 | BR | 6512 | 3 | 10/22 |
| http://35.183.29.62:8181 | CA | 2739 | 3 | 52/173 |
| http://45.225.205.240:999 | CL | 4538 | 3 | 13/48 |
| http://167.249.29.105:999 | CL | 3847 | 3 | 28/93 |
| http://38.211.76.201:999 | CO | 2608 | 3 | 20/37 |
| http://181.119.84.80:999 | CO | 651 | 3 | 14/39 |
| http://186.148.180.131:999 | CO | 6003 | 3 | 6/22 |
