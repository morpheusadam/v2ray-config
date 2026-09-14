# Proxy status

Generated 2026-09-14T18:34:21Z by `harvest.py`.

- **887** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1704** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **20481** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 161/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1149 |
| socks5 | 542 |
| socks4 | 13 |

| country | entries |
|---|---|
| NL | 349 |
| ID | 296 |
| US | 109 |
| CN | 89 |
| RU | 64 |
| CO | 53 |
| MX | 53 |
| BD | 49 |
| VN | 47 |
| PH | 45 |
| VE | 41 |
| DE | 32 |
| SG | 30 |
| BR | 29 |
| IN | 29 |
| EG | 28 |
| EC | 25 |
| FR | 25 |
| HK | 18 |
| TH | 18 |
| KH | 17 |
| DO | 14 |
| FI | 14 |
| TR | 14 |
| CL | 12 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-09-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 48 | 48 | 26 | 2026-09-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 85 | 85 | 21 | 2026-09-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 78 | 2026-09-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 70 | 2026-09-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 153 | 153 | 87 | 2026-09-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 279 | 279 | 169 | 2026-09-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 292 | 292 | 99 | 2026-09-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 354 | 354 | 92 | 2026-09-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 373 | 373 | 153 | 2026-09-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 533 | 2026-09-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-09-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-09-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1595 | 2026-09-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1959 | 1955 | 180 | 2026-09-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2703 | 2701 | 489 | 2026-09-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2859 | 2857 | 704 | 2026-09-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2936 | 2934 | 2238 | 2026-09-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 3288 | 3288 | 2117 | 2026-09-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 9455 | 9454 | 3162 | 2026-09-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 590 | 62 | 67/70 |
| http://34.43.46.91:80 | US | 713 | 62 | 67/70 |
| http://95.211.174.135:3128 | NL | 1133 | 56 | 69/70 |
| http://185.200.188.234:10001 | RU | 1321 | 56 | 69/70 |
| http://130.110.103.245:3128 | SA | 1646 | 56 | 68/70 |
| http://1.231.81.166:3128 | KR | 1039 | 35 | 67/70 |
| http://176.111.37.5:39811 | HK | 1116 | 30 | 64/70 |
| http://181.78.23.187:999 | CO | 820 | 27 | 37/39 |
| http://181.78.74.252:999 | CO | 924 | 27 | 59/61 |
| http://181.78.74.253:999 | CO | 965 | 27 | 59/61 |
| http://190.97.236.128:999 | VE | 954 | 27 | 58/60 |
| http://190.97.236.129:999 | VE | 887 | 27 | 58/60 |
| http://95.3.69.222:8080 | TR | 1509 | 25 | 67/70 |
| http://190.97.241.106:999 | VE | 2284 | 22 | 31/54 |
| http://45.186.6.104:3128 | EC | 801 | 18 | 47/48 |
| socks5://107.167.18.122:443 | US | 1124 | 15 | 21/22 |
| http://103.237.102.191:11111 | DE | 1039 | 14 | 66/70 |
| socks5://83.147.216.208:1080 | FI | 2400 | 14 | 20/38 |
| socks5://144.91.111.48:1088 | FR | 3645 | 12 | 40/70 |
| http://184.75.221.82:3118 | CA | 1523 | 11 | 32/35 |
| socks5://144.91.121.61:1088 | FR | 5626 | 11 | 61/70 |
| http://91.134.141.4:3128 | FR | 765 | 9 | 29/31 |
| socks5://51.178.49.241:1088 | FR | 2345 | 8 | 26/31 |
| socks5://103.75.118.84:1080 | JP | 1726 | 8 | 48/65 |
| http://186.5.94.206:999 | EC | 6155 | 7 | 30/32 |
| http://107.150.41.226:18080 | US | 593 | 7 | 7/7 |
| http://14.251.13.20:8080 | VN | 1107 | 7 | 40/42 |
| socks5://213.199.47.140:1080 | FR | 2092 | 7 | 29/36 |
| socks5://43.135.176.121:1080 | US | 168 | 7 | 22/25 |
| http://165.154.162.73:8888 | US | 430 | 6 | 40/70 |
| socks5://101.36.104.239:10808 | JP | 1069 | 6 | 58/70 |
| socks5://161.35.90.93:1083 | NL | 1860 | 6 | 35/68 |
| http://114.236.137.41:21000 | CN | 1585 | 5 | 48/70 |
| http://45.240.232.61:8080 | EG | 2053 | 5 | 18/50 |
| http://43.153.195.69:80 | SG | 891 | 5 | 7/10 |
| http://43.156.236.238:80 | SG | 889 | 5 | 34/68 |
| http://124.156.194.52:8081 | SG | 879 | 5 | 5/5 |
| http://195.158.8.123:3128 | UZ | 3437 | 5 | 46/68 |
| socks5://5.75.133.113:10801 | DE | 2250 | 5 | 25/36 |
| socks5://54.95.120.6:1080 | JP | 724 | 5 | 5/5 |
| socks5://191.223.220.23:1080 | JP | 838 | 5 | 17/67 |
| socks5://193.25.215.182:22222 | US | 835 | 5 | 65/70 |
| http://8.138.217.152:21001 | CN | 4163 | 4 | 46/70 |
| http://119.188.131.55:17981 | CN | 3106 | 4 | 29/70 |
| http://120.232.115.170:17981 | CN | 1379 | 4 | 49/69 |
| http://94.43.164.242:8080 | GE | 6971 | 4 | 4/4 |
| http://46.183.134.50:8080 | RU | 6834 | 4 | 12/67 |
| socks5://103.163.244.106:1080 | IN | 7238 | 4 | 16/66 |
| socks5://202.79.26.242:1080 | KH | 1536 | 4 | 8/29 |
| socks5://95.81.96.158:1080 | NL | 2573 | 4 | 7/30 |
| http://103.177.118.145:8118 | BD | 1380 | 3 | 47/51 |
| http://47.103.30.64:8080 | CN | 1481 | 3 | 3/3 |
| http://114.252.15.106:8888 | CN | 2216 | 3 | 10/23 |
| http://114.254.49.43:8888 | CN | 2092 | 3 | 10/17 |
| http://123.119.179.34:8888 | CN | 6230 | 3 | 12/32 |
| http://123.119.179.101:8888 | CN | 1228 | 3 | 11/28 |
| http://123.121.209.108:8888 | CN | 5903 | 3 | 11/20 |
| http://45.172.218.67:3028 | CO | 4516 | 3 | 31/60 |
| http://190.0.246.210:4040 | CO | 2102 | 3 | 60/69 |
| http://186.33.45.219:999 | EC | 5111 | 3 | 33/59 |
| http://186.33.45.220:999 | EC | 7410 | 3 | 17/39 |
| http://196.204.26.243:1981 | EG | 4593 | 3 | 4/5 |
| http://65.109.217.164:3128 | FI | 1972 | 3 | 3/3 |
| http://37.59.125.131:8888 | FR | 1126 | 3 | 55/70 |
| http://84.8.216.230:2001 | MA | 915 | 3 | 3/3 |
| http://144.124.251.24:10230 | NL | 887 | 3 | 6/17 |
| http://144.124.251.24:10453 | NL | 1251 | 3 | 4/7 |
| http://144.124.251.24:10551 | NL | 1054 | 3 | 7/18 |
| http://144.124.251.24:10566 | NL | 1056 | 3 | 3/3 |
| http://144.124.251.24:11124 | NL | 988 | 3 | 5/19 |
| http://43.156.199.63:8080 | SG | 5884 | 3 | 4/5 |
| http://202.28.194.139:31280 | TH | 1967 | 3 | 63/70 |
| http://38.51.207.104:8080 | VE | 1755 | 3 | 10/11 |
| http://200.59.191.27:999 | VE | 2546 | 3 | 40/65 |
| http://210.211.113.34:80 | VN | 2575 | 3 | 35/42 |
| socks5://59.152.97.233:1080 | BD | 1960 | 3 | 44/68 |
| socks5://91.107.179.68:10809 | DE | 1374 | 3 | 3/3 |
| socks5://103.31.235.211:69 | ID | 1379 | 3 | 8/28 |
| socks5://144.24.111.128:1088 | IN | 1581 | 3 | 53/70 |
| socks5://45.61.129.165:9050 | US | 5979 | 3 | 58/70 |
| socks5://118.70.82.27:1083 | VN | 1451 | 3 | 3/3 |
| http://151.158.121.73:8080 | BD | 6196 | 2 | 3/8 |
| http://114.249.237.87:8888 | CN | 2254 | 2 | 17/34 |
| http://123.121.208.63:8888 | CN | 7278 | 2 | 7/16 |
| http://45.65.138.48:999 | CO | 6898 | 2 | 25/70 |
| http://179.1.196.134:999 | CO | 5348 | 2 | 11/47 |
| http://181.78.1.226:999 | CO | 4263 | 2 | 3/12 |
| http://190.0.246.211:4040 | CO | 2869 | 2 | 59/70 |
| http://45.71.186.212:999 | EC | 4717 | 2 | 17/57 |
| http://45.71.186.214:999 | EC | 7035 | 2 | 8/16 |
| http://41.196.16.229:1976 | EG | 1330 | 2 | 2/2 |
| http://167.86.104.220:80 | FR | 976 | 2 | 5/6 |
| http://154.223.77.54:10001 | HK | 2909 | 2 | 3/4 |
| http://103.224.65.89:8080 | ID | 7455 | 2 | 4/8 |
| http://144.79.37.44:8080 | ID | 6191 | 2 | 4/20 |
| http://103.209.38.132:8080 | IN | 4485 | 2 | 5/26 |
| http://168.144.68.176:3129 | IN | 1535 | 2 | 7/20 |
| http://112.216.54.226:12121 | KR | 902 | 2 | 20/64 |
| http://45.168.238.193:8443 | MX | 7772 | 2 | 7/30 |
| http://144.124.251.24:10000 | NL | 1134 | 2 | 6/16 |
