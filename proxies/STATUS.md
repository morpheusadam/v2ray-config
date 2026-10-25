# Proxy status

Generated 2026-10-25T17:18:54Z by `harvest.py`.

- **2773** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5317** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39768** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 196/600 (33%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3080 |
| http | 2228 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 2873 |
| ID | 631 |
| PH | 119 |
| MX | 114 |
| US | 111 |
| CO | 97 |
| VN | 78 |
| RU | 77 |
| VE | 77 |
| TH | 76 |
| CN | 71 |
| BD | 69 |
| BR | 62 |
| IN | 54 |
| TR | 54 |
| EC | 52 |
| DO | 44 |
| PE | 39 |
| SG | 39 |
| DE | 37 |
| AR | 35 |
| EG | 33 |
| PK | 33 |
| SY | 28 |
| JP | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-10-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 85 | 85 | 18 | 2026-10-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 109 | 109 | 65 | 2026-10-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 125 | 125 | 50 | 2026-10-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 87 | 2026-10-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 210 | 210 | 16 | 2026-10-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 268 | 268 | 93 | 2026-10-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 316 | 316 | 130 | 2026-10-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 456 | 2026-10-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 679 | 679 | 411 | 2026-10-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1284 | 1280 | 98 | 2026-10-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1132 | 2026-10-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1591 | 2026-10-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2274 | 2272 | 1684 | 2026-10-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2349 | 2347 | 734 | 2026-10-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3399 | 3397 | 1208 | 2026-10-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 78594 | 78594 | 63847 | 2026-10-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 85111 | 85110 | 2380 | 2026-10-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1165 | 71 | 138/151 |
| http://149.130.173.58:9443 | CO | 475 | 62 | 62/62 |
| http://190.0.246.213:4040 | CO | 640 | 45 | 108/116 |
| http://197.224.185.3:3128 | MU | 2112 | 43 | 112/119 |
| http://103.237.102.191:11111 | DE | 942 | 38 | 144/151 |
| http://203.252.142.217:80 | KR | 862 | 33 | 33/33 |
| http://45.186.6.104:3128 | EC | 738 | 32 | 122/129 |
| http://103.133.26.72:8080 | ID | 1470 | 27 | 32/77 |
| http://103.133.26.73:3128 | ID | 1436 | 27 | 47/129 |
| http://103.133.26.119:8080 | ID | 1897 | 27 | 31/61 |
| http://176.111.37.5:39811 | HK | 873 | 22 | 132/151 |
| http://34.43.46.91:80 | US | 531 | 21 | 145/151 |
| socks5://43.245.199.34:1080 | HK | 1219 | 20 | 20/20 |
| http://4.144.146.21:80 | SG | 1048 | 19 | 36/43 |
| http://190.0.246.210:4040 | CO | 1356 | 18 | 137/150 |
| http://43.155.62.157:443 | HK | 3379 | 18 | 46/54 |
| http://102.244.78.61:8081 | CM | 1508 | 17 | 30/37 |
| http://186.5.94.206:999 | EC | 1001 | 16 | 104/113 |
| http://205.164.192.115:999 | MX | 5820 | 16 | 101/149 |
| socks5://103.100.158.115:10809 | JP | 2181 | 16 | 31/39 |
| http://184.75.221.82:3118 | CA | 188 | 15 | 102/116 |
| http://189.51.168.165:999 | MX | 463 | 15 | 58/63 |
| http://130.110.103.245:3128 | SA | 1310 | 15 | 135/151 |
| http://176.111.37.216:39811 | HK | 865 | 14 | 123/151 |
| http://103.130.61.61:8081 | ID | 4929 | 13 | 121/151 |
| http://185.191.239.248:3128 | CH | 3068 | 11 | 107/150 |
| http://103.133.26.50:8080 | ID | 1377 | 11 | 30/52 |
| http://45.125.64.215:443 | HK | 3904 | 10 | 20/21 |
| socks5://101.36.104.239:10808 | JP | 2719 | 10 | 128/151 |
| socks5://143.198.90.221:1088 | SG | 1355 | 10 | 17/19 |
| http://45.65.138.48:999 | CO | 3576 | 8 | 63/151 |
| http://82.152.138.127:999 | MX | 6180 | 8 | 32/113 |
| socks5://123.58.219.171:10808 | HK | 2703 | 8 | 120/151 |
| socks5://171.25.158.95:1080 | SE | 1454 | 8 | 57/66 |
| socks5://129.146.121.2:10808 | US | 540 | 8 | 8/8 |
| socks5://209.50.255.91:1080 | US | 1469 | 8 | 36/68 |
| http://181.78.195.136:999 | EC | 5990 | 7 | 7/7 |
| http://198.244.254.77:3128 | GB | 5560 | 7 | 32/35 |
| http://103.130.61.60:8081 | ID | 4910 | 7 | 7/7 |
| http://162.214.159.94:3128 | US | 1449 | 7 | 7/7 |
| socks5://213.199.47.140:1080 | FR | 1317 | 7 | 92/117 |
| http://123.121.132.234:8888 | CN | 1355 | 6 | 10/12 |
| http://8.215.25.3:2081 | ID | 1565 | 6 | 38/149 |
| http://51.17.99.116:40013 | IL | 6543 | 6 | 16/39 |
| http://45.177.178.23:999 | MX | 3453 | 6 | 6/6 |
| http://146.190.80.158:9090 | SG | 1031 | 6 | 55/77 |
| socks5://8.215.25.3:2080 | ID | 2395 | 6 | 42/151 |
| socks5://67.207.92.87:1088 | US | 685 | 6 | 92/150 |
| socks5://69.55.49.177:38182 | US | 266 | 6 | 6/6 |
| http://89.58.42.118:3129 | DE | 749 | 5 | 17/40 |
| http://102.164.252.150:8080 | GQ | 2032 | 5 | 42/110 |
| http://5.129.254.5:8888 | RU | 1288 | 5 | 90/106 |
| http://5.129.254.49:8888 | RU | 1256 | 5 | 91/106 |
| http://5.129.254.51:8888 | RU | 1354 | 5 | 91/106 |
| http://5.129.254.60:8888 | RU | 1306 | 5 | 90/105 |
| http://5.129.254.70:8888 | RU | 1272 | 5 | 91/106 |
| http://5.129.254.129:8888 | RU | 1356 | 5 | 96/112 |
| http://5.129.254.154:8888 | RU | 2322 | 5 | 87/102 |
| http://5.129.254.215:8888 | RU | 1248 | 5 | 40/48 |
| http://5.129.254.243:8888 | RU | 1297 | 5 | 40/47 |
| http://147.45.164.178:8888 | RU | 1272 | 5 | 20/25 |
| http://64.118.155.2:22222 | US | 2306 | 5 | 5/5 |
| socks5://101.36.104.46:10808 | JP | 3005 | 5 | 130/151 |
| socks5://5.255.103.55:1080 | NL | 1306 | 5 | 20/46 |
| socks5://45.61.129.165:9050 | US | 1387 | 5 | 114/151 |
| socks5://193.25.215.182:22222 | US | 1065 | 5 | 127/151 |
| http://15.229.149.81:3128 | BR | 3413 | 4 | 32/61 |
| http://16.18.22.211:9090 | CH | 1080 | 4 | 32/111 |
| http://119.188.131.55:17981 | CN | 1852 | 4 | 77/151 |
| http://89.167.124.218:8888 | DE | 929 | 4 | 4/4 |
| http://181.78.194.249:999 | EC | 3877 | 4 | 54/134 |
| http://41.33.203.235:1975 | EG | 1688 | 4 | 4/4 |
| http://103.168.210.122:80 | IN | 2361 | 4 | 4/4 |
| http://201.163.14.195:999 | MX | 435 | 4 | 5/6 |
| http://185.146.138.162:8080 | SY | 2699 | 4 | 4/4 |
| http://72.241.55.239:8080 | US | 5637 | 4 | 4/4 |
| socks5://45.74.31.41:5259 | NL | 6395 | 4 | 6/19 |
| socks5://45.74.31.41:5313 | NL | 3232 | 4 | 5/24 |
| socks5://45.74.31.42:4674 | NL | 1983 | 4 | 5/7 |
| socks5://45.61.188.134:44499 | US | 459 | 4 | 56/118 |
| socks5://143.198.239.45:10012 | US | 1969 | 4 | 15/38 |
| http://45.65.224.74:999 | AR | 2531 | 3 | 11/16 |
| http://45.65.224.125:999 | AR | 2575 | 3 | 11/13 |
| http://13.239.253.213:3128 | AU | 5383 | 3 | 32/116 |
| http://45.71.189.51:8080 | BR | 2002 | 3 | 3/3 |
| http://191.195.51.243:8080 | BR | 1475 | 3 | 3/3 |
| http://102.244.78.61:8080 | CM | 1463 | 3 | 32/40 |
| http://102.244.78.61:8082 | CM | 1518 | 3 | 32/40 |
| http://102.244.78.61:8083 | CM | 1473 | 3 | 32/39 |
| http://102.244.78.61:8084 | CM | 1485 | 3 | 30/39 |
| http://102.244.78.61:8085 | CM | 1557 | 3 | 30/41 |
| http://102.244.78.61:8086 | CM | 1463 | 3 | 31/39 |
| http://102.244.78.61:8087 | CM | 1515 | 3 | 29/41 |
| http://102.244.78.61:8088 | CM | 1528 | 3 | 31/39 |
| http://102.244.78.61:8089 | CM | 1541 | 3 | 30/39 |
| http://102.244.78.61:8090 | CM | 1384 | 3 | 32/43 |
| http://101.251.204.174:8080 | CN | 1718 | 3 | 74/137 |
| http://114.246.197.252:8888 | CN | 7360 | 3 | 21/70 |
| http://123.121.118.107:8888 | CN | 1357 | 3 | 8/17 |
| http://123.121.140.72:8888 | CN | 1666 | 3 | 3/3 |
