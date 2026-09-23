# Proxy status

Generated 2026-09-23T17:51:10Z by `harvest.py`.

- **1949** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3461** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34446** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 195/600 (32%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1945 |
| socks5 | 1499 |
| socks4 | 17 |

| country | entries |
|---|---|
| NL | 1262 |
| ID | 489 |
| US | 142 |
| ?? | 128 |
| CN | 94 |
| RU | 84 |
| MX | 80 |
| CO | 69 |
| DE | 68 |
| IN | 68 |
| PH | 68 |
| BD | 60 |
| VN | 50 |
| BR | 48 |
| VE | 48 |
| SG | 43 |
| EG | 33 |
| FR | 30 |
| PL | 29 |
| TR | 29 |
| HK | 28 |
| JP | 28 |
| AR | 26 |
| CA | 26 |
| EC | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 2 | 2026-09-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 70 | 70 | 9 | 2026-09-23 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 108 | 108 | 42 | 2026-09-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 67 | 2026-09-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 151 | 151 | 85 | 2026-09-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 155 | 155 | 60 | 2026-09-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-23 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 409 | 409 | 55 | 2026-09-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 425 | 425 | 182 | 2026-09-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 492 | 492 | 226 | 2026-09-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-09-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-09-23 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1435 | 1431 | 328 | 2026-09-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1146 | 2026-09-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-09-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2532 | 2530 | 677 | 2026-09-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2774 | 2772 | 2068 | 2026-09-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2947 | 2945 | 636 | 2026-09-23 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 19130 | 19130 | 9982 | 2026-09-23 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 25811 | 25810 | 2507 | 2026-09-23 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 795 | 74 | 87/88 |
| http://130.110.103.245:3128 | SA | 1189 | 74 | 86/88 |
| http://1.231.81.166:3128 | KR | 1172 | 53 | 85/88 |
| http://190.97.236.128:999 | VE | 814 | 45 | 76/78 |
| http://190.97.236.129:999 | VE | 733 | 45 | 76/78 |
| http://95.3.69.222:8080 | TR | 1245 | 43 | 85/88 |
| http://186.5.94.206:999 | EC | 1901 | 25 | 48/50 |
| http://107.150.41.226:18080 | US | 314 | 25 | 25/25 |
| http://38.51.207.104:8080 | VE | 555 | 21 | 28/29 |
| http://193.104.179.115:3128 | UZ | 1450 | 18 | 36/53 |
| http://190.0.246.213:4040 | CO | 553 | 17 | 46/53 |
| http://213.111.146.36:18080 | NL | 6557 | 17 | 20/25 |
| http://153.51.201.35:999 | VE | 737 | 15 | 15/15 |
| http://201.71.2.27:999 | VE | 3628 | 14 | 35/86 |
| socks5://193.233.223.47:1080 | RU | 1251 | 13 | 13/13 |
| http://144.124.251.24:10007 | NL | 806 | 12 | 19/37 |
| http://144.124.251.24:10008 | NL | 816 | 12 | 15/19 |
| http://144.124.251.24:10104 | NL | 851 | 12 | 15/20 |
| http://144.124.251.24:10176 | NL | 777 | 12 | 19/36 |
| http://144.124.251.24:10185 | NL | 873 | 12 | 16/20 |
| http://144.124.251.24:10216 | NL | 769 | 12 | 20/37 |
| http://144.124.251.24:10226 | NL | 632 | 12 | 14/19 |
| http://144.124.251.24:10333 | NL | 615 | 12 | 18/37 |
| http://144.124.251.24:10346 | NL | 946 | 12 | 16/20 |
| http://144.124.251.24:10366 | NL | 592 | 12 | 17/34 |
| http://144.124.251.24:10372 | NL | 837 | 12 | 19/32 |
| http://144.124.251.24:10431 | NL | 917 | 12 | 21/36 |
| http://144.124.251.24:10453 | NL | 580 | 12 | 18/25 |
| http://144.124.251.24:10551 | NL | 768 | 12 | 20/36 |
| http://144.124.251.24:10574 | NL | 677 | 12 | 20/37 |
| http://144.124.251.24:10628 | NL | 791 | 12 | 15/20 |
| http://144.124.251.24:10771 | NL | 787 | 12 | 15/20 |
| http://144.124.251.24:10953 | NL | 637 | 12 | 16/20 |
| http://144.124.251.24:11011 | NL | 651 | 12 | 16/20 |
| http://144.124.251.24:11265 | NL | 721 | 12 | 19/36 |
| http://144.124.251.24:11266 | NL | 635 | 12 | 16/20 |
| http://144.124.251.24:11274 | NL | 617 | 12 | 19/36 |
| http://144.124.251.24:11480 | NL | 1156 | 12 | 14/20 |
| http://144.124.251.24:11491 | NL | 737 | 12 | 19/36 |
| socks5://45.32.160.61:1088 | US | 333 | 11 | 38/41 |
| socks5://83.147.217.103:1080 | US | 195 | 11 | 11/11 |
| http://144.124.251.24:10801 | NL | 602 | 10 | 16/36 |
| socks5://213.199.47.140:1080 | FR | 2671 | 10 | 46/54 |
| socks5://95.181.160.37:1080 | DE | 1614 | 9 | 9/9 |
| socks5://185.87.255.54:1080 | GB | 828 | 9 | 9/9 |
| socks5://101.36.104.239:10808 | JP | 1298 | 9 | 72/88 |
| socks5://150.109.247.86:8443 | KR | 1091 | 9 | 9/9 |
| socks5://135.148.120.20:1080 | US | 436 | 9 | 14/15 |
| http://190.0.246.211:4040 | CO | 951 | 8 | 75/88 |
| http://144.124.251.24:10082 | NL | 1151 | 8 | 18/36 |
| http://167.172.76.176:9090 | SG | 1101 | 8 | 30/49 |
| socks5://103.75.118.84:1080 | JP | 2480 | 8 | 62/83 |
| http://185.195.71.218:18080 | CH | 672 | 7 | 17/25 |
| http://144.124.251.24:10261 | NL | 851 | 7 | 15/20 |
| http://128.199.116.219:9090 | SG | 1077 | 7 | 7/7 |
| socks5://101.36.104.46:10808 | JP | 1756 | 7 | 78/88 |
| http://213.32.70.99:3128 | FR | 588 | 6 | 6/6 |
| http://154.59.56.76:999 | VE | 2103 | 6 | 37/48 |
| http://200.59.191.27:999 | VE | 4533 | 6 | 53/83 |
| socks5://121.169.46.116:1090 | KR | 2308 | 6 | 59/88 |
| socks5://45.61.129.165:9050 | US | 2026 | 6 | 70/88 |
| http://181.119.224.25:8080 | EC | 776 | 5 | 5/5 |
| http://197.224.185.3:3128 | MU | 1826 | 5 | 51/56 |
| http://144.124.251.24:10084 | NL | 763 | 5 | 15/20 |
| http://144.124.251.24:10088 | NL | 651 | 5 | 14/20 |
| http://144.124.251.24:10299 | NL | 675 | 5 | 15/20 |
| http://144.124.251.24:10337 | NL | 706 | 5 | 15/20 |
| http://144.124.251.24:10412 | NL | 682 | 5 | 15/20 |
| http://144.124.251.24:10471 | NL | 610 | 5 | 19/35 |
| http://144.124.251.24:10566 | NL | 600 | 5 | 16/21 |
| http://144.124.251.24:10605 | NL | 749 | 5 | 15/20 |
| http://144.124.251.24:10610 | NL | 869 | 5 | 15/20 |
| http://144.124.251.24:10631 | NL | 1193 | 5 | 15/20 |
| http://144.124.251.24:10658 | NL | 725 | 5 | 15/20 |
| http://144.124.251.24:10689 | NL | 658 | 5 | 16/24 |
| http://144.124.251.24:10800 | NL | 737 | 5 | 15/20 |
| http://144.124.251.24:10811 | NL | 583 | 5 | 15/20 |
| http://144.124.251.24:10818 | NL | 761 | 5 | 12/20 |
| http://144.124.251.24:11450 | NL | 840 | 5 | 13/20 |
| http://34.43.46.91:80 | US | 447 | 5 | 84/88 |
| http://172.210.12.8:3128 | US | 152 | 5 | 10/24 |
| socks5://77.110.104.9:1080 | RU | 1134 | 5 | 17/31 |
| socks5://141.148.158.143:1080 | US | 3761 | 5 | 42/87 |
| http://40.176.175.23:26204 | CA | 2720 | 4 | 20/74 |
| http://120.232.115.170:17981 | CN | 4666 | 4 | 64/87 |
| http://190.0.246.210:4040 | CO | 721 | 4 | 76/87 |
| http://103.237.102.191:11111 | DE | 708 | 4 | 82/88 |
| http://142.93.217.232:3129 | IN | 1779 | 4 | 21/48 |
| http://35.78.212.217:32053 | JP | 3116 | 4 | 14/70 |
| http://154.59.56.72:999 | VE | 3416 | 4 | 30/47 |
| http://154.59.56.73:999 | VE | 6378 | 4 | 47/60 |
| http://190.97.236.130:999 | VE | 773 | 4 | 14/17 |
| http://210.211.113.36:80 | VN | 2067 | 4 | 36/59 |
| socks5://216.9.224.173:1080 | TR | 6350 | 4 | 5/7 |
| http://168.194.34.196:9001 | AR | 2359 | 3 | 23/86 |
| http://187.102.219.32:999 | AR | 4265 | 3 | 20/87 |
| http://190.181.45.6:3128 | BO | 2441 | 3 | 8/26 |
| http://200.229.65.172:3128 | BR | 1577 | 3 | 3/3 |
| http://38.7.195.50:999 | CL | 3015 | 3 | 22/47 |
| http://38.7.195.53:999 | CL | 7097 | 3 | 29/87 |
