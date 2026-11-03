# Proxy status

Generated 2026-11-03T01:46:11Z by `harvest.py`.

- **2995** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5174** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34683** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 192/600 (32%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3198 |
| socks5 | 1956 |
| socks4 | 20 |

| country | entries |
|---|---|
| NL | 1711 |
| ?? | 1023 |
| ID | 757 |
| PH | 119 |
| CO | 111 |
| MX | 104 |
| US | 87 |
| VE | 81 |
| TH | 79 |
| BD | 66 |
| TR | 66 |
| BR | 59 |
| RU | 54 |
| IN | 51 |
| CN | 49 |
| DO | 49 |
| AR | 47 |
| EC | 45 |
| PE | 42 |
| PK | 30 |
| ZA | 30 |
| EG | 29 |
| JP | 29 |
| DE | 28 |
| KH | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 12 | 12 | 5 | 2026-11-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 59 | 2026-11-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-11-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 159 | 159 | 21 | 2026-11-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 220 | 220 | 46 | 2026-11-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 345 | 345 | 181 | 2026-11-03 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-11-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 921 | 921 | 267 | 2026-11-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1374 | 1374 | 457 | 2026-11-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1423 | 1423 | 725 | 2026-11-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1134 | 2026-11-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1584 | 2026-11-03 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1869 | 1869 | 274 | 2026-11-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2463 | 2463 | 659 | 2026-11-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2948 | 2948 | 1795 | 2026-11-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3346 | 3346 | 912 | 2026-11-03 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4938 | 4938 | 3693 | 2026-11-03 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11357 | 11356 | 2575 | 2026-11-03 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 630 | 79 | 79/79 |
| http://103.237.102.191:11111 | DE | 1118 | 55 | 161/168 |
| http://103.133.26.73:3128 | ID | 1349 | 44 | 64/146 |
| http://176.111.37.5:39811 | HK | 1125 | 39 | 149/168 |
| http://34.43.46.91:80 | US | 537 | 38 | 162/168 |
| http://4.144.146.21:80 | SG | 976 | 36 | 53/60 |
| http://176.111.37.216:39811 | HK | 1102 | 31 | 140/168 |
| http://34.43.46.91:443 | US | 535 | 17 | 157/168 |
| http://167.172.76.176:9090 | SG | 958 | 15 | 92/129 |
| socks5://101.36.104.239:10808 | JP | 1682 | 15 | 144/168 |
| http://130.110.103.245:3128 | SA | 1443 | 14 | 150/168 |
| socks5://45.61.188.134:44499 | US | 1070 | 14 | 70/135 |
| socks5://193.25.215.182:22222 | US | 791 | 14 | 141/168 |
| http://103.133.26.72:8080 | ID | 1330 | 11 | 48/94 |
| http://154.59.56.78:999 | VE | 4136 | 10 | 87/124 |
| http://45.189.57.114:3129 | ?? | 835 | 10 | 10/10 |
| http://15.229.149.81:1080 | BR | 3156 | 9 | 33/70 |
| http://102.244.78.61:8085 | CM | 1362 | 9 | 46/58 |
| http://102.244.78.61:8087 | CM | 1392 | 9 | 45/58 |
| http://102.244.78.61:8090 | CM | 1349 | 8 | 46/60 |
| http://38.172.160.16:999 | VE | 1661 | 8 | 71/119 |
| http://200.59.191.27:999 | VE | 4584 | 8 | 112/163 |
| http://130.127.204.197:8080 | ?? | 300 | 8 | 8/8 |
| http://45.65.224.74:999 | AR | 7012 | 7 | 26/33 |
| http://123.200.8.170:10000 | BD | 2266 | 7 | 74/166 |
| http://102.244.78.61:8082 | CM | 1407 | 7 | 46/57 |
| http://102.244.78.61:8089 | CM | 1314 | 7 | 44/56 |
| http://190.12.150.244:999 | EC | 1291 | 7 | 120/164 |
| http://185.238.238.49:58080 | PL | 1263 | 7 | 56/162 |
| http://154.59.56.72:999 | VE | 2038 | 7 | 94/127 |
| socks5://69.55.49.177:38182 | US | 1291 | 7 | 22/23 |
| http://187.102.219.32:999 | AR | 1769 | 6 | 57/167 |
| http://186.96.111.214:999 | CO | 2914 | 6 | 76/157 |
| http://45.186.6.104:3128 | EC | 821 | 6 | 138/146 |
| http://197.164.101.13:1981 | EG | 2368 | 6 | 56/157 |
| http://164.163.74.97:999 | HN | 1873 | 6 | 29/90 |
| http://13.208.246.143:46557 | JP | 6392 | 6 | 34/128 |
| http://195.226.213.251:8888 | UA | 3655 | 6 | 66/162 |
| http://165.154.162.73:8888 | US | 465 | 6 | 111/168 |
| socks5://45.61.129.165:9050 | US | 2081 | 6 | 127/168 |
| http://190.0.246.213:4040 | CO | 637 | 5 | 123/133 |
| http://198.244.254.77:3128 | GB | 3577 | 5 | 45/52 |
| http://43.155.62.157:443 | HK | 1104 | 5 | 61/71 |
| http://45.198.11.183:9191 | ID | 2427 | 5 | 14/49 |
| http://103.189.97.113:8087 | ID | 3874 | 5 | 35/160 |
| http://160.22.207.95:8082 | ID | 1711 | 5 | 39/146 |
| http://189.51.168.165:999 | MX | 503 | 5 | 74/80 |
| http://206.135.47.107:999 | MX | 6866 | 5 | 20/38 |
| http://45.175.39.64:8080 | VE | 4304 | 5 | 36/153 |
| http://154.59.56.74:999 | VE | 6150 | 5 | 88/131 |
| http://38.19.213.80:999 | ?? | 3007 | 5 | 6/7 |
| http://103.147.134.79:8082 | ?? | 3794 | 5 | 6/8 |
| http://161.22.33.169:999 | ?? | 6255 | 5 | 5/5 |
| http://190.123.83.137:999 | ?? | 7513 | 5 | 5/5 |
| socks5://101.36.104.46:10808 | JP | 4206 | 5 | 144/168 |
| http://119.188.131.55:17981 | CN | 1704 | 4 | 87/168 |
| http://8.243.167.51:999 | CO | 3243 | 4 | 14/55 |
| http://45.65.137.218:999 | CO | 4396 | 4 | 56/133 |
| http://177.234.217.92:999 | EC | 1744 | 4 | 12/17 |
| http://37.187.109.70:10111 | FR | 868 | 4 | 57/168 |
| http://85.117.56.85:8080 | GE | 7705 | 4 | 15/52 |
| http://38.183.146.122:8080 | ID | 3450 | 4 | 13/88 |
| http://103.133.26.119:8080 | ID | 1642 | 4 | 47/78 |
| http://103.155.196.83:8082 | ID | 5399 | 4 | 33/81 |
| http://103.158.210.80:8082 | ID | 6528 | 4 | 45/158 |
| http://160.19.146.221:2022 | ID | 5382 | 4 | 37/133 |
| http://160.22.45.114:8080 | ID | 4390 | 4 | 16/27 |
| http://160.22.134.39:1111 | ID | 3225 | 4 | 7/29 |
| http://160.191.56.1:8082 | ID | 6469 | 4 | 43/114 |
| http://163.61.55.243:8081 | ID | 5100 | 4 | 31/162 |
| http://163.227.146.38:8080 | ID | 3843 | 4 | 42/168 |
| http://202.47.185.153:8090 | ID | 5256 | 4 | 26/123 |
| http://52.195.147.51:3128 | JP | 3532 | 4 | 39/132 |
| http://140.238.32.108:3128 | JP | 967 | 4 | 93/167 |
| http://38.210.179.30:999 | MX | 4235 | 4 | 24/100 |
| http://82.152.138.127:999 | MX | 348 | 4 | 44/130 |
| http://38.172.130.175:999 | PE | 3314 | 4 | 21/54 |
| http://49.229.100.235:8080 | TH | 1373 | 4 | 76/116 |
| http://180.180.156.117:80 | TH | 5781 | 4 | 11/30 |
| http://18.191.250.90:42918 | US | 2037 | 4 | 20/128 |
| http://209.62.196.68:8080 | US | 4749 | 4 | 21/111 |
| http://23.94.68.53:3128 | ?? | 1246 | 4 | 4/4 |
| http://83.171.113.43:3128 | ?? | 1286 | 4 | 8/14 |
| http://103.153.83.47:8080 | ?? | 5133 | 4 | 5/6 |
| http://103.183.58.230:8085 | ?? | 3813 | 4 | 4/4 |
| http://124.6.156.226:8082 | ?? | 6068 | 4 | 5/6 |
| http://128.201.30.222:8666 | ?? | 2377 | 4 | 7/14 |
| http://131.221.40.131:4040 | ?? | 747 | 4 | 6/7 |
| http://137.220.199.209:18080 | ?? | 1239 | 4 | 4/4 |
| http://152.42.170.187:9090 | ?? | 1008 | 4 | 4/4 |
| http://160.191.130.131:8080 | ?? | 4545 | 4 | 6/8 |
| http://161.49.84.3:8081 | ?? | 6494 | 4 | 4/4 |
| http://171.100.254.137:8080 | ?? | 1387 | 4 | 4/4 |
| http://177.234.217.83:999 | ?? | 3065 | 4 | 11/15 |
| http://177.234.217.84:999 | ?? | 2984 | 4 | 11/15 |
| http://184.82.164.23:8080 | ?? | 4682 | 4 | 8/10 |
| http://187.86.161.2:8080 | ?? | 4414 | 4 | 4/4 |
| http://189.51.168.164:999 | ?? | 535 | 4 | 4/4 |
| http://203.150.113.238:8080 | ?? | 2305 | 4 | 4/4 |
| socks5://5.75.133.113:10813 | DE | 6446 | 4 | 24/95 |
