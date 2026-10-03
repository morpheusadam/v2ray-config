# Proxy status

Generated 2026-10-03T17:03:35Z by `harvest.py`.

- **2331** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4953** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 134/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3005 |
| http | 1943 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 2656 |
| ID | 546 |
| ?? | 282 |
| US | 116 |
| RU | 89 |
| CN | 87 |
| PH | 87 |
| MX | 75 |
| CO | 73 |
| BD | 56 |
| IN | 50 |
| TR | 47 |
| EC | 45 |
| BR | 43 |
| VE | 37 |
| DE | 36 |
| VN | 35 |
| SG | 34 |
| DO | 33 |
| KH | 32 |
| AR | 27 |
| JP | 27 |
| CA | 26 |
| HK | 26 |
| CL | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 2 | 2026-10-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 36 | 36 | 13 | 2026-10-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 75 | 75 | 30 | 2026-10-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 75 | 75 | 15 | 2026-10-03 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 118 | 118 | 28 | 2026-10-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-10-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 171 | 171 | 53 | 2026-10-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 326 | 326 | 97 | 2026-10-03 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 457 | 2026-10-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 646 | 646 | 248 | 2026-10-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-10-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-10-03 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1887 | 1883 | 0 | 2026-10-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2401 | 2399 | 654 | 2026-10-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2493 | 2491 | 1742 | 2026-10-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3965 | 3963 | 1130 | 2026-10-03 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 39561 | 39561 | 23361 | 2026-10-03 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 45621 | 45620 | 2231 | 2026-10-03 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 863 | 94 | 107/108 |
| http://95.3.69.222:8080 | TR | 1197 | 63 | 105/108 |
| http://190.0.246.211:4040 | CO | 740 | 28 | 95/108 |
| http://34.43.46.91:80 | US | 418 | 25 | 104/108 |
| http://190.0.246.210:4040 | CO | 576 | 24 | 96/107 |
| http://103.237.102.191:11111 | DE | 704 | 24 | 102/108 |
| http://18.157.123.132:3128 | DE | 521 | 23 | 55/69 |
| http://34.43.46.91:443 | US | 301 | 21 | 102/108 |
| http://149.130.173.58:9443 | CO | 386 | 19 | 19/19 |
| http://43.173.120.13:8899 | US | 1186 | 19 | 19/19 |
| http://45.186.6.104:3128 | EC | 2696 | 13 | 81/86 |
| http://185.191.239.248:3128 | CH | 6462 | 12 | 78/107 |
| socks5://101.36.104.239:10808 | JP | 1319 | 12 | 91/108 |
| http://190.97.241.106:999 | VE | 5634 | 11 | 64/92 |
| http://222.128.172.158:8888 | CN | 2105 | 10 | 36/73 |
| http://5.129.254.5:8888 | RU | 1409 | 9 | 54/63 |
| http://5.129.254.49:8888 | RU | 1639 | 9 | 55/63 |
| http://5.129.254.51:8888 | RU | 1010 | 9 | 55/63 |
| http://5.129.254.60:8888 | RU | 1184 | 9 | 54/62 |
| http://5.129.254.70:8888 | RU | 1999 | 9 | 55/63 |
| http://5.129.254.129:8888 | RU | 2030 | 9 | 60/69 |
| http://5.129.254.154:8888 | RU | 1038 | 9 | 51/59 |
| http://104.248.151.93:9090 | SG | 1236 | 9 | 9/9 |
| http://154.59.56.78:999 | VE | 4017 | 9 | 44/64 |
| http://159.223.41.216:9090 | SG | 1617 | 8 | 47/68 |
| http://154.59.56.74:999 | VE | 3526 | 8 | 50/71 |
| socks5://212.77.75.25:1088 | IT | 853 | 8 | 8/8 |
| http://189.84.157.245:3126 | BR | 7967 | 7 | 7/7 |
| socks5://101.36.104.46:10808 | JP | 1266 | 7 | 95/108 |
| http://187.102.219.64:999 | AR | 7331 | 6 | 23/47 |
| http://103.162.54.18:8181 | ID | 7451 | 6 | 6/6 |
| http://128.199.254.13:9090 | SG | 1243 | 6 | 29/37 |
| http://129.226.89.151:80 | SG | 1170 | 6 | 37/55 |
| socks5://59.152.97.233:1080 | BD | 5245 | 6 | 63/106 |
| socks5://141.148.206.170:1088 | IN | 2323 | 6 | 19/28 |
| socks5://5.255.113.177:1080 | NL | 904 | 6 | 6/6 |
| socks5://5.255.123.162:1080 | NL | 606 | 6 | 30/91 |
| socks5://171.25.158.95:1080 | SE | 2148 | 6 | 18/23 |
| http://120.232.115.57:17981 | CN | 1569 | 5 | 26/33 |
| http://189.51.168.165:999 | MX | 421 | 5 | 19/20 |
| http://178.128.146.125:10000 | US | 99 | 5 | 5/5 |
| socks4://185.112.83.80:1080 | FI | 817 | 5 | 12/13 |
| socks5://213.199.47.140:1080 | FR | 2382 | 5 | 60/74 |
| socks5://47.238.126.208:1080 | HK | 1521 | 5 | 12/13 |
| socks5://45.74.31.42:8998 | NL | 2235 | 5 | 5/5 |
| socks5://85.209.156.148:1080 | US | 6480 | 5 | 42/79 |
| http://101.251.204.174:8080 | CN | 7633 | 4 | 51/94 |
| http://114.249.225.156:8888 | CN | 2275 | 4 | 16/30 |
| http://103.119.19.218:3128 | CZ | 4805 | 4 | 19/21 |
| http://177.234.221.204:999 | EC | 1698 | 4 | 8/11 |
| http://185.73.39.118:9999 | GB | 551 | 4 | 4/4 |
| http://103.144.54.73:8082 | ID | 4633 | 4 | 28/53 |
| http://110.76.144.119:8082 | ID | 1664 | 4 | 7/9 |
| http://160.22.206.154:8082 | ID | 1661 | 4 | 7/9 |
| http://165.101.43.43:8080 | ID | 3779 | 4 | 18/81 |
| http://5.129.254.243:8888 | RU | 1633 | 4 | 4/4 |
| http://130.110.103.245:3128 | SA | 1290 | 4 | 102/108 |
| http://89.43.133.235:8080 | SY | 3613 | 4 | 11/23 |
| http://107.167.18.122:443 | US | 337 | 4 | 56/60 |
| http://43.109.48.179:9999 | VN | 1674 | 4 | 32/106 |
| socks5://38.49.210.79:40000 | CA | 5263 | 4 | 46/108 |
| socks5://49.13.22.249:10805 | DE | 2751 | 4 | 16/26 |
| socks5://202.47.180.112:1080 | HK | 5030 | 4 | 6/14 |
| socks5://110.235.240.223:1080 | KH | 3203 | 4 | 22/107 |
| socks5://202.62.55.95:1080 | KH | 4999 | 4 | 22/94 |
| socks5://121.169.46.116:1090 | KR | 2313 | 4 | 73/108 |
| socks5://45.74.31.30:10246 | NL | 3925 | 4 | 4/4 |
| socks5://45.74.31.30:13024 | NL | 4146 | 4 | 4/4 |
| socks5://45.74.31.30:8013 | NL | 2140 | 4 | 6/31 |
| socks5://45.74.31.47:5552 | NL | 4440 | 4 | 4/4 |
| socks5://45.74.31.50:4318 | NL | 7110 | 4 | 6/10 |
| socks5://79.137.198.71:7777 | NL | 3406 | 4 | 5/8 |
| socks5://83.147.217.103:1080 | US | 203 | 4 | 28/31 |
| http://180.149.44.182:3128 | AZ | 1024 | 3 | 3/3 |
| http://103.153.211.221:8080 | BD | 4874 | 3 | 5/8 |
| http://103.204.209.126:8080 | BD | 7463 | 3 | 9/32 |
| http://201.71.24.65:8082 | BR | 7649 | 3 | 17/97 |
| http://144.217.82.40:8089 | CA | 133 | 3 | 24/44 |
| http://184.75.221.82:3118 | CA | 220 | 3 | 64/73 |
| http://114.249.230.202:8888 | CN | 1684 | 3 | 19/31 |
| http://114.254.48.23:8888 | CN | 1657 | 3 | 31/61 |
| http://123.121.123.115:8888 | CN | 3378 | 3 | 17/32 |
| http://123.121.142.252:8888 | CN | 1841 | 3 | 17/30 |
| http://123.121.208.55:8888 | CN | 6681 | 3 | 25/61 |
| http://177.234.217.43:999 | EC | 6205 | 3 | 26/81 |
| http://41.65.55.27:1981 | EG | 3934 | 3 | 16/48 |
| http://84.36.141.180:1976 | EG | 4302 | 3 | 31/94 |
| http://65.109.215.187:8090 | FI | 684 | 3 | 3/3 |
| http://176.111.37.216:39811 | HK | 879 | 3 | 88/108 |
| http://34.101.184.164:3128 | ID | 2440 | 3 | 6/13 |
| http://38.226.243.61:8080 | ID | 3014 | 3 | 5/11 |
| http://103.122.64.232:8080 | ID | 7789 | 3 | 8/19 |
| http://103.139.126.85:8080 | ID | 7275 | 3 | 14/88 |
| http://103.158.210.80:8082 | ID | 2653 | 3 | 23/98 |
| http://157.15.1.190:8080 | ID | 2573 | 3 | 7/29 |
| http://202.136.82.219:8080 | ID | 4686 | 3 | 28/106 |
| http://161.248.176.17:8080 | IN | 7913 | 3 | 10/45 |
| http://180.194.103.158:8082 | PH | 6744 | 3 | 3/3 |
| http://203.177.217.222:8082 | PH | 6064 | 3 | 28/53 |
| http://43.153.195.69:80 | SG | 1138 | 3 | 30/48 |
