# Proxy status

Generated 2026-10-08T23:56:31Z by `harvest.py`.

- **1598** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3570** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39515** endpoints on record
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
| http | 1848 |
| socks5 | 1713 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1516 |
| ID | 505 |
| ?? | 166 |
| MX | 86 |
| US | 85 |
| PH | 83 |
| RU | 77 |
| CO | 76 |
| CN | 57 |
| EC | 51 |
| BD | 50 |
| BR | 50 |
| IN | 45 |
| VE | 41 |
| DE | 37 |
| TR | 37 |
| JP | 34 |
| VN | 32 |
| DO | 29 |
| CA | 28 |
| SG | 27 |
| AR | 25 |
| PE | 22 |
| PK | 22 |
| ZA | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 2 | 2 | 1 | 2026-10-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 67 | 67 | 34 | 2026-10-08 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-10-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 113 | 113 | 45 | 2026-10-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 120 | 120 | 34 | 2026-10-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 59 | 2026-10-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 236 | 236 | 65 | 2026-10-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 294 | 294 | 172 | 2026-10-08 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 544 | 544 | 299 | 2026-10-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-10-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 456 | 2026-10-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 792 | 792 | 92 | 2026-10-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1153 | 2026-10-08 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1736 | 1732 | 451 | 2026-10-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-10-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1928 | 1926 | 607 | 2026-10-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2126 | 2124 | 1557 | 2026-10-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2140 | 2138 | 496 | 2026-10-08 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 46595 | 46595 | 30607 | 2026-10-08 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 52636 | 52635 | 2360 | 2026-10-08 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.3.69.222:8080 | TR | 1505 | 73 | 115/118 |
| http://190.0.246.211:4040 | CO | 668 | 38 | 105/118 |
| http://34.43.46.91:80 | US | 625 | 35 | 114/118 |
| http://190.0.246.210:4040 | CO | 596 | 34 | 106/117 |
| http://34.43.46.91:443 | US | 614 | 31 | 112/118 |
| http://149.130.173.58:9443 | CO | 468 | 29 | 29/29 |
| http://43.173.120.13:8899 | US | 223 | 29 | 29/29 |
| socks5://83.147.217.103:1080 | US | 349 | 14 | 38/41 |
| socks5://107.167.18.122:443 | US | 273 | 14 | 66/70 |
| http://190.0.246.213:4040 | CO | 515 | 12 | 75/83 |
| http://144.124.251.24:10000 | NL | 829 | 12 | 44/64 |
| http://144.124.251.24:10007 | NL | 992 | 12 | 44/67 |
| http://144.124.251.24:10008 | NL | 749 | 12 | 40/49 |
| http://144.124.251.24:10082 | NL | 738 | 12 | 41/66 |
| http://144.124.251.24:10088 | NL | 687 | 12 | 39/50 |
| http://144.124.251.24:10104 | NL | 731 | 12 | 40/50 |
| http://144.124.251.24:10176 | NL | 942 | 12 | 44/66 |
| http://144.124.251.24:10185 | NL | 735 | 12 | 41/50 |
| http://144.124.251.24:10187 | NL | 962 | 12 | 40/64 |
| http://144.124.251.24:10216 | NL | 732 | 12 | 45/67 |
| http://144.124.251.24:10226 | NL | 662 | 12 | 39/49 |
| http://144.124.251.24:10230 | NL | 822 | 12 | 43/65 |
| http://144.124.251.24:10261 | NL | 686 | 12 | 40/50 |
| http://144.124.251.24:10299 | NL | 756 | 12 | 39/50 |
| http://144.124.251.24:10333 | NL | 733 | 12 | 43/67 |
| http://144.124.251.24:10337 | NL | 853 | 12 | 38/50 |
| http://144.124.251.24:10346 | NL | 773 | 12 | 41/50 |
| http://144.124.251.24:10366 | NL | 773 | 12 | 41/64 |
| http://144.124.251.24:10372 | NL | 771 | 12 | 44/62 |
| http://144.124.251.24:10412 | NL | 4803 | 12 | 40/50 |
| http://144.124.251.24:10431 | NL | 756 | 12 | 46/66 |
| http://144.124.251.24:10453 | NL | 1828 | 12 | 43/55 |
| http://144.124.251.24:10471 | NL | 785 | 12 | 44/65 |
| http://144.124.251.24:10551 | NL | 990 | 12 | 45/66 |
| http://144.124.251.24:10566 | NL | 676 | 12 | 41/51 |
| http://144.124.251.24:10574 | NL | 786 | 12 | 45/67 |
| http://144.124.251.24:10601 | NL | 699 | 12 | 38/65 |
| http://144.124.251.24:10605 | NL | 657 | 12 | 40/50 |
| http://144.124.251.24:10610 | NL | 731 | 12 | 40/50 |
| http://144.124.251.24:10628 | NL | 913 | 12 | 38/50 |
| http://144.124.251.24:10631 | NL | 742 | 12 | 40/50 |
| http://144.124.251.24:10658 | NL | 862 | 12 | 40/50 |
| http://144.124.251.24:10689 | NL | 739 | 12 | 41/54 |
| http://144.124.251.24:10771 | NL | 720 | 12 | 40/50 |
| http://144.124.251.24:10800 | NL | 714 | 12 | 40/50 |
| http://144.124.251.24:10801 | NL | 4853 | 12 | 41/66 |
| http://144.124.251.24:10811 | NL | 701 | 12 | 40/50 |
| http://144.124.251.24:10818 | NL | 762 | 12 | 37/50 |
| http://144.124.251.24:10829 | NL | 725 | 12 | 38/50 |
| http://144.124.251.24:10953 | NL | 667 | 12 | 41/50 |
| http://144.124.251.24:11011 | NL | 776 | 12 | 41/50 |
| http://144.124.251.24:11108 | NL | 1029 | 12 | 41/65 |
| http://144.124.251.24:11124 | NL | 740 | 12 | 42/67 |
| http://144.124.251.24:11180 | NL | 943 | 12 | 39/49 |
| http://144.124.251.24:11265 | NL | 673 | 12 | 44/66 |
| http://144.124.251.24:11266 | NL | 672 | 12 | 41/50 |
| http://144.124.251.24:11274 | NL | 669 | 12 | 44/66 |
| http://144.124.251.24:11450 | NL | 666 | 12 | 38/50 |
| http://144.124.251.24:11480 | NL | 853 | 12 | 39/50 |
| http://144.124.251.24:11491 | NL | 752 | 12 | 44/66 |
| http://44.216.27.249:3128 | US | 3188 | 11 | 14/15 |
| http://197.224.185.3:3128 | MU | 1997 | 10 | 79/86 |
| http://4.144.146.21:80 | SG | 1052 | 10 | 10/10 |
| http://128.199.121.61:9090 | SG | 1032 | 10 | 32/38 |
| http://165.154.162.73:8888 | US | 659 | 10 | 72/118 |
| socks5://160.187.0.89:1080 | VN | 1571 | 9 | 24/31 |
| http://176.111.37.5:39811 | HK | 1238 | 8 | 100/118 |
| http://176.111.37.216:39811 | HK | 1272 | 8 | 97/118 |
| http://167.99.74.174:9090 | SG | 1081 | 8 | 52/78 |
| http://34.88.38.81:9443 | FI | 762 | 7 | 57/83 |
| http://35.228.49.168:9443 | FI | 750 | 7 | 38/55 |
| http://130.110.103.245:3128 | SA | 2505 | 7 | 110/118 |
| http://195.158.8.123:3128 | UZ | 2973 | 7 | 77/116 |
| http://120.232.115.57:17981 | CN | 1415 | 6 | 33/43 |
| http://45.186.6.104:3128 | EC | 647 | 6 | 90/96 |
| http://189.51.168.165:999 | MX | 380 | 6 | 28/30 |
| http://5.129.254.5:8888 | RU | 1114 | 6 | 63/73 |
| http://5.129.254.49:8888 | RU | 1160 | 6 | 64/73 |
| http://5.129.254.51:8888 | RU | 1152 | 6 | 64/73 |
| http://5.129.254.60:8888 | RU | 1155 | 6 | 63/72 |
| http://5.129.254.70:8888 | RU | 1156 | 6 | 64/73 |
| http://5.129.254.129:8888 | RU | 1181 | 6 | 69/79 |
| http://5.129.254.154:8888 | RU | 1207 | 6 | 60/69 |
| http://5.129.254.215:8888 | RU | 4761 | 6 | 13/15 |
| http://5.129.254.243:8888 | RU | 3789 | 6 | 13/14 |
| http://49.229.100.235:8080 | TH | 1420 | 6 | 38/66 |
| http://114.244.214.18:8888 | CN | 6944 | 5 | 21/41 |
| http://103.237.102.191:11111 | DE | 1235 | 5 | 111/118 |
| http://43.99.60.244:8089 | HK | 6769 | 5 | 38/68 |
| http://43.155.62.157:443 | HK | 7449 | 5 | 18/21 |
| http://128.199.116.219:9090 | SG | 1029 | 5 | 30/37 |
| http://61.91.162.126:8080 | TH | 1738 | 5 | 47/61 |
| http://103.10.231.189:8080 | TH | 1653 | 5 | 72/103 |
| http://38.51.207.116:999 | VE | 5317 | 5 | 26/116 |
| socks5://101.36.104.239:10808 | JP | 1426 | 5 | 100/118 |
| http://35.183.127.162:22308 | CA | 5120 | 4 | 8/20 |
| http://185.191.239.248:3128 | CH | 1834 | 4 | 86/117 |
| http://102.244.78.61:8081 | CM | 1311 | 4 | 4/4 |
| http://85.239.156.66:5555 | CZ | 883 | 4 | 5/7 |
| http://144.124.251.24:10084 | NL | 987 | 4 | 38/50 |
