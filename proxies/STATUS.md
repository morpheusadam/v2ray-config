# Proxy status

Generated 2026-08-14T14:16:31Z by `harvest.py`.

- **424** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **802** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11736** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 192/600 (32%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 592 |
| socks5 | 196 |
| socks4 | 14 |

| country | entries |
|---|---|
| ID | 168 |
| US | 66 |
| RU | 43 |
| VN | 40 |
| CN | 36 |
| NL | 31 |
| PH | 28 |
| FR | 27 |
| BD | 24 |
| CO | 21 |
| DE | 21 |
| SG | 20 |
| TR | 19 |
| JP | 17 |
| VE | 17 |
| MX | 16 |
| BR | 15 |
| IN | 15 |
| HK | 12 |
| TH | 11 |
| DO | 10 |
| FI | 10 |
| CL | 8 |
| EC | 7 |
| KH | 7 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 1 | 2026-08-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 93 | 93 | 44 | 2026-08-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 98 | 98 | 23 | 2026-08-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 99 | 99 | 68 | 2026-08-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 118 | 118 | 13 | 2026-08-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 119 | 119 | 42 | 2026-08-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 85 | 2026-08-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 163 | 163 | 29 | 2026-08-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 167 | 167 | 97 | 2026-08-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 394 | 394 | 210 | 2026-08-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 532 | 2026-08-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-08-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1137 | 2026-08-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1625 | 2026-08-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1945 | 1941 | 0 | 2026-08-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2147 | 2145 | 172 | 2026-08-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2378 | 2378 | 1871 | 2026-08-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2697 | 2695 | 709 | 2026-08-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2806 | 2804 | 2440 | 2026-08-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1393 | 8 | 8/8 |
| http://87.251.77.29:3128 | DE | 853 | 8 | 8/8 |
| http://103.237.102.191:11111 | DE | 738 | 8 | 8/8 |
| http://43.99.100.108:3128 | HK | 1442 | 8 | 8/8 |
| http://176.111.37.5:39811 | HK | 2855 | 8 | 8/8 |
| http://176.111.37.216:39811 | HK | 1161 | 8 | 8/8 |
| http://103.130.61.61:8081 | ID | 7881 | 8 | 8/8 |
| http://1.231.81.166:3128 | KR | 1465 | 8 | 8/8 |
| http://95.211.64.139:8889 | NL | 760 | 8 | 8/8 |
| http://95.211.174.135:3128 | NL | 1107 | 8 | 8/8 |
| http://204.76.203.9:3128 | NL | 953 | 8 | 8/8 |
| http://185.200.188.234:10001 | RU | 1176 | 8 | 8/8 |
| http://152.42.167.241:3128 | SG | 1740 | 8 | 8/8 |
| http://202.28.194.139:31280 | TH | 1890 | 8 | 8/8 |
| http://95.3.69.222:8080 | TR | 1573 | 8 | 8/8 |
| http://43.153.82.179:8888 | US | 672 | 8 | 8/8 |
| http://64.112.184.210:3128 | US | 210 | 8 | 8/8 |
| socks5://66.163.118.99:10006 | ES | 1758 | 8 | 8/8 |
| socks5://144.91.121.61:1088 | FR | 3377 | 8 | 8/8 |
| socks5://212.58.132.5:1080 | GB | 1692 | 8 | 8/8 |
| socks5://123.58.219.171:10808 | HK | 2419 | 8 | 8/8 |
| socks5://66.163.119.55:10006 | IT | 1827 | 8 | 8/8 |
| socks5://149.62.186.244:1080 | IT | 3971 | 8 | 8/8 |
| socks5://101.36.104.46:10808 | JP | 2961 | 8 | 8/8 |
| socks5://101.36.104.239:10808 | JP | 1552 | 8 | 8/8 |
| socks5://193.233.218.213:1080 | RU | 1045 | 8 | 8/8 |
| socks5://69.55.49.177:38182 | US | 1146 | 8 | 8/8 |
| socks5://193.25.215.182:22222 | US | 1351 | 8 | 8/8 |
| http://185.191.239.248:3128 | CH | 571 | 7 | 7/7 |
| http://95.211.64.139:8887 | NL | 2561 | 7 | 7/7 |
| http://157.230.178.216:40000 | US | 1464 | 7 | 7/7 |
| http://174.137.134.182:2999 | US | 3892 | 7 | 7/7 |
| http://153.80.240.37:8080 | NL | 1691 | 6 | 7/8 |
| http://34.94.46.8:80 | US | 343 | 6 | 6/6 |
| socks5://161.35.90.93:1081 | NL | 2395 | 6 | 7/8 |
| socks5://161.35.90.93:1082 | NL | 2914 | 6 | 7/8 |
| socks5://45.43.63.37:10808 | SG | 2552 | 6 | 7/8 |
| http://181.39.25.196:8118 | EC | 857 | 5 | 7/8 |
| http://130.110.103.245:3128 | SA | 1179 | 5 | 7/8 |
| http://43.160.242.118:3128 | SG | 4238 | 5 | 5/5 |
| socks5://51.159.97.242:10006 | FR | 5778 | 5 | 7/8 |
| socks5://109.199.105.194:1080 | FR | 1982 | 5 | 5/5 |
| socks5://43.164.136.189:1080 | KR | 1852 | 5 | 6/8 |
| socks5://45.10.42.68:1080 | NL | 2704 | 5 | 5/5 |
| socks5://5.249.165.195:20000 | US | 813 | 5 | 5/5 |
| socks5://204.152.192.13:1080 | US | 5475 | 5 | 5/5 |
| http://114.94.148.37:18080 | CN | 2992 | 4 | 6/7 |
| http://190.0.246.210:4040 | CO | 1071 | 4 | 6/7 |
| http://190.12.150.244:999 | EC | 4929 | 4 | 4/4 |
| http://37.59.125.131:8888 | FR | 937 | 4 | 7/8 |
| http://82.102.11.164:3460 | GB | 1267 | 4 | 7/8 |
| http://103.28.112.172:3125 | ID | 4765 | 4 | 4/4 |
| http://160.187.174.121:8080 | ID | 3718 | 4 | 4/4 |
| http://45.43.60.220:8080 | JP | 6393 | 4 | 6/7 |
| http://205.164.192.115:999 | MX | 1915 | 4 | 5/6 |
| http://95.211.64.139:8886 | NL | 515 | 4 | 4/4 |
| http://43.156.114.4:80 | SG | 1183 | 4 | 4/4 |
| http://209.7.244.3:5999 | US | 2302 | 4 | 4/4 |
| http://216.106.182.177:3128 | US | 554 | 4 | 7/8 |
| http://216.125.22.2:5999 | US | 2191 | 4 | 4/4 |
| http://113.160.132.26:8080 | VN | 1778 | 4 | 7/8 |
| http://163.181.207.169:9999 | VN | 1476 | 4 | 5/6 |
| socks4://151.115.99.193:10006 | PL | 1213 | 4 | 6/8 |
| socks4://45.61.129.165:9050 | US | 1638 | 4 | 6/8 |
| socks5://213.136.92.91:1080 | FR | 764 | 4 | 5/8 |
| socks5://47.250.211.53:1080 | MY | 1727 | 4 | 7/8 |
| http://91.92.143.148:80 | CH | 579 | 3 | 3/3 |
| http://123.57.0.163:8888 | CN | 6473 | 3 | 3/3 |
| http://123.57.213.24:3539 | CN | 2214 | 3 | 4/7 |
| http://159.195.49.27:8888 | DE | 2921 | 3 | 5/8 |
| http://176.57.189.138:3128 | FR | 6030 | 3 | 3/3 |
| http://43.203.140.58:23536 | KR | 2733 | 3 | 3/3 |
| http://175.136.239.173:8181 | MY | 4867 | 3 | 6/8 |
| http://175.139.255.25:8181 | MY | 4217 | 3 | 7/8 |
| http://175.143.76.177:8181 | MY | 7808 | 3 | 7/8 |
| http://190.93.224.32:999 | PE | 5307 | 3 | 3/3 |
| http://43.163.112.8:80 | SG | 1406 | 3 | 4/5 |
| http://165.245.187.193:3128 | SG | 1184 | 3 | 3/3 |
| http://216.125.22.3:5999 | US | 1194 | 3 | 3/3 |
| socks5://192.9.171.168:1080 | AU | 2402 | 3 | 6/7 |
| socks5://59.152.97.233:1080 | BD | 2103 | 3 | 5/6 |
| socks5://45.95.232.35:1080 | CH | 4485 | 3 | 5/8 |
| socks5://62.133.62.27:1082 | FR | 622 | 3 | 3/3 |
| socks5://144.91.111.48:1088 | FR | 6446 | 3 | 6/8 |
| socks5://185.185.80.58:1088 | FR | 2259 | 3 | 6/7 |
| socks5://43.162.94.99:1080 | US | 845 | 3 | 7/8 |
| http://103.161.69.252:2698 | BD | 7152 | 2 | 3/8 |
| http://177.177.59.253:8080 | BR | 5079 | 2 | 2/2 |
| http://1.15.53.214:8888 | CN | 2146 | 2 | 2/2 |
| http://58.254.153.146:17981 | CN | 1830 | 2 | 4/6 |
| http://111.230.27.213:3128 | CN | 6096 | 2 | 5/8 |
| http://112.64.135.45:8080 | CN | 2732 | 2 | 4/7 |
| http://114.236.137.41:21000 | CN | 2861 | 2 | 7/8 |
| http://179.1.76.147:8080 | CO | 7191 | 2 | 3/6 |
| http://200.107.205.44:999 | DO | 3993 | 2 | 3/7 |
| http://205.235.1.36:999 | EC | 6949 | 2 | 2/2 |
| http://213.131.85.29:1976 | EG | 1092 | 2 | 2/2 |
| http://45.144.53.63:6022 | FI | 1364 | 2 | 2/2 |
| http://103.61.234.186:8180 | ID | 2640 | 2 | 4/5 |
| http://103.155.65.166:8080 | ID | 6748 | 2 | 2/2 |
