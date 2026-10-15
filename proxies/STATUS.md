# Proxy status

Generated 2026-10-15T17:48:22Z by `harvest.py`.

- **1692** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3494** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **38259** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 151/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1934 |
| socks5 | 1556 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 1346 |
| ID | 549 |
| PH | 104 |
| MX | 94 |
| US | 92 |
| ?? | 88 |
| CO | 86 |
| RU | 80 |
| CN | 70 |
| BD | 60 |
| BR | 55 |
| VE | 54 |
| IN | 53 |
| VN | 50 |
| EC | 47 |
| TR | 47 |
| DO | 40 |
| SG | 35 |
| EG | 31 |
| JP | 29 |
| TH | 26 |
| AR | 25 |
| KH | 23 |
| DE | 22 |
| CA | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 3 | 2026-10-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 62 | 62 | 34 | 2026-10-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 84 | 84 | 33 | 2026-10-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 65 | 2026-10-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 171 | 171 | 47 | 2026-10-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 269 | 269 | 81 | 2026-10-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 305 | 305 | 125 | 2026-10-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 581 | 581 | 427 | 2026-10-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 898 | 898 | 331 | 2026-10-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-10-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-10-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1847 | 1843 | 141 | 2026-10-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2367 | 2365 | 684 | 2026-10-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2418 | 2416 | 618 | 2026-10-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2438 | 2436 | 1767 | 2026-10-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 60694 | 60694 | 45804 | 2026-10-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 66622 | 66621 | 2099 | 2026-10-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1173 | 51 | 118/131 |
| http://149.130.173.58:9443 | CO | 596 | 42 | 42/42 |
| http://190.0.246.213:4040 | CO | 1442 | 25 | 88/96 |
| http://197.224.185.3:3128 | MU | 6481 | 23 | 92/99 |
| http://103.237.102.191:11111 | DE | 1125 | 18 | 124/131 |
| http://186.5.94.206:999 | EC | 2466 | 16 | 86/93 |
| http://203.252.142.217:80 | KR | 841 | 13 | 13/13 |
| http://146.190.80.158:9090 | SG | 890 | 13 | 41/57 |
| http://45.186.6.104:3128 | EC | 2880 | 12 | 102/109 |
| socks5://101.36.104.46:10808 | JP | 2810 | 12 | 115/131 |
| http://3.211.120.181:443 | US | 453 | 11 | 25/42 |
| http://165.154.162.73:8888 | US | 801 | 11 | 84/131 |
| http://102.244.78.61:8083 | CM | 1432 | 10 | 16/19 |
| http://103.130.61.61:8081 | ID | 2720 | 10 | 102/131 |
| http://144.124.251.24:10261 | NL | 1041 | 10 | 52/63 |
| http://101.206.186.99:8080 | CN | 3603 | 9 | 57/131 |
| http://144.124.251.24:10811 | NL | 792 | 9 | 51/63 |
| http://34.196.85.244:3128 | US | 1263 | 9 | 9/9 |
| http://102.244.78.61:8088 | CM | 1465 | 8 | 15/19 |
| http://144.124.251.24:10187 | NL | 758 | 8 | 51/77 |
| http://144.124.251.24:11265 | NL | 774 | 8 | 56/79 |
| http://5.129.254.5:8888 | RU | 1736 | 8 | 75/86 |
| http://5.129.254.49:8888 | RU | 1380 | 8 | 76/86 |
| http://5.129.254.51:8888 | RU | 1712 | 8 | 76/86 |
| http://5.129.254.60:8888 | RU | 1644 | 8 | 75/85 |
| http://5.129.254.70:8888 | RU | 1392 | 8 | 76/86 |
| http://5.129.254.129:8888 | RU | 1703 | 8 | 81/92 |
| http://5.129.254.154:8888 | RU | 1704 | 8 | 72/82 |
| http://5.129.254.215:8888 | RU | 1510 | 8 | 25/28 |
| http://5.129.254.243:8888 | RU | 1525 | 8 | 25/27 |
| http://34.88.38.81:9443 | FI | 1132 | 7 | 66/96 |
| http://35.228.49.168:9443 | FI | 886 | 7 | 47/68 |
| http://103.133.26.50:8080 | ID | 1226 | 7 | 11/32 |
| http://103.133.26.72:8080 | ID | 2375 | 7 | 12/57 |
| http://103.133.26.73:3128 | ID | 1275 | 7 | 27/109 |
| http://103.133.26.119:8080 | ID | 1577 | 7 | 11/41 |
| http://144.124.251.24:10176 | NL | 808 | 7 | 55/79 |
| http://144.124.251.24:10566 | NL | 817 | 7 | 51/64 |
| socks5://67.207.92.87:1088 | US | 754 | 7 | 75/130 |
| socks5://193.25.215.182:22222 | US | 559 | 7 | 110/131 |
| http://184.75.221.82:3118 | CA | 2555 | 6 | 84/96 |
| http://177.234.217.88:999 | EC | 3810 | 6 | 48/123 |
| http://49.156.44.115:8080 | KH | 4787 | 6 | 29/97 |
| http://144.124.251.24:10658 | NL | 775 | 6 | 48/63 |
| http://144.124.251.24:11450 | NL | 917 | 6 | 47/63 |
| http://144.124.251.24:11480 | NL | 769 | 6 | 49/63 |
| http://18.228.228.159:3822 | BR | 2780 | 5 | 14/41 |
| http://120.232.115.170:17981 | CN | 1599 | 5 | 93/130 |
| http://121.46.226.221:10808 | CN | 5529 | 5 | 7/8 |
| http://223.85.21.195:8080 | CN | 5611 | 5 | 50/129 |
| http://38.75.82.222:999 | DO | 2112 | 5 | 25/75 |
| http://41.33.245.138:1976 | EG | 6161 | 5 | 14/56 |
| http://41.128.90.51:1976 | EG | 1160 | 5 | 6/7 |
| http://213.131.85.29:1976 | EG | 1361 | 5 | 6/7 |
| http://78.14.19.3:3128 | MX | 4780 | 5 | 23/91 |
| http://43.216.197.62:26130 | MY | 5862 | 5 | 28/99 |
| http://144.124.251.24:10088 | NL | 767 | 5 | 48/63 |
| http://144.124.251.24:10226 | NL | 765 | 5 | 48/62 |
| http://144.124.251.24:10631 | NL | 769 | 5 | 50/63 |
| http://144.124.251.24:10689 | NL | 803 | 5 | 53/67 |
| http://203.177.217.222:8082 | PH | 1269 | 5 | 46/76 |
| http://147.45.164.178:8888 | RU | 2372 | 5 | 5/5 |
| http://13.215.184.250:3128 | SG | 3037 | 5 | 9/17 |
| http://152.42.177.32:8888 | SG | 890 | 5 | 55/91 |
| http://167.99.74.174:9090 | SG | 893 | 5 | 63/91 |
| http://20.33.10.132:80 | ZA | 7475 | 5 | 5/5 |
| socks5://148.251.68.232:8888 | DE | 3864 | 5 | 7/10 |
| socks5://45.74.31.46:5440 | NL | 5030 | 5 | 5/5 |
| socks5://8.219.122.8:9999 | SG | 1063 | 5 | 11/21 |
| socks5://45.61.129.165:9050 | US | 2043 | 5 | 98/131 |
| http://15.229.149.81:1080 | BR | 2979 | 4 | 13/33 |
| http://123.121.142.252:8888 | CN | 1173 | 4 | 25/53 |
| http://38.50.165.123:999 | DO | 7439 | 4 | 29/116 |
| http://190.110.36.184:999 | DO | 3150 | 4 | 8/31 |
| http://41.33.245.138:1981 | EG | 5877 | 4 | 29/61 |
| http://103.147.135.35:8082 | ID | 1322 | 4 | 25/67 |
| http://160.22.65.129:4004 | ID | 4685 | 4 | 11/26 |
| http://195.226.213.254:8888 | UA | 6190 | 4 | 44/129 |
| http://185.226.194.226:999 | VE | 3839 | 4 | 7/27 |
| http://14.225.2.98:808 | VN | 4460 | 4 | 22/75 |
| socks5://121.169.46.116:1090 | KR | 6872 | 4 | 89/131 |
| socks5://45.74.31.41:5534 | NL | 7064 | 4 | 5/16 |
| socks5://45.74.31.41:6522 | NL | 4023 | 4 | 4/4 |
| socks5://45.74.31.41:8548 | NL | 2646 | 4 | 4/4 |
| socks5://45.74.31.46:15792 | NL | 4878 | 4 | 6/13 |
| socks5://178.252.74.29:1081 | RU | 1455 | 4 | 4/4 |
| socks5://209.50.255.91:1080 | US | 6456 | 4 | 24/48 |
| socks5://116.104.251.199:1119 | VN | 1670 | 4 | 4/4 |
| http://143.208.152.62:3180 | BR | 3027 | 3 | 27/115 |
| http://56.112.92.32:16486 | CA | 6965 | 3 | 5/16 |
| http://61.149.132.196:8888 | CN | 1916 | 3 | 30/76 |
| http://113.45.195.147:3128 | CN | 2707 | 3 | 59/96 |
| http://114.249.232.222:8888 | CN | 6691 | 3 | 37/96 |
| http://222.128.173.231:8888 | CN | 1195 | 3 | 39/99 |
| http://45.65.138.48:999 | CO | 5671 | 3 | 48/131 |
| http://186.96.111.214:999 | CO | 3145 | 3 | 49/120 |
| http://103.172.17.51:8080 | ID | 6077 | 3 | 9/23 |
| http://103.193.144.223:8080 | ID | 5346 | 3 | 15/99 |
| http://56.155.73.159:27549 | JP | 1910 | 3 | 16/72 |
| http://56.68.116.64:15932 | MY | 3459 | 3 | 13/71 |
