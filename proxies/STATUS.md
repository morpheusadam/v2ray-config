# Proxy status

Generated 2026-10-26T19:26:41Z by `harvest.py`.

- **1187** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3888** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39278** endpoints on record
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
| socks5 | 2239 |
| http | 1640 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 2041 |
| ID | 478 |
| US | 99 |
| PH | 79 |
| CO | 77 |
| MX | 71 |
| CN | 66 |
| RU | 65 |
| BD | 54 |
| VE | 52 |
| BR | 48 |
| TH | 46 |
| EC | 43 |
| VN | 41 |
| ?? | 39 |
| AR | 34 |
| IN | 31 |
| SG | 29 |
| TR | 29 |
| DE | 26 |
| DO | 26 |
| JP | 26 |
| EG | 25 |
| PK | 21 |
| PE | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 3 | 2026-10-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 110 | 110 | 48 | 2026-10-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 123 | 123 | 72 | 2026-10-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 81 | 2026-10-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 227 | 227 | 79 | 2026-10-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 227 | 227 | 77 | 2026-10-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 352 | 352 | 135 | 2026-10-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-10-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 652 | 652 | 385 | 2026-10-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 673 | 673 | 40 | 2026-10-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1319 | 1315 | 99 | 2026-10-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1134 | 2026-10-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1590 | 2026-10-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2105 | 2103 | 711 | 2026-10-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2701 | 2699 | 1869 | 2026-10-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2712 | 2710 | 909 | 2026-10-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 79213 | 79213 | 64580 | 2026-10-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 85648 | 85647 | 2161 | 2026-10-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1303 | 73 | 140/153 |
| http://149.130.173.58:9443 | CO | 580 | 64 | 64/64 |
| http://190.0.246.213:4040 | CO | 681 | 47 | 110/118 |
| http://103.237.102.191:11111 | DE | 944 | 40 | 146/153 |
| http://45.186.6.104:3128 | EC | 726 | 34 | 124/131 |
| http://103.133.26.72:8080 | ID | 1276 | 29 | 34/79 |
| http://103.133.26.73:3128 | ID | 1384 | 29 | 49/131 |
| http://103.133.26.119:8080 | ID | 1630 | 29 | 33/63 |
| http://176.111.37.5:39811 | HK | 1093 | 24 | 134/153 |
| http://34.43.46.91:80 | US | 551 | 23 | 147/153 |
| socks5://43.245.199.34:1080 | HK | 1094 | 22 | 22/22 |
| http://4.144.146.21:80 | SG | 931 | 21 | 38/45 |
| http://190.0.246.210:4040 | CO | 1143 | 20 | 139/152 |
| http://43.155.62.157:443 | HK | 2650 | 20 | 48/56 |
| http://102.244.78.61:8081 | CM | 1417 | 19 | 32/39 |
| http://186.5.94.206:999 | EC | 2042 | 18 | 106/115 |
| http://184.75.221.82:3118 | CA | 515 | 17 | 104/118 |
| http://189.51.168.165:999 | MX | 476 | 17 | 60/65 |
| http://176.111.37.216:39811 | HK | 958 | 16 | 125/153 |
| http://103.130.61.61:8081 | ID | 6255 | 15 | 123/153 |
| http://185.191.239.248:3128 | CH | 7960 | 13 | 109/152 |
| http://103.133.26.50:8080 | ID | 1291 | 13 | 32/54 |
| http://45.125.64.215:443 | HK | 1890 | 12 | 22/23 |
| http://45.65.138.48:999 | CO | 7689 | 10 | 65/153 |
| socks5://123.58.219.171:10808 | HK | 1310 | 10 | 122/153 |
| socks5://129.146.121.2:10808 | US | 113 | 10 | 10/10 |
| http://181.78.195.136:999 | EC | 4128 | 9 | 9/9 |
| http://103.130.61.60:8081 | ID | 3251 | 9 | 9/9 |
| http://162.214.159.94:3128 | US | 239 | 9 | 9/9 |
| http://123.121.132.234:8888 | CN | 1883 | 8 | 12/14 |
| http://45.177.178.23:999 | MX | 4465 | 8 | 8/8 |
| http://146.190.80.158:9090 | SG | 925 | 8 | 57/79 |
| socks5://67.207.92.87:1088 | US | 578 | 8 | 94/152 |
| socks5://69.55.49.177:38182 | US | 1139 | 8 | 8/8 |
| http://5.129.254.5:8888 | RU | 1426 | 7 | 92/108 |
| http://5.129.254.49:8888 | RU | 1976 | 7 | 93/108 |
| http://5.129.254.51:8888 | RU | 2068 | 7 | 93/108 |
| http://5.129.254.60:8888 | RU | 3267 | 7 | 92/107 |
| http://5.129.254.70:8888 | RU | 1923 | 7 | 93/108 |
| http://5.129.254.129:8888 | RU | 1522 | 7 | 98/114 |
| http://5.129.254.154:8888 | RU | 1394 | 7 | 89/104 |
| http://5.129.254.215:8888 | RU | 1457 | 7 | 42/50 |
| http://5.129.254.243:8888 | RU | 3478 | 7 | 42/49 |
| http://147.45.164.178:8888 | RU | 1987 | 7 | 22/27 |
| http://64.118.155.2:22222 | US | 173 | 7 | 7/7 |
| socks5://101.36.104.46:10808 | JP | 1582 | 7 | 132/153 |
| http://15.229.149.81:3128 | BR | 5367 | 6 | 34/63 |
| http://119.188.131.55:17981 | CN | 1439 | 6 | 79/153 |
| http://89.167.124.218:8888 | DE | 1047 | 6 | 6/6 |
| http://45.65.224.74:999 | AR | 6566 | 5 | 13/18 |
| http://102.244.78.61:8080 | CM | 1370 | 5 | 34/42 |
| http://102.244.78.61:8082 | CM | 1449 | 5 | 34/42 |
| http://102.244.78.61:8083 | CM | 1369 | 5 | 34/41 |
| http://102.244.78.61:8084 | CM | 1352 | 5 | 32/41 |
| http://102.244.78.61:8085 | CM | 1378 | 5 | 32/43 |
| http://102.244.78.61:8086 | CM | 1322 | 5 | 33/41 |
| http://102.244.78.61:8087 | CM | 1375 | 5 | 31/43 |
| http://102.244.78.61:8088 | CM | 1346 | 5 | 33/41 |
| http://102.244.78.61:8089 | CM | 1367 | 5 | 32/41 |
| http://102.244.78.61:8090 | CM | 1363 | 5 | 34/45 |
| http://123.121.118.107:8888 | CN | 7298 | 5 | 10/19 |
| http://103.119.19.218:3128 | CZ | 830 | 5 | 53/66 |
| http://51.85.44.162:31819 | IL | 2313 | 5 | 5/5 |
| socks5://79.137.160.138:1080 | RU | 6150 | 5 | 5/5 |
| socks5://47.87.97.94:1080 | TH | 1339 | 5 | 25/29 |
| http://15.217.214.40:36960 | ES | 4301 | 4 | 4/4 |
| http://43.202.114.177:7428 | KR | 3986 | 4 | 27/67 |
| http://112.216.54.226:12121 | KR | 1703 | 4 | 55/147 |
| http://38.194.246.34:999 | MX | 3814 | 4 | 84/144 |
| http://104.248.151.93:9090 | SG | 960 | 4 | 40/54 |
| http://154.59.56.78:999 | VE | 1874 | 4 | 75/109 |
| socks5://45.74.31.46:4692 | NL | 5774 | 4 | 5/24 |
| http://187.102.219.42:999 | AR | 1831 | 3 | 82/148 |
| http://15.229.149.81:1080 | BR | 4372 | 3 | 22/55 |
| http://18.230.23.72:26881 | BR | 3382 | 3 | 16/69 |
| http://1.15.53.214:8888 | CN | 1576 | 3 | 41/147 |
| http://103.156.57.135:9988 | ID | 7794 | 3 | 22/93 |
| http://51.85.44.162:8089 | IL | 2284 | 3 | 3/3 |
| http://140.227.61.201:3128 | JP | 3666 | 3 | 44/145 |
| http://157.120.37.23:3128 | JP | 1644 | 3 | 7/9 |
| http://185.238.238.137:58080 | PL | 6233 | 3 | 50/149 |
| http://185.238.238.165:58080 | PL | 6199 | 3 | 18/43 |
| http://159.223.41.216:9090 | SG | 953 | 3 | 80/113 |
| http://49.229.100.235:8080 | TH | 1696 | 3 | 65/101 |
| http://61.91.162.126:8080 | TH | 1309 | 3 | 72/96 |
| http://103.10.231.189:8080 | TH | 1702 | 3 | 99/138 |
| http://77.95.2.9:8080 | TJ | 3338 | 3 | 4/5 |
| socks5://107.191.47.162:1081 | FR | 846 | 3 | 3/3 |
| socks5://47.238.126.208:1080 | HK | 1095 | 3 | 29/58 |
| socks5://103.38.82.221:5555 | HK | 1130 | 3 | 8/29 |
| socks5://45.74.31.40:4399 | NL | 4664 | 3 | 3/3 |
| socks5://45.74.31.40:4566 | NL | 3106 | 3 | 3/3 |
| socks5://45.74.31.40:4863 | NL | 3407 | 3 | 4/8 |
| socks5://45.74.31.41:5560 | NL | 4579 | 3 | 12/53 |
| socks5://45.74.31.42:5793 | NL | 6286 | 3 | 3/3 |
| socks5://51.15.20.32:1088 | NL | 2679 | 3 | 14/17 |
| socks5://93.153.222.83:1080 | RU | 2362 | 3 | 8/37 |
| socks5://47.251.127.154:1080 | US | 7695 | 3 | 31/106 |
| socks5://166.1.90.114:1090 | US | 467 | 3 | 9/12 |
| http://138.121.113.179:999 | AR | 4831 | 2 | 25/151 |
