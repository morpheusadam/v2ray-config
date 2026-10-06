# Proxy status

Generated 2026-10-06T23:14:01Z by `harvest.py`.

- **2419** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4770** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39487** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 134/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2654 |
| http | 2109 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 2460 |
| ID | 616 |
| ?? | 128 |
| US | 107 |
| PH | 83 |
| MX | 81 |
| CO | 79 |
| CN | 77 |
| RU | 74 |
| IN | 65 |
| BD | 62 |
| EC | 58 |
| BR | 57 |
| VE | 56 |
| PK | 39 |
| JP | 38 |
| TR | 38 |
| DE | 37 |
| VN | 37 |
| SG | 34 |
| AR | 32 |
| CA | 32 |
| DO | 30 |
| EG | 28 |
| HK | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 2 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 74 | 74 | 12 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 82 | 82 | 35 | 2026-10-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 103 | 103 | 28 | 2026-10-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 113 | 113 | 47 | 2026-10-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 69 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 277 | 277 | 135 | 2026-10-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 552 | 552 | 323 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 584 | 584 | 140 | 2026-10-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-10-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1217 | 1213 | 160 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1148 | 2026-10-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1865 | 1863 | 702 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2045 | 2043 | 548 | 2026-10-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2058 | 2056 | 1438 | 2026-10-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 45146 | 45146 | 28516 | 2026-10-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 51293 | 51292 | 2544 | 2026-10-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.3.69.222:8080 | TR | 1351 | 69 | 111/114 |
| http://190.0.246.211:4040 | CO | 832 | 34 | 101/114 |
| http://34.43.46.91:80 | US | 394 | 31 | 110/114 |
| http://190.0.246.210:4040 | CO | 667 | 30 | 102/113 |
| http://34.43.46.91:443 | US | 388 | 27 | 108/114 |
| http://149.130.173.58:9443 | CO | 529 | 25 | 25/25 |
| http://43.173.120.13:8899 | US | 240 | 25 | 25/25 |
| socks5://171.25.158.95:1080 | SE | 1741 | 12 | 24/29 |
| socks5://213.199.47.140:1080 | FR | 1457 | 11 | 66/80 |
| socks5://47.238.126.208:1080 | HK | 1237 | 11 | 18/19 |
| socks5://85.209.156.148:1080 | US | 2801 | 11 | 48/85 |
| socks5://83.147.217.103:1080 | US | 313 | 10 | 34/37 |
| socks5://107.167.18.122:443 | US | 349 | 10 | 62/66 |
| http://184.75.221.82:3118 | CA | 307 | 9 | 70/79 |
| http://123.121.123.115:8888 | CN | 1585 | 9 | 23/38 |
| socks5://123.58.219.171:10808 | HK | 3133 | 9 | 88/114 |
| http://119.188.131.55:17981 | CN | 3791 | 8 | 56/114 |
| http://190.0.246.213:4040 | CO | 581 | 8 | 71/79 |
| http://45.245.208.181:8080 | EG | 3218 | 8 | 10/18 |
| http://144.124.251.24:10000 | NL | 1046 | 8 | 40/60 |
| http://144.124.251.24:10007 | NL | 935 | 8 | 40/63 |
| http://144.124.251.24:10008 | NL | 652 | 8 | 36/45 |
| http://144.124.251.24:10082 | NL | 1277 | 8 | 37/62 |
| http://144.124.251.24:10088 | NL | 746 | 8 | 35/46 |
| http://144.124.251.24:10104 | NL | 1404 | 8 | 36/46 |
| http://144.124.251.24:10176 | NL | 690 | 8 | 40/62 |
| http://144.124.251.24:10185 | NL | 676 | 8 | 37/46 |
| http://144.124.251.24:10187 | NL | 993 | 8 | 36/60 |
| http://144.124.251.24:10216 | NL | 695 | 8 | 41/63 |
| http://144.124.251.24:10226 | NL | 2929 | 8 | 35/45 |
| http://144.124.251.24:10230 | NL | 777 | 8 | 39/61 |
| http://144.124.251.24:10261 | NL | 779 | 8 | 36/46 |
| http://144.124.251.24:10299 | NL | 757 | 8 | 35/46 |
| http://144.124.251.24:10333 | NL | 646 | 8 | 39/63 |
| http://144.124.251.24:10337 | NL | 669 | 8 | 34/46 |
| http://144.124.251.24:10346 | NL | 823 | 8 | 37/46 |
| http://144.124.251.24:10366 | NL | 931 | 8 | 37/60 |
| http://144.124.251.24:10372 | NL | 772 | 8 | 40/58 |
| http://144.124.251.24:10412 | NL | 1418 | 8 | 36/46 |
| http://144.124.251.24:10431 | NL | 703 | 8 | 42/62 |
| http://144.124.251.24:10453 | NL | 844 | 8 | 39/51 |
| http://144.124.251.24:10471 | NL | 956 | 8 | 40/61 |
| http://144.124.251.24:10551 | NL | 1274 | 8 | 41/62 |
| http://144.124.251.24:10566 | NL | 694 | 8 | 37/47 |
| http://144.124.251.24:10574 | NL | 994 | 8 | 41/63 |
| http://144.124.251.24:10601 | NL | 746 | 8 | 34/61 |
| http://144.124.251.24:10605 | NL | 702 | 8 | 36/46 |
| http://144.124.251.24:10610 | NL | 698 | 8 | 36/46 |
| http://144.124.251.24:10628 | NL | 1078 | 8 | 34/46 |
| http://144.124.251.24:10631 | NL | 649 | 8 | 36/46 |
| http://144.124.251.24:10658 | NL | 637 | 8 | 36/46 |
| http://144.124.251.24:10689 | NL | 785 | 8 | 37/50 |
| http://144.124.251.24:10771 | NL | 725 | 8 | 36/46 |
| http://144.124.251.24:10800 | NL | 723 | 8 | 36/46 |
| http://144.124.251.24:10801 | NL | 841 | 8 | 37/62 |
| http://144.124.251.24:10811 | NL | 799 | 8 | 36/46 |
| http://144.124.251.24:10818 | NL | 695 | 8 | 33/46 |
| http://144.124.251.24:10829 | NL | 764 | 8 | 34/46 |
| http://144.124.251.24:10953 | NL | 730 | 8 | 37/46 |
| http://144.124.251.24:11011 | NL | 850 | 8 | 37/46 |
| http://144.124.251.24:11108 | NL | 878 | 8 | 37/61 |
| http://144.124.251.24:11124 | NL | 638 | 8 | 38/63 |
| http://144.124.251.24:11180 | NL | 695 | 8 | 35/45 |
| http://144.124.251.24:11265 | NL | 755 | 8 | 40/62 |
| http://144.124.251.24:11266 | NL | 759 | 8 | 37/46 |
| http://144.124.251.24:11274 | NL | 776 | 8 | 40/62 |
| http://144.124.251.24:11450 | NL | 706 | 8 | 34/46 |
| http://144.124.251.24:11480 | NL | 853 | 8 | 35/46 |
| http://144.124.251.24:11491 | NL | 785 | 8 | 40/62 |
| http://190.12.150.244:999 | EC | 2753 | 7 | 79/110 |
| http://44.216.27.249:3128 | US | 237 | 7 | 10/11 |
| socks5://103.75.118.84:1080 | JP | 855 | 7 | 79/109 |
| http://102.244.78.61:8090 | CM | 1327 | 6 | 6/6 |
| http://51.170.133.249:80 | MA | 2324 | 6 | 20/37 |
| http://197.224.185.3:3128 | MU | 1941 | 6 | 75/82 |
| http://4.144.146.21:80 | SG | 1037 | 6 | 6/6 |
| http://128.199.121.61:9090 | SG | 1050 | 6 | 28/34 |
| http://165.154.162.73:8888 | US | 701 | 6 | 68/114 |
| socks5://65.21.252.66:10805 | FI | 3328 | 6 | 18/28 |
| http://187.102.219.64:999 | AR | 1870 | 5 | 28/53 |
| http://186.5.94.206:999 | EC | 930 | 5 | 70/76 |
| http://154.59.56.74:999 | VE | 2788 | 5 | 55/77 |
| socks5://47.83.158.131:3128 | HK | 1211 | 5 | 5/5 |
| socks5://107.149.92.23:8443 | HK | 3738 | 5 | 9/31 |
| socks5://101.36.104.46:10808 | JP | 1900 | 5 | 100/114 |
| socks5://57.128.231.218:1202 | PL | 1375 | 5 | 7/27 |
| socks5://57.128.231.218:1203 | PL | 1492 | 5 | 7/29 |
| socks5://212.3.127.242:10801 | UA | 1246 | 5 | 27/105 |
| socks5://107.174.30.94:1080 | US | 4363 | 5 | 6/8 |
| socks5://160.187.0.89:1080 | VN | 1581 | 5 | 20/27 |
| http://102.244.78.61:8085 | CM | 1309 | 4 | 4/4 |
| http://102.244.78.61:8087 | CM | 1316 | 4 | 4/4 |
| http://65.109.215.187:8090 | FI | 745 | 4 | 7/9 |
| http://65.109.219.108:2000 | FI | 1970 | 4 | 6/7 |
| http://176.111.37.5:39811 | HK | 1023 | 4 | 96/114 |
| http://176.111.37.216:39811 | HK | 865 | 4 | 93/114 |
| http://103.130.61.61:8081 | ID | 1703 | 4 | 89/114 |
| http://103.183.8.135:8080 | ID | 5998 | 4 | 18/102 |
| http://110.76.147.26:1111 | ID | 2597 | 4 | 18/114 |
| http://160.22.195.10:8097 | ID | 6750 | 4 | 9/27 |
