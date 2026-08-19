# Proxy status

Generated 2026-08-19T19:56:26Z by `harvest.py`.

- **968** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1514** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13854** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 218/600 (36%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1242 |
| socks5 | 253 |
| socks4 | 19 |

| country | entries |
|---|---|
| ID | 381 |
| US | 98 |
| RU | 69 |
| CO | 67 |
| PH | 63 |
| CN | 54 |
| BD | 48 |
| BR | 44 |
| MX | 43 |
| TR | 40 |
| FR | 36 |
| EC | 35 |
| VE | 34 |
| NL | 31 |
| DE | 28 |
| SG | 28 |
| HK | 23 |
| IN | 23 |
| VN | 21 |
| DO | 18 |
| AR | 17 |
| JP | 17 |
| IR | 16 |
| KH | 16 |
| CL | 15 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 12 | 12 | 5 | 2026-08-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 78 | 78 | 47 | 2026-08-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 136 | 136 | 53 | 2026-08-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 148 | 148 | 38 | 2026-08-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 149 | 149 | 62 | 2026-08-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 74 | 2026-08-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 158 | 158 | 64 | 2026-08-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 166 | 166 | 21 | 2026-08-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 213 | 213 | 87 | 2026-08-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-08-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 599 | 599 | 252 | 2026-08-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-08-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1404 | 1404 | 82 | 2026-08-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-08-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1610 | 2026-08-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2399 | 2397 | 190 | 2026-08-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2465 | 2465 | 2016 | 2026-08-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2850 | 2848 | 686 | 2026-08-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3243 | 3241 | 2572 | 2026-08-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1626 | 19 | 19/19 |
| http://64.112.184.210:3128 | US | 836 | 19 | 19/19 |
| socks5://69.55.49.177:38182 | US | 1712 | 19 | 19/19 |
| http://181.39.25.196:8118 | EC | 1116 | 16 | 18/19 |
| http://190.0.246.210:4040 | CO | 4864 | 15 | 17/18 |
| http://34.43.46.91:443 | US | 1157 | 11 | 16/19 |
| http://34.43.46.91:80 | US | 1113 | 11 | 16/19 |
| http://181.78.74.252:999 | CO | 857 | 10 | 10/10 |
| http://181.78.74.253:999 | CO | 863 | 10 | 10/10 |
| http://190.97.236.128:999 | VE | 926 | 9 | 9/9 |
| http://190.97.236.129:999 | VE | 799 | 9 | 9/9 |
| http://213.136.77.119:8888 | FR | 2362 | 7 | 7/7 |
| http://49.51.253.118:8888 | US | 1018 | 6 | 6/6 |
| http://8.138.217.152:21001 | CN | 2148 | 5 | 12/19 |
| http://47.107.82.96:30051 | CN | 1659 | 5 | 10/12 |
| http://103.237.102.191:11111 | DE | 1862 | 5 | 18/19 |
| http://212.58.132.5:8888 | GB | 1244 | 5 | 14/18 |
| http://176.111.37.216:39811 | HK | 1405 | 5 | 17/19 |
| http://103.147.134.114:8082 | ID | 2547 | 5 | 5/5 |
| http://117.236.124.166:3128 | IN | 2351 | 5 | 12/19 |
| http://1.231.81.166:3128 | KR | 2404 | 5 | 18/19 |
| http://94.131.92.155:3128 | KZ | 1396 | 5 | 11/17 |
| http://175.136.239.173:8181 | MY | 3461 | 5 | 15/19 |
| http://95.211.174.135:3128 | NL | 1171 | 5 | 18/19 |
| http://204.76.203.9:3128 | NL | 1859 | 5 | 18/19 |
| http://204.76.203.9:8080 | NL | 743 | 5 | 11/12 |
| http://185.141.26.131:3128 | RO | 1677 | 5 | 5/5 |
| http://85.193.65.88:8888 | RU | 1308 | 5 | 8/9 |
| http://185.200.188.234:10001 | RU | 1464 | 5 | 18/19 |
| http://130.110.103.245:3128 | SA | 2095 | 5 | 17/19 |
| http://202.28.194.139:31280 | TH | 2371 | 5 | 18/19 |
| http://95.3.69.222:8080 | TR | 1443 | 5 | 18/19 |
| http://34.69.61.247:80 | US | 311 | 5 | 12/18 |
| http://45.66.249.187:3128 | US | 599 | 5 | 9/10 |
| http://45.66.249.187:8080 | US | 312 | 5 | 11/14 |
| http://45.66.249.187:8181 | US | 567 | 5 | 9/10 |
| http://42.96.18.62:1311 | VN | 3335 | 5 | 13/18 |
| socks5://45.144.54.40:1080 | DE | 1845 | 5 | 13/19 |
| socks5://144.91.111.48:1088 | FR | 3508 | 5 | 16/19 |
| socks5://144.91.121.61:1088 | FR | 3843 | 5 | 18/19 |
| socks5://150.241.91.238:7777 | FR | 2168 | 5 | 5/5 |
| socks5://212.58.132.5:1080 | GB | 3172 | 5 | 18/19 |
| socks5://144.24.111.128:1088 | IN | 2868 | 5 | 14/19 |
| socks5://178.128.82.131:10808 | SG | 1933 | 5 | 10/19 |
| socks5://43.162.94.99:1080 | US | 521 | 5 | 15/19 |
| socks5://45.61.129.165:9050 | US | 3058 | 5 | 16/19 |
| http://120.232.115.170:17981 | CN | 1260 | 4 | 9/18 |
| http://87.251.77.29:3128 | DE | 2009 | 4 | 17/19 |
| http://41.128.90.50:1976 | EG | 1111 | 4 | 4/4 |
| http://43.99.100.108:3128 | HK | 2129 | 4 | 16/19 |
| http://103.130.61.61:8081 | ID | 2862 | 4 | 16/19 |
| http://5.129.228.92:443 | NL | 1043 | 4 | 4/4 |
| http://77.222.54.205:3128 | RU | 980 | 4 | 4/4 |
| http://95.189.35.234:81 | RU | 4734 | 4 | 10/17 |
| http://43.156.228.168:80 | SG | 1040 | 4 | 10/18 |
| http://103.10.231.189:8080 | TH | 1418 | 4 | 4/4 |
| http://216.106.182.177:3128 | US | 737 | 4 | 16/19 |
| http://43.109.48.179:9999 | VN | 1416 | 4 | 7/17 |
| socks5://103.138.145.228:1999 | BD | 5968 | 4 | 7/17 |
| socks5://77.239.106.24:1080 | DE | 2011 | 4 | 4/4 |
| socks5://159.195.49.27:1080 | DE | 823 | 4 | 12/18 |
| socks5://103.111.136.82:8199 | ID | 7101 | 4 | 6/14 |
| socks5://95.31.16.116:1081 | RU | 1438 | 4 | 8/10 |
| http://27.185.218.213:17981 | CN | 1956 | 3 | 10/19 |
| http://200.10.31.45:8081 | CO | 6880 | 3 | 7/16 |
| http://45.176.99.58:999 | DO | 2322 | 3 | 9/14 |
| http://80.241.214.192:3128 | FR | 1344 | 3 | 3/3 |
| http://103.122.65.242:8080 | ID | 2526 | 3 | 5/15 |
| http://103.142.21.197:8080 | ID | 3527 | 3 | 6/11 |
| http://103.156.17.235:8818 | ID | 2468 | 3 | 3/3 |
| http://103.171.240.170:8090 | ID | 7979 | 3 | 4/16 |
| http://43.206.240.252:32840 | JP | 5215 | 3 | 3/3 |
| http://46.247.41.222:443 | KZ | 6347 | 3 | 6/9 |
| http://154.73.28.79:8080 | LY | 7191 | 3 | 4/13 |
| http://5.102.108.221:999 | MX | 3727 | 3 | 4/6 |
| http://38.210.179.146:999 | MX | 5480 | 3 | 4/17 |
| http://175.139.255.25:8181 | MY | 4137 | 3 | 14/19 |
| http://119.93.128.161:8082 | PH | 4853 | 3 | 3/3 |
| http://109.94.1.23:4050 | RU | 1751 | 3 | 15/19 |
| http://217.25.230.70:8080 | RU | 1204 | 3 | 4/15 |
| http://13.214.151.56:8081 | SG | 1195 | 3 | 3/3 |
| http://176.88.166.162:8080 | TR | 1263 | 3 | 6/15 |
| http://34.94.46.8:80 | US | 556 | 3 | 14/17 |
| http://195.158.8.123:3128 | UZ | 6137 | 3 | 13/17 |
| socks5://103.161.104.96:1080 | BD | 2920 | 3 | 3/3 |
| socks5://27.155.93.29:5080 | CN | 1568 | 3 | 5/9 |
| socks5://123.58.219.171:10808 | HK | 2253 | 3 | 15/19 |
| socks5://149.62.186.244:1080 | IT | 1751 | 3 | 16/19 |
| socks5://72.255.38.180:1080 | PK | 4661 | 3 | 5/17 |
| socks5://85.209.120.145:1080 | TR | 1120 | 3 | 4/5 |
| socks5://34.229.113.62:1080 | US | 1194 | 3 | 9/12 |
| socks5://216.106.179.216:49418 | US | 2527 | 3 | 5/8 |
| http://168.196.227.203:999 | AR | 1509 | 2 | 4/13 |
| http://187.102.219.42:999 | AR | 1169 | 2 | 8/14 |
| http://103.239.253.66:8080 | BD | 5403 | 2 | 3/9 |
| http://163.227.144.80:8080 | BD | 2600 | 2 | 6/14 |
| http://182.48.66.154:8080 | BD | 6809 | 2 | 2/2 |
| http://182.160.124.153:12331 | BD | 3963 | 2 | 5/11 |
| http://45.175.171.4:8085 | BR | 6219 | 2 | 3/5 |
| http://45.179.107.253:8080 | BR | 3472 | 2 | 4/15 |
