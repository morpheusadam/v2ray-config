# Proxy status

Generated 2026-08-14T20:08:05Z by `harvest.py`.

- **550** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **869** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11924** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 162/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 657 |
| socks5 | 200 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 166 |
| US | 66 |
| CN | 40 |
| VN | 40 |
| RU | 38 |
| PH | 33 |
| BD | 30 |
| NL | 30 |
| CO | 29 |
| FR | 27 |
| DE | 23 |
| IN | 23 |
| MX | 23 |
| SG | 19 |
| BR | 17 |
| JP | 17 |
| TR | 17 |
| HK | 16 |
| DO | 12 |
| TH | 12 |
| EC | 11 |
| VE | 11 |
| PE | 8 |
| AU | 7 |
| CL | 7 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 3 | 2026-08-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 86 | 86 | 14 | 2026-08-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 92 | 92 | 60 | 2026-08-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 128 | 128 | 53 | 2026-08-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-08-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 152 | 152 | 23 | 2026-08-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 159 | 159 | 32 | 2026-08-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 236 | 236 | 148 | 2026-08-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 237 | 237 | 80 | 2026-08-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 505 | 505 | 271 | 2026-08-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 533 | 2026-08-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-08-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1133 | 2026-08-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1623 | 2026-08-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1866 | 1862 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1965 | 1963 | 172 | 2026-08-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2526 | 2524 | 741 | 2026-08-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2596 | 2596 | 1834 | 2026-08-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2750 | 2748 | 2340 | 2026-08-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2285 | 9 | 9/9 |
| http://87.251.77.29:3128 | DE | 1093 | 9 | 9/9 |
| http://103.237.102.191:11111 | DE | 1107 | 9 | 9/9 |
| http://43.99.100.108:3128 | HK | 1351 | 9 | 9/9 |
| http://176.111.37.5:39811 | HK | 2277 | 9 | 9/9 |
| http://176.111.37.216:39811 | HK | 2023 | 9 | 9/9 |
| http://103.130.61.61:8081 | ID | 2439 | 9 | 9/9 |
| http://1.231.81.166:3128 | KR | 1893 | 9 | 9/9 |
| http://95.211.64.139:8889 | NL | 2200 | 9 | 9/9 |
| http://95.211.174.135:3128 | NL | 2136 | 9 | 9/9 |
| http://204.76.203.9:3128 | NL | 4520 | 9 | 9/9 |
| http://185.200.188.234:10001 | RU | 1508 | 9 | 9/9 |
| http://152.42.167.241:3128 | SG | 6864 | 9 | 9/9 |
| http://202.28.194.139:31280 | TH | 2825 | 9 | 9/9 |
| http://95.3.69.222:8080 | TR | 1860 | 9 | 9/9 |
| http://43.153.82.179:8888 | US | 3834 | 9 | 9/9 |
| http://64.112.184.210:3128 | US | 559 | 9 | 9/9 |
| socks5://66.163.118.99:10006 | ES | 6091 | 9 | 9/9 |
| socks5://144.91.121.61:1088 | FR | 1972 | 9 | 9/9 |
| socks5://212.58.132.5:1080 | GB | 2169 | 9 | 9/9 |
| socks5://66.163.119.55:10006 | IT | 3427 | 9 | 9/9 |
| socks5://149.62.186.244:1080 | IT | 4503 | 9 | 9/9 |
| socks5://101.36.104.46:10808 | JP | 1000 | 9 | 9/9 |
| socks5://101.36.104.239:10808 | JP | 1012 | 9 | 9/9 |
| socks5://193.233.218.213:1080 | RU | 1717 | 9 | 9/9 |
| socks5://69.55.49.177:38182 | US | 845 | 9 | 9/9 |
| socks5://193.25.215.182:22222 | US | 859 | 9 | 9/9 |
| http://185.191.239.248:3128 | CH | 5086 | 8 | 8/8 |
| http://95.211.64.139:8887 | NL | 1208 | 8 | 8/8 |
| http://174.137.134.182:2999 | US | 2529 | 8 | 8/8 |
| http://153.80.240.37:8080 | NL | 5017 | 7 | 8/9 |
| http://34.94.46.8:80 | US | 101 | 7 | 7/7 |
| socks5://45.43.63.37:10808 | SG | 3903 | 7 | 8/9 |
| http://181.39.25.196:8118 | EC | 1259 | 6 | 8/9 |
| http://130.110.103.245:3128 | SA | 1762 | 6 | 8/9 |
| socks5://51.159.97.242:10006 | FR | 2282 | 6 | 8/9 |
| socks5://109.199.105.194:1080 | FR | 2250 | 6 | 6/6 |
| socks5://43.164.136.189:1080 | KR | 1792 | 6 | 7/9 |
| socks5://45.10.42.68:1080 | NL | 1088 | 6 | 6/6 |
| socks5://5.249.165.195:20000 | US | 3462 | 6 | 6/6 |
| http://114.94.148.37:18080 | CN | 1461 | 5 | 7/8 |
| http://190.0.246.210:4040 | CO | 2111 | 5 | 7/8 |
| http://190.12.150.244:999 | EC | 3182 | 5 | 5/5 |
| http://37.59.125.131:8888 | FR | 2007 | 5 | 8/9 |
| http://205.164.192.115:999 | MX | 2266 | 5 | 6/7 |
| http://95.211.64.139:8886 | NL | 803 | 5 | 5/5 |
| http://209.7.244.3:5999 | US | 1384 | 5 | 5/5 |
| http://216.106.182.177:3128 | US | 785 | 5 | 8/9 |
| socks4://151.115.99.193:10006 | PL | 2605 | 5 | 7/9 |
| socks4://45.61.129.165:9050 | US | 1999 | 5 | 7/9 |
| socks5://213.136.92.91:1080 | FR | 1206 | 5 | 6/9 |
| socks5://47.250.211.53:1080 | MY | 1701 | 5 | 8/9 |
| http://123.57.213.24:3539 | CN | 5092 | 4 | 5/8 |
| http://159.195.49.27:8888 | DE | 4773 | 4 | 6/9 |
| http://176.57.189.138:3128 | FR | 2474 | 4 | 4/4 |
| http://43.203.140.58:23536 | KR | 3925 | 4 | 4/4 |
| http://175.136.239.173:8181 | MY | 2928 | 4 | 7/9 |
| http://175.139.255.25:8181 | MY | 4441 | 4 | 8/9 |
| http://175.143.76.177:8181 | MY | 2219 | 4 | 8/9 |
| http://216.125.22.3:5999 | US | 1339 | 4 | 4/4 |
| socks5://59.152.97.233:1080 | BD | 1946 | 4 | 6/7 |
| socks5://144.91.111.48:1088 | FR | 3096 | 4 | 7/9 |
| socks5://185.185.80.58:1088 | FR | 1363 | 4 | 7/8 |
| http://114.236.137.41:21000 | CN | 1546 | 3 | 8/9 |
| http://103.61.234.186:8180 | ID | 2482 | 3 | 5/6 |
| http://37.191.95.202:80 | IR | 6783 | 3 | 4/5 |
| http://201.116.64.226:7734 | MX | 3331 | 3 | 4/5 |
| http://109.94.1.23:4050 | RU | 5889 | 3 | 8/9 |
| http://5.161.50.82:8118 | US | 5581 | 3 | 4/8 |
| socks4://95.85.233.144:18443 | DE | 2801 | 3 | 5/9 |
| socks4://89.169.168.25:6101 | RU | 3586 | 3 | 4/9 |
| socks5://182.163.96.66:1080 | BD | 7055 | 3 | 3/3 |
| socks5://59.38.113.185:20000 | CN | 3615 | 3 | 7/9 |
| socks5://112.90.88.102:20000 | CN | 1168 | 3 | 3/3 |
| socks5://151.243.224.12:1080 | DE | 949 | 3 | 3/3 |
| socks5://38.76.215.92:1080 | HK | 3952 | 3 | 6/9 |
| socks5://144.24.111.128:1088 | IN | 1966 | 3 | 7/9 |
| socks5://89.208.106.37:32712 | NL | 1538 | 3 | 4/5 |
| socks5://62.113.113.114:1080 | RU | 4489 | 3 | 5/9 |
| socks5://144.24.47.42:1080 | US | 3295 | 3 | 4/5 |
| http://103.150.49.90:8090 | BD | 3113 | 2 | 2/2 |
| http://115.127.95.82:8080 | BD | 5408 | 2 | 3/4 |
| http://5.104.183.25:8080 | BG | 1099 | 2 | 2/2 |
| http://45.175.59.17:61950 | BR | 7863 | 2 | 2/2 |
| http://186.227.119.91:8080 | BR | 5080 | 2 | 3/4 |
| http://45.161.112.227:999 | CL | 2898 | 2 | 2/2 |
| http://47.107.82.96:30051 | CN | 1651 | 2 | 2/2 |
| http://186.148.162.155:999 | CO | 5182 | 2 | 2/2 |
| http://185.248.179.99:8080 | CZ | 7473 | 2 | 4/8 |
| http://38.44.17.142:999 | DO | 5741 | 2 | 2/2 |
| http://45.176.99.58:999 | DO | 2214 | 2 | 3/4 |
| http://152.0.51.69:8080 | DO | 7839 | 2 | 2/2 |
| http://18.170.25.193:53656 | GB | 5308 | 2 | 4/9 |
| http://181.189.27.163:999 | GT | 7960 | 2 | 4/5 |
| http://38.52.148.18:3125 | ID | 4712 | 2 | 2/2 |
| http://103.80.83.27:8080 | ID | 3468 | 2 | 2/2 |
| http://103.80.214.108:8080 | ID | 5437 | 2 | 2/2 |
| http://103.106.216.231:8097 | ID | 1341 | 2 | 3/4 |
| http://103.166.9.50:3128 | ID | 3300 | 2 | 2/2 |
| http://103.169.38.186:8080 | ID | 3807 | 2 | 2/2 |
