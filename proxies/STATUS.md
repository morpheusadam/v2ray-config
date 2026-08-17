# Proxy status

Generated 2026-08-17T13:43:32Z by `harvest.py`.

- **100** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **872** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **12278** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 57/600 (10%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 657 |
| socks5 | 200 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 173 |
| US | 76 |
| CO | 52 |
| RU | 48 |
| CN | 38 |
| NL | 31 |
| PH | 27 |
| MX | 25 |
| VE | 24 |
| BD | 21 |
| BR | 21 |
| DE | 20 |
| VN | 20 |
| EC | 19 |
| JP | 19 |
| FR | 18 |
| IN | 18 |
| SG | 18 |
| HK | 16 |
| TR | 16 |
| DO | 11 |
| TH | 10 |
| FI | 9 |
| CL | 8 |
| PE | 8 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 2 | 0 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 4 | 2026-08-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 60 | 60 | 36 | 2026-08-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 105 | 105 | 11 | 2026-08-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 128 | 128 | 74 | 2026-08-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 138 | 138 | 33 | 2026-08-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 140 | 140 | 58 | 2026-08-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 92 | 2026-08-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 174 | 174 | 87 | 2026-08-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 313 | 313 | 153 | 2026-08-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-08-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 459 | 2026-08-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1145 | 2026-08-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1620 | 2026-08-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1846 | 1842 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1990 | 1988 | 181 | 2026-08-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2264 | 2262 | 704 | 2026-08-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2281 | 2281 | 1855 | 2026-08-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2441 | 2439 | 2007 | 2026-08-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 7280 | 14 | 14/14 |
| http://64.112.184.210:3128 | US | 251 | 14 | 14/14 |
| socks5://69.55.49.177:38182 | US | 1502 | 14 | 14/14 |
| http://181.39.25.196:8118 | EC | 964 | 11 | 13/14 |
| http://190.0.246.210:4040 | CO | 2026 | 10 | 12/13 |
| socks5://144.24.47.42:1080 | US | 5539 | 8 | 9/10 |
| http://14.139.235.82:3128 | IN | 2340 | 6 | 11/14 |
| http://34.43.46.91:443 | US | 1169 | 6 | 11/14 |
| http://34.43.46.91:80 | US | 670 | 6 | 11/14 |
| http://181.78.74.252:999 | CO | 674 | 5 | 5/5 |
| http://181.78.74.253:999 | CO | 690 | 5 | 5/5 |
| http://157.230.178.216:40000 | US | 2910 | 5 | 12/13 |
| socks5://129.151.9.55:10808 | US | 811 | 5 | 11/14 |
| socks5://147.45.60.139:1082 | US | 5272 | 5 | 5/5 |
| http://186.148.162.155:999 | CO | 2961 | 4 | 6/7 |
| http://174.137.134.182:2999 | US | 4204 | 4 | 12/13 |
| http://190.97.229.118:999 | VE | 2067 | 4 | 4/4 |
| http://190.97.236.128:999 | VE | 636 | 4 | 4/4 |
| http://190.97.236.129:999 | VE | 643 | 4 | 4/4 |
| http://200.10.30.5:8083 | CO | 2951 | 3 | 3/3 |
| http://186.33.45.219:999 | EC | 3229 | 3 | 3/3 |
| http://200.59.191.27:999 | VE | 3417 | 3 | 7/9 |
| socks5://5.249.165.195:20000 | US | 1807 | 3 | 10/11 |
| http://38.75.82.213:999 | DO | 4361 | 2 | 3/8 |
| http://213.136.77.119:8888 | FR | 1176 | 2 | 2/2 |
| http://38.224.223.234:8080 | MX | 535 | 2 | 2/2 |
| http://201.46.86.37:8080 | MX | 4285 | 2 | 3/12 |
| http://201.71.2.24:999 | VE | 3310 | 2 | 2/2 |
| socks5://103.96.233.10:1080 | AF | 7836 | 2 | 3/12 |
| socks5://210.76.193.152:10808 | CN | 2063 | 2 | 3/10 |
| socks5://64.83.12.6:1080 | US | 5473 | 2 | 5/9 |
| socks5://147.45.60.124:1082 | US | 488 | 2 | 8/14 |
| http://45.233.90.10:443 | BR | 4785 | 1 | 1/1 |
| http://101.6.51.91:6696 | CN | 7347 | 1 | 1/1 |
| http://38.10.240.130:3128 | CO | 3433 | 1 | 4/12 |
| http://38.19.40.9:8083 | CO | 5761 | 1 | 4/6 |
| http://38.156.76.112:999 | CO | 7570 | 1 | 1/1 |
| http://38.191.194.250:999 | CO | 5115 | 1 | 1/1 |
| http://38.211.76.203:999 | CO | 2995 | 1 | 2/6 |
| http://45.167.124.69:999 | CO | 4158 | 1 | 1/1 |
| http://45.173.10.212:999 | CO | 7515 | 1 | 1/1 |
| http://177.73.155.247:999 | CO | 5751 | 1 | 1/1 |
| http://177.93.33.55:999 | CO | 1775 | 1 | 1/1 |
| http://181.78.7.222:8080 | CO | 7595 | 1 | 2/3 |
| http://181.78.17.131:999 | CO | 4990 | 1 | 2/11 |
| http://181.78.74.171:999 | CO | 691 | 1 | 1/1 |
| http://181.78.74.174:999 | CO | 673 | 1 | 1/1 |
| http://181.78.169.130:999 | CO | 1695 | 1 | 1/1 |
| http://181.78.208.227:999 | CO | 1731 | 1 | 1/1 |
| http://186.31.197.3:8080 | CO | 3169 | 1 | 2/12 |
| http://186.96.97.203:999 | CO | 2562 | 1 | 2/4 |
| http://186.96.111.214:999 | CO | 2954 | 1 | 2/3 |
| http://190.60.39.230:999 | CO | 5977 | 1 | 1/1 |
| http://190.60.61.204:999 | CO | 7398 | 1 | 2/4 |
| http://209.14.112.98:999 | CO | 7243 | 1 | 1/1 |
| http://38.44.17.142:999 | DO | 7238 | 1 | 5/7 |
| http://38.75.82.44:999 | DO | 2346 | 1 | 2/6 |
| http://45.176.99.58:999 | DO | 1337 | 1 | 5/9 |
| http://45.71.0.121:999 | EC | 3745 | 1 | 1/1 |
| http://45.71.186.212:999 | EC | 7161 | 1 | 1/1 |
| http://177.234.217.85:999 | EC | 3960 | 1 | 3/7 |
| http://177.234.217.238:999 | EC | 6385 | 1 | 1/1 |
| http://181.78.195.137:999 | EC | 6205 | 1 | 5/14 |
| http://181.78.203.148:999 | EC | 7190 | 1 | 2/12 |
| http://190.12.150.244:999 | EC | 4907 | 1 | 6/10 |
| http://200.24.148.21:999 | EC | 7158 | 1 | 1/1 |
| http://65.108.203.37:28080 | FI | 1133 | 1 | 1/1 |
| http://103.199.215.43:6262 | IN | 5391 | 1 | 1/1 |
| http://161.248.176.2:8080 | IN | 4998 | 1 | 1/1 |
| http://202.62.67.209:53281 | IN | 5797 | 1 | 1/1 |
| http://91.228.133.191:8888 | IR | 2317 | 1 | 5/14 |
| http://5.102.108.221:999 | MX | 6963 | 1 | 1/1 |
| http://45.189.60.72:999 | MX | 7953 | 1 | 1/1 |
| http://153.51.241.50:999 | MX | 7157 | 1 | 6/11 |
| http://187.251.224.167:80 | MX | 5371 | 1 | 3/10 |
| http://190.93.224.32:999 | PE | 3820 | 1 | 5/9 |
| http://200.39.153.1:999 | PE | 7072 | 1 | 2/8 |
| http://23.138.88.1:999 | PR | 6908 | 1 | 1/1 |
| http://192.203.0.166:999 | PR | 4047 | 1 | 1/1 |
| http://1.20.169.34:8080 | TH | 7930 | 1 | 1/1 |
| http://49.51.253.118:8888 | US | 1917 | 1 | 1/1 |
| http://50.200.166.130:8080 | US | 2709 | 1 | 2/11 |
| http://104.154.186.48:80 | US | 972 | 1 | 9/13 |
| http://104.194.8.103:40001 | US | 376 | 1 | 1/1 |
| http://216.106.179.216:49331 | US | 3538 | 1 | 4/13 |
| http://216.106.182.177:3128 | US | 306 | 1 | 12/14 |
| http://45.230.170.13:999 | VE | 6686 | 1 | 1/1 |
| http://201.71.2.25:999 | VE | 6960 | 1 | 1/1 |
| socks4://163.192.14.135:50161 | US | 3904 | 1 | 7/13 |
| socks4://216.106.179.216:49222 | US | 2629 | 1 | 4/12 |
| socks4://216.106.179.216:49242 | US | 6542 | 1 | 1/1 |
| socks5://159.195.61.240:1080 | DE | 7992 | 1 | 4/12 |
| socks5://45.76.164.255:1085 | US | 109 | 1 | 7/10 |
| socks5://137.131.12.103:1080 | US | 401 | 1 | 3/5 |
| socks5://147.45.60.110:1082 | US | 191 | 1 | 4/13 |
| socks5://147.45.60.250:1082 | US | 4273 | 1 | 4/14 |
| socks5://178.130.47.50:1082 | US | 1450 | 1 | 3/4 |
| socks5://216.106.179.216:49155 | US | 5046 | 1 | 1/1 |
| socks5://216.106.179.216:49340 | US | 1488 | 1 | 1/1 |
| socks5://216.106.179.216:49473 | US | 6838 | 1 | 2/10 |
