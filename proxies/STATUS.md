# Proxy status

Generated 2026-09-12T21:37:21Z by `harvest.py`.

- **1057** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1801** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16730** endpoints on record
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
| http | 1330 |
| socks5 | 457 |
| socks4 | 14 |

| country | entries |
|---|---|
| ID | 357 |
| NL | 208 |
| US | 109 |
| CN | 85 |
| RU | 77 |
| MX | 69 |
| CO | 66 |
| BD | 60 |
| PH | 56 |
| VE | 43 |
| BR | 42 |
| VN | 41 |
| DE | 34 |
| IN | 34 |
| SG | 33 |
| FR | 31 |
| EC | 30 |
| TH | 25 |
| CL | 22 |
| DO | 22 |
| KH | 22 |
| TR | 22 |
| EG | 21 |
| HK | 20 |
| AR | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 1 | 2026-09-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 66 | 66 | 35 | 2026-09-12 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 145 | 145 | 77 | 2026-09-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-09-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 193 | 193 | 64 | 2026-09-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 235 | 235 | 115 | 2026-09-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-12 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 339 | 339 | 128 | 2026-09-12 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 404 | 404 | 126 | 2026-09-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 429 | 429 | 138 | 2026-09-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 460 | 460 | 190 | 2026-09-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 534 | 2026-09-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-09-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1117 | 2026-09-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1602 | 2026-09-12 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1983 | 1979 | 298 | 2026-09-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2071 | 2069 | 329 | 2026-09-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2410 | 2408 | 728 | 2026-09-12 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2509 | 2509 | 1648 | 2026-09-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2615 | 2613 | 1989 | 2026-09-12 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 761 | 59 | 64/67 |
| http://34.43.46.91:80 | US | 862 | 59 | 64/67 |
| http://95.211.174.135:3128 | NL | 1522 | 53 | 66/67 |
| http://185.200.188.234:10001 | RU | 2616 | 53 | 66/67 |
| http://130.110.103.245:3128 | SA | 1344 | 53 | 65/67 |
| http://1.231.81.166:3128 | KR | 1615 | 32 | 64/67 |
| http://189.51.168.164:999 | MX | 1031 | 32 | 32/32 |
| http://176.111.37.5:39811 | HK | 941 | 27 | 61/67 |
| http://181.78.23.187:999 | CO | 632 | 24 | 34/36 |
| http://181.78.74.252:999 | CO | 670 | 24 | 56/58 |
| http://181.78.74.253:999 | CO | 686 | 24 | 56/58 |
| http://190.97.236.128:999 | VE | 694 | 24 | 55/57 |
| http://190.97.236.129:999 | VE | 669 | 24 | 55/57 |
| http://176.111.37.216:39811 | HK | 852 | 22 | 55/67 |
| http://5.129.254.49:8888 | RU | 1537 | 22 | 22/22 |
| http://5.129.254.51:8888 | RU | 1566 | 22 | 22/22 |
| http://5.129.254.70:8888 | RU | 1311 | 22 | 22/22 |
| http://95.3.69.222:8080 | TR | 1491 | 22 | 64/67 |
| http://5.129.254.60:8888 | RU | 1075 | 21 | 21/21 |
| http://5.129.254.5:8888 | RU | 1043 | 20 | 21/22 |
| http://190.97.241.106:999 | VE | 5536 | 19 | 28/51 |
| http://5.129.254.154:8888 | RU | 1041 | 18 | 18/18 |
| socks5://108.174.152.80:1080 | MX | 462 | 16 | 16/16 |
| http://45.186.6.104:3128 | EC | 591 | 15 | 44/45 |
| http://107.167.18.122:443 | US | 324 | 12 | 18/19 |
| http://103.237.102.191:11111 | DE | 1011 | 11 | 63/67 |
| socks5://83.147.216.208:1080 | FI | 909 | 11 | 17/35 |
| http://61.91.162.126:8080 | TH | 1884 | 10 | 10/10 |
| http://103.10.231.189:8080 | TH | 1566 | 10 | 35/52 |
| http://201.71.2.26:999 | VE | 7086 | 9 | 23/60 |
| socks5://144.91.111.48:1088 | FR | 2188 | 9 | 37/67 |
| socks5://101.36.104.46:10808 | JP | 1750 | 9 | 60/67 |
| socks5://45.32.160.61:1088 | US | 287 | 9 | 19/20 |
| http://108.61.213.218:80 | AU | 1235 | 8 | 8/8 |
| http://184.75.221.82:3118 | CA | 185 | 8 | 29/32 |
| http://113.45.195.147:3128 | CN | 1921 | 8 | 21/32 |
| http://5.129.254.129:8888 | RU | 1090 | 8 | 27/28 |
| http://154.59.56.72:999 | VE | 4688 | 8 | 19/26 |
| socks5://5.45.119.70:1080 | EE | 721 | 8 | 35/65 |
| socks5://144.91.121.61:1088 | FR | 2028 | 8 | 58/67 |
| http://103.130.61.61:8081 | ID | 2687 | 7 | 55/67 |
| http://197.224.185.3:3128 | MU | 1047 | 7 | 32/35 |
| http://91.134.141.4:3128 | FR | 522 | 6 | 26/28 |
| http://157.85.111.64:3128 | TH | 1301 | 6 | 29/35 |
| http://154.59.56.76:999 | VE | 7170 | 6 | 22/27 |
| socks5://43.156.84.41:10808 | SG | 2120 | 6 | 6/6 |
| socks5://144.24.47.42:1080 | US | 5705 | 6 | 33/63 |
| http://123.121.210.208:8888 | CN | 5569 | 5 | 10/19 |
| http://205.164.192.115:999 | MX | 3716 | 5 | 40/65 |
| http://159.223.41.216:9090 | SG | 1221 | 5 | 17/27 |
| http://167.172.76.176:9090 | SG | 2988 | 5 | 14/28 |
| http://70.61.188.34:3128 | US | 953 | 5 | 10/26 |
| socks5://51.178.49.241:1088 | FR | 1162 | 5 | 23/28 |
| socks5://144.126.197.184:1088 | GB | 1564 | 5 | 18/23 |
| socks5://103.75.118.84:1080 | JP | 3445 | 5 | 45/62 |
| socks5://5.130.50.118:1080 | RU | 1169 | 5 | 13/40 |
| http://185.191.239.248:3128 | CH | 1200 | 4 | 51/66 |
| http://186.5.94.206:999 | EC | 767 | 4 | 27/29 |
| http://197.164.101.13:1981 | EG | 5184 | 4 | 23/56 |
| http://103.194.46.99:8082 | ID | 6143 | 4 | 14/65 |
| http://117.236.124.166:3128 | IN | 2674 | 4 | 43/67 |
| http://43.156.199.63:8081 | SG | 3617 | 4 | 4/4 |
| http://213.163.196.45:80 | SG | 1263 | 4 | 4/4 |
| http://38.172.179.192:999 | VE | 6178 | 4 | 17/61 |
| http://154.59.56.78:999 | VE | 6757 | 4 | 14/23 |
| http://14.251.13.20:8080 | VN | 1390 | 4 | 37/39 |
| socks5://118.179.195.140:9090 | BD | 4193 | 4 | 11/18 |
| socks5://103.210.161.8:1080 | CN | 1526 | 4 | 30/40 |
| socks5://193.233.139.106:1080 | FI | 880 | 4 | 13/25 |
| socks5://109.123.251.109:1080 | FR | 4306 | 4 | 31/67 |
| socks5://213.199.47.140:1080 | FR | 1573 | 4 | 26/33 |
| socks5://123.58.219.171:10808 | HK | 2899 | 4 | 54/67 |
| socks5://103.142.255.33:69 | ID | 5236 | 4 | 22/60 |
| socks5://103.174.122.197:8199 | ID | 2082 | 4 | 23/67 |
| socks5://45.74.31.42:14215 | NL | 4238 | 4 | 4/4 |
| socks5://213.165.38.49:1080 | NL | 1217 | 4 | 16/34 |
| socks5://43.135.176.121:1080 | US | 1237 | 4 | 19/22 |
| socks5://107.150.41.226:18080 | US | 256 | 4 | 4/4 |
| socks5://162.120.16.210:1080 | US | 2281 | 4 | 7/15 |
| http://144.217.82.40:8089 | CA | 3039 | 3 | 3/3 |
| http://114.249.209.219:8888 | CN | 7690 | 3 | 14/25 |
| http://123.121.78.138:8888 | CN | 2136 | 3 | 17/32 |
| http://123.121.122.28:8888 | CN | 2016 | 3 | 11/16 |
| http://200.10.31.45:8081 | CO | 2542 | 3 | 26/64 |
| http://200.35.34.134:999 | CO | 6433 | 3 | 8/67 |
| http://41.128.77.76:1976 | EG | 2046 | 3 | 10/33 |
| http://194.113.38.196:3128 | FI | 5812 | 3 | 15/46 |
| http://167.86.104.220:80 | FR | 1820 | 3 | 3/3 |
| http://154.90.48.21:9090 | ID | 1289 | 3 | 3/3 |
| http://157.66.2.5:1111 | ID | 7931 | 3 | 7/29 |
| http://79.32.158.19:3128 | IT | 6078 | 3 | 4/14 |
| http://91.201.113.151:8888 | NL | 641 | 3 | 3/3 |
| http://160.238.65.2:3128 | NL | 571 | 3 | 17/50 |
| http://160.238.65.3:3128 | NL | 1914 | 3 | 18/49 |
| http://160.238.65.7:3128 | NL | 1789 | 3 | 18/50 |
| http://165.154.162.73:8888 | US | 4143 | 3 | 37/67 |
| http://154.59.56.73:999 | VE | 5416 | 3 | 34/39 |
| http://190.97.229.118:999 | VE | 1931 | 3 | 26/57 |
| http://190.114.245.194:999 | VE | 6067 | 3 | 11/61 |
| socks5://5.75.133.113:10808 | DE | 4603 | 3 | 21/40 |
