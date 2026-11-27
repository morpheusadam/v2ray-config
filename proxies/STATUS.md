# Proxy status

Generated 2026-11-27T22:04:55Z by `harvest.py`.

- **1420** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3673** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **24744** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 113/600 (19%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3263 |
| socks5 | 398 |
| socks4 | 12 |

| country | entries |
|---|---|
| ID | 1004 |
| ?? | 287 |
| NL | 177 |
| PH | 170 |
| CO | 156 |
| MX | 155 |
| US | 106 |
| IN | 101 |
| BR | 100 |
| TR | 99 |
| CN | 93 |
| VE | 93 |
| TH | 84 |
| RU | 78 |
| BD | 63 |
| EC | 57 |
| AR | 55 |
| PK | 40 |
| DE | 38 |
| DO | 38 |
| CH | 33 |
| VN | 33 |
| EG | 31 |
| PE | 30 |
| SG | 30 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-11-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 87 | 2026-11-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 108 | 108 | 31 | 2026-11-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 132 | 132 | 35 | 2026-11-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 86 | 2026-11-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 158 | 158 | 39 | 2026-11-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 185 | 185 | 11 | 2026-11-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 109 | 2026-11-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 320 | 320 | 118 | 2026-11-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 337 | 337 | 259 | 2026-11-27 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 175 | 2026-11-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 567 | 2026-11-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1225 | 1225 | 211 | 2026-11-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1469 | 1469 | 53 | 2026-11-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1565 | 1565 | 89 | 2026-11-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1239 | 2026-11-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-27 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1953 | 1953 | 374 | 2026-11-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2206 | 2206 | 1437 | 2026-11-27 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5797 | 5797 | 4659 | 2026-11-27 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11749 | 11749 | 1903 | 2026-11-27 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1020 | 88 | 198/217 |
| http://130.110.103.245:3128 | SA | 1337 | 63 | 199/217 |
| http://45.155.226.177:3128 | HK | 786 | 26 | 31/33 |
| http://4.144.146.21:80 | SG | 965 | 24 | 100/109 |
| http://34.43.46.91:80 | US | 1445 | 22 | 210/217 |
| http://189.51.168.164:999 | MX | 6507 | 21 | 49/53 |
| http://20.98.234.24:8080 | US | 298 | 21 | 21/21 |
| socks5://69.55.49.177:38182 | US | 807 | 21 | 61/72 |
| http://103.237.102.191:11111 | DE | 837 | 20 | 204/217 |
| http://45.186.6.104:3128 | EC | 792 | 19 | 185/195 |
| http://103.133.26.50:8080 | ID | 1265 | 19 | 83/118 |
| http://103.133.26.73:3128 | ID | 1325 | 19 | 107/195 |
| http://45.135.95.185:3128 | RU | 4577 | 15 | 15/15 |
| http://128.199.113.85:9090 | SG | 961 | 15 | 35/48 |
| socks5://123.58.219.171:10808 | HK | 1419 | 15 | 159/217 |
| http://103.163.80.181:8085 | ID | 1298 | 13 | 13/13 |
| http://50.238.106.26:3128 | US | 351 | 13 | 13/13 |
| http://158.247.125.5:9443 | CO | 505 | 12 | 12/12 |
| http://34.43.46.91:443 | US | 1450 | 12 | 201/217 |
| http://216.125.18.67:3128 | US | 952 | 12 | 12/12 |
| http://185.191.239.248:3128 | CH | 2677 | 10 | 153/216 |
| http://45.136.253.145:3128 | TH | 1072 | 10 | 15/21 |
| http://102.244.78.61:8083 | CM | 1318 | 9 | 83/105 |
| http://45.65.138.48:999 | CO | 6328 | 9 | 114/217 |
| http://177.234.217.89:999 | EC | 7145 | 9 | 28/42 |
| http://129.153.97.250:9443 | US | 7464 | 9 | 9/9 |
| http://154.59.56.78:999 | VE | 3467 | 9 | 119/173 |
| http://103.81.86.170:8888 | VN | 4274 | 9 | 9/9 |
| socks5://59.11.209.162:1080 | KR | 966 | 9 | 9/9 |
| http://190.12.150.244:999 | EC | 2707 | 8 | 159/213 |
| http://128.199.116.219:9090 | SG | 956 | 8 | 106/136 |
| http://114.249.228.162:8888 | CN | 6687 | 7 | 7/7 |
| http://45.65.137.218:999 | CO | 6694 | 7 | 94/182 |
| http://197.164.101.14:1981 | EG | 4133 | 7 | 57/187 |
| http://173.212.207.102:1214 | FR | 729 | 7 | 7/7 |
| http://189.187.131.201:999 | MX | 5332 | 7 | 7/7 |
| http://123.115.143.194:8888 | CN | 1667 | 6 | 10/16 |
| http://197.164.101.11:1981 | EG | 5134 | 6 | 15/34 |
| http://213.131.85.28:1976 | EG | 1165 | 6 | 21/31 |
| http://187.102.219.42:999 | AR | 1285 | 5 | 124/212 |
| http://114.249.219.234:8888 | CN | 1672 | 5 | 9/13 |
| http://38.41.184.73:999 | DO | 4305 | 5 | 22/90 |
| http://41.65.55.27:1981 | EG | 5268 | 5 | 60/157 |
| http://41.196.16.231:1976 | EG | 1214 | 5 | 9/44 |
| http://45.245.208.180:8080 | EG | 5358 | 5 | 64/90 |
| http://81.10.102.153:8080 | EG | 1573 | 5 | 5/5 |
| http://198.244.254.77:3128 | GB | 3751 | 5 | 81/101 |
| http://9.154.240.122:8085 | ID | 6676 | 5 | 28/111 |
| http://38.188.63.115:8081 | ID | 6181 | 5 | 33/141 |
| http://49.213.59.105:8082 | ID | 7871 | 5 | 60/176 |
| http://103.110.10.166:8181 | ID | 3760 | 5 | 46/180 |
| http://103.172.70.27:9090 | ID | 5864 | 5 | 11/31 |
| http://45.43.60.220:8080 | JP | 3877 | 5 | 121/216 |
| http://78.14.19.3:3128 | MX | 2354 | 5 | 54/177 |
| http://202.154.241.199:808 | PK | 6536 | 5 | 12/38 |
| http://81.27.101.176:443 | PL | 820 | 5 | 5/5 |
| http://81.27.101.176:80 | PL | 794 | 5 | 5/5 |
| http://128.199.121.61:9090 | SG | 960 | 5 | 107/137 |
| http://195.158.8.123:3128 | UZ | 5665 | 5 | 140/215 |
| http://154.59.56.74:999 | VE | 5792 | 5 | 123/180 |
| socks5://103.13.19.219:10808 | JP | 2281 | 5 | 25/34 |
| socks5://193.218.118.128:1080 | UA | 6893 | 5 | 53/73 |
| socks5://172.104.210.252:1080 | US | 356 | 5 | 5/5 |
| http://168.194.34.196:9001 | AR | 2509 | 4 | 86/215 |
| http://16.51.5.77:16637 | AU | 5395 | 4 | 46/157 |
| http://114.246.207.179:8888 | CN | 1815 | 4 | 12/19 |
| http://114.249.233.148:8888 | CN | 6619 | 4 | 11/13 |
| http://123.115.226.82:8888 | CN | 1465 | 4 | 62/163 |
| http://123.121.113.161:8888 | CN | 1937 | 4 | 24/42 |
| http://123.121.140.72:8888 | CN | 1728 | 4 | 41/69 |
| http://123.121.142.252:8888 | CN | 1506 | 4 | 64/139 |
| http://38.50.165.126:999 | DO | 4975 | 4 | 45/140 |
| http://45.175.167.73:999 | EC | 7592 | 4 | 9/40 |
| http://38.226.242.71:8080 | ID | 1974 | 4 | 48/156 |
| http://103.133.26.72:8080 | ID | 1462 | 4 | 90/143 |
| http://103.166.255.170:8080 | ID | 4138 | 4 | 37/155 |
| http://103.187.86.34:8182 | ID | 1421 | 4 | 39/190 |
| http://121.101.133.105:8586 | ID | 6888 | 4 | 34/126 |
| http://162.4.96.24:4567 | ID | 7856 | 4 | 15/51 |
| http://163.227.149.135:8080 | ID | 1939 | 4 | 38/212 |
| http://163.227.248.81:8818 | ID | 6837 | 4 | 36/189 |
| http://102.68.76.247:5566 | KE | 6965 | 4 | 69/170 |
| http://180.190.222.136:8082 | PH | 7357 | 4 | 15/42 |
| http://185.238.236.226:58080 | PL | 3631 | 4 | 73/139 |
| http://116.204.166.151:8080 | TR | 7721 | 4 | 41/172 |
| http://93.170.118.112:8989 | UA | 5659 | 4 | 5/6 |
| http://161.22.33.109:999 | VE | 6578 | 4 | 27/102 |
| http://200.59.191.27:999 | VE | 4214 | 4 | 147/212 |
| http://114.249.208.204:8888 | ?? | 6026 | 4 | 4/4 |
| socks5://78.142.217.197:1080 | DE | 853 | 4 | 10/13 |
| socks5://95.31.115.101:9150 | RU | 3130 | 4 | 26/37 |
| http://186.125.218.150:999 | AR | 4247 | 3 | 32/147 |
| http://187.102.219.32:999 | AR | 1566 | 3 | 86/216 |
| http://190.104.35.30:8081 | AR | 7954 | 3 | 37/131 |
| http://138.59.233.59:8080 | BR | 7693 | 3 | 29/123 |
| http://189.124.85.77:33333 | BR | 3746 | 3 | 30/127 |
| http://200.126.94.179:999 | CL | 6589 | 3 | 13/42 |
| http://114.246.196.98:8888 | CN | 1828 | 3 | 9/19 |
| http://114.246.207.203:8888 | CN | 3907 | 3 | 4/5 |
| http://114.249.208.179:8888 | CN | 1970 | 3 | 4/5 |
