# Proxy status

Generated 2026-10-15T22:39:53Z by `harvest.py`.

- **2229** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3938** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39543** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 166/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2103 |
| socks5 | 1829 |
| socks4 | 6 |

| country | entries |
|---|---|
| NL | 1629 |
| ID | 629 |
| PH | 115 |
| US | 110 |
| CO | 95 |
| MX | 93 |
| RU | 93 |
| CN | 88 |
| IN | 67 |
| BD | 65 |
| BR | 61 |
| VN | 56 |
| EC | 54 |
| VE | 54 |
| TR | 48 |
| DO | 45 |
| AR | 38 |
| SG | 38 |
| EG | 34 |
| JP | 29 |
| DE | 26 |
| PE | 26 |
| TH | 26 |
| KH | 23 |
| CA | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 3 | 3 | 2 | 2026-10-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 79 | 79 | 24 | 2026-10-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 92 | 92 | 45 | 2026-10-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 123 | 123 | 53 | 2026-10-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 69 | 2026-10-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 199 | 199 | 47 | 2026-10-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-10-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 345 | 345 | 146 | 2026-10-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 348 | 348 | 232 | 2026-10-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-10-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 661 | 661 | 81 | 2026-10-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1146 | 2026-10-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1758 | 1754 | 160 | 2026-10-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-10-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2305 | 2303 | 687 | 2026-10-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2446 | 2444 | 1726 | 2026-10-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2767 | 2765 | 810 | 2026-10-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 61127 | 61127 | 47416 | 2026-10-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 67035 | 67034 | 2033 | 2026-10-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1502 | 52 | 119/132 |
| http://149.130.173.58:9443 | CO | 456 | 43 | 43/43 |
| http://190.0.246.213:4040 | CO | 921 | 26 | 89/97 |
| http://197.224.185.3:3128 | MU | 2129 | 24 | 93/100 |
| http://103.237.102.191:11111 | DE | 1443 | 19 | 125/132 |
| http://186.5.94.206:999 | EC | 1977 | 17 | 87/94 |
| http://203.252.142.217:80 | KR | 889 | 14 | 14/14 |
| http://45.186.6.104:3128 | EC | 2695 | 13 | 103/110 |
| socks5://101.36.104.46:10808 | JP | 2307 | 13 | 116/132 |
| http://3.211.120.181:443 | US | 270 | 12 | 26/43 |
| http://165.154.162.73:8888 | US | 7052 | 12 | 85/132 |
| http://102.244.78.61:8083 | CM | 1381 | 11 | 17/20 |
| http://103.130.61.61:8081 | ID | 2582 | 11 | 103/132 |
| http://102.244.78.61:8088 | CM | 1476 | 9 | 16/20 |
| http://144.124.251.24:10187 | NL | 728 | 9 | 52/78 |
| http://5.129.254.5:8888 | RU | 1210 | 9 | 76/87 |
| http://5.129.254.49:8888 | RU | 2174 | 9 | 77/87 |
| http://5.129.254.51:8888 | RU | 2332 | 9 | 77/87 |
| http://5.129.254.60:8888 | RU | 1142 | 9 | 76/86 |
| http://5.129.254.70:8888 | RU | 2249 | 9 | 77/87 |
| http://5.129.254.129:8888 | RU | 1193 | 9 | 82/93 |
| http://5.129.254.154:8888 | RU | 1688 | 9 | 73/83 |
| http://5.129.254.215:8888 | RU | 1592 | 9 | 26/29 |
| http://5.129.254.243:8888 | RU | 1251 | 9 | 26/28 |
| http://34.88.38.81:9443 | FI | 907 | 8 | 67/97 |
| http://35.228.49.168:9443 | FI | 751 | 8 | 48/69 |
| http://103.133.26.50:8080 | ID | 1385 | 8 | 12/33 |
| http://103.133.26.72:8080 | ID | 2144 | 8 | 13/58 |
| http://103.133.26.73:3128 | ID | 1455 | 8 | 28/110 |
| http://103.133.26.119:8080 | ID | 3799 | 8 | 12/42 |
| http://144.124.251.24:10176 | NL | 1038 | 8 | 56/80 |
| http://144.124.251.24:10566 | NL | 730 | 8 | 52/65 |
| socks5://67.207.92.87:1088 | US | 430 | 8 | 76/131 |
| socks5://193.25.215.182:22222 | US | 767 | 8 | 111/132 |
| http://184.75.221.82:3118 | CA | 200 | 7 | 85/97 |
| http://177.234.217.88:999 | EC | 2199 | 7 | 49/124 |
| http://49.156.44.115:8080 | KH | 6654 | 7 | 30/98 |
| http://144.124.251.24:10658 | NL | 624 | 7 | 49/64 |
| http://144.124.251.24:11450 | NL | 598 | 7 | 48/64 |
| http://144.124.251.24:11480 | NL | 609 | 7 | 50/64 |
| http://18.228.228.159:3822 | BR | 2120 | 6 | 15/42 |
| http://121.46.226.221:10808 | CN | 2729 | 6 | 8/9 |
| http://223.85.21.195:8080 | CN | 5241 | 6 | 51/130 |
| http://41.33.245.138:1976 | EG | 1552 | 6 | 15/57 |
| http://213.131.85.29:1976 | EG | 1112 | 6 | 7/8 |
| http://144.124.251.24:10088 | NL | 640 | 6 | 49/64 |
| http://144.124.251.24:10689 | NL | 594 | 6 | 54/68 |
| http://203.177.217.222:8082 | PH | 1417 | 6 | 47/77 |
| http://147.45.164.178:8888 | RU | 1168 | 6 | 6/6 |
| http://13.215.184.250:3128 | SG | 2689 | 6 | 10/18 |
| http://152.42.177.32:8888 | SG | 1032 | 6 | 56/92 |
| http://20.33.10.132:80 | ZA | 3463 | 6 | 6/6 |
| socks5://8.219.122.8:9999 | SG | 2423 | 6 | 12/22 |
| socks5://45.61.129.165:9050 | US | 2716 | 6 | 99/132 |
| http://123.121.142.252:8888 | CN | 6335 | 5 | 26/54 |
| http://38.50.165.123:999 | DO | 4295 | 5 | 30/117 |
| http://41.33.245.138:1981 | EG | 1151 | 5 | 30/62 |
| socks5://178.252.74.29:1081 | RU | 1065 | 5 | 5/5 |
| socks5://209.50.255.91:1080 | US | 270 | 5 | 25/49 |
| socks5://116.104.251.199:1119 | VN | 1866 | 5 | 5/5 |
| http://143.208.152.62:3180 | BR | 6785 | 4 | 28/116 |
| http://56.112.92.32:16486 | CA | 1637 | 4 | 6/17 |
| http://61.149.132.196:8888 | CN | 3531 | 4 | 31/77 |
| http://113.45.195.147:3128 | CN | 1812 | 4 | 60/97 |
| http://222.128.173.231:8888 | CN | 7353 | 4 | 40/100 |
| http://45.65.138.48:999 | CO | 4923 | 4 | 49/132 |
| http://56.155.73.159:27549 | JP | 3693 | 4 | 17/73 |
| http://56.68.116.64:15932 | MY | 2239 | 4 | 14/72 |
| http://128.199.121.61:9090 | SG | 1045 | 4 | 42/52 |
| http://172.236.140.184:80 | SG | 1173 | 4 | 4/4 |
| http://195.158.8.123:3128 | UZ | 3761 | 4 | 86/130 |
| socks5://144.24.111.128:1088 | IN | 2116 | 4 | 99/132 |
| socks5://45.74.31.41:5549 | NL | 3502 | 4 | 4/4 |
| socks5://45.74.31.41:8941 | NL | 1941 | 4 | 4/4 |
| socks5://45.74.31.47:9837 | NL | 4711 | 4 | 4/4 |
| socks5://185.73.115.43:2080 | NL | 5977 | 4 | 6/8 |
| socks5://171.25.158.95:1080 | SE | 4039 | 4 | 39/47 |
| socks5://47.87.97.94:1080 | TH | 1517 | 4 | 7/8 |
| socks5://45.61.188.134:44499 | US | 600 | 4 | 41/99 |
| socks5://158.101.8.92:1080 | US | 1443 | 4 | 10/43 |
| http://16.51.53.116:23517 | AU | 2306 | 3 | 13/48 |
| http://38.7.195.51:999 | CL | 2357 | 3 | 50/123 |
| http://102.244.78.61:8082 | CM | 1529 | 3 | 16/21 |
| http://102.244.78.61:8086 | CM | 1364 | 3 | 15/20 |
| http://102.244.78.61:8089 | CM | 1511 | 3 | 14/20 |
| http://111.201.98.99:8888 | CN | 7690 | 3 | 9/20 |
| http://114.246.203.194:8888 | CN | 1313 | 3 | 19/55 |
| http://190.0.246.210:4040 | CO | 1241 | 3 | 119/131 |
| http://18.157.123.132:3128 | DE | 697 | 3 | 72/93 |
| http://95.133.236.11:3128 | DE | 3470 | 3 | 3/3 |
| http://217.76.245.80:999 | DO | 459 | 3 | 22/88 |
| http://177.234.221.202:999 | EC | 4288 | 3 | 21/36 |
| http://190.12.150.244:999 | EC | 6279 | 3 | 93/128 |
| http://41.128.72.143:1981 | EG | 2095 | 3 | 17/62 |
| http://41.128.90.51:1981 | EG | 1787 | 3 | 8/39 |
| http://205.237.105.49:3129 | FR | 660 | 3 | 3/3 |
| http://198.244.254.77:3128 | GB | 3264 | 3 | 14/16 |
| http://18.166.56.240:39593 | HK | 1990 | 3 | 17/54 |
| http://176.111.37.5:39811 | HK | 1419 | 3 | 113/132 |
| http://38.103.250.205:8080 | ID | 2004 | 3 | 13/95 |
