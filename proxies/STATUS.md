# Proxy status

Generated 2026-10-07T23:47:40Z by `harvest.py`.

- **2052** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4120** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39245** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 130/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2241 |
| http | 1871 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 2088 |
| ID | 505 |
| ?? | 111 |
| MX | 91 |
| US | 87 |
| PH | 78 |
| CN | 70 |
| CO | 68 |
| RU | 65 |
| IN | 53 |
| BD | 49 |
| EC | 49 |
| VE | 49 |
| BR | 45 |
| VN | 41 |
| JP | 36 |
| DE | 34 |
| CA | 33 |
| PK | 31 |
| EG | 29 |
| TR | 28 |
| AR | 27 |
| SG | 26 |
| HK | 24 |
| PE | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 3 | 2026-10-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 56 | 56 | 12 | 2026-10-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 70 | 70 | 33 | 2026-10-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 74 | 74 | 31 | 2026-10-07 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 124 | 124 | 33 | 2026-10-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-10-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 194 | 194 | 49 | 2026-10-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 296 | 296 | 151 | 2026-10-07 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 440 | 440 | 210 | 2026-10-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-10-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-10-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-10-07 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1734 | 1730 | 589 | 2026-10-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-10-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2108 | 2106 | 611 | 2026-10-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2454 | 2452 | 1697 | 2026-10-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2486 | 2484 | 604 | 2026-10-07 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 45880 | 45880 | 29191 | 2026-10-07 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 51438 | 51437 | 2122 | 2026-10-07 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.3.69.222:8080 | TR | 1127 | 71 | 113/116 |
| http://190.0.246.211:4040 | CO | 659 | 36 | 103/116 |
| http://34.43.46.91:80 | US | 633 | 33 | 112/116 |
| http://190.0.246.210:4040 | CO | 547 | 32 | 104/115 |
| http://34.43.46.91:443 | US | 619 | 29 | 110/116 |
| http://149.130.173.58:9443 | CO | 434 | 27 | 27/27 |
| http://43.173.120.13:8899 | US | 607 | 27 | 27/27 |
| http://107.167.18.122:443 | US | 332 | 12 | 64/68 |
| socks5://83.147.217.103:1080 | US | 326 | 12 | 36/39 |
| http://184.75.221.82:3118 | CA | 219 | 11 | 72/81 |
| socks5://123.58.219.171:10808 | HK | 3355 | 11 | 90/116 |
| http://190.0.246.213:4040 | CO | 572 | 10 | 73/81 |
| http://144.124.251.24:10000 | NL | 698 | 10 | 42/62 |
| http://144.124.251.24:10007 | NL | 704 | 10 | 42/65 |
| http://144.124.251.24:10008 | NL | 660 | 10 | 38/47 |
| http://144.124.251.24:10082 | NL | 975 | 10 | 39/64 |
| http://144.124.251.24:10088 | NL | 572 | 10 | 37/48 |
| http://144.124.251.24:10104 | NL | 597 | 10 | 38/48 |
| http://144.124.251.24:10176 | NL | 746 | 10 | 42/64 |
| http://144.124.251.24:10185 | NL | 601 | 10 | 39/48 |
| http://144.124.251.24:10187 | NL | 964 | 10 | 38/62 |
| http://144.124.251.24:10216 | NL | 824 | 10 | 43/65 |
| http://144.124.251.24:10226 | NL | 661 | 10 | 37/47 |
| http://144.124.251.24:10230 | NL | 549 | 10 | 41/63 |
| http://144.124.251.24:10261 | NL | 946 | 10 | 38/48 |
| http://144.124.251.24:10299 | NL | 688 | 10 | 37/48 |
| http://144.124.251.24:10333 | NL | 623 | 10 | 41/65 |
| http://144.124.251.24:10337 | NL | 601 | 10 | 36/48 |
| http://144.124.251.24:10346 | NL | 607 | 10 | 39/48 |
| http://144.124.251.24:10366 | NL | 622 | 10 | 39/62 |
| http://144.124.251.24:10372 | NL | 539 | 10 | 42/60 |
| http://144.124.251.24:10412 | NL | 912 | 10 | 38/48 |
| http://144.124.251.24:10431 | NL | 695 | 10 | 44/64 |
| http://144.124.251.24:10453 | NL | 595 | 10 | 41/53 |
| http://144.124.251.24:10471 | NL | 643 | 10 | 42/63 |
| http://144.124.251.24:10551 | NL | 695 | 10 | 43/64 |
| http://144.124.251.24:10566 | NL | 559 | 10 | 39/49 |
| http://144.124.251.24:10574 | NL | 632 | 10 | 43/65 |
| http://144.124.251.24:10601 | NL | 662 | 10 | 36/63 |
| http://144.124.251.24:10605 | NL | 530 | 10 | 38/48 |
| http://144.124.251.24:10610 | NL | 635 | 10 | 38/48 |
| http://144.124.251.24:10628 | NL | 696 | 10 | 36/48 |
| http://144.124.251.24:10631 | NL | 595 | 10 | 38/48 |
| http://144.124.251.24:10658 | NL | 595 | 10 | 38/48 |
| http://144.124.251.24:10689 | NL | 697 | 10 | 39/52 |
| http://144.124.251.24:10771 | NL | 575 | 10 | 38/48 |
| http://144.124.251.24:10800 | NL | 570 | 10 | 38/48 |
| http://144.124.251.24:10801 | NL | 809 | 10 | 39/64 |
| http://144.124.251.24:10811 | NL | 1767 | 10 | 38/48 |
| http://144.124.251.24:10818 | NL | 6134 | 10 | 35/48 |
| http://144.124.251.24:10829 | NL | 606 | 10 | 36/48 |
| http://144.124.251.24:10953 | NL | 553 | 10 | 39/48 |
| http://144.124.251.24:11011 | NL | 640 | 10 | 39/48 |
| http://144.124.251.24:11108 | NL | 637 | 10 | 39/63 |
| http://144.124.251.24:11124 | NL | 595 | 10 | 40/65 |
| http://144.124.251.24:11180 | NL | 611 | 10 | 37/47 |
| http://144.124.251.24:11265 | NL | 642 | 10 | 42/64 |
| http://144.124.251.24:11266 | NL | 578 | 10 | 39/48 |
| http://144.124.251.24:11274 | NL | 688 | 10 | 42/64 |
| http://144.124.251.24:11450 | NL | 665 | 10 | 36/48 |
| http://144.124.251.24:11480 | NL | 641 | 10 | 37/48 |
| http://144.124.251.24:11491 | NL | 725 | 10 | 42/64 |
| http://44.216.27.249:3128 | US | 108 | 9 | 12/13 |
| http://102.244.78.61:8090 | CM | 1227 | 8 | 8/8 |
| http://197.224.185.3:3128 | MU | 2008 | 8 | 77/84 |
| http://4.144.146.21:80 | SG | 1146 | 8 | 8/8 |
| http://128.199.121.61:9090 | SG | 1149 | 8 | 30/36 |
| http://165.154.162.73:8888 | US | 2427 | 8 | 70/116 |
| http://187.102.219.64:999 | AR | 1457 | 7 | 30/55 |
| socks5://107.149.92.23:8443 | HK | 4157 | 7 | 11/33 |
| socks5://101.36.104.46:10808 | JP | 2085 | 7 | 102/116 |
| socks5://57.128.231.218:1202 | PL | 1214 | 7 | 9/29 |
| socks5://160.187.0.89:1080 | VN | 3390 | 7 | 22/29 |
| http://102.244.78.61:8085 | CM | 1241 | 6 | 6/6 |
| http://102.244.78.61:8087 | CM | 1238 | 6 | 6/6 |
| http://65.109.219.108:2000 | FI | 714 | 6 | 8/9 |
| http://176.111.37.5:39811 | HK | 889 | 6 | 98/116 |
| http://176.111.37.216:39811 | HK | 901 | 6 | 95/116 |
| http://167.99.74.174:9090 | SG | 1184 | 6 | 50/76 |
| http://16.18.22.211:9090 | CH | 893 | 5 | 23/76 |
| http://102.244.78.61:8080 | CM | 1188 | 5 | 5/5 |
| http://102.244.78.61:8082 | CM | 1237 | 5 | 5/5 |
| http://114.249.221.24:8888 | CN | 2141 | 5 | 17/51 |
| http://114.249.225.156:8888 | CN | 7560 | 5 | 23/38 |
| http://41.128.90.52:1976 | EG | 1035 | 5 | 10/21 |
| http://34.88.38.81:9443 | FI | 786 | 5 | 55/81 |
| http://35.228.49.168:9443 | FI | 587 | 5 | 36/53 |
| http://62.72.43.79:3129 | IN | 3510 | 5 | 5/5 |
| http://203.177.217.222:8082 | PH | 1545 | 5 | 34/61 |
| http://130.110.103.245:3128 | SA | 1110 | 5 | 108/116 |
| http://195.158.8.123:3128 | UZ | 3089 | 5 | 75/114 |
| http://16.28.101.55:2080 | ZA | 2909 | 5 | 16/56 |
| socks5://193.25.215.182:22222 | US | 1843 | 5 | 100/116 |
| http://16.18.22.211:36560 | CH | 932 | 4 | 22/66 |
| http://102.244.78.61:8083 | CM | 1193 | 4 | 4/4 |
| http://102.244.78.61:8084 | CM | 1244 | 4 | 4/4 |
| http://102.244.78.61:8086 | CM | 1186 | 4 | 4/4 |
| http://102.244.78.61:8088 | CM | 1243 | 4 | 4/4 |
| http://102.244.78.61:8089 | CM | 1244 | 4 | 4/4 |
| http://101.206.186.99:8080 | CN | 3242 | 4 | 47/116 |
