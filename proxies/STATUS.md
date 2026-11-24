# Proxy status

Generated 2026-11-24T00:49:36Z by `harvest.py`.

- **1684** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3647** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **26100** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 152/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3132 |
| socks5 | 511 |
| socks4 | 4 |

| country | entries |
|---|---|
| ID | 939 |
| ?? | 564 |
| NL | 299 |
| PH | 138 |
| MX | 133 |
| CO | 113 |
| US | 98 |
| BR | 82 |
| TH | 82 |
| VE | 82 |
| IN | 74 |
| BD | 69 |
| RU | 69 |
| TR | 66 |
| EC | 53 |
| CN | 48 |
| PK | 48 |
| DO | 45 |
| AR | 39 |
| PE | 35 |
| ZA | 33 |
| VN | 30 |
| EG | 27 |
| SG | 26 |
| KE | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 119 | 119 | 11 | 2026-11-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 32 | 2026-11-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 61 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 221 | 221 | 38 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 228 | 228 | 40 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 416 | 416 | 291 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 523 | 523 | 129 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 766 | 766 | 112 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1115 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1576 | 2026-11-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1946 | 1946 | 186 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2322 | 2322 | 176 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2780 | 2780 | 716 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3103 | 3103 | 1841 | 2026-11-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5704 | 5704 | 4483 | 2026-11-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12559 | 12559 | 2176 | 2026-11-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 918 | 80 | 190/209 |
| http://130.110.103.245:3128 | SA | 1250 | 55 | 191/209 |
| http://141.94.22.37:3128 | FR | 687 | 21 | 24/25 |
| http://45.155.226.177:3128 | HK | 643 | 18 | 23/25 |
| http://4.144.146.21:80 | SG | 1044 | 16 | 92/101 |
| socks5://193.25.215.182:22222 | US | 756 | 15 | 174/209 |
| http://34.43.46.91:80 | US | 218 | 14 | 202/209 |
| socks5://46.246.12.31:1080 | SE | 3030 | 14 | 14/14 |
| http://189.51.168.164:999 | MX | 1898 | 13 | 41/45 |
| http://104.248.151.93:9090 | SG | 1170 | 13 | 78/110 |
| http://20.98.234.24:8080 | US | 295 | 13 | 13/13 |
| socks5://69.55.49.177:38182 | US | 594 | 13 | 53/64 |
| http://103.237.102.191:11111 | DE | 884 | 12 | 196/209 |
| http://45.186.6.104:3128 | EC | 738 | 11 | 177/187 |
| http://103.133.26.50:8080 | ID | 1364 | 11 | 75/110 |
| http://103.133.26.72:8080 | ID | 3526 | 11 | 83/135 |
| http://103.133.26.73:3128 | ID | 1439 | 11 | 99/187 |
| http://140.238.32.108:3128 | JP | 1047 | 10 | 125/208 |
| http://54.36.150.233:3128 | FR | 5669 | 9 | 22/31 |
| http://147.161.246.34:80 | ?? | 4076 | 9 | 9/9 |
| http://45.240.232.61:8080 | EG | 6739 | 8 | 83/189 |
| http://146.190.80.158:9090 | SG | 1505 | 8 | 97/135 |
| socks5://101.36.104.46:10808 | JP | 1147 | 8 | 173/209 |
| socks5://101.36.104.239:10808 | JP | 1098 | 8 | 171/209 |
| http://187.102.219.42:999 | AR | 5264 | 7 | 117/204 |
| http://177.234.217.235:999 | EC | 2634 | 7 | 97/178 |
| http://49.156.44.116:8080 | KH | 3695 | 7 | 21/43 |
| http://128.199.113.85:9090 | SG | 3236 | 7 | 27/40 |
| http://167.99.74.174:9090 | SG | 1351 | 7 | 114/169 |
| http://195.226.213.251:8888 | UA | 7614 | 7 | 84/203 |
| http://38.172.181.0:999 | VE | 1603 | 7 | 62/116 |
| http://45.135.95.185:3128 | ?? | 2485 | 7 | 7/7 |
| socks4://188.226.27.24:1080 | RU | 1380 | 7 | 34/45 |
| socks5://91.107.179.68:10809 | DE | 1176 | 7 | 76/142 |
| socks5://123.58.219.171:10808 | HK | 1499 | 7 | 151/209 |
| http://190.123.83.137:999 | AR | 4876 | 6 | 39/46 |
| http://111.192.28.24:8888 | CN | 1923 | 6 | 16/31 |
| http://114.244.221.178:8888 | CN | 1782 | 6 | 69/132 |
| http://195.154.176.34:3128 | FR | 1636 | 6 | 12/14 |
| http://198.244.254.77:3128 | GB | 2738 | 6 | 75/93 |
| http://144.124.251.24:10000 | NL | 681 | 6 | 89/155 |
| http://144.124.251.24:10007 | NL | 764 | 6 | 82/158 |
| http://144.124.251.24:10082 | NL | 782 | 6 | 80/157 |
| http://144.124.251.24:10084 | NL | 856 | 6 | 79/141 |
| http://144.124.251.24:10088 | NL | 827 | 6 | 75/141 |
| http://144.124.251.24:10104 | NL | 776 | 6 | 78/141 |
| http://144.124.251.24:10176 | NL | 792 | 6 | 91/157 |
| http://144.124.251.24:10185 | NL | 794 | 6 | 80/141 |
| http://144.124.251.24:10187 | NL | 684 | 6 | 87/155 |
| http://144.124.251.24:10216 | NL | 682 | 6 | 93/158 |
| http://144.124.251.24:10230 | NL | 835 | 6 | 86/156 |
| http://144.124.251.24:10333 | NL | 875 | 6 | 87/158 |
| http://144.124.251.24:10346 | NL | 749 | 6 | 81/141 |
| http://144.124.251.24:10366 | NL | 894 | 6 | 85/155 |
| http://144.124.251.24:10431 | NL | 707 | 6 | 84/157 |
| http://144.124.251.24:10453 | NL | 783 | 6 | 87/146 |
| http://144.124.251.24:10471 | NL | 694 | 6 | 83/156 |
| http://144.124.251.24:10485 | NL | 791 | 6 | 63/141 |
| http://144.124.251.24:10551 | NL | 675 | 6 | 84/157 |
| http://144.124.251.24:10566 | NL | 882 | 6 | 88/142 |
| http://144.124.251.24:10574 | NL | 921 | 6 | 88/158 |
| http://144.124.251.24:10601 | NL | 858 | 6 | 83/156 |
| http://144.124.251.24:10605 | NL | 782 | 6 | 86/141 |
| http://144.124.251.24:10689 | NL | 790 | 6 | 88/145 |
| http://144.124.251.24:10801 | NL | 718 | 6 | 76/157 |
| http://144.124.251.24:10818 | NL | 663 | 6 | 72/141 |
| http://144.124.251.24:11011 | NL | 909 | 6 | 82/141 |
| http://144.124.251.24:11108 | NL | 846 | 6 | 81/156 |
| http://144.124.251.24:11124 | NL | 772 | 6 | 87/158 |
| http://144.124.251.24:11180 | NL | 711 | 6 | 88/140 |
| http://144.124.251.24:11265 | NL | 844 | 6 | 88/157 |
| http://144.124.251.24:11274 | NL | 833 | 6 | 79/157 |
| http://144.124.251.24:11450 | NL | 818 | 6 | 75/141 |
| http://144.124.251.24:11491 | NL | 802 | 6 | 81/157 |
| http://200.59.191.27:999 | VE | 3332 | 6 | 141/204 |
| http://150.228.10.232:8080 | YE | 4566 | 6 | 7/11 |
| http://217.154.195.87:8888 | ?? | 7824 | 6 | 8/9 |
| socks5://45.194.33.12:30001 | HK | 4735 | 6 | 35/85 |
| socks5://103.13.19.219:10808 | JP | 2713 | 6 | 18/26 |
| socks5://121.169.46.116:1090 | KR | 1309 | 6 | 139/209 |
| socks5://88.84.204.217:1080 | RU | 3249 | 6 | 19/92 |
| socks5://79.98.32.107:1080 | TR | 6153 | 6 | 8/13 |
| http://45.65.137.218:999 | CO | 5708 | 5 | 87/174 |
| http://200.10.31.42:8081 | CO | 1152 | 5 | 40/82 |
| http://103.183.8.135:8080 | ID | 5423 | 5 | 39/197 |
| http://144.124.251.24:10008 | NL | 798 | 5 | 85/140 |
| http://144.124.251.24:10610 | NL | 783 | 5 | 81/141 |
| http://195.158.8.123:3128 | UZ | 2549 | 5 | 134/207 |
| http://5.75.173.39:3128 | ?? | 778 | 5 | 5/5 |
| http://41.57.136.174:8080 | ?? | 7014 | 5 | 5/5 |
| http://50.238.106.26:3128 | ?? | 259 | 5 | 5/5 |
| http://103.163.80.181:8085 | ?? | 1387 | 5 | 5/5 |
| http://114.246.201.118:8888 | ?? | 1784 | 5 | 5/5 |
| http://114.249.215.249:8888 | ?? | 6705 | 5 | 5/5 |
| socks5://65.21.252.66:10805 | FI | 6557 | 5 | 63/123 |
| socks5://171.25.158.95:1080 | SE | 2799 | 5 | 90/124 |
| socks5://193.218.118.128:1080 | UA | 4835 | 5 | 47/65 |
| socks5://47.76.227.81:6002 | ?? | 2869 | 5 | 5/5 |
| http://190.188.131.87:8080 | AR | 7410 | 4 | 34/123 |
| http://16.174.124.173:425 | CA | 2276 | 4 | 48/177 |
