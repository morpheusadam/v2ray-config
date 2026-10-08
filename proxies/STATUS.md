# Proxy status

Generated 2026-10-08T19:21:20Z by `harvest.py`.

- **1347** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3302** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39203** endpoints on record
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
| http | 1785 |
| socks5 | 1511 |
| socks4 | 6 |

| country | entries |
|---|---|
| NL | 1331 |
| ID | 470 |
| MX | 88 |
| US | 87 |
| ?? | 87 |
| PH | 81 |
| CO | 75 |
| RU | 72 |
| CN | 69 |
| BR | 50 |
| EC | 49 |
| IN | 49 |
| BD | 46 |
| VE | 41 |
| DE | 40 |
| JP | 39 |
| TR | 34 |
| VN | 31 |
| AR | 26 |
| CA | 26 |
| EG | 26 |
| PE | 24 |
| PK | 24 |
| SG | 24 |
| AU | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 3 | 2026-10-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 64 | 64 | 29 | 2026-10-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 65 | 65 | 25 | 2026-10-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 73 | 73 | 11 | 2026-10-08 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-10-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 53 | 2026-10-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 163 | 163 | 53 | 2026-10-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 177 | 177 | 22 | 2026-10-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 231 | 231 | 130 | 2026-10-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 310 | 310 | 137 | 2026-10-08 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-10-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-10-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1151 | 2026-10-08 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1724 | 1720 | 181 | 2026-10-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-10-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1928 | 1926 | 609 | 2026-10-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2126 | 2124 | 1569 | 2026-10-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2140 | 2138 | 507 | 2026-10-08 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 46550 | 46550 | 30128 | 2026-10-08 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 51991 | 51990 | 2749 | 2026-10-08 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.3.69.222:8080 | TR | 1260 | 72 | 114/117 |
| http://190.0.246.211:4040 | CO | 826 | 37 | 104/117 |
| http://34.43.46.91:80 | US | 608 | 34 | 113/117 |
| http://190.0.246.210:4040 | CO | 685 | 33 | 105/116 |
| http://34.43.46.91:443 | US | 810 | 30 | 111/117 |
| http://149.130.173.58:9443 | CO | 417 | 28 | 28/28 |
| http://43.173.120.13:8899 | US | 355 | 28 | 28/28 |
| socks5://83.147.217.103:1080 | US | 161 | 13 | 37/40 |
| socks5://107.167.18.122:443 | US | 380 | 13 | 65/69 |
| http://184.75.221.82:3118 | CA | 280 | 12 | 73/82 |
| socks5://123.58.219.171:10808 | HK | 2587 | 12 | 91/117 |
| http://190.0.246.213:4040 | CO | 976 | 11 | 74/82 |
| http://144.124.251.24:10000 | NL | 535 | 11 | 43/63 |
| http://144.124.251.24:10007 | NL | 970 | 11 | 43/66 |
| http://144.124.251.24:10008 | NL | 611 | 11 | 39/48 |
| http://144.124.251.24:10082 | NL | 720 | 11 | 40/65 |
| http://144.124.251.24:10088 | NL | 603 | 11 | 38/49 |
| http://144.124.251.24:10104 | NL | 542 | 11 | 39/49 |
| http://144.124.251.24:10176 | NL | 1160 | 11 | 43/65 |
| http://144.124.251.24:10185 | NL | 528 | 11 | 40/49 |
| http://144.124.251.24:10187 | NL | 606 | 11 | 39/63 |
| http://144.124.251.24:10216 | NL | 782 | 11 | 44/66 |
| http://144.124.251.24:10226 | NL | 1122 | 11 | 38/48 |
| http://144.124.251.24:10230 | NL | 648 | 11 | 42/64 |
| http://144.124.251.24:10261 | NL | 512 | 11 | 39/49 |
| http://144.124.251.24:10299 | NL | 646 | 11 | 38/49 |
| http://144.124.251.24:10333 | NL | 733 | 11 | 42/66 |
| http://144.124.251.24:10337 | NL | 1006 | 11 | 37/49 |
| http://144.124.251.24:10346 | NL | 609 | 11 | 40/49 |
| http://144.124.251.24:10366 | NL | 535 | 11 | 40/63 |
| http://144.124.251.24:10372 | NL | 510 | 11 | 43/61 |
| http://144.124.251.24:10412 | NL | 522 | 11 | 39/49 |
| http://144.124.251.24:10431 | NL | 687 | 11 | 45/65 |
| http://144.124.251.24:10453 | NL | 574 | 11 | 42/54 |
| http://144.124.251.24:10471 | NL | 657 | 11 | 43/64 |
| http://144.124.251.24:10551 | NL | 692 | 11 | 44/65 |
| http://144.124.251.24:10566 | NL | 580 | 11 | 40/50 |
| http://144.124.251.24:10574 | NL | 717 | 11 | 44/66 |
| http://144.124.251.24:10601 | NL | 835 | 11 | 37/64 |
| http://144.124.251.24:10605 | NL | 510 | 11 | 39/49 |
| http://144.124.251.24:10610 | NL | 522 | 11 | 39/49 |
| http://144.124.251.24:10628 | NL | 512 | 11 | 37/49 |
| http://144.124.251.24:10631 | NL | 507 | 11 | 39/49 |
| http://144.124.251.24:10658 | NL | 595 | 11 | 39/49 |
| http://144.124.251.24:10689 | NL | 510 | 11 | 40/53 |
| http://144.124.251.24:10771 | NL | 638 | 11 | 39/49 |
| http://144.124.251.24:10800 | NL | 511 | 11 | 39/49 |
| http://144.124.251.24:10801 | NL | 3253 | 11 | 40/65 |
| http://144.124.251.24:10811 | NL | 680 | 11 | 39/49 |
| http://144.124.251.24:10818 | NL | 536 | 11 | 36/49 |
| http://144.124.251.24:10829 | NL | 502 | 11 | 37/49 |
| http://144.124.251.24:10953 | NL | 502 | 11 | 40/49 |
| http://144.124.251.24:11011 | NL | 515 | 11 | 40/49 |
| http://144.124.251.24:11108 | NL | 1166 | 11 | 40/64 |
| http://144.124.251.24:11124 | NL | 716 | 11 | 41/66 |
| http://144.124.251.24:11180 | NL | 493 | 11 | 38/48 |
| http://144.124.251.24:11265 | NL | 919 | 11 | 43/65 |
| http://144.124.251.24:11266 | NL | 514 | 11 | 40/49 |
| http://144.124.251.24:11274 | NL | 690 | 11 | 43/65 |
| http://144.124.251.24:11450 | NL | 543 | 11 | 37/49 |
| http://144.124.251.24:11480 | NL | 522 | 11 | 38/49 |
| http://144.124.251.24:11491 | NL | 698 | 11 | 43/65 |
| http://44.216.27.249:3128 | US | 3025 | 10 | 13/14 |
| http://197.224.185.3:3128 | MU | 1762 | 9 | 78/85 |
| http://4.144.146.21:80 | SG | 1180 | 9 | 9/9 |
| http://128.199.121.61:9090 | SG | 1181 | 9 | 31/37 |
| http://165.154.162.73:8888 | US | 1476 | 9 | 71/117 |
| http://187.102.219.64:999 | AR | 2231 | 8 | 31/56 |
| socks5://107.149.92.23:8443 | HK | 4444 | 8 | 12/34 |
| socks5://57.128.231.218:1202 | PL | 5895 | 8 | 10/30 |
| socks5://160.187.0.89:1080 | VN | 1667 | 8 | 23/30 |
| http://102.244.78.61:8085 | CM | 1245 | 7 | 7/7 |
| http://102.244.78.61:8087 | CM | 1262 | 7 | 7/7 |
| http://65.109.219.108:2000 | FI | 4370 | 7 | 9/10 |
| http://176.111.37.5:39811 | HK | 881 | 7 | 99/117 |
| http://176.111.37.216:39811 | HK | 797 | 7 | 96/117 |
| http://167.99.74.174:9090 | SG | 1179 | 7 | 51/77 |
| http://114.249.221.24:8888 | CN | 2256 | 6 | 18/52 |
| http://34.88.38.81:9443 | FI | 864 | 6 | 56/82 |
| http://35.228.49.168:9443 | FI | 632 | 6 | 37/54 |
| http://203.177.217.222:8082 | PH | 6716 | 6 | 35/62 |
| http://130.110.103.245:3128 | SA | 1498 | 6 | 109/117 |
| http://195.158.8.123:3128 | UZ | 3045 | 6 | 76/115 |
| http://16.28.101.55:2080 | ZA | 3730 | 6 | 17/57 |
| socks5://193.25.215.182:22222 | US | 694 | 6 | 101/117 |
| http://102.244.78.61:8083 | CM | 1192 | 5 | 5/5 |
| http://102.244.78.61:8084 | CM | 1194 | 5 | 5/5 |
| http://102.244.78.61:8086 | CM | 1198 | 5 | 5/5 |
| http://102.244.78.61:8088 | CM | 1236 | 5 | 5/5 |
| http://102.244.78.61:8089 | CM | 1230 | 5 | 5/5 |
| http://120.232.115.57:17981 | CN | 1647 | 5 | 32/42 |
| http://45.186.6.104:3128 | EC | 686 | 5 | 89/95 |
| http://140.238.32.108:3128 | JP | 5978 | 5 | 59/116 |
| http://189.51.168.165:999 | MX | 342 | 5 | 27/29 |
| http://5.129.254.5:8888 | RU | 1044 | 5 | 62/72 |
| http://5.129.254.49:8888 | RU | 1026 | 5 | 63/72 |
| http://5.129.254.51:8888 | RU | 1220 | 5 | 63/72 |
| http://5.129.254.60:8888 | RU | 915 | 5 | 62/71 |
| http://5.129.254.70:8888 | RU | 1076 | 5 | 63/72 |
| http://5.129.254.129:8888 | RU | 1089 | 5 | 68/78 |
