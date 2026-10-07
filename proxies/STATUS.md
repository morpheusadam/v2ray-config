# Proxy status

Generated 2026-10-07T19:29:06Z by `harvest.py`.

- **1396** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3494** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39573** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 91/600 (15%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1775 |
| http | 1710 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1646 |
| ID | 463 |
| US | 98 |
| MX | 78 |
| CN | 73 |
| CO | 68 |
| PH | 62 |
| RU | 53 |
| ?? | 52 |
| IN | 50 |
| BR | 48 |
| EC | 48 |
| BD | 46 |
| VE | 43 |
| VN | 41 |
| DE | 38 |
| JP | 38 |
| PK | 34 |
| CA | 32 |
| SG | 31 |
| AR | 29 |
| EG | 29 |
| HK | 24 |
| DO | 22 |
| TR | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 3 | 2026-10-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 45 | 45 | 2 | 2026-10-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 51 | 51 | 27 | 2026-10-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 95 | 95 | 26 | 2026-10-07 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 100 | 100 | 21 | 2026-10-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 103 | 103 | 44 | 2026-10-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 87 | 2026-10-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 260 | 260 | 118 | 2026-10-07 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 449 | 449 | 182 | 2026-10-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-07 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1213 | 1209 | 63 | 2026-10-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1137 | 2026-10-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1595 | 2026-10-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2108 | 2106 | 611 | 2026-10-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2454 | 2452 | 1716 | 2026-10-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2486 | 2484 | 635 | 2026-10-07 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 45733 | 45733 | 28965 | 2026-10-07 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 52320 | 52319 | 3142 | 2026-10-07 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.3.69.222:8080 | TR | 1364 | 70 | 112/115 |
| http://190.0.246.211:4040 | CO | 754 | 35 | 102/115 |
| http://34.43.46.91:80 | US | 576 | 32 | 111/115 |
| http://190.0.246.210:4040 | CO | 709 | 31 | 103/114 |
| http://34.43.46.91:443 | US | 572 | 28 | 109/115 |
| http://149.130.173.58:9443 | CO | 468 | 26 | 26/26 |
| http://43.173.120.13:8899 | US | 239 | 26 | 26/26 |
| socks5://171.25.158.95:1080 | SE | 6382 | 13 | 25/30 |
| socks4://107.167.18.122:443 | US | 307 | 11 | 63/67 |
| socks5://83.147.217.103:1080 | US | 5559 | 11 | 35/38 |
| http://184.75.221.82:3118 | CA | 236 | 10 | 71/80 |
| http://123.121.123.115:8888 | CN | 2187 | 10 | 24/39 |
| socks5://123.58.219.171:10808 | HK | 1936 | 10 | 89/115 |
| http://119.188.131.55:17981 | CN | 1752 | 9 | 57/115 |
| http://190.0.246.213:4040 | CO | 579 | 9 | 72/80 |
| http://45.245.208.181:8080 | EG | 5032 | 9 | 11/19 |
| http://144.124.251.24:10000 | NL | 636 | 9 | 41/61 |
| http://144.124.251.24:10007 | NL | 1140 | 9 | 41/64 |
| http://144.124.251.24:10008 | NL | 627 | 9 | 37/46 |
| http://144.124.251.24:10082 | NL | 854 | 9 | 38/63 |
| http://144.124.251.24:10088 | NL | 608 | 9 | 36/47 |
| http://144.124.251.24:10104 | NL | 607 | 9 | 37/47 |
| http://144.124.251.24:10176 | NL | 708 | 9 | 41/63 |
| http://144.124.251.24:10185 | NL | 728 | 9 | 38/47 |
| http://144.124.251.24:10187 | NL | 741 | 9 | 37/61 |
| http://144.124.251.24:10216 | NL | 780 | 9 | 42/64 |
| http://144.124.251.24:10226 | NL | 1385 | 9 | 36/46 |
| http://144.124.251.24:10230 | NL | 771 | 9 | 40/62 |
| http://144.124.251.24:10261 | NL | 593 | 9 | 37/47 |
| http://144.124.251.24:10299 | NL | 617 | 9 | 36/47 |
| http://144.124.251.24:10333 | NL | 626 | 9 | 40/64 |
| http://144.124.251.24:10337 | NL | 602 | 9 | 35/47 |
| http://144.124.251.24:10346 | NL | 644 | 9 | 38/47 |
| http://144.124.251.24:10366 | NL | 758 | 9 | 38/61 |
| http://144.124.251.24:10372 | NL | 635 | 9 | 41/59 |
| http://144.124.251.24:10412 | NL | 586 | 9 | 37/47 |
| http://144.124.251.24:10431 | NL | 761 | 9 | 43/63 |
| http://144.124.251.24:10453 | NL | 901 | 9 | 40/52 |
| http://144.124.251.24:10471 | NL | 870 | 9 | 41/62 |
| http://144.124.251.24:10551 | NL | 615 | 9 | 42/63 |
| http://144.124.251.24:10566 | NL | 613 | 9 | 38/48 |
| http://144.124.251.24:10574 | NL | 608 | 9 | 42/64 |
| http://144.124.251.24:10601 | NL | 794 | 9 | 35/62 |
| http://144.124.251.24:10605 | NL | 579 | 9 | 37/47 |
| http://144.124.251.24:10610 | NL | 721 | 9 | 37/47 |
| http://144.124.251.24:10628 | NL | 630 | 9 | 35/47 |
| http://144.124.251.24:10631 | NL | 580 | 9 | 37/47 |
| http://144.124.251.24:10658 | NL | 621 | 9 | 37/47 |
| http://144.124.251.24:10689 | NL | 883 | 9 | 38/51 |
| http://144.124.251.24:10771 | NL | 626 | 9 | 37/47 |
| http://144.124.251.24:10800 | NL | 620 | 9 | 37/47 |
| http://144.124.251.24:10801 | NL | 693 | 9 | 38/63 |
| http://144.124.251.24:10811 | NL | 616 | 9 | 37/47 |
| http://144.124.251.24:10818 | NL | 650 | 9 | 34/47 |
| http://144.124.251.24:10829 | NL | 801 | 9 | 35/47 |
| http://144.124.251.24:10953 | NL | 685 | 9 | 38/47 |
| http://144.124.251.24:11011 | NL | 590 | 9 | 38/47 |
| http://144.124.251.24:11108 | NL | 703 | 9 | 38/62 |
| http://144.124.251.24:11124 | NL | 721 | 9 | 39/64 |
| http://144.124.251.24:11180 | NL | 718 | 9 | 36/46 |
| http://144.124.251.24:11265 | NL | 658 | 9 | 41/63 |
| http://144.124.251.24:11266 | NL | 628 | 9 | 38/47 |
| http://144.124.251.24:11274 | NL | 704 | 9 | 41/63 |
| http://144.124.251.24:11450 | NL | 756 | 9 | 35/47 |
| http://144.124.251.24:11480 | NL | 640 | 9 | 36/47 |
| http://144.124.251.24:11491 | NL | 762 | 9 | 41/63 |
| http://44.216.27.249:3128 | US | 4983 | 8 | 11/12 |
| http://102.244.78.61:8090 | CM | 1511 | 7 | 7/7 |
| http://197.224.185.3:3128 | MU | 1912 | 7 | 76/83 |
| http://4.144.146.21:80 | SG | 1044 | 7 | 7/7 |
| http://128.199.121.61:9090 | SG | 1026 | 7 | 29/35 |
| http://165.154.162.73:8888 | US | 492 | 7 | 69/115 |
| http://187.102.219.64:999 | AR | 5985 | 6 | 29/54 |
| socks5://107.149.92.23:8443 | HK | 2545 | 6 | 10/32 |
| socks5://101.36.104.46:10808 | JP | 2174 | 6 | 101/115 |
| socks5://57.128.231.218:1202 | PL | 2893 | 6 | 8/28 |
| socks5://160.187.0.89:1080 | VN | 1541 | 6 | 21/28 |
| http://102.244.78.61:8085 | CM | 1357 | 5 | 5/5 |
| http://102.244.78.61:8087 | CM | 1361 | 5 | 5/5 |
| http://41.196.16.228:1981 | EG | 7285 | 5 | 5/5 |
| http://65.109.215.187:8090 | FI | 964 | 5 | 8/10 |
| http://65.109.219.108:2000 | FI | 944 | 5 | 7/8 |
| http://176.111.37.5:39811 | HK | 1723 | 5 | 97/115 |
| http://176.111.37.216:39811 | HK | 1378 | 5 | 94/115 |
| http://167.99.74.174:9090 | SG | 1033 | 5 | 49/75 |
| http://190.97.241.106:999 | VE | 3691 | 5 | 70/99 |
| http://123.200.8.170:10000 | BD | 5769 | 4 | 39/113 |
| http://15.229.149.81:3128 | BR | 3711 | 4 | 15/25 |
| http://16.18.22.211:9090 | CH | 1023 | 4 | 22/75 |
| http://102.244.78.61:8080 | CM | 1345 | 4 | 4/4 |
| http://102.244.78.61:8082 | CM | 1365 | 4 | 4/4 |
| http://114.249.221.24:8888 | CN | 6304 | 4 | 16/50 |
| http://114.249.225.156:8888 | CN | 3123 | 4 | 22/37 |
| http://123.119.25.143:8888 | CN | 6399 | 4 | 34/80 |
| http://123.119.176.120:8888 | CN | 6631 | 4 | 29/80 |
| http://45.71.186.212:999 | EC | 4632 | 4 | 37/102 |
| http://41.128.90.52:1976 | EG | 974 | 4 | 9/20 |
| http://45.245.208.182:8080 | EG | 3410 | 4 | 4/4 |
| http://34.88.38.81:9443 | FI | 921 | 4 | 54/80 |
| http://35.228.49.168:9443 | FI | 765 | 4 | 35/52 |
