# Proxy status

Generated 2026-09-23T22:26:33Z by `harvest.py`.

- **2435** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3877** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34916** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 179/600 (30%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2445 |
| socks5 | 1412 |
| socks4 | 20 |

| country | entries |
|---|---|
| NL | 1154 |
| ID | 619 |
| US | 259 |
| CN | 133 |
| RU | 113 |
| PH | 97 |
| ?? | 97 |
| MX | 86 |
| CO | 78 |
| DE | 76 |
| IN | 75 |
| BR | 70 |
| BD | 68 |
| VN | 58 |
| VE | 57 |
| SG | 46 |
| TR | 44 |
| FR | 42 |
| EC | 34 |
| JP | 34 |
| DO | 33 |
| PL | 33 |
| EG | 31 |
| HK | 29 |
| CA | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 2 | 2026-09-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 70 | 70 | 36 | 2026-09-23 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-09-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 134 | 134 | 57 | 2026-09-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-09-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 182 | 182 | 72 | 2026-09-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 258 | 258 | 98 | 2026-09-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 350 | 350 | 121 | 2026-09-23 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 429 | 429 | 225 | 2026-09-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 539 | 539 | 49 | 2026-09-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-09-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-09-23 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1772 | 1768 | 183 | 2026-09-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1592 | 2026-09-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2478 | 2476 | 679 | 2026-09-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2648 | 2646 | 1909 | 2026-09-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2680 | 2678 | 444 | 2026-09-23 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 19456 | 19456 | 10231 | 2026-09-23 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 26626 | 26625 | 2764 | 2026-09-23 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 968 | 75 | 88/89 |
| http://130.110.103.245:3128 | SA | 1212 | 75 | 87/89 |
| http://1.231.81.166:3128 | KR | 1299 | 54 | 86/89 |
| http://190.97.236.128:999 | VE | 699 | 46 | 77/79 |
| http://190.97.236.129:999 | VE | 694 | 46 | 77/79 |
| http://95.3.69.222:8080 | TR | 1216 | 44 | 86/89 |
| http://186.5.94.206:999 | EC | 759 | 26 | 49/51 |
| http://107.150.41.226:18080 | US | 454 | 26 | 26/26 |
| http://38.51.207.104:8080 | VE | 906 | 22 | 29/30 |
| http://193.104.179.115:3128 | UZ | 1532 | 19 | 37/54 |
| http://190.0.246.213:4040 | CO | 500 | 18 | 47/54 |
| http://213.111.146.36:18080 | NL | 5628 | 18 | 21/26 |
| http://153.51.201.35:999 | VE | 685 | 16 | 16/16 |
| http://201.71.2.27:999 | VE | 2388 | 15 | 36/87 |
| socks5://193.233.223.47:1080 | RU | 1090 | 14 | 14/14 |
| http://144.124.251.24:10007 | NL | 499 | 13 | 20/38 |
| http://144.124.251.24:10008 | NL | 637 | 13 | 16/20 |
| http://144.124.251.24:10104 | NL | 496 | 13 | 16/21 |
| http://144.124.251.24:10176 | NL | 479 | 13 | 20/37 |
| http://144.124.251.24:10185 | NL | 500 | 13 | 17/21 |
| http://144.124.251.24:10216 | NL | 635 | 13 | 21/38 |
| http://144.124.251.24:10226 | NL | 706 | 13 | 15/20 |
| http://144.124.251.24:10333 | NL | 2020 | 13 | 19/38 |
| http://144.124.251.24:10346 | NL | 597 | 13 | 17/21 |
| http://144.124.251.24:10366 | NL | 556 | 13 | 18/35 |
| http://144.124.251.24:10372 | NL | 479 | 13 | 20/33 |
| http://144.124.251.24:10431 | NL | 821 | 13 | 22/37 |
| http://144.124.251.24:10453 | NL | 592 | 13 | 19/26 |
| http://144.124.251.24:10551 | NL | 526 | 13 | 21/37 |
| http://144.124.251.24:10574 | NL | 496 | 13 | 21/38 |
| http://144.124.251.24:10628 | NL | 504 | 13 | 16/21 |
| http://144.124.251.24:10771 | NL | 652 | 13 | 16/21 |
| http://144.124.251.24:10953 | NL | 750 | 13 | 17/21 |
| http://144.124.251.24:11011 | NL | 589 | 13 | 17/21 |
| http://144.124.251.24:11265 | NL | 1095 | 13 | 20/37 |
| http://144.124.251.24:11266 | NL | 523 | 13 | 17/21 |
| http://144.124.251.24:11274 | NL | 495 | 13 | 20/37 |
| http://144.124.251.24:11480 | NL | 527 | 13 | 15/21 |
| http://144.124.251.24:11491 | NL | 511 | 13 | 20/37 |
| socks5://45.32.160.61:1088 | US | 272 | 12 | 39/42 |
| socks5://83.147.217.103:1080 | US | 118 | 12 | 12/12 |
| http://144.124.251.24:10801 | NL | 1469 | 11 | 17/37 |
| socks5://213.199.47.140:1080 | FR | 3071 | 11 | 47/55 |
| socks5://95.181.160.37:1080 | DE | 5566 | 10 | 10/10 |
| socks5://185.87.255.54:1080 | GB | 715 | 10 | 10/10 |
| socks5://101.36.104.239:10808 | JP | 2279 | 10 | 73/89 |
| socks5://135.148.120.20:1080 | US | 310 | 10 | 15/16 |
| http://190.0.246.211:4040 | CO | 624 | 9 | 76/89 |
| http://144.124.251.24:10082 | NL | 899 | 9 | 19/37 |
| http://167.172.76.176:9090 | SG | 1150 | 9 | 31/50 |
| socks5://103.75.118.84:1080 | JP | 1858 | 9 | 63/84 |
| http://185.195.71.218:18080 | CH | 1492 | 8 | 18/26 |
| http://144.124.251.24:10261 | NL | 556 | 8 | 16/21 |
| http://128.199.116.219:9090 | SG | 1148 | 8 | 8/8 |
| socks5://101.36.104.46:10808 | JP | 1923 | 8 | 79/89 |
| http://213.32.70.99:3128 | FR | 615 | 7 | 7/7 |
| http://154.59.56.76:999 | VE | 4565 | 7 | 38/49 |
| http://200.59.191.27:999 | VE | 6595 | 7 | 54/84 |
| http://181.119.224.25:8080 | EC | 728 | 6 | 6/6 |
| http://197.224.185.3:3128 | MU | 1003 | 6 | 52/57 |
| http://144.124.251.24:10084 | NL | 493 | 6 | 16/21 |
| http://144.124.251.24:10088 | NL | 2206 | 6 | 15/21 |
| http://144.124.251.24:10299 | NL | 464 | 6 | 16/21 |
| http://144.124.251.24:10337 | NL | 488 | 6 | 16/21 |
| http://144.124.251.24:10412 | NL | 490 | 6 | 16/21 |
| http://144.124.251.24:10471 | NL | 587 | 6 | 20/36 |
| http://144.124.251.24:10566 | NL | 615 | 6 | 17/22 |
| http://144.124.251.24:10605 | NL | 516 | 6 | 16/21 |
| http://144.124.251.24:10610 | NL | 500 | 6 | 16/21 |
| http://144.124.251.24:10631 | NL | 522 | 6 | 16/21 |
| http://144.124.251.24:10658 | NL | 502 | 6 | 16/21 |
| http://144.124.251.24:10689 | NL | 494 | 6 | 17/25 |
| http://144.124.251.24:10800 | NL | 489 | 6 | 16/21 |
| http://144.124.251.24:10811 | NL | 574 | 6 | 16/21 |
| http://144.124.251.24:10818 | NL | 651 | 6 | 13/21 |
| http://144.124.251.24:11450 | NL | 521 | 6 | 14/21 |
| http://34.43.46.91:80 | US | 545 | 6 | 85/89 |
| http://172.210.12.8:3128 | US | 188 | 6 | 11/25 |
| socks5://77.110.104.9:1080 | RU | 908 | 6 | 18/32 |
| socks5://141.148.158.143:1080 | US | 623 | 6 | 43/88 |
| http://40.176.175.23:26204 | CA | 1385 | 5 | 21/75 |
| http://120.232.115.170:17981 | CN | 1578 | 5 | 65/88 |
| http://190.0.246.210:4040 | CO | 571 | 5 | 77/88 |
| http://103.237.102.191:11111 | DE | 1118 | 5 | 83/89 |
| http://142.93.217.232:3129 | IN | 1526 | 5 | 22/49 |
| http://35.78.212.217:32053 | JP | 2912 | 5 | 15/71 |
| http://154.59.56.72:999 | VE | 2467 | 5 | 31/48 |
| http://154.59.56.73:999 | VE | 4116 | 5 | 48/61 |
| http://190.97.236.130:999 | VE | 595 | 5 | 15/18 |
| http://210.211.113.36:80 | VN | 6727 | 5 | 37/60 |
| http://168.194.34.196:9001 | AR | 1554 | 4 | 24/87 |
| http://187.102.219.32:999 | AR | 1587 | 4 | 21/88 |
| http://200.229.65.172:3128 | BR | 2732 | 4 | 4/4 |
| http://38.7.195.50:999 | CL | 2763 | 4 | 23/48 |
| http://38.7.195.53:999 | CL | 3259 | 4 | 30/88 |
| http://47.110.226.74:19991 | CN | 1578 | 4 | 38/87 |
| http://200.10.31.45:8081 | CO | 4849 | 4 | 36/86 |
| http://18.157.123.132:3128 | DE | 513 | 4 | 36/50 |
| http://67.207.72.60:3128 | DE | 515 | 4 | 4/4 |
| http://159.195.53.110:3128 | DE | 730 | 4 | 6/9 |
