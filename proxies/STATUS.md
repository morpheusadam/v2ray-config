# Proxy status

Generated 2026-08-22T19:53:53Z by `harvest.py`.

- **621** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1436** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14061** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 144/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1167 |
| socks5 | 251 |
| socks4 | 18 |

| country | entries |
|---|---|
| ID | 346 |
| US | 91 |
| PH | 65 |
| CO | 62 |
| RU | 54 |
| BD | 50 |
| CN | 41 |
| NL | 41 |
| TR | 41 |
| MX | 39 |
| BR | 32 |
| IN | 32 |
| EC | 31 |
| VN | 30 |
| VE | 29 |
| FR | 28 |
| SG | 28 |
| DE | 26 |
| EG | 24 |
| DO | 21 |
| HK | 20 |
| IR | 19 |
| FI | 18 |
| KH | 16 |
| CL | 14 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-08-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 80 | 80 | 10 | 2026-08-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 92 | 92 | 44 | 2026-08-22 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 105 | 105 | 54 | 2026-08-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-08-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 164 | 164 | 68 | 2026-08-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 170 | 170 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 188 | 188 | 56 | 2026-08-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 208 | 208 | 80 | 2026-08-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 276 | 276 | 94 | 2026-08-22 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-08-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-08-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1143 | 2026-08-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1600 | 2026-08-22 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1912 | 1908 | 270 | 2026-08-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2264 | 2262 | 189 | 2026-08-22 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2563 | 2563 | 1892 | 2026-08-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2753 | 2751 | 654 | 2026-08-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3016 | 3014 | 2240 | 2026-08-22 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 916 | 22 | 24/25 |
| http://34.43.46.91:443 | US | 776 | 17 | 22/25 |
| http://34.43.46.91:80 | US | 877 | 17 | 22/25 |
| http://181.78.74.252:999 | CO | 667 | 16 | 16/16 |
| http://181.78.74.253:999 | CO | 674 | 16 | 16/16 |
| http://190.97.236.128:999 | VE | 589 | 15 | 15/15 |
| http://190.97.236.129:999 | VE | 589 | 15 | 15/15 |
| http://103.237.102.191:11111 | DE | 783 | 11 | 24/25 |
| http://212.58.132.5:8888 | GB | 2380 | 11 | 20/24 |
| http://1.231.81.166:3128 | KR | 1164 | 11 | 24/25 |
| http://95.211.174.135:3128 | NL | 924 | 11 | 24/25 |
| http://204.76.203.9:3128 | NL | 756 | 11 | 24/25 |
| http://204.76.203.9:8080 | NL | 513 | 11 | 17/18 |
| http://185.200.188.234:10001 | RU | 1344 | 11 | 24/25 |
| http://130.110.103.245:3128 | SA | 3358 | 11 | 23/25 |
| http://202.28.194.139:31280 | TH | 2006 | 11 | 24/25 |
| http://95.3.69.222:8080 | TR | 1377 | 11 | 24/25 |
| socks5://144.91.121.61:1088 | FR | 1612 | 11 | 24/25 |
| socks5://144.24.111.128:1088 | IN | 1782 | 11 | 20/25 |
| http://87.251.77.29:3128 | DE | 6083 | 10 | 23/25 |
| http://116.196.150.180:17981 | CN | 1842 | 8 | 12/25 |
| http://13.221.202.200:3128 | US | 62 | 8 | 8/8 |
| http://199.7.149.90:3128 | US | 494 | 8 | 8/8 |
| socks5://101.36.104.46:10808 | JP | 1276 | 8 | 23/25 |
| socks5://103.75.118.84:1080 | JP | 3163 | 8 | 14/20 |
| socks5://45.43.63.37:10808 | SG | 6464 | 8 | 22/25 |
| socks5://193.25.215.182:22222 | US | 924 | 7 | 23/25 |
| http://103.177.118.145:8118 | BD | 1591 | 6 | 6/6 |
| http://190.12.150.244:999 | EC | 3645 | 6 | 16/21 |
| http://84.36.141.180:1976 | EG | 5434 | 6 | 7/11 |
| http://41.128.90.50:1976 | EG | 1303 | 5 | 9/10 |
| socks5://193.222.99.32:1080 | DE | 1837 | 5 | 8/10 |
| socks5://152.228.237.108:1080 | FR | 1580 | 5 | 7/10 |
| http://109.236.45.95:8989 | AL | 4160 | 4 | 8/21 |
| http://138.117.13.129:999 | AR | 7617 | 4 | 6/14 |
| http://187.102.219.42:999 | AR | 1088 | 4 | 13/20 |
| http://187.49.176.141:8080 | BR | 5834 | 4 | 7/15 |
| http://8.138.217.152:21001 | CN | 2233 | 4 | 16/25 |
| http://223.85.21.195:8080 | CN | 4832 | 4 | 14/23 |
| http://38.253.240.231:8080 | ID | 5389 | 4 | 7/23 |
| http://94.131.92.155:3128 | KZ | 1121 | 4 | 15/23 |
| http://153.51.241.50:999 | MX | 2585 | 4 | 13/22 |
| http://152.42.167.241:3128 | SG | 1478 | 4 | 22/25 |
| http://34.238.165.158:3128 | US | 63 | 4 | 4/4 |
| http://165.154.162.73:8888 | US | 1175 | 4 | 16/25 |
| http://199.7.149.96:3128 | US | 679 | 4 | 4/4 |
| socks5://77.239.106.24:1080 | DE | 6058 | 4 | 9/10 |
| socks5://103.142.255.33:69 | ID | 1891 | 4 | 7/18 |
| socks5://161.35.90.93:1082 | NL | 4117 | 4 | 12/25 |
| socks5://85.198.82.207:1080 | RU | 1904 | 4 | 9/14 |
| socks5://34.229.113.62:1080 | US | 5791 | 4 | 14/18 |
| http://45.186.6.104:3128 | EC | 708 | 3 | 3/3 |
| http://45.239.48.102:999 | EC | 4962 | 3 | 8/19 |
| http://186.33.45.219:999 | EC | 3528 | 3 | 11/14 |
| http://82.102.11.164:3460 | GB | 875 | 3 | 14/25 |
| http://101.47.75.240:5000 | HK | 1142 | 3 | 3/3 |
| http://176.111.37.216:39811 | HK | 758 | 3 | 22/25 |
| http://103.149.194.23:32650 | IN | 7610 | 3 | 3/3 |
| http://103.169.154.4:83 | IN | 4038 | 3 | 5/24 |
| http://117.236.124.166:3128 | IN | 3792 | 3 | 16/25 |
| http://91.228.133.191:8888 | IR | 2068 | 3 | 10/25 |
| http://72.56.109.88:3128 | NL | 475 | 3 | 6/23 |
| http://153.80.240.37:8080 | NL | 5578 | 3 | 17/25 |
| http://112.198.52.194:8080 | PH | 5100 | 3 | 7/24 |
| http://112.207.169.6:8082 | PH | 4028 | 3 | 7/24 |
| http://70.34.249.28:2001 | PL | 2929 | 3 | 3/3 |
| http://109.94.1.23:4050 | RU | 4276 | 3 | 18/25 |
| http://43.160.242.118:3128 | SG | 2801 | 3 | 18/22 |
| http://78.26.146.16:443 | UA | 6233 | 3 | 8/23 |
| http://44.193.20.213:443 | US | 560 | 3 | 3/3 |
| http://45.26.30.144:8888 | US | 575 | 3 | 7/24 |
| http://47.252.52.58:8081 | US | 3188 | 3 | 3/3 |
| http://64.112.184.210:3128 | US | 632 | 3 | 24/25 |
| socks5://213.136.92.91:1080 | FR | 5720 | 3 | 15/25 |
| socks5://45.196.218.123:1080 | HK | 1450 | 3 | 3/3 |
| socks5://123.58.219.171:10808 | HK | 4588 | 3 | 19/25 |
| socks5://171.22.182.164:1080 | IT | 1887 | 3 | 3/3 |
| socks5://101.36.104.239:10808 | JP | 3733 | 3 | 20/25 |
| socks5://144.124.232.204:1080 | NL | 986 | 3 | 7/22 |
| socks5://45.95.202.92:10808 | RU | 1147 | 3 | 3/3 |
| socks5://109.111.79.212:1080 | RU | 2980 | 3 | 3/3 |
| socks5://79.76.59.115:1080 | SE | 1789 | 3 | 6/15 |
| socks5://168.253.92.93:10808 | ZA | 5690 | 3 | 6/23 |
| http://43.231.78.203:8080 | BD | 4575 | 2 | 4/15 |
| http://103.134.27.129:8080 | BD | 4937 | 2 | 5/13 |
| http://103.141.174.38:11411 | BD | 6877 | 2 | 4/9 |
| http://179.48.25.1:8095 | BR | 2807 | 2 | 9/20 |
| http://186.226.167.191:3128 | BR | 6437 | 2 | 4/15 |
| http://167.249.29.218:999 | CL | 7197 | 2 | 2/2 |
| http://45.172.218.67:3028 | CO | 4510 | 2 | 6/15 |
| http://177.93.33.55:999 | CO | 5126 | 2 | 4/12 |
| http://181.78.7.219:8080 | CO | 4629 | 2 | 3/4 |
| http://200.69.83.203:999 | CO | 3164 | 2 | 2/2 |
| http://38.50.165.123:999 | DO | 2725 | 2 | 6/10 |
| http://67.215.226.71:999 | DO | 6225 | 2 | 4/17 |
| http://45.71.0.1:999 | EC | 2355 | 2 | 3/8 |
| http://45.239.48.100:999 | EC | 2612 | 2 | 2/2 |
| http://205.235.1.38:999 | EC | 3016 | 2 | 5/11 |
| http://41.33.60.42:8081 | EG | 4058 | 2 | 4/23 |
| http://41.65.236.37:8080 | EG | 1888 | 2 | 6/7 |
