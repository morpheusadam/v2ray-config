# Proxy status

Generated 2026-08-12T20:23:09Z by `harvest.py`.

- **564** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **754** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11349** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 252/600 (42%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 547 |
| socks5 | 192 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 136 |
| US | 76 |
| CN | 45 |
| RU | 42 |
| VN | 30 |
| NL | 26 |
| PH | 25 |
| DE | 24 |
| FR | 24 |
| BD | 23 |
| CO | 21 |
| SG | 21 |
| MX | 19 |
| VE | 18 |
| BR | 16 |
| HK | 14 |
| JP | 14 |
| IN | 11 |
| TH | 10 |
| TR | 10 |
| AR | 8 |
| EC | 8 |
| FI | 7 |
| PL | 7 |
| ZA | 7 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-08-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 79 | 79 | 59 | 2026-08-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 94 | 94 | 21 | 2026-08-12 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 106 | 106 | 44 | 2026-08-12 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 126 | 126 | 36 | 2026-08-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 139 | 139 | 10 | 2026-08-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 145 | 145 | 44 | 2026-08-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 94 | 2026-08-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 216 | 216 | 141 | 2026-08-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-12 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 553 | 553 | 368 | 2026-08-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 534 | 2026-08-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 461 | 2026-08-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1144 | 2026-08-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1633 | 2026-08-12 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1849 | 1845 | 0 | 2026-08-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1962 | 1960 | 192 | 2026-08-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2446 | 2444 | 688 | 2026-08-12 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2498 | 2498 | 1941 | 2026-08-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2731 | 2729 | 2427 | 2026-08-12 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://114.236.137.41:21000 | CN | 1973 | 5 | 5/5 |
| http://190.0.246.211:4040 | CO | 849 | 5 | 5/5 |
| http://87.251.77.29:3128 | DE | 886 | 5 | 5/5 |
| http://103.237.102.191:11111 | DE | 948 | 5 | 5/5 |
| http://43.99.100.108:3128 | HK | 1793 | 5 | 5/5 |
| http://176.111.37.5:39811 | HK | 1126 | 5 | 5/5 |
| http://176.111.37.216:39811 | HK | 1122 | 5 | 5/5 |
| http://103.130.61.61:8081 | ID | 1989 | 5 | 5/5 |
| http://1.231.81.166:3128 | KR | 1482 | 5 | 5/5 |
| http://88.210.11.216:8989 | NL | 734 | 5 | 5/5 |
| http://95.211.64.139:8888 | NL | 1835 | 5 | 5/5 |
| http://95.211.64.139:8889 | NL | 709 | 5 | 5/5 |
| http://95.211.174.135:3128 | NL | 784 | 5 | 5/5 |
| http://144.178.199.118:8443 | NL | 1295 | 5 | 5/5 |
| http://147.45.166.120:3333 | NL | 795 | 5 | 5/5 |
| http://204.76.203.9:3128 | NL | 1195 | 5 | 5/5 |
| http://109.94.1.23:4050 | RU | 3195 | 5 | 5/5 |
| http://185.200.188.234:10001 | RU | 1392 | 5 | 5/5 |
| http://143.198.87.117:8888 | SG | 2902 | 5 | 5/5 |
| http://152.42.167.241:3128 | SG | 2490 | 5 | 5/5 |
| http://202.28.194.139:31280 | TH | 2209 | 5 | 5/5 |
| http://95.3.69.222:8080 | TR | 1723 | 5 | 5/5 |
| http://34.43.46.91:443 | US | 519 | 5 | 5/5 |
| http://34.43.46.91:80 | US | 254 | 5 | 5/5 |
| http://43.153.82.179:8888 | US | 818 | 5 | 5/5 |
| http://64.112.184.210:3128 | US | 312 | 5 | 5/5 |
| socks5://144.22.165.206:1088 | BR | 2081 | 5 | 5/5 |
| socks5://45.144.54.40:1080 | DE | 1371 | 5 | 5/5 |
| socks5://66.163.118.99:10006 | ES | 2039 | 5 | 5/5 |
| socks5://144.91.121.61:1088 | FR | 4010 | 5 | 5/5 |
| socks5://212.58.132.5:1080 | GB | 2493 | 5 | 5/5 |
| socks5://123.58.219.171:10808 | HK | 2444 | 5 | 5/5 |
| socks5://66.163.119.55:10006 | IT | 5936 | 5 | 5/5 |
| socks5://149.62.186.244:1080 | IT | 5171 | 5 | 5/5 |
| socks5://101.36.104.46:10808 | JP | 3576 | 5 | 5/5 |
| socks5://101.36.104.239:10808 | JP | 1497 | 5 | 5/5 |
| socks5://193.233.218.213:1080 | RU | 1140 | 5 | 5/5 |
| socks5://43.134.58.45:1080 | SG | 4098 | 5 | 5/5 |
| socks5://43.156.84.41:10808 | SG | 2450 | 5 | 5/5 |
| socks5://69.55.49.177:38182 | US | 868 | 5 | 5/5 |
| socks5://129.151.9.55:10808 | US | 807 | 5 | 5/5 |
| socks5://193.25.215.182:22222 | US | 3395 | 5 | 5/5 |
| http://185.191.239.248:3128 | CH | 2254 | 4 | 4/4 |
| http://38.7.195.53:999 | CL | 4200 | 4 | 4/4 |
| http://95.211.64.139:8887 | NL | 587 | 4 | 4/4 |
| http://203.150.128.134:8080 | TH | 5978 | 4 | 4/4 |
| http://178.18.207.85:8888 | TR | 6892 | 4 | 4/4 |
| http://157.230.178.216:40000 | US | 3345 | 4 | 4/4 |
| http://162.214.74.29:3128 | US | 4775 | 4 | 4/4 |
| http://162.214.159.94:3128 | US | 4592 | 4 | 4/4 |
| http://174.137.134.182:2999 | US | 364 | 4 | 4/4 |
| http://163.181.207.167:9999 | VN | 1453 | 4 | 4/4 |
| socks5://134.175.238.113:1080 | CN | 3283 | 4 | 4/4 |
| socks5://144.21.39.252:1080 | NL | 735 | 4 | 4/4 |
| socks5://171.25.158.95:1080 | SE | 4850 | 4 | 4/4 |
| socks5://141.148.158.143:1080 | US | 3465 | 4 | 4/4 |
| http://170.238.38.15:8080 | BR | 6230 | 3 | 3/3 |
| http://122.246.3.210:17981 | CN | 1661 | 3 | 4/5 |
| http://152.53.20.190:20000 | DE | 2498 | 3 | 4/5 |
| http://103.124.197.26:8090 | ID | 5767 | 3 | 3/3 |
| http://103.167.68.84:8080 | ID | 5555 | 3 | 3/3 |
| http://210.87.124.213:1111 | ID | 5665 | 3 | 3/3 |
| http://210.131.214.36:80 | JP | 1442 | 3 | 4/5 |
| http://187.190.58.152:80 | MX | 3828 | 3 | 3/3 |
| http://66.163.127.204:10006 | NL | 1112 | 3 | 4/5 |
| http://153.80.240.37:8080 | NL | 2715 | 3 | 4/5 |
| http://120.28.211.162:8081 | PH | 7457 | 3 | 3/3 |
| http://180.191.235.152:8082 | PH | 3508 | 3 | 3/3 |
| http://43.156.237.221:80 | SG | 1087 | 3 | 3/3 |
| http://34.94.46.8:80 | US | 311 | 3 | 3/3 |
| http://195.158.8.123:3128 | UZ | 3814 | 3 | 3/3 |
| http://38.51.207.116:999 | VE | 7831 | 3 | 3/3 |
| http://154.62.127.108:999 | VE | 6293 | 3 | 3/3 |
| socks5://43.138.214.122:9981 | CN | 1728 | 3 | 3/3 |
| socks5://59.38.113.185:20000 | CN | 2299 | 3 | 4/5 |
| socks5://38.175.197.50:5555 | HK | 3934 | 3 | 3/3 |
| socks5://161.35.90.93:1081 | NL | 7361 | 3 | 4/5 |
| socks5://161.35.90.93:1082 | NL | 1699 | 3 | 4/5 |
| socks5://185.209.29.226:1080 | RU | 1723 | 3 | 4/5 |
| socks5://45.43.63.37:10808 | SG | 3425 | 3 | 4/5 |
| http://103.72.198.132:55 | BD | 2869 | 2 | 3/4 |
| http://38.7.206.186:999 | CL | 2841 | 2 | 2/2 |
| http://59.36.210.211:13552 | CN | 2929 | 2 | 2/2 |
| http://200.10.31.45:8081 | CO | 2081 | 2 | 2/2 |
| http://181.39.25.196:8118 | EC | 1511 | 2 | 4/5 |
| http://196.204.80.110:1981 | EG | 6334 | 2 | 2/2 |
| http://213.131.85.26:1976 | EG | 5784 | 2 | 2/2 |
| http://169.58.85.194:443 | FR | 1690 | 2 | 2/2 |
| http://103.235.174.137:7777 | HK | 7152 | 2 | 2/2 |
| http://103.235.174.138:7777 | HK | 7866 | 2 | 2/2 |
| http://103.61.234.186:8180 | ID | 5386 | 2 | 2/2 |
| http://103.154.53.67:1111 | ID | 3539 | 2 | 3/4 |
| http://103.158.210.25:8080 | ID | 1537 | 2 | 2/2 |
| http://103.164.231.243:8080 | ID | 1719 | 2 | 2/2 |
| http://103.179.183.153:8080 | ID | 1514 | 2 | 2/2 |
| http://113.192.48.11:8080 | ID | 6100 | 2 | 3/4 |
| http://114.9.25.74:8080 | ID | 4118 | 2 | 2/2 |
| http://157.66.51.201:8080 | ID | 5434 | 2 | 2/2 |
| http://202.154.19.153:8080 | ID | 1694 | 2 | 2/2 |
| http://223.25.110.77:8090 | ID | 2755 | 2 | 3/4 |
