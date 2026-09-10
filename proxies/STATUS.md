# Proxy status

Generated 2026-09-10T16:57:54Z by `harvest.py`.

- **1199** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2288** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16423** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 120/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1961 |
| socks5 | 308 |
| socks4 | 19 |

| country | entries |
|---|---|
| ID | 514 |
| US | 150 |
| CO | 94 |
| MX | 94 |
| CN | 86 |
| BD | 82 |
| NL | 73 |
| PH | 72 |
| RU | 67 |
| BR | 66 |
| IN | 62 |
| DE | 55 |
| VE | 50 |
| FR | 43 |
| VN | 41 |
| EC | 39 |
| SG | 38 |
| HK | 34 |
| JP | 34 |
| DO | 28 |
| TH | 28 |
| AR | 27 |
| CA | 27 |
| CL | 25 |
| AU | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 86 | 86 | 40 | 2026-09-10 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 119 | 119 | 59 | 2026-09-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 119 | 119 | 19 | 2026-09-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 146 | 146 | 45 | 2026-09-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 81 | 2026-09-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 264 | 264 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 283 | 283 | 58 | 2026-09-10 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 567 | 567 | 198 | 2026-09-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 589 | 589 | 246 | 2026-09-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-09-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1120 | 2026-09-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1599 | 2026-09-10 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1969 | 1965 | 371 | 2026-09-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2398 | 2396 | 200 | 2026-09-10 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2572 | 2572 | 1462 | 2026-09-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2847 | 2845 | 713 | 2026-09-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3105 | 3103 | 2346 | 2026-09-10 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1030 | 54 | 59/62 |
| http://34.43.46.91:80 | US | 1257 | 54 | 59/62 |
| http://95.211.174.135:3128 | NL | 1247 | 48 | 61/62 |
| http://185.200.188.234:10001 | RU | 4210 | 48 | 61/62 |
| http://130.110.103.245:3128 | SA | 1307 | 48 | 60/62 |
| http://64.112.184.210:3128 | US | 190 | 40 | 61/62 |
| http://1.231.81.166:3128 | KR | 1377 | 27 | 59/62 |
| http://189.51.168.164:999 | MX | 353 | 27 | 27/27 |
| socks5://193.25.215.182:22222 | US | 3882 | 25 | 58/62 |
| http://176.111.37.5:39811 | HK | 1200 | 22 | 56/62 |
| http://14.251.13.20:8080 | VN | 1429 | 22 | 33/34 |
| http://181.78.23.187:999 | CO | 815 | 19 | 29/31 |
| http://181.78.74.252:999 | CO | 827 | 19 | 51/53 |
| http://181.78.74.253:999 | CO | 816 | 19 | 51/53 |
| http://190.97.236.128:999 | VE | 529 | 19 | 50/52 |
| http://190.97.236.129:999 | VE | 644 | 19 | 50/52 |
| http://103.177.118.145:8118 | BD | 2765 | 18 | 41/43 |
| http://186.5.94.206:999 | EC | 758 | 18 | 23/24 |
| http://176.111.37.216:39811 | HK | 1155 | 17 | 50/62 |
| http://5.129.254.49:8888 | RU | 916 | 17 | 17/17 |
| http://5.129.254.51:8888 | RU | 1030 | 17 | 17/17 |
| http://5.129.254.70:8888 | RU | 939 | 17 | 17/17 |
| http://95.3.69.222:8080 | TR | 1365 | 17 | 59/62 |
| http://5.129.254.60:8888 | RU | 1020 | 16 | 16/16 |
| http://5.129.254.5:8888 | RU | 1010 | 15 | 16/17 |
| http://202.28.194.139:31280 | TH | 2283 | 15 | 59/62 |
| http://190.97.241.106:999 | VE | 1856 | 14 | 23/46 |
| http://5.129.254.154:8888 | RU | 961 | 13 | 13/13 |
| http://161.35.181.96:999 | US | 113 | 11 | 11/11 |
| socks5://108.174.152.80:1080 | MX | 7666 | 11 | 11/11 |
| http://45.186.6.104:3128 | EC | 675 | 10 | 39/40 |
| http://43.99.60.244:8089 | HK | 1216 | 10 | 11/12 |
| http://52.21.158.119:3128 | US | 185 | 10 | 14/15 |
| socks5://213.165.38.49:1080 | NL | 1121 | 10 | 12/29 |
| socks5://58.187.162.191:1083 | VN | 1816 | 10 | 10/10 |
| http://190.0.246.211:4040 | CO | 4793 | 9 | 53/62 |
| http://103.157.200.126:3128 | PK | 1148 | 9 | 15/39 |
| http://213.131.85.29:1981 | EG | 945 | 7 | 7/7 |
| http://34.88.38.81:9443 | FI | 619 | 7 | 18/27 |
| http://37.59.125.131:8888 | FR | 7525 | 7 | 48/62 |
| http://107.167.18.122:443 | US | 327 | 7 | 13/14 |
| http://210.211.113.34:80 | VN | 2748 | 7 | 29/34 |
| socks5://147.45.60.139:1082 | US | 137 | 7 | 34/53 |
| http://103.237.102.191:11111 | DE | 1197 | 6 | 58/62 |
| http://43.134.141.85:80 | SG | 1159 | 6 | 22/60 |
| socks5://83.147.216.208:1080 | FI | 876 | 6 | 12/30 |
| socks5://147.45.60.110:1082 | US | 4358 | 6 | 22/61 |
| http://111.192.19.39:8888 | CN | 1375 | 5 | 16/26 |
| http://61.91.162.126:8080 | TH | 1595 | 5 | 5/5 |
| http://103.10.231.189:8080 | TH | 1537 | 5 | 30/47 |
| http://69.87.216.54:7989 | US | 491 | 5 | 6/7 |
| socks5://59.152.97.233:1080 | BD | 3197 | 5 | 40/60 |
| http://190.0.246.213:4040 | CO | 1367 | 4 | 24/27 |
| http://167.233.169.253:1084 | DE | 1953 | 4 | 10/11 |
| http://38.44.17.142:999 | DO | 4080 | 4 | 28/55 |
| http://177.234.217.46:999 | EC | 3062 | 4 | 5/9 |
| http://213.131.85.29:1976 | EG | 992 | 4 | 6/7 |
| http://173.212.240.48:8888 | FR | 825 | 4 | 22/23 |
| http://153.51.241.50:999 | MX | 3437 | 4 | 34/59 |
| http://43.156.236.238:80 | SG | 1201 | 4 | 27/60 |
| http://195.158.22.212:3128 | UZ | 7962 | 4 | 7/21 |
| http://201.71.2.26:999 | VE | 7152 | 4 | 18/55 |
| socks5://81.0.49.104:18500 | ES | 2232 | 4 | 21/59 |
| socks5://85.117.248.36:1080 | ES | 1783 | 4 | 8/47 |
| socks5://144.91.111.48:1088 | FR | 4327 | 4 | 32/62 |
| socks5://101.36.104.46:10808 | JP | 1732 | 4 | 55/62 |
| socks5://203.189.150.44:1080 | KH | 3234 | 4 | 22/62 |
| socks5://45.32.160.61:1088 | US | 316 | 4 | 14/15 |
| http://108.61.213.218:80 | AU | 999 | 3 | 3/3 |
| http://184.75.221.82:3118 | CA | 430 | 3 | 24/27 |
| http://8.138.217.152:21001 | CN | 4191 | 3 | 40/62 |
| http://47.110.226.74:19991 | CN | 5570 | 3 | 23/60 |
| http://113.45.195.147:3128 | CN | 1679 | 3 | 16/27 |
| http://114.236.137.41:21000 | CN | 1745 | 3 | 43/62 |
| http://45.65.138.48:999 | CO | 7898 | 3 | 19/62 |
| http://152.231.27.124:999 | CO | 4826 | 3 | 9/45 |
| http://181.57.171.254:8095 | CO | 3293 | 3 | 9/44 |
| http://186.96.111.214:999 | CO | 6571 | 3 | 18/51 |
| http://167.233.169.253:1083 | DE | 2034 | 3 | 13/14 |
| http://149.2.82.179:999 | DO | 4625 | 3 | 5/31 |
| http://41.33.219.140:1981 | EG | 1086 | 3 | 16/44 |
| http://196.61.42.26:3128 | GH | 3017 | 3 | 13/30 |
| http://103.133.26.73:3128 | ID | 5542 | 3 | 7/40 |
| http://144.79.75.222:8080 | ID | 4412 | 3 | 8/44 |
| http://185.238.238.137:58080 | PL | 6371 | 3 | 19/58 |
| http://5.129.254.129:8888 | RU | 948 | 3 | 22/23 |
| http://43.128.73.106:80 | SG | 1153 | 3 | 15/57 |
| http://193.104.179.115:3128 | UZ | 5003 | 3 | 15/27 |
| http://38.51.207.104:8080 | VE | 4619 | 3 | 3/3 |
| http://154.59.56.72:999 | VE | 3859 | 3 | 14/21 |
| http://154.59.56.73:999 | VE | 4203 | 3 | 30/34 |
| http://154.59.56.78:999 | VE | 4553 | 3 | 10/18 |
| http://103.218.122.183:8080 | VN | 1442 | 3 | 17/33 |
| http://116.104.54.38:2080 | VN | 6455 | 3 | 3/3 |
| http://123.16.15.41:1452 | VN | 5825 | 3 | 4/10 |
| http://210.211.113.33:80 | VN | 4492 | 3 | 17/32 |
| socks5://103.138.145.204:1999 | BD | 5204 | 3 | 9/19 |
| socks5://118.179.144.113:9090 | BD | 1939 | 3 | 9/13 |
| socks5://103.210.161.8:1080 | CN | 2275 | 3 | 26/35 |
| socks5://5.45.119.70:1080 | EE | 1321 | 3 | 30/60 |
