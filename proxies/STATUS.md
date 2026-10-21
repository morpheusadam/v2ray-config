# Proxy status

Generated 2026-10-21T18:07:47Z by `harvest.py`.

- **1324** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3517** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39657** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 84/600 (14%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2189 |
| socks5 | 1325 |
| socks4 | 3 |

| country | entries |
|---|---|
| NL | 1103 |
| ID | 654 |
| ?? | 220 |
| PH | 115 |
| CO | 107 |
| MX | 100 |
| RU | 91 |
| US | 81 |
| BR | 64 |
| CN | 63 |
| BD | 60 |
| VE | 60 |
| EC | 56 |
| IN | 48 |
| TR | 46 |
| DO | 44 |
| AR | 37 |
| SG | 37 |
| DE | 35 |
| TH | 30 |
| PK | 26 |
| KH | 23 |
| VN | 22 |
| CL | 21 |
| EG | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 3 | 2026-10-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 86 | 86 | 23 | 2026-10-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 120 | 120 | 61 | 2026-10-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 132 | 132 | 51 | 2026-10-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 135 | 135 | 41 | 2026-10-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 84 | 2026-10-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 243 | 243 | 77 | 2026-10-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 398 | 398 | 122 | 2026-10-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-10-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 679 | 679 | 474 | 2026-10-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1459 | 1455 | 170 | 2026-10-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1142 | 2026-10-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-10-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2391 | 2389 | 739 | 2026-10-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2613 | 2611 | 1902 | 2026-10-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2717 | 2715 | 844 | 2026-10-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 74330 | 74330 | 61588 | 2026-10-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 80413 | 80412 | 2153 | 2026-10-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1070 | 63 | 130/143 |
| http://149.130.173.58:9443 | CO | 579 | 54 | 54/54 |
| http://190.0.246.213:4040 | CO | 611 | 37 | 100/108 |
| http://197.224.185.3:3128 | MU | 1268 | 35 | 104/111 |
| http://103.237.102.191:11111 | DE | 1315 | 30 | 136/143 |
| http://203.252.142.217:80 | KR | 740 | 25 | 25/25 |
| http://45.186.6.104:3128 | EC | 712 | 24 | 114/121 |
| http://3.211.120.181:443 | US | 333 | 23 | 37/54 |
| http://103.133.26.72:8080 | ID | 1279 | 19 | 24/69 |
| http://103.133.26.73:3128 | ID | 1327 | 19 | 39/121 |
| http://103.133.26.119:8080 | ID | 1557 | 19 | 23/53 |
| socks5://47.87.97.94:1080 | TH | 1401 | 15 | 18/19 |
| http://198.244.254.77:3128 | GB | 2674 | 14 | 25/27 |
| http://176.111.37.5:39811 | HK | 2025 | 14 | 124/143 |
| http://34.43.46.91:80 | US | 1458 | 13 | 137/143 |
| socks5://43.245.199.34:1080 | HK | 1076 | 12 | 12/12 |
| http://4.144.146.21:80 | SG | 933 | 11 | 28/35 |
| http://190.0.246.210:4040 | CO | 884 | 10 | 129/142 |
| http://43.155.62.157:443 | HK | 1872 | 10 | 38/46 |
| http://102.244.78.61:8081 | CM | 1377 | 9 | 22/29 |
| http://102.244.78.61:8090 | CM | 1386 | 9 | 25/35 |
| http://103.119.19.218:3128 | CZ | 799 | 9 | 44/56 |
| http://186.5.94.206:999 | EC | 1462 | 8 | 96/105 |
| http://49.156.44.115:8080 | KH | 7259 | 8 | 39/109 |
| http://205.164.192.115:999 | MX | 1688 | 8 | 93/141 |
| socks5://103.100.158.115:10809 | JP | 950 | 8 | 23/31 |
| http://184.75.221.82:3118 | CA | 532 | 7 | 94/108 |
| http://45.71.186.212:999 | EC | 3975 | 7 | 51/130 |
| http://189.51.168.165:999 | MX | 499 | 7 | 50/55 |
| http://130.110.103.245:3128 | SA | 1541 | 7 | 127/143 |
| http://102.244.78.61:8086 | CM | 1353 | 6 | 24/31 |
| http://181.78.195.137:999 | EC | 4897 | 6 | 45/143 |
| http://176.111.37.216:39811 | HK | 1502 | 6 | 115/143 |
| http://46.209.30.11:8080 | IR | 6834 | 6 | 6/6 |
| http://222.127.206.145:8085 | PH | 2952 | 6 | 12/83 |
| socks5://14.36.232.55:1080 | KR | 2731 | 6 | 6/6 |
| http://102.244.78.61:8082 | CM | 1375 | 5 | 25/32 |
| http://101.206.186.99:8080 | CN | 6129 | 5 | 62/143 |
| http://223.85.21.195:8080 | CN | 4506 | 5 | 59/141 |
| http://181.78.79.11:999 | CO | 1093 | 5 | 22/138 |
| http://177.234.221.194:999 | EC | 5132 | 5 | 25/42 |
| http://34.88.38.81:9443 | FI | 1061 | 5 | 74/108 |
| http://35.228.49.168:9443 | FI | 880 | 5 | 55/80 |
| http://103.130.61.61:8081 | ID | 1801 | 5 | 113/143 |
| http://159.223.41.216:9090 | SG | 962 | 5 | 74/103 |
| http://45.65.224.125:999 | ?? | 4859 | 5 | 5/5 |
| http://45.65.226.169:999 | ?? | 4020 | 5 | 5/5 |
| http://45.198.11.193:8282 | ?? | 2298 | 5 | 5/5 |
| http://62.146.180.4:3000 | ?? | 476 | 5 | 5/5 |
| socks5://47.251.127.154:1080 | US | 7749 | 5 | 24/96 |
| http://138.117.13.65:999 | AR | 5249 | 4 | 30/139 |
| http://102.244.78.61:8083 | CM | 1350 | 4 | 25/31 |
| http://102.244.78.61:8085 | CM | 1428 | 4 | 23/33 |
| http://102.244.78.61:8087 | CM | 1375 | 4 | 23/33 |
| http://102.244.78.61:8089 | CM | 1382 | 4 | 23/31 |
| http://101.251.204.174:8080 | CN | 1745 | 4 | 68/129 |
| http://111.192.23.52:8888 | CN | 1273 | 4 | 6/7 |
| http://38.156.89.76:999 | DO | 1828 | 4 | 6/9 |
| http://177.234.217.43:999 | EC | 6888 | 4 | 38/116 |
| http://177.234.217.88:999 | EC | 3571 | 4 | 55/135 |
| http://190.12.150.244:999 | EC | 5205 | 4 | 100/139 |
| http://200.24.148.21:999 | EC | 4291 | 4 | 20/130 |
| http://45.245.208.180:8080 | EG | 2396 | 4 | 14/16 |
| http://205.237.105.49:3129 | FR | 795 | 4 | 13/14 |
| http://34.105.252.3:3128 | GB | 710 | 4 | 16/25 |
| http://103.131.18.82:8011 | ID | 5284 | 4 | 11/76 |
| http://103.156.15.122:8087 | ID | 3289 | 4 | 9/29 |
| http://103.168.254.198:8080 | ID | 2553 | 4 | 5/7 |
| http://102.68.131.31:8080 | LY | 4463 | 4 | 16/92 |
| http://200.94.38.45:2604 | MX | 1167 | 4 | 14/32 |
| http://134.185.85.16:3128 | SG | 976 | 4 | 13/18 |
| socks5://51.15.20.32:1088 | NL | 835 | 4 | 6/7 |
| socks5://178.252.74.29:1081 | RU | 2528 | 4 | 12/16 |
| socks5://64.176.166.106:1080 | ?? | 1148 | 4 | 4/4 |
| http://177.184.195.168:8080 | BR | 5949 | 3 | 25/141 |
| http://185.191.239.248:3128 | CH | 2723 | 3 | 99/142 |
| http://120.232.115.170:17981 | CN | 1750 | 3 | 101/142 |
| http://221.221.162.6:8888 | CN | 7750 | 3 | 20/41 |
| http://152.200.200.217:999 | CO | 2706 | 3 | 23/121 |
| http://179.1.182.20:999 | CO | 7020 | 3 | 10/71 |
| http://179.1.221.26:3128 | CO | 5895 | 3 | 25/83 |
| http://186.97.200.210:999 | CO | 6870 | 3 | 10/57 |
| http://190.99.192.158:999 | CO | 3416 | 3 | 13/92 |
| http://38.159.37.173:999 | DO | 1833 | 3 | 13/98 |
| http://103.18.77.101:8080 | ID | 1225 | 3 | 18/97 |
| http://103.133.26.50:8080 | ID | 1323 | 3 | 22/44 |
| http://123.176.126.95:8080 | ID | 5096 | 3 | 25/89 |
| http://160.19.18.243:8080 | ID | 7654 | 3 | 19/139 |
| http://160.191.56.1:8082 | ID | 5197 | 3 | 33/89 |
| http://49.145.58.197:8082 | PH | 3535 | 3 | 12/17 |
| http://163.223.105.86:5052 | PH | 6718 | 3 | 8/27 |
| http://128.199.116.219:9090 | SG | 2399 | 3 | 49/62 |
| http://49.229.100.235:8080 | TH | 1277 | 3 | 58/91 |
| http://103.10.231.189:8080 | TH | 1554 | 3 | 93/128 |
| http://212.175.50.80:8085 | TR | 4477 | 3 | 12/65 |
| http://38.183.212.8:999 | ?? | 6376 | 3 | 3/3 |
| socks5://101.36.104.46:10808 | JP | 1383 | 3 | 123/143 |
| socks5://45.74.31.41:11094 | NL | 7883 | 3 | 3/3 |
| socks5://45.61.129.165:9050 | US | 1142 | 3 | 108/143 |
| http://185.196.182.29:8080 | AL | 5790 | 2 | 6/15 |
