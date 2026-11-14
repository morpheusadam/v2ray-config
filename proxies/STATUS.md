# Proxy status

Generated 2026-11-14T19:03:52Z by `harvest.py`.

- **1125** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3227** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34476** endpoints on record
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
| http | 2600 |
| socks5 | 614 |
| socks4 | 13 |

| country | entries |
|---|---|
| ID | 743 |
| NL | 438 |
| US | 156 |
| PH | 150 |
| CO | 131 |
| MX | 117 |
| CN | 102 |
| TH | 84 |
| BR | 83 |
| VE | 77 |
| RU | 68 |
| BD | 65 |
| IN | 64 |
| TR | 64 |
| EC | 50 |
| VN | 50 |
| AR | 47 |
| SG | 38 |
| CA | 37 |
| DO | 37 |
| DE | 36 |
| ZA | 36 |
| PK | 35 |
| PE | 32 |
| HK | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 85 | 85 | 8 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 97 | 97 | 23 | 2026-11-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-11-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 134 | 134 | 32 | 2026-11-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 72 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 221 | 221 | 157 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 244 | 244 | 21 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 429 | 429 | 79 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 470 | 470 | 215 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-11-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1382 | 1382 | 162 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1133 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1581 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1853 | 1853 | 677 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1870 | 1870 | 442 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 1920 | 1920 | 1219 | 2026-11-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5354 | 5354 | 4091 | 2026-11-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10762 | 10762 | 1880 | 2026-11-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 3931 | 62 | 172/191 |
| http://34.43.46.91:80 | US | 410 | 61 | 185/191 |
| http://130.110.103.245:3128 | SA | 7294 | 37 | 173/191 |
| http://45.189.57.114:3129 | EC | 1070 | 33 | 33/33 |
| http://45.186.6.104:3128 | EC | 747 | 21 | 160/169 |
| http://38.180.18.103:3128 | BE | 767 | 20 | 20/20 |
| socks5://121.46.226.221:10808 | CN | 2285 | 17 | 17/17 |
| http://43.155.62.157:443 | HK | 2669 | 14 | 81/94 |
| http://27.147.155.206:12051 | BD | 3960 | 11 | 11/11 |
| http://51.85.44.162:31819 | IL | 5482 | 10 | 28/43 |
| http://140.238.32.108:3128 | JP | 3784 | 9 | 111/190 |
| http://167.172.76.176:9090 | SG | 5962 | 7 | 111/152 |
| http://123.121.73.146:8888 | CN | 6210 | 6 | 9/13 |
| http://185.166.27.208:2020 | IQ | 4730 | 6 | 18/25 |
| http://128.199.121.61:9090 | SG | 3435 | 6 | 85/111 |
| http://38.63.98.32:999 | VE | 5827 | 6 | 30/79 |
| http://101.251.204.174:8080 | CN | 1765 | 5 | 98/177 |
| http://177.234.217.235:999 | EC | 4991 | 5 | 81/160 |
| http://51.68.102.5:3128 | FR | 1833 | 5 | 5/5 |
| http://119.12.161.248:3128 | HK | 4264 | 5 | 5/5 |
| http://57.182.226.41:3128 | JP | 2293 | 5 | 5/5 |
| http://112.208.174.83:8080 | PH | 5474 | 5 | 32/77 |
| http://82.138.122.43:80 | TR | 3048 | 5 | 41/155 |
| http://104.129.203.85:9480 | US | 334 | 5 | 5/5 |
| socks5://202.61.239.148:8383 | DE | 4756 | 5 | 5/5 |
| socks5://45.194.33.12:30002 | HK | 6039 | 5 | 19/35 |
| http://114.249.209.219:8888 | CN | 6867 | 4 | 58/149 |
| http://123.119.24.241:8888 | CN | 7860 | 4 | 51/126 |
| http://24.152.58.101:999 | CO | 3413 | 4 | 26/85 |
| http://185.145.4.8:8080 | EE | 6341 | 4 | 5/7 |
| http://103.125.212.28:8080 | ID | 2900 | 4 | 24/148 |
| http://157.10.97.101:8181 | ID | 4628 | 4 | 38/169 |
| http://82.152.138.127:999 | MX | 7796 | 4 | 65/153 |
| http://58.69.124.137:8080 | PH | 5021 | 4 | 51/190 |
| http://146.190.80.158:9090 | SG | 3455 | 4 | 83/117 |
| socks4://188.226.27.24:1080 | RU | 6183 | 4 | 19/27 |
| socks5://82.180.146.251:10800 | IN | 2691 | 4 | 18/30 |
| http://103.106.34.49:4995 | BD | 3121 | 3 | 3/3 |
| http://15.229.149.81:3128 | BR | 2810 | 3 | 65/101 |
| http://45.175.59.17:61950 | BR | 6219 | 3 | 10/51 |
| http://45.226.130.66:3128 | BR | 1446 | 3 | 6/7 |
| http://179.125.61.201:8080 | BR | 7688 | 3 | 7/22 |
| http://35.183.29.62:8181 | CA | 2299 | 3 | 45/159 |
| http://56.112.92.32:14172 | CA | 5646 | 3 | 4/18 |
| http://111.192.54.182:8888 | CN | 2826 | 3 | 4/8 |
| http://114.250.195.77:8888 | CN | 3068 | 3 | 11/19 |
| http://123.121.102.115:8888 | CN | 3512 | 3 | 36/151 |
| http://123.121.123.216:8888 | CN | 1704 | 3 | 9/15 |
| http://221.221.144.98:8888 | CN | 3874 | 3 | 22/48 |
| http://221.223.203.55:8888 | CN | 3462 | 3 | 3/3 |
| http://45.65.137.218:999 | CO | 3149 | 3 | 73/156 |
| http://200.10.30.5:8083 | CO | 5880 | 3 | 58/180 |
| http://141.147.19.47:12345 | DE | 3452 | 3 | 13/52 |
| http://181.78.205.45:999 | EC | 5978 | 3 | 10/15 |
| http://54.36.150.233:3128 | FR | 663 | 3 | 9/13 |
| http://141.94.22.37:3128 | FR | 2059 | 3 | 6/7 |
| http://157.173.113.88:3128 | FR | 890 | 3 | 3/3 |
| http://39.109.76.241:8080 | HK | 3394 | 3 | 14/47 |
| http://103.87.85.198:80 | ID | 4141 | 3 | 3/3 |
| http://103.120.174.75:1818 | ID | 5027 | 3 | 42/175 |
| http://160.22.45.66:8080 | ID | 6171 | 3 | 20/50 |
| http://160.22.45.114:8080 | ID | 3693 | 3 | 33/50 |
| http://202.164.220.226:1111 | ID | 4345 | 3 | 20/80 |
| http://51.17.99.116:40013 | IL | 7356 | 3 | 29/79 |
| http://51.85.44.162:8089 | IL | 5446 | 3 | 22/41 |
| http://34.100.244.79:80 | IN | 1956 | 3 | 3/3 |
| http://59.145.185.162:8080 | IN | 2596 | 3 | 8/24 |
| http://102.68.76.247:5566 | KE | 6073 | 3 | 55/144 |
| http://201.163.152.54:999 | MX | 7238 | 3 | 24/78 |
| http://41.203.76.166:8080 | NG | 5680 | 3 | 6/22 |
| http://112.202.247.109:3128 | PH | 3534 | 3 | 4/8 |
| http://124.105.86.222:8090 | PH | 3857 | 3 | 25/143 |
| http://126.209.16.171:5050 | PH | 4099 | 3 | 18/92 |
| http://160.30.141.21:8080 | PH | 7799 | 3 | 20/103 |
| http://185.238.238.21:58080 | PL | 2144 | 3 | 54/155 |
| http://185.238.238.29:58080 | PL | 2006 | 3 | 80/183 |
| http://185.238.238.49:58080 | PL | 1282 | 3 | 70/185 |
| http://45.177.16.131:999 | PY | 1694 | 3 | 45/187 |
| http://45.177.16.134:999 | PY | 4452 | 3 | 43/189 |
| http://128.199.254.13:9090 | SG | 3890 | 3 | 74/120 |
| http://188.166.178.163:3129 | SG | 1800 | 3 | 3/3 |
| http://193.33.157.195:8080 | SY | 6120 | 3 | 5/21 |
| http://216.152.149.246:80 | US | 5434 | 3 | 3/3 |
| http://31.135.214.17:8026 | UZ | 5904 | 3 | 28/113 |
| http://38.63.98.16:999 | VE | 5878 | 3 | 26/80 |
| http://200.59.191.27:999 | VE | 2430 | 3 | 126/186 |
| http://16.28.32.67:36 | ZA | 5320 | 3 | 44/183 |
| socks4://143.198.239.45:10001 | US | 3428 | 3 | 5/6 |
| socks5://45.194.33.12:30001 | HK | 2850 | 3 | 21/67 |
| socks5://45.74.31.47:9405 | NL | 4198 | 3 | 3/3 |
| socks5://37.18.73.60:5566 | RU | 2143 | 3 | 39/88 |
| socks5://188.166.178.163:1088 | SG | 2818 | 3 | 3/3 |
| socks5://116.101.73.52:1057 | VN | 4168 | 3 | 3/3 |
| socks5://116.101.73.161:1057 | VN | 3745 | 3 | 3/3 |
| http://45.65.224.125:999 | AR | 5886 | 2 | 39/53 |
| http://45.178.55.2:999 | AR | 5305 | 2 | 9/32 |
| http://186.38.100.130:999 | AR | 5703 | 2 | 22/66 |
| http://187.102.219.34:999 | AR | 3261 | 2 | 82/142 |
| http://190.123.83.137:999 | AR | 4473 | 2 | 24/28 |
| http://16.26.208.68:18596 | AU | 6488 | 2 | 53/156 |
