# Proxy status

Generated 2026-10-25T22:01:28Z by `harvest.py`.

- **1289** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4050** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39691** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 101/600 (17%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2021 |
| socks5 | 2021 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 1850 |
| ID | 618 |
| US | 112 |
| PH | 106 |
| CO | 101 |
| MX | 87 |
| CN | 65 |
| BD | 62 |
| RU | 62 |
| VE | 62 |
| BR | 55 |
| TH | 55 |
| VN | 55 |
| EC | 49 |
| IN | 47 |
| AR | 39 |
| TR | 38 |
| DE | 32 |
| EG | 31 |
| PE | 30 |
| SG | 30 |
| DO | 27 |
| PK | 25 |
| SY | 23 |
| ZA | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 1 | 2026-10-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 80 | 80 | 27 | 2026-10-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 125 | 125 | 60 | 2026-10-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 47 | 2026-10-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-10-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 245 | 245 | 96 | 2026-10-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 252 | 252 | 13 | 2026-10-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 338 | 338 | 190 | 2026-10-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 377 | 377 | 143 | 2026-10-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-10-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1129 | 2026-10-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1733 | 1729 | 271 | 2026-10-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1592 | 2026-10-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1994 | 1992 | 720 | 2026-10-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2620 | 2618 | 1727 | 2026-10-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4171 | 4169 | 1832 | 2026-10-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 78772 | 78772 | 63345 | 2026-10-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 85237 | 85236 | 2143 | 2026-10-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 924 | 72 | 139/152 |
| http://149.130.173.58:9443 | CO | 521 | 63 | 63/63 |
| http://190.0.246.213:4040 | CO | 590 | 46 | 109/117 |
| http://197.224.185.3:3128 | MU | 1896 | 44 | 113/120 |
| http://103.237.102.191:11111 | DE | 962 | 39 | 145/152 |
| http://203.252.142.217:80 | KR | 897 | 34 | 34/34 |
| http://45.186.6.104:3128 | EC | 2694 | 33 | 123/130 |
| http://103.133.26.72:8080 | ID | 2207 | 28 | 33/78 |
| http://103.133.26.73:3128 | ID | 1461 | 28 | 48/130 |
| http://103.133.26.119:8080 | ID | 1693 | 28 | 32/62 |
| http://176.111.37.5:39811 | HK | 970 | 23 | 133/152 |
| http://34.43.46.91:80 | US | 509 | 22 | 146/152 |
| socks5://43.245.199.34:1080 | HK | 1204 | 21 | 21/21 |
| http://4.144.146.21:80 | SG | 1046 | 20 | 37/44 |
| http://190.0.246.210:4040 | CO | 683 | 19 | 138/151 |
| http://43.155.62.157:443 | HK | 2311 | 19 | 47/55 |
| http://102.244.78.61:8081 | CM | 1330 | 18 | 31/38 |
| http://186.5.94.206:999 | EC | 2180 | 17 | 105/114 |
| http://184.75.221.82:3118 | CA | 254 | 16 | 103/117 |
| http://189.51.168.165:999 | MX | 450 | 16 | 59/64 |
| http://130.110.103.245:3128 | SA | 1286 | 16 | 136/152 |
| http://176.111.37.216:39811 | HK | 949 | 15 | 124/152 |
| http://103.130.61.61:8081 | ID | 1831 | 14 | 122/152 |
| http://185.191.239.248:3128 | CH | 966 | 12 | 108/151 |
| http://103.133.26.50:8080 | ID | 1400 | 12 | 31/53 |
| http://45.125.64.215:443 | HK | 2470 | 11 | 21/22 |
| socks5://101.36.104.239:10808 | JP | 1875 | 11 | 129/152 |
| http://45.65.138.48:999 | CO | 1983 | 9 | 64/152 |
| http://82.152.138.127:999 | MX | 315 | 9 | 33/114 |
| socks5://123.58.219.171:10808 | HK | 1728 | 9 | 121/152 |
| socks5://171.25.158.95:1080 | SE | 7971 | 9 | 58/67 |
| socks5://129.146.121.2:10808 | US | 396 | 9 | 9/9 |
| http://181.78.195.136:999 | EC | 4452 | 8 | 8/8 |
| http://103.130.61.60:8081 | ID | 3746 | 8 | 8/8 |
| http://162.214.159.94:3128 | US | 339 | 8 | 8/8 |
| http://123.121.132.234:8888 | CN | 1566 | 7 | 11/13 |
| http://45.177.178.23:999 | MX | 325 | 7 | 7/7 |
| http://146.190.80.158:9090 | SG | 3069 | 7 | 56/78 |
| socks5://67.207.92.87:1088 | US | 376 | 7 | 93/151 |
| socks5://69.55.49.177:38182 | US | 277 | 7 | 7/7 |
| http://89.58.42.118:3129 | DE | 1773 | 6 | 18/41 |
| http://5.129.254.5:8888 | RU | 3375 | 6 | 91/107 |
| http://5.129.254.49:8888 | RU | 3370 | 6 | 92/107 |
| http://5.129.254.51:8888 | RU | 3185 | 6 | 92/107 |
| http://5.129.254.60:8888 | RU | 4145 | 6 | 91/106 |
| http://5.129.254.70:8888 | RU | 3446 | 6 | 92/107 |
| http://5.129.254.129:8888 | RU | 1147 | 6 | 97/113 |
| http://5.129.254.154:8888 | RU | 3075 | 6 | 88/103 |
| http://5.129.254.215:8888 | RU | 2723 | 6 | 41/49 |
| http://5.129.254.243:8888 | RU | 1237 | 6 | 41/48 |
| http://147.45.164.178:8888 | RU | 4127 | 6 | 21/26 |
| http://64.118.155.2:22222 | US | 293 | 6 | 6/6 |
| socks5://101.36.104.46:10808 | JP | 1367 | 6 | 131/152 |
| socks5://5.255.103.55:1080 | NL | 2619 | 6 | 21/47 |
| http://15.229.149.81:3128 | BR | 5252 | 5 | 33/62 |
| http://119.188.131.55:17981 | CN | 1761 | 5 | 78/152 |
| http://89.167.124.218:8888 | DE | 1099 | 5 | 5/5 |
| http://45.65.224.74:999 | AR | 5135 | 4 | 12/17 |
| http://45.65.224.125:999 | AR | 1768 | 4 | 12/14 |
| http://45.71.189.51:8080 | BR | 1954 | 4 | 4/4 |
| http://102.244.78.61:8080 | CM | 1324 | 4 | 33/41 |
| http://102.244.78.61:8082 | CM | 1361 | 4 | 33/41 |
| http://102.244.78.61:8083 | CM | 1336 | 4 | 33/40 |
| http://102.244.78.61:8084 | CM | 1329 | 4 | 31/40 |
| http://102.244.78.61:8085 | CM | 1351 | 4 | 31/42 |
| http://102.244.78.61:8086 | CM | 1318 | 4 | 32/40 |
| http://102.244.78.61:8087 | CM | 1316 | 4 | 30/42 |
| http://102.244.78.61:8088 | CM | 1341 | 4 | 32/40 |
| http://102.244.78.61:8089 | CM | 1322 | 4 | 31/40 |
| http://102.244.78.61:8090 | CM | 1340 | 4 | 33/44 |
| http://123.121.118.107:8888 | CN | 7987 | 4 | 9/18 |
| http://64.204.90.17:999 | CO | 943 | 4 | 41/140 |
| http://103.119.19.218:3128 | CZ | 693 | 4 | 52/65 |
| http://213.131.85.28:1981 | EG | 1038 | 4 | 12/16 |
| http://51.85.44.162:31819 | IL | 1430 | 4 | 4/4 |
| http://152.67.191.232:6800 | IN | 1241 | 4 | 19/21 |
| http://206.135.47.107:999 | MX | 7667 | 4 | 9/22 |
| socks5://79.137.160.138:1080 | RU | 3558 | 4 | 4/4 |
| socks5://47.87.97.94:1080 | TH | 1456 | 4 | 24/28 |
| http://168.194.34.196:9001 | AR | 3662 | 3 | 53/150 |
| http://221.221.159.97:8888 | CN | 2646 | 3 | 52/105 |
| http://186.33.51.12:999 | CO | 6352 | 3 | 8/15 |
| http://177.234.217.42:999 | EC | 3725 | 3 | 20/49 |
| http://41.196.16.233:1981 | EG | 1223 | 3 | 5/6 |
| http://84.36.141.180:1976 | EG | 3598 | 3 | 45/138 |
| http://15.217.214.40:36960 | ES | 2801 | 3 | 3/3 |
| http://51.94.221.175:1857 | ES | 2272 | 3 | 17/93 |
| http://43.202.114.177:7428 | KR | 3345 | 3 | 26/66 |
| http://112.216.54.226:12121 | KR | 1276 | 3 | 54/146 |
| http://38.194.246.34:999 | MX | 1936 | 3 | 83/143 |
| http://43.224.188.142:8080 | PH | 2169 | 3 | 5/6 |
| http://49.145.53.55:8080 | PH | 6660 | 3 | 11/17 |
| http://43.134.39.221:10000 | SG | 2448 | 3 | 5/6 |
| http://104.248.151.93:9090 | SG | 1956 | 3 | 39/53 |
| http://3.134.245.77:4145 | US | 1592 | 3 | 12/54 |
| http://18.222.231.188:55985 | US | 2312 | 3 | 3/3 |
| http://34.220.80.147:33647 | US | 3042 | 3 | 23/68 |
| http://154.59.56.78:999 | VE | 4796 | 3 | 74/108 |
| http://186.167.113.103:999 | VE | 5538 | 3 | 25/148 |
| socks5://31.211.142.115:8192 | BG | 6644 | 3 | 32/150 |
