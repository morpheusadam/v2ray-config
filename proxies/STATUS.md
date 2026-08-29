# Proxy status

Generated 2026-08-29T21:56:02Z by `harvest.py`.

- **812** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1569** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14998** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 137/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1364 |
| socks5 | 193 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 325 |
| US | 155 |
| CN | 110 |
| CO | 63 |
| PH | 52 |
| MX | 48 |
| BR | 45 |
| BD | 40 |
| RU | 40 |
| DE | 38 |
| VE | 37 |
| FR | 35 |
| TH | 33 |
| IN | 32 |
| NL | 30 |
| TR | 28 |
| EC | 27 |
| SG | 25 |
| HK | 23 |
| VN | 22 |
| JP | 20 |
| AU | 19 |
| DO | 18 |
| EG | 16 |
| KH | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 3 | 3 | 1 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 63 | 63 | 32 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 64 | 64 | 12 | 2026-08-29 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 103 | 103 | 45 | 2026-08-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 112 | 112 | 46 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 116 | 116 | 52 | 2026-08-29 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 125 | 125 | 38 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 186 | 186 | 45 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 246 | 246 | 61 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-29 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 613 | 613 | 286 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-08-29 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1374 | 1370 | 391 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1149 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1599 | 2026-08-29 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 1979 | 1979 | 1568 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2178 | 2176 | 298 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2490 | 2488 | 616 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3062 | 3060 | 2304 | 2026-08-29 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1403 | 36 | 38/39 |
| http://34.43.46.91:443 | US | 979 | 31 | 36/39 |
| http://34.43.46.91:80 | US | 1233 | 31 | 36/39 |
| http://103.237.102.191:11111 | DE | 1293 | 25 | 38/39 |
| http://95.211.174.135:3128 | NL | 1752 | 25 | 38/39 |
| http://204.76.203.9:3128 | NL | 1339 | 25 | 38/39 |
| http://204.76.203.9:8080 | NL | 739 | 25 | 31/32 |
| http://185.200.188.234:10001 | RU | 2877 | 25 | 38/39 |
| http://130.110.103.245:3128 | SA | 1838 | 25 | 37/39 |
| http://95.3.69.222:8080 | TR | 1677 | 25 | 38/39 |
| http://199.7.149.90:3128 | US | 352 | 22 | 22/22 |
| http://199.7.149.96:3128 | US | 362 | 18 | 18/18 |
| http://45.186.6.104:3128 | EC | 763 | 17 | 17/17 |
| http://64.112.184.210:3128 | US | 912 | 17 | 38/39 |
| http://190.0.246.210:4040 | CO | 1265 | 15 | 35/38 |
| http://103.130.61.61:8081 | ID | 1701 | 14 | 34/39 |
| http://42.96.18.62:1311 | VN | 2259 | 13 | 28/38 |
| socks5://144.91.121.61:1088 | FR | 4420 | 13 | 37/39 |
| http://176.111.37.5:39811 | HK | 1158 | 12 | 34/39 |
| http://190.0.246.211:4040 | CO | 2464 | 11 | 34/39 |
| http://103.211.103.170:3128 | HK | 990 | 11 | 11/11 |
| http://202.28.194.139:31280 | TH | 2449 | 11 | 37/39 |
| http://14.251.13.20:8080 | VN | 1183 | 11 | 11/11 |
| socks4://45.61.129.165:9050 | US | 3753 | 11 | 31/39 |
| socks5://101.36.104.46:10808 | JP | 1597 | 11 | 36/39 |
| http://87.251.77.29:3128 | DE | 997 | 10 | 36/39 |
| socks5://45.194.33.12:30001 | HK | 1138 | 10 | 28/35 |
| socks5://45.194.33.12:30002 | HK | 1146 | 10 | 12/13 |
| http://103.177.118.145:8118 | BD | 5617 | 9 | 19/20 |
| http://81.19.210.10:80 | GB | 678 | 9 | 9/9 |
| http://87.237.15.238:7080 | BE | 737 | 7 | 7/7 |
| http://197.224.185.3:3128 | MU | 1968 | 7 | 7/7 |
| http://175.136.239.173:8181 | MY | 4046 | 7 | 31/39 |
| http://157.85.108.68:3128 | TH | 4235 | 7 | 7/7 |
| http://157.85.111.64:3128 | TH | 2088 | 7 | 7/7 |
| http://68.178.174.239:3128 | US | 974 | 7 | 7/7 |
| http://68.178.174.239:8888 | US | 1228 | 7 | 7/7 |
| http://209.174.97.162:5999 | US | 387 | 7 | 7/7 |
| http://8.138.217.152:21001 | CN | 2961 | 6 | 26/39 |
| http://181.78.23.187:999 | CO | 748 | 6 | 7/8 |
| http://181.78.74.252:999 | CO | 871 | 6 | 29/30 |
| http://181.78.74.253:999 | CO | 785 | 6 | 29/30 |
| http://190.97.236.128:999 | VE | 714 | 6 | 28/29 |
| http://190.97.236.129:999 | VE | 1742 | 6 | 28/29 |
| http://210.211.113.34:80 | VN | 3376 | 6 | 10/11 |
| socks5://113.249.111.67:1080 | CN | 3370 | 6 | 6/6 |
| socks5://45.12.18.106:1080 | RU | 1381 | 6 | 6/6 |
| socks5://84.8.102.52:1080 | SA | 1680 | 6 | 6/6 |
| http://152.53.136.178:10000 | DE | 2137 | 5 | 10/14 |
| http://212.154.169.90:3128 | KZ | 1363 | 5 | 15/18 |
| socks5://5.75.133.113:10811 | DE | 1440 | 5 | 7/10 |
| socks5://213.199.47.140:1080 | FR | 2660 | 5 | 5/5 |
| http://87.237.15.239:7080 | BE | 3880 | 4 | 4/4 |
| http://184.75.221.82:3118 | CA | 455 | 4 | 4/4 |
| http://114.248.86.121:8888 | CN | 6159 | 4 | 4/4 |
| http://114.248.179.223:8888 | CN | 1897 | 4 | 6/7 |
| http://120.232.115.170:17981 | CN | 1638 | 4 | 23/38 |
| http://123.115.212.50:8888 | CN | 2170 | 4 | 4/4 |
| http://123.121.115.239:8888 | CN | 1594 | 4 | 4/4 |
| http://123.121.121.123:8888 | CN | 1939 | 4 | 4/4 |
| http://123.121.141.57:8888 | CN | 1250 | 4 | 4/4 |
| http://190.0.246.213:4040 | CO | 723 | 4 | 4/4 |
| http://130.61.112.125:443 | DE | 3641 | 4 | 4/4 |
| http://194.163.175.167:40000 | FR | 957 | 4 | 4/4 |
| http://1.231.81.166:3128 | KR | 1149 | 4 | 36/39 |
| http://189.51.168.164:999 | MX | 514 | 4 | 4/4 |
| http://175.136.239.174:8181 | MY | 5439 | 4 | 25/39 |
| http://43.156.227.68:80 | SG | 961 | 4 | 4/4 |
| http://43.160.242.118:3128 | SG | 3407 | 4 | 29/36 |
| http://157.85.97.203:3128 | TH | 1124 | 4 | 4/4 |
| http://157.85.97.204:3128 | TH | 1120 | 4 | 4/4 |
| http://157.85.97.242:3128 | TH | 1117 | 4 | 4/4 |
| http://157.85.105.218:3128 | TH | 4431 | 4 | 4/4 |
| http://157.85.105.220:3128 | TH | 1311 | 4 | 4/4 |
| http://157.85.108.50:3128 | TH | 1314 | 4 | 4/4 |
| http://157.85.108.69:3128 | TH | 1087 | 4 | 4/4 |
| http://157.85.108.135:3128 | TH | 1092 | 4 | 4/4 |
| http://35.94.193.222:5001 | US | 2652 | 4 | 4/4 |
| http://45.59.100.205:3128 | US | 282 | 4 | 4/4 |
| socks4://158.220.99.85:4545 | FR | 4694 | 4 | 4/4 |
| socks5://47.250.211.53:1080 | MY | 5344 | 4 | 20/39 |
| socks5://185.118.143.141:1080 | TR | 5412 | 4 | 9/11 |
| http://111.192.21.92:8888 | CN | 2176 | 3 | 3/3 |
| http://114.246.196.30:8888 | CN | 4272 | 3 | 3/3 |
| http://114.249.219.180:8888 | CN | 3252 | 3 | 3/3 |
| http://114.252.13.224:8888 | CN | 1394 | 3 | 3/3 |
| http://139.159.97.82:10900 | CN | 1261 | 3 | 5/8 |
| http://223.85.21.195:8080 | CN | 4471 | 3 | 21/37 |
| http://38.75.82.219:999 | DO | 7542 | 3 | 5/13 |
| http://154.88.132.50:8080 | DO | 5526 | 3 | 3/3 |
| http://186.33.45.220:999 | EC | 2561 | 3 | 5/8 |
| http://84.36.141.180:1976 | EG | 1316 | 3 | 12/25 |
| http://37.59.125.131:8888 | FR | 3642 | 3 | 29/39 |
| http://82.64.186.155:8080 | FR | 7468 | 3 | 3/3 |
| http://8.215.25.3:2081 | ID | 1651 | 3 | 11/37 |
| http://103.156.15.103:3125 | ID | 5059 | 3 | 5/15 |
| http://185.166.27.208:2020 | IQ | 7352 | 3 | 4/6 |
| http://94.131.92.155:3128 | KZ | 6436 | 3 | 23/37 |
| http://20.61.126.88:3128 | NL | 776 | 3 | 3/3 |
| http://40.115.63.18:3128 | NL | 741 | 3 | 3/3 |
