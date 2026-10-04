# Proxy status

Generated 2026-10-04T17:21:15Z by `harvest.py`.

- **1565** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3947** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39507** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 98/600 (16%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2563 |
| http | 1380 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 2216 |
| ID | 398 |
| ?? | 250 |
| US | 85 |
| RU | 80 |
| CN | 64 |
| MX | 56 |
| PH | 50 |
| CO | 49 |
| BD | 40 |
| IN | 40 |
| DE | 37 |
| EC | 35 |
| BR | 34 |
| VN | 33 |
| TR | 30 |
| VE | 30 |
| DO | 26 |
| SG | 26 |
| KH | 25 |
| PK | 23 |
| CL | 22 |
| EG | 21 |
| HK | 19 |
| SY | 15 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-10-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 60 | 60 | 6 | 2026-10-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 92 | 92 | 36 | 2026-10-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 100 | 100 | 36 | 2026-10-04 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 146 | 146 | 54 | 2026-10-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 89 | 2026-10-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 162 | 162 | 51 | 2026-10-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 209 | 209 | 34 | 2026-10-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-04 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-10-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 606 | 606 | 328 | 2026-10-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-10-04 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1270 | 1266 | 0 | 2026-10-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1143 | 2026-10-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1591 | 2026-10-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1971 | 1969 | 694 | 2026-10-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2053 | 2051 | 1365 | 2026-10-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2267 | 2265 | 578 | 2026-10-04 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 41560 | 41560 | 25133 | 2026-10-04 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 46858 | 46857 | 2071 | 2026-10-04 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1020 | 96 | 109/110 |
| http://95.3.69.222:8080 | TR | 1610 | 65 | 107/110 |
| http://190.0.246.211:4040 | CO | 1044 | 30 | 97/110 |
| http://34.43.46.91:80 | US | 878 | 27 | 106/110 |
| http://190.0.246.210:4040 | CO | 912 | 26 | 98/109 |
| http://103.237.102.191:11111 | DE | 1036 | 26 | 104/110 |
| http://18.157.123.132:3128 | DE | 810 | 25 | 57/71 |
| http://34.43.46.91:443 | US | 1015 | 23 | 104/110 |
| http://149.130.173.58:9443 | CO | 639 | 21 | 21/21 |
| http://43.173.120.13:8899 | US | 61 | 21 | 21/21 |
| http://45.186.6.104:3128 | EC | 897 | 15 | 83/88 |
| socks5://101.36.104.239:10808 | JP | 1347 | 14 | 93/110 |
| http://5.129.254.5:8888 | RU | 2842 | 11 | 56/65 |
| http://5.129.254.49:8888 | RU | 1424 | 11 | 57/65 |
| http://5.129.254.51:8888 | RU | 1456 | 11 | 57/65 |
| http://5.129.254.60:8888 | RU | 3663 | 11 | 56/64 |
| http://5.129.254.70:8888 | RU | 1577 | 11 | 57/65 |
| http://5.129.254.129:8888 | RU | 1660 | 11 | 62/71 |
| http://5.129.254.154:8888 | RU | 1446 | 11 | 53/61 |
| http://104.248.151.93:9090 | SG | 937 | 11 | 11/11 |
| http://159.223.41.216:9090 | SG | 1077 | 10 | 49/70 |
| socks5://212.77.75.25:1088 | IT | 1220 | 10 | 10/10 |
| http://189.84.157.245:3126 | BR | 6522 | 9 | 9/9 |
| socks5://5.255.123.162:1080 | NL | 958 | 8 | 32/93 |
| socks5://171.25.158.95:1080 | SE | 1963 | 8 | 20/25 |
| http://189.51.168.165:999 | MX | 851 | 7 | 21/22 |
| socks5://185.112.83.80:1080 | FI | 1424 | 7 | 14/15 |
| socks5://213.199.47.140:1080 | FR | 6641 | 7 | 62/76 |
| socks5://47.238.126.208:1080 | HK | 1121 | 7 | 14/15 |
| socks5://85.209.156.148:1080 | US | 6021 | 7 | 44/81 |
| http://114.249.225.156:8888 | CN | 1260 | 6 | 18/32 |
| http://103.119.19.218:3128 | CZ | 1354 | 6 | 21/23 |
| http://103.144.54.73:8082 | ID | 1201 | 6 | 30/55 |
| http://5.129.254.243:8888 | RU | 2422 | 6 | 6/6 |
| socks5://121.169.46.116:1090 | KR | 1970 | 6 | 75/110 |
| socks5://79.137.198.71:7777 | NL | 1525 | 6 | 7/10 |
| socks5://83.147.217.103:1080 | US | 554 | 6 | 30/33 |
| socks5://107.167.18.122:443 | US | 114 | 6 | 58/62 |
| http://201.71.24.65:8082 | BR | 3154 | 5 | 19/99 |
| http://184.75.221.82:3118 | CA | 586 | 5 | 66/75 |
| http://123.121.123.115:8888 | CN | 5294 | 5 | 19/34 |
| http://177.234.217.43:999 | EC | 7386 | 5 | 28/83 |
| http://103.139.126.85:8080 | ID | 4953 | 5 | 16/90 |
| http://202.136.82.219:8080 | ID | 2283 | 5 | 30/108 |
| http://43.153.195.69:80 | SG | 886 | 5 | 32/50 |
| socks5://5.75.133.113:10805 | DE | 1807 | 5 | 12/28 |
| socks5://123.58.219.171:10808 | HK | 1843 | 5 | 84/110 |
| socks5://45.74.31.23:4324 | NL | 4073 | 5 | 5/5 |
| http://119.188.131.55:17981 | CN | 2085 | 4 | 52/110 |
| http://123.121.122.28:8888 | CN | 1219 | 4 | 37/59 |
| http://190.0.246.213:4040 | CO | 796 | 4 | 67/75 |
| http://45.245.208.181:8080 | EG | 1433 | 4 | 6/14 |
| http://110.74.206.40:8181 | KH | 4934 | 4 | 20/94 |
| http://38.194.246.34:999 | MX | 5618 | 4 | 62/101 |
| http://144.124.251.24:10000 | NL | 785 | 4 | 36/56 |
| http://144.124.251.24:10007 | NL | 1399 | 4 | 36/59 |
| http://144.124.251.24:10008 | NL | 820 | 4 | 32/41 |
| http://144.124.251.24:10082 | NL | 1030 | 4 | 33/58 |
| http://144.124.251.24:10084 | NL | 817 | 4 | 31/42 |
| http://144.124.251.24:10088 | NL | 826 | 4 | 31/42 |
| http://144.124.251.24:10104 | NL | 805 | 4 | 32/42 |
| http://144.124.251.24:10176 | NL | 995 | 4 | 36/58 |
| http://144.124.251.24:10185 | NL | 806 | 4 | 33/42 |
| http://144.124.251.24:10187 | NL | 908 | 4 | 32/56 |
| http://144.124.251.24:10216 | NL | 814 | 4 | 37/59 |
| http://144.124.251.24:10226 | NL | 879 | 4 | 31/41 |
| http://144.124.251.24:10230 | NL | 801 | 4 | 35/57 |
| http://144.124.251.24:10261 | NL | 845 | 4 | 32/42 |
| http://144.124.251.24:10299 | NL | 801 | 4 | 31/42 |
| http://144.124.251.24:10333 | NL | 990 | 4 | 35/59 |
| http://144.124.251.24:10337 | NL | 827 | 4 | 30/42 |
| http://144.124.251.24:10346 | NL | 822 | 4 | 33/42 |
| http://144.124.251.24:10366 | NL | 857 | 4 | 33/56 |
| http://144.124.251.24:10372 | NL | 1051 | 4 | 36/54 |
| http://144.124.251.24:10412 | NL | 922 | 4 | 32/42 |
| http://144.124.251.24:10431 | NL | 1444 | 4 | 38/58 |
| http://144.124.251.24:10453 | NL | 810 | 4 | 35/47 |
| http://144.124.251.24:10471 | NL | 843 | 4 | 36/57 |
| http://144.124.251.24:10485 | NL | 811 | 4 | 29/42 |
| http://144.124.251.24:10551 | NL | 836 | 4 | 37/58 |
| http://144.124.251.24:10566 | NL | 852 | 4 | 33/43 |
| http://144.124.251.24:10574 | NL | 824 | 4 | 37/59 |
| http://144.124.251.24:10601 | NL | 854 | 4 | 30/57 |
| http://144.124.251.24:10605 | NL | 962 | 4 | 32/42 |
| http://144.124.251.24:10610 | NL | 1318 | 4 | 32/42 |
| http://144.124.251.24:10628 | NL | 797 | 4 | 30/42 |
| http://144.124.251.24:10631 | NL | 814 | 4 | 32/42 |
| http://144.124.251.24:10658 | NL | 785 | 4 | 32/42 |
| http://144.124.251.24:10689 | NL | 948 | 4 | 33/46 |
| http://144.124.251.24:10771 | NL | 1073 | 4 | 32/42 |
| http://144.124.251.24:10800 | NL | 837 | 4 | 32/42 |
| http://144.124.251.24:10801 | NL | 2186 | 4 | 33/58 |
| http://144.124.251.24:10811 | NL | 824 | 4 | 32/42 |
| http://144.124.251.24:10818 | NL | 843 | 4 | 29/42 |
| http://144.124.251.24:10829 | NL | 828 | 4 | 30/42 |
| http://144.124.251.24:10953 | NL | 955 | 4 | 33/42 |
| http://144.124.251.24:11011 | NL | 795 | 4 | 33/42 |
| http://144.124.251.24:11108 | NL | 1071 | 4 | 33/57 |
| http://144.124.251.24:11124 | NL | 1683 | 4 | 34/59 |
| http://144.124.251.24:11180 | NL | 1351 | 4 | 31/41 |
