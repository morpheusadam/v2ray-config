# Proxy status

Generated 2026-11-24T23:12:58Z by `harvest.py`.

- **1638** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3840** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25958** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 118/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3354 |
| socks5 | 478 |
| socks4 | 8 |

| country | entries |
|---|---|
| ID | 948 |
| ?? | 653 |
| NL | 244 |
| PH | 143 |
| CO | 134 |
| MX | 126 |
| US | 104 |
| VE | 101 |
| BR | 99 |
| TR | 97 |
| TH | 88 |
| RU | 82 |
| IN | 78 |
| BD | 66 |
| EC | 58 |
| DO | 50 |
| AR | 48 |
| PK | 43 |
| ZA | 35 |
| CN | 32 |
| VN | 32 |
| EG | 31 |
| PE | 28 |
| DE | 25 |
| KE | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 94 | 94 | 9 | 2026-11-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 31 | 2026-11-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 62 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 162 | 162 | 22 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 260 | 260 | 58 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 396 | 396 | 272 | 2026-11-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 455 | 455 | 122 | 2026-11-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 441 | 2026-11-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 800 | 800 | 134 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1114 | 2026-11-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1576 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1883 | 1883 | 243 | 2026-11-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1930 | 1930 | 363 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2248 | 2248 | 727 | 2026-11-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2561 | 2561 | 1566 | 2026-11-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5709 | 5709 | 4491 | 2026-11-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12324 | 12324 | 2429 | 2026-11-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 771 | 82 | 192/211 |
| http://130.110.103.245:3128 | SA | 1104 | 57 | 193/211 |
| http://141.94.22.37:3128 | FR | 481 | 23 | 26/27 |
| http://45.155.226.177:3128 | HK | 439 | 20 | 25/27 |
| http://4.144.146.21:80 | SG | 1147 | 18 | 94/103 |
| socks5://193.25.215.182:22222 | US | 3342 | 17 | 176/211 |
| http://34.43.46.91:80 | US | 1012 | 16 | 204/211 |
| http://189.51.168.164:999 | MX | 3075 | 15 | 43/47 |
| http://20.98.234.24:8080 | US | 103 | 15 | 15/15 |
| socks5://69.55.49.177:38182 | US | 731 | 15 | 55/66 |
| http://103.237.102.191:11111 | DE | 684 | 14 | 198/211 |
| http://45.186.6.104:3128 | EC | 626 | 13 | 179/189 |
| http://103.133.26.50:8080 | ID | 1510 | 13 | 77/112 |
| http://103.133.26.72:8080 | ID | 1541 | 13 | 85/137 |
| http://103.133.26.73:3128 | ID | 1581 | 13 | 101/189 |
| http://147.161.246.34:80 | ?? | 3055 | 11 | 11/11 |
| http://146.190.80.158:9090 | SG | 1162 | 10 | 99/137 |
| socks5://101.36.104.46:10808 | JP | 3225 | 10 | 175/211 |
| http://187.102.219.42:999 | AR | 3546 | 9 | 119/206 |
| http://128.199.113.85:9090 | SG | 1173 | 9 | 29/42 |
| http://167.99.74.174:9090 | SG | 1148 | 9 | 116/171 |
| http://45.135.95.185:3128 | ?? | 1062 | 9 | 9/9 |
| socks5://123.58.219.171:10808 | HK | 2103 | 9 | 153/211 |
| http://190.123.83.137:999 | AR | 4025 | 8 | 41/48 |
| http://195.154.176.34:3128 | FR | 1009 | 8 | 14/16 |
| http://144.124.251.24:10007 | NL | 600 | 8 | 84/160 |
| http://144.124.251.24:10082 | NL | 856 | 8 | 82/159 |
| http://144.124.251.24:10084 | NL | 535 | 8 | 81/143 |
| http://144.124.251.24:10104 | NL | 521 | 8 | 80/143 |
| http://144.124.251.24:10216 | NL | 769 | 8 | 95/160 |
| http://144.124.251.24:10333 | NL | 788 | 8 | 89/160 |
| http://144.124.251.24:10471 | NL | 614 | 8 | 85/158 |
| http://144.124.251.24:10551 | NL | 682 | 8 | 86/159 |
| http://144.124.251.24:10566 | NL | 549 | 8 | 90/144 |
| http://144.124.251.24:10574 | NL | 794 | 8 | 90/160 |
| http://144.124.251.24:10605 | NL | 608 | 8 | 88/143 |
| http://144.124.251.24:10689 | NL | 623 | 8 | 90/147 |
| http://144.124.251.24:10801 | NL | 523 | 8 | 78/159 |
| http://144.124.251.24:10818 | NL | 491 | 8 | 74/143 |
| http://144.124.251.24:11011 | NL | 586 | 8 | 84/143 |
| http://144.124.251.24:11124 | NL | 644 | 8 | 89/160 |
| http://144.124.251.24:11180 | NL | 521 | 8 | 90/142 |
| http://144.124.251.24:11491 | NL | 641 | 8 | 83/159 |
| socks4://103.13.19.219:10808 | JP | 894 | 8 | 20/28 |
| socks5://45.194.33.12:30001 | HK | 3659 | 8 | 37/87 |
| http://144.124.251.24:10008 | NL | 611 | 7 | 87/142 |
| http://144.124.251.24:10610 | NL | 564 | 7 | 83/143 |
| http://5.75.173.39:3128 | ?? | 1908 | 7 | 7/7 |
| http://50.238.106.26:3128 | ?? | 602 | 7 | 7/7 |
| http://103.163.80.181:8085 | ?? | 1521 | 7 | 7/7 |
| socks5://171.25.158.95:1080 | SE | 2336 | 7 | 92/126 |
| socks5://47.76.227.81:6002 | ?? | 5053 | 7 | 7/7 |
| http://190.188.131.87:8080 | AR | 4199 | 6 | 36/125 |
| http://123.121.122.125:8888 | CN | 2015 | 6 | 23/34 |
| http://177.234.217.84:999 | EC | 4698 | 6 | 35/58 |
| http://41.196.16.228:1981 | EG | 990 | 6 | 8/24 |
| http://144.79.37.148:8080 | ID | 4561 | 6 | 23/64 |
| http://34.43.46.91:443 | US | 1024 | 6 | 195/211 |
| http://154.3.76.16:999 | VE | 3997 | 6 | 16/19 |
| http://154.59.56.74:999 | VE | 6569 | 6 | 118/174 |
| http://158.247.125.5:9443 | ?? | 494 | 6 | 6/6 |
| http://216.125.18.67:3128 | ?? | 1151 | 6 | 6/6 |
| socks5://49.13.22.249:10805 | DE | 1157 | 6 | 74/129 |
| http://45.187.105.196:8080 | BR | 7853 | 5 | 31/160 |
| http://103.120.76.34:8085 | ID | 5159 | 5 | 17/92 |
| http://103.130.61.61:8081 | ID | 4634 | 5 | 175/211 |
| http://103.195.65.150:8080 | ID | 4414 | 5 | 31/123 |
| http://187.251.130.143:8081 | MX | 5252 | 5 | 17/38 |
| http://144.124.251.24:10299 | NL | 564 | 5 | 80/143 |
| http://103.21.150.15:3128 | VN | 1313 | 5 | 7/23 |
| http://103.125.15.45:8181 | ?? | 3162 | 5 | 6/7 |
| http://103.187.226.52:8082 | ?? | 4575 | 5 | 5/5 |
| http://160.22.192.76:8082 | ?? | 6056 | 5 | 6/10 |
| http://193.124.33.31:2052 | ?? | 831 | 5 | 5/5 |
| socks5://103.191.218.119:69 | ID | 1770 | 5 | 55/197 |
| http://185.196.182.22:8080 | AL | 6177 | 4 | 49/190 |
| http://185.191.239.248:3128 | CH | 669 | 4 | 147/210 |
| http://177.234.217.93:999 | EC | 2775 | 4 | 49/70 |
| http://181.188.203.40:999 | EC | 6609 | 4 | 50/108 |
| http://41.196.16.228:1976 | EG | 987 | 4 | 4/4 |
| http://197.164.101.13:1981 | EG | 2652 | 4 | 71/200 |
| http://43.198.78.37:48065 | HK | 7388 | 4 | 36/167 |
| http://175.158.40.224:1616 | ID | 7969 | 4 | 31/206 |
| http://180.148.25.190:3128 | ID | 5726 | 4 | 24/69 |
| http://192.42.85.14:8080 | ID | 6198 | 4 | 23/77 |
| http://51.17.99.116:37158 | IL | 3934 | 4 | 34/97 |
| http://43.202.114.177:31192 | KR | 3281 | 4 | 44/121 |
| http://38.19.106.44:999 | MX | 1529 | 4 | 19/84 |
| http://206.135.47.108:999 | MX | 5913 | 4 | 40/79 |
| http://144.124.251.24:10226 | NL | 517 | 4 | 85/142 |
| http://144.124.251.24:10412 | NL | 509 | 4 | 79/143 |
| http://144.124.251.24:10628 | NL | 603 | 4 | 82/143 |
| http://144.124.251.24:10631 | NL | 551 | 4 | 84/143 |
| http://144.124.251.24:10771 | NL | 504 | 4 | 88/143 |
| http://144.124.251.24:10800 | NL | 535 | 4 | 85/143 |
| http://144.124.251.24:10811 | NL | 570 | 4 | 84/143 |
| http://144.124.251.24:10829 | NL | 526 | 4 | 84/143 |
| http://144.124.251.24:10953 | NL | 552 | 4 | 79/143 |
| http://144.124.251.24:11266 | NL | 602 | 4 | 90/143 |
| http://144.124.251.24:11480 | NL | 644 | 4 | 81/143 |
