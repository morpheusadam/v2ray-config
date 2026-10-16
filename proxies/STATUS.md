# Proxy status

Generated 2026-10-16T22:11:22Z by `harvest.py`.

- **1041** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3258** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 157/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1934 |
| socks5 | 1316 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 1136 |
| ID | 571 |
| PH | 101 |
| US | 99 |
| CO | 87 |
| MX | 85 |
| CN | 81 |
| RU | 79 |
| VE | 61 |
| BD | 52 |
| IN | 52 |
| BR | 51 |
| EC | 46 |
| VN | 45 |
| SG | 37 |
| DO | 36 |
| JP | 35 |
| TR | 35 |
| AR | 33 |
| DE | 30 |
| TH | 29 |
| ?? | 28 |
| PK | 26 |
| EG | 24 |
| CA | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 1 | 2026-10-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 58 | 58 | 13 | 2026-10-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 95 | 95 | 47 | 2026-10-16 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 123 | 123 | 51 | 2026-10-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 127 | 127 | 38 | 2026-10-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-10-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 337 | 337 | 80 | 2026-10-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 349 | 349 | 147 | 2026-10-16 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 505 | 505 | 344 | 2026-10-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-10-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1142 | 2026-10-16 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1610 | 1606 | 136 | 2026-10-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1598 | 2026-10-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1916 | 1914 | 848 | 2026-10-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2339 | 2337 | 1718 | 2026-10-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2876 | 2874 | 1137 | 2026-10-16 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 63787 | 63787 | 49762 | 2026-10-16 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 70006 | 70005 | 2305 | 2026-10-16 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1039 | 54 | 121/134 |
| http://149.130.173.58:9443 | CO | 599 | 45 | 45/45 |
| http://190.0.246.213:4040 | CO | 1925 | 28 | 91/99 |
| http://197.224.185.3:3128 | MU | 2036 | 26 | 95/102 |
| http://103.237.102.191:11111 | DE | 966 | 21 | 127/134 |
| http://203.252.142.217:80 | KR | 726 | 16 | 16/16 |
| http://45.186.6.104:3128 | EC | 2842 | 15 | 105/112 |
| socks5://101.36.104.46:10808 | JP | 1584 | 15 | 118/134 |
| http://3.211.120.181:443 | US | 402 | 14 | 28/45 |
| http://165.154.162.73:8888 | US | 893 | 14 | 87/134 |
| http://102.244.78.61:8083 | CM | 1427 | 13 | 19/22 |
| http://103.130.61.61:8081 | ID | 4891 | 13 | 105/134 |
| http://102.244.78.61:8088 | CM | 1458 | 11 | 18/22 |
| http://5.129.254.5:8888 | RU | 2397 | 11 | 78/89 |
| http://5.129.254.49:8888 | RU | 3404 | 11 | 79/89 |
| http://5.129.254.51:8888 | RU | 3466 | 11 | 79/89 |
| http://5.129.254.60:8888 | RU | 1397 | 11 | 78/88 |
| http://5.129.254.70:8888 | RU | 1340 | 11 | 79/89 |
| http://5.129.254.129:8888 | RU | 2405 | 11 | 84/95 |
| http://5.129.254.154:8888 | RU | 3377 | 11 | 75/85 |
| http://5.129.254.215:8888 | RU | 2425 | 11 | 28/31 |
| http://5.129.254.243:8888 | RU | 1327 | 11 | 28/30 |
| http://34.88.38.81:9443 | FI | 1299 | 10 | 69/99 |
| http://35.228.49.168:9443 | FI | 926 | 10 | 50/71 |
| http://103.133.26.50:8080 | ID | 1206 | 10 | 14/35 |
| http://103.133.26.72:8080 | ID | 1179 | 10 | 15/60 |
| http://103.133.26.73:3128 | ID | 1583 | 10 | 30/112 |
| http://103.133.26.119:8080 | ID | 1534 | 10 | 14/44 |
| socks5://67.207.92.87:1088 | US | 662 | 10 | 78/133 |
| http://184.75.221.82:3118 | CA | 515 | 9 | 87/99 |
| http://147.45.164.178:8888 | RU | 1402 | 8 | 8/8 |
| http://56.112.92.32:16486 | CA | 1106 | 6 | 8/19 |
| http://56.68.116.64:15932 | MY | 2183 | 6 | 16/74 |
| http://128.199.121.61:9090 | SG | 895 | 6 | 44/54 |
| socks5://171.25.158.95:1080 | SE | 5044 | 6 | 41/49 |
| socks5://47.87.97.94:1080 | TH | 1301 | 6 | 9/10 |
| http://16.51.53.116:23517 | AU | 3409 | 5 | 15/50 |
| http://38.7.195.51:999 | CL | 6012 | 5 | 52/125 |
| http://102.244.78.61:8082 | CM | 1451 | 5 | 18/23 |
| http://102.244.78.61:8086 | CM | 1424 | 5 | 17/22 |
| http://102.244.78.61:8089 | CM | 1444 | 5 | 16/22 |
| http://205.237.105.49:3129 | FR | 850 | 5 | 5/5 |
| http://198.244.254.77:3128 | GB | 4855 | 5 | 16/18 |
| http://176.111.37.5:39811 | HK | 1246 | 5 | 115/134 |
| http://101.32.94.127:8089 | JP | 3429 | 5 | 13/22 |
| http://34.43.46.91:443 | US | 1242 | 5 | 125/134 |
| http://38.7.195.53:999 | CL | 3178 | 4 | 46/133 |
| http://123.121.123.115:8888 | CN | 1553 | 4 | 34/58 |
| http://31.76.127.171:3128 | DE | 1818 | 4 | 12/19 |
| http://41.128.77.76:1976 | EG | 4523 | 4 | 39/100 |
| http://45.125.64.215:443 | HK | 1119 | 4 | 4/4 |
| http://176.111.37.216:39811 | HK | 1277 | 4 | 107/134 |
| http://103.171.183.148:7777 | ID | 7226 | 4 | 23/126 |
| http://13.208.246.143:46557 | JP | 2716 | 4 | 22/94 |
| http://140.238.32.108:3128 | JP | 951 | 4 | 67/133 |
| http://189.51.168.165:999 | MX | 555 | 4 | 42/46 |
| http://180.191.121.220:8181 | PH | 3761 | 4 | 4/4 |
| http://18.222.28.236:1256 | US | 1631 | 4 | 5/6 |
| http://34.43.46.91:80 | US | 1357 | 4 | 128/134 |
| http://154.59.56.73:999 | VE | 3114 | 4 | 78/106 |
| http://161.22.32.31:8080 | VE | 2240 | 4 | 8/12 |
| http://116.104.251.199:2080 | VN | 1461 | 4 | 5/7 |
| http://16.28.29.244:4744 | ZA | 5785 | 4 | 9/48 |
| socks5://47.238.126.208:1080 | HK | 1054 | 4 | 22/39 |
| socks5://101.36.104.239:10808 | JP | 1366 | 4 | 113/134 |
| socks5://116.104.251.199:1080 | VN | 1664 | 4 | 5/7 |
| http://16.26.208.68:18596 | AU | 3119 | 3 | 32/99 |
| http://18.231.214.206:14559 | BR | 4966 | 3 | 27/112 |
| http://40.176.175.23:26204 | CA | 5145 | 3 | 30/120 |
| http://102.244.78.61:8080 | CM | 1422 | 3 | 18/23 |
| http://102.244.78.61:8084 | CM | 1421 | 3 | 17/22 |
| http://123.119.179.161:8888 | CN | 1157 | 3 | 41/99 |
| http://221.221.157.102:8888 | CN | 3738 | 3 | 35/86 |
| http://63.180.203.233:37086 | DE | 3905 | 3 | 20/94 |
| http://217.12.215.163:10808 | DE | 2919 | 3 | 18/116 |
| http://38.75.82.216:999 | DO | 7856 | 3 | 22/103 |
| http://177.234.217.237:999 | EC | 3288 | 3 | 49/107 |
| http://181.78.194.249:999 | EC | 7872 | 3 | 41/117 |
| http://41.65.103.168:8080 | EG | 1439 | 3 | 10/22 |
| http://45.245.208.180:8080 | EG | 2528 | 3 | 6/7 |
| http://80.65.211.149:8888 | FR | 6576 | 3 | 6/13 |
| http://103.98.116.209:8080 | ID | 3203 | 3 | 3/3 |
| http://103.183.8.243:8080 | ID | 7135 | 3 | 5/15 |
| http://103.203.233.134:8080 | ID | 2651 | 3 | 4/15 |
| http://115.178.55.223:8080 | ID | 7425 | 3 | 5/19 |
| http://51.17.99.116:40013 | IL | 3079 | 3 | 8/22 |
| http://51.85.44.149:1081 | IL | 1647 | 3 | 23/130 |
| http://152.67.191.232:6800 | IN | 2367 | 3 | 3/3 |
| http://43.202.114.177:7428 | KR | 1912 | 3 | 19/48 |
| http://94.198.188.140:81 | KZ | 4192 | 3 | 3/3 |
| http://187.251.224.167:80 | MX | 5527 | 3 | 36/130 |
| http://205.164.192.115:999 | MX | 7934 | 3 | 85/132 |
| http://152.32.85.141:8081 | PH | 2214 | 3 | 13/56 |
| http://49.229.100.235:8080 | TH | 1638 | 3 | 51/82 |
| http://61.91.162.126:8080 | TH | 1237 | 3 | 60/77 |
| http://103.10.231.189:8080 | TH | 1620 | 3 | 86/119 |
| http://3.134.245.77:4145 | US | 1232 | 3 | 8/36 |
| http://34.229.190.39:33893 | US | 1895 | 3 | 15/75 |
| http://162.255.110.107:8080 | US | 2236 | 3 | 28/105 |
| http://154.59.56.78:999 | VE | 6074 | 3 | 62/90 |
