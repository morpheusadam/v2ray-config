# Proxy status

Generated 2026-09-22T22:24:16Z by `harvest.py`.

- **1441** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3096** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33852** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 150/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1552 |
| socks5 | 1534 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 1303 |
| ID | 350 |
| US | 156 |
| CN | 99 |
| RU | 94 |
| DE | 62 |
| MX | 60 |
| CO | 56 |
| PH | 55 |
| IN | 54 |
| SG | 52 |
| VE | 48 |
| BD | 40 |
| VN | 37 |
| BR | 36 |
| EG | 32 |
| FR | 32 |
| JP | 28 |
| CA | 26 |
| AR | 25 |
| HK | 25 |
| TR | 25 |
| ZA | 25 |
| EC | 22 |
| PL | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 3 | 2026-09-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 75 | 75 | 37 | 2026-09-22 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 84 | 2026-09-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 120 | 120 | 51 | 2026-09-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 84 | 2026-09-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 155 | 155 | 48 | 2026-09-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 228 | 228 | 98 | 2026-09-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 228 | 228 | 112 | 2026-09-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 345 | 345 | 42 | 2026-09-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 378 | 378 | 186 | 2026-09-22 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-09-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1144 | 2026-09-22 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1737 | 1733 | 323 | 2026-09-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-09-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2487 | 2485 | 661 | 2026-09-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2677 | 2675 | 443 | 2026-09-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2913 | 2911 | 2074 | 2026-09-22 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 18366 | 18366 | 9708 | 2026-09-22 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 25475 | 25474 | 2711 | 2026-09-22 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1068 | 73 | 86/87 |
| http://130.110.103.245:3128 | SA | 1688 | 73 | 85/87 |
| http://1.231.81.166:3128 | KR | 1466 | 52 | 84/87 |
| http://190.97.236.128:999 | VE | 662 | 44 | 75/77 |
| http://190.97.236.129:999 | VE | 692 | 44 | 75/77 |
| http://95.3.69.222:8080 | TR | 1447 | 42 | 84/87 |
| http://186.5.94.206:999 | EC | 810 | 24 | 47/49 |
| http://107.150.41.226:18080 | US | 582 | 24 | 24/24 |
| http://38.51.207.104:8080 | VE | 2571 | 20 | 27/28 |
| http://193.104.179.115:3128 | UZ | 1151 | 17 | 35/52 |
| http://190.0.246.213:4040 | CO | 551 | 16 | 45/52 |
| http://213.111.146.36:18080 | NL | 493 | 16 | 19/24 |
| http://153.51.201.35:999 | VE | 697 | 14 | 14/14 |
| http://201.71.2.27:999 | VE | 2183 | 13 | 34/85 |
| http://190.97.241.106:999 | VE | 522 | 12 | 47/71 |
| socks5://193.233.223.47:1080 | RU | 1126 | 12 | 12/12 |
| http://176.111.37.5:39811 | HK | 833 | 11 | 80/87 |
| http://144.124.251.24:10000 | NL | 619 | 11 | 19/33 |
| http://144.124.251.24:10007 | NL | 645 | 11 | 18/36 |
| http://144.124.251.24:10008 | NL | 744 | 11 | 14/18 |
| http://144.124.251.24:10104 | NL | 703 | 11 | 14/19 |
| http://144.124.251.24:10176 | NL | 1070 | 11 | 18/35 |
| http://144.124.251.24:10185 | NL | 716 | 11 | 15/19 |
| http://144.124.251.24:10216 | NL | 646 | 11 | 19/36 |
| http://144.124.251.24:10226 | NL | 686 | 11 | 13/18 |
| http://144.124.251.24:10333 | NL | 561 | 11 | 17/36 |
| http://144.124.251.24:10346 | NL | 698 | 11 | 15/19 |
| http://144.124.251.24:10366 | NL | 565 | 11 | 16/33 |
| http://144.124.251.24:10372 | NL | 512 | 11 | 18/31 |
| http://144.124.251.24:10431 | NL | 1906 | 11 | 20/35 |
| http://144.124.251.24:10453 | NL | 685 | 11 | 17/24 |
| http://144.124.251.24:10551 | NL | 701 | 11 | 19/35 |
| http://144.124.251.24:10574 | NL | 565 | 11 | 19/36 |
| http://144.124.251.24:10628 | NL | 754 | 11 | 14/19 |
| http://144.124.251.24:10771 | NL | 1307 | 11 | 14/19 |
| http://144.124.251.24:10829 | NL | 574 | 11 | 14/19 |
| http://144.124.251.24:10953 | NL | 553 | 11 | 15/19 |
| http://144.124.251.24:11011 | NL | 644 | 11 | 15/19 |
| http://144.124.251.24:11108 | NL | 533 | 11 | 16/34 |
| http://144.124.251.24:11180 | NL | 705 | 11 | 14/18 |
| http://144.124.251.24:11265 | NL | 598 | 11 | 18/35 |
| http://144.124.251.24:11266 | NL | 557 | 11 | 15/19 |
| http://144.124.251.24:11274 | NL | 648 | 11 | 18/35 |
| http://144.124.251.24:11480 | NL | 673 | 11 | 13/19 |
| http://144.124.251.24:11491 | NL | 694 | 11 | 18/35 |
| socks5://161.35.90.93:1082 | NL | 1863 | 11 | 49/87 |
| socks5://45.32.160.61:1088 | US | 235 | 10 | 37/40 |
| socks5://83.147.217.103:1080 | US | 114 | 10 | 10/10 |
| http://144.124.251.24:10187 | NL | 577 | 9 | 15/33 |
| http://144.124.251.24:10230 | NL | 539 | 9 | 18/34 |
| http://144.124.251.24:10801 | NL | 713 | 9 | 15/35 |
| socks5://213.199.47.140:1080 | FR | 2363 | 9 | 45/53 |
| socks5://95.181.160.37:1080 | DE | 631 | 8 | 8/8 |
| socks5://144.91.111.48:1088 | FR | 1950 | 8 | 55/87 |
| socks5://185.87.255.54:1080 | GB | 609 | 8 | 8/8 |
| socks5://101.36.104.239:10808 | JP | 3098 | 8 | 71/87 |
| socks5://150.109.247.86:8443 | KR | 1146 | 8 | 8/8 |
| socks5://135.148.120.20:1080 | US | 291 | 8 | 13/14 |
| http://190.0.246.211:4040 | CO | 829 | 7 | 74/87 |
| http://144.124.251.24:10082 | NL | 746 | 7 | 17/35 |
| http://167.172.76.176:9090 | SG | 1137 | 7 | 29/48 |
| socks5://103.75.118.84:1080 | JP | 1411 | 7 | 61/82 |
| http://185.195.71.218:18080 | CH | 576 | 6 | 16/24 |
| http://47.107.107.24:80 | CN | 2224 | 6 | 32/55 |
| http://144.124.251.24:10261 | NL | 711 | 6 | 14/19 |
| http://128.199.116.219:9090 | SG | 1149 | 6 | 6/6 |
| http://14.225.68.207:1337 | VN | 1351 | 6 | 6/6 |
| socks5://101.36.104.46:10808 | JP | 3390 | 6 | 77/87 |
| socks5://144.24.47.42:1080 | US | 411 | 6 | 49/83 |
| http://213.32.70.99:3128 | FR | 484 | 5 | 5/5 |
| http://144.124.251.24:10601 | NL | 570 | 5 | 15/34 |
| http://154.59.56.74:999 | VE | 3945 | 5 | 35/50 |
| http://154.59.56.76:999 | VE | 4317 | 5 | 36/47 |
| http://200.59.191.27:999 | VE | 3437 | 5 | 52/82 |
| socks5://121.169.46.116:1090 | KR | 1820 | 5 | 58/87 |
| socks5://45.61.129.165:9050 | US | 1679 | 5 | 69/87 |
| http://181.119.224.25:8080 | EC | 887 | 4 | 4/4 |
| http://103.157.79.5:8080 | ID | 2598 | 4 | 5/20 |
| http://43.207.141.180:1586 | JP | 5922 | 4 | 16/71 |
| http://197.224.185.3:3128 | MU | 1769 | 4 | 50/55 |
| http://144.124.251.24:10084 | NL | 680 | 4 | 14/19 |
| http://144.124.251.24:10088 | NL | 543 | 4 | 13/19 |
| http://144.124.251.24:10299 | NL | 808 | 4 | 14/19 |
| http://144.124.251.24:10337 | NL | 754 | 4 | 14/19 |
| http://144.124.251.24:10412 | NL | 650 | 4 | 14/19 |
| http://144.124.251.24:10471 | NL | 613 | 4 | 18/34 |
| http://144.124.251.24:10566 | NL | 620 | 4 | 15/20 |
| http://144.124.251.24:10605 | NL | 547 | 4 | 14/19 |
| http://144.124.251.24:10610 | NL | 605 | 4 | 14/19 |
| http://144.124.251.24:10631 | NL | 592 | 4 | 14/19 |
| http://144.124.251.24:10658 | NL | 607 | 4 | 14/19 |
| http://144.124.251.24:10689 | NL | 594 | 4 | 15/23 |
| http://144.124.251.24:10800 | NL | 702 | 4 | 14/19 |
| http://144.124.251.24:10811 | NL | 541 | 4 | 14/19 |
| http://144.124.251.24:10818 | NL | 615 | 4 | 11/19 |
| http://144.124.251.24:11124 | NL | 665 | 4 | 17/36 |
| http://144.124.251.24:11450 | NL | 1199 | 4 | 12/19 |
| http://34.43.46.91:80 | US | 583 | 4 | 83/87 |
| http://172.210.12.8:3128 | US | 59 | 4 | 9/23 |
| socks5://109.123.249.138:10808 | FR | 821 | 4 | 4/4 |
