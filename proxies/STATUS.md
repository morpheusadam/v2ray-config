# Proxy status

Generated 2026-10-22T22:44:37Z by `harvest.py`.

- **2615** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4858** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 167/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2626 |
| socks5 | 2223 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 2009 |
| ID | 767 |
| ?? | 183 |
| CO | 144 |
| MX | 127 |
| PH | 114 |
| US | 106 |
| RU | 85 |
| VE | 84 |
| BD | 83 |
| CN | 73 |
| BR | 72 |
| IN | 63 |
| DO | 61 |
| TR | 58 |
| EC | 55 |
| TH | 54 |
| AR | 47 |
| SG | 39 |
| VN | 38 |
| PK | 37 |
| PE | 35 |
| DE | 31 |
| EG | 30 |
| KH | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-10-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 125 | 125 | 34 | 2026-10-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 127 | 127 | 51 | 2026-10-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 68 | 2026-10-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 151 | 151 | 75 | 2026-10-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 188 | 188 | 56 | 2026-10-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-22 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 497 | 497 | 193 | 2026-10-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-10-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 697 | 697 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1071 | 1071 | 691 | 2026-10-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-10-22 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1733 | 1729 | 307 | 2026-10-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1592 | 2026-10-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2030 | 2028 | 743 | 2026-10-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2259 | 2257 | 1548 | 2026-10-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3024 | 3022 | 1307 | 2026-10-22 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 76031 | 76031 | 62512 | 2026-10-22 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 82736 | 82735 | 2391 | 2026-10-22 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2197 | 66 | 133/146 |
| http://149.130.173.58:9443 | CO | 437 | 57 | 57/57 |
| http://190.0.246.213:4040 | CO | 1357 | 40 | 103/111 |
| http://197.224.185.3:3128 | MU | 1736 | 38 | 107/114 |
| http://103.237.102.191:11111 | DE | 864 | 33 | 139/146 |
| http://203.252.142.217:80 | KR | 1014 | 28 | 28/28 |
| http://45.186.6.104:3128 | EC | 2711 | 27 | 117/124 |
| http://3.211.120.181:443 | US | 120 | 26 | 40/57 |
| http://103.133.26.72:8080 | ID | 2969 | 22 | 27/72 |
| http://103.133.26.73:3128 | ID | 1559 | 22 | 42/124 |
| http://103.133.26.119:8080 | ID | 1895 | 22 | 26/56 |
| http://176.111.37.5:39811 | HK | 797 | 17 | 127/146 |
| http://34.43.46.91:80 | US | 1206 | 16 | 140/146 |
| socks5://43.245.199.34:1080 | HK | 1341 | 15 | 15/15 |
| http://4.144.146.21:80 | SG | 1153 | 14 | 31/38 |
| http://190.0.246.210:4040 | CO | 4145 | 13 | 132/145 |
| http://43.155.62.157:443 | HK | 1293 | 13 | 41/49 |
| http://102.244.78.61:8081 | CM | 1176 | 12 | 25/32 |
| http://102.244.78.61:8090 | CM | 1232 | 12 | 28/38 |
| http://103.119.19.218:3128 | CZ | 639 | 12 | 47/59 |
| http://186.5.94.206:999 | EC | 776 | 11 | 99/108 |
| http://49.156.44.115:8080 | KH | 5272 | 11 | 42/112 |
| http://205.164.192.115:999 | MX | 2840 | 11 | 96/144 |
| socks5://103.100.158.115:10809 | JP | 1244 | 11 | 26/34 |
| http://184.75.221.82:3118 | CA | 244 | 10 | 97/111 |
| http://45.71.186.212:999 | EC | 1808 | 10 | 54/133 |
| http://189.51.168.165:999 | MX | 398 | 10 | 53/58 |
| http://130.110.103.245:3128 | SA | 1120 | 10 | 130/146 |
| http://102.244.78.61:8086 | CM | 1165 | 9 | 27/34 |
| http://181.78.195.137:999 | EC | 1967 | 9 | 48/146 |
| http://176.111.37.216:39811 | HK | 733 | 9 | 118/146 |
| http://46.209.30.11:8080 | IR | 1301 | 9 | 9/9 |
| http://102.244.78.61:8082 | CM | 1200 | 8 | 28/35 |
| http://34.88.38.81:9443 | FI | 788 | 8 | 77/111 |
| http://35.228.49.168:9443 | FI | 587 | 8 | 58/83 |
| http://103.130.61.61:8081 | ID | 3231 | 8 | 116/146 |
| http://102.244.78.61:8083 | CM | 1183 | 7 | 28/34 |
| http://102.244.78.61:8085 | CM | 1351 | 7 | 26/36 |
| http://102.244.78.61:8089 | CM | 1171 | 7 | 26/34 |
| http://177.234.217.88:999 | EC | 5884 | 7 | 58/138 |
| http://205.237.105.49:3129 | FR | 923 | 7 | 16/17 |
| socks5://51.15.20.32:1088 | NL | 5460 | 7 | 9/10 |
| http://185.191.239.248:3128 | CH | 1128 | 6 | 102/145 |
| http://120.232.115.170:17981 | CN | 1725 | 6 | 104/145 |
| http://103.133.26.50:8080 | ID | 1531 | 6 | 25/47 |
| http://102.244.78.61:8080 | CM | 1189 | 5 | 28/35 |
| http://170.254.228.90:999 | CO | 4073 | 5 | 31/129 |
| http://186.96.111.214:999 | CO | 1895 | 5 | 61/135 |
| http://181.78.194.249:999 | EC | 1812 | 5 | 50/129 |
| http://41.128.90.54:1976 | EG | 2513 | 5 | 24/67 |
| http://45.125.64.215:443 | HK | 2209 | 5 | 15/16 |
| http://116.254.118.180:80 | ID | 4842 | 5 | 12/19 |
| http://34.142.210.154:40001 | SG | 2620 | 5 | 5/5 |
| http://167.172.76.176:9090 | SG | 1144 | 5 | 74/107 |
| http://34.43.46.91:443 | US | 1177 | 5 | 136/146 |
| http://165.154.162.73:8888 | US | 3129 | 5 | 95/146 |
| http://38.172.160.16:999 | VE | 3781 | 5 | 55/97 |
| socks5://101.36.104.239:10808 | JP | 2675 | 5 | 123/146 |
| socks5://143.198.90.221:1088 | SG | 1503 | 5 | 12/14 |
| socks5://45.61.188.134:44499 | US | 846 | 5 | 52/113 |
| socks5://113.22.224.63:1083 | VN | 2000 | 5 | 13/14 |
| http://103.245.109.70:21458 | BD | 4615 | 4 | 16/51 |
| http://15.223.187.219:55865 | CA | 4193 | 4 | 18/60 |
| http://67.215.226.71:999 | DO | 1880 | 4 | 31/138 |
| http://45.71.186.210:999 | EC | 3084 | 4 | 43/120 |
| http://177.234.217.42:999 | EC | 3279 | 4 | 16/43 |
| http://81.19.210.10:80 | GB | 1729 | 4 | 6/7 |
| http://103.39.51.140:8181 | ID | 1617 | 4 | 19/81 |
| http://103.61.234.186:8180 | ID | 5256 | 4 | 61/143 |
| http://103.193.144.13:8080 | ID | 1750 | 4 | 23/125 |
| http://198.15.30.198:3125 | ID | 4659 | 4 | 8/12 |
| http://45.43.60.220:8080 | JP | 4572 | 4 | 76/145 |
| http://110.74.195.34:25 | KH | 7908 | 4 | 46/139 |
| http://187.245.202.15:999 | MX | 4894 | 4 | 9/27 |
| http://152.42.177.32:8888 | SG | 1142 | 4 | 67/106 |
| http://167.99.74.174:9090 | SG | 1146 | 4 | 71/106 |
| http://1.20.101.15:80 | TH | 4604 | 4 | 4/4 |
| http://103.22.181.107:3128 | TH | 1334 | 4 | 4/4 |
| http://195.142.250.34:8080 | TR | 4085 | 4 | 4/4 |
| http://144.202.78.114:1234 | US | 3061 | 4 | 4/4 |
| http://38.41.0.60:11201 | VE | 1600 | 4 | 25/72 |
| http://200.59.191.27:999 | VE | 4052 | 4 | 95/141 |
| http://14.224.183.185:8080 | VN | 6314 | 4 | 6/10 |
| http://14.225.2.98:808 | VN | 4670 | 4 | 28/90 |
| socks5://121.169.46.116:1090 | KR | 3504 | 4 | 99/146 |
| http://45.65.226.40:999 | AR | 5494 | 3 | 7/22 |
| http://45.65.226.174:999 | AR | 4044 | 3 | 4/7 |
| http://181.209.118.254:999 | AR | 5542 | 3 | 6/22 |
| http://181.209.125.237:999 | AR | 7204 | 3 | 3/3 |
| http://103.79.183.109:8080 | BD | 3011 | 3 | 3/3 |
| http://131.196.50.128:8080 | BR | 2188 | 3 | 13/69 |
| http://177.12.140.107:8080 | BR | 5528 | 3 | 13/54 |
| http://102.244.78.61:8084 | CM | 1189 | 3 | 26/34 |
| http://102.244.78.61:8088 | CM | 1161 | 3 | 27/34 |
| http://114.248.179.223:8888 | CN | 1737 | 3 | 44/114 |
| http://119.188.131.55:17981 | CN | 1643 | 3 | 73/146 |
| http://122.246.3.12:17981 | CN | 1909 | 3 | 63/140 |
| http://123.121.118.107:8888 | CN | 3411 | 3 | 4/12 |
| http://123.121.123.115:8888 | CN | 1722 | 3 | 42/70 |
| http://123.121.123.207:8888 | CN | 2730 | 3 | 17/31 |
