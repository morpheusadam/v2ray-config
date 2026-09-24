# Proxy status

Generated 2026-09-24T18:00:27Z by `harvest.py`.

- **1737** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3814** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35888** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 116/600 (19%)** — of a random sample of the shipped file, how many worked on a second pass

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
| socks5 | 1524 |
| socks4 | 20 |

| country | entries |
|---|---|
| NL | 1267 |
| ID | 597 |
| ?? | 152 |
| US | 151 |
| CN | 127 |
| RU | 103 |
| MX | 92 |
| PH | 90 |
| CO | 79 |
| BD | 73 |
| BR | 65 |
| IN | 65 |
| DE | 64 |
| VE | 57 |
| VN | 52 |
| SG | 46 |
| TR | 42 |
| EC | 36 |
| JP | 35 |
| FR | 34 |
| DO | 33 |
| PL | 31 |
| CA | 27 |
| EG | 27 |
| AR | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 1 | 2026-09-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 54 | 54 | 27 | 2026-09-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 77 | 77 | 20 | 2026-09-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 89 | 89 | 36 | 2026-09-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 125 | 125 | 41 | 2026-09-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 60 | 2026-09-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 213 | 213 | 89 | 2026-09-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 330 | 330 | 46 | 2026-09-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 387 | 387 | 172 | 2026-09-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-09-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-09-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1143 | 2026-09-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-09-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1893 | 1889 | 642 | 2026-09-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2112 | 2110 | 690 | 2026-09-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2468 | 2466 | 566 | 2026-09-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2519 | 2517 | 1860 | 2026-09-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 20219 | 20219 | 10521 | 2026-09-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 26583 | 26582 | 2571 | 2026-09-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 2639 | 76 | 89/90 |
| http://130.110.103.245:3128 | SA | 3273 | 76 | 88/90 |
| http://1.231.81.166:3128 | KR | 1768 | 55 | 87/90 |
| http://190.97.236.128:999 | VE | 917 | 47 | 78/80 |
| http://190.97.236.129:999 | VE | 822 | 47 | 78/80 |
| http://95.3.69.222:8080 | TR | 2581 | 45 | 87/90 |
| http://186.5.94.206:999 | EC | 1175 | 27 | 50/52 |
| http://107.150.41.226:18080 | US | 366 | 27 | 27/27 |
| http://38.51.207.104:8080 | VE | 673 | 23 | 30/31 |
| http://193.104.179.115:3128 | UZ | 1741 | 20 | 38/55 |
| http://190.0.246.213:4040 | CO | 782 | 19 | 48/55 |
| http://213.111.146.36:18080 | NL | 1023 | 19 | 22/27 |
| http://153.51.201.35:999 | VE | 1075 | 17 | 17/17 |
| socks5://193.233.223.47:1080 | RU | 1313 | 15 | 15/15 |
| http://144.124.251.24:10007 | NL | 1885 | 14 | 21/39 |
| http://144.124.251.24:10008 | NL | 2248 | 14 | 17/21 |
| http://144.124.251.24:10104 | NL | 1688 | 14 | 17/22 |
| http://144.124.251.24:10176 | NL | 679 | 14 | 21/38 |
| http://144.124.251.24:10185 | NL | 1238 | 14 | 18/22 |
| http://144.124.251.24:10216 | NL | 743 | 14 | 22/39 |
| http://144.124.251.24:10226 | NL | 1480 | 14 | 16/21 |
| http://144.124.251.24:10333 | NL | 857 | 14 | 20/39 |
| http://144.124.251.24:10346 | NL | 1799 | 14 | 18/22 |
| http://144.124.251.24:10366 | NL | 925 | 14 | 19/36 |
| http://144.124.251.24:10372 | NL | 704 | 14 | 21/34 |
| http://144.124.251.24:10431 | NL | 824 | 14 | 23/38 |
| http://144.124.251.24:10453 | NL | 706 | 14 | 20/27 |
| http://144.124.251.24:10551 | NL | 788 | 14 | 22/38 |
| http://144.124.251.24:10574 | NL | 723 | 14 | 22/39 |
| http://144.124.251.24:10628 | NL | 885 | 14 | 17/22 |
| http://144.124.251.24:10771 | NL | 2066 | 14 | 17/22 |
| http://144.124.251.24:10953 | NL | 1546 | 14 | 18/22 |
| http://144.124.251.24:11011 | NL | 1579 | 14 | 18/22 |
| http://144.124.251.24:11265 | NL | 838 | 14 | 21/38 |
| http://144.124.251.24:11266 | NL | 1443 | 14 | 18/22 |
| http://144.124.251.24:11274 | NL | 761 | 14 | 21/38 |
| http://144.124.251.24:11480 | NL | 7264 | 14 | 16/22 |
| http://144.124.251.24:11491 | NL | 813 | 14 | 21/38 |
| socks5://45.32.160.61:1088 | US | 489 | 13 | 40/43 |
| socks5://83.147.217.103:1080 | US | 583 | 13 | 13/13 |
| http://144.124.251.24:10801 | NL | 732 | 12 | 18/38 |
| socks5://213.199.47.140:1080 | FR | 2395 | 12 | 48/56 |
| socks5://185.87.255.54:1080 | GB | 1572 | 11 | 11/11 |
| socks5://101.36.104.239:10808 | JP | 4334 | 11 | 74/90 |
| http://190.0.246.211:4040 | CO | 1821 | 10 | 77/90 |
| http://144.124.251.24:10082 | NL | 875 | 10 | 20/38 |
| http://167.172.76.176:9090 | SG | 1017 | 10 | 32/51 |
| socks5://103.75.118.84:1080 | JP | 2987 | 10 | 64/85 |
| http://185.195.71.218:18080 | CH | 838 | 9 | 19/27 |
| http://144.124.251.24:10261 | NL | 1982 | 9 | 17/22 |
| http://128.199.116.219:9090 | SG | 1275 | 9 | 9/9 |
| socks5://101.36.104.46:10808 | JP | 1999 | 9 | 80/90 |
| http://213.32.70.99:3128 | FR | 1354 | 8 | 8/8 |
| http://154.59.56.76:999 | VE | 4460 | 8 | 39/50 |
| http://200.59.191.27:999 | VE | 6359 | 8 | 55/85 |
| http://181.119.224.25:8080 | EC | 1313 | 7 | 7/7 |
| http://197.224.185.3:3128 | MU | 1967 | 7 | 53/58 |
| http://144.124.251.24:10084 | NL | 3474 | 7 | 17/22 |
| http://144.124.251.24:10088 | NL | 2411 | 7 | 16/22 |
| http://144.124.251.24:10299 | NL | 935 | 7 | 17/22 |
| http://144.124.251.24:10337 | NL | 1255 | 7 | 17/22 |
| http://144.124.251.24:10412 | NL | 1550 | 7 | 17/22 |
| http://144.124.251.24:10471 | NL | 894 | 7 | 21/37 |
| http://144.124.251.24:10566 | NL | 873 | 7 | 18/23 |
| http://144.124.251.24:10605 | NL | 914 | 7 | 17/22 |
| http://144.124.251.24:10610 | NL | 1336 | 7 | 17/22 |
| http://144.124.251.24:10631 | NL | 1396 | 7 | 17/22 |
| http://144.124.251.24:10658 | NL | 2136 | 7 | 17/22 |
| http://144.124.251.24:10689 | NL | 727 | 7 | 18/26 |
| http://144.124.251.24:10800 | NL | 1726 | 7 | 17/22 |
| http://144.124.251.24:10811 | NL | 1841 | 7 | 17/22 |
| http://144.124.251.24:10818 | NL | 1514 | 7 | 14/22 |
| http://144.124.251.24:11450 | NL | 2352 | 7 | 15/22 |
| http://34.43.46.91:80 | US | 796 | 7 | 86/90 |
| http://172.210.12.8:3128 | US | 358 | 7 | 12/26 |
| http://190.0.246.210:4040 | CO | 1249 | 6 | 78/89 |
| http://103.237.102.191:11111 | DE | 1855 | 6 | 84/90 |
| http://142.93.217.232:3129 | IN | 1543 | 6 | 23/50 |
| http://35.78.212.217:32053 | JP | 3245 | 6 | 16/72 |
| http://154.59.56.72:999 | VE | 5876 | 6 | 32/49 |
| http://154.59.56.73:999 | VE | 5370 | 6 | 49/62 |
| http://190.97.236.130:999 | VE | 1227 | 6 | 16/19 |
| http://210.211.113.36:80 | VN | 4930 | 6 | 38/61 |
| http://187.102.219.32:999 | AR | 6237 | 5 | 22/89 |
| http://200.229.65.172:3128 | BR | 1637 | 5 | 5/5 |
| http://38.7.195.50:999 | CL | 5336 | 5 | 24/49 |
| http://38.7.195.53:999 | CL | 6418 | 5 | 31/89 |
| http://18.157.123.132:3128 | DE | 786 | 5 | 37/51 |
| http://159.195.53.110:3128 | DE | 4060 | 5 | 7/10 |
| http://103.130.61.61:8081 | ID | 1511 | 5 | 72/90 |
| http://3.216.199.128:3128 | US | 443 | 5 | 5/5 |
| http://195.158.8.123:3128 | UZ | 3336 | 5 | 60/88 |
| socks4://107.167.18.122:443 | US | 256 | 5 | 40/42 |
| socks5://109.205.182.143:1088 | FR | 970 | 5 | 5/5 |
| socks5://123.58.219.171:10808 | HK | 1977 | 5 | 72/90 |
| socks5://45.74.31.47:4707 | NL | 3215 | 5 | 5/5 |
| http://190.7.19.110:8080 | AR | 6118 | 4 | 12/54 |
| http://200.229.76.160:3128 | BR | 1893 | 4 | 8/10 |
| http://16.174.124.173:3851 | CA | 2706 | 4 | 14/54 |
| http://184.75.221.82:3118 | CA | 455 | 4 | 49/55 |
