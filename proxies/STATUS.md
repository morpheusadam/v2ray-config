# Proxy status

Generated 2026-09-29T23:10:56Z by `harvest.py`.

- **2567** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4650** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39709** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 166/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2474 |
| http | 2172 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 2197 |
| ID | 560 |
| ?? | 170 |
| US | 149 |
| CN | 125 |
| RU | 86 |
| CO | 84 |
| PH | 84 |
| MX | 75 |
| IN | 67 |
| VE | 60 |
| BR | 59 |
| BD | 56 |
| TR | 51 |
| DE | 50 |
| EC | 50 |
| VN | 41 |
| PK | 39 |
| FR | 35 |
| SG | 35 |
| JP | 32 |
| HK | 31 |
| DO | 29 |
| ZA | 25 |
| AR | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-09-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 81 | 81 | 41 | 2026-09-29 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 52 | 2026-09-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 89 | 2026-09-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 185 | 185 | 41 | 2026-09-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 305 | 305 | 130 | 2026-09-29 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 412 | 412 | 168 | 2026-09-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 482 | 482 | 235 | 2026-09-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 955 | 955 | 243 | 2026-09-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1132 | 2026-09-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1585 | 2026-09-29 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1965 | 1964 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2769 | 2768 | 701 | 2026-09-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3189 | 3187 | 2107 | 2026-09-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3612 | 3611 | 887 | 2026-09-29 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 31892 | 31892 | 17474 | 2026-09-29 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 39085 | 39084 | 2168 | 2026-09-29 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 729 | 87 | 100/101 |
| http://95.3.69.222:8080 | TR | 1351 | 56 | 98/101 |
| http://190.0.246.213:4040 | CO | 479 | 30 | 59/66 |
| http://213.111.146.36:18080 | NL | 486 | 30 | 33/38 |
| http://190.0.246.211:4040 | CO | 1051 | 21 | 88/101 |
| http://34.43.46.91:80 | US | 440 | 18 | 97/101 |
| http://190.0.246.210:4040 | CO | 625 | 17 | 89/100 |
| http://103.237.102.191:11111 | DE | 789 | 17 | 95/101 |
| http://18.157.123.132:3128 | DE | 513 | 16 | 48/62 |
| socks5://107.167.18.122:443 | US | 388 | 16 | 51/53 |
| socks5://144.91.121.61:1088 | FR | 1114 | 15 | 87/101 |
| http://34.43.46.91:443 | US | 781 | 14 | 95/101 |
| http://189.51.168.165:999 | MX | 731 | 13 | 13/13 |
| http://149.130.173.58:9443 | CO | 549 | 12 | 12/12 |
| http://43.173.120.13:8899 | US | 384 | 12 | 12/12 |
| http://3.212.18.54:3128 | US | 92 | 11 | 11/11 |
| socks5://171.25.158.95:1080 | SE | 6127 | 11 | 12/16 |
| http://36.137.204.11:8002 | CN | 4301 | 10 | 13/17 |
| http://185.195.71.218:18080 | CH | 1273 | 9 | 29/38 |
| http://103.119.19.218:3128 | CZ | 572 | 9 | 13/14 |
| http://186.5.94.206:999 | EC | 3876 | 9 | 60/63 |
| http://37.59.125.131:8888 | FR | 1184 | 9 | 80/101 |
| http://43.159.54.178:80 | SG | 1169 | 9 | 16/21 |
| http://107.150.41.226:18080 | US | 244 | 9 | 37/38 |
| http://172.236.242.244:3128 | US | 350 | 9 | 9/9 |
| socks5://144.76.61.252:1080 | DE | 2257 | 8 | 11/14 |
| socks5://154.201.71.12:2080 | HK | 1441 | 8 | 9/10 |
| http://197.224.185.3:3128 | MU | 2090 | 7 | 63/69 |
| http://128.199.254.13:9090 | SG | 1411 | 7 | 23/30 |
| http://129.226.89.151:80 | SG | 1161 | 7 | 31/48 |
| socks5://121.169.46.116:1090 | KR | 2321 | 7 | 68/101 |
| socks5://174.138.189.26:2001 | US | 97 | 7 | 7/7 |
| http://184.75.221.82:3118 | CA | 221 | 6 | 58/66 |
| http://144.76.61.252:3128 | DE | 1576 | 6 | 12/14 |
| http://45.186.6.104:3128 | EC | 2647 | 6 | 74/79 |
| http://49.147.104.23:8082 | PH | 3198 | 6 | 6/6 |
| http://24.52.147.103:5999 | US | 1391 | 6 | 8/9 |
| socks5://5.75.133.113:10801 | DE | 2845 | 6 | 39/67 |
| socks5://185.112.83.80:1080 | FI | 5451 | 6 | 6/6 |
| socks5://47.238.126.208:1080 | HK | 1365 | 6 | 6/6 |
| http://187.102.219.34:999 | AR | 7379 | 5 | 23/52 |
| http://185.191.239.248:3128 | CH | 736 | 5 | 71/100 |
| http://1.15.53.214:8888 | CN | 1713 | 5 | 24/95 |
| http://47.103.30.64:8080 | CN | 4329 | 5 | 13/34 |
| http://111.192.24.82:8888 | CN | 2128 | 5 | 7/20 |
| http://123.121.122.28:8888 | CN | 7420 | 5 | 30/50 |
| http://123.121.208.55:8888 | CN | 1501 | 5 | 20/54 |
| http://221.221.154.156:8888 | CN | 6406 | 5 | 21/61 |
| http://153.51.241.50:999 | MX | 2541 | 5 | 52/98 |
| http://49.229.100.235:8080 | TH | 1622 | 5 | 25/49 |
| http://61.91.162.126:8080 | TH | 1542 | 5 | 35/44 |
| http://103.10.231.189:8080 | TH | 1840 | 5 | 60/86 |
| http://3.235.0.113:29303 | US | 754 | 5 | 9/17 |
| http://193.104.179.115:3128 | UZ | 1794 | 5 | 48/66 |
| socks5://101.36.104.239:10808 | JP | 1470 | 5 | 84/101 |
| http://16.26.208.68:18596 | AU | 3156 | 4 | 19/66 |
| http://15.223.187.219:35507 | CA | 666 | 4 | 5/14 |
| http://38.7.195.55:999 | CL | 5613 | 4 | 28/75 |
| http://47.107.107.24:80 | CN | 1934 | 4 | 41/69 |
| http://47.121.139.13:3128 | CN | 5343 | 4 | 51/100 |
| http://114.244.214.18:8888 | CN | 1721 | 4 | 13/24 |
| http://114.244.223.68:8888 | CN | 1463 | 4 | 33/64 |
| http://221.221.154.122:8888 | CN | 1475 | 4 | 19/54 |
| http://67.207.78.208:3128 | DE | 2095 | 4 | 11/14 |
| http://129.212.171.38:3128 | DE | 4343 | 4 | 4/4 |
| http://134.199.191.115:3128 | DE | 510 | 4 | 12/13 |
| http://209.38.115.253:3128 | DE | 497 | 4 | 10/13 |
| http://34.88.38.81:9443 | FI | 587 | 4 | 44/66 |
| http://35.228.49.168:9443 | FI | 636 | 4 | 25/38 |
| http://91.134.141.4:3128 | FR | 2223 | 4 | 54/62 |
| http://43.155.62.157:443 | HK | 1138 | 4 | 4/4 |
| http://176.111.37.216:39811 | HK | 1066 | 4 | 82/101 |
| http://103.77.206.114:3128 | ID | 1401 | 4 | 4/4 |
| http://202.154.19.50:3125 | ID | 7335 | 4 | 13/70 |
| http://34.131.37.209:40001 | IN | 2809 | 4 | 4/4 |
| http://65.20.79.228:40000 | IN | 4664 | 4 | 4/4 |
| http://111.92.88.27:3128 | IN | 7342 | 4 | 11/70 |
| http://52.195.147.51:3128 | JP | 5319 | 4 | 17/65 |
| http://212.252.73.66:8080 | TR | 3167 | 4 | 6/14 |
| http://136.114.233.244:3128 | US | 888 | 4 | 5/6 |
| http://90.156.196.230:3128 | UZ | 1986 | 4 | 4/4 |
| http://195.158.8.123:3128 | UZ | 1832 | 4 | 65/99 |
| http://190.97.229.118:999 | VE | 2798 | 4 | 48/91 |
| http://190.97.241.106:999 | VE | 526 | 4 | 57/85 |
| http://113.161.93.6:8080 | VN | 3731 | 4 | 11/25 |
| http://16.28.101.55:2080 | ZA | 2774 | 4 | 10/41 |
| socks5://185.133.239.244:16299 | DE | 6422 | 4 | 21/99 |
| socks5://109.123.251.109:1080 | FR | 2323 | 4 | 56/101 |
| socks5://123.58.219.171:10808 | HK | 1628 | 4 | 78/101 |
| socks5://45.74.31.23:14518 | NL | 5542 | 4 | 6/17 |
| socks5://45.74.31.42:4861 | NL | 5670 | 4 | 4/4 |
| socks5://45.74.31.50:12425 | NL | 3512 | 4 | 5/16 |
| socks5://193.25.215.182:22222 | US | 1116 | 4 | 90/101 |
| http://16.51.5.77:8367 | AU | 2674 | 3 | 3/3 |
| http://103.150.166.160:8090 | BD | 7197 | 3 | 11/63 |
| http://38.7.195.49:999 | CL | 5592 | 3 | 29/75 |
| http://47.107.82.96:30051 | CN | 1923 | 3 | 52/94 |
| http://61.149.132.196:8888 | CN | 1440 | 3 | 19/46 |
| http://114.250.195.77:8888 | CN | 2195 | 3 | 24/66 |
| http://114.252.15.106:8888 | CN | 3478 | 3 | 30/54 |
