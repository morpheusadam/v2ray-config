# Proxy status

Generated 2026-10-02T18:23:36Z by `harvest.py`.

- **1578** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3986** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39387** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 121/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2378 |
| http | 1604 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 2153 |
| ID | 447 |
| US | 135 |
| CN | 87 |
| RU | 80 |
| MX | 63 |
| IN | 53 |
| CO | 49 |
| PH | 48 |
| BR | 47 |
| VE | 47 |
| DE | 44 |
| SG | 42 |
| EC | 38 |
| BD | 35 |
| VN | 34 |
| CA | 32 |
| JP | 32 |
| TR | 31 |
| DO | 30 |
| HK | 28 |
| PK | 25 |
| AU | 22 |
| FR | 22 |
| KH | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-10-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 37 | 37 | 18 | 2026-10-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 58 | 58 | 21 | 2026-10-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 71 | 71 | 21 | 2026-10-02 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 85 | 2026-10-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 193 | 193 | 54 | 2026-10-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 218 | 218 | 93 | 2026-10-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 372 | 372 | 123 | 2026-10-02 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 561 | 561 | 163 | 2026-10-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 457 | 2026-10-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1150 | 2026-10-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-10-02 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1843 | 1839 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2524 | 2522 | 658 | 2026-10-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2738 | 2736 | 1922 | 2026-10-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3552 | 3550 | 982 | 2026-10-02 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 37636 | 37636 | 21923 | 2026-10-02 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 43483 | 43482 | 2073 | 2026-10-02 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1268 | 92 | 105/106 |
| http://95.3.69.222:8080 | TR | 2871 | 61 | 103/106 |
| http://213.111.146.36:18080 | NL | 698 | 35 | 38/43 |
| http://190.0.246.211:4040 | CO | 1719 | 26 | 93/106 |
| http://34.43.46.91:80 | US | 1560 | 23 | 102/106 |
| http://190.0.246.210:4040 | CO | 1540 | 22 | 94/105 |
| http://103.237.102.191:11111 | DE | 2649 | 22 | 100/106 |
| http://18.157.123.132:3128 | DE | 693 | 21 | 53/67 |
| http://34.43.46.91:443 | US | 1644 | 19 | 100/106 |
| http://149.130.173.58:9443 | CO | 616 | 17 | 17/17 |
| http://43.173.120.13:8899 | US | 756 | 17 | 17/17 |
| http://185.195.71.218:18080 | CH | 866 | 14 | 34/43 |
| http://37.59.125.131:8888 | FR | 1655 | 14 | 85/106 |
| http://107.150.41.226:18080 | US | 292 | 14 | 42/43 |
| http://197.224.185.3:3128 | MU | 2004 | 12 | 68/74 |
| http://45.186.6.104:3128 | EC | 853 | 11 | 79/84 |
| http://185.191.239.248:3128 | CH | 1448 | 10 | 76/105 |
| socks5://101.36.104.239:10808 | JP | 2692 | 10 | 89/106 |
| http://34.88.38.81:9443 | FI | 758 | 9 | 49/71 |
| http://35.228.49.168:9443 | FI | 779 | 9 | 30/43 |
| http://195.158.8.123:3128 | UZ | 2913 | 9 | 70/104 |
| http://190.97.229.118:999 | VE | 7135 | 9 | 53/96 |
| http://190.97.241.106:999 | VE | 2985 | 9 | 62/90 |
| http://222.128.172.158:8888 | CN | 1395 | 8 | 34/71 |
| http://47.81.56.193:8888 | TH | 1381 | 8 | 66/106 |
| http://35.78.212.217:32053 | JP | 6136 | 7 | 27/88 |
| http://5.129.254.5:8888 | RU | 2278 | 7 | 52/61 |
| http://5.129.254.49:8888 | RU | 1283 | 7 | 53/61 |
| http://5.129.254.51:8888 | RU | 1518 | 7 | 53/61 |
| http://5.129.254.60:8888 | RU | 6300 | 7 | 52/60 |
| http://5.129.254.70:8888 | RU | 1263 | 7 | 53/61 |
| http://5.129.254.129:8888 | RU | 4328 | 7 | 58/67 |
| http://5.129.254.154:8888 | RU | 1338 | 7 | 49/57 |
| http://104.248.151.93:9090 | SG | 1159 | 7 | 7/7 |
| http://154.59.56.78:999 | VE | 2253 | 7 | 42/62 |
| http://190.12.150.244:999 | EC | 6503 | 6 | 72/102 |
| http://159.223.41.216:9090 | SG | 1210 | 6 | 45/66 |
| http://154.59.56.74:999 | VE | 2295 | 6 | 48/69 |
| http://210.211.113.33:80 | VN | 5429 | 6 | 48/76 |
| socks5://212.77.75.25:1088 | IT | 5330 | 6 | 6/6 |
| http://54.206.129.120:41345 | AU | 5621 | 5 | 21/84 |
| http://189.84.157.245:3126 | BR | 6247 | 5 | 5/5 |
| http://38.7.195.51:999 | CL | 2131 | 5 | 36/97 |
| http://122.246.3.12:17981 | CN | 2457 | 5 | 47/100 |
| http://156.240.114.210:3129 | HK | 1494 | 5 | 5/5 |
| http://160.22.217.93:8082 | ID | 4641 | 5 | 18/48 |
| http://128.199.121.61:9090 | SG | 1809 | 5 | 21/26 |
| socks5://109.205.182.143:1088 | FR | 2323 | 5 | 19/21 |
| socks5://101.36.104.46:10808 | JP | 2729 | 5 | 93/106 |
| socks5://202.160.76.169:1080 | TW | 1881 | 5 | 5/5 |
| http://187.102.219.34:999 | AR | 7801 | 4 | 27/57 |
| http://187.102.219.64:999 | AR | 1997 | 4 | 21/45 |
| http://120.232.115.170:17981 | CN | 1524 | 4 | 76/105 |
| http://103.162.54.18:8181 | ID | 2501 | 4 | 4/4 |
| http://103.188.169.95:8080 | ID | 5492 | 4 | 11/73 |
| http://202.169.250.149:8111 | ID | 7897 | 4 | 14/47 |
| http://140.227.61.201:3128 | JP | 4803 | 4 | 24/98 |
| http://202.59.75.5:8080 | PK | 2327 | 4 | 13/24 |
| http://3.1.100.245:3128 | SG | 1134 | 4 | 13/18 |
| http://128.199.254.13:9090 | SG | 4957 | 4 | 27/35 |
| http://129.226.89.151:80 | SG | 1152 | 4 | 35/53 |
| http://38.18.230.153:8888 | US | 750 | 4 | 6/22 |
| http://54.215.41.74:8220 | US | 2637 | 4 | 7/22 |
| socks5://59.152.97.233:1080 | BD | 3990 | 4 | 61/104 |
| socks5://65.21.252.66:10802 | FI | 4367 | 4 | 13/29 |
| socks5://141.148.206.170:1088 | IN | 3596 | 4 | 17/26 |
| socks5://43.155.143.227:1080 | KR | 1043 | 4 | 12/15 |
| socks5://5.255.113.177:1080 | NL | 3362 | 4 | 4/4 |
| socks5://5.255.123.162:1080 | NL | 807 | 4 | 28/89 |
| socks5://45.74.31.23:4452 | NL | 4977 | 4 | 4/4 |
| socks5://45.74.31.47:5934 | NL | 3494 | 4 | 6/7 |
| socks5://45.74.31.50:12399 | NL | 6486 | 4 | 4/4 |
| socks5://171.25.158.95:1080 | SE | 2585 | 4 | 16/21 |
| socks5://202.160.76.221:1080 | TW | 2088 | 4 | 4/4 |
| socks5://162.120.16.210:1080 | US | 430 | 4 | 25/54 |
| http://16.176.232.186:1222 | AU | 6730 | 3 | 9/22 |
| http://16.18.22.211:9090 | CH | 1183 | 3 | 18/66 |
| http://38.7.195.55:999 | CL | 4891 | 3 | 31/80 |
| http://114.244.223.68:8888 | CN | 1355 | 3 | 36/69 |
| http://120.232.115.57:17981 | CN | 2004 | 3 | 24/31 |
| http://221.221.150.127:8888 | CN | 1344 | 3 | 21/52 |
| http://221.221.159.97:8888 | CN | 2125 | 3 | 27/59 |
| http://15.217.214.40:41371 | ES | 1509 | 3 | 15/70 |
| http://18.175.170.244:23666 | GB | 2758 | 3 | 10/18 |
| http://103.20.191.118:8080 | ID | 5651 | 3 | 19/71 |
| http://175.111.96.161:3128 | ID | 6683 | 3 | 3/3 |
| http://82.180.145.170:3129 | IN | 2100 | 3 | 4/8 |
| http://95.215.161.153:8080 | IR | 1421 | 3 | 4/13 |
| http://102.208.166.30:8082 | KE | 6929 | 3 | 15/77 |
| http://189.51.168.165:999 | MX | 846 | 3 | 17/18 |
| http://146.190.80.158:9090 | SG | 2091 | 3 | 23/32 |
| http://18.188.53.175:8181 | US | 4657 | 3 | 8/28 |
| http://44.216.27.249:3128 | US | 291 | 3 | 3/3 |
| http://98.81.204.137:32859 | US | 3282 | 3 | 6/20 |
| http://98.94.14.234:36508 | US | 1542 | 3 | 15/66 |
| http://178.128.146.125:10000 | US | 1388 | 3 | 3/3 |
| http://38.51.207.118:999 | VE | 3816 | 3 | 27/101 |
| http://210.211.113.35:80 | VN | 2784 | 3 | 38/78 |
| socks5://185.112.83.80:1080 | FI | 4330 | 3 | 10/11 |
| socks5://213.199.47.140:1080 | FR | 1766 | 3 | 58/72 |
