# Proxy status

Generated 2026-08-20T13:48:09Z by `harvest.py`.

- **326** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1198** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13397** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 100/600 (17%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 963 |
| socks5 | 221 |
| socks4 | 14 |

| country | entries |
|---|---|
| ID | 279 |
| US | 84 |
| RU | 63 |
| CO | 55 |
| CN | 46 |
| PH | 43 |
| BR | 39 |
| BD | 38 |
| MX | 33 |
| NL | 32 |
| FR | 30 |
| TR | 27 |
| VE | 26 |
| EC | 25 |
| DE | 23 |
| IN | 23 |
| HK | 21 |
| SG | 21 |
| VN | 19 |
| EG | 17 |
| JP | 15 |
| DO | 14 |
| PE | 12 |
| AR | 10 |
| CL | 10 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-08-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 54 | 54 | 19 | 2026-08-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 68 | 68 | 36 | 2026-08-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 83 | 83 | 17 | 2026-08-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 88 | 88 | 23 | 2026-08-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 98 | 98 | 49 | 2026-08-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 143 | 143 | 9 | 2026-08-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 83 | 2026-08-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 176 | 176 | 67 | 2026-08-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 193 | 193 | 73 | 2026-08-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-08-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-08-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-08-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1604 | 2026-08-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1935 | 1931 | 341 | 2026-08-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2030 | 2028 | 204 | 2026-08-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2180 | 2180 | 1859 | 2026-08-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2532 | 2530 | 680 | 2026-08-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2678 | 2676 | 2133 | 2026-08-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://64.112.184.210:3128 | US | 983 | 20 | 20/20 |
| http://181.39.25.196:8118 | EC | 943 | 17 | 19/20 |
| http://34.43.46.91:443 | US | 982 | 12 | 17/20 |
| http://34.43.46.91:80 | US | 1055 | 12 | 17/20 |
| http://181.78.74.252:999 | CO | 822 | 11 | 11/11 |
| http://181.78.74.253:999 | CO | 808 | 11 | 11/11 |
| http://190.97.236.128:999 | VE | 2812 | 10 | 10/10 |
| http://190.97.236.129:999 | VE | 4882 | 10 | 10/10 |
| http://213.136.77.119:8888 | FR | 2223 | 8 | 8/8 |
| http://49.51.253.118:8888 | US | 2382 | 7 | 7/7 |
| http://47.107.82.96:30051 | CN | 1759 | 6 | 11/13 |
| http://103.237.102.191:11111 | DE | 1265 | 6 | 19/20 |
| http://212.58.132.5:8888 | GB | 1880 | 6 | 15/19 |
| http://176.111.37.216:39811 | HK | 1354 | 6 | 18/20 |
| http://1.231.81.166:3128 | KR | 2005 | 6 | 19/20 |
| http://175.136.239.173:8181 | MY | 5977 | 6 | 16/20 |
| http://95.211.174.135:3128 | NL | 949 | 6 | 19/20 |
| http://204.76.203.9:3128 | NL | 1264 | 6 | 19/20 |
| http://204.76.203.9:8080 | NL | 710 | 6 | 12/13 |
| http://185.141.26.131:3128 | RO | 1147 | 6 | 6/6 |
| http://185.200.188.234:10001 | RU | 1630 | 6 | 19/20 |
| http://130.110.103.245:3128 | SA | 1399 | 6 | 18/20 |
| http://202.28.194.139:31280 | TH | 3063 | 6 | 19/20 |
| http://95.3.69.222:8080 | TR | 1386 | 6 | 19/20 |
| http://45.66.249.187:3128 | US | 1196 | 6 | 10/11 |
| http://45.66.249.187:8080 | US | 1376 | 6 | 12/15 |
| http://45.66.249.187:8181 | US | 670 | 6 | 10/11 |
| socks5://45.144.54.40:1080 | DE | 2831 | 6 | 14/20 |
| socks5://144.91.121.61:1088 | FR | 5406 | 6 | 19/20 |
| socks5://150.241.91.238:7777 | FR | 4834 | 6 | 6/6 |
| socks5://212.58.132.5:1080 | GB | 3073 | 6 | 19/20 |
| socks5://144.24.111.128:1088 | IN | 1984 | 6 | 15/20 |
| socks5://178.128.82.131:10808 | SG | 4720 | 6 | 11/20 |
| socks5://45.61.129.165:9050 | US | 1417 | 6 | 17/20 |
| http://87.251.77.29:3128 | DE | 1445 | 5 | 18/20 |
| http://43.99.100.108:3128 | HK | 1845 | 5 | 17/20 |
| http://5.129.228.92:443 | NL | 4772 | 5 | 5/5 |
| http://95.189.35.234:81 | RU | 2884 | 5 | 11/18 |
| http://103.10.231.189:8080 | TH | 1687 | 5 | 5/5 |
| http://216.106.182.177:3128 | US | 651 | 5 | 17/20 |
| socks5://77.239.106.24:1080 | DE | 1274 | 5 | 5/5 |
| socks5://103.111.136.82:8199 | ID | 6467 | 5 | 7/15 |
| socks5://95.31.16.116:1081 | RU | 1249 | 5 | 9/11 |
| http://27.185.218.213:17981 | CN | 2688 | 4 | 11/20 |
| http://200.10.31.45:8081 | CO | 4127 | 4 | 8/17 |
| http://45.176.99.58:999 | DO | 4672 | 4 | 10/15 |
| http://80.241.214.192:3128 | FR | 3473 | 4 | 4/4 |
| http://103.122.65.242:8080 | ID | 5545 | 4 | 6/16 |
| http://103.142.21.197:8080 | ID | 5417 | 4 | 7/12 |
| http://46.247.41.222:443 | KZ | 5164 | 4 | 7/10 |
| http://175.139.255.25:8181 | MY | 5953 | 4 | 15/20 |
| http://34.94.46.8:80 | US | 278 | 4 | 15/18 |
| http://195.158.8.123:3128 | UZ | 7269 | 4 | 14/18 |
| socks5://149.62.186.244:1080 | IT | 3341 | 4 | 17/20 |
| socks5://85.209.120.145:1080 | TR | 1177 | 4 | 5/6 |
| socks5://34.229.113.62:1080 | US | 4013 | 4 | 10/13 |
| http://187.102.219.42:999 | AR | 2360 | 3 | 9/15 |
| http://185.191.239.248:3128 | CH | 1480 | 3 | 11/19 |
| http://116.196.150.180:17981 | CN | 1985 | 3 | 7/20 |
| http://196.204.83.229:8080 | EG | 5476 | 3 | 9/17 |
| http://13.38.27.183:9824 | FR | 2214 | 3 | 6/16 |
| http://95.40.233.164:3128 | HK | 4482 | 3 | 3/3 |
| http://103.155.190.130:8080 | ID | 3225 | 3 | 6/10 |
| http://103.172.71.135:3127 | ID | 5535 | 3 | 4/17 |
| http://103.249.19.50:10001 | ID | 3381 | 3 | 3/3 |
| http://43.156.236.238:80 | SG | 955 | 3 | 9/18 |
| http://43.160.242.118:3128 | SG | 6991 | 3 | 14/17 |
| http://152.42.167.241:3128 | SG | 6131 | 3 | 18/20 |
| http://13.221.202.200:3128 | US | 856 | 3 | 3/3 |
| http://98.83.197.228:3128 | US | 1840 | 3 | 3/3 |
| http://199.7.149.90:3128 | US | 254 | 3 | 3/3 |
| http://82.86.112.48:999 | VE | 1691 | 3 | 4/10 |
| http://200.59.191.27:999 | VE | 5775 | 3 | 12/15 |
| socks5://202.91.41.102:1080 | BD | 5047 | 3 | 6/19 |
| socks5://185.185.80.58:1088 | FR | 3912 | 3 | 13/19 |
| socks5://154.91.176.171:1080 | HK | 3251 | 3 | 6/11 |
| socks5://101.36.104.46:10808 | JP | 2600 | 3 | 18/20 |
| socks5://101.36.104.239:10808 | JP | 2412 | 3 | 16/20 |
| socks5://103.75.118.84:1080 | JP | 3187 | 3 | 9/15 |
| socks5://43.230.193.154:1080 | KH | 7613 | 3 | 5/18 |
| socks5://121.169.46.116:1090 | KR | 1543 | 3 | 13/20 |
| socks5://45.43.63.37:10808 | SG | 2862 | 3 | 17/20 |
| socks5://144.24.47.42:1080 | US | 4421 | 3 | 12/16 |
| http://170.168.102.55:3128 | AM | 5142 | 2 | 5/11 |
| http://103.106.34.49:4995 | BD | 6509 | 2 | 2/2 |
| http://179.48.25.1:8095 | BR | 2076 | 2 | 7/15 |
| http://114.236.137.41:21000 | CN | 6692 | 2 | 13/20 |
| http://123.57.213.24:3539 | CN | 3503 | 2 | 11/19 |
| http://223.85.21.195:8080 | CN | 3307 | 2 | 10/18 |
| http://190.131.254.134:8154 | CO | 5339 | 2 | 3/15 |
| http://130.17.12.137:3128 | DE | 4836 | 2 | 6/19 |
| http://38.44.17.142:999 | DO | 3920 | 2 | 7/13 |
| http://152.0.51.69:8080 | DO | 7049 | 2 | 5/13 |
| http://45.71.0.121:999 | EC | 7604 | 2 | 4/7 |
| http://186.33.45.219:999 | EC | 3085 | 2 | 8/9 |
| http://41.65.236.37:8080 | EG | 1172 | 2 | 2/2 |
| http://41.128.72.140:1981 | EG | 5332 | 2 | 2/2 |
| http://213.131.85.29:1976 | EG | 5284 | 2 | 6/14 |
| http://37.59.125.131:8888 | FR | 1582 | 2 | 16/20 |
| http://186.33.0.11:999 | GT | 6135 | 2 | 3/18 |
