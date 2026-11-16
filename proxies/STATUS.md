# Proxy status

Generated 2026-11-16T23:05:58Z by `harvest.py`.

- **1679** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3226** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **32392** endpoints on record
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
| http | 2270 |
| socks5 | 941 |
| socks4 | 15 |

| country | entries |
|---|---|
| NL | 709 |
| ID | 678 |
| ?? | 158 |
| US | 124 |
| CO | 115 |
| MX | 114 |
| PH | 99 |
| BR | 76 |
| VE | 71 |
| TR | 68 |
| TH | 61 |
| BD | 59 |
| RU | 54 |
| IN | 53 |
| CN | 52 |
| VN | 44 |
| AR | 40 |
| EC | 37 |
| DO | 35 |
| CA | 33 |
| DE | 33 |
| SG | 33 |
| ZA | 33 |
| PE | 27 |
| PK | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-11-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 82 | 82 | 13 | 2026-11-16 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 147 | 147 | 17 | 2026-11-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 38 | 2026-11-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 59 | 2026-11-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 292 | 292 | 76 | 2026-11-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 314 | 314 | 207 | 2026-11-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 392 | 392 | 151 | 2026-11-16 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-11-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 441 | 2026-11-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 718 | 718 | 101 | 2026-11-16 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1197 | 1197 | 2 | 2026-11-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1123 | 2026-11-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1577 | 2026-11-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1808 | 1808 | 668 | 2026-11-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2223 | 2223 | 1251 | 2026-11-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2251 | 2251 | 702 | 2026-11-16 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5421 | 5421 | 4175 | 2026-11-16 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11118 | 11118 | 2142 | 2026-11-16 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 2479 | 66 | 176/195 |
| http://130.110.103.245:3128 | SA | 2465 | 41 | 177/195 |
| http://45.186.6.104:3128 | EC | 756 | 25 | 164/173 |
| http://38.180.18.103:3128 | BE | 629 | 24 | 24/24 |
| http://27.147.155.206:12051 | BD | 1760 | 15 | 15/15 |
| http://167.172.76.176:9090 | SG | 1254 | 11 | 115/156 |
| http://177.234.217.235:999 | EC | 2461 | 9 | 85/164 |
| http://104.129.203.85:9480 | US | 595 | 9 | 9/9 |
| http://54.36.150.233:3128 | FR | 611 | 7 | 13/17 |
| http://141.94.22.37:3128 | FR | 732 | 7 | 10/11 |
| http://188.166.178.163:3129 | SG | 1478 | 7 | 7/7 |
| http://200.59.191.27:999 | VE | 3938 | 7 | 130/190 |
| socks5://37.18.73.60:5566 | RU | 1595 | 7 | 43/92 |
| socks5://188.166.178.163:1088 | SG | 1506 | 7 | 7/7 |
| socks5://116.101.73.52:1057 | VN | 6808 | 7 | 7/7 |
| http://181.74.82.91:999 | CL | 3143 | 5 | 33/154 |
| http://45.65.138.48:999 | CO | 3124 | 5 | 95/195 |
| http://190.71.72.85:2525 | CO | 891 | 5 | 38/80 |
| http://103.237.102.191:11111 | DE | 3333 | 5 | 184/195 |
| socks5://107.174.30.92:1080 | US | 6569 | 5 | 51/91 |
| http://102.244.78.61:8083 | CM | 1251 | 4 | 66/83 |
| http://102.244.78.61:8084 | CM | 1267 | 4 | 64/83 |
| http://102.244.78.61:8086 | CM | 1237 | 4 | 65/83 |
| http://102.244.78.61:8089 | CM | 1261 | 4 | 67/83 |
| http://190.12.150.244:999 | EC | 2573 | 4 | 141/191 |
| http://45.155.226.177:3128 | HK | 879 | 4 | 9/11 |
| http://103.176.96.32:8082 | ID | 6412 | 4 | 46/188 |
| http://157.66.51.201:8080 | ID | 4850 | 4 | 47/192 |
| http://160.22.198.17:8082 | ID | 2381 | 4 | 49/187 |
| http://148.230.4.146:999 | MX | 5263 | 4 | 53/187 |
| http://128.199.116.219:9090 | SG | 1175 | 4 | 89/114 |
| http://211.188.50.146:80 | ?? | 1064 | 4 | 4/4 |
| http://211.188.53.248:80 | ?? | 1132 | 4 | 4/4 |
| http://211.188.55.218:80 | ?? | 1314 | 4 | 4/4 |
| http://211.188.59.191:80 | ?? | 1212 | 4 | 4/4 |
| http://211.188.60.84:80 | ?? | 1104 | 4 | 4/4 |
| socks5://101.36.104.239:10808 | JP | 3398 | 4 | 161/195 |
| socks5://129.222.104.186:1080 | NE | 2566 | 4 | 5/15 |
| socks5://193.218.118.128:1080 | UA | 5010 | 4 | 36/51 |
| socks5://47.251.166.203:1080 | US | 581 | 4 | 8/13 |
| http://16.174.124.173:4499 | CA | 1143 | 3 | 24/97 |
| http://102.244.78.61:8080 | CM | 1246 | 3 | 68/84 |
| http://102.244.78.61:8088 | CM | 1302 | 3 | 65/83 |
| http://123.121.122.28:8888 | CN | 1663 | 3 | 89/144 |
| http://221.223.203.55:8888 | CN | 3210 | 3 | 6/7 |
| http://63.180.203.233:20854 | DE | 1624 | 3 | 3/3 |
| http://38.50.165.123:999 | DO | 5155 | 3 | 49/180 |
| http://38.50.165.124:999 | DO | 4408 | 3 | 36/132 |
| http://35.43.246.3:28152 | ES | 781 | 3 | 6/10 |
| http://35.43.246.3:31071 | ES | 1488 | 3 | 6/9 |
| http://43.99.60.244:8089 | HK | 1183 | 3 | 77/145 |
| http://103.144.18.84:3128 | ID | 5182 | 3 | 10/30 |
| http://103.173.139.22:8080 | ID | 1702 | 3 | 24/106 |
| http://157.10.97.91:7000 | ID | 5664 | 3 | 19/54 |
| http://160.191.130.131:8080 | ID | 1730 | 3 | 12/35 |
| http://198.15.30.198:3125 | ID | 6385 | 3 | 24/61 |
| http://202.154.17.18:8080 | ID | 5363 | 3 | 31/179 |
| http://210.79.141.137:8080 | ID | 5210 | 3 | 23/95 |
| http://51.85.44.162:2974 | IL | 1850 | 3 | 4/22 |
| http://5.181.178.46:8080 | JP | 7356 | 3 | 15/71 |
| http://192.81.249.2:999 | MX | 3699 | 3 | 8/13 |
| http://120.28.200.84:5050 | PH | 4994 | 3 | 26/115 |
| http://126.209.110.120:8087 | PH | 5232 | 3 | 27/163 |
| http://180.191.228.36:8082 | PH | 4920 | 3 | 20/105 |
| http://1.10.248.242:80 | TH | 7463 | 3 | 13/40 |
| http://182.53.143.200:8180 | TH | 3579 | 3 | 6/33 |
| http://194.124.37.123:8080 | TR | 5410 | 3 | 6/25 |
| http://195.226.213.254:8888 | UA | 4195 | 3 | 70/193 |
| http://3.21.129.156:8000 | US | 4491 | 3 | 35/82 |
| http://71.14.23.121:8080 | US | 4797 | 3 | 13/32 |
| http://38.76.138.14:999 | VE | 4342 | 3 | 25/107 |
| http://181.225.53.141:999 | VE | 3778 | 3 | 31/164 |
| http://18.130.47.116:9080 | ?? | 6100 | 3 | 3/3 |
| http://103.152.140.182:8090 | ?? | 1891 | 3 | 3/3 |
| socks5://45.169.106.140:1086 | AR | 3616 | 3 | 10/24 |
| socks5://101.36.104.46:10808 | JP | 1726 | 3 | 162/195 |
| socks5://203.189.155.68:1080 | KH | 2453 | 3 | 47/194 |
| socks5://80.79.241.118:1080 | RU | 915 | 3 | 27/107 |
| socks5://67.204.153.223:1080 | US | 3207 | 3 | 10/39 |
| http://203.171.115.116:8080 | AF | 4034 | 2 | 6/28 |
| http://185.196.182.22:8080 | AL | 5521 | 2 | 42/174 |
| http://45.65.224.74:999 | AR | 6262 | 2 | 49/60 |
| http://45.232.0.2:8080 | AR | 2295 | 2 | 64/193 |
| http://190.15.194.72:8080 | AR | 5931 | 2 | 20/65 |
| http://16.51.5.77:16637 | AU | 4454 | 2 | 37/135 |
| http://16.51.53.116:23517 | AU | 3022 | 2 | 40/111 |
| http://27.147.142.156:12051 | BD | 5020 | 2 | 12/23 |
| http://27.147.157.125:12051 | BD | 6002 | 2 | 5/14 |
| http://16.52.81.236:54740 | CA | 4630 | 2 | 4/33 |
| http://35.183.29.62:59475 | CA | 4221 | 2 | 3/16 |
| http://56.112.92.32:4904 | CA | 5030 | 2 | 32/105 |
| http://102.244.78.61:8081 | CM | 1434 | 2 | 65/81 |
| http://102.244.78.61:8082 | CM | 1386 | 2 | 66/84 |
| http://102.244.78.61:8085 | CM | 1313 | 2 | 66/85 |
| http://102.244.78.61:8087 | CM | 1253 | 2 | 63/85 |
| http://102.244.78.61:8090 | CM | 1298 | 2 | 69/87 |
| http://1.15.53.214:8888 | CN | 6369 | 2 | 56/189 |
| http://47.110.226.74:19991 | CN | 7287 | 2 | 85/193 |
| http://123.121.122.125:8888 | CN | 2312 | 2 | 11/18 |
| http://124.128.149.84:8090 | CN | 6687 | 2 | 13/29 |
