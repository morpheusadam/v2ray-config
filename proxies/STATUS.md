# Proxy status

Generated 2026-10-11T18:14:46Z by `harvest.py`.

- **1038** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2273** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39399** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 127/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1316 |
| socks5 | 946 |
| socks4 | 11 |

| country | entries |
|---|---|
| NL | 727 |
| ID | 364 |
| RU | 81 |
| CN | 80 |
| MX | 79 |
| US | 79 |
| CO | 64 |
| PH | 64 |
| BD | 52 |
| VE | 46 |
| VN | 42 |
| EC | 39 |
| DE | 37 |
| BR | 34 |
| AR | 33 |
| IN | 32 |
| DO | 31 |
| PK | 26 |
| EG | 25 |
| SG | 25 |
| TR | 23 |
| KH | 15 |
| CL | 14 |
| TH | 14 |
| SY | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 70 | 70 | 18 | 2026-10-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 89 | 89 | 38 | 2026-10-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 128 | 128 | 67 | 2026-10-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-10-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 181 | 181 | 57 | 2026-10-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 198 | 198 | 61 | 2026-10-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 276 | 276 | 104 | 2026-10-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-10-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 654 | 654 | 386 | 2026-10-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-10-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1598 | 2026-10-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1833 | 1829 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2543 | 2541 | 742 | 2026-10-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2842 | 2840 | 1982 | 2026-10-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3334 | 3332 | 1154 | 2026-10-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 51567 | 51567 | 35357 | 2026-10-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 57498 | 57497 | 2626 | 2026-10-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1147 | 43 | 110/123 |
| http://34.43.46.91:80 | US | 1342 | 40 | 119/123 |
| http://190.0.246.210:4040 | CO | 959 | 39 | 111/122 |
| http://149.130.173.58:9443 | CO | 458 | 34 | 34/34 |
| http://43.173.120.13:8899 | US | 1652 | 34 | 34/34 |
| http://190.0.246.213:4040 | CO | 592 | 17 | 80/88 |
| http://144.124.251.24:10008 | NL | 569 | 17 | 45/54 |
| http://144.124.251.24:10230 | NL | 618 | 17 | 48/70 |
| http://144.124.251.24:10337 | NL | 697 | 17 | 43/55 |
| http://144.124.251.24:10366 | NL | 2397 | 17 | 46/69 |
| http://144.124.251.24:10551 | NL | 617 | 17 | 50/71 |
| http://144.124.251.24:10689 | NL | 636 | 17 | 46/59 |
| http://144.124.251.24:10829 | NL | 603 | 17 | 43/55 |
| http://144.124.251.24:11108 | NL | 620 | 17 | 46/70 |
| http://197.224.185.3:3128 | MU | 2224 | 15 | 84/91 |
| socks5://160.187.0.89:1080 | VN | 5640 | 14 | 29/36 |
| http://176.111.37.5:39811 | HK | 866 | 13 | 105/123 |
| http://189.51.168.165:999 | MX | 476 | 11 | 33/35 |
| http://103.237.102.191:11111 | DE | 932 | 10 | 116/123 |
| http://128.199.116.219:9090 | SG | 1023 | 10 | 35/42 |
| http://61.91.162.126:8080 | TH | 1405 | 10 | 52/66 |
| http://103.10.231.189:8080 | TH | 1432 | 10 | 77/108 |
| socks5://101.36.104.239:10808 | JP | 2511 | 10 | 105/123 |
| http://144.124.251.24:10084 | NL | 712 | 9 | 43/55 |
| http://186.5.94.206:999 | EC | 2839 | 8 | 78/85 |
| http://154.59.56.72:999 | VE | 4374 | 8 | 58/82 |
| socks5://45.155.71.236:1080 | AT | 878 | 8 | 16/28 |
| http://198.244.254.77:3128 | GB | 3982 | 7 | 7/7 |
| socks5://36.155.23.163:10808 | CN | 1419 | 7 | 31/60 |
| socks5://212.77.75.25:1088 | IT | 1175 | 7 | 21/23 |
| socks5://171.25.158.95:1080 | SE | 2477 | 7 | 32/38 |
| http://200.59.191.27:999 | VE | 2313 | 6 | 79/118 |
| socks5://45.81.154.75:1080 | CA | 3213 | 6 | 15/30 |
| http://190.12.150.244:999 | EC | 3998 | 5 | 85/119 |
| http://41.33.245.138:1981 | EG | 7900 | 5 | 24/53 |
| http://203.252.142.217:80 | KR | 882 | 5 | 5/5 |
| http://104.248.151.93:9090 | SG | 1024 | 5 | 21/24 |
| http://146.190.80.158:9090 | SG | 1034 | 5 | 33/49 |
| http://159.223.41.216:9090 | SG | 1056 | 5 | 60/83 |
| http://190.97.241.106:999 | VE | 3633 | 5 | 75/107 |
| socks5://5.75.133.113:10803 | DE | 1254 | 5 | 21/46 |
| socks5://123.58.219.171:10808 | HK | 1867 | 5 | 96/123 |
| socks5://103.88.234.239:40017 | MX | 1030 | 5 | 10/20 |
| socks5://38.79.114.43:8885 | US | 397 | 5 | 5/5 |
| socks5://162.120.16.210:1080 | US | 1344 | 5 | 37/71 |
| http://201.190.178.191:8080 | AR | 7653 | 4 | 14/56 |
| http://184.75.221.82:3118 | CA | 302 | 4 | 77/88 |
| http://114.249.219.180:8888 | CN | 1622 | 4 | 35/87 |
| http://18.157.123.132:3128 | DE | 684 | 4 | 66/84 |
| http://45.186.6.104:3128 | EC | 707 | 4 | 94/101 |
| http://177.234.217.45:999 | EC | 4211 | 4 | 19/54 |
| http://144.124.251.24:10605 | NL | 645 | 4 | 44/55 |
| http://144.124.251.24:11491 | NL | 573 | 4 | 48/71 |
| http://130.110.103.245:3128 | SA | 1360 | 4 | 114/123 |
| http://34.43.46.91:443 | US | 1695 | 4 | 116/123 |
| http://193.104.179.115:3128 | UZ | 1431 | 4 | 61/88 |
| socks5://101.36.104.46:10808 | JP | 3130 | 4 | 107/123 |
| socks5://195.13.182.212:8080 | LV | 1889 | 4 | 4/4 |
| http://187.102.219.34:999 | AR | 1697 | 3 | 37/74 |
| http://187.102.219.64:999 | AR | 6706 | 3 | 35/62 |
| http://185.191.239.248:3128 | CH | 861 | 3 | 89/122 |
| http://123.121.122.247:8888 | CN | 1742 | 3 | 3/3 |
| http://123.121.123.207:8888 | CN | 2080 | 3 | 6/8 |
| http://103.119.19.218:3128 | CZ | 6791 | 3 | 29/36 |
| http://38.191.161.182:999 | DO | 6616 | 3 | 11/23 |
| http://45.240.232.61:8080 | EG | 2881 | 3 | 42/103 |
| http://213.131.85.30:1976 | EG | 6039 | 3 | 11/40 |
| http://178.92.72.129:8080 | IN | 1358 | 3 | 12/34 |
| http://144.124.251.24:10000 | NL | 631 | 3 | 47/69 |
| http://144.124.251.24:10431 | NL | 856 | 3 | 50/71 |
| http://144.124.251.24:10953 | NL | 622 | 3 | 44/55 |
| http://58.69.123.64:8082 | PH | 1381 | 3 | 4/6 |
| http://112.198.134.143:8081 | PH | 6959 | 3 | 11/43 |
| http://185.238.238.49:58080 | PL | 950 | 3 | 35/117 |
| http://128.199.121.61:9090 | SG | 1025 | 3 | 35/43 |
| http://167.99.74.174:9090 | SG | 1141 | 3 | 56/83 |
| http://3.211.120.181:443 | US | 247 | 3 | 17/34 |
| http://104.36.237.230:8080 | US | 5620 | 3 | 16/66 |
| http://165.154.162.73:8888 | US | 984 | 3 | 76/123 |
| socks5://118.179.205.159:9090 | BD | 4856 | 3 | 10/40 |
| socks5://202.4.123.220:9090 | BD | 2845 | 3 | 4/7 |
| socks5://134.175.238.113:1080 | CN | 6020 | 3 | 3/3 |
| socks5://213.199.47.140:1080 | FR | 5049 | 3 | 70/89 |
| socks5://156.225.20.83:1080 | HK | 7849 | 3 | 12/40 |
| socks5://220.158.232.118:1080 | KH | 6854 | 3 | 32/122 |
| socks5://5.255.103.55:1080 | NL | 2103 | 3 | 6/18 |
| socks5://5.255.117.250:1080 | NL | 776 | 3 | 42/108 |
| socks5://79.76.59.115:1080 | SE | 2376 | 3 | 35/113 |
| socks5://143.198.239.45:10012 | US | 6515 | 3 | 5/10 |
| http://172.86.76.137:3128 | AE | 2320 | 2 | 13/36 |
| http://168.228.140.145:999 | AR | 3783 | 2 | 22/73 |
| http://181.209.39.90:999 | AR | 3359 | 2 | 4/10 |
| http://213.169.33.8:8001 | BG | 5874 | 2 | 4/17 |
| http://138.204.95.193:8989 | BR | 1571 | 2 | 8/21 |
| http://186.232.176.210:3128 | BR | 3280 | 2 | 2/2 |
| http://38.7.195.50:999 | CL | 7083 | 2 | 41/82 |
| http://102.244.78.61:8082 | CM | 1328 | 2 | 9/12 |
| http://102.244.78.61:8083 | CM | 1334 | 2 | 8/11 |
| http://102.244.78.61:8084 | CM | 1307 | 2 | 8/11 |
| http://102.244.78.61:8086 | CM | 1277 | 2 | 8/11 |
