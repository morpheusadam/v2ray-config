# Proxy status

Generated 2026-10-24T16:45:15Z by `harvest.py`.

- **2641** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5352** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39767** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 175/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2744 |
| http | 2601 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 2516 |
| ID | 805 |
| PH | 153 |
| MX | 138 |
| CO | 136 |
| US | 114 |
| RU | 97 |
| ?? | 97 |
| VE | 77 |
| BD | 75 |
| BR | 70 |
| CN | 65 |
| TR | 61 |
| IN | 58 |
| EC | 55 |
| VN | 54 |
| TH | 51 |
| DO | 44 |
| AR | 41 |
| PE | 40 |
| SG | 40 |
| PK | 39 |
| EG | 34 |
| DE | 32 |
| SY | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 5 | 2026-10-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 87 | 87 | 38 | 2026-10-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 110 | 110 | 24 | 2026-10-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 135 | 135 | 69 | 2026-10-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 86 | 2026-10-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 218 | 218 | 90 | 2026-10-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 347 | 347 | 147 | 2026-10-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-10-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1081 | 1081 | 56 | 2026-10-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1132 | 1132 | 656 | 2026-10-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1148 | 2026-10-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1595 | 2026-10-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1882 | 1880 | 770 | 2026-10-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1884 | 1880 | 438 | 2026-10-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2164 | 2162 | 1494 | 2026-10-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2305 | 2303 | 834 | 2026-10-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 77556 | 77556 | 63544 | 2026-10-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 83295 | 83294 | 2146 | 2026-10-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 987 | 69 | 136/149 |
| http://149.130.173.58:9443 | CO | 427 | 60 | 60/60 |
| http://190.0.246.213:4040 | CO | 483 | 43 | 106/114 |
| http://197.224.185.3:3128 | MU | 1771 | 41 | 110/117 |
| http://103.237.102.191:11111 | DE | 764 | 36 | 142/149 |
| http://203.252.142.217:80 | KR | 999 | 31 | 31/31 |
| http://45.186.6.104:3128 | EC | 659 | 30 | 120/127 |
| http://103.133.26.72:8080 | ID | 2507 | 25 | 30/75 |
| http://103.133.26.73:3128 | ID | 1605 | 25 | 45/127 |
| http://103.133.26.119:8080 | ID | 1925 | 25 | 29/59 |
| http://176.111.37.5:39811 | HK | 1022 | 20 | 130/149 |
| http://34.43.46.91:80 | US | 2403 | 19 | 143/149 |
| socks5://43.245.199.34:1080 | HK | 2264 | 18 | 18/18 |
| http://4.144.146.21:80 | SG | 1173 | 17 | 34/41 |
| http://190.0.246.210:4040 | CO | 653 | 16 | 135/148 |
| http://43.155.62.157:443 | HK | 3808 | 16 | 44/52 |
| http://102.244.78.61:8081 | CM | 1233 | 15 | 28/35 |
| http://186.5.94.206:999 | EC | 1179 | 14 | 102/111 |
| http://49.156.44.115:8080 | KH | 4542 | 14 | 45/115 |
| http://205.164.192.115:999 | MX | 5758 | 14 | 99/147 |
| socks5://103.100.158.115:10809 | JP | 5426 | 14 | 29/37 |
| http://184.75.221.82:3118 | CA | 218 | 13 | 100/114 |
| http://189.51.168.165:999 | MX | 1382 | 13 | 56/61 |
| http://130.110.103.245:3128 | SA | 1105 | 13 | 133/149 |
| http://176.111.37.216:39811 | HK | 4055 | 12 | 121/149 |
| http://103.130.61.61:8081 | ID | 2998 | 11 | 119/149 |
| http://205.237.105.49:3129 | FR | 726 | 10 | 19/20 |
| http://185.191.239.248:3128 | CH | 1215 | 9 | 105/148 |
| http://103.133.26.50:8080 | ID | 1648 | 9 | 28/50 |
| http://45.125.64.215:443 | HK | 1193 | 8 | 18/19 |
| http://34.43.46.91:443 | US | 2716 | 8 | 139/149 |
| http://38.172.160.16:999 | VE | 681 | 8 | 58/100 |
| socks5://101.36.104.239:10808 | JP | 1556 | 8 | 126/149 |
| socks5://143.198.90.221:1088 | SG | 1428 | 8 | 15/17 |
| http://45.43.60.220:8080 | JP | 3889 | 7 | 79/148 |
| http://195.142.250.34:8080 | TR | 6182 | 7 | 7/7 |
| http://200.59.191.27:999 | VE | 1782 | 7 | 98/144 |
| socks5://121.169.46.116:1090 | KR | 2218 | 7 | 102/149 |
| http://45.65.138.48:999 | CO | 3117 | 6 | 61/149 |
| http://82.152.138.127:999 | MX | 371 | 6 | 30/111 |
| http://88.210.37.30:3128 | US | 700 | 6 | 6/6 |
| socks5://123.58.219.171:10808 | HK | 2272 | 6 | 118/149 |
| socks5://171.25.158.95:1080 | SE | 3394 | 6 | 55/64 |
| socks5://129.146.121.2:10808 | US | 427 | 6 | 6/6 |
| socks5://209.50.255.91:1080 | US | 830 | 6 | 34/66 |
| http://38.57.65.195:999 | DO | 4625 | 5 | 11/34 |
| http://45.71.186.213:999 | EC | 6876 | 5 | 51/133 |
| http://181.78.195.136:999 | EC | 5169 | 5 | 5/5 |
| http://198.244.254.77:3128 | GB | 2643 | 5 | 30/33 |
| http://103.63.26.59:1111 | ID | 7272 | 5 | 19/50 |
| http://103.130.61.60:8081 | ID | 7609 | 5 | 5/5 |
| http://168.144.121.183:3129 | IN | 1828 | 5 | 46/100 |
| http://38.172.130.175:999 | PE | 3927 | 5 | 14/35 |
| http://1.20.101.33:80 | TH | 5470 | 5 | 5/5 |
| http://162.214.159.94:3128 | US | 349 | 5 | 5/5 |
| socks5://213.199.47.140:1080 | FR | 2728 | 5 | 90/115 |
| socks5://217.71.230.103:1080 | RU | 1398 | 5 | 5/5 |
| http://45.65.226.172:999 | AR | 4153 | 4 | 5/6 |
| http://170.246.36.225:999 | AR | 7788 | 4 | 5/6 |
| http://186.10.150.185:8080 | CL | 4016 | 4 | 20/68 |
| http://123.121.107.143:8888 | CN | 1389 | 4 | 8/14 |
| http://123.121.122.28:8888 | CN | 1441 | 4 | 57/98 |
| http://123.121.132.234:8888 | CN | 1308 | 4 | 8/10 |
| http://221.221.154.122:8888 | CN | 2114 | 4 | 34/102 |
| http://38.199.30.82:999 | CO | 7734 | 4 | 32/145 |
| http://41.128.77.76:1981 | EG | 2002 | 4 | 44/103 |
| http://8.215.25.3:2080 | ID | 2324 | 4 | 40/149 |
| http://8.215.25.3:2081 | ID | 2184 | 4 | 36/147 |
| http://41.216.191.154:8080 | ID | 2676 | 4 | 4/4 |
| http://103.172.42.131:1111 | ID | 7550 | 4 | 12/51 |
| http://103.184.98.33:8082 | ID | 6576 | 4 | 13/56 |
| http://103.203.234.103:8080 | ID | 6020 | 4 | 29/148 |
| http://202.138.242.31:9090 | ID | 6749 | 4 | 19/132 |
| http://223.25.110.250:8088 | ID | 6992 | 4 | 31/143 |
| http://51.17.99.116:40013 | IL | 1315 | 4 | 14/37 |
| http://18.61.230.250:9898 | IN | 3000 | 4 | 22/99 |
| http://129.159.239.33:3128 | IN | 1308 | 4 | 5/6 |
| http://38.58.130.128:999 | MX | 7908 | 4 | 24/144 |
| http://38.210.179.30:999 | MX | 6271 | 4 | 18/81 |
| http://45.177.178.23:999 | MX | 379 | 4 | 4/4 |
| http://51.15.20.32:3129 | NL | 496 | 4 | 10/13 |
| http://119.93.151.254:8081 | PH | 4217 | 4 | 19/68 |
| http://146.190.80.158:9090 | SG | 1154 | 4 | 53/75 |
| http://109.224.242.26:8080 | TR | 7724 | 4 | 13/57 |
| http://201.4.64.239:8080 | TR | 5611 | 4 | 11/30 |
| http://161.22.32.31:8080 | VE | 4665 | 4 | 17/27 |
| socks4://103.71.23.31:1080 | FI | 1513 | 4 | 4/4 |
| socks5://45.74.31.46:4241 | NL | 7828 | 4 | 6/21 |
| socks5://45.74.31.47:8546 | NL | 5211 | 4 | 7/19 |
| socks5://103.178.121.234:1080 | PK | 3840 | 4 | 8/29 |
| socks5://67.207.92.87:1088 | US | 264 | 4 | 90/148 |
| socks5://69.55.49.177:38182 | US | 302 | 4 | 4/4 |
| socks5://166.1.90.114:1090 | US | 76 | 4 | 6/8 |
| http://79.106.44.66:2095 | AL | 5356 | 3 | 16/88 |
| http://59.153.30.20:8888 | BD | 2212 | 3 | 16/62 |
| http://103.141.174.38:11411 | BD | 4645 | 3 | 34/133 |
| http://179.48.80.9:8085 | BR | 7473 | 3 | 16/61 |
| http://186.211.194.21:8080 | BR | 4665 | 3 | 5/6 |
| http://186.235.255.220:8080 | BR | 3904 | 3 | 16/50 |
| http://45.161.112.227:999 | CL | 6257 | 3 | 38/142 |
