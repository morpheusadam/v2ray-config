# Proxy status

Generated 2026-08-16T19:52:13Z by `harvest.py`.

- **678** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1118** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **12835** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 156/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 830 |
| socks5 | 263 |
| socks4 | 25 |

| country | entries |
|---|---|
| ID | 248 |
| US | 82 |
| RU | 60 |
| CN | 50 |
| CO | 44 |
| VN | 42 |
| PH | 40 |
| BD | 35 |
| NL | 34 |
| DE | 29 |
| MX | 28 |
| VE | 27 |
| HK | 25 |
| BR | 23 |
| IN | 23 |
| SG | 22 |
| FR | 21 |
| JP | 19 |
| TR | 19 |
| EC | 18 |
| CL | 13 |
| FI | 13 |
| DO | 12 |
| TH | 12 |
| GB | 11 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-08-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 77 | 77 | 49 | 2026-08-16 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 114 | 114 | 21 | 2026-08-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 118 | 118 | 55 | 2026-08-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 93 | 2026-08-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 152 | 152 | 18 | 2026-08-16 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 164 | 164 | 26 | 2026-08-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 218 | 218 | 85 | 2026-08-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 227 | 227 | 126 | 2026-08-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 345 | 345 | 155 | 2026-08-16 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-08-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-08-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1124 | 2026-08-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1617 | 2026-08-16 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1852 | 1848 | 255 | 2026-08-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2059 | 2057 | 185 | 2026-08-16 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2502 | 2502 | 1856 | 2026-08-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2549 | 2547 | 702 | 2026-08-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2971 | 2969 | 2427 | 2026-08-16 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 5087 | 13 | 13/13 |
| http://87.251.77.29:3128 | DE | 1761 | 13 | 13/13 |
| http://103.237.102.191:11111 | DE | 2218 | 13 | 13/13 |
| http://176.111.37.5:39811 | HK | 1463 | 13 | 13/13 |
| http://1.231.81.166:3128 | KR | 2075 | 13 | 13/13 |
| http://95.211.64.139:8889 | NL | 2265 | 13 | 13/13 |
| http://95.211.174.135:3128 | NL | 2914 | 13 | 13/13 |
| http://204.76.203.9:3128 | NL | 1297 | 13 | 13/13 |
| http://185.200.188.234:10001 | RU | 2843 | 13 | 13/13 |
| http://152.42.167.241:3128 | SG | 2969 | 13 | 13/13 |
| http://202.28.194.139:31280 | TH | 2901 | 13 | 13/13 |
| http://95.3.69.222:8080 | TR | 2521 | 13 | 13/13 |
| http://64.112.184.210:3128 | US | 1284 | 13 | 13/13 |
| socks5://144.91.121.61:1088 | FR | 3304 | 13 | 13/13 |
| socks5://212.58.132.5:1080 | GB | 2159 | 13 | 13/13 |
| socks5://66.163.119.55:10006 | IT | 4876 | 13 | 13/13 |
| socks5://101.36.104.46:10808 | JP | 2030 | 13 | 13/13 |
| socks5://193.233.218.213:1080 | RU | 2567 | 13 | 13/13 |
| socks5://69.55.49.177:38182 | US | 2176 | 13 | 13/13 |
| socks5://193.25.215.182:22222 | US | 1766 | 13 | 13/13 |
| http://95.211.64.139:8887 | NL | 1258 | 12 | 12/12 |
| socks5://45.43.63.37:10808 | SG | 4138 | 11 | 12/13 |
| http://181.39.25.196:8118 | EC | 2069 | 10 | 12/13 |
| http://130.110.103.245:3128 | SA | 2407 | 10 | 12/13 |
| socks5://51.159.97.242:10006 | FR | 2737 | 10 | 12/13 |
| http://190.0.246.210:4040 | CO | 6174 | 9 | 11/12 |
| http://95.211.64.139:8886 | NL | 754 | 9 | 9/9 |
| socks4://151.115.99.193:10006 | PL | 2854 | 9 | 11/13 |
| socks4://45.61.129.165:9050 | US | 2864 | 9 | 11/13 |
| socks5://59.152.97.233:1080 | BD | 1818 | 8 | 10/11 |
| socks5://144.91.111.48:1088 | FR | 6395 | 8 | 11/13 |
| http://109.94.1.23:4050 | RU | 4285 | 7 | 12/13 |
| socks5://112.90.88.102:20000 | CN | 1270 | 7 | 7/7 |
| socks5://89.208.106.37:32712 | NL | 1812 | 7 | 8/9 |
| socks5://144.24.47.42:1080 | US | 6261 | 7 | 8/9 |
| http://204.76.203.9:8080 | NL | 801 | 6 | 6/6 |
| socks5://45.194.33.12:30001 | HK | 1132 | 6 | 8/9 |
| socks5://80.93.61.39:1080 | RU | 1251 | 6 | 6/6 |
| socks5://34.229.113.62:1080 | US | 1059 | 6 | 6/6 |
| http://101.206.186.99:8080 | CN | 7727 | 5 | 9/13 |
| http://212.58.132.5:8888 | GB | 1272 | 5 | 9/12 |
| http://165.99.194.184:8080 | ID | 2374 | 5 | 7/11 |
| http://14.139.235.82:3128 | IN | 3091 | 5 | 10/13 |
| http://95.211.64.139:8888 | NL | 1548 | 5 | 12/13 |
| http://144.124.227.88:3128 | NL | 783 | 5 | 6/7 |
| http://34.43.46.91:443 | US | 1791 | 5 | 10/13 |
| http://34.43.46.91:80 | US | 2868 | 5 | 10/13 |
| http://34.69.61.247:80 | US | 453 | 5 | 7/12 |
| http://181.78.74.252:999 | CO | 876 | 4 | 4/4 |
| http://181.78.74.253:999 | CO | 897 | 4 | 4/4 |
| http://117.236.124.166:3128 | IN | 2889 | 4 | 7/13 |
| http://38.194.246.34:999 | MX | 5597 | 4 | 4/4 |
| http://43.160.242.118:3128 | SG | 965 | 4 | 9/10 |
| http://45.66.249.187:3128 | US | 2208 | 4 | 4/4 |
| http://45.66.249.187:8080 | US | 629 | 4 | 6/8 |
| http://45.66.249.187:8181 | US | 544 | 4 | 4/4 |
| http://157.230.178.216:40000 | US | 3131 | 4 | 11/12 |
| http://165.154.162.73:8888 | US | 1600 | 4 | 8/13 |
| socks5://119.148.20.109:22122 | BD | 7216 | 4 | 4/4 |
| socks5://123.58.219.171:10808 | HK | 3647 | 4 | 12/13 |
| socks5://185.125.200.80:1090 | NL | 2039 | 4 | 4/4 |
| socks5://95.31.16.116:1081 | RU | 1196 | 4 | 4/4 |
| socks5://130.193.43.183:1080 | RU | 1209 | 4 | 4/4 |
| socks5://129.151.9.55:10808 | US | 2890 | 4 | 10/13 |
| socks5://147.45.60.139:1082 | US | 318 | 4 | 4/4 |
| http://103.147.230.130:8090 | BD | 3823 | 3 | 3/3 |
| http://138.0.143.119:8080 | BR | 7760 | 3 | 3/3 |
| http://112.74.101.87:9999 | CN | 1873 | 3 | 3/3 |
| http://122.246.3.12:17981 | CN | 1735 | 3 | 4/7 |
| http://186.148.162.155:999 | CO | 2782 | 3 | 5/6 |
| http://38.75.82.212:999 | DO | 3240 | 3 | 4/7 |
| http://181.78.200.27:999 | EC | 6502 | 3 | 4/9 |
| http://176.57.189.138:3128 | FR | 1137 | 3 | 7/8 |
| http://43.99.100.108:3128 | HK | 1776 | 3 | 12/13 |
| http://113.11.179.134:8080 | ID | 6060 | 3 | 3/3 |
| http://114.9.55.102:1111 | ID | 2644 | 3 | 3/3 |
| http://157.15.44.82:8085 | ID | 6107 | 3 | 3/3 |
| http://46.247.41.222:443 | KZ | 3604 | 3 | 3/3 |
| http://205.164.192.115:999 | MX | 7529 | 3 | 9/11 |
| http://85.193.65.88:8888 | RU | 2899 | 3 | 3/3 |
| http://131.222.252.181:8080 | TR | 1339 | 3 | 3/3 |
| http://174.137.134.182:2999 | US | 4068 | 3 | 11/12 |
| http://190.97.229.118:999 | VE | 2814 | 3 | 3/3 |
| http://190.97.236.128:999 | VE | 837 | 3 | 3/3 |
| http://190.97.236.129:999 | VE | 834 | 3 | 3/3 |
| socks4://95.85.233.144:18443 | DE | 4457 | 3 | 8/13 |
| socks5://112.28.149.152:8443 | CN | 2443 | 3 | 7/13 |
| socks5://45.144.54.40:1080 | DE | 2369 | 3 | 8/13 |
| socks5://150.242.218.137:1080 | HK | 4161 | 3 | 5/7 |
| socks5://160.22.200.60:69 | ID | 3658 | 3 | 3/3 |
| socks5://101.36.104.239:10808 | JP | 2455 | 3 | 12/13 |
| socks5://144.31.207.141:1080 | NL | 1105 | 3 | 3/3 |
| socks5://130.49.153.135:1088 | RU | 2729 | 3 | 3/3 |
| http://123.0.26.73:10000 | BD | 6038 | 2 | 5/11 |
| http://45.180.84.105:443 | BR | 6589 | 2 | 3/7 |
| http://177.184.195.168:8080 | BR | 4281 | 2 | 4/11 |
| http://179.48.80.9:8085 | BR | 6093 | 2 | 4/5 |
| http://179.189.126.46:8080 | BR | 4003 | 2 | 2/2 |
| http://45.239.208.5:999 | CL | 2981 | 2 | 3/5 |
| http://115.231.181.40:8128 | CN | 1448 | 2 | 7/12 |
