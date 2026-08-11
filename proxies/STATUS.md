# Proxy status

Generated 2026-08-11T20:22:06Z by `harvest.py`.

- **619** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **656** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11462** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 327/600 (55%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 463 |
| socks5 | 181 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 130 |
| US | 52 |
| RU | 33 |
| CN | 31 |
| NL | 29 |
| PH | 27 |
| BD | 22 |
| VN | 19 |
| CO | 18 |
| DE | 18 |
| SG | 17 |
| BR | 16 |
| FR | 16 |
| VE | 16 |
| HK | 15 |
| MX | 13 |
| TR | 11 |
| IN | 9 |
| KH | 9 |
| TH | 9 |
| AR | 8 |
| JP | 8 |
| IR | 7 |
| IT | 7 |
| MY | 6 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 11 | 11 | 5 | 2026-08-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 84 | 2026-08-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 105 | 105 | 88 | 2026-08-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 121 | 121 | 62 | 2026-08-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 124 | 124 | 31 | 2026-08-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 93 | 2026-08-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 200 | 200 | 41 | 2026-08-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 216 | 216 | 142 | 2026-08-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 221 | 221 | 34 | 2026-08-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 286 | 286 | 112 | 2026-08-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 537 | 2026-08-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-08-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 713 | 713 | 498 | 2026-08-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1132 | 2026-08-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1641 | 2026-08-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1845 | 1844 | 0 | 2026-08-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1937 | 1936 | 222 | 2026-08-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2400 | 2399 | 687 | 2026-08-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2593 | 2593 | 2033 | 2026-08-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2943 | 2942 | 2744 | 2026-08-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://8.138.217.152:21001 | CN | 3395 | 3 | 3/3 |
| http://114.236.137.41:21000 | CN | 1616 | 3 | 3/3 |
| http://119.188.131.55:17981 | CN | 1698 | 3 | 3/3 |
| http://190.0.246.211:4040 | CO | 2377 | 3 | 3/3 |
| http://87.251.77.29:3128 | DE | 1037 | 3 | 3/3 |
| http://103.237.102.191:11111 | DE | 893 | 3 | 3/3 |
| http://37.59.125.131:8888 | FR | 1328 | 3 | 3/3 |
| http://169.58.85.194:8080 | FR | 1115 | 3 | 3/3 |
| http://82.102.11.164:3460 | GB | 1390 | 3 | 3/3 |
| http://43.99.100.108:3128 | HK | 1428 | 3 | 3/3 |
| http://172.110.220.36:3128 | HK | 1019 | 3 | 3/3 |
| http://176.111.37.5:39811 | HK | 1111 | 3 | 3/3 |
| http://176.111.37.216:39811 | HK | 1160 | 3 | 3/3 |
| http://103.130.61.61:8081 | ID | 1580 | 3 | 3/3 |
| http://5.200.72.62:3128 | IR | 2214 | 3 | 3/3 |
| http://178.252.180.59:10909 | IR | 1475 | 3 | 3/3 |
| http://1.231.81.166:3128 | KR | 1260 | 3 | 3/3 |
| http://175.139.255.25:8181 | MY | 3098 | 3 | 3/3 |
| http://175.143.76.177:8181 | MY | 6346 | 3 | 3/3 |
| http://88.210.11.216:8989 | NL | 1417 | 3 | 3/3 |
| http://95.211.64.139:8888 | NL | 1178 | 3 | 3/3 |
| http://95.211.64.139:8889 | NL | 1097 | 3 | 3/3 |
| http://95.211.174.135:3128 | NL | 1168 | 3 | 3/3 |
| http://144.178.199.118:8443 | NL | 1073 | 3 | 3/3 |
| http://147.45.166.120:3333 | NL | 765 | 3 | 3/3 |
| http://195.133.14.222:49152 | NL | 845 | 3 | 3/3 |
| http://204.76.203.9:3128 | NL | 900 | 3 | 3/3 |
| http://109.94.1.23:4050 | RU | 1066 | 3 | 3/3 |
| http://185.200.188.234:10001 | RU | 1214 | 3 | 3/3 |
| http://143.198.87.117:8888 | SG | 3506 | 3 | 3/3 |
| http://152.42.167.241:3128 | SG | 1242 | 3 | 3/3 |
| http://47.81.56.193:8888 | TH | 1580 | 3 | 3/3 |
| http://202.28.194.139:31280 | TH | 2126 | 3 | 3/3 |
| http://95.3.69.222:8080 | TR | 1437 | 3 | 3/3 |
| http://34.43.46.91:443 | US | 386 | 3 | 3/3 |
| http://34.43.46.91:80 | US | 497 | 3 | 3/3 |
| http://43.153.82.179:8888 | US | 7436 | 3 | 3/3 |
| http://64.112.184.210:3128 | US | 566 | 3 | 3/3 |
| http://216.106.182.177:3128 | US | 429 | 3 | 3/3 |
| http://38.76.9.0:999 | VE | 1193 | 3 | 3/3 |
| http://113.160.132.26:8080 | VN | 1729 | 3 | 3/3 |
| socks4://216.106.179.216:49430 | US | 5406 | 3 | 3/3 |
| socks5://144.22.165.206:1088 | BR | 2182 | 3 | 3/3 |
| socks5://38.49.210.79:40000 | CA | 461 | 3 | 3/3 |
| socks5://45.144.54.40:1080 | DE | 1167 | 3 | 3/3 |
| socks5://66.163.118.99:10006 | ES | 1058 | 3 | 3/3 |
| socks5://144.91.111.48:1088 | FR | 1832 | 3 | 3/3 |
| socks5://144.91.121.61:1088 | FR | 1459 | 3 | 3/3 |
| socks5://194.163.174.78:1085 | FR | 4250 | 3 | 3/3 |
| socks5://212.58.132.5:1080 | GB | 1838 | 3 | 3/3 |
| socks5://123.58.219.171:10808 | HK | 1506 | 3 | 3/3 |
| socks5://103.174.122.197:8199 | ID | 5780 | 3 | 3/3 |
| socks5://144.24.111.128:1088 | IN | 1650 | 3 | 3/3 |
| socks5://66.163.119.55:10006 | IT | 5078 | 3 | 3/3 |
| socks5://149.62.186.244:1080 | IT | 2758 | 3 | 3/3 |
| socks5://101.36.104.46:10808 | JP | 1331 | 3 | 3/3 |
| socks5://101.36.104.239:10808 | JP | 1707 | 3 | 3/3 |
| socks5://195.135.255.98:1080 | LV | 4966 | 3 | 3/3 |
| socks5://47.250.211.53:1080 | MY | 1785 | 3 | 3/3 |
| socks5://193.233.218.213:1080 | RU | 1162 | 3 | 3/3 |
| socks5://43.134.58.45:1080 | SG | 3249 | 3 | 3/3 |
| socks5://43.156.84.41:10808 | SG | 1662 | 3 | 3/3 |
| socks5://43.163.122.46:8080 | SG | 3877 | 3 | 3/3 |
| socks5://43.162.94.99:1080 | US | 1775 | 3 | 3/3 |
| socks5://69.55.49.177:38182 | US | 798 | 3 | 3/3 |
| socks5://129.151.9.55:10808 | US | 3196 | 3 | 3/3 |
| socks5://147.45.60.124:1082 | US | 4401 | 3 | 3/3 |
| socks5://193.25.215.182:22222 | US | 1454 | 3 | 3/3 |
| http://177.19.167.242:80 | BR | 6279 | 2 | 2/2 |
| http://185.191.239.248:3128 | CH | 1110 | 2 | 2/2 |
| http://38.7.195.53:999 | CL | 5707 | 2 | 2/2 |
| http://47.121.139.13:3128 | CN | 2156 | 2 | 2/2 |
| http://112.64.135.45:8080 | CN | 1778 | 2 | 2/2 |
| http://114.94.148.37:18080 | CN | 1990 | 2 | 2/2 |
| http://115.231.181.40:8128 | CN | 1531 | 2 | 2/2 |
| http://190.0.246.210:4040 | CO | 957 | 2 | 2/2 |
| http://185.248.179.99:8080 | CZ | 7708 | 2 | 2/2 |
| http://195.133.65.238:10909 | DE | 3230 | 2 | 2/2 |
| http://185.236.25.231:8080 | ES | 909 | 2 | 2/2 |
| http://103.123.85.89:8080 | ID | 3380 | 2 | 2/2 |
| http://103.155.65.194:80 | ID | 4734 | 2 | 2/2 |
| http://103.155.246.42:8080 | ID | 7129 | 2 | 2/2 |
| http://103.157.58.49:8080 | ID | 2534 | 2 | 2/2 |
| http://45.43.60.220:8080 | JP | 3512 | 2 | 2/2 |
| http://140.238.32.108:3128 | JP | 1832 | 2 | 2/2 |
| http://177.224.225.7:3128 | MX | 1647 | 2 | 2/2 |
| http://95.211.64.139:8887 | NL | 1246 | 2 | 2/2 |
| http://112.203.207.111:8082 | PH | 4967 | 2 | 2/2 |
| http://180.191.125.28:8081 | PH | 7617 | 2 | 2/2 |
| http://180.191.231.149:8082 | PH | 6256 | 2 | 2/2 |
| http://180.191.232.48:5050 | PH | 5695 | 2 | 2/2 |
| http://180.191.254.36:8181 | PH | 6949 | 2 | 2/2 |
| http://185.238.238.37:58080 | PL | 5717 | 2 | 2/2 |
| http://184.82.138.156:8081 | TH | 6023 | 2 | 2/2 |
| http://203.150.128.134:8080 | TH | 4392 | 2 | 2/2 |
| http://178.18.207.85:8888 | TR | 1219 | 2 | 2/2 |
| http://154.219.125.230:3128 | US | 359 | 2 | 2/2 |
| http://157.230.178.216:40000 | US | 801 | 2 | 2/2 |
| http://162.214.74.29:3128 | US | 5627 | 2 | 2/2 |
| http://162.214.159.94:3128 | US | 5378 | 2 | 2/2 |
