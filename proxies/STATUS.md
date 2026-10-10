# Proxy status

Generated 2026-10-10T22:55:17Z by `harvest.py`.

- **1051** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2809** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39655** endpoints on record
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
| http | 1747 |
| socks5 | 1050 |
| socks4 | 12 |

| country | entries |
|---|---|
| NL | 844 |
| ID | 540 |
| PH | 96 |
| US | 93 |
| CO | 88 |
| MX | 86 |
| RU | 85 |
| CN | 84 |
| BD | 56 |
| BR | 53 |
| VE | 52 |
| EC | 51 |
| IN | 40 |
| DE | 39 |
| VN | 37 |
| PK | 36 |
| TR | 35 |
| SG | 34 |
| AR | 30 |
| DO | 28 |
| EG | 28 |
| TH | 27 |
| ZA | 18 |
| CL | 17 |
| FR | 15 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 69 | 69 | 36 | 2026-10-10 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-10-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 116 | 116 | 37 | 2026-10-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 123 | 123 | 36 | 2026-10-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 129 | 129 | 59 | 2026-10-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 82 | 2026-10-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 168 | 168 | 62 | 2026-10-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-10 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 625 | 625 | 237 | 2026-10-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-10-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 820 | 820 | 519 | 2026-10-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-10-10 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1755 | 1751 | 136 | 2026-10-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-10-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1917 | 1915 | 476 | 2026-10-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2003 | 2001 | 765 | 2026-10-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2305 | 2303 | 1669 | 2026-10-10 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 49695 | 49695 | 33907 | 2026-10-10 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 55857 | 55856 | 2717 | 2026-10-10 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 962 | 42 | 109/122 |
| http://34.43.46.91:80 | US | 6834 | 39 | 118/122 |
| http://190.0.246.210:4040 | CO | 774 | 38 | 110/121 |
| http://149.130.173.58:9443 | CO | 494 | 33 | 33/33 |
| http://43.173.120.13:8899 | US | 544 | 33 | 33/33 |
| http://190.0.246.213:4040 | CO | 492 | 16 | 79/87 |
| http://144.124.251.24:10008 | NL | 600 | 16 | 44/53 |
| http://144.124.251.24:10176 | NL | 1041 | 16 | 48/70 |
| http://144.124.251.24:10185 | NL | 709 | 16 | 45/54 |
| http://144.124.251.24:10216 | NL | 706 | 16 | 49/71 |
| http://144.124.251.24:10230 | NL | 611 | 16 | 47/69 |
| http://144.124.251.24:10299 | NL | 531 | 16 | 43/54 |
| http://144.124.251.24:10333 | NL | 650 | 16 | 47/71 |
| http://144.124.251.24:10337 | NL | 765 | 16 | 42/54 |
| http://144.124.251.24:10366 | NL | 624 | 16 | 45/68 |
| http://144.124.251.24:10551 | NL | 1090 | 16 | 49/70 |
| http://144.124.251.24:10574 | NL | 603 | 16 | 49/71 |
| http://144.124.251.24:10601 | NL | 530 | 16 | 42/69 |
| http://144.124.251.24:10631 | NL | 580 | 16 | 44/54 |
| http://144.124.251.24:10689 | NL | 668 | 16 | 45/58 |
| http://144.124.251.24:10829 | NL | 656 | 16 | 42/54 |
| http://144.124.251.24:11108 | NL | 605 | 16 | 45/69 |
| http://144.124.251.24:11124 | NL | 644 | 16 | 46/71 |
| http://144.124.251.24:11265 | NL | 533 | 16 | 48/70 |
| http://197.224.185.3:3128 | MU | 2003 | 14 | 83/90 |
| socks5://160.187.0.89:1080 | VN | 1690 | 13 | 28/35 |
| http://176.111.37.5:39811 | HK | 1310 | 12 | 104/122 |
| http://176.111.37.216:39811 | HK | 1056 | 12 | 101/122 |
| http://189.51.168.165:999 | MX | 370 | 10 | 32/34 |
| http://5.129.254.5:8888 | RU | 1073 | 10 | 67/77 |
| http://5.129.254.49:8888 | RU | 1103 | 10 | 68/77 |
| http://5.129.254.51:8888 | RU | 1088 | 10 | 68/77 |
| http://5.129.254.60:8888 | RU | 910 | 10 | 67/76 |
| http://5.129.254.70:8888 | RU | 1071 | 10 | 68/77 |
| http://5.129.254.129:8888 | RU | 1056 | 10 | 73/83 |
| http://5.129.254.154:8888 | RU | 960 | 10 | 64/73 |
| http://5.129.254.215:8888 | RU | 943 | 10 | 17/19 |
| http://5.129.254.243:8888 | RU | 974 | 10 | 17/18 |
| http://49.229.100.235:8080 | TH | 1577 | 10 | 42/70 |
| http://103.237.102.191:11111 | DE | 1127 | 9 | 115/122 |
| http://43.155.62.157:443 | HK | 1066 | 9 | 22/25 |
| http://128.199.116.219:9090 | SG | 1195 | 9 | 34/41 |
| http://61.91.162.126:8080 | TH | 2031 | 9 | 51/65 |
| http://103.10.231.189:8080 | TH | 1581 | 9 | 76/107 |
| socks5://101.36.104.239:10808 | JP | 1313 | 9 | 104/122 |
| http://144.124.251.24:10084 | NL | 570 | 8 | 42/54 |
| socks5://164.68.114.118:1080 | FR | 863 | 8 | 8/8 |
| http://186.5.94.206:999 | EC | 2441 | 7 | 77/84 |
| http://154.59.56.72:999 | VE | 6370 | 7 | 57/81 |
| http://154.59.56.78:999 | VE | 4942 | 7 | 55/78 |
| socks5://45.155.71.236:1080 | AT | 680 | 7 | 15/27 |
| socks5://129.153.11.56:1080 | US | 76 | 7 | 20/27 |
| http://200.128.84.82:3128 | BR | 684 | 6 | 11/15 |
| http://181.78.195.137:999 | EC | 5716 | 6 | 33/122 |
| http://198.244.254.77:3128 | GB | 5007 | 6 | 6/6 |
| http://65.20.79.228:40002 | IN | 5262 | 6 | 8/10 |
| socks5://36.155.23.163:10808 | CN | 1552 | 6 | 30/59 |
| socks5://212.77.75.25:1088 | IT | 5299 | 6 | 20/22 |
| socks5://171.25.158.95:1080 | SE | 7427 | 6 | 31/37 |
| http://62.193.104.29:1981 | EG | 5259 | 5 | 12/21 |
| http://200.94.38.46:2604 | MX | 3346 | 5 | 12/18 |
| http://200.59.191.27:999 | VE | 2087 | 5 | 78/117 |
| socks4://45.81.154.75:1080 | CA | 5425 | 5 | 14/29 |
| http://190.14.32.231:1080 | AR | 1187 | 4 | 8/17 |
| http://190.12.150.244:999 | EC | 4882 | 4 | 84/118 |
| http://41.33.245.138:1981 | EG | 1055 | 4 | 23/52 |
| http://181.78.44.63:999 | HN | 7723 | 4 | 17/46 |
| http://103.147.135.35:8082 | ID | 1589 | 4 | 21/58 |
| http://203.252.142.217:80 | KR | 1161 | 4 | 4/4 |
| http://45.174.243.160:999 | MX | 4610 | 4 | 14/66 |
| http://104.248.151.93:9090 | SG | 1163 | 4 | 20/23 |
| http://146.190.80.158:9090 | SG | 1376 | 4 | 32/48 |
| http://159.223.41.216:9090 | SG | 1187 | 4 | 59/82 |
| http://23.177.184.95:18080 | US | 515 | 4 | 8/9 |
| http://38.172.181.0:999 | VE | 1816 | 4 | 13/29 |
| http://190.97.229.118:999 | VE | 2223 | 4 | 63/112 |
| http://190.97.241.106:999 | VE | 1360 | 4 | 74/106 |
| socks5://5.75.133.113:10803 | DE | 2739 | 4 | 20/45 |
| socks5://123.58.219.171:10808 | HK | 3067 | 4 | 95/122 |
| socks5://103.88.234.239:40017 | MX | 588 | 4 | 9/19 |
| socks5://38.79.114.43:8885 | US | 418 | 4 | 4/4 |
| socks5://162.120.16.210:1080 | US | 207 | 4 | 36/70 |
| http://187.102.219.42:999 | AR | 1075 | 3 | 62/117 |
| http://201.190.178.191:8080 | AR | 4522 | 3 | 13/55 |
| http://184.75.221.82:3118 | CA | 815 | 3 | 76/87 |
| http://114.249.219.180:8888 | CN | 4299 | 3 | 34/86 |
| http://222.128.173.38:8888 | CN | 1920 | 3 | 24/82 |
| http://18.157.123.132:3128 | DE | 510 | 3 | 65/83 |
| http://38.75.82.219:999 | DO | 2105 | 3 | 24/51 |
| http://38.156.233.219:999 | DO | 6675 | 3 | 7/23 |
| http://45.186.6.104:3128 | EC | 663 | 3 | 93/100 |
| http://177.234.217.45:999 | EC | 3595 | 3 | 18/53 |
| http://181.188.203.40:999 | EC | 4945 | 3 | 9/19 |
| http://84.36.141.180:1976 | EG | 5929 | 3 | 37/108 |
| http://45.198.32.223:8080 | ID | 1625 | 3 | 15/42 |
| http://102.38.7.110:1972 | LY | 5373 | 3 | 3/3 |
| http://144.124.251.24:10187 | NL | 548 | 3 | 43/68 |
| http://144.124.251.24:10605 | NL | 610 | 3 | 43/54 |
| http://144.124.251.24:11491 | NL | 568 | 3 | 47/70 |
| http://130.110.103.245:3128 | SA | 1520 | 3 | 113/122 |
