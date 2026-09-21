# Proxy status

Generated 2026-09-21T18:45:38Z by `harvest.py`.

- **1321** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2924** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **32112** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 82/600 (14%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1478 |
| socks5 | 1438 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 1110 |
| ID | 371 |
| ?? | 160 |
| CN | 105 |
| US | 91 |
| RU | 80 |
| SG | 65 |
| PH | 62 |
| MX | 60 |
| DE | 59 |
| CO | 52 |
| BD | 49 |
| VE | 45 |
| IN | 43 |
| VN | 37 |
| EC | 31 |
| TR | 30 |
| DO | 27 |
| EG | 27 |
| BR | 26 |
| FR | 26 |
| PK | 25 |
| TH | 22 |
| AR | 20 |
| HK | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 1 | 2026-09-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 73 | 73 | 36 | 2026-09-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-09-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 103 | 103 | 57 | 2026-09-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 137 | 137 | 50 | 2026-09-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-09-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 167 | 167 | 58 | 2026-09-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 182 | 182 | 28 | 2026-09-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 192 | 192 | 83 | 2026-09-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 400 | 400 | 187 | 2026-09-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-09-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-09-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-09-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1788 | 1784 | 535 | 2026-09-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1611 | 2026-09-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1879 | 1877 | 702 | 2026-09-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 1968 | 1966 | 1487 | 2026-09-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1992 | 1990 | 522 | 2026-09-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 17384 | 17384 | 9758 | 2026-09-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 22576 | 22575 | 2150 | 2026-09-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1031 | 70 | 83/84 |
| http://185.200.188.234:10001 | RU | 3437 | 70 | 83/84 |
| http://130.110.103.245:3128 | SA | 1495 | 70 | 82/84 |
| http://1.231.81.166:3128 | KR | 964 | 49 | 81/84 |
| http://190.97.236.128:999 | VE | 1017 | 41 | 72/74 |
| http://190.97.236.129:999 | VE | 957 | 41 | 72/74 |
| http://95.3.69.222:8080 | TR | 1582 | 39 | 81/84 |
| socks5://107.167.18.122:443 | US | 328 | 29 | 35/36 |
| http://91.134.141.4:3128 | FR | 939 | 23 | 43/45 |
| http://186.5.94.206:999 | EC | 4386 | 21 | 44/46 |
| http://107.150.41.226:18080 | US | 493 | 21 | 21/21 |
| http://38.51.207.104:8080 | VE | 816 | 17 | 24/25 |
| http://189.51.168.164:999 | MX | 1681 | 15 | 48/49 |
| http://45.132.252.25:49156 | RU | 1070 | 15 | 15/15 |
| http://193.104.179.115:3128 | UZ | 1402 | 14 | 32/49 |
| http://190.0.246.213:4040 | CO | 768 | 13 | 42/49 |
| http://213.111.146.36:18080 | NL | 2113 | 13 | 16/21 |
| http://45.186.6.104:3128 | EC | 887 | 11 | 60/62 |
| http://61.91.162.126:8080 | TH | 1237 | 11 | 24/27 |
| http://103.10.231.189:8080 | TH | 1226 | 11 | 49/69 |
| http://153.51.201.35:999 | VE | 957 | 11 | 11/11 |
| http://176.111.37.216:39811 | HK | 954 | 10 | 70/84 |
| http://201.71.2.25:999 | VE | 832 | 10 | 25/71 |
| http://201.71.2.27:999 | VE | 6413 | 10 | 31/82 |
| http://190.97.241.106:999 | VE | 1717 | 9 | 44/68 |
| socks5://193.233.223.47:1080 | RU | 1462 | 9 | 9/9 |
| http://176.111.37.5:39811 | HK | 1172 | 8 | 77/84 |
| http://144.124.251.24:10000 | NL | 1032 | 8 | 16/30 |
| http://144.124.251.24:10007 | NL | 1201 | 8 | 15/33 |
| http://144.124.251.24:10008 | NL | 898 | 8 | 11/15 |
| http://144.124.251.24:10104 | NL | 875 | 8 | 11/16 |
| http://144.124.251.24:10176 | NL | 986 | 8 | 15/32 |
| http://144.124.251.24:10185 | NL | 878 | 8 | 12/16 |
| http://144.124.251.24:10216 | NL | 994 | 8 | 16/33 |
| http://144.124.251.24:10226 | NL | 817 | 8 | 10/15 |
| http://144.124.251.24:10333 | NL | 1240 | 8 | 14/33 |
| http://144.124.251.24:10346 | NL | 873 | 8 | 12/16 |
| http://144.124.251.24:10366 | NL | 819 | 8 | 13/30 |
| http://144.124.251.24:10372 | NL | 1009 | 8 | 15/28 |
| http://144.124.251.24:10431 | NL | 914 | 8 | 17/32 |
| http://144.124.251.24:10453 | NL | 878 | 8 | 14/21 |
| http://144.124.251.24:10551 | NL | 1054 | 8 | 16/32 |
| http://144.124.251.24:10574 | NL | 959 | 8 | 16/33 |
| http://144.124.251.24:10628 | NL | 1440 | 8 | 11/16 |
| http://144.124.251.24:10771 | NL | 863 | 8 | 11/16 |
| http://144.124.251.24:10829 | NL | 901 | 8 | 11/16 |
| http://144.124.251.24:10953 | NL | 814 | 8 | 12/16 |
| http://144.124.251.24:11011 | NL | 801 | 8 | 12/16 |
| http://144.124.251.24:11108 | NL | 1327 | 8 | 13/31 |
| http://144.124.251.24:11180 | NL | 878 | 8 | 11/15 |
| http://144.124.251.24:11265 | NL | 895 | 8 | 15/32 |
| http://144.124.251.24:11266 | NL | 873 | 8 | 12/16 |
| http://144.124.251.24:11274 | NL | 935 | 8 | 15/32 |
| http://144.124.251.24:11480 | NL | 837 | 8 | 10/16 |
| http://144.124.251.24:11491 | NL | 984 | 8 | 15/32 |
| socks5://161.35.90.93:1082 | NL | 2464 | 8 | 46/84 |
| http://103.130.61.61:8081 | ID | 3281 | 7 | 67/84 |
| socks5://45.32.160.61:1088 | US | 488 | 7 | 34/37 |
| socks5://83.147.217.103:1080 | US | 474 | 7 | 7/7 |
| http://62.193.104.26:1981 | EG | 5121 | 6 | 8/12 |
| http://144.124.251.24:10187 | NL | 961 | 6 | 12/30 |
| http://144.124.251.24:10230 | NL | 869 | 6 | 15/31 |
| http://144.124.251.24:10801 | NL | 2290 | 6 | 12/32 |
| http://43.128.76.140:8080 | SG | 4190 | 6 | 13/17 |
| http://43.163.7.224:8080 | SG | 2391 | 6 | 6/6 |
| http://159.223.41.216:9090 | SG | 876 | 6 | 28/44 |
| http://201.71.2.26:999 | VE | 4964 | 6 | 35/77 |
| socks5://213.199.47.140:1080 | FR | 4195 | 6 | 42/50 |
| http://101.251.204.174:8080 | CN | 1757 | 5 | 36/70 |
| http://31.31.74.185:9898 | CZ | 2302 | 5 | 5/5 |
| http://85.133.250.27:80 | IR | 6936 | 5 | 8/9 |
| http://43.156.199.63:8080 | SG | 2092 | 5 | 16/19 |
| http://146.190.80.158:9090 | SG | 876 | 5 | 8/10 |
| socks5://95.181.160.37:1080 | DE | 2240 | 5 | 5/5 |
| socks5://135.125.232.151:1080 | DE | 958 | 5 | 13/15 |
| socks5://109.123.251.109:1080 | FR | 2178 | 5 | 44/84 |
| socks5://144.91.111.48:1088 | FR | 1614 | 5 | 52/84 |
| socks5://185.87.255.54:1080 | GB | 2015 | 5 | 5/5 |
| socks5://123.58.219.171:10808 | HK | 1701 | 5 | 67/84 |
| socks5://101.36.104.239:10808 | JP | 1252 | 5 | 68/84 |
| socks5://150.109.247.86:8443 | KR | 772 | 5 | 5/5 |
| socks5://135.148.120.20:1080 | US | 670 | 5 | 10/11 |
| socks5://193.25.215.182:22222 | US | 1818 | 5 | 77/84 |
| http://123.119.178.176:8888 | CN | 6256 | 4 | 24/49 |
| http://190.0.246.211:4040 | CO | 6859 | 4 | 71/84 |
| http://190.12.150.244:999 | EC | 3444 | 4 | 53/80 |
| http://18.163.182.106:21128 | HK | 5465 | 4 | 23/52 |
| http://117.236.124.166:3128 | IN | 1510 | 4 | 56/84 |
| http://144.124.251.24:10082 | NL | 919 | 4 | 14/32 |
| http://43.153.195.69:80 | SG | 857 | 4 | 16/24 |
| http://43.163.7.224:8081 | SG | 3455 | 4 | 4/4 |
| http://43.163.124.191:8080 | SG | 1839 | 4 | 8/9 |
| http://128.199.121.61:9090 | SG | 860 | 4 | 4/4 |
| http://128.199.254.13:9090 | SG | 865 | 4 | 9/13 |
| http://167.172.76.176:9090 | SG | 1506 | 4 | 26/45 |
| socks5://5.75.133.113:10814 | DE | 2530 | 4 | 7/9 |
| socks5://144.91.121.61:1088 | FR | 2720 | 4 | 72/84 |
| socks5://64.227.186.105:1080 | IN | 1686 | 4 | 4/4 |
| socks5://103.75.118.84:1080 | JP | 1906 | 4 | 58/79 |
| socks5://57.128.231.218:1004 | PL | 4083 | 4 | 13/18 |
