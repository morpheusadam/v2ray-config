# Proxy status

Generated 2026-11-24T04:25:42Z by `harvest.py`.

- **2024** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3961** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25783** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 191/600 (32%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3416 |
| socks5 | 541 |
| socks4 | 4 |

| country | entries |
|---|---|
| ID | 959 |
| ?? | 737 |
| NL | 306 |
| PH | 143 |
| CO | 136 |
| MX | 124 |
| US | 102 |
| TH | 95 |
| VE | 94 |
| BR | 92 |
| TR | 86 |
| IN | 71 |
| RU | 70 |
| BD | 62 |
| EC | 57 |
| DO | 49 |
| PK | 49 |
| AR | 46 |
| CN | 43 |
| PE | 36 |
| VN | 33 |
| EG | 30 |
| ZA | 29 |
| SG | 24 |
| SY | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 105 | 105 | 18 | 2026-11-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 27 | 2026-11-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 51 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 206 | 206 | 25 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 282 | 282 | 77 | 2026-11-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 424 | 424 | 108 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 435 | 435 | 303 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1004 | 1004 | 160 | 2026-11-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1563 | 1563 | 160 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1114 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1577 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2322 | 2322 | 173 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2780 | 2780 | 716 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3103 | 3103 | 1792 | 2026-11-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5704 | 5704 | 4482 | 2026-11-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12559 | 12559 | 2175 | 2026-11-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 754 | 81 | 191/210 |
| http://130.110.103.245:3128 | SA | 1196 | 56 | 192/210 |
| http://141.94.22.37:3128 | FR | 486 | 22 | 25/26 |
| http://45.155.226.177:3128 | HK | 446 | 19 | 24/26 |
| http://4.144.146.21:80 | SG | 1170 | 17 | 93/102 |
| socks5://193.25.215.182:22222 | US | 734 | 16 | 175/210 |
| http://34.43.46.91:80 | US | 276 | 15 | 203/210 |
| http://189.51.168.164:999 | MX | 1984 | 14 | 42/46 |
| http://104.248.151.93:9090 | SG | 1268 | 14 | 79/111 |
| http://20.98.234.24:8080 | US | 84 | 14 | 14/14 |
| socks5://69.55.49.177:38182 | US | 405 | 14 | 54/65 |
| http://103.237.102.191:11111 | DE | 622 | 13 | 197/210 |
| http://45.186.6.104:3128 | EC | 604 | 12 | 178/188 |
| http://103.133.26.50:8080 | ID | 1555 | 12 | 76/111 |
| http://103.133.26.72:8080 | ID | 1796 | 12 | 84/136 |
| http://103.133.26.73:3128 | ID | 1579 | 12 | 100/188 |
| http://140.238.32.108:3128 | JP | 972 | 11 | 126/209 |
| http://54.36.150.233:3128 | FR | 512 | 10 | 23/32 |
| http://147.161.246.34:80 | ?? | 3992 | 10 | 10/10 |
| http://45.240.232.61:8080 | EG | 5350 | 9 | 84/190 |
| http://146.190.80.158:9090 | SG | 1182 | 9 | 98/136 |
| socks5://101.36.104.46:10808 | JP | 1044 | 9 | 174/210 |
| socks5://101.36.104.239:10808 | JP | 1333 | 9 | 172/210 |
| http://187.102.219.42:999 | AR | 3652 | 8 | 118/205 |
| http://128.199.113.85:9090 | SG | 1177 | 8 | 28/41 |
| http://167.99.74.174:9090 | SG | 1176 | 8 | 115/170 |
| http://45.135.95.185:3128 | ?? | 1359 | 8 | 8/8 |
| socks4://188.226.27.24:1080 | RU | 1445 | 8 | 35/46 |
| socks5://91.107.179.68:10809 | DE | 1159 | 8 | 77/143 |
| socks5://123.58.219.171:10808 | HK | 1521 | 8 | 152/210 |
| http://190.123.83.137:999 | AR | 6762 | 7 | 40/47 |
| http://195.154.176.34:3128 | FR | 745 | 7 | 13/15 |
| http://198.244.254.77:3128 | GB | 489 | 7 | 76/94 |
| http://144.124.251.24:10000 | NL | 643 | 7 | 90/156 |
| http://144.124.251.24:10007 | NL | 689 | 7 | 83/159 |
| http://144.124.251.24:10082 | NL | 620 | 7 | 81/158 |
| http://144.124.251.24:10084 | NL | 585 | 7 | 80/142 |
| http://144.124.251.24:10104 | NL | 743 | 7 | 79/142 |
| http://144.124.251.24:10176 | NL | 640 | 7 | 92/158 |
| http://144.124.251.24:10187 | NL | 744 | 7 | 88/156 |
| http://144.124.251.24:10216 | NL | 646 | 7 | 94/159 |
| http://144.124.251.24:10333 | NL | 548 | 7 | 88/159 |
| http://144.124.251.24:10471 | NL | 547 | 7 | 84/157 |
| http://144.124.251.24:10551 | NL | 669 | 7 | 85/158 |
| http://144.124.251.24:10566 | NL | 588 | 7 | 89/143 |
| http://144.124.251.24:10574 | NL | 637 | 7 | 89/159 |
| http://144.124.251.24:10605 | NL | 561 | 7 | 87/142 |
| http://144.124.251.24:10689 | NL | 718 | 7 | 89/146 |
| http://144.124.251.24:10801 | NL | 649 | 7 | 77/158 |
| http://144.124.251.24:10818 | NL | 681 | 7 | 73/142 |
| http://144.124.251.24:11011 | NL | 582 | 7 | 83/142 |
| http://144.124.251.24:11124 | NL | 700 | 7 | 88/159 |
| http://144.124.251.24:11180 | NL | 641 | 7 | 89/141 |
| http://144.124.251.24:11450 | NL | 565 | 7 | 76/142 |
| http://144.124.251.24:11491 | NL | 671 | 7 | 82/158 |
| http://200.59.191.27:999 | VE | 6909 | 7 | 142/205 |
| http://217.154.195.87:8888 | ?? | 2566 | 7 | 9/10 |
| socks5://45.194.33.12:30001 | HK | 3039 | 7 | 36/86 |
| socks5://103.13.19.219:10808 | JP | 3054 | 7 | 19/27 |
| socks5://121.169.46.116:1090 | KR | 1386 | 7 | 140/210 |
| http://103.183.8.135:8080 | ID | 7972 | 6 | 40/198 |
| http://144.124.251.24:10008 | NL | 664 | 6 | 86/141 |
| http://144.124.251.24:10610 | NL | 653 | 6 | 82/142 |
| http://195.158.8.123:3128 | UZ | 5355 | 6 | 135/208 |
| http://5.75.173.39:3128 | ?? | 621 | 6 | 6/6 |
| http://50.238.106.26:3128 | ?? | 188 | 6 | 6/6 |
| http://103.163.80.181:8085 | ?? | 1546 | 6 | 6/6 |
| socks5://65.21.252.66:10805 | FI | 7980 | 6 | 64/124 |
| socks5://171.25.158.95:1080 | SE | 3425 | 6 | 91/125 |
| socks5://193.218.118.128:1080 | UA | 1956 | 6 | 48/66 |
| socks5://47.76.227.81:6002 | ?? | 1406 | 6 | 6/6 |
| http://190.188.131.87:8080 | AR | 2470 | 5 | 35/124 |
| http://16.174.124.173:425 | CA | 1180 | 5 | 49/178 |
| http://123.121.122.125:8888 | CN | 2640 | 5 | 22/33 |
| http://177.234.217.84:999 | EC | 6586 | 5 | 34/57 |
| http://41.196.16.228:1981 | EG | 948 | 5 | 7/23 |
| http://43.155.62.157:443 | HK | 2222 | 5 | 95/113 |
| http://144.79.37.148:8080 | ID | 3087 | 5 | 22/63 |
| http://160.187.221.150:8082 | PH | 3667 | 5 | 18/44 |
| http://167.172.76.176:9090 | SG | 1177 | 5 | 126/171 |
| http://34.43.46.91:443 | US | 292 | 5 | 194/210 |
| http://154.3.76.16:999 | VE | 2536 | 5 | 15/18 |
| http://154.59.56.74:999 | VE | 1474 | 5 | 117/173 |
| http://158.247.125.5:9443 | ?? | 424 | 5 | 5/5 |
| http://186.233.119.183:3128 | ?? | 4943 | 5 | 8/9 |
| http://216.125.18.67:3128 | ?? | 1622 | 5 | 5/5 |
| socks5://49.13.22.249:10805 | DE | 845 | 5 | 73/128 |
| socks5://216.234.216.39:1080 | ?? | 7082 | 5 | 5/5 |
| http://182.160.110.154:9898 | BD | 4483 | 4 | 18/85 |
| http://45.187.105.196:8080 | BR | 3986 | 4 | 30/159 |
| http://177.234.217.92:999 | EC | 4166 | 4 | 40/59 |
| http://43.99.60.244:8089 | HK | 1061 | 4 | 86/160 |
| http://31.58.57.74:1111 | ID | 6426 | 4 | 47/168 |
| http://103.120.76.34:8085 | ID | 2413 | 4 | 16/91 |
| http://103.130.61.61:8081 | ID | 3769 | 4 | 174/210 |
| http://103.195.65.150:8080 | ID | 2985 | 4 | 30/122 |
| http://103.248.9.95:8080 | ID | 2283 | 4 | 26/133 |
| http://198.15.30.138:8080 | ID | 5094 | 4 | 15/54 |
| http://38.210.179.4:999 | MX | 3006 | 4 | 32/105 |
| http://187.251.130.143:8081 | MX | 1204 | 4 | 16/37 |
