# Proxy status

Generated 2026-11-05T00:30:57Z by `harvest.py`.

- **3966** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **36240** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 172/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 4135 |
| socks5 | 1859 |
| socks4 | 6 |

| country | entries |
|---|---|
| NL | 1730 |
| ID | 1350 |
| PH | 214 |
| CO | 202 |
| CH | 181 |
| MX | 175 |
| TH | 167 |
| BR | 121 |
| TR | 119 |
| IN | 118 |
| US | 103 |
| RU | 90 |
| DO | 86 |
| BD | 82 |
| CN | 82 |
| EC | 78 |
| AR | 75 |
| VE | 59 |
| PE | 57 |
| PK | 54 |
| SG | 49 |
| DE | 47 |
| EG | 42 |
| JP | 40 |
| CL | 36 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-11-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 141 | 141 | 14 | 2026-11-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 44 | 2026-11-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 65 | 2026-11-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 312 | 312 | 60 | 2026-11-05 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 426 | 426 | 245 | 2026-11-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 606 | 606 | 174 | 2026-11-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-11-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1394 | 1394 | 355 | 2026-11-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1129 | 2026-11-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1581 | 2026-11-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1851 | 1851 | 778 | 2026-11-05 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1891 | 1891 | 182 | 2026-11-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2696 | 2696 | 659 | 2026-11-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3728 | 3728 | 1855 | 2026-11-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4514 | 4514 | 1183 | 2026-11-05 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4997 | 4997 | 3756 | 2026-11-05 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 13047 | 13047 | 2183 | 2026-11-05 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 463 | 83 | 83/83 |
| http://103.237.102.191:11111 | DE | 940 | 59 | 165/172 |
| http://103.133.26.73:3128 | ID | 1434 | 48 | 68/150 |
| http://176.111.37.5:39811 | HK | 947 | 43 | 153/172 |
| http://34.43.46.91:80 | US | 446 | 42 | 166/172 |
| http://4.144.146.21:80 | SG | 1036 | 40 | 57/64 |
| http://176.111.37.216:39811 | HK | 889 | 35 | 144/172 |
| http://34.43.46.91:443 | US | 308 | 21 | 161/172 |
| socks5://101.36.104.239:10808 | JP | 2777 | 19 | 148/172 |
| http://130.110.103.245:3128 | SA | 1288 | 18 | 154/172 |
| socks5://193.25.215.182:22222 | US | 1097 | 18 | 145/172 |
| http://103.133.26.72:8080 | ID | 2402 | 15 | 52/98 |
| http://45.189.57.114:3129 | EC | 721 | 14 | 14/14 |
| http://38.172.160.16:999 | VE | 2378 | 12 | 75/123 |
| http://123.200.8.170:10000 | BD | 3600 | 11 | 78/170 |
| http://102.244.78.61:8082 | CM | 1295 | 11 | 50/61 |
| http://190.12.150.244:999 | EC | 1268 | 11 | 124/168 |
| http://154.59.56.72:999 | VE | 2741 | 11 | 98/131 |
| socks5://69.55.49.177:38182 | US | 260 | 11 | 26/27 |
| http://186.96.111.214:999 | CO | 3110 | 10 | 80/161 |
| http://195.226.213.251:8888 | UA | 6325 | 10 | 70/166 |
| http://165.154.162.73:8888 | US | 1879 | 10 | 115/172 |
| socks5://45.61.129.165:9050 | US | 1574 | 10 | 131/172 |
| http://190.123.83.137:999 | AR | 1131 | 9 | 9/9 |
| http://190.0.246.213:4040 | CO | 561 | 9 | 127/137 |
| http://189.51.168.165:999 | MX | 414 | 9 | 78/84 |
| http://154.59.56.74:999 | VE | 6606 | 9 | 92/135 |
| socks5://101.36.104.46:10808 | JP | 1567 | 9 | 148/172 |
| http://128.201.30.222:8666 | BR | 6398 | 8 | 11/18 |
| http://45.65.137.218:999 | CO | 740 | 8 | 60/137 |
| http://131.221.40.131:4040 | CO | 598 | 8 | 10/11 |
| http://177.234.217.83:999 | EC | 4021 | 8 | 15/19 |
| http://177.234.217.92:999 | EC | 2139 | 8 | 16/21 |
| http://103.133.26.119:8080 | ID | 1675 | 8 | 51/82 |
| http://202.47.185.153:8090 | ID | 6042 | 8 | 30/127 |
| http://140.238.32.108:3128 | JP | 2326 | 8 | 97/171 |
| http://82.152.138.127:999 | MX | 316 | 8 | 48/134 |
| http://189.51.168.164:999 | MX | 755 | 8 | 8/8 |
| http://152.42.170.187:9090 | SG | 1314 | 8 | 8/8 |
| http://49.229.100.235:8080 | TH | 1398 | 8 | 80/120 |
| http://171.100.254.137:8080 | TH | 1664 | 8 | 8/8 |
| socks5://176.124.206.150:8443 | FI | 997 | 8 | 8/8 |
| http://187.102.219.64:999 | AR | 1757 | 7 | 69/111 |
| http://185.191.239.248:3128 | CH | 1055 | 7 | 123/171 |
| http://102.244.78.61:8080 | CM | 1304 | 7 | 50/61 |
| http://41.33.245.139:1976 | EG | 1077 | 7 | 10/11 |
| http://43.161.254.16:3128 | HK | 1138 | 7 | 9/12 |
| http://103.130.61.61:8081 | ID | 1367 | 7 | 141/172 |
| http://128.199.116.219:9090 | SG | 1035 | 7 | 72/91 |
| http://61.91.162.126:8080 | TH | 1368 | 7 | 85/115 |
| http://103.10.231.189:8080 | TH | 1887 | 7 | 112/157 |
| http://38.172.181.0:999 | VE | 1914 | 7 | 39/79 |
| socks5://84.200.89.140:1080 | DE | 1316 | 7 | 7/7 |
| http://45.65.224.125:999 | AR | 5125 | 6 | 24/34 |
| http://103.134.56.148:8080 | BD | 5370 | 6 | 37/114 |
| http://184.75.221.82:3118 | CA | 226 | 6 | 119/137 |
| http://27.185.218.213:17981 | CN | 1651 | 6 | 68/172 |
| http://123.121.122.142:8888 | CN | 2259 | 6 | 11/18 |
| http://190.0.246.210:4040 | CO | 965 | 6 | 157/171 |
| http://38.50.165.126:999 | DO | 5140 | 6 | 27/95 |
| http://177.234.217.93:999 | EC | 4224 | 6 | 20/31 |
| http://41.33.89.100:1976 | EG | 1042 | 6 | 12/34 |
| http://37.59.138.176:8080 | ES | 822 | 6 | 32/114 |
| http://34.88.38.81:9443 | FI | 1034 | 6 | 95/137 |
| http://35.228.49.168:9443 | FI | 802 | 6 | 76/109 |
| http://47.86.97.230:18080 | HK | 1917 | 6 | 7/15 |
| http://181.78.44.63:999 | HN | 1704 | 6 | 37/96 |
| http://36.95.245.7:8090 | ID | 3342 | 6 | 8/10 |
| http://103.98.117.98:8080 | ID | 1767 | 6 | 9/12 |
| http://103.133.26.50:8080 | ID | 1422 | 6 | 46/73 |
| http://103.144.54.73:8082 | ID | 1452 | 6 | 56/117 |
| http://103.145.34.112:1111 | ID | 1375 | 6 | 32/144 |
| http://103.147.134.65:8082 | ID | 3304 | 6 | 31/109 |
| http://93.118.120.60:8080 | IR | 2579 | 6 | 14/39 |
| http://103.167.116.166:8087 | PH | 1346 | 6 | 8/11 |
| http://152.42.177.32:8888 | SG | 1035 | 6 | 87/132 |
| http://159.138.84.187:3128 | SG | 1065 | 6 | 6/6 |
| http://195.142.25.185:8080 | TR | 3067 | 6 | 7/8 |
| http://18.217.248.118:5050 | US | 2254 | 6 | 7/8 |
| http://23.177.184.175:3128 | US | 4772 | 6 | 13/24 |
| socks5://188.226.27.24:1080 | RU | 3566 | 6 | 7/8 |
| http://13.239.253.213:29050 | AU | 2473 | 5 | 20/84 |
| http://123.121.98.109:8888 | CN | 3428 | 5 | 19/39 |
| http://186.148.180.133:999 | CO | 3952 | 5 | 6/12 |
| http://200.10.31.42:8081 | CO | 6639 | 5 | 23/45 |
| http://84.36.141.180:1976 | EG | 5293 | 5 | 50/158 |
| http://84.36.141.180:1981 | EG | 953 | 5 | 25/123 |
| http://36.94.27.65:8080 | ID | 2623 | 5 | 8/24 |
| http://103.18.79.197:8085 | ID | 1394 | 5 | 33/108 |
| http://103.194.47.53:8082 | ID | 2388 | 5 | 45/141 |
| http://113.192.30.240:8080 | ID | 4536 | 5 | 22/97 |
| http://157.10.97.85:1111 | ID | 1618 | 5 | 10/26 |
| http://160.19.18.243:8080 | ID | 5387 | 5 | 29/168 |
| http://160.19.146.117:2022 | ID | 1402 | 5 | 30/135 |
| http://160.22.206.37:8082 | ID | 6561 | 5 | 29/126 |
| http://163.223.172.29:1080 | ID | 7307 | 5 | 10/53 |
| http://45.174.242.145:999 | MX | 632 | 5 | 31/127 |
| http://148.230.4.146:999 | MX | 2641 | 5 | 43/164 |
| http://94.183.206.215:8080 | NL | 685 | 5 | 6/9 |
| http://64.76.106.145:999 | PE | 2171 | 5 | 14/45 |
