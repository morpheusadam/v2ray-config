# Proxy status

Generated 2026-09-08T17:13:10Z by `harvest.py`.

- **419** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1981** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15996** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 117/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1677 |
| socks5 | 290 |
| socks4 | 14 |

| country | entries |
|---|---|
| ID | 500 |
| CN | 106 |
| US | 99 |
| CO | 98 |
| PH | 88 |
| MX | 74 |
| BD | 70 |
| RU | 65 |
| ?? | 61 |
| VE | 57 |
| DE | 50 |
| BR | 49 |
| EC | 42 |
| VN | 41 |
| NL | 34 |
| IN | 32 |
| FR | 27 |
| TR | 27 |
| DO | 26 |
| CL | 25 |
| EG | 24 |
| HK | 24 |
| SG | 24 |
| TH | 21 |
| AR | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 52 | 52 | 24 | 2026-09-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 68 | 68 | 18 | 2026-09-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 89 | 89 | 21 | 2026-09-08 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 126 | 126 | 72 | 2026-09-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 128 | 128 | 23 | 2026-09-08 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 133 | 133 | 36 | 2026-09-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-09-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 272 | 272 | 117 | 2026-09-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 306 | 306 | 103 | 2026-09-08 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-09-08 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1458 | 1454 | 362 | 2026-09-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-09-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-09-08 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2054 | 2054 | 1594 | 2026-09-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2369 | 2367 | 179 | 2026-09-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2807 | 2805 | 2151 | 2026-09-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2841 | 2839 | 718 | 2026-09-08 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 797 | 50 | 55/58 |
| http://34.43.46.91:80 | US | 2115 | 50 | 55/58 |
| http://95.211.174.135:3128 | NL | 1574 | 44 | 57/58 |
| http://185.200.188.234:10001 | RU | 1297 | 44 | 57/58 |
| http://130.110.103.245:3128 | SA | 1733 | 44 | 56/58 |
| http://199.7.149.96:3128 | US | 327 | 37 | 37/37 |
| http://64.112.184.210:3128 | US | 1961 | 36 | 57/58 |
| http://103.211.103.170:3128 | HK | 6841 | 30 | 30/30 |
| http://68.178.174.239:3128 | US | 1107 | 26 | 26/26 |
| http://68.178.174.239:8888 | US | 1101 | 26 | 26/26 |
| http://1.231.81.166:3128 | KR | 3882 | 23 | 55/58 |
| http://189.51.168.164:999 | MX | 3633 | 23 | 23/23 |
| socks5://193.25.215.182:22222 | US | 690 | 21 | 54/58 |
| http://116.202.172.187:11000 | DE | 1333 | 19 | 19/19 |
| http://91.134.141.4:3128 | FR | 1426 | 19 | 19/19 |
| http://5.129.254.129:8888 | RU | 1329 | 19 | 19/19 |
| http://176.111.37.5:39811 | HK | 2283 | 18 | 52/58 |
| http://14.251.13.20:8080 | VN | 1208 | 18 | 29/30 |
| http://154.59.56.73:999 | VE | 1928 | 16 | 27/30 |
| http://181.78.23.187:999 | CO | 867 | 15 | 25/27 |
| http://181.78.74.252:999 | CO | 919 | 15 | 47/49 |
| http://181.78.74.253:999 | CO | 910 | 15 | 47/49 |
| http://190.97.236.128:999 | VE | 1887 | 15 | 46/48 |
| http://190.97.236.129:999 | VE | 1902 | 15 | 46/48 |
| http://103.177.118.145:8118 | BD | 3999 | 14 | 37/39 |
| http://186.5.94.206:999 | EC | 1161 | 14 | 19/20 |
| socks5://147.45.60.124:1082 | US | 1826 | 14 | 34/58 |
| http://176.111.37.216:39811 | HK | 3279 | 13 | 46/58 |
| http://197.224.185.3:3128 | MU | 3061 | 13 | 24/26 |
| http://5.129.254.49:8888 | RU | 2278 | 13 | 13/13 |
| http://5.129.254.51:8888 | RU | 1299 | 13 | 13/13 |
| http://5.129.254.70:8888 | RU | 1338 | 13 | 13/13 |
| http://95.3.69.222:8080 | TR | 2279 | 13 | 55/58 |
| socks5://43.135.176.121:1080 | US | 3613 | 13 | 13/13 |
| socks5://45.61.129.165:9050 | US | 3165 | 13 | 49/58 |
| http://5.129.254.60:8888 | RU | 1298 | 12 | 12/12 |
| http://157.85.97.204:3128 | TH | 3066 | 12 | 20/23 |
| http://5.129.254.5:8888 | RU | 1312 | 11 | 12/13 |
| http://202.28.194.139:31280 | TH | 1664 | 11 | 55/58 |
| socks5://185.222.138.237:1080 | XK | 1216 | 11 | 11/11 |
| http://167.233.169.253:1083 | DE | 6995 | 10 | 10/10 |
| http://190.97.241.106:999 | VE | 2222 | 10 | 19/42 |
| socks5://103.210.161.8:1080 | CN | 1496 | 10 | 23/31 |
| http://185.191.239.248:3128 | CH | 3886 | 9 | 44/57 |
| http://117.236.124.166:3128 | IN | 1803 | 9 | 38/58 |
| http://5.129.254.154:8888 | RU | 1290 | 9 | 9/9 |
| http://42.96.18.62:1311 | VN | 3488 | 8 | 44/57 |
| socks5://65.109.196.122:2091 | FI | 5045 | 8 | 11/12 |
| http://157.85.108.47:3128 | TH | 3521 | 7 | 20/26 |
| http://161.35.181.96:999 | US | 523 | 7 | 7/7 |
| socks5://108.174.152.80:1080 | MX | 601 | 7 | 7/7 |
| socks5://107.181.252.58:1081 | US | 2878 | 7 | 7/7 |
| http://190.0.246.210:4040 | CO | 1753 | 6 | 51/57 |
| http://45.186.6.104:3128 | EC | 2860 | 6 | 35/36 |
| http://43.99.60.244:8089 | HK | 881 | 6 | 7/8 |
| http://103.130.61.61:8081 | ID | 7734 | 6 | 47/58 |
| http://52.21.158.119:3128 | US | 1924 | 6 | 10/11 |
| http://107.181.252.58:1082 | US | 1735 | 6 | 6/6 |
| socks5://5.255.113.177:1080 | NL | 1074 | 6 | 16/57 |
| socks5://213.165.38.49:1080 | NL | 2039 | 6 | 8/25 |
| socks5://58.187.162.191:1083 | VN | 2090 | 6 | 6/6 |
| http://184.75.221.82:3118 | CA | 1494 | 5 | 21/23 |
| http://190.0.246.211:4040 | CO | 3495 | 5 | 49/58 |
| http://144.31.185.67:8080 | FI | 6401 | 5 | 11/26 |
| http://168.144.117.43:3129 | IN | 1776 | 5 | 6/8 |
| http://168.144.121.183:3129 | IN | 1481 | 5 | 6/9 |
| http://103.157.200.126:3128 | PK | 1717 | 5 | 11/35 |
| http://129.226.89.151:80 | SG | 849 | 5 | 5/5 |
| http://101.79.26.53:80 | KR | 1327 | 4 | 4/4 |
| http://154.59.56.76:999 | VE | 2615 | 4 | 14/18 |
| socks5://118.179.102.168:9090 | BD | 1703 | 4 | 4/4 |
| socks5://5.75.133.113:10801 | DE | 3472 | 4 | 17/24 |
| socks5://45.144.54.40:1080 | DE | 4842 | 4 | 40/58 |
| socks5://185.49.110.155:1080 | RU | 2803 | 4 | 16/55 |
| http://187.102.219.34:999 | AR | 6486 | 3 | 5/9 |
| http://122.246.3.12:17981 | CN | 1936 | 3 | 25/52 |
| http://124.128.149.84:8090 | CN | 7693 | 3 | 15/54 |
| http://177.234.226.83:1994 | EC | 3830 | 3 | 6/16 |
| http://41.33.219.140:1976 | EG | 1464 | 3 | 15/43 |
| http://41.196.16.232:1976 | EG | 1772 | 3 | 4/5 |
| http://196.204.3.21:1981 | EG | 3497 | 3 | 8/37 |
| http://213.131.85.29:1981 | EG | 1297 | 3 | 3/3 |
| http://34.88.38.81:9443 | FI | 1096 | 3 | 14/23 |
| http://37.59.125.131:8888 | FR | 2009 | 3 | 44/58 |
| http://103.144.54.73:8082 | ID | 6037 | 3 | 3/3 |
| http://103.155.196.166:3125 | ID | 5575 | 3 | 6/40 |
| http://103.250.128.18:8082 | ID | 6576 | 3 | 18/54 |
| http://43.207.239.56:3128 | JP | 550 | 3 | 3/3 |
| http://38.194.246.34:999 | MX | 3975 | 3 | 27/49 |
| http://203.177.217.222:8082 | PH | 6473 | 3 | 3/3 |
| http://107.167.18.122:443 | US | 7423 | 3 | 9/10 |
| http://201.71.2.24:999 | VE | 5167 | 3 | 10/46 |
| http://210.211.113.34:80 | VN | 3860 | 3 | 25/30 |
| http://210.211.113.35:80 | VN | 4057 | 3 | 17/30 |
| socks5://118.179.144.113:9090 | BD | 4653 | 3 | 6/9 |
| socks5://180.165.49.4:1088 | CN | 6532 | 3 | 3/3 |
| socks5://31.76.111.88:1080 | DE | 1095 | 3 | 8/30 |
| socks5://109.123.251.109:1080 | FR | 4689 | 3 | 25/58 |
| socks5://101.36.104.239:10808 | JP | 1012 | 3 | 48/58 |
| socks5://5.255.123.162:1080 | NL | 933 | 3 | 18/41 |
