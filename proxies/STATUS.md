# Proxy status

Generated 2026-08-24T13:53:38Z by `harvest.py`.

- **716** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1127** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13681** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 171/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 894 |
| socks5 | 219 |
| socks4 | 14 |

| country | entries |
|---|---|
| ID | 277 |
| US | 65 |
| CO | 55 |
| RU | 54 |
| PH | 46 |
| BD | 39 |
| CN | 36 |
| MX | 35 |
| EC | 32 |
| BR | 30 |
| IN | 30 |
| DE | 27 |
| NL | 27 |
| TR | 27 |
| VE | 26 |
| AR | 18 |
| SG | 18 |
| FR | 16 |
| VN | 16 |
| EG | 15 |
| IR | 13 |
| CL | 12 |
| HK | 12 |
| KH | 12 |
| FI | 10 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 3 | 2026-08-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 79 | 79 | 39 | 2026-08-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 104 | 104 | 53 | 2026-08-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 124 | 124 | 36 | 2026-08-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 146 | 146 | 66 | 2026-08-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 192 | 192 | 68 | 2026-08-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 197 | 197 | 20 | 2026-08-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 218 | 218 | 37 | 2026-08-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 230 | 230 | 90 | 2026-08-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 470 | 470 | 180 | 2026-08-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-08-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 457 | 2026-08-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-08-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1600 | 2026-08-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1861 | 1857 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1953 | 1951 | 206 | 2026-08-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2356 | 2356 | 1762 | 2026-08-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2363 | 2361 | 693 | 2026-08-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2810 | 2808 | 2067 | 2026-08-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 857 | 25 | 27/28 |
| http://34.43.46.91:443 | US | 534 | 20 | 25/28 |
| http://34.43.46.91:80 | US | 731 | 20 | 25/28 |
| http://181.78.74.252:999 | CO | 969 | 19 | 19/19 |
| http://181.78.74.253:999 | CO | 978 | 19 | 19/19 |
| http://190.97.236.128:999 | VE | 1925 | 18 | 18/18 |
| http://190.97.236.129:999 | VE | 1941 | 18 | 18/18 |
| http://103.237.102.191:11111 | DE | 846 | 14 | 27/28 |
| http://1.231.81.166:3128 | KR | 960 | 14 | 27/28 |
| http://95.211.174.135:3128 | NL | 1379 | 14 | 27/28 |
| http://204.76.203.9:3128 | NL | 898 | 14 | 27/28 |
| http://204.76.203.9:8080 | NL | 794 | 14 | 20/21 |
| http://185.200.188.234:10001 | RU | 2465 | 14 | 27/28 |
| http://130.110.103.245:3128 | SA | 1422 | 14 | 26/28 |
| http://95.3.69.222:8080 | TR | 1982 | 14 | 27/28 |
| http://87.251.77.29:3128 | DE | 876 | 13 | 26/28 |
| http://199.7.149.90:3128 | US | 353 | 11 | 11/11 |
| socks5://103.75.118.84:1080 | JP | 7528 | 11 | 17/23 |
| http://103.177.118.145:8118 | BD | 5495 | 9 | 9/9 |
| http://152.42.167.241:3128 | SG | 946 | 7 | 25/28 |
| http://199.7.149.96:3128 | US | 351 | 7 | 7/7 |
| http://45.186.6.104:3128 | EC | 1018 | 6 | 6/6 |
| http://101.47.75.240:5000 | HK | 919 | 6 | 6/6 |
| http://70.34.249.28:2001 | PL | 888 | 6 | 6/6 |
| http://64.112.184.210:3128 | US | 539 | 6 | 27/28 |
| socks5://213.136.92.91:1080 | FR | 4905 | 6 | 18/28 |
| socks5://123.58.219.171:10808 | HK | 1037 | 6 | 22/28 |
| http://175.139.255.25:8181 | MY | 3355 | 5 | 21/28 |
| http://5.129.228.92:443 | NL | 1531 | 5 | 11/13 |
| http://93.93.207.219:8088 | RU | 3639 | 5 | 5/5 |
| socks5://43.162.94.99:1080 | US | 548 | 5 | 21/28 |
| http://190.0.246.210:4040 | CO | 5141 | 4 | 24/27 |
| http://41.128.90.50:1981 | EG | 5465 | 4 | 8/11 |
| http://43.99.100.108:3128 | HK | 964 | 4 | 22/28 |
| http://47.81.56.193:8888 | TH | 1474 | 4 | 12/28 |
| http://103.10.231.189:8080 | TH | 1411 | 4 | 10/13 |
| http://195.158.8.123:3128 | UZ | 3253 | 4 | 20/26 |
| socks5://45.194.33.12:30001 | HK | 1158 | 4 | 18/24 |
| http://120.232.115.170:17981 | CN | 1376 | 3 | 14/27 |
| http://186.33.45.218:999 | EC | 6277 | 3 | 9/17 |
| http://37.59.125.131:8888 | FR | 2142 | 3 | 22/28 |
| http://103.130.61.61:8081 | ID | 1768 | 3 | 23/28 |
| http://49.147.127.126:8082 | PH | 4457 | 3 | 3/3 |
| http://103.157.200.126:3128 | PK | 1465 | 3 | 4/5 |
| http://5.161.50.82:8118 | US | 5226 | 3 | 10/27 |
| http://44.193.20.213:8081 | US | 1267 | 3 | 3/3 |
| http://45.66.249.187:3128 | US | 383 | 3 | 16/19 |
| socks5://103.236.190.197:1080 | ID | 2447 | 3 | 8/26 |
| socks5://149.62.186.244:1080 | IT | 6364 | 3 | 23/28 |
| socks5://37.18.73.60:5566 | RU | 2355 | 3 | 16/28 |
| socks5://185.170.10.176:1080 | RU | 6833 | 3 | 4/5 |
| http://168.194.34.196:9001 | AR | 1777 | 2 | 9/26 |
| http://103.113.152.73:14158 | BD | 3819 | 2 | 5/22 |
| http://168.195.168.182:8080 | BR | 2192 | 2 | 5/23 |
| http://39.108.103.25:10185 | CN | 2907 | 2 | 3/6 |
| http://115.231.181.40:8128 | CN | 1588 | 2 | 13/27 |
| http://116.62.60.22:3128 | CN | 4638 | 2 | 7/13 |
| http://209.14.115.222:999 | CO | 911 | 2 | 3/8 |
| http://159.69.45.217:1083 | DE | 2608 | 2 | 2/2 |
| http://38.50.165.122:999 | DO | 7785 | 2 | 3/16 |
| http://38.255.121.1:999 | DO | 1784 | 2 | 5/16 |
| http://41.33.219.140:1981 | EG | 1468 | 2 | 5/10 |
| http://45.198.20.166:8080 | ID | 2236 | 2 | 5/22 |
| http://101.255.165.105:8090 | ID | 5241 | 2 | 4/16 |
| http://103.125.174.151:1111 | ID | 6432 | 2 | 9/24 |
| http://103.142.255.32:8080 | ID | 1272 | 2 | 3/18 |
| http://103.162.63.107:8085 | ID | 2076 | 2 | 7/27 |
| http://103.247.13.134:8080 | ID | 7734 | 2 | 3/11 |
| http://114.9.26.202:8080 | ID | 4905 | 2 | 5/13 |
| http://160.187.174.249:8090 | ID | 4948 | 2 | 3/4 |
| http://182.253.38.179:3128 | ID | 6492 | 2 | 6/16 |
| http://103.143.39.97:1111 | IN | 1513 | 2 | 4/5 |
| http://151.185.41.195:8080 | IN | 1354 | 2 | 2/2 |
| http://93.187.26.134:58080 | IT | 6241 | 2 | 5/12 |
| http://45.43.60.220:8080 | JP | 2691 | 2 | 17/27 |
| http://197.248.16.109:8080 | KE | 3514 | 2 | 3/24 |
| http://203.81.75.202:8080 | MM | 4602 | 2 | 4/6 |
| http://175.136.239.173:8181 | MY | 5173 | 2 | 21/28 |
| http://175.136.239.174:8181 | MY | 5799 | 2 | 16/28 |
| http://190.43.231.101:999 | PE | 4324 | 2 | 3/5 |
| http://120.28.192.201:8081 | PH | 6483 | 2 | 3/18 |
| http://180.191.231.149:8082 | PH | 2561 | 2 | 8/27 |
| http://180.191.254.36:8181 | PH | 1121 | 2 | 6/27 |
| http://212.200.223.89:8080 | RS | 4274 | 2 | 7/26 |
| http://85.237.39.139:8080 | RU | 1424 | 2 | 3/6 |
| http://43.160.242.118:3128 | SG | 5631 | 2 | 20/25 |
| http://109.224.242.38:8080 | TR | 2596 | 2 | 2/2 |
| http://195.226.213.254:8888 | UA | 4453 | 2 | 8/26 |
| http://45.66.249.187:8080 | US | 292 | 2 | 16/23 |
| http://104.154.186.48:80 | US | 417 | 2 | 14/27 |
| http://42.96.18.62:1311 | VN | 2542 | 2 | 17/27 |
| http://115.78.135.4:3334 | VN | 1187 | 2 | 4/6 |
| socks4://157.90.113.23:9052 | DE | 972 | 2 | 7/10 |
| socks5://59.152.97.233:1080 | BD | 4065 | 2 | 17/26 |
| socks5://185.128.104.152:8443 | DE | 1291 | 2 | 3/9 |
| socks5://45.95.233.88:1082 | FR | 4042 | 2 | 13/25 |
| socks5://144.91.121.61:1088 | FR | 4096 | 2 | 26/28 |
| socks5://152.228.237.108:1080 | FR | 2852 | 2 | 9/13 |
| socks5://45.194.33.12:30002 | HK | 1597 | 2 | 2/2 |
| socks5://103.103.146.149:7080 | ID | 3477 | 2 | 6/26 |
