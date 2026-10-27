# Proxy status

Generated 2026-10-27T23:08:48Z by `harvest.py`.

- **2114** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4756** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39614** endpoints on record
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
| http | 2820 |
| socks5 | 1925 |
| socks4 | 11 |

| country | entries |
|---|---|
| NL | 1672 |
| ID | 888 |
| ?? | 244 |
| PH | 142 |
| CO | 133 |
| MX | 116 |
| US | 113 |
| RU | 98 |
| BR | 81 |
| BD | 80 |
| TH | 79 |
| CN | 75 |
| VE | 72 |
| EC | 66 |
| VN | 65 |
| IN | 58 |
| AR | 49 |
| TR | 49 |
| SG | 38 |
| DO | 37 |
| PK | 34 |
| DE | 30 |
| ZA | 30 |
| EG | 29 |
| PE | 28 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 2 | 2026-10-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 123 | 123 | 56 | 2026-10-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 138 | 138 | 82 | 2026-10-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 91 | 2026-10-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 249 | 249 | 82 | 2026-10-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 350 | 350 | 33 | 2026-10-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 352 | 352 | 155 | 2026-10-27 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 559 | 559 | 279 | 2026-10-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-10-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 642 | 642 | 237 | 2026-10-27 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1599 | 1599 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1125 | 2026-10-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1591 | 2026-10-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2261 | 2261 | 823 | 2026-10-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2620 | 2620 | 745 | 2026-10-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2882 | 2882 | 1797 | 2026-10-27 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 79759 | 79759 | 65470 | 2026-10-27 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 87227 | 87226 | 3041 | 2026-10-27 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1500 | 76 | 143/156 |
| http://149.130.173.58:9443 | CO | 655 | 67 | 67/67 |
| http://190.0.246.213:4040 | CO | 762 | 50 | 113/121 |
| http://103.237.102.191:11111 | DE | 1511 | 43 | 149/156 |
| http://45.186.6.104:3128 | EC | 888 | 37 | 127/134 |
| http://103.133.26.72:8080 | ID | 1965 | 32 | 37/82 |
| http://103.133.26.73:3128 | ID | 1218 | 32 | 52/134 |
| http://103.133.26.119:8080 | ID | 1505 | 32 | 36/66 |
| http://176.111.37.5:39811 | HK | 1329 | 27 | 137/156 |
| http://34.43.46.91:80 | US | 1009 | 26 | 150/156 |
| socks5://43.245.199.34:1080 | HK | 1164 | 25 | 25/25 |
| http://4.144.146.21:80 | SG | 852 | 24 | 41/48 |
| http://190.0.246.210:4040 | CO | 1281 | 23 | 142/155 |
| http://43.155.62.157:443 | HK | 2265 | 23 | 51/59 |
| http://102.244.78.61:8081 | CM | 1437 | 22 | 35/42 |
| http://186.5.94.206:999 | EC | 1138 | 21 | 109/118 |
| http://184.75.221.82:3118 | CA | 404 | 20 | 107/121 |
| http://189.51.168.165:999 | MX | 626 | 20 | 63/68 |
| http://176.111.37.216:39811 | HK | 1372 | 19 | 128/156 |
| http://103.130.61.61:8081 | ID | 4204 | 18 | 126/156 |
| http://185.191.239.248:3128 | CH | 3412 | 16 | 112/155 |
| http://103.133.26.50:8080 | ID | 1184 | 16 | 35/57 |
| socks5://129.146.121.2:10808 | US | 819 | 13 | 13/13 |
| http://103.130.61.60:8081 | ID | 2189 | 12 | 12/12 |
| http://123.121.132.234:8888 | CN | 1565 | 11 | 15/17 |
| http://146.190.80.158:9090 | SG | 852 | 11 | 60/82 |
| socks5://67.207.92.87:1088 | US | 897 | 11 | 97/155 |
| socks5://69.55.49.177:38182 | US | 572 | 11 | 11/11 |
| socks5://101.36.104.46:10808 | JP | 1512 | 10 | 135/156 |
| http://15.229.149.81:3128 | BR | 5170 | 9 | 37/66 |
| http://89.167.124.218:8888 | DE | 1189 | 9 | 9/9 |
| http://45.65.224.74:999 | AR | 3274 | 8 | 16/21 |
| http://102.244.78.61:8080 | CM | 1428 | 8 | 37/45 |
| http://102.244.78.61:8082 | CM | 1490 | 8 | 37/45 |
| http://102.244.78.61:8083 | CM | 1412 | 8 | 37/44 |
| http://102.244.78.61:8084 | CM | 1412 | 8 | 35/44 |
| http://102.244.78.61:8085 | CM | 1468 | 8 | 35/46 |
| http://102.244.78.61:8086 | CM | 1430 | 8 | 36/44 |
| http://102.244.78.61:8087 | CM | 1401 | 8 | 34/46 |
| http://102.244.78.61:8088 | CM | 1436 | 8 | 36/44 |
| http://102.244.78.61:8089 | CM | 1438 | 8 | 35/44 |
| http://43.202.114.177:7428 | KR | 4160 | 7 | 30/70 |
| http://187.102.219.42:999 | AR | 1828 | 6 | 85/151 |
| http://159.223.41.216:9090 | SG | 852 | 6 | 83/116 |
| socks5://47.238.126.208:1080 | HK | 890 | 6 | 32/61 |
| socks5://51.15.20.32:1088 | NL | 921 | 6 | 17/20 |
| socks5://47.251.127.154:1080 | US | 289 | 6 | 34/109 |
| socks5://166.1.90.114:1090 | US | 636 | 6 | 12/15 |
| http://179.43.10.233:8874 | BR | 2970 | 5 | 24/148 |
| http://122.246.3.12:17981 | CN | 6551 | 5 | 69/150 |
| http://45.65.137.218:999 | CO | 3518 | 5 | 49/121 |
| http://45.71.186.211:999 | EC | 1802 | 5 | 48/109 |
| http://177.234.217.235:999 | EC | 1715 | 5 | 58/125 |
| http://190.12.150.244:999 | EC | 1025 | 5 | 110/152 |
| http://36.50.56.105:8818 | ID | 6380 | 5 | 26/152 |
| http://46.209.30.11:8080 | IR | 1926 | 5 | 17/19 |
| http://116.80.65.235:3128 | JP | 5654 | 5 | 5/5 |
| http://51.15.20.32:3129 | NL | 6169 | 5 | 16/20 |
| http://128.199.116.219:9090 | SG | 855 | 5 | 59/75 |
| http://195.226.213.251:8888 | UA | 7695 | 5 | 57/150 |
| http://34.43.46.91:443 | US | 756 | 5 | 145/156 |
| http://34.207.102.197:5512 | US | 4360 | 5 | 12/56 |
| http://195.158.8.123:3128 | UZ | 2663 | 5 | 104/154 |
| http://82.86.112.48:999 | VE | 6192 | 5 | 36/146 |
| http://45.65.226.169:999 | AR | 3201 | 4 | 13/18 |
| http://123.200.8.170:10000 | BD | 4000 | 4 | 64/154 |
| http://123.121.140.72:8888 | CN | 1480 | 4 | 7/8 |
| http://190.7.138.78:8080 | CO | 1026 | 4 | 40/85 |
| http://177.234.221.197:999 | EC | 5564 | 4 | 30/61 |
| http://34.88.38.81:9443 | FI | 1089 | 4 | 83/121 |
| http://35.228.49.168:9443 | FI | 876 | 4 | 64/93 |
| http://198.244.254.77:3128 | GB | 7559 | 4 | 36/40 |
| http://103.146.38.107:1111 | ID | 5521 | 4 | 21/90 |
| http://103.194.47.53:8082 | ID | 7560 | 4 | 35/125 |
| http://140.238.32.108:3128 | JP | 803 | 4 | 83/155 |
| http://200.94.38.45:2604 | MX | 3539 | 4 | 22/45 |
| http://185.238.238.21:58080 | PL | 1226 | 4 | 37/120 |
| http://154.59.56.72:999 | VE | 1417 | 4 | 83/115 |
| http://16.28.32.67:48907 | ZA | 6180 | 4 | 22/68 |
| socks5://148.251.68.232:8888 | DE | 2114 | 4 | 19/35 |
| socks5://213.199.47.140:1080 | FR | 1400 | 4 | 96/122 |
| socks5://144.24.111.128:1088 | IN | 2103 | 4 | 116/156 |
| socks5://103.100.158.115:10809 | JP | 855 | 4 | 35/44 |
| socks5://103.182.22.221:9000 | ?? | 1836 | 4 | 5/8 |
| http://79.106.108.147:8079 | AL | 3590 | 3 | 13/54 |
| http://45.65.226.173:999 | AR | 2412 | 3 | 7/17 |
| http://187.102.219.34:999 | AR | 1441 | 3 | 58/107 |
| http://13.239.253.213:3128 | AU | 5549 | 3 | 35/121 |
| http://115.127.95.82:8080 | BD | 6648 | 3 | 29/151 |
| http://158.172.153.36:999 | BO | 2512 | 3 | 20/135 |
| http://143.208.84.2:8589 | BR | 2132 | 3 | 19/78 |
| http://179.48.25.1:8095 | BR | 6031 | 3 | 30/151 |
| http://187.108.238.122:8080 | BR | 6698 | 3 | 4/6 |
| http://40.177.104.199:38213 | CA | 2371 | 3 | 20/78 |
| http://40.177.104.199:48086 | CA | 2770 | 3 | 33/123 |
| http://184.70.113.34:3128 | CA | 6258 | 3 | 37/154 |
| http://16.18.22.211:9090 | CH | 3049 | 3 | 35/116 |
| http://101.251.204.174:8080 | CN | 1709 | 3 | 77/142 |
| http://111.201.98.99:8888 | CN | 3835 | 3 | 14/44 |
| http://114.249.232.222:8888 | CN | 1191 | 3 | 44/121 |
