# Proxy status

Generated 2026-10-04T22:30:53Z by `harvest.py`.

- **3403** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5044** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39342** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 156/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3364 |
| http | 1673 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 2972 |
| ID | 496 |
| ?? | 380 |
| US | 76 |
| RU | 75 |
| PH | 74 |
| MX | 65 |
| CO | 64 |
| CN | 63 |
| BD | 52 |
| BR | 44 |
| DE | 44 |
| EC | 40 |
| IN | 39 |
| VE | 35 |
| PK | 32 |
| TR | 32 |
| VN | 29 |
| DO | 28 |
| CL | 24 |
| SG | 23 |
| EG | 22 |
| KH | 19 |
| HK | 18 |
| AR | 17 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 2 | 2026-10-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 88 | 88 | 34 | 2026-10-04 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 113 | 113 | 46 | 2026-10-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 87 | 2026-10-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 243 | 243 | 91 | 2026-10-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 244 | 244 | 95 | 2026-10-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 252 | 252 | 68 | 2026-10-04 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-10-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 595 | 595 | 108 | 2026-10-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-10-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 777 | 777 | 378 | 2026-10-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-10-04 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1770 | 1766 | 241 | 2026-10-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-10-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2134 | 2132 | 759 | 2026-10-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2231 | 2229 | 1520 | 2026-10-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3542 | 3540 | 1243 | 2026-10-04 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 42057 | 42057 | 25081 | 2026-10-04 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 47424 | 47423 | 2210 | 2026-10-04 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 993 | 97 | 110/111 |
| http://95.3.69.222:8080 | TR | 1535 | 66 | 108/111 |
| http://190.0.246.211:4040 | CO | 3791 | 31 | 98/111 |
| http://34.43.46.91:80 | US | 381 | 28 | 107/111 |
| http://190.0.246.210:4040 | CO | 2721 | 27 | 99/110 |
| http://103.237.102.191:11111 | DE | 1040 | 27 | 105/111 |
| http://18.157.123.132:3128 | DE | 738 | 26 | 58/72 |
| http://34.43.46.91:443 | US | 816 | 24 | 105/111 |
| http://149.130.173.58:9443 | CO | 571 | 22 | 22/22 |
| http://43.173.120.13:8899 | US | 147 | 22 | 22/22 |
| http://45.186.6.104:3128 | EC | 2739 | 16 | 84/89 |
| socks5://101.36.104.239:10808 | JP | 1664 | 15 | 94/111 |
| http://5.129.254.5:8888 | RU | 3326 | 12 | 57/66 |
| http://5.129.254.49:8888 | RU | 1895 | 12 | 58/66 |
| http://5.129.254.51:8888 | RU | 1283 | 12 | 58/66 |
| http://5.129.254.60:8888 | RU | 1324 | 12 | 57/65 |
| http://5.129.254.70:8888 | RU | 3363 | 12 | 58/66 |
| http://5.129.254.129:8888 | RU | 1252 | 12 | 63/72 |
| http://5.129.254.154:8888 | RU | 2226 | 12 | 54/62 |
| http://104.248.151.93:9090 | SG | 941 | 12 | 12/12 |
| http://159.223.41.216:9090 | SG | 964 | 11 | 50/71 |
| socks5://212.77.75.25:1088 | IT | 1041 | 11 | 11/11 |
| socks5://5.255.123.162:1080 | NL | 868 | 9 | 33/94 |
| socks5://171.25.158.95:1080 | SE | 3896 | 9 | 21/26 |
| http://189.51.168.165:999 | MX | 4586 | 8 | 22/23 |
| socks5://185.112.83.80:1080 | FI | 1016 | 8 | 15/16 |
| socks5://213.199.47.140:1080 | FR | 1222 | 8 | 63/77 |
| socks5://47.238.126.208:1080 | HK | 1116 | 8 | 15/16 |
| socks5://85.209.156.148:1080 | US | 4365 | 8 | 45/82 |
| http://103.119.19.218:3128 | CZ | 6252 | 7 | 22/24 |
| http://103.144.54.73:8082 | ID | 1292 | 7 | 31/56 |
| http://5.129.254.243:8888 | RU | 1760 | 7 | 7/7 |
| socks5://121.169.46.116:1090 | KR | 1856 | 7 | 76/111 |
| socks5://79.137.198.71:7777 | NL | 1045 | 7 | 8/11 |
| socks5://83.147.217.103:1080 | US | 497 | 7 | 31/34 |
| socks5://107.167.18.122:443 | US | 98 | 7 | 59/63 |
| http://184.75.221.82:3118 | CA | 411 | 6 | 67/76 |
| http://123.121.123.115:8888 | CN | 1895 | 6 | 20/35 |
| http://177.234.217.43:999 | EC | 6306 | 6 | 29/84 |
| http://202.136.82.219:8080 | ID | 7402 | 6 | 31/109 |
| socks5://123.58.219.171:10808 | HK | 5260 | 6 | 85/111 |
| socks5://45.74.31.23:4324 | NL | 1334 | 6 | 6/6 |
| http://119.188.131.55:17981 | CN | 1515 | 5 | 53/111 |
| http://190.0.246.213:4040 | CO | 982 | 5 | 68/76 |
| http://45.245.208.181:8080 | EG | 2347 | 5 | 7/15 |
| http://144.124.251.24:10000 | NL | 812 | 5 | 37/57 |
| http://144.124.251.24:10007 | NL | 1076 | 5 | 37/60 |
| http://144.124.251.24:10008 | NL | 1293 | 5 | 33/42 |
| http://144.124.251.24:10082 | NL | 743 | 5 | 34/59 |
| http://144.124.251.24:10084 | NL | 742 | 5 | 32/43 |
| http://144.124.251.24:10088 | NL | 765 | 5 | 32/43 |
| http://144.124.251.24:10104 | NL | 857 | 5 | 33/43 |
| http://144.124.251.24:10176 | NL | 994 | 5 | 37/59 |
| http://144.124.251.24:10185 | NL | 956 | 5 | 34/43 |
| http://144.124.251.24:10187 | NL | 814 | 5 | 33/57 |
| http://144.124.251.24:10216 | NL | 880 | 5 | 38/60 |
| http://144.124.251.24:10226 | NL | 749 | 5 | 32/42 |
| http://144.124.251.24:10230 | NL | 1402 | 5 | 36/58 |
| http://144.124.251.24:10261 | NL | 769 | 5 | 33/43 |
| http://144.124.251.24:10299 | NL | 757 | 5 | 32/43 |
| http://144.124.251.24:10333 | NL | 872 | 5 | 36/60 |
| http://144.124.251.24:10337 | NL | 958 | 5 | 31/43 |
| http://144.124.251.24:10346 | NL | 870 | 5 | 34/43 |
| http://144.124.251.24:10366 | NL | 878 | 5 | 34/57 |
| http://144.124.251.24:10372 | NL | 982 | 5 | 37/55 |
| http://144.124.251.24:10412 | NL | 759 | 5 | 33/43 |
| http://144.124.251.24:10431 | NL | 1011 | 5 | 39/59 |
| http://144.124.251.24:10453 | NL | 921 | 5 | 36/48 |
| http://144.124.251.24:10471 | NL | 772 | 5 | 37/58 |
| http://144.124.251.24:10485 | NL | 818 | 5 | 30/43 |
| http://144.124.251.24:10551 | NL | 814 | 5 | 38/59 |
| http://144.124.251.24:10566 | NL | 753 | 5 | 34/44 |
| http://144.124.251.24:10574 | NL | 750 | 5 | 38/60 |
| http://144.124.251.24:10601 | NL | 777 | 5 | 31/58 |
| http://144.124.251.24:10605 | NL | 748 | 5 | 33/43 |
| http://144.124.251.24:10610 | NL | 1564 | 5 | 33/43 |
| http://144.124.251.24:10628 | NL | 862 | 5 | 31/43 |
| http://144.124.251.24:10631 | NL | 958 | 5 | 33/43 |
| http://144.124.251.24:10658 | NL | 959 | 5 | 33/43 |
| http://144.124.251.24:10689 | NL | 1107 | 5 | 34/47 |
| http://144.124.251.24:10771 | NL | 751 | 5 | 33/43 |
| http://144.124.251.24:10800 | NL | 837 | 5 | 33/43 |
| http://144.124.251.24:10801 | NL | 966 | 5 | 34/59 |
| http://144.124.251.24:10811 | NL | 1087 | 5 | 33/43 |
| http://144.124.251.24:10818 | NL | 1112 | 5 | 30/43 |
| http://144.124.251.24:10829 | NL | 1062 | 5 | 31/43 |
| http://144.124.251.24:10953 | NL | 744 | 5 | 34/43 |
| http://144.124.251.24:11011 | NL | 742 | 5 | 34/43 |
| http://144.124.251.24:11108 | NL | 754 | 5 | 34/58 |
| http://144.124.251.24:11124 | NL | 814 | 5 | 35/60 |
| http://144.124.251.24:11180 | NL | 816 | 5 | 32/42 |
| http://144.124.251.24:11265 | NL | 751 | 5 | 37/59 |
| http://144.124.251.24:11266 | NL | 748 | 5 | 34/43 |
| http://144.124.251.24:11274 | NL | 871 | 5 | 37/59 |
| http://144.124.251.24:11450 | NL | 749 | 5 | 31/43 |
| http://144.124.251.24:11480 | NL | 1301 | 5 | 32/43 |
| http://144.124.251.24:11491 | NL | 810 | 5 | 37/59 |
| http://5.129.254.215:8888 | RU | 1203 | 5 | 7/8 |
| http://49.229.100.235:8080 | TH | 1317 | 5 | 32/59 |
| http://154.59.56.72:999 | VE | 2892 | 5 | 48/70 |
