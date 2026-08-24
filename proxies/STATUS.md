# Proxy status

Generated 2026-08-24T20:00:12Z by `harvest.py`.

- **881** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1412** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13831** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 160/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1188 |
| socks5 | 211 |
| socks4 | 13 |

| country | entries |
|---|---|
| ID | 378 |
| US | 74 |
| PH | 66 |
| CO | 62 |
| BD | 46 |
| MX | 45 |
| RU | 45 |
| BR | 41 |
| IN | 39 |
| CN | 36 |
| NL | 35 |
| VE | 35 |
| DE | 33 |
| EC | 31 |
| TR | 31 |
| VN | 24 |
| FR | 22 |
| SG | 21 |
| DO | 18 |
| PK | 18 |
| HK | 17 |
| KH | 17 |
| AR | 14 |
| CL | 14 |
| EG | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 1 | 2026-08-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 65 | 65 | 10 | 2026-08-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 81 | 81 | 9 | 2026-08-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 91 | 91 | 32 | 2026-08-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 95 | 95 | 15 | 2026-08-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-08-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 103 | 103 | 51 | 2026-08-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 145 | 145 | 39 | 2026-08-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-08-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 170 | 170 | 65 | 2026-08-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 538 | 538 | 195 | 2026-08-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-08-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-08-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1144 | 2026-08-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1599 | 2026-08-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1837 | 1833 | 100 | 2026-08-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2132 | 2132 | 1704 | 2026-08-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2147 | 2145 | 173 | 2026-08-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2664 | 2662 | 648 | 2026-08-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3069 | 3067 | 2250 | 2026-08-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1556 | 26 | 28/29 |
| http://34.43.46.91:443 | US | 643 | 21 | 26/29 |
| http://34.43.46.91:80 | US | 657 | 21 | 26/29 |
| http://181.78.74.252:999 | CO | 935 | 20 | 20/20 |
| http://181.78.74.253:999 | CO | 874 | 20 | 20/20 |
| http://190.97.236.128:999 | VE | 790 | 19 | 19/19 |
| http://190.97.236.129:999 | VE | 788 | 19 | 19/19 |
| http://103.237.102.191:11111 | DE | 1310 | 15 | 28/29 |
| http://1.231.81.166:3128 | KR | 1144 | 15 | 28/29 |
| http://95.211.174.135:3128 | NL | 1284 | 15 | 28/29 |
| http://204.76.203.9:3128 | NL | 1019 | 15 | 28/29 |
| http://204.76.203.9:8080 | NL | 813 | 15 | 21/22 |
| http://185.200.188.234:10001 | RU | 1619 | 15 | 28/29 |
| http://130.110.103.245:3128 | SA | 1462 | 15 | 27/29 |
| http://95.3.69.222:8080 | TR | 1636 | 15 | 28/29 |
| http://199.7.149.90:3128 | US | 355 | 12 | 12/12 |
| socks5://103.75.118.84:1080 | JP | 2270 | 12 | 18/24 |
| http://103.177.118.145:8118 | BD | 4474 | 10 | 10/10 |
| http://152.42.167.241:3128 | SG | 2613 | 8 | 26/29 |
| http://199.7.149.96:3128 | US | 388 | 8 | 8/8 |
| http://45.186.6.104:3128 | EC | 816 | 7 | 7/7 |
| http://101.47.75.240:5000 | HK | 2150 | 7 | 7/7 |
| http://70.34.249.28:2001 | PL | 916 | 7 | 7/7 |
| http://64.112.184.210:3128 | US | 861 | 7 | 28/29 |
| socks5://123.58.219.171:10808 | HK | 3452 | 7 | 23/29 |
| http://175.139.255.25:8181 | MY | 2465 | 6 | 22/29 |
| http://5.129.228.92:443 | NL | 893 | 6 | 12/14 |
| socks5://43.162.94.99:1080 | US | 1451 | 6 | 22/29 |
| http://190.0.246.210:4040 | CO | 2095 | 5 | 25/28 |
| http://47.81.56.193:8888 | TH | 1586 | 5 | 13/29 |
| http://120.232.115.170:17981 | CN | 1379 | 4 | 15/28 |
| http://186.33.45.218:999 | EC | 3197 | 4 | 10/18 |
| http://103.130.61.61:8081 | ID | 2855 | 4 | 24/29 |
| http://103.157.200.126:3128 | PK | 1486 | 4 | 5/6 |
| http://5.161.50.82:8118 | US | 6046 | 4 | 11/28 |
| http://44.193.20.213:8081 | US | 408 | 4 | 4/4 |
| http://45.66.249.187:3128 | US | 106 | 4 | 17/20 |
| socks5://149.62.186.244:1080 | IT | 5332 | 4 | 24/29 |
| http://168.194.34.196:9001 | AR | 6722 | 3 | 10/27 |
| http://103.113.152.73:14158 | BD | 3605 | 3 | 6/23 |
| http://115.231.181.40:8128 | CN | 3835 | 3 | 14/28 |
| http://159.69.45.217:1083 | DE | 2148 | 3 | 3/3 |
| http://45.198.20.166:8080 | ID | 1232 | 3 | 6/23 |
| http://101.255.165.105:8090 | ID | 2634 | 3 | 5/17 |
| http://45.43.60.220:8080 | JP | 4100 | 3 | 18/28 |
| http://175.136.239.173:8181 | MY | 1983 | 3 | 22/29 |
| http://175.136.239.174:8181 | MY | 4644 | 3 | 17/29 |
| http://180.191.231.149:8082 | PH | 2561 | 3 | 9/28 |
| http://43.160.242.118:3128 | SG | 3946 | 3 | 21/26 |
| http://109.224.242.38:8080 | TR | 3525 | 3 | 3/3 |
| http://45.66.249.187:8080 | US | 92 | 3 | 17/24 |
| http://42.96.18.62:1311 | VN | 2949 | 3 | 18/28 |
| socks5://59.152.97.233:1080 | BD | 1750 | 3 | 18/27 |
| socks5://185.128.104.152:8443 | DE | 1274 | 3 | 4/10 |
| socks5://144.91.121.61:1088 | FR | 3289 | 3 | 27/29 |
| socks5://152.228.237.108:1080 | FR | 5300 | 3 | 10/14 |
| socks5://101.36.104.239:10808 | JP | 1039 | 3 | 23/29 |
| socks5://203.189.150.44:1080 | KH | 4888 | 3 | 12/29 |
| socks5://103.150.206.77:1080 | PK | 5818 | 3 | 9/27 |
| socks5://79.76.59.115:1080 | SE | 2499 | 3 | 9/19 |
| socks5://67.207.92.87:1088 | US | 5590 | 3 | 14/28 |
| socks5://141.148.158.143:1080 | US | 1314 | 3 | 14/28 |
| socks5://193.25.215.182:22222 | US | 742 | 3 | 26/29 |
| http://45.174.149.222:999 | AR | 6768 | 2 | 2/2 |
| http://180.181.215.232:3128 | AU | 3354 | 2 | 4/18 |
| http://38.10.91.114:8084 | BR | 6383 | 2 | 4/23 |
| http://138.0.207.246:8082 | BR | 4198 | 2 | 6/14 |
| http://179.185.75.94:8080 | BR | 4351 | 2 | 3/18 |
| http://179.57.172.172:999 | CL | 5644 | 2 | 6/28 |
| http://8.243.167.50:999 | CO | 2871 | 2 | 5/25 |
| http://45.172.218.67:3028 | CO | 3503 | 2 | 8/19 |
| http://177.93.46.124:999 | CO | 5378 | 2 | 4/25 |
| http://181.78.10.110:999 | CO | 6914 | 2 | 8/25 |
| http://181.78.208.227:999 | CO | 2938 | 2 | 4/16 |
| http://186.33.54.194:999 | CO | 2747 | 2 | 3/12 |
| http://190.14.224.244:999 | CO | 3889 | 2 | 5/20 |
| http://190.60.39.230:999 | CO | 6805 | 2 | 5/16 |
| http://31.25.236.95:3128 | DE | 7036 | 2 | 2/2 |
| http://92.113.150.45:3128 | DK | 835 | 2 | 3/19 |
| http://38.75.82.220:999 | DO | 5361 | 2 | 5/10 |
| http://185.27.144.16:999 | DO | 4792 | 2 | 2/2 |
| http://45.164.64.116:999 | EC | 3827 | 2 | 2/2 |
| http://177.234.217.236:999 | EC | 6227 | 2 | 2/2 |
| http://181.188.203.112:999 | EC | 4670 | 2 | 6/21 |
| http://186.33.45.219:999 | EC | 2029 | 2 | 13/18 |
| http://190.12.150.244:999 | EC | 3879 | 2 | 18/25 |
| http://176.111.37.5:39811 | HK | 1178 | 2 | 24/29 |
| http://176.111.37.216:39811 | HK | 1131 | 2 | 25/29 |
| http://9.154.224.101:8080 | ID | 5373 | 2 | 2/2 |
| http://45.198.8.6:8080 | ID | 3085 | 2 | 4/7 |
| http://45.198.20.173:8080 | ID | 7306 | 2 | 2/2 |
| http://103.3.58.162:8088 | ID | 2771 | 2 | 7/28 |
| http://103.4.76.237:1111 | ID | 3671 | 2 | 4/26 |
| http://103.31.204.158:3128 | ID | 3239 | 2 | 5/15 |
| http://103.41.247.34:8080 | ID | 4312 | 2 | 5/13 |
| http://103.68.214.175:8080 | ID | 6999 | 2 | 3/6 |
| http://103.80.88.77:8080 | ID | 1373 | 2 | 4/13 |
| http://103.81.195.150:3125 | ID | 3616 | 2 | 3/12 |
| http://103.97.140.226:8080 | ID | 7084 | 2 | 4/11 |
| http://103.102.12.67:8080 | ID | 1246 | 2 | 7/21 |
