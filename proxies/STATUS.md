# Proxy status

Generated 2026-10-09T18:53:31Z by `harvest.py`.

- **1429** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3116** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39380** endpoints on record
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
| http | 1777 |
| socks5 | 1329 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 1123 |
| ID | 523 |
| US | 92 |
| CO | 84 |
| PH | 82 |
| RU | 81 |
| MX | 78 |
| CN | 67 |
| BR | 57 |
| BD | 55 |
| EC | 52 |
| VE | 49 |
| VN | 46 |
| TR | 45 |
| IN | 42 |
| DE | 39 |
| DO | 35 |
| SG | 32 |
| JP | 31 |
| AR | 30 |
| PK | 24 |
| EG | 23 |
| TH | 23 |
| CL | 22 |
| PE | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 3 | 2026-10-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 59 | 59 | 14 | 2026-10-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 95 | 95 | 45 | 2026-10-09 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 101 | 101 | 47 | 2026-10-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 125 | 125 | 38 | 2026-10-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-10-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 258 | 258 | 128 | 2026-10-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 273 | 273 | 81 | 2026-10-09 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 474 | 474 | 267 | 2026-10-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-10-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-10-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-10-09 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1730 | 1726 | 247 | 2026-10-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-10-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2616 | 2614 | 682 | 2026-10-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2744 | 2742 | 1981 | 2026-10-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2964 | 2962 | 657 | 2026-10-09 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 47229 | 47229 | 31156 | 2026-10-09 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 53141 | 53140 | 2591 | 2026-10-09 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 789 | 39 | 106/119 |
| http://34.43.46.91:80 | US | 607 | 36 | 115/119 |
| http://190.0.246.210:4040 | CO | 967 | 35 | 107/118 |
| http://149.130.173.58:9443 | CO | 465 | 30 | 30/30 |
| http://43.173.120.13:8899 | US | 459 | 30 | 30/30 |
| socks5://83.147.217.103:1080 | US | 226 | 15 | 39/42 |
| socks5://107.167.18.122:443 | US | 304 | 15 | 67/71 |
| http://190.0.246.213:4040 | CO | 593 | 13 | 76/84 |
| http://144.124.251.24:10008 | NL | 715 | 13 | 41/50 |
| http://144.124.251.24:10088 | NL | 1101 | 13 | 40/51 |
| http://144.124.251.24:10176 | NL | 690 | 13 | 45/67 |
| http://144.124.251.24:10185 | NL | 657 | 13 | 42/51 |
| http://144.124.251.24:10216 | NL | 704 | 13 | 46/68 |
| http://144.124.251.24:10226 | NL | 736 | 13 | 40/50 |
| http://144.124.251.24:10230 | NL | 777 | 13 | 44/66 |
| http://144.124.251.24:10261 | NL | 753 | 13 | 41/51 |
| http://144.124.251.24:10299 | NL | 851 | 13 | 40/51 |
| http://144.124.251.24:10333 | NL | 1325 | 13 | 44/68 |
| http://144.124.251.24:10337 | NL | 669 | 13 | 39/51 |
| http://144.124.251.24:10346 | NL | 687 | 13 | 42/51 |
| http://144.124.251.24:10366 | NL | 894 | 13 | 42/65 |
| http://144.124.251.24:10372 | NL | 774 | 13 | 45/63 |
| http://144.124.251.24:10431 | NL | 950 | 13 | 47/67 |
| http://144.124.251.24:10453 | NL | 682 | 13 | 44/56 |
| http://144.124.251.24:10471 | NL | 733 | 13 | 45/66 |
| http://144.124.251.24:10551 | NL | 703 | 13 | 46/67 |
| http://144.124.251.24:10566 | NL | 720 | 13 | 42/52 |
| http://144.124.251.24:10574 | NL | 680 | 13 | 46/68 |
| http://144.124.251.24:10601 | NL | 812 | 13 | 39/66 |
| http://144.124.251.24:10610 | NL | 736 | 13 | 41/51 |
| http://144.124.251.24:10628 | NL | 835 | 13 | 39/51 |
| http://144.124.251.24:10631 | NL | 726 | 13 | 41/51 |
| http://144.124.251.24:10689 | NL | 646 | 13 | 42/55 |
| http://144.124.251.24:10771 | NL | 778 | 13 | 41/51 |
| http://144.124.251.24:10800 | NL | 763 | 13 | 41/51 |
| http://144.124.251.24:10811 | NL | 796 | 13 | 41/51 |
| http://144.124.251.24:10818 | NL | 697 | 13 | 38/51 |
| http://144.124.251.24:10829 | NL | 709 | 13 | 39/51 |
| http://144.124.251.24:11011 | NL | 903 | 13 | 42/51 |
| http://144.124.251.24:11108 | NL | 779 | 13 | 42/66 |
| http://144.124.251.24:11124 | NL | 733 | 13 | 43/68 |
| http://144.124.251.24:11180 | NL | 896 | 13 | 40/50 |
| http://144.124.251.24:11265 | NL | 798 | 13 | 45/67 |
| http://144.124.251.24:11266 | NL | 810 | 13 | 42/51 |
| http://144.124.251.24:11450 | NL | 749 | 13 | 39/51 |
| http://197.224.185.3:3128 | MU | 2148 | 11 | 80/87 |
| http://165.154.162.73:8888 | US | 4398 | 11 | 73/119 |
| socks5://160.187.0.89:1080 | VN | 1927 | 10 | 25/32 |
| http://176.111.37.5:39811 | HK | 915 | 9 | 101/119 |
| http://176.111.37.216:39811 | HK | 967 | 9 | 98/119 |
| http://167.99.74.174:9090 | SG | 1035 | 9 | 53/79 |
| http://34.88.38.81:9443 | FI | 696 | 8 | 58/84 |
| http://35.228.49.168:9443 | FI | 746 | 8 | 39/56 |
| http://195.158.8.123:3128 | UZ | 2640 | 8 | 78/117 |
| http://120.232.115.57:17981 | CN | 1508 | 7 | 34/44 |
| http://189.51.168.165:999 | MX | 452 | 7 | 29/31 |
| http://5.129.254.5:8888 | RU | 1397 | 7 | 64/74 |
| http://5.129.254.49:8888 | RU | 1186 | 7 | 65/74 |
| http://5.129.254.51:8888 | RU | 1136 | 7 | 65/74 |
| http://5.129.254.60:8888 | RU | 1739 | 7 | 64/73 |
| http://5.129.254.70:8888 | RU | 1999 | 7 | 65/74 |
| http://5.129.254.129:8888 | RU | 1180 | 7 | 70/80 |
| http://5.129.254.154:8888 | RU | 1045 | 7 | 61/70 |
| http://5.129.254.215:8888 | RU | 1072 | 7 | 14/16 |
| http://5.129.254.243:8888 | RU | 2520 | 7 | 14/15 |
| http://49.229.100.235:8080 | TH | 1428 | 7 | 39/67 |
| http://114.244.214.18:8888 | CN | 7322 | 6 | 22/42 |
| http://103.237.102.191:11111 | DE | 865 | 6 | 112/119 |
| http://43.99.60.244:8089 | HK | 1089 | 6 | 39/69 |
| http://43.155.62.157:443 | HK | 5404 | 6 | 19/22 |
| http://128.199.116.219:9090 | SG | 1027 | 6 | 31/38 |
| http://61.91.162.126:8080 | TH | 1429 | 6 | 48/62 |
| http://103.10.231.189:8080 | TH | 1437 | 6 | 73/104 |
| http://38.51.207.116:999 | VE | 2772 | 6 | 27/117 |
| socks5://101.36.104.239:10808 | JP | 2755 | 6 | 101/119 |
| http://102.244.78.61:8081 | CM | 1353 | 5 | 5/5 |
| http://85.239.156.66:5555 | CZ | 3780 | 5 | 6/8 |
| http://144.124.251.24:10084 | NL | 692 | 5 | 39/51 |
| socks5://164.68.114.118:1080 | FR | 1001 | 5 | 5/5 |
| socks5://45.74.31.47:15727 | NL | 5517 | 5 | 5/5 |
| socks5://67.207.92.87:1088 | US | 692 | 5 | 65/118 |
| http://101.251.204.174:8080 | CN | 2109 | 4 | 58/105 |
| http://181.214.29.86:999 | DO | 5816 | 4 | 7/25 |
| http://186.5.94.206:999 | EC | 3118 | 4 | 74/81 |
| http://49.0.2.104:8989 | ID | 1338 | 4 | 15/42 |
| http://187.201.225.188:999 | MX | 519 | 4 | 4/4 |
| http://152.42.177.32:8888 | SG | 1026 | 4 | 46/79 |
| http://167.172.76.176:9090 | SG | 1029 | 4 | 55/80 |
| http://89.104.102.209:58080 | UZ | 6140 | 4 | 9/63 |
| http://38.51.207.117:999 | VE | 5267 | 4 | 25/96 |
| http://154.59.56.72:999 | VE | 2046 | 4 | 54/78 |
| http://154.59.56.78:999 | VE | 7208 | 4 | 52/75 |
| socks5://45.155.71.236:1080 | AT | 1942 | 4 | 12/24 |
| socks5://103.75.118.84:1080 | JP | 1070 | 4 | 83/114 |
| socks5://45.74.31.41:12507 | NL | 5505 | 4 | 4/4 |
| socks5://45.74.31.41:12929 | NL | 5474 | 4 | 8/34 |
| socks5://45.74.31.46:12764 | NL | 4675 | 4 | 5/6 |
| socks5://79.137.198.71:7777 | NL | 1248 | 4 | 14/19 |
| socks5://85.209.156.148:1080 | US | 1947 | 4 | 52/90 |
| socks5://129.153.11.56:1080 | US | 2320 | 4 | 17/24 |
