# Proxy status

Generated 2026-10-01T19:00:43Z by `harvest.py`.

- **1667** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4583** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39670** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 101/600 (17%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2372 |
| http | 2210 |
| socks4 | 1 |

| country | entries |
|---|---|
| NL | 2175 |
| ID | 613 |
| ?? | 326 |
| US | 109 |
| CN | 87 |
| PH | 85 |
| MX | 79 |
| RU | 65 |
| CO | 63 |
| IN | 63 |
| VE | 50 |
| DE | 48 |
| BR | 46 |
| EC | 43 |
| BD | 42 |
| SG | 39 |
| AR | 35 |
| TR | 32 |
| JP | 31 |
| CA | 30 |
| PK | 29 |
| FR | 28 |
| VN | 28 |
| HK | 25 |
| TH | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-10-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 95 | 95 | 21 | 2026-10-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 96 | 96 | 49 | 2026-10-01 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 108 | 108 | 48 | 2026-10-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 91 | 2026-10-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 155 | 155 | 54 | 2026-10-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 210 | 210 | 89 | 2026-10-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-01 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 441 | 441 | 107 | 2026-10-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 557 | 557 | 290 | 2026-10-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-10-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1146 | 2026-10-01 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1784 | 1780 | 541 | 2026-10-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1585 | 2026-10-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2321 | 2319 | 740 | 2026-10-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2688 | 2686 | 1863 | 2026-10-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3525 | 3523 | 1139 | 2026-10-01 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 35700 | 35700 | 20026 | 2026-10-01 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 41999 | 41998 | 2212 | 2026-10-01 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1193 | 90 | 103/104 |
| http://95.3.69.222:8080 | TR | 1517 | 59 | 101/104 |
| http://190.0.246.213:4040 | CO | 1017 | 33 | 62/69 |
| http://213.111.146.36:18080 | NL | 733 | 33 | 36/41 |
| http://190.0.246.211:4040 | CO | 928 | 24 | 91/104 |
| http://34.43.46.91:80 | US | 579 | 21 | 100/104 |
| http://190.0.246.210:4040 | CO | 1298 | 20 | 92/103 |
| http://103.237.102.191:11111 | DE | 937 | 20 | 98/104 |
| http://18.157.123.132:3128 | DE | 784 | 19 | 51/65 |
| socks5://144.91.121.61:1088 | FR | 2752 | 18 | 90/104 |
| http://34.43.46.91:443 | US | 615 | 17 | 98/104 |
| http://149.130.173.58:9443 | CO | 551 | 15 | 15/15 |
| http://43.173.120.13:8899 | US | 574 | 15 | 15/15 |
| http://185.195.71.218:18080 | CH | 2786 | 12 | 32/41 |
| http://186.5.94.206:999 | EC | 5264 | 12 | 63/66 |
| http://37.59.125.131:8888 | FR | 1909 | 12 | 83/104 |
| http://107.150.41.226:18080 | US | 499 | 12 | 40/41 |
| http://197.224.185.3:3128 | MU | 2272 | 10 | 66/72 |
| http://184.75.221.82:3118 | CA | 390 | 9 | 61/69 |
| http://45.186.6.104:3128 | EC | 706 | 9 | 77/82 |
| http://185.191.239.248:3128 | CH | 5765 | 8 | 74/103 |
| socks5://101.36.104.239:10808 | JP | 896 | 8 | 87/104 |
| http://34.88.38.81:9443 | FI | 1125 | 7 | 47/69 |
| http://35.228.49.168:9443 | FI | 872 | 7 | 28/41 |
| http://176.111.37.216:39811 | HK | 1012 | 7 | 85/104 |
| http://195.158.8.123:3128 | UZ | 5511 | 7 | 68/102 |
| http://190.97.229.118:999 | VE | 2271 | 7 | 51/94 |
| http://190.97.241.106:999 | VE | 3901 | 7 | 60/88 |
| http://222.128.172.158:8888 | CN | 1203 | 6 | 32/69 |
| http://47.81.56.193:8888 | TH | 4856 | 6 | 64/104 |
| http://38.172.160.16:999 | VE | 1861 | 6 | 33/55 |
| socks5://144.91.111.48:1088 | FR | 4767 | 6 | 67/104 |
| socks5://45.61.129.165:9050 | US | 3234 | 6 | 84/104 |
| socks5://129.153.11.56:1080 | US | 366 | 6 | 8/9 |
| socks5://160.187.0.89:1080 | VN | 1479 | 6 | 13/17 |
| http://123.121.121.123:8888 | CN | 1826 | 5 | 35/69 |
| http://103.169.130.130:8080 | ID | 5524 | 5 | 7/17 |
| http://35.78.212.217:32053 | JP | 3227 | 5 | 25/86 |
| http://38.56.111.104:999 | PE | 3866 | 5 | 5/5 |
| http://5.129.254.5:8888 | RU | 1721 | 5 | 50/59 |
| http://5.129.254.49:8888 | RU | 1497 | 5 | 51/59 |
| http://5.129.254.51:8888 | RU | 1490 | 5 | 51/59 |
| http://5.129.254.60:8888 | RU | 1559 | 5 | 50/58 |
| http://5.129.254.70:8888 | RU | 1405 | 5 | 51/59 |
| http://5.129.254.129:8888 | RU | 2316 | 5 | 56/65 |
| http://5.129.254.154:8888 | RU | 2058 | 5 | 47/55 |
| http://104.248.151.93:9090 | SG | 947 | 5 | 5/5 |
| http://128.199.116.219:9090 | SG | 988 | 5 | 19/23 |
| http://167.99.74.174:9090 | SG | 941 | 5 | 41/64 |
| http://13.59.172.95:3128 | US | 471 | 5 | 5/5 |
| http://154.59.56.78:999 | VE | 3363 | 5 | 40/60 |
| socks5://45.155.71.236:1080 | AT | 4085 | 5 | 7/9 |
| http://15.229.149.81:3128 | BR | 2677 | 4 | 9/14 |
| http://181.78.17.131:999 | CO | 6646 | 4 | 28/101 |
| http://190.12.150.244:999 | EC | 4925 | 4 | 70/100 |
| http://159.223.41.216:9090 | SG | 961 | 4 | 43/64 |
| http://18.190.253.157:5051 | US | 1825 | 4 | 5/16 |
| http://54.215.41.74:5678 | US | 3989 | 4 | 11/68 |
| http://165.154.162.73:8888 | US | 247 | 4 | 60/104 |
| http://38.51.207.104:8080 | VE | 2706 | 4 | 43/45 |
| http://154.3.76.14:999 | VE | 6737 | 4 | 40/57 |
| http://154.59.56.74:999 | VE | 4878 | 4 | 46/67 |
| http://210.211.113.33:80 | VN | 3373 | 4 | 46/74 |
| http://89.36.160.2:3128 | ?? | 4861 | 4 | 4/4 |
| http://203.175.102.67:3125 | ?? | 2366 | 4 | 4/4 |
| socks5://45.74.31.40:4281 | NL | 7970 | 4 | 4/4 |
| socks5://185.50.202.185:1080 | ?? | 3366 | 4 | 4/4 |
| socks5://212.77.75.25:1088 | ?? | 2295 | 4 | 4/4 |
| http://187.102.219.32:999 | AR | 4388 | 3 | 28/103 |
| http://3.26.199.107:1234 | AU | 6049 | 3 | 6/17 |
| http://54.206.129.120:41345 | AU | 4155 | 3 | 19/82 |
| http://118.179.152.122:81 | BD | 5857 | 3 | 16/82 |
| http://18.231.214.206:14559 | BR | 6337 | 3 | 18/82 |
| http://40.177.104.199:48086 | CA | 3373 | 3 | 21/71 |
| http://38.7.195.51:999 | CL | 2537 | 3 | 34/95 |
| http://119.188.131.55:17981 | CN | 3773 | 3 | 47/104 |
| http://122.246.3.12:17981 | CN | 4905 | 3 | 45/98 |
| http://31.31.74.185:9898 | CZ | 1443 | 3 | 21/25 |
| http://177.53.215.196:1812 | EC | 7350 | 3 | 6/19 |
| http://177.234.221.195:999 | EC | 2769 | 3 | 5/6 |
| http://177.234.221.197:999 | EC | 6978 | 3 | 6/9 |
| http://205.235.1.34:999 | EC | 4145 | 3 | 8/13 |
| http://41.33.60.42:8081 | EG | 4261 | 3 | 32/102 |
| http://84.36.141.180:1976 | EG | 3332 | 3 | 28/90 |
| http://18.163.182.106:21128 | HK | 4657 | 3 | 35/72 |
| http://18.166.56.240:39593 | HK | 5162 | 3 | 10/26 |
| http://103.167.169.78:3128 | ID | 2242 | 3 | 11/55 |
| http://103.184.54.87:8081 | ID | 1369 | 3 | 13/59 |
| http://103.191.196.212:8080 | ID | 3326 | 3 | 16/82 |
| http://103.238.232.202:8080 | ID | 7558 | 3 | 10/43 |
| http://160.22.217.93:8082 | ID | 1339 | 3 | 16/46 |
| http://223.25.106.206:8181 | ID | 4435 | 3 | 5/17 |
| http://150.241.245.131:8080 | IN | 1314 | 3 | 8/16 |
| http://168.144.121.183:3129 | IN | 1579 | 3 | 26/55 |
| http://178.92.72.194:8080 | IN | 1544 | 3 | 5/11 |
| http://102.213.179.210:8080 | KE | 5727 | 3 | 6/36 |
| http://144.124.251.24:10000 | NL | 996 | 3 | 31/50 |
| http://144.124.251.24:10007 | NL | 848 | 3 | 31/53 |
| http://144.124.251.24:10008 | NL | 798 | 3 | 27/35 |
| http://144.124.251.24:10082 | NL | 1846 | 3 | 28/52 |
