# Proxy status

Generated 2026-08-22T13:34:32Z by `harvest.py`.

- **646** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1482** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14123** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 110/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1212 |
| socks5 | 257 |
| socks4 | 13 |

| country | entries |
|---|---|
| ID | 367 |
| US | 98 |
| CO | 65 |
| PH | 65 |
| RU | 61 |
| BD | 56 |
| TR | 44 |
| MX | 42 |
| CN | 41 |
| NL | 40 |
| BR | 39 |
| IN | 38 |
| EC | 31 |
| VE | 31 |
| VN | 30 |
| DE | 29 |
| FR | 26 |
| SG | 23 |
| DO | 21 |
| EG | 21 |
| HK | 20 |
| FI | 16 |
| CL | 15 |
| IR | 15 |
| GB | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-08-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 84 | 84 | 47 | 2026-08-22 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 101 | 101 | 10 | 2026-08-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 115 | 115 | 39 | 2026-08-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 149 | 149 | 53 | 2026-08-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-08-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 151 | 151 | 46 | 2026-08-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 159 | 159 | 28 | 2026-08-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 202 | 202 | 43 | 2026-08-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-22 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 452 | 452 | 175 | 2026-08-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-08-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-08-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1128 | 2026-08-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1606 | 2026-08-22 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1919 | 1915 | 205 | 2026-08-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2066 | 2064 | 210 | 2026-08-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2522 | 2520 | 697 | 2026-08-22 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2591 | 2591 | 1989 | 2026-08-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3048 | 3046 | 2316 | 2026-08-22 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 975 | 21 | 23/24 |
| http://34.43.46.91:443 | US | 674 | 16 | 21/24 |
| http://34.43.46.91:80 | US | 640 | 16 | 21/24 |
| http://181.78.74.252:999 | CO | 694 | 15 | 15/15 |
| http://181.78.74.253:999 | CO | 682 | 15 | 15/15 |
| http://190.97.236.128:999 | VE | 582 | 14 | 14/14 |
| http://190.97.236.129:999 | VE | 588 | 14 | 14/14 |
| http://103.237.102.191:11111 | DE | 690 | 10 | 23/24 |
| http://212.58.132.5:8888 | GB | 2290 | 10 | 19/23 |
| http://1.231.81.166:3128 | KR | 1411 | 10 | 23/24 |
| http://95.211.174.135:3128 | NL | 830 | 10 | 23/24 |
| http://204.76.203.9:3128 | NL | 894 | 10 | 23/24 |
| http://204.76.203.9:8080 | NL | 528 | 10 | 16/17 |
| http://185.200.188.234:10001 | RU | 972 | 10 | 23/24 |
| http://130.110.103.245:3128 | SA | 1262 | 10 | 22/24 |
| http://202.28.194.139:31280 | TH | 1939 | 10 | 23/24 |
| http://95.3.69.222:8080 | TR | 1303 | 10 | 23/24 |
| socks5://45.144.54.40:1080 | DE | 3644 | 10 | 18/24 |
| socks5://144.91.121.61:1088 | FR | 1859 | 10 | 23/24 |
| socks5://212.58.132.5:1080 | GB | 2910 | 10 | 23/24 |
| socks5://144.24.111.128:1088 | IN | 1788 | 10 | 19/24 |
| http://87.251.77.29:3128 | DE | 1004 | 9 | 22/24 |
| http://80.241.214.192:3128 | FR | 1103 | 8 | 8/8 |
| http://185.191.239.248:3128 | CH | 2079 | 7 | 15/23 |
| http://116.196.150.180:17981 | CN | 5682 | 7 | 11/24 |
| http://13.221.202.200:3128 | US | 63 | 7 | 7/7 |
| http://199.7.149.90:3128 | US | 19 | 7 | 7/7 |
| socks5://101.36.104.46:10808 | JP | 2920 | 7 | 22/24 |
| socks5://103.75.118.84:1080 | JP | 2123 | 7 | 13/19 |
| socks5://45.43.63.37:10808 | SG | 1936 | 7 | 21/24 |
| socks5://193.25.215.182:22222 | US | 3276 | 6 | 22/24 |
| http://103.177.118.145:8118 | BD | 1660 | 5 | 5/5 |
| http://190.12.150.244:999 | EC | 3332 | 5 | 15/20 |
| http://84.36.141.180:1976 | EG | 5993 | 5 | 6/10 |
| http://41.128.90.50:1976 | EG | 7295 | 4 | 8/9 |
| http://37.58.221.247:3128 | FR | 1606 | 4 | 7/16 |
| http://103.130.61.61:8081 | ID | 7841 | 4 | 20/24 |
| http://38.194.246.34:999 | MX | 7241 | 4 | 10/15 |
| socks5://193.222.99.32:1080 | DE | 1171 | 4 | 7/9 |
| socks5://152.228.237.108:1080 | FR | 2651 | 4 | 6/9 |
| socks5://107.191.44.214:1081 | US | 4975 | 4 | 13/24 |
| socks5://147.45.60.250:1082 | US | 2385 | 4 | 11/24 |
| http://109.236.45.95:8989 | AL | 4871 | 3 | 7/20 |
| http://46.36.123.30:81 | AM | 7819 | 3 | 8/22 |
| http://138.117.13.129:999 | AR | 3940 | 3 | 5/13 |
| http://187.102.219.42:999 | AR | 2090 | 3 | 12/19 |
| http://187.49.176.141:8080 | BR | 4328 | 3 | 6/14 |
| http://8.138.217.152:21001 | CN | 3551 | 3 | 15/24 |
| http://123.60.155.1:3128 | CN | 1682 | 3 | 9/22 |
| http://223.85.21.195:8080 | CN | 4749 | 3 | 13/22 |
| http://38.156.76.112:999 | CO | 6608 | 3 | 6/11 |
| http://190.107.23.150:8080 | CO | 5039 | 3 | 5/12 |
| http://5.7.135.228:8080 | DE | 7793 | 3 | 3/3 |
| http://213.165.55.41:8080 | DE | 7751 | 3 | 3/3 |
| http://37.59.125.131:8888 | FR | 3210 | 3 | 19/24 |
| http://145.239.41.4:5060 | FR | 522 | 3 | 3/3 |
| http://186.33.0.11:999 | GT | 2022 | 3 | 6/22 |
| http://38.253.240.231:8080 | ID | 5707 | 3 | 6/22 |
| http://103.81.65.77:8080 | ID | 7068 | 3 | 7/22 |
| http://103.147.118.67:8080 | ID | 2632 | 3 | 5/12 |
| http://103.172.42.41:3128 | ID | 4056 | 3 | 6/18 |
| http://103.172.120.189:8080 | ID | 5425 | 3 | 6/20 |
| http://103.187.226.52:8082 | ID | 6613 | 3 | 4/10 |
| http://103.234.35.147:3128 | ID | 6548 | 3 | 5/13 |
| http://163.223.78.87:3127 | ID | 1623 | 3 | 3/3 |
| http://45.43.60.220:8080 | JP | 5137 | 3 | 15/23 |
| http://94.131.92.155:3128 | KZ | 1010 | 3 | 14/22 |
| http://212.154.169.90:3128 | KZ | 1157 | 3 | 3/3 |
| http://153.51.241.50:999 | MX | 1306 | 3 | 12/21 |
| http://187.251.130.143:8081 | MX | 5271 | 3 | 9/16 |
| http://175.136.239.173:8181 | MY | 4504 | 3 | 19/24 |
| http://49.144.29.132:8082 | PH | 7284 | 3 | 3/3 |
| http://112.203.207.111:8082 | PH | 2425 | 3 | 6/23 |
| http://181.94.197.37:8080 | PY | 6016 | 3 | 9/19 |
| http://152.42.167.241:3128 | SG | 6674 | 3 | 21/24 |
| http://34.94.46.8:80 | US | 369 | 3 | 18/22 |
| http://34.238.165.158:3128 | US | 66 | 3 | 3/3 |
| http://165.154.162.73:8888 | US | 1168 | 3 | 15/24 |
| http://199.7.149.96:3128 | US | 22 | 3 | 3/3 |
| http://190.114.245.194:999 | VE | 5056 | 3 | 5/18 |
| http://165.99.14.18:5566 | VN | 3367 | 3 | 3/3 |
| http://102.218.41.98:8082 | ZA | 6714 | 3 | 7/13 |
| socks5://31.25.236.95:1080 | DE | 5674 | 3 | 4/8 |
| socks5://77.239.106.24:1080 | DE | 6822 | 3 | 8/9 |
| socks5://150.241.70.126:1080 | FI | 4008 | 3 | 3/3 |
| socks5://152.32.168.221:10808 | HK | 1407 | 3 | 9/13 |
| socks5://103.142.255.33:69 | ID | 5074 | 3 | 6/17 |
| socks5://109.73.181.237:7080 | IT | 2008 | 3 | 5/16 |
| socks5://149.62.186.244:1080 | IT | 5243 | 3 | 20/24 |
| socks5://202.79.27.12:1080 | KH | 5044 | 3 | 5/14 |
| socks5://161.35.90.93:1082 | NL | 2235 | 3 | 11/24 |
| socks5://85.198.82.207:1080 | RU | 4423 | 3 | 8/13 |
| socks5://34.229.113.62:1080 | US | 2132 | 3 | 13/17 |
| http://187.102.219.32:999 | AR | 3446 | 2 | 6/23 |
| http://103.109.96.129:2610 | BD | 1630 | 2 | 3/4 |
| http://103.142.69.62:8080 | BD | 2994 | 2 | 7/22 |
| http://103.147.230.130:8090 | BD | 4228 | 2 | 6/14 |
| http://103.170.185.162:46 | BD | 5690 | 2 | 3/12 |
| http://190.124.252.129:6666 | BR | 7357 | 2 | 2/2 |
| http://38.7.195.52:999 | CL | 4041 | 2 | 3/6 |
