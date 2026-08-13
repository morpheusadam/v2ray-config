# Proxy status

Generated 2026-08-13T20:17:26Z by `harvest.py`.

- **548** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **891** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11905** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 176/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 661 |
| socks5 | 208 |
| socks4 | 22 |

| country | entries |
|---|---|
| ID | 192 |
| US | 75 |
| CN | 52 |
| VN | 42 |
| RU | 40 |
| FR | 29 |
| BD | 26 |
| DE | 26 |
| NL | 26 |
| PH | 26 |
| SG | 24 |
| CO | 23 |
| BR | 22 |
| VE | 21 |
| IN | 18 |
| HK | 16 |
| JP | 16 |
| MX | 15 |
| TR | 14 |
| TH | 10 |
| EC | 9 |
| KR | 9 |
| PE | 9 |
| FI | 8 |
| DO | 7 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 4 | 2026-08-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-08-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 107 | 107 | 54 | 2026-08-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 109 | 109 | 27 | 2026-08-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 125 | 125 | 89 | 2026-08-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 126 | 126 | 72 | 2026-08-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 137 | 137 | 27 | 2026-08-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 100 | 2026-08-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 157 | 157 | 21 | 2026-08-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 205 | 205 | 80 | 2026-08-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 513 | 513 | 277 | 2026-08-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 534 | 2026-08-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-08-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1150 | 2026-08-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1622 | 2026-08-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1897 | 1893 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2079 | 2077 | 200 | 2026-08-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2458 | 2456 | 737 | 2026-08-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2470 | 2470 | 2009 | 2026-08-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2863 | 2861 | 2483 | 2026-08-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 4211 | 7 | 7/7 |
| http://87.251.77.29:3128 | DE | 1093 | 7 | 7/7 |
| http://103.237.102.191:11111 | DE | 1141 | 7 | 7/7 |
| http://43.99.100.108:3128 | HK | 2405 | 7 | 7/7 |
| http://176.111.37.5:39811 | HK | 952 | 7 | 7/7 |
| http://176.111.37.216:39811 | HK | 1023 | 7 | 7/7 |
| http://103.130.61.61:8081 | ID | 1406 | 7 | 7/7 |
| http://1.231.81.166:3128 | KR | 933 | 7 | 7/7 |
| http://88.210.11.216:8989 | NL | 1338 | 7 | 7/7 |
| http://95.211.64.139:8888 | NL | 842 | 7 | 7/7 |
| http://95.211.64.139:8889 | NL | 1178 | 7 | 7/7 |
| http://95.211.174.135:3128 | NL | 1775 | 7 | 7/7 |
| http://204.76.203.9:3128 | NL | 1287 | 7 | 7/7 |
| http://185.200.188.234:10001 | RU | 7770 | 7 | 7/7 |
| http://143.198.87.117:8888 | SG | 3294 | 7 | 7/7 |
| http://152.42.167.241:3128 | SG | 1334 | 7 | 7/7 |
| http://202.28.194.139:31280 | TH | 2162 | 7 | 7/7 |
| http://95.3.69.222:8080 | TR | 1474 | 7 | 7/7 |
| http://43.153.82.179:8888 | US | 275 | 7 | 7/7 |
| http://64.112.184.210:3128 | US | 704 | 7 | 7/7 |
| socks5://66.163.118.99:10006 | ES | 2516 | 7 | 7/7 |
| socks5://144.91.121.61:1088 | FR | 4283 | 7 | 7/7 |
| socks5://212.58.132.5:1080 | GB | 2125 | 7 | 7/7 |
| socks5://123.58.219.171:10808 | HK | 4955 | 7 | 7/7 |
| socks5://66.163.119.55:10006 | IT | 4192 | 7 | 7/7 |
| socks5://149.62.186.244:1080 | IT | 3595 | 7 | 7/7 |
| socks5://101.36.104.46:10808 | JP | 2069 | 7 | 7/7 |
| socks5://101.36.104.239:10808 | JP | 2116 | 7 | 7/7 |
| socks5://193.233.218.213:1080 | RU | 3201 | 7 | 7/7 |
| socks5://43.134.58.45:1080 | SG | 5993 | 7 | 7/7 |
| socks5://69.55.49.177:38182 | US | 1058 | 7 | 7/7 |
| socks5://193.25.215.182:22222 | US | 2034 | 7 | 7/7 |
| http://185.191.239.248:3128 | CH | 1644 | 6 | 6/6 |
| http://95.211.64.139:8887 | NL | 753 | 6 | 6/6 |
| http://157.230.178.216:40000 | US | 5381 | 6 | 6/6 |
| http://162.214.74.29:3128 | US | 4694 | 6 | 6/6 |
| http://162.214.159.94:3128 | US | 4811 | 6 | 6/6 |
| http://174.137.134.182:2999 | US | 4693 | 6 | 6/6 |
| socks5://171.25.158.95:1080 | SE | 1407 | 6 | 6/6 |
| http://152.53.20.190:20000 | DE | 1304 | 5 | 6/7 |
| http://153.80.240.37:8080 | NL | 2486 | 5 | 6/7 |
| http://34.94.46.8:80 | US | 95 | 5 | 5/5 |
| socks5://161.35.90.93:1081 | NL | 3082 | 5 | 6/7 |
| socks5://161.35.90.93:1082 | NL | 7481 | 5 | 6/7 |
| socks5://45.43.63.37:10808 | SG | 2442 | 5 | 6/7 |
| http://181.39.25.196:8118 | EC | 1068 | 4 | 6/7 |
| http://103.162.136.23:8080 | PK | 5096 | 4 | 4/4 |
| http://130.110.103.245:3128 | SA | 1532 | 4 | 6/7 |
| http://43.160.242.118:3128 | SG | 952 | 4 | 4/4 |
| socks5://191.44.118.236:1080 | DE | 934 | 4 | 4/4 |
| socks5://45.95.233.88:1082 | FR | 1892 | 4 | 4/4 |
| socks5://51.159.97.242:10006 | FR | 2453 | 4 | 6/7 |
| socks5://109.199.105.194:1080 | FR | 2447 | 4 | 4/4 |
| socks5://43.164.136.189:1080 | KR | 6578 | 4 | 5/7 |
| socks5://45.10.42.68:1080 | NL | 3580 | 4 | 4/4 |
| socks5://5.249.165.195:20000 | US | 5793 | 4 | 4/4 |
| socks5://47.85.195.135:1080 | US | 556 | 4 | 6/7 |
| socks5://107.191.44.214:1081 | US | 4795 | 4 | 6/7 |
| socks5://147.45.60.136:1082 | US | 2405 | 4 | 4/4 |
| socks5://204.152.192.13:1080 | US | 6945 | 4 | 4/4 |
| http://203.76.220.126:16464 | BD | 6039 | 3 | 3/3 |
| http://114.94.148.37:18080 | CN | 1205 | 3 | 5/6 |
| http://190.0.246.210:4040 | CO | 3414 | 3 | 5/6 |
| http://190.12.150.244:999 | EC | 7021 | 3 | 3/3 |
| http://45.144.53.63:6019 | FI | 1386 | 3 | 3/3 |
| http://37.59.125.131:8888 | FR | 2461 | 3 | 6/7 |
| http://18.170.25.193:57422 | GB | 1037 | 3 | 3/3 |
| http://82.102.11.164:3460 | GB | 1193 | 3 | 6/7 |
| http://212.58.132.5:8888 | GB | 1270 | 3 | 4/6 |
| http://36.50.56.105:8818 | ID | 5487 | 3 | 3/3 |
| http://43.133.128.153:16012 | ID | 1594 | 3 | 5/7 |
| http://45.123.143.10:8080 | ID | 2392 | 3 | 3/3 |
| http://103.28.112.172:3125 | ID | 3702 | 3 | 3/3 |
| http://103.102.12.105:8080 | ID | 6442 | 3 | 4/5 |
| http://160.187.174.121:8080 | ID | 2356 | 3 | 3/3 |
| http://45.43.60.220:8080 | JP | 6363 | 3 | 5/6 |
| http://205.164.192.115:999 | MX | 4566 | 3 | 4/5 |
| http://95.211.64.139:8886 | NL | 748 | 3 | 3/3 |
| http://176.120.28.106:8080 | RU | 2648 | 3 | 5/7 |
| http://43.156.114.4:80 | SG | 1124 | 3 | 3/3 |
| http://209.7.244.3:5999 | US | 1369 | 3 | 3/3 |
| http://216.106.182.177:3128 | US | 661 | 3 | 6/7 |
| http://216.125.22.2:5999 | US | 1361 | 3 | 3/3 |
| http://113.160.132.26:8080 | VN | 1418 | 3 | 6/7 |
| http://163.181.207.169:9999 | VN | 1123 | 3 | 4/5 |
| http://171.253.95.3:2102 | VN | 6472 | 3 | 3/3 |
| http://185.174.208.195:8080 | XK | 4168 | 3 | 4/5 |
| socks4://151.115.99.193:10006 | PL | 2736 | 3 | 5/7 |
| socks4://45.61.129.165:9050 | US | 1253 | 3 | 5/7 |
| socks5://147.45.221.112:1082 | AL | 1988 | 3 | 4/5 |
| socks5://159.195.49.27:1080 | DE | 3414 | 3 | 5/6 |
| socks5://213.136.92.91:1080 | FR | 1095 | 3 | 4/7 |
| socks5://47.250.211.53:1080 | MY | 1479 | 3 | 6/7 |
| socks5://37.18.73.60:5566 | RU | 2293 | 3 | 5/7 |
| socks5://43.164.3.124:1080 | TH | 2289 | 3 | 5/6 |
| http://163.227.144.80:8080 | BD | 4092 | 2 | 2/2 |
| http://182.160.124.174:9669 | BD | 7540 | 2 | 3/6 |
| http://170.150.202.15:8080 | BR | 5108 | 2 | 2/2 |
| http://91.92.143.148:80 | CH | 919 | 2 | 2/2 |
| http://179.57.172.172:999 | CL | 3661 | 2 | 3/6 |
