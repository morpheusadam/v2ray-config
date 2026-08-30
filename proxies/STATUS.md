# Proxy status

Generated 2026-08-30T17:24:22Z by `harvest.py`.

- **670** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1421** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14423** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 143/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1228 |
| socks5 | 186 |
| socks4 | 7 |

| country | entries |
|---|---|
| ID | 324 |
| US | 117 |
| CN | 96 |
| CO | 69 |
| PH | 49 |
| MX | 48 |
| VE | 48 |
| DE | 43 |
| BD | 42 |
| BR | 38 |
| TH | 33 |
| RU | 32 |
| VN | 31 |
| EC | 30 |
| NL | 28 |
| FR | 27 |
| IN | 27 |
| TR | 22 |
| DO | 19 |
| EG | 19 |
| HK | 19 |
| SG | 18 |
| CL | 17 |
| AR | 14 |
| KH | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 2 | 2 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 54 | 54 | 30 | 2026-08-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 57 | 57 | 21 | 2026-08-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 57 | 57 | 23 | 2026-08-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 68 | 68 | 12 | 2026-08-30 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 72 | 72 | 23 | 2026-08-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 87 | 87 | 41 | 2026-08-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 93 | 93 | 20 | 2026-08-30 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 102 | 102 | 41 | 2026-08-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-30 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 519 | 519 | 258 | 2026-08-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-08-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 457 | 2026-08-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1160 | 2026-08-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1605 | 2026-08-30 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1816 | 1812 | 0 | 2026-08-30 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 1863 | 1863 | 1557 | 2026-08-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2129 | 2127 | 392 | 2026-08-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2425 | 2423 | 660 | 2026-08-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2678 | 2676 | 2055 | 2026-08-30 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1142 | 37 | 39/40 |
| http://34.43.46.91:443 | US | 2397 | 32 | 37/40 |
| http://34.43.46.91:80 | US | 1466 | 32 | 37/40 |
| http://103.237.102.191:11111 | DE | 930 | 26 | 39/40 |
| http://95.211.174.135:3128 | NL | 1245 | 26 | 39/40 |
| http://204.76.203.9:3128 | NL | 1040 | 26 | 39/40 |
| http://204.76.203.9:8080 | NL | 772 | 26 | 32/33 |
| http://185.200.188.234:10001 | RU | 1275 | 26 | 39/40 |
| http://130.110.103.245:3128 | SA | 1398 | 26 | 38/40 |
| http://95.3.69.222:8080 | TR | 1590 | 26 | 39/40 |
| http://199.7.149.90:3128 | US | 344 | 23 | 23/23 |
| http://199.7.149.96:3128 | US | 355 | 19 | 19/19 |
| http://45.186.6.104:3128 | EC | 753 | 18 | 18/18 |
| http://64.112.184.210:3128 | US | 520 | 18 | 39/40 |
| http://42.96.18.62:1311 | VN | 2206 | 14 | 29/39 |
| socks5://144.91.121.61:1088 | FR | 4931 | 14 | 38/40 |
| http://190.0.246.211:4040 | CO | 1820 | 12 | 35/40 |
| http://103.211.103.170:3128 | HK | 2456 | 12 | 12/12 |
| http://202.28.194.139:31280 | TH | 2767 | 12 | 38/40 |
| socks4://45.61.129.165:9050 | US | 1642 | 12 | 32/40 |
| socks5://101.36.104.46:10808 | JP | 2322 | 12 | 37/40 |
| http://87.251.77.29:3128 | DE | 959 | 11 | 37/40 |
| socks5://45.194.33.12:30001 | HK | 1979 | 11 | 29/36 |
| socks5://45.194.33.12:30002 | HK | 1585 | 11 | 13/14 |
| http://103.177.118.145:8118 | BD | 1489 | 10 | 20/21 |
| http://87.237.15.238:7080 | BE | 3795 | 8 | 8/8 |
| http://197.224.185.3:3128 | MU | 1988 | 8 | 8/8 |
| http://175.136.239.173:8181 | MY | 6713 | 8 | 32/40 |
| http://157.85.111.64:3128 | TH | 4161 | 8 | 8/8 |
| http://68.178.174.239:3128 | US | 965 | 8 | 8/8 |
| http://68.178.174.239:8888 | US | 967 | 8 | 8/8 |
| http://209.174.97.162:5999 | US | 393 | 8 | 8/8 |
| http://8.138.217.152:21001 | CN | 2543 | 7 | 27/40 |
| http://181.78.23.187:999 | CO | 715 | 7 | 8/9 |
| http://181.78.74.252:999 | CO | 769 | 7 | 30/31 |
| http://181.78.74.253:999 | CO | 752 | 7 | 30/31 |
| http://190.97.236.128:999 | VE | 716 | 7 | 29/30 |
| http://190.97.236.129:999 | VE | 1805 | 7 | 29/30 |
| socks5://45.12.18.106:1080 | RU | 1308 | 7 | 7/7 |
| socks5://84.8.102.52:1080 | SA | 1671 | 7 | 7/7 |
| http://212.154.169.90:3128 | KZ | 1303 | 6 | 16/19 |
| socks5://5.75.133.113:10811 | DE | 1512 | 6 | 8/11 |
| socks5://213.199.47.140:1080 | FR | 6882 | 6 | 6/6 |
| http://87.237.15.239:7080 | BE | 731 | 5 | 5/5 |
| http://184.75.221.82:3118 | CA | 441 | 5 | 5/5 |
| http://120.232.115.170:17981 | CN | 1570 | 5 | 24/39 |
| http://123.115.212.50:8888 | CN | 1927 | 5 | 5/5 |
| http://123.121.115.239:8888 | CN | 1434 | 5 | 5/5 |
| http://123.121.121.123:8888 | CN | 1526 | 5 | 5/5 |
| http://190.0.246.213:4040 | CO | 1328 | 5 | 5/5 |
| http://130.61.112.125:443 | DE | 709 | 5 | 5/5 |
| http://194.163.175.167:40000 | FR | 2210 | 5 | 5/5 |
| http://1.231.81.166:3128 | KR | 1044 | 5 | 37/40 |
| http://189.51.168.164:999 | MX | 1469 | 5 | 5/5 |
| http://175.136.239.174:8181 | MY | 5463 | 5 | 26/40 |
| http://43.156.227.68:80 | SG | 961 | 5 | 5/5 |
| http://43.160.242.118:3128 | SG | 2554 | 5 | 30/37 |
| http://157.85.97.203:3128 | TH | 1087 | 5 | 5/5 |
| http://157.85.97.204:3128 | TH | 1125 | 5 | 5/5 |
| http://157.85.97.242:3128 | TH | 1117 | 5 | 5/5 |
| http://157.85.105.218:3128 | TH | 1102 | 5 | 5/5 |
| http://157.85.105.220:3128 | TH | 3162 | 5 | 5/5 |
| http://157.85.108.50:3128 | TH | 1098 | 5 | 5/5 |
| http://45.59.100.205:3128 | US | 223 | 5 | 5/5 |
| socks4://158.220.99.85:4545 | FR | 1729 | 5 | 5/5 |
| socks5://47.250.211.53:1080 | MY | 1440 | 5 | 21/40 |
| socks5://185.118.143.141:1080 | TR | 4926 | 5 | 10/12 |
| http://111.192.21.92:8888 | CN | 1448 | 4 | 4/4 |
| http://186.33.45.220:999 | EC | 4195 | 4 | 6/9 |
| http://84.36.141.180:1976 | EG | 3509 | 4 | 13/26 |
| http://82.64.186.155:8080 | FR | 6242 | 4 | 4/4 |
| http://103.156.15.103:3125 | ID | 7122 | 4 | 6/16 |
| http://20.61.126.88:3128 | NL | 2691 | 4 | 4/4 |
| socks5://101.36.104.239:10808 | JP | 1127 | 4 | 33/40 |
| socks5://85.209.156.148:1080 | US | 2888 | 4 | 8/11 |
| http://193.233.232.49:3131 | AT | 3878 | 3 | 3/3 |
| http://103.141.174.38:11411 | BD | 2570 | 3 | 10/24 |
| http://38.7.195.55:999 | CL | 3688 | 3 | 6/14 |
| http://114.244.223.68:8888 | CN | 1365 | 3 | 3/3 |
| http://114.246.205.76:8888 | CN | 1957 | 3 | 3/3 |
| http://123.121.131.112:8888 | CN | 1544 | 3 | 3/3 |
| http://221.221.165.188:8888 | CN | 1501 | 3 | 4/5 |
| http://190.109.1.58:8080 | CO | 3935 | 3 | 7/35 |
| http://128.140.113.110:8081 | DE | 2287 | 3 | 3/3 |
| http://205.235.1.38:999 | EC | 4086 | 3 | 12/26 |
| http://103.80.214.43:8080 | ID | 3920 | 3 | 6/30 |
| http://103.172.42.221:1111 | ID | 1255 | 3 | 10/38 |
| http://160.25.222.41:7979 | ID | 1313 | 3 | 6/22 |
| http://203.128.69.230:8080 | ID | 2321 | 3 | 8/37 |
| http://45.137.12.90:8080 | MX | 7324 | 3 | 9/34 |
| http://46.8.229.31:8080 | NL | 2237 | 3 | 3/3 |
| http://85.193.65.88:8888 | RU | 1965 | 3 | 11/30 |
| http://35.94.193.222:130 | US | 4507 | 3 | 3/3 |
| http://174.138.162.38:32561 | US | 7212 | 3 | 3/3 |
| http://190.94.213.132:999 | VE | 963 | 3 | 8/35 |
| http://102.23.229.93:8080 | ZA | 3840 | 3 | 8/22 |
| socks5://109.172.55.177:1082 | FR | 4967 | 3 | 20/40 |
| socks5://124.248.177.44:1080 | KH | 1557 | 3 | 6/29 |
| socks5://121.169.46.116:1090 | KR | 2555 | 3 | 26/40 |
| socks5://109.200.111.171:1080 | RU | 3278 | 3 | 16/39 |
