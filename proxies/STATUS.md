# Proxy status

Generated 2026-11-25T03:09:24Z by `harvest.py`.

- **1079** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3473** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25533** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 90/600 (15%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3006 |
| socks5 | 460 |
| socks4 | 7 |

| country | entries |
|---|---|
| ID | 832 |
| ?? | 607 |
| NL | 237 |
| PH | 133 |
| MX | 120 |
| CO | 118 |
| VE | 102 |
| US | 96 |
| TR | 84 |
| BR | 79 |
| TH | 74 |
| RU | 69 |
| IN | 65 |
| BD | 59 |
| EC | 52 |
| DO | 44 |
| AR | 43 |
| ZA | 34 |
| PK | 33 |
| CN | 31 |
| EG | 30 |
| VN | 30 |
| SG | 27 |
| DE | 23 |
| KE | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-11-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 112 | 112 | 17 | 2026-11-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 149 | 149 | 35 | 2026-11-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 56 | 2026-11-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 235 | 235 | 19 | 2026-11-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 251 | 251 | 52 | 2026-11-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 446 | 446 | 109 | 2026-11-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 460 | 460 | 312 | 2026-11-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 437 | 2026-11-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 646 | 646 | 99 | 2026-11-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1121 | 2026-11-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1883 | 1883 | 231 | 2026-11-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1904 | 1904 | 411 | 2026-11-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2248 | 2248 | 727 | 2026-11-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2561 | 2561 | 1528 | 2026-11-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5721 | 5721 | 4494 | 2026-11-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12404 | 12404 | 2019 | 2026-11-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1001 | 83 | 193/212 |
| http://130.110.103.245:3128 | SA | 1404 | 58 | 194/212 |
| http://141.94.22.37:3128 | FR | 770 | 24 | 27/28 |
| http://45.155.226.177:3128 | HK | 747 | 21 | 26/28 |
| http://4.144.146.21:80 | SG | 878 | 19 | 95/104 |
| socks5://193.25.215.182:22222 | US | 675 | 18 | 177/212 |
| http://34.43.46.91:80 | US | 384 | 17 | 205/212 |
| http://189.51.168.164:999 | MX | 2565 | 16 | 44/48 |
| http://20.98.234.24:8080 | US | 430 | 16 | 16/16 |
| socks5://69.55.49.177:38182 | US | 1129 | 16 | 56/67 |
| http://103.237.102.191:11111 | DE | 975 | 15 | 199/212 |
| http://45.186.6.104:3128 | EC | 885 | 14 | 180/190 |
| http://103.133.26.50:8080 | ID | 1186 | 14 | 78/113 |
| http://103.133.26.72:8080 | ID | 1124 | 14 | 86/138 |
| http://103.133.26.73:3128 | ID | 1186 | 14 | 102/190 |
| http://147.161.246.34:80 | ?? | 2918 | 12 | 12/12 |
| http://146.190.80.158:9090 | SG | 877 | 11 | 100/138 |
| socks5://101.36.104.46:10808 | JP | 2153 | 11 | 176/212 |
| http://128.199.113.85:9090 | SG | 865 | 10 | 30/43 |
| http://45.135.95.185:3128 | ?? | 5845 | 10 | 10/10 |
| socks5://123.58.219.171:10808 | HK | 1346 | 10 | 154/212 |
| http://190.123.83.137:999 | AR | 3140 | 9 | 42/49 |
| http://144.124.251.24:10007 | NL | 932 | 9 | 85/161 |
| http://144.124.251.24:10082 | NL | 977 | 9 | 83/160 |
| http://144.124.251.24:10104 | NL | 909 | 9 | 81/144 |
| http://144.124.251.24:10216 | NL | 875 | 9 | 96/161 |
| http://144.124.251.24:10471 | NL | 992 | 9 | 86/159 |
| http://144.124.251.24:10566 | NL | 867 | 9 | 91/145 |
| http://144.124.251.24:10574 | NL | 896 | 9 | 91/161 |
| http://144.124.251.24:10801 | NL | 1087 | 9 | 79/160 |
| http://144.124.251.24:11011 | NL | 832 | 9 | 85/144 |
| http://144.124.251.24:11124 | NL | 936 | 9 | 90/161 |
| http://144.124.251.24:11180 | NL | 942 | 9 | 91/143 |
| http://144.124.251.24:11491 | NL | 1009 | 9 | 84/160 |
| socks5://45.194.33.12:30001 | HK | 2772 | 9 | 38/88 |
| http://5.75.173.39:3128 | ?? | 882 | 8 | 8/8 |
| http://50.238.106.26:3128 | ?? | 388 | 8 | 8/8 |
| http://103.163.80.181:8085 | ?? | 1183 | 8 | 8/8 |
| socks5://171.25.158.95:1080 | SE | 7920 | 8 | 93/127 |
| socks5://47.76.227.81:6002 | ?? | 3137 | 8 | 8/8 |
| http://41.196.16.228:1981 | EG | 1307 | 7 | 9/25 |
| http://34.43.46.91:443 | US | 389 | 7 | 196/212 |
| http://154.3.76.16:999 | VE | 5990 | 7 | 17/20 |
| http://158.247.125.5:9443 | ?? | 2775 | 7 | 7/7 |
| http://216.125.18.67:3128 | ?? | 1880 | 7 | 7/7 |
| http://103.120.76.34:8085 | ID | 7002 | 6 | 18/93 |
| http://103.130.61.61:8081 | ID | 2083 | 6 | 176/212 |
| http://103.21.150.15:3128 | VN | 1028 | 6 | 8/24 |
| http://103.125.15.45:8181 | ?? | 5194 | 6 | 7/8 |
| http://193.124.33.31:2052 | ?? | 1074 | 6 | 6/6 |
| http://185.196.182.22:8080 | AL | 3544 | 5 | 50/191 |
| http://185.191.239.248:3128 | CH | 1221 | 5 | 148/211 |
| http://177.234.217.93:999 | EC | 4363 | 5 | 50/71 |
| http://181.188.203.40:999 | EC | 5852 | 5 | 51/109 |
| http://41.196.16.228:1976 | EG | 1456 | 5 | 5/5 |
| http://192.42.85.14:8080 | ID | 6589 | 5 | 24/78 |
| http://43.202.114.177:31192 | KR | 2793 | 5 | 45/122 |
| http://144.124.251.24:10631 | NL | 914 | 5 | 85/144 |
| http://144.124.251.24:10811 | NL | 870 | 5 | 85/144 |
| http://144.124.251.24:10829 | NL | 914 | 5 | 85/144 |
| http://144.124.251.24:11266 | NL | 966 | 5 | 91/144 |
| http://45.136.253.145:3128 | TH | 972 | 5 | 10/16 |
| http://114.249.231.103:8888 | ?? | 5279 | 5 | 5/5 |
| http://114.249.233.148:8888 | ?? | 2877 | 5 | 7/8 |
| socks4://207.246.122.209:20000 | ?? | 459 | 5 | 7/9 |
| socks5://45.74.31.42:4139 | NL | 4531 | 5 | 12/59 |
| socks5://95.31.115.101:9150 | RU | 4661 | 5 | 22/32 |
| socks5://209.50.255.91:1080 | US | 2618 | 5 | 64/129 |
| http://18.231.214.206:14559 | BR | 2286 | 4 | 53/190 |
| http://102.244.78.61:8082 | CM | 1460 | 4 | 78/101 |
| http://102.244.78.61:8083 | CM | 1415 | 4 | 78/100 |
| http://102.244.78.61:8087 | CM | 1421 | 4 | 75/102 |
| http://45.65.138.48:999 | CO | 2396 | 4 | 109/212 |
| http://181.174.228.175:999 | CO | 5859 | 4 | 17/52 |
| http://38.51.48.181:999 | DO | 6909 | 4 | 8/34 |
| http://177.234.217.82:999 | EC | 2451 | 4 | 41/109 |
| http://177.234.217.89:999 | EC | 2389 | 4 | 23/37 |
| http://41.33.89.100:1981 | EG | 3104 | 4 | 20/68 |
| http://52.128.238.98:18080 | HK | 308 | 4 | 21/27 |
| http://103.162.220.246:8085 | ID | 5446 | 4 | 24/106 |
| http://157.66.16.45:7789 | ID | 3622 | 4 | 9/32 |
| http://163.61.245.70:8080 | ID | 7022 | 4 | 17/88 |
| http://154.73.28.253:8080 | LY | 5304 | 4 | 17/44 |
| http://189.51.168.165:999 | MX | 1642 | 4 | 111/124 |
| http://144.124.251.24:10337 | NL | 888 | 4 | 82/144 |
| http://144.124.251.24:10372 | NL | 951 | 4 | 93/156 |
| http://185.238.236.226:58080 | PL | 6599 | 4 | 69/134 |
| http://13.215.184.250:3128 | SG | 1982 | 4 | 42/98 |
| http://89.43.132.239:8080 | SY | 3596 | 4 | 20/125 |
| http://212.175.50.76:8085 | TR | 5961 | 4 | 27/131 |
| http://165.154.162.73:8888 | US | 1688 | 4 | 141/212 |
| http://38.121.212.134:999 | VE | 5953 | 4 | 23/73 |
| http://154.59.56.78:999 | VE | 5079 | 4 | 114/168 |
| http://13.59.11.63:3128 | ?? | 470 | 4 | 4/4 |
| http://31.130.153.132:3128 | ?? | 1561 | 4 | 4/4 |
| http://38.44.17.142:999 | ?? | 2988 | 4 | 4/4 |
| http://101.79.22.162:80 | ?? | 1114 | 4 | 4/4 |
| http://103.81.86.170:8888 | ?? | 7909 | 4 | 4/4 |
| http://103.112.44.197:8085 | ?? | 7777 | 4 | 7/12 |
| http://119.94.185.43:8082 | ?? | 4290 | 4 | 10/12 |
