# Proxy status

Generated 2026-10-13T20:07:39Z by `harvest.py`.

- **1934** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3420** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39546** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 196/600 (33%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2121 |
| socks5 | 1290 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1015 |
| ID | 587 |
| ?? | 175 |
| US | 105 |
| RU | 103 |
| MX | 100 |
| PH | 99 |
| CO | 91 |
| BD | 87 |
| VE | 67 |
| CN | 64 |
| IN | 58 |
| EC | 57 |
| TR | 47 |
| VN | 45 |
| BR | 44 |
| DE | 37 |
| DO | 36 |
| EG | 33 |
| SG | 33 |
| JP | 29 |
| PK | 29 |
| AR | 28 |
| CA | 26 |
| TH | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 119 | 119 | 38 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 130 | 130 | 69 | 2026-10-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 70 | 2026-10-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 391 | 391 | 143 | 2026-10-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 477 | 477 | 209 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 557 | 557 | 224 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1061 | 1061 | 810 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-10-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1792 | 1788 | 244 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1590 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2437 | 2435 | 734 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2715 | 2713 | 818 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2718 | 2716 | 1871 | 2026-10-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 55286 | 55286 | 40546 | 2026-10-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 62000 | 61999 | 2407 | 2026-10-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1144 | 47 | 114/127 |
| http://34.43.46.91:80 | US | 848 | 44 | 123/127 |
| http://190.0.246.210:4040 | CO | 964 | 43 | 115/126 |
| http://149.130.173.58:9443 | CO | 566 | 38 | 38/38 |
| http://190.0.246.213:4040 | CO | 604 | 21 | 84/92 |
| http://144.124.251.24:10366 | NL | 732 | 21 | 50/73 |
| http://197.224.185.3:3128 | MU | 2390 | 19 | 88/95 |
| http://176.111.37.5:39811 | HK | 1111 | 17 | 109/127 |
| http://189.51.168.165:999 | MX | 478 | 15 | 37/39 |
| http://103.237.102.191:11111 | DE | 987 | 14 | 120/127 |
| http://186.5.94.206:999 | EC | 1282 | 12 | 82/89 |
| socks5://36.155.23.163:10808 | CN | 6011 | 11 | 35/64 |
| http://190.12.150.244:999 | EC | 3219 | 9 | 89/123 |
| http://203.252.142.217:80 | KR | 736 | 9 | 9/9 |
| http://104.248.151.93:9090 | SG | 1030 | 9 | 25/28 |
| http://146.190.80.158:9090 | SG | 1015 | 9 | 37/53 |
| http://45.186.6.104:3128 | EC | 726 | 8 | 98/105 |
| http://144.124.251.24:10605 | NL | 797 | 8 | 48/59 |
| socks5://101.36.104.46:10808 | JP | 1291 | 8 | 111/127 |
| socks5://195.13.182.212:8080 | LV | 5223 | 8 | 8/8 |
| http://187.102.219.64:999 | AR | 2314 | 7 | 39/66 |
| http://144.124.251.24:10000 | NL | 742 | 7 | 51/73 |
| http://3.211.120.181:443 | US | 343 | 7 | 21/38 |
| http://165.154.162.73:8888 | US | 6965 | 7 | 80/127 |
| http://102.244.78.61:8083 | CM | 2759 | 6 | 12/15 |
| http://45.245.208.182:8080 | EG | 3422 | 6 | 12/16 |
| http://103.130.61.61:8081 | ID | 1324 | 6 | 98/127 |
| http://187.190.58.152:8081 | MX | 6640 | 6 | 27/100 |
| http://144.124.251.24:10261 | NL | 759 | 6 | 48/59 |
| http://144.124.251.24:10628 | NL | 855 | 6 | 46/59 |
| http://144.124.251.24:10771 | NL | 781 | 6 | 48/59 |
| http://144.124.251.24:11180 | NL | 735 | 6 | 47/58 |
| socks5://144.24.111.128:1088 | IN | 2934 | 6 | 95/127 |
| http://101.206.186.99:8080 | CN | 3118 | 5 | 53/127 |
| http://119.188.131.55:17981 | CN | 5296 | 5 | 64/127 |
| http://187.190.114.40:999 | MX | 7932 | 5 | 21/51 |
| http://144.124.251.24:10811 | NL | 765 | 5 | 47/59 |
| http://34.196.85.244:3128 | US | 317 | 5 | 5/5 |
| http://104.225.162.20:8082 | US | 4747 | 5 | 5/5 |
| socks5://52.128.241.109:1080 | US | 124 | 5 | 6/8 |
| socks5://107.174.30.94:1080 | US | 5548 | 5 | 11/21 |
| http://143.208.152.62:3180 | BR | 7641 | 4 | 24/111 |
| http://186.235.255.220:8080 | BR | 1684 | 4 | 10/28 |
| http://102.244.78.61:8080 | CM | 5868 | 4 | 12/16 |
| http://102.244.78.61:8088 | CM | 2952 | 4 | 11/15 |
| http://45.238.56.249:2010 | EC | 3683 | 4 | 14/76 |
| http://103.133.26.17:3128 | ID | 1709 | 4 | 10/68 |
| http://102.68.76.247:5566 | KE | 5023 | 4 | 23/80 |
| http://144.124.251.24:10082 | NL | 754 | 4 | 47/75 |
| http://144.124.251.24:10187 | NL | 738 | 4 | 47/73 |
| http://144.124.251.24:10412 | NL | 931 | 4 | 46/59 |
| http://144.124.251.24:10601 | NL | 883 | 4 | 46/74 |
| http://144.124.251.24:11265 | NL | 741 | 4 | 52/75 |
| http://5.129.254.5:8888 | RU | 1250 | 4 | 71/82 |
| http://5.129.254.49:8888 | RU | 1198 | 4 | 72/82 |
| http://5.129.254.51:8888 | RU | 1206 | 4 | 72/82 |
| http://5.129.254.60:8888 | RU | 1210 | 4 | 71/81 |
| http://5.129.254.70:8888 | RU | 1217 | 4 | 72/82 |
| http://5.129.254.129:8888 | RU | 1204 | 4 | 77/88 |
| http://5.129.254.154:8888 | RU | 1223 | 4 | 68/78 |
| http://5.129.254.215:8888 | RU | 1194 | 4 | 21/24 |
| http://5.129.254.243:8888 | RU | 1147 | 4 | 21/23 |
| http://44.216.27.249:3128 | US | 366 | 4 | 20/24 |
| socks5://110.38.233.122:1080 | PK | 2063 | 4 | 6/7 |
| socks5://31.129.107.119:443 | RU | 3797 | 4 | 5/6 |
| socks5://116.101.14.169:1089 | VN | 1672 | 4 | 4/4 |
| socks5://168.253.92.93:10808 | ZA | 5212 | 4 | 22/125 |
| http://179.185.75.94:8080 | BR | 4100 | 3 | 6/39 |
| http://186.235.123.3:8080 | BR | 7150 | 3 | 16/110 |
| http://38.7.195.49:999 | CL | 5199 | 3 | 44/101 |
| http://38.7.195.52:999 | CL | 3189 | 3 | 49/109 |
| http://38.7.195.55:999 | CL | 4126 | 3 | 43/101 |
| http://123.119.176.120:8888 | CN | 1779 | 3 | 36/92 |
| http://38.50.165.122:999 | DO | 2638 | 3 | 23/115 |
| http://45.71.186.213:999 | EC | 1970 | 3 | 42/111 |
| http://45.173.228.217:1550 | EC | 1593 | 3 | 5/12 |
| http://181.188.203.112:999 | EC | 4060 | 3 | 34/119 |
| http://186.5.94.216:999 | EC | 6461 | 3 | 24/127 |
| http://41.65.55.27:1981 | EG | 5831 | 3 | 22/67 |
| http://34.88.38.81:9443 | FI | 1059 | 3 | 62/92 |
| http://35.228.49.168:9443 | FI | 843 | 3 | 43/64 |
| http://34.105.252.3:3128 | GB | 2742 | 3 | 6/9 |
| http://43.155.62.157:443 | HK | 6039 | 3 | 25/30 |
| http://8.215.25.3:2080 | ID | 1371 | 3 | 35/127 |
| http://8.215.25.3:2081 | ID | 1050 | 3 | 31/125 |
| http://43.241.247.43:8080 | ID | 1357 | 3 | 13/61 |
| http://103.66.62.125:8080 | ID | 6901 | 3 | 7/36 |
| http://103.124.137.171:8080 | ID | 4337 | 3 | 16/69 |
| http://103.133.26.50:8080 | ID | 1277 | 3 | 7/28 |
| http://103.133.26.72:8080 | ID | 2019 | 3 | 8/53 |
| http://103.133.26.73:3128 | ID | 1418 | 3 | 23/105 |
| http://103.133.26.119:8080 | ID | 2034 | 3 | 7/37 |
| http://103.193.144.91:8080 | ID | 6431 | 3 | 12/66 |
| http://111.92.88.27:3128 | IN | 3842 | 3 | 16/96 |
| http://160.19.41.37:80 | IN | 1572 | 3 | 3/3 |
| http://164.52.219.64:8080 | IN | 3754 | 3 | 3/3 |
| http://178.92.72.129:8080 | IN | 1446 | 3 | 15/38 |
| http://102.203.101.77:8080 | KE | 6608 | 3 | 3/3 |
| http://187.188.171.231:10101 | MX | 5635 | 3 | 13/47 |
| http://144.124.251.24:10084 | NL | 767 | 3 | 46/59 |
