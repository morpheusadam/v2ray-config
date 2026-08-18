# Proxy status

Generated 2026-08-18T13:46:42Z by `harvest.py`.

- **596** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1002** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13385** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 150/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 772 |
| socks5 | 210 |
| socks4 | 20 |

| country | entries |
|---|---|
| ID | 203 |
| US | 91 |
| CO | 51 |
| CN | 46 |
| PH | 44 |
| RU | 43 |
| MX | 33 |
| BD | 29 |
| NL | 26 |
| BR | 25 |
| DE | 24 |
| FR | 24 |
| VE | 24 |
| TR | 22 |
| SG | 21 |
| VN | 21 |
| EC | 17 |
| HK | 17 |
| JP | 15 |
| GB | 14 |
| DO | 12 |
| IN | 12 |
| KH | 12 |
| TH | 12 |
| AR | 10 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-08-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 65 | 65 | 37 | 2026-08-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 89 | 89 | 46 | 2026-08-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 102 | 102 | 14 | 2026-08-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 117 | 117 | 32 | 2026-08-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 120 | 120 | 26 | 2026-08-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 130 | 130 | 50 | 2026-08-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 139 | 139 | 72 | 2026-08-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-08-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 259 | 259 | 115 | 2026-08-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-08-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-08-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1134 | 2026-08-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1618 | 2026-08-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1929 | 1925 | 415 | 2026-08-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2207 | 2205 | 180 | 2026-08-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2351 | 2351 | 1963 | 2026-08-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2709 | 2707 | 683 | 2026-08-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3080 | 3078 | 2519 | 2026-08-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 4283 | 16 | 16/16 |
| http://64.112.184.210:3128 | US | 386 | 16 | 16/16 |
| socks5://69.55.49.177:38182 | US | 1067 | 16 | 16/16 |
| http://181.39.25.196:8118 | EC | 944 | 13 | 15/16 |
| http://190.0.246.210:4040 | CO | 5240 | 12 | 14/15 |
| http://14.139.235.82:3128 | IN | 2773 | 8 | 13/16 |
| http://34.43.46.91:443 | US | 1979 | 8 | 13/16 |
| http://34.43.46.91:80 | US | 1486 | 8 | 13/16 |
| http://181.78.74.252:999 | CO | 784 | 7 | 7/7 |
| http://181.78.74.253:999 | CO | 788 | 7 | 7/7 |
| http://157.230.178.216:40000 | US | 1158 | 7 | 14/15 |
| socks5://147.45.60.139:1082 | US | 4376 | 7 | 7/7 |
| http://174.137.134.182:2999 | US | 4929 | 6 | 14/15 |
| http://190.97.236.128:999 | VE | 749 | 6 | 6/6 |
| http://190.97.236.129:999 | VE | 750 | 6 | 6/6 |
| http://186.33.45.219:999 | EC | 3489 | 5 | 5/5 |
| http://200.59.191.27:999 | VE | 3590 | 5 | 9/11 |
| http://213.136.77.119:8888 | FR | 1181 | 4 | 4/4 |
| socks5://103.96.233.10:1080 | AF | 2057 | 4 | 5/14 |
| http://181.78.7.222:8080 | CO | 2161 | 3 | 4/5 |
| http://181.78.203.148:999 | EC | 2597 | 3 | 4/14 |
| http://190.12.150.244:999 | EC | 6132 | 3 | 8/12 |
| http://153.51.241.50:999 | MX | 2851 | 3 | 8/13 |
| http://49.51.253.118:8888 | US | 1370 | 3 | 3/3 |
| http://104.194.8.103:40001 | US | 333 | 3 | 3/3 |
| socks4://163.192.14.135:50161 | US | 649 | 3 | 9/15 |
| socks5://147.45.60.110:1082 | US | 3359 | 3 | 6/15 |
| socks5://147.45.60.250:1082 | US | 4369 | 3 | 6/16 |
| socks5://178.130.47.50:1082 | US | 2374 | 3 | 5/6 |
| http://191.252.219.129:8889 | BR | 1514 | 2 | 2/2 |
| http://201.71.24.65:8082 | BR | 5336 | 2 | 3/5 |
| http://8.138.217.152:21001 | CN | 5623 | 2 | 9/16 |
| http://47.107.82.96:30051 | CN | 4186 | 2 | 7/9 |
| http://47.121.139.13:3128 | CN | 2283 | 2 | 7/15 |
| http://101.206.186.99:8080 | CN | 4072 | 2 | 11/16 |
| http://101.251.204.174:8080 | CN | 2142 | 2 | 2/2 |
| http://112.74.101.87:9999 | CN | 6113 | 2 | 5/6 |
| http://114.94.148.37:18080 | CN | 1139 | 2 | 12/15 |
| http://120.24.202.132:19000 | CN | 1830 | 2 | 5/10 |
| http://123.57.94.90:8888 | CN | 5932 | 2 | 6/14 |
| http://123.57.213.24:3539 | CN | 6351 | 2 | 9/15 |
| http://223.85.21.195:8080 | CN | 1695 | 2 | 7/14 |
| http://45.179.200.38:999 | CO | 5870 | 2 | 2/2 |
| http://181.204.190.234:999 | CO | 1977 | 2 | 3/5 |
| http://85.234.100.149:8080 | DE | 1667 | 2 | 6/12 |
| http://103.237.102.191:11111 | DE | 831 | 2 | 15/16 |
| http://200.107.206.9:999 | DO | 639 | 2 | 4/8 |
| http://45.236.107.106:808 | EC | 7439 | 2 | 3/15 |
| http://205.235.1.37:999 | EC | 3734 | 2 | 5/7 |
| http://196.204.83.229:8080 | EG | 6364 | 2 | 6/13 |
| http://80.78.128.94:8080 | ES | 4906 | 2 | 3/5 |
| http://37.59.125.131:8888 | FR | 1101 | 2 | 13/16 |
| http://191.44.125.11:8080 | FR | 5374 | 2 | 3/14 |
| http://18.170.25.193:57422 | GB | 2531 | 2 | 6/12 |
| http://212.58.132.5:8888 | GB | 5406 | 2 | 11/15 |
| http://200.119.141.114:999 | GT | 1250 | 2 | 3/5 |
| http://176.111.37.5:39811 | HK | 1702 | 2 | 15/16 |
| http://176.111.37.216:39811 | HK | 1831 | 2 | 14/16 |
| http://164.163.74.97:999 | HN | 5730 | 2 | 4/9 |
| http://95.214.123.140:8080 | HU | 4210 | 2 | 2/2 |
| http://45.126.250.34:8080 | ID | 4366 | 2 | 3/14 |
| http://103.61.16.92:8080 | ID | 7384 | 2 | 5/13 |
| http://103.110.100.25:1111 | ID | 6771 | 2 | 5/14 |
| http://103.118.102.98:80 | ID | 6574 | 2 | 3/9 |
| http://103.126.119.110:8080 | ID | 5542 | 2 | 5/14 |
| http://103.147.134.114:8082 | ID | 6632 | 2 | 2/2 |
| http://103.155.64.250:8080 | ID | 7576 | 2 | 6/14 |
| http://103.165.157.247:8090 | ID | 4006 | 2 | 4/14 |
| http://103.166.33.54:8080 | ID | 1673 | 2 | 3/9 |
| http://103.172.42.193:1111 | ID | 2373 | 2 | 5/13 |
| http://103.172.70.203:8080 | ID | 2468 | 2 | 2/2 |
| http://103.175.237.232:8080 | ID | 7148 | 2 | 3/5 |
| http://103.176.96.32:8082 | ID | 4396 | 2 | 3/9 |
| http://103.176.97.57:8082 | ID | 2448 | 2 | 4/5 |
| http://103.178.3.140:8818 | ID | 4087 | 2 | 3/5 |
| http://103.179.252.229:1111 | ID | 3588 | 2 | 4/6 |
| http://103.189.249.210:8080 | ID | 3754 | 2 | 3/4 |
| http://103.236.143.55:8080 | ID | 5189 | 2 | 4/9 |
| http://103.245.16.134:8080 | ID | 4755 | 2 | 5/9 |
| http://110.76.147.31:8080 | ID | 2607 | 2 | 4/12 |
| http://157.20.128.141:8080 | ID | 7220 | 2 | 2/2 |
| http://160.19.145.103:3127 | ID | 6795 | 2 | 3/6 |
| http://160.20.39.3:3125 | ID | 2538 | 2 | 4/6 |
| http://160.187.174.121:8080 | ID | 5151 | 2 | 6/12 |
| http://161.248.226.7:80 | ID | 6985 | 2 | 5/15 |
| http://202.52.48.42:4444 | ID | 1610 | 2 | 6/16 |
| http://202.58.77.7:7777 | ID | 4567 | 2 | 3/4 |
| http://117.236.124.166:3128 | IN | 1871 | 2 | 9/16 |
| http://164.52.216.18:8080 | IN | 1303 | 2 | 3/10 |
| http://46.209.15.187:8080 | IR | 6935 | 2 | 2/2 |
| http://102.213.179.210:8080 | KE | 2789 | 2 | 4/5 |
| http://1.231.81.166:3128 | KR | 2159 | 2 | 15/16 |
| http://94.131.92.155:3128 | KZ | 7388 | 2 | 8/14 |
| http://154.73.28.49:8080 | LY | 3207 | 2 | 2/2 |
| http://187.243.251.254:999 | MX | 564 | 2 | 4/8 |
| http://175.136.239.173:8181 | MY | 3699 | 2 | 12/16 |
| http://175.136.239.174:8181 | MY | 2973 | 2 | 9/16 |
| http://175.143.76.177:8181 | MY | 2987 | 2 | 13/16 |
| http://102.134.19.170:8080 | NG | 5112 | 2 | 4/7 |
| http://95.211.174.135:3128 | NL | 1201 | 2 | 15/16 |
