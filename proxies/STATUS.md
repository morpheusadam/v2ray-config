# Proxy status

Generated 2026-11-10T20:32:13Z by `harvest.py`.

- **1852** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4028** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35472** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 170/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2667 |
| socks5 | 1341 |
| socks4 | 20 |

| country | entries |
|---|---|
| NL | 1108 |
| ID | 831 |
| US | 158 |
| PH | 143 |
| MX | 139 |
| CO | 126 |
| CN | 118 |
| TH | 92 |
| RU | 88 |
| BR | 79 |
| TR | 75 |
| BD | 70 |
| VE | 70 |
| IN | 60 |
| EC | 59 |
| AR | 51 |
| DO | 49 |
| PK | 44 |
| VN | 43 |
| PE | 37 |
| DE | 36 |
| EG | 33 |
| SG | 31 |
| ZA | 30 |
| JP | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-11-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 40 | 40 | 10 | 2026-11-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 75 | 75 | 25 | 2026-11-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 98 | 98 | 13 | 2026-11-10 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 39 | 2026-11-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 69 | 2026-11-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 282 | 282 | 32 | 2026-11-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 331 | 331 | 251 | 2026-11-10 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 650 | 650 | 117 | 2026-11-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1576 | 1576 | 643 | 2026-11-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-11-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1621 | 1621 | 470 | 2026-11-10 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1702 | 1702 | 151 | 2026-11-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2194 | 2194 | 1268 | 2026-11-10 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5191 | 5191 | 3944 | 2026-11-10 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10481 | 10481 | 1808 | 2026-11-10 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1586 | 59 | 79/161 |
| http://176.111.37.5:39811 | HK | 1040 | 54 | 164/183 |
| http://34.43.46.91:80 | US | 434 | 53 | 177/183 |
| http://4.144.146.21:80 | SG | 1158 | 51 | 68/75 |
| http://176.111.37.216:39811 | HK | 960 | 46 | 155/183 |
| http://34.43.46.91:443 | US | 327 | 32 | 172/183 |
| http://130.110.103.245:3128 | SA | 1365 | 29 | 165/183 |
| http://103.133.26.72:8080 | ID | 1542 | 26 | 63/109 |
| http://45.189.57.114:3129 | EC | 1823 | 25 | 25/25 |
| http://103.133.26.119:8080 | ID | 2021 | 19 | 62/93 |
| http://189.51.168.164:999 | MX | 4915 | 19 | 19/19 |
| http://49.229.100.235:8080 | TH | 1574 | 19 | 91/131 |
| http://171.100.254.137:8080 | TH | 1790 | 19 | 19/19 |
| http://43.161.254.16:3128 | HK | 1864 | 18 | 20/23 |
| http://103.130.61.61:8081 | ID | 4436 | 18 | 152/183 |
| http://184.75.221.82:3118 | CA | 222 | 17 | 130/148 |
| http://102.244.78.61:8089 | CM | 3775 | 14 | 58/71 |
| http://45.186.6.104:3128 | EC | 634 | 13 | 152/161 |
| http://38.180.18.103:3128 | BE | 515 | 12 | 12/12 |
| http://190.71.72.85:2525 | CO | 602 | 11 | 27/68 |
| http://102.244.78.61:8090 | CM | 2408 | 10 | 59/75 |
| http://167.172.76.176:9090 | SG | 1147 | 9 | 104/144 |
| socks5://121.46.226.221:10808 | CN | 3205 | 9 | 9/9 |
| http://177.234.217.44:999 | EC | 1985 | 7 | 30/83 |
| http://84.36.141.180:1981 | EG | 5872 | 7 | 34/134 |
| http://104.248.151.93:9090 | SG | 1158 | 7 | 62/84 |
| http://1.20.178.212:80 | TH | 3481 | 7 | 22/47 |
| http://172.239.170.24:3128 | US | 1162 | 7 | 12/17 |
| http://45.65.224.125:999 | AR | 1712 | 6 | 33/45 |
| http://102.244.78.61:8083 | CM | 1687 | 6 | 57/71 |
| http://102.244.78.61:8088 | CM | 1688 | 6 | 56/71 |
| http://123.121.108.22:8888 | CN | 2306 | 6 | 24/34 |
| http://123.121.132.234:8888 | CN | 2068 | 6 | 30/44 |
| http://204.199.106.226:999 | CO | 6006 | 6 | 6/6 |
| http://103.237.102.191:11111 | DE | 567 | 6 | 174/183 |
| http://43.155.62.157:443 | HK | 2153 | 6 | 73/86 |
| http://82.152.138.127:999 | MX | 366 | 6 | 58/145 |
| http://189.51.168.165:999 | MX | 4345 | 6 | 88/95 |
| http://144.124.251.24:10216 | NL | 506 | 6 | 79/132 |
| socks5://5.255.113.177:1080 | NL | 4714 | 6 | 32/81 |
| http://182.252.89.134:8080 | BD | 3926 | 5 | 16/42 |
| http://15.223.187.219:55865 | CA | 792 | 5 | 37/97 |
| http://102.244.78.61:8080 | CM | 2647 | 5 | 60/72 |
| http://123.119.24.241:8888 | CN | 6986 | 5 | 45/118 |
| http://123.121.99.174:8888 | CN | 1839 | 5 | 5/5 |
| http://221.221.144.98:8888 | CN | 2061 | 5 | 16/40 |
| http://45.65.137.218:999 | CO | 1797 | 5 | 68/148 |
| http://45.245.208.180:8080 | EG | 3071 | 5 | 38/56 |
| http://51.94.221.175:1857 | ES | 5450 | 5 | 33/124 |
| http://202.58.77.131:7777 | ID | 4624 | 5 | 13/23 |
| http://206.135.80.74:999 | MX | 3648 | 5 | 5/5 |
| http://144.124.251.24:10771 | NL | 478 | 5 | 72/115 |
| http://45.177.16.133:999 | PY | 3828 | 5 | 21/77 |
| http://3.21.129.156:2085 | US | 1952 | 5 | 27/67 |
| http://195.158.8.123:3128 | UZ | 5259 | 5 | 120/181 |
| socks5://101.36.104.46:10808 | JP | 2070 | 5 | 156/183 |
| http://201.28.86.18:61804 | BR | 2787 | 4 | 4/4 |
| http://15.223.187.219:35507 | CA | 902 | 4 | 22/96 |
| http://185.191.239.248:3128 | CH | 2129 | 4 | 132/182 |
| http://102.244.78.61:8081 | CM | 1677 | 4 | 56/69 |
| http://49.233.205.10:3128 | CN | 3814 | 4 | 27/182 |
| http://114.249.210.198:8888 | CN | 1951 | 4 | 8/18 |
| http://123.121.109.207:8888 | CN | 7724 | 4 | 4/4 |
| http://123.121.113.161:8888 | CN | 2224 | 4 | 7/8 |
| http://123.121.114.100:8888 | CN | 7144 | 4 | 10/15 |
| http://63.180.203.233:1976 | DE | 1994 | 4 | 29/95 |
| http://177.234.217.92:999 | EC | 2034 | 4 | 25/32 |
| http://177.234.217.93:999 | EC | 5122 | 4 | 30/42 |
| http://177.234.217.235:999 | EC | 2562 | 4 | 76/152 |
| http://94.43.164.242:8080 | GE | 7556 | 4 | 28/117 |
| http://15.232.45.244:38353 | ID | 3247 | 4 | 25/138 |
| http://38.226.242.83:8080 | ID | 3456 | 4 | 10/28 |
| http://45.198.11.164:9191 | ID | 5699 | 4 | 34/77 |
| http://45.43.60.220:8080 | JP | 2802 | 4 | 101/182 |
| http://45.174.241.224:999 | MX | 2900 | 4 | 4/4 |
| http://206.135.47.107:999 | MX | 3401 | 4 | 31/53 |
| http://38.210.106.24:999 | PE | 7302 | 4 | 11/38 |
| http://180.191.0.205:8081 | PH | 5925 | 4 | 10/23 |
| http://91.185.193.115:8080 | SI | 5152 | 4 | 17/79 |
| http://61.91.162.126:8080 | TH | 1510 | 4 | 95/126 |
| http://103.10.231.189:8080 | TH | 1975 | 4 | 122/168 |
| http://195.142.250.34:8080 | TR | 7298 | 4 | 15/41 |
| http://13.143.240.243:999 | VE | 7469 | 4 | 4/4 |
| http://38.76.9.1:999 | VE | 3669 | 4 | 23/46 |
| http://154.59.56.72:999 | VE | 2953 | 4 | 106/142 |
| socks4://143.198.239.45:10043 | US | 6914 | 4 | 8/29 |
| socks5://157.254.223.42:1080 | IN | 1465 | 4 | 5/12 |
| socks5://171.25.158.95:1080 | SE | 3779 | 4 | 77/98 |
| http://45.65.226.171:999 | AR | 3234 | 3 | 11/21 |
| http://27.147.153.179:12051 | BD | 6697 | 3 | 3/3 |
| http://27.147.155.206:12051 | BD | 1951 | 3 | 3/3 |
| http://103.170.185.162:46 | BD | 6963 | 3 | 32/171 |
| http://187.0.36.2:8080 | BR | 6148 | 3 | 7/22 |
| http://35.183.29.62:19094 | CA | 4119 | 3 | 20/98 |
| http://102.244.78.61:8086 | CM | 2428 | 3 | 58/71 |
| http://1.15.53.214:8888 | CN | 3219 | 3 | 51/177 |
| http://111.192.28.24:8888 | CN | 4675 | 3 | 4/5 |
| http://114.252.202.38:8888 | CN | 5700 | 3 | 10/18 |
| http://38.19.238.36:999 | CO | 1746 | 3 | 10/19 |
| http://45.65.138.48:999 | CO | 1303 | 3 | 86/183 |
