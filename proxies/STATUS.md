# Proxy status

Generated 2026-08-21T19:54:34Z by `harvest.py`.

- **918** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1437** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13777** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 215/600 (36%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1157 |
| socks5 | 262 |
| socks4 | 18 |

| country | entries |
|---|---|
| ID | 353 |
| US | 101 |
| CO | 56 |
| PH | 54 |
| RU | 54 |
| BD | 51 |
| CN | 46 |
| TR | 41 |
| BR | 37 |
| MX | 36 |
| IN | 35 |
| NL | 35 |
| FR | 34 |
| EC | 31 |
| SG | 28 |
| VN | 27 |
| DE | 26 |
| VE | 26 |
| EG | 22 |
| HK | 21 |
| DO | 19 |
| JP | 14 |
| PK | 14 |
| AU | 13 |
| GB | 12 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-08-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 92 | 92 | 52 | 2026-08-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-08-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 114 | 114 | 42 | 2026-08-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 115 | 115 | 16 | 2026-08-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 116 | 116 | 28 | 2026-08-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-08-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 171 | 171 | 80 | 2026-08-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 172 | 172 | 18 | 2026-08-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 206 | 206 | 42 | 2026-08-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 541 | 541 | 231 | 2026-08-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-08-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 456 | 2026-08-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1148 | 2026-08-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1607 | 2026-08-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1901 | 1897 | 162 | 2026-08-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2208 | 2206 | 229 | 2026-08-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2467 | 2467 | 1919 | 2026-08-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2628 | 2626 | 646 | 2026-08-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2865 | 2863 | 2194 | 2026-08-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 959 | 20 | 22/23 |
| http://34.43.46.91:443 | US | 540 | 15 | 20/23 |
| http://34.43.46.91:80 | US | 480 | 15 | 20/23 |
| http://181.78.74.252:999 | CO | 660 | 14 | 14/14 |
| http://181.78.74.253:999 | CO | 685 | 14 | 14/14 |
| http://190.97.236.128:999 | VE | 679 | 13 | 13/13 |
| http://190.97.236.129:999 | VE | 593 | 13 | 13/13 |
| http://47.107.82.96:30051 | CN | 1919 | 9 | 14/16 |
| http://103.237.102.191:11111 | DE | 554 | 9 | 22/23 |
| http://212.58.132.5:8888 | GB | 1539 | 9 | 18/22 |
| http://1.231.81.166:3128 | KR | 1356 | 9 | 22/23 |
| http://95.211.174.135:3128 | NL | 976 | 9 | 22/23 |
| http://204.76.203.9:3128 | NL | 757 | 9 | 22/23 |
| http://204.76.203.9:8080 | NL | 533 | 9 | 15/16 |
| http://185.200.188.234:10001 | RU | 5906 | 9 | 22/23 |
| http://130.110.103.245:3128 | SA | 1386 | 9 | 21/23 |
| http://202.28.194.139:31280 | TH | 3269 | 9 | 22/23 |
| http://95.3.69.222:8080 | TR | 1237 | 9 | 22/23 |
| http://45.66.249.187:3128 | US | 752 | 9 | 13/14 |
| http://45.66.249.187:8181 | US | 362 | 9 | 13/14 |
| socks5://45.144.54.40:1080 | DE | 5668 | 9 | 17/23 |
| socks5://144.91.121.61:1088 | FR | 2602 | 9 | 22/23 |
| socks5://212.58.132.5:1080 | GB | 2353 | 9 | 22/23 |
| socks5://144.24.111.128:1088 | IN | 1559 | 9 | 18/23 |
| socks5://178.128.82.131:10808 | SG | 2269 | 9 | 14/23 |
| http://87.251.77.29:3128 | DE | 851 | 8 | 21/23 |
| http://80.241.214.192:3128 | FR | 2206 | 7 | 7/7 |
| http://185.191.239.248:3128 | CH | 542 | 6 | 14/22 |
| http://116.196.150.180:17981 | CN | 1938 | 6 | 10/23 |
| http://13.221.202.200:3128 | US | 618 | 6 | 6/6 |
| http://98.83.197.228:3128 | US | 356 | 6 | 6/6 |
| http://199.7.149.90:3128 | US | 30 | 6 | 6/6 |
| socks5://101.36.104.46:10808 | JP | 2887 | 6 | 21/23 |
| socks5://103.75.118.84:1080 | JP | 3657 | 6 | 12/18 |
| socks5://121.169.46.116:1090 | KR | 5533 | 6 | 16/23 |
| socks5://45.43.63.37:10808 | SG | 3332 | 6 | 20/23 |
| http://45.71.0.121:999 | EC | 7490 | 5 | 7/10 |
| socks5://193.25.215.182:22222 | US | 1242 | 5 | 21/23 |
| http://103.161.69.252:2698 | BD | 5169 | 4 | 11/23 |
| http://103.177.118.145:8118 | BD | 1579 | 4 | 4/4 |
| http://190.12.150.244:999 | EC | 7319 | 4 | 14/19 |
| http://41.196.16.233:1981 | EG | 6054 | 4 | 6/8 |
| http://84.36.141.180:1976 | EG | 1941 | 4 | 5/9 |
| http://190.0.246.210:4040 | CO | 526 | 3 | 20/22 |
| http://190.0.246.211:4040 | CO | 911 | 3 | 22/23 |
| http://41.128.90.50:1976 | EG | 3854 | 3 | 7/8 |
| http://37.58.221.247:3128 | FR | 647 | 3 | 6/15 |
| http://101.255.107.122:1111 | ID | 2519 | 3 | 3/3 |
| http://103.130.61.61:8081 | ID | 1454 | 3 | 19/23 |
| http://103.203.234.103:8080 | ID | 5551 | 3 | 6/22 |
| http://38.194.246.34:999 | MX | 5467 | 3 | 9/14 |
| http://195.226.213.251:8888 | UA | 3865 | 3 | 7/17 |
| http://156.238.250.51:8080 | US | 4213 | 3 | 11/18 |
| socks5://38.49.210.79:40000 | CA | 325 | 3 | 12/23 |
| socks5://45.95.232.35:1080 | CH | 6639 | 3 | 10/23 |
| socks5://193.222.99.32:1080 | DE | 1201 | 3 | 6/8 |
| socks5://152.228.237.108:1080 | FR | 4948 | 3 | 5/8 |
| socks5://43.164.3.124:1080 | TH | 4079 | 3 | 14/22 |
| socks5://107.191.44.214:1081 | US | 2158 | 3 | 12/23 |
| socks5://141.148.158.143:1080 | US | 4490 | 3 | 11/22 |
| socks5://147.45.60.124:1082 | US | 361 | 3 | 13/23 |
| socks5://147.45.60.250:1082 | US | 4511 | 3 | 10/23 |
| socks5://216.106.179.216:49231 | US | 2454 | 3 | 3/3 |
| http://109.236.45.95:8989 | AL | 2085 | 2 | 6/19 |
| http://46.36.123.30:81 | AM | 5824 | 2 | 7/21 |
| http://138.117.13.129:999 | AR | 7707 | 2 | 4/12 |
| http://168.194.34.196:9001 | AR | 1215 | 2 | 7/21 |
| http://187.102.219.42:999 | AR | 6226 | 2 | 11/18 |
| http://103.81.175.146:22311 | BD | 5490 | 2 | 2/2 |
| http://103.138.123.196:8090 | BD | 3822 | 2 | 4/20 |
| http://113.11.120.105:30226 | BD | 6974 | 2 | 6/22 |
| http://182.160.124.174:9669 | BD | 5822 | 2 | 5/22 |
| http://45.180.84.105:443 | BR | 2390 | 2 | 7/17 |
| http://138.0.207.246:8082 | BR | 1923 | 2 | 4/8 |
| http://177.44.182.128:8088 | BR | 3016 | 2 | 2/2 |
| http://187.49.176.141:8080 | BR | 5257 | 2 | 5/13 |
| http://201.23.119.74:3128 | BR | 7818 | 2 | 3/8 |
| http://1.15.53.214:8888 | CN | 1926 | 2 | 7/17 |
| http://8.138.217.152:21001 | CN | 2855 | 2 | 14/23 |
| http://58.254.153.146:17981 | CN | 1638 | 2 | 10/21 |
| http://114.236.137.41:21000 | CN | 1812 | 2 | 15/23 |
| http://120.92.111.242:15010 | CN | 3213 | 2 | 8/19 |
| http://120.232.115.170:17981 | CN | 1749 | 2 | 11/22 |
| http://123.60.155.1:3128 | CN | 3683 | 2 | 8/21 |
| http://223.85.21.195:8080 | CN | 2685 | 2 | 12/21 |
| http://38.156.76.112:999 | CO | 2209 | 2 | 5/10 |
| http://38.211.76.203:999 | CO | 613 | 2 | 6/15 |
| http://181.225.107.53:999 | CO | 6104 | 2 | 7/23 |
| http://190.14.224.244:999 | CO | 3886 | 2 | 3/14 |
| http://190.60.61.202:999 | CO | 6964 | 2 | 2/2 |
| http://190.107.23.150:8080 | CO | 6645 | 2 | 4/11 |
| http://200.10.30.5:8083 | CO | 6359 | 2 | 8/12 |
| http://200.10.31.45:8081 | CO | 4971 | 2 | 10/20 |
| http://201.234.186.225:999 | CO | 7495 | 2 | 5/18 |
| http://5.7.135.228:8080 | DE | 2252 | 2 | 2/2 |
| http://86.53.111.249:8080 | DE | 532 | 2 | 3/6 |
| http://213.165.55.41:8080 | DE | 623 | 2 | 2/2 |
| http://38.44.17.142:999 | DO | 2621 | 2 | 9/16 |
| http://186.5.94.216:999 | EC | 893 | 2 | 6/23 |
| http://41.128.90.50:1981 | EG | 2590 | 2 | 4/6 |
