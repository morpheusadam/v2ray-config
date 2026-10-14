# Proxy status

Generated 2026-10-14T22:36:14Z by `harvest.py`.

- **1895** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4217** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39656** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 149/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2461 |
| socks5 | 1748 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 1495 |
| ID | 718 |
| PH | 135 |
| MX | 133 |
| CO | 120 |
| US | 113 |
| RU | 107 |
| ?? | 84 |
| CN | 79 |
| BD | 71 |
| BR | 70 |
| VE | 70 |
| TR | 66 |
| IN | 64 |
| EC | 60 |
| VN | 60 |
| SG | 46 |
| DO | 45 |
| DE | 34 |
| AR | 32 |
| EG | 31 |
| JP | 30 |
| PE | 29 |
| TH | 29 |
| ZA | 28 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-10-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 102 | 102 | 49 | 2026-10-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 125 | 125 | 43 | 2026-10-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 132 | 132 | 29 | 2026-10-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 70 | 2026-10-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 294 | 294 | 93 | 2026-10-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 295 | 295 | 105 | 2026-10-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-10-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 644 | 644 | 414 | 2026-10-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 938 | 938 | 314 | 2026-10-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1139 | 2026-10-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1792 | 1788 | 180 | 2026-10-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-10-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2416 | 2414 | 697 | 2026-10-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2793 | 2791 | 1897 | 2026-10-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3150 | 3148 | 1103 | 2026-10-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 58812 | 58812 | 43923 | 2026-10-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 65620 | 65619 | 2352 | 2026-10-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 3733 | 50 | 117/130 |
| http://149.130.173.58:9443 | CO | 418 | 41 | 41/41 |
| http://190.0.246.213:4040 | CO | 491 | 24 | 87/95 |
| http://144.124.251.24:10366 | NL | 464 | 24 | 53/76 |
| http://197.224.185.3:3128 | MU | 1051 | 22 | 91/98 |
| http://103.237.102.191:11111 | DE | 822 | 17 | 123/130 |
| http://186.5.94.206:999 | EC | 788 | 15 | 85/92 |
| http://203.252.142.217:80 | KR | 963 | 12 | 12/12 |
| http://146.190.80.158:9090 | SG | 1260 | 12 | 40/56 |
| http://45.186.6.104:3128 | EC | 632 | 11 | 101/108 |
| http://144.124.251.24:10605 | NL | 493 | 11 | 51/62 |
| socks5://101.36.104.46:10808 | JP | 2427 | 11 | 114/130 |
| http://144.124.251.24:10000 | NL | 546 | 10 | 54/76 |
| http://3.211.120.181:443 | US | 86 | 10 | 24/41 |
| http://165.154.162.73:8888 | US | 5051 | 10 | 83/130 |
| http://102.244.78.61:8083 | CM | 1159 | 9 | 15/18 |
| http://103.130.61.61:8081 | ID | 4725 | 9 | 101/130 |
| http://144.124.251.24:10261 | NL | 491 | 9 | 51/62 |
| http://144.124.251.24:10628 | NL | 493 | 9 | 49/62 |
| http://144.124.251.24:10771 | NL | 467 | 9 | 51/62 |
| http://144.124.251.24:11180 | NL | 547 | 9 | 50/61 |
| http://101.206.186.99:8080 | CN | 4926 | 8 | 56/130 |
| http://144.124.251.24:10811 | NL | 479 | 8 | 50/62 |
| http://34.196.85.244:3128 | US | 64 | 8 | 8/8 |
| http://102.244.78.61:8080 | CM | 1157 | 7 | 15/19 |
| http://102.244.78.61:8088 | CM | 1190 | 7 | 14/18 |
| http://144.124.251.24:10187 | NL | 469 | 7 | 50/76 |
| http://144.124.251.24:10412 | NL | 483 | 7 | 49/62 |
| http://144.124.251.24:11265 | NL | 475 | 7 | 55/78 |
| http://5.129.254.5:8888 | RU | 2039 | 7 | 74/85 |
| http://5.129.254.49:8888 | RU | 1109 | 7 | 75/85 |
| http://5.129.254.51:8888 | RU | 1047 | 7 | 75/85 |
| http://5.129.254.60:8888 | RU | 991 | 7 | 74/84 |
| http://5.129.254.70:8888 | RU | 2021 | 7 | 75/85 |
| http://5.129.254.129:8888 | RU | 3357 | 7 | 80/91 |
| http://5.129.254.154:8888 | RU | 993 | 7 | 71/81 |
| http://5.129.254.215:8888 | RU | 1053 | 7 | 24/27 |
| http://5.129.254.243:8888 | RU | 1017 | 7 | 24/26 |
| socks5://116.101.14.169:1089 | VN | 7005 | 7 | 7/7 |
| http://41.65.55.27:1981 | EG | 4465 | 6 | 25/70 |
| http://34.88.38.81:9443 | FI | 739 | 6 | 65/95 |
| http://35.228.49.168:9443 | FI | 587 | 6 | 46/67 |
| http://103.133.26.50:8080 | ID | 1559 | 6 | 10/31 |
| http://103.133.26.72:8080 | ID | 2454 | 6 | 11/56 |
| http://103.133.26.73:3128 | ID | 1616 | 6 | 26/108 |
| http://103.133.26.119:8080 | ID | 2016 | 6 | 10/40 |
| http://144.124.251.24:10084 | NL | 708 | 6 | 49/62 |
| http://144.124.251.24:10176 | NL | 642 | 6 | 54/78 |
| http://144.124.251.24:10185 | NL | 465 | 6 | 51/62 |
| http://144.124.251.24:10299 | NL | 461 | 6 | 49/62 |
| http://144.124.251.24:10566 | NL | 574 | 6 | 50/63 |
| http://144.124.251.24:11491 | NL | 481 | 6 | 54/78 |
| socks5://67.207.92.87:1088 | US | 245 | 6 | 74/129 |
| socks5://193.25.215.182:22222 | US | 786 | 6 | 109/130 |
| http://185.222.94.66:808 | AZ | 3183 | 5 | 9/27 |
| http://184.75.221.82:3118 | CA | 1646 | 5 | 83/95 |
| http://177.234.217.88:999 | EC | 4066 | 5 | 47/122 |
| http://45.198.11.164:9191 | ID | 6649 | 5 | 9/24 |
| http://122.176.158.103:80 | IN | 4410 | 5 | 8/16 |
| http://49.156.44.115:8080 | KH | 2884 | 5 | 28/96 |
| http://187.251.224.167:8081 | MX | 4797 | 5 | 20/90 |
| http://144.124.251.24:10008 | NL | 466 | 5 | 50/61 |
| http://144.124.251.24:10104 | NL | 489 | 5 | 47/62 |
| http://144.124.251.24:10346 | NL | 633 | 5 | 49/62 |
| http://144.124.251.24:10453 | NL | 468 | 5 | 51/67 |
| http://144.124.251.24:10610 | NL | 732 | 5 | 47/62 |
| http://144.124.251.24:10658 | NL | 475 | 5 | 47/62 |
| http://144.124.251.24:10818 | NL | 500 | 5 | 45/62 |
| http://144.124.251.24:10953 | NL | 491 | 5 | 49/62 |
| http://144.124.251.24:11108 | NL | 474 | 5 | 52/77 |
| http://144.124.251.24:11450 | NL | 560 | 5 | 46/62 |
| http://144.124.251.24:11480 | NL | 1163 | 5 | 48/62 |
| http://134.185.85.16:3128 | SG | 1192 | 5 | 5/5 |
| http://108.61.29.163:10001 | US | 1348 | 5 | 16/24 |
| http://187.102.219.34:999 | AR | 1136 | 4 | 43/81 |
| http://187.102.219.42:999 | AR | 1071 | 4 | 68/125 |
| http://18.228.228.159:3822 | BR | 1835 | 4 | 13/40 |
| http://40.177.104.199:38213 | CA | 2420 | 4 | 14/52 |
| http://120.232.115.170:17981 | CN | 1896 | 4 | 92/129 |
| http://121.46.226.221:10808 | CN | 1332 | 4 | 6/7 |
| http://223.85.21.195:8080 | CN | 5809 | 4 | 49/128 |
| http://38.75.82.222:999 | DO | 7942 | 4 | 24/74 |
| http://41.33.245.138:1976 | EG | 3243 | 4 | 13/55 |
| http://41.128.90.51:1976 | EG | 1009 | 4 | 5/6 |
| http://213.131.85.29:1976 | EG | 980 | 4 | 5/6 |
| http://103.144.54.71:8082 | ID | 5621 | 4 | 23/66 |
| http://103.166.8.238:3125 | ID | 1635 | 4 | 12/41 |
| http://78.14.19.3:3128 | MX | 2501 | 4 | 22/90 |
| http://43.216.197.62:26130 | MY | 5576 | 4 | 27/98 |
| http://144.124.251.24:10088 | NL | 498 | 4 | 47/62 |
| http://144.124.251.24:10226 | NL | 742 | 4 | 47/61 |
| http://144.124.251.24:10333 | NL | 737 | 4 | 52/79 |
| http://144.124.251.24:10372 | NL | 731 | 4 | 53/74 |
| http://144.124.251.24:10431 | NL | 493 | 4 | 55/78 |
| http://144.124.251.24:10574 | NL | 484 | 4 | 55/79 |
| http://144.124.251.24:10631 | NL | 574 | 4 | 49/62 |
| http://144.124.251.24:10689 | NL | 463 | 4 | 52/66 |
| http://144.124.251.24:10829 | NL | 476 | 4 | 49/62 |
| http://144.124.251.24:11011 | NL | 495 | 4 | 48/62 |
| http://144.124.251.24:11124 | NL | 506 | 4 | 52/79 |
