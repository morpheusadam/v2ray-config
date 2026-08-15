# Proxy status

Generated 2026-08-15T19:52:53Z by `harvest.py`.

- **498** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **939** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **12337** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 158/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 679 |
| socks5 | 244 |
| socks4 | 16 |

| country | entries |
|---|---|
| ID | 185 |
| US | 60 |
| RU | 56 |
| CN | 45 |
| VN | 43 |
| CO | 31 |
| BD | 29 |
| NL | 28 |
| IN | 27 |
| MX | 27 |
| FR | 26 |
| HK | 26 |
| PH | 26 |
| DE | 23 |
| BR | 20 |
| TR | 19 |
| SG | 18 |
| VE | 18 |
| EC | 15 |
| JP | 15 |
| GB | 12 |
| KH | 12 |
| DO | 9 |
| FI | 9 |
| KR | 8 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-08-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 72 | 72 | 46 | 2026-08-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 73 | 73 | 24 | 2026-08-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 94 | 94 | 52 | 2026-08-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 94 | 94 | 8 | 2026-08-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-08-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 134 | 134 | 57 | 2026-08-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 134 | 134 | 21 | 2026-08-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 87 | 2026-08-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 178 | 178 | 41 | 2026-08-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 407 | 407 | 210 | 2026-08-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 534 | 2026-08-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-08-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1423 | 1419 | 312 | 2026-08-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-08-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1622 | 2026-08-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1915 | 1913 | 170 | 2026-08-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2454 | 2452 | 704 | 2026-08-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2463 | 2463 | 1950 | 2026-08-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2699 | 2697 | 2256 | 2026-08-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2605 | 11 | 11/11 |
| http://87.251.77.29:3128 | DE | 846 | 11 | 11/11 |
| http://103.237.102.191:11111 | DE | 1652 | 11 | 11/11 |
| http://176.111.37.5:39811 | HK | 1484 | 11 | 11/11 |
| http://103.130.61.61:8081 | ID | 2167 | 11 | 11/11 |
| http://1.231.81.166:3128 | KR | 1056 | 11 | 11/11 |
| http://95.211.64.139:8889 | NL | 988 | 11 | 11/11 |
| http://95.211.174.135:3128 | NL | 1495 | 11 | 11/11 |
| http://204.76.203.9:3128 | NL | 1303 | 11 | 11/11 |
| http://185.200.188.234:10001 | RU | 2486 | 11 | 11/11 |
| http://152.42.167.241:3128 | SG | 1612 | 11 | 11/11 |
| http://202.28.194.139:31280 | TH | 2100 | 11 | 11/11 |
| http://95.3.69.222:8080 | TR | 1636 | 11 | 11/11 |
| http://64.112.184.210:3128 | US | 498 | 11 | 11/11 |
| socks5://66.163.118.99:10006 | ES | 1611 | 11 | 11/11 |
| socks5://144.91.121.61:1088 | FR | 1914 | 11 | 11/11 |
| socks5://212.58.132.5:1080 | GB | 1967 | 11 | 11/11 |
| socks5://66.163.119.55:10006 | IT | 1492 | 11 | 11/11 |
| socks5://101.36.104.46:10808 | JP | 2384 | 11 | 11/11 |
| socks5://193.233.218.213:1080 | RU | 3224 | 11 | 11/11 |
| socks5://69.55.49.177:38182 | US | 678 | 11 | 11/11 |
| socks5://193.25.215.182:22222 | US | 699 | 11 | 11/11 |
| http://95.211.64.139:8887 | NL | 879 | 10 | 10/10 |
| http://153.80.240.37:8080 | NL | 845 | 9 | 10/11 |
| socks5://45.43.63.37:10808 | SG | 2771 | 9 | 10/11 |
| http://181.39.25.196:8118 | EC | 926 | 8 | 10/11 |
| http://130.110.103.245:3128 | SA | 1589 | 8 | 10/11 |
| socks5://51.159.97.242:10006 | FR | 1510 | 8 | 10/11 |
| socks5://109.199.105.194:1080 | FR | 2478 | 8 | 8/8 |
| http://114.94.148.37:18080 | CN | 1044 | 7 | 9/10 |
| http://190.0.246.210:4040 | CO | 2930 | 7 | 9/10 |
| http://95.211.64.139:8886 | NL | 1803 | 7 | 7/7 |
| http://216.106.182.177:3128 | US | 525 | 7 | 10/11 |
| socks4://151.115.99.193:10006 | PL | 6671 | 7 | 9/11 |
| socks5://47.250.211.53:1080 | MY | 1634 | 7 | 10/11 |
| socks5://45.61.129.165:9050 | US | 3941 | 7 | 9/11 |
| http://159.195.49.27:8888 | DE | 6201 | 6 | 8/11 |
| http://175.143.76.177:8181 | MY | 5097 | 6 | 10/11 |
| socks5://59.152.97.233:1080 | BD | 5955 | 6 | 8/9 |
| socks5://144.91.111.48:1088 | FR | 1844 | 6 | 9/11 |
| http://201.116.64.226:7734 | MX | 1423 | 5 | 6/7 |
| http://109.94.1.23:4050 | RU | 4050 | 5 | 10/11 |
| socks4://89.169.168.25:6101 | RU | 4422 | 5 | 6/11 |
| socks5://59.38.113.185:20000 | CN | 1783 | 5 | 9/11 |
| socks5://112.90.88.102:20000 | CN | 1243 | 5 | 5/5 |
| socks5://89.208.106.37:32712 | NL | 1315 | 5 | 6/7 |
| socks5://62.113.113.114:1080 | RU | 7622 | 5 | 7/11 |
| socks5://144.24.47.42:1080 | US | 3172 | 5 | 6/7 |
| http://47.107.82.96:30051 | CN | 1457 | 4 | 4/4 |
| http://204.76.203.9:8080 | NL | 734 | 4 | 4/4 |
| http://79.137.192.65:30081 | RU | 4280 | 4 | 7/11 |
| http://195.158.8.123:3128 | UZ | 7898 | 4 | 8/9 |
| socks5://45.194.33.12:30001 | HK | 1100 | 4 | 6/7 |
| socks5://121.169.46.116:1090 | KR | 2008 | 4 | 9/11 |
| socks5://139.28.240.201:1082 | NL | 3966 | 4 | 6/10 |
| socks5://80.93.61.39:1080 | RU | 1249 | 4 | 4/4 |
| socks5://34.229.113.62:1080 | US | 2145 | 4 | 4/4 |
| http://187.102.219.42:999 | AR | 2228 | 3 | 4/6 |
| http://101.206.186.99:8080 | CN | 5922 | 3 | 7/11 |
| http://219.142.66.244:9090 | CN | 2217 | 3 | 6/11 |
| http://212.58.132.5:8888 | GB | 1349 | 3 | 7/10 |
| http://49.156.22.42:8082 | ID | 6423 | 3 | 4/9 |
| http://103.160.205.244:8181 | ID | 6501 | 3 | 3/3 |
| http://165.99.194.184:8080 | ID | 1366 | 3 | 5/9 |
| http://14.139.235.82:3128 | IN | 2604 | 3 | 8/11 |
| http://95.211.64.139:8888 | NL | 1310 | 3 | 10/11 |
| http://144.124.227.88:3128 | NL | 1636 | 3 | 4/5 |
| http://200.123.27.122:999 | PE | 6457 | 3 | 3/3 |
| http://34.43.46.91:443 | US | 600 | 3 | 8/11 |
| http://34.43.46.91:80 | US | 524 | 3 | 8/11 |
| http://34.69.61.247:80 | US | 358 | 3 | 5/10 |
| socks4://163.192.14.135:50161 | US | 480 | 3 | 6/10 |
| socks5://147.45.66.117:1082 | DE | 1379 | 3 | 7/9 |
| socks5://37.18.73.60:5566 | RU | 1788 | 3 | 8/11 |
| socks5://195.133.53.59:10808 | RU | 2727 | 3 | 3/3 |
| socks5://43.164.3.124:1080 | TH | 1868 | 3 | 8/10 |
| http://45.232.0.2:8080 | AR | 6319 | 2 | 3/9 |
| http://168.194.34.196:9001 | AR | 1519 | 2 | 3/9 |
| http://8.138.217.152:21001 | CN | 2280 | 2 | 6/11 |
| http://47.121.139.13:3128 | CN | 2118 | 2 | 5/10 |
| http://58.254.153.146:17981 | CN | 1353 | 2 | 6/9 |
| http://45.167.125.62:999 | CO | 7354 | 2 | 3/10 |
| http://181.78.74.252:999 | CO | 822 | 2 | 2/2 |
| http://181.78.74.253:999 | CO | 832 | 2 | 2/2 |
| http://181.119.84.104:999 | CO | 6954 | 2 | 2/2 |
| http://190.7.138.78:8080 | CO | 7283 | 2 | 3/5 |
| http://157.100.26.250:999 | EC | 6231 | 2 | 2/2 |
| http://205.235.1.37:999 | EC | 3975 | 2 | 2/2 |
| http://81.168.119.85:443 | GB | 5444 | 2 | 2/2 |
| http://91.231.186.236:3128 | GB | 4493 | 2 | 2/2 |
| http://91.231.186.236:8080 | GB | 6537 | 2 | 2/2 |
| http://91.231.186.236:8181 | GB | 5239 | 2 | 2/2 |
| http://181.215.18.40:3128 | HK | 1361 | 2 | 2/2 |
| http://43.133.128.153:16012 | ID | 3552 | 2 | 7/11 |
| http://103.133.24.73:8787 | ID | 4092 | 2 | 2/2 |
| http://103.155.64.212:8080 | ID | 7037 | 2 | 2/2 |
| http://103.165.227.58:8080 | ID | 1251 | 2 | 2/2 |
| http://146.196.40.146:8080 | ID | 2326 | 2 | 3/4 |
| http://117.236.124.166:3128 | IN | 1584 | 2 | 5/11 |
| http://216.48.184.253:8080 | IN | 1315 | 2 | 2/2 |
