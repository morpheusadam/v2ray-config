# Proxy status

Generated 2026-10-03T22:25:18Z by `harvest.py`.

- **1864** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5053** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39762** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 149/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3111 |
| http | 1937 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 2731 |
| ID | 563 |
| ?? | 337 |
| US | 110 |
| PH | 94 |
| RU | 87 |
| CO | 78 |
| CN | 77 |
| MX | 75 |
| BD | 59 |
| TR | 50 |
| IN | 46 |
| EC | 45 |
| BR | 44 |
| VN | 36 |
| VE | 35 |
| DE | 32 |
| PK | 31 |
| SG | 31 |
| KH | 30 |
| DO | 28 |
| AR | 26 |
| EG | 24 |
| SY | 24 |
| HK | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 1 | 2026-10-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 32 | 32 | 15 | 2026-10-03 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-10-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 102 | 102 | 25 | 2026-10-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 113 | 113 | 22 | 2026-10-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 121 | 121 | 37 | 2026-10-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 74 | 2026-10-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 253 | 253 | 63 | 2026-10-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 254 | 254 | 31 | 2026-10-03 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 452 | 452 | 161 | 2026-10-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1145 | 2026-10-03 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1743 | 1740 | 146 | 2026-10-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1586 | 2026-10-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2317 | 2315 | 695 | 2026-10-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2702 | 2700 | 1799 | 2026-10-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 5174 | 5172 | 1678 | 2026-10-03 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 40115 | 40115 | 23001 | 2026-10-03 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 46354 | 46353 | 2179 | 2026-10-03 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 676 | 95 | 108/109 |
| http://95.3.69.222:8080 | TR | 1546 | 64 | 106/109 |
| http://190.0.246.211:4040 | CO | 929 | 29 | 96/109 |
| http://34.43.46.91:80 | US | 740 | 26 | 105/109 |
| http://190.0.246.210:4040 | CO | 857 | 25 | 97/108 |
| http://103.237.102.191:11111 | DE | 731 | 25 | 103/109 |
| http://18.157.123.132:3128 | DE | 581 | 24 | 56/70 |
| http://34.43.46.91:443 | US | 696 | 22 | 103/109 |
| http://149.130.173.58:9443 | CO | 455 | 20 | 20/20 |
| http://43.173.120.13:8899 | US | 1543 | 20 | 20/20 |
| http://45.186.6.104:3128 | EC | 607 | 14 | 82/87 |
| http://185.191.239.248:3128 | CH | 2963 | 13 | 79/108 |
| socks5://101.36.104.239:10808 | JP | 1444 | 13 | 92/109 |
| http://190.97.241.106:999 | VE | 589 | 12 | 65/93 |
| http://5.129.254.5:8888 | RU | 1236 | 10 | 55/64 |
| http://5.129.254.49:8888 | RU | 1339 | 10 | 56/64 |
| http://5.129.254.51:8888 | RU | 2205 | 10 | 56/64 |
| http://5.129.254.60:8888 | RU | 1341 | 10 | 55/63 |
| http://5.129.254.70:8888 | RU | 2373 | 10 | 56/64 |
| http://5.129.254.129:8888 | RU | 2435 | 10 | 61/70 |
| http://5.129.254.154:8888 | RU | 1568 | 10 | 52/60 |
| http://104.248.151.93:9090 | SG | 1106 | 10 | 10/10 |
| http://159.223.41.216:9090 | SG | 1086 | 9 | 48/69 |
| socks5://212.77.75.25:1088 | IT | 775 | 9 | 9/9 |
| http://189.84.157.245:3126 | BR | 4660 | 8 | 8/8 |
| http://128.199.254.13:9090 | SG | 1088 | 7 | 30/38 |
| socks5://5.255.123.162:1080 | NL | 1716 | 7 | 31/92 |
| socks5://171.25.158.95:1080 | SE | 1246 | 7 | 19/24 |
| http://120.232.115.57:17981 | CN | 2319 | 6 | 27/34 |
| http://189.51.168.165:999 | MX | 387 | 6 | 20/21 |
| http://178.128.146.125:10000 | US | 546 | 6 | 6/6 |
| socks4://185.112.83.80:1080 | FI | 1492 | 6 | 13/14 |
| socks5://213.199.47.140:1080 | FR | 1516 | 6 | 61/75 |
| socks5://47.238.126.208:1080 | HK | 1269 | 6 | 13/14 |
| socks5://45.74.31.42:8998 | NL | 3825 | 6 | 6/6 |
| socks5://85.209.156.148:1080 | US | 1964 | 6 | 43/80 |
| http://114.249.225.156:8888 | CN | 1801 | 5 | 17/31 |
| http://103.119.19.218:3128 | CZ | 2641 | 5 | 20/22 |
| http://103.144.54.73:8082 | ID | 2438 | 5 | 29/54 |
| http://110.76.144.119:8082 | ID | 7463 | 5 | 8/10 |
| http://5.129.254.243:8888 | RU | 963 | 5 | 5/5 |
| socks5://121.169.46.116:1090 | KR | 1617 | 5 | 74/109 |
| socks5://79.137.198.71:7777 | NL | 781 | 5 | 6/9 |
| socks5://83.147.217.103:1080 | US | 193 | 5 | 29/32 |
| socks5://107.167.18.122:443 | US | 394 | 5 | 57/61 |
| http://103.204.209.126:8080 | BD | 5713 | 4 | 10/33 |
| http://201.71.24.65:8082 | BR | 3232 | 4 | 18/98 |
| http://184.75.221.82:3118 | CA | 135 | 4 | 65/74 |
| http://114.249.230.202:8888 | CN | 1407 | 4 | 20/32 |
| http://123.121.123.115:8888 | CN | 2154 | 4 | 18/33 |
| http://177.234.217.43:999 | EC | 7427 | 4 | 27/82 |
| http://176.111.37.216:39811 | HK | 953 | 4 | 89/109 |
| http://103.139.126.85:8080 | ID | 3453 | 4 | 15/89 |
| http://103.158.210.80:8082 | ID | 1457 | 4 | 24/99 |
| http://202.136.82.219:8080 | ID | 3573 | 4 | 29/107 |
| http://203.177.217.222:8082 | PH | 2615 | 4 | 29/54 |
| http://43.153.195.69:80 | SG | 2360 | 4 | 31/49 |
| http://104.218.199.245:16062 | US | 6627 | 4 | 6/21 |
| socks5://5.75.133.113:10805 | DE | 3785 | 4 | 11/27 |
| socks5://123.58.219.171:10808 | HK | 1736 | 4 | 83/109 |
| socks5://45.74.31.23:4324 | NL | 754 | 4 | 4/4 |
| socks5://45.74.31.47:5798 | NL | 1928 | 4 | 5/16 |
| socks5://82.23.173.223:1080 | NL | 4116 | 4 | 5/6 |
| socks5://8.219.245.123:1080 | SG | 5832 | 4 | 7/18 |
| http://114.248.179.223:8888 | CN | 3153 | 3 | 28/77 |
| http://119.188.131.55:17981 | CN | 1953 | 3 | 51/109 |
| http://123.121.122.28:8888 | CN | 2001 | 3 | 36/58 |
| http://222.128.171.2:8888 | CN | 7100 | 3 | 33/61 |
| http://181.78.17.131:999 | CO | 2680 | 3 | 31/106 |
| http://181.79.57.57:8080 | CO | 7228 | 3 | 5/10 |
| http://190.0.246.213:4040 | CO | 856 | 3 | 66/74 |
| http://200.10.30.5:8083 | CO | 3130 | 3 | 35/98 |
| http://38.75.82.213:999 | DO | 4811 | 3 | 31/103 |
| http://181.188.203.40:999 | EC | 4640 | 3 | 5/6 |
| http://41.33.245.138:1981 | EG | 986 | 3 | 13/39 |
| http://45.240.232.62:8080 | EG | 4185 | 3 | 33/95 |
| http://45.245.208.181:8080 | EG | 1273 | 3 | 5/13 |
| http://103.130.61.61:8081 | ID | 2722 | 3 | 85/109 |
| http://103.132.41.198:7777 | ID | 3518 | 3 | 5/19 |
| http://103.189.117.82:1111 | ID | 3645 | 3 | 7/22 |
| http://160.19.18.115:3127 | ID | 5647 | 3 | 11/56 |
| http://160.19.19.227:8080 | ID | 7487 | 3 | 16/86 |
| http://65.20.79.228:40000 | IN | 1222 | 3 | 9/12 |
| http://37.239.47.74:8080 | IQ | 4581 | 3 | 5/22 |
| http://5.181.178.177:8080 | JP | 4510 | 3 | 4/10 |
| http://110.74.206.40:8181 | KH | 5588 | 3 | 19/93 |
| http://38.194.246.34:999 | MX | 3481 | 3 | 61/100 |
| http://205.164.192.115:999 | MX | 2549 | 3 | 69/107 |
| http://144.124.251.24:10000 | NL | 551 | 3 | 35/55 |
| http://144.124.251.24:10007 | NL | 619 | 3 | 35/58 |
| http://144.124.251.24:10008 | NL | 577 | 3 | 31/40 |
| http://144.124.251.24:10082 | NL | 546 | 3 | 32/57 |
| http://144.124.251.24:10084 | NL | 594 | 3 | 30/41 |
| http://144.124.251.24:10088 | NL | 526 | 3 | 30/41 |
| http://144.124.251.24:10104 | NL | 642 | 3 | 31/41 |
| http://144.124.251.24:10176 | NL | 732 | 3 | 35/57 |
| http://144.124.251.24:10185 | NL | 641 | 3 | 32/41 |
| http://144.124.251.24:10187 | NL | 530 | 3 | 31/55 |
| http://144.124.251.24:10216 | NL | 558 | 3 | 36/58 |
| http://144.124.251.24:10226 | NL | 684 | 3 | 30/40 |
