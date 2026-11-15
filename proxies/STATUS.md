# Proxy status

Generated 2026-11-15T23:30:29Z by `harvest.py`.

- **1176** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3342** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33704** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 79/600 (13%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2366 |
| socks5 | 965 |
| socks4 | 11 |

| country | entries |
|---|---|
| NL | 754 |
| ID | 706 |
| ?? | 189 |
| PH | 120 |
| US | 119 |
| CO | 108 |
| MX | 106 |
| BR | 77 |
| TH | 67 |
| IN | 65 |
| TR | 65 |
| VE | 64 |
| BD | 59 |
| CN | 59 |
| AR | 47 |
| RU | 47 |
| VN | 44 |
| DO | 42 |
| ZA | 37 |
| DE | 34 |
| EC | 34 |
| SG | 32 |
| JP | 27 |
| PE | 27 |
| PK | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 5 | 2026-11-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 89 | 89 | 7 | 2026-11-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 93 | 93 | 22 | 2026-11-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 108 | 108 | 24 | 2026-11-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 149 | 149 | 9 | 2026-11-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 62 | 2026-11-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 331 | 331 | 224 | 2026-11-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 340 | 340 | 59 | 2026-11-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 360 | 360 | 183 | 2026-11-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-11-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1134 | 2026-11-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1705 | 1705 | 183 | 2026-11-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1582 | 2026-11-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2263 | 2263 | 677 | 2026-11-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2283 | 2283 | 480 | 2026-11-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2390 | 2390 | 1432 | 2026-11-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5399 | 5399 | 4122 | 2026-11-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10964 | 10964 | 1840 | 2026-11-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 2260 | 65 | 175/194 |
| http://34.43.46.91:80 | US | 2671 | 64 | 188/194 |
| http://130.110.103.245:3128 | SA | 2399 | 40 | 176/194 |
| http://45.189.57.114:3129 | EC | 1160 | 36 | 36/36 |
| http://45.186.6.104:3128 | EC | 976 | 24 | 163/172 |
| http://38.180.18.103:3128 | BE | 1193 | 23 | 23/23 |
| http://27.147.155.206:12051 | BD | 2335 | 14 | 14/14 |
| http://167.172.76.176:9090 | SG | 1078 | 10 | 114/155 |
| http://101.251.204.174:8080 | CN | 2015 | 8 | 101/180 |
| http://177.234.217.235:999 | EC | 3260 | 8 | 84/163 |
| http://104.129.203.85:9480 | US | 264 | 8 | 8/8 |
| http://54.36.150.233:3128 | FR | 2056 | 6 | 12/16 |
| http://141.94.22.37:3128 | FR | 1594 | 6 | 9/10 |
| http://34.100.244.79:80 | IN | 1790 | 6 | 6/6 |
| http://188.166.178.163:3129 | SG | 1477 | 6 | 6/6 |
| http://200.59.191.27:999 | VE | 6346 | 6 | 129/189 |
| socks5://37.18.73.60:5566 | RU | 4050 | 6 | 42/91 |
| socks5://188.166.178.163:1088 | SG | 1987 | 6 | 6/6 |
| socks5://116.101.73.52:1057 | VN | 7478 | 6 | 6/6 |
| http://190.123.83.137:999 | AR | 4224 | 5 | 27/31 |
| http://184.75.221.82:3118 | CA | 2673 | 4 | 138/159 |
| http://181.74.82.91:999 | CL | 3172 | 4 | 32/153 |
| http://45.65.138.48:999 | CO | 4134 | 4 | 94/194 |
| http://181.129.183.19:53281 | CO | 5399 | 4 | 43/189 |
| http://190.71.72.85:2525 | CO | 1270 | 4 | 37/79 |
| http://103.237.102.191:11111 | DE | 2096 | 4 | 183/194 |
| http://45.86.72.52:8080 | US | 7721 | 4 | 6/8 |
| socks5://118.179.93.24:9090 | BD | 3613 | 4 | 42/142 |
| socks5://45.74.31.47:4817 | NL | 1781 | 4 | 4/4 |
| socks5://107.174.30.92:1080 | US | 3443 | 4 | 50/90 |
| http://38.226.251.66:999 | AR | 5559 | 3 | 17/104 |
| http://102.244.78.61:8083 | CM | 1970 | 3 | 65/82 |
| http://102.244.78.61:8084 | CM | 1678 | 3 | 63/82 |
| http://102.244.78.61:8086 | CM | 1978 | 3 | 64/82 |
| http://102.244.78.61:8089 | CM | 1695 | 3 | 66/82 |
| http://8.242.153.166:999 | CO | 6196 | 3 | 8/52 |
| http://190.12.150.244:999 | EC | 4940 | 3 | 140/190 |
| http://45.155.226.177:3128 | HK | 1731 | 3 | 8/10 |
| http://103.144.54.35:8082 | ID | 6962 | 3 | 42/117 |
| http://103.176.96.32:8082 | ID | 3469 | 3 | 45/187 |
| http://151.158.133.147:8080 | ID | 6261 | 3 | 21/47 |
| http://157.66.51.201:8080 | ID | 7062 | 3 | 46/191 |
| http://160.22.198.17:8082 | ID | 3601 | 3 | 48/186 |
| http://163.61.187.18:7777 | ID | 5988 | 3 | 9/20 |
| http://65.20.230.118:9090 | IQ | 3451 | 3 | 12/59 |
| http://148.230.4.146:999 | MX | 6226 | 3 | 52/186 |
| http://122.2.79.174:8082 | PH | 5362 | 3 | 21/81 |
| http://124.83.97.51:8081 | PH | 5955 | 3 | 7/24 |
| http://128.199.116.219:9090 | SG | 1145 | 3 | 88/113 |
| http://3.21.156.147:8097 | US | 2436 | 3 | 15/34 |
| http://13.245.183.150:8182 | ZA | 2499 | 3 | 47/162 |
| http://187.33.150.169:3128 | ?? | 956 | 3 | 3/3 |
| http://211.188.50.146:80 | ?? | 1145 | 3 | 3/3 |
| http://211.188.53.248:80 | ?? | 4310 | 3 | 3/3 |
| http://211.188.55.218:80 | ?? | 1124 | 3 | 3/3 |
| http://211.188.59.191:80 | ?? | 1242 | 3 | 3/3 |
| http://211.188.60.84:80 | ?? | 1319 | 3 | 3/3 |
| socks5://200.4.107.137:1080 | BR | 6523 | 3 | 5/24 |
| socks5://101.36.104.239:10808 | JP | 2388 | 3 | 160/194 |
| socks5://203.189.135.73:1080 | KH | 2887 | 3 | 41/176 |
| socks5://45.74.31.40:4112 | NL | 4222 | 3 | 6/34 |
| socks5://8.219.122.8:9999 | SG | 2923 | 3 | 35/84 |
| socks5://193.218.118.128:1080 | UA | 3145 | 3 | 35/50 |
| socks5://45.61.129.165:9050 | US | 2875 | 3 | 147/194 |
| socks5://47.251.166.203:1080 | US | 501 | 3 | 7/12 |
| socks5://91.143.161.163:1080 | ?? | 3386 | 3 | 4/5 |
| socks5://129.222.104.186:1080 | ?? | 7013 | 3 | 4/14 |
| http://200.110.218.11:999 | AR | 6741 | 2 | 33/154 |
| http://85.132.108.42:3128 | AZ | 3799 | 2 | 9/12 |
| http://16.174.124.173:11672 | CA | 4744 | 2 | 5/24 |
| http://16.174.124.173:425 | CA | 4613 | 2 | 41/162 |
| http://16.174.124.173:4499 | CA | 1752 | 2 | 23/96 |
| http://40.177.104.199:48086 | CA | 4509 | 2 | 50/161 |
| http://102.244.78.61:8080 | CM | 1768 | 2 | 67/83 |
| http://102.244.78.61:8088 | CM | 2024 | 2 | 64/82 |
| http://47.107.107.24:80 | CN | 1897 | 2 | 61/162 |
| http://123.121.113.161:8888 | CN | 5415 | 2 | 12/19 |
| http://123.121.114.100:8888 | CN | 4208 | 2 | 13/26 |
| http://123.121.122.28:8888 | CN | 1848 | 2 | 88/143 |
| http://221.223.203.55:8888 | CN | 2497 | 2 | 5/6 |
| http://38.211.76.193:999 | CO | 4230 | 2 | 5/17 |
| http://18.157.159.247:21196 | DE | 2715 | 2 | 3/19 |
| http://63.180.203.233:20854 | DE | 4353 | 2 | 2/2 |
| http://38.50.165.123:999 | DO | 6559 | 2 | 48/179 |
| http://38.50.165.124:999 | DO | 4205 | 2 | 35/131 |
| http://38.76.251.115:999 | DO | 6906 | 2 | 6/10 |
| http://185.27.144.74:999 | DO | 6689 | 2 | 14/59 |
| http://15.217.107.97:40207 | ES | 3245 | 2 | 10/30 |
| http://35.43.246.3:28152 | ES | 1608 | 2 | 5/9 |
| http://35.43.246.3:31071 | ES | 4665 | 2 | 5/8 |
| http://43.99.60.244:8089 | HK | 933 | 2 | 76/144 |
| http://15.232.45.244:56713 | ID | 5116 | 2 | 6/37 |
| http://103.51.205.117:8090 | ID | 7475 | 2 | 3/22 |
| http://103.97.141.142:8080 | ID | 5260 | 2 | 15/30 |
| http://103.144.18.84:3128 | ID | 7319 | 2 | 9/29 |
| http://103.147.247.203:8080 | ID | 6877 | 2 | 20/61 |
| http://103.173.138.225:8080 | ID | 7189 | 2 | 14/27 |
| http://103.173.139.22:8080 | ID | 2847 | 2 | 23/105 |
| http://103.174.237.190:3125 | ID | 5673 | 2 | 31/176 |
| http://103.176.96.131:8082 | ID | 6426 | 2 | 18/70 |
