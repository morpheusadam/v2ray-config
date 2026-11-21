# Proxy status

Generated 2026-11-21T00:56:22Z by `harvest.py`.

- **1800** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3709** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **27059** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 155/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3241 |
| socks5 | 464 |
| socks4 | 4 |

| country | entries |
|---|---|
| ID | 955 |
| ?? | 523 |
| NL | 233 |
| PH | 158 |
| MX | 139 |
| CO | 130 |
| US | 104 |
| TR | 97 |
| TH | 94 |
| BR | 86 |
| VE | 86 |
| RU | 78 |
| IN | 76 |
| BD | 67 |
| EC | 60 |
| AR | 49 |
| DO | 41 |
| ZA | 41 |
| CN | 35 |
| DE | 35 |
| EG | 35 |
| PK | 35 |
| PE | 31 |
| SG | 29 |
| CL | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 2 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 60 | 60 | 11 | 2026-11-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 111 | 111 | 14 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 123 | 123 | 16 | 2026-11-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 31 | 2026-11-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 57 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 240 | 240 | 25 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 405 | 405 | 288 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1114 | 1114 | 201 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1125 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2068 | 2068 | 207 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2458 | 2458 | 249 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2817 | 2817 | 672 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3153 | 3153 | 1810 | 2026-11-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5607 | 5607 | 4347 | 2026-11-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12431 | 12431 | 2260 | 2026-11-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1056 | 75 | 185/204 |
| http://130.110.103.245:3128 | SA | 1360 | 50 | 186/204 |
| http://141.94.22.37:3128 | FR | 793 | 16 | 19/20 |
| http://45.155.226.177:3128 | HK | 671 | 13 | 18/20 |
| http://4.144.146.21:80 | SG | 956 | 11 | 87/96 |
| http://15.229.149.81:3128 | BR | 2063 | 10 | 76/114 |
| http://52.128.238.98:18080 | HK | 100 | 10 | 15/19 |
| http://185.238.236.226:58080 | PL | 1291 | 10 | 63/126 |
| http://128.199.121.61:9090 | SG | 1213 | 10 | 97/124 |
| socks5://193.25.215.182:22222 | US | 310 | 10 | 169/204 |
| http://103.130.61.61:8081 | ID | 3491 | 9 | 169/204 |
| http://34.43.46.91:443 | US | 593 | 9 | 189/204 |
| http://34.43.46.91:80 | US | 679 | 9 | 197/204 |
| socks5://45.61.129.165:9050 | US | 1254 | 9 | 156/204 |
| socks5://46.246.12.31:1080 | ?? | 3802 | 9 | 9/9 |
| http://15.229.149.81:1080 | BR | 2282 | 8 | 60/106 |
| http://103.176.96.225:8082 | ID | 4483 | 8 | 54/149 |
| http://189.51.168.164:999 | MX | 868 | 8 | 36/40 |
| http://104.248.151.93:9090 | SG | 980 | 8 | 73/105 |
| http://20.98.234.24:8080 | ?? | 327 | 8 | 8/8 |
| socks5://69.55.49.177:38182 | US | 769 | 8 | 48/59 |
| http://103.237.102.191:11111 | DE | 850 | 7 | 191/204 |
| http://103.61.234.186:8180 | ID | 2523 | 7 | 92/201 |
| http://201.46.86.37:8080 | MX | 5127 | 7 | 14/38 |
| http://172.235.157.127:3128 | ?? | 316 | 7 | 7/7 |
| http://45.186.6.104:3128 | EC | 700 | 6 | 172/182 |
| http://49.213.59.105:8082 | ID | 1780 | 6 | 54/163 |
| http://103.133.26.50:8080 | ID | 1304 | 6 | 70/105 |
| http://103.133.26.72:8080 | ID | 2246 | 6 | 78/130 |
| http://103.133.26.73:3128 | ID | 1311 | 6 | 94/182 |
| http://103.158.210.80:8082 | ID | 3572 | 6 | 65/194 |
| http://110.74.195.34:25 | KH | 6257 | 6 | 68/197 |
| http://159.223.41.216:9090 | SG | 1198 | 6 | 120/164 |
| http://91.134.141.4:3128 | ?? | 796 | 6 | 6/6 |
| socks5://103.119.1.160:5555 | HK | 4863 | 6 | 14/19 |
| socks5://45.61.188.134:44499 | US | 594 | 6 | 93/171 |
| socks5://103.124.172.134:1080 | ?? | 3848 | 6 | 6/6 |
| http://35.183.78.223:58093 | CA | 4724 | 5 | 35/102 |
| http://38.57.65.195:999 | DO | 5152 | 5 | 27/89 |
| http://181.78.195.136:999 | EC | 5957 | 5 | 34/60 |
| http://45.245.208.180:8080 | EG | 2307 | 5 | 53/77 |
| http://103.86.117.23:8080 | ID | 1343 | 5 | 38/124 |
| http://103.144.54.35:8082 | ID | 6629 | 5 | 49/127 |
| http://185.142.156.203:80 | IR | 2008 | 5 | 33/69 |
| http://140.238.32.108:3128 | JP | 808 | 5 | 120/203 |
| http://185.238.238.49:58080 | PL | 5486 | 5 | 79/198 |
| http://43.159.54.178:80 | SG | 964 | 5 | 52/124 |
| http://165.154.162.73:8888 | US | 158 | 5 | 135/204 |
| http://154.59.56.76:999 | VE | 5506 | 5 | 118/164 |
| http://181.79.89.140:999 | ?? | 6193 | 5 | 5/5 |
| http://190.112.193.64:999 | ?? | 3664 | 5 | 7/9 |
| http://217.142.139.207:8085 | ?? | 2982 | 5 | 6/7 |
| http://187.102.219.32:999 | AR | 1485 | 4 | 79/203 |
| http://123.115.226.82:8888 | CN | 1451 | 4 | 57/150 |
| http://200.10.30.5:8083 | CO | 4364 | 4 | 63/193 |
| http://63.180.203.233:37086 | DE | 3285 | 4 | 51/164 |
| http://185.174.80.7:3128 | ES | 1382 | 4 | 44/173 |
| http://54.36.150.233:3128 | FR | 1011 | 4 | 17/26 |
| http://38.199.88.1:999 | GT | 2188 | 4 | 15/24 |
| http://103.133.24.75:8080 | ID | 6203 | 4 | 20/93 |
| http://103.147.134.179:8080 | ID | 1905 | 4 | 23/66 |
| http://103.162.16.109:8080 | ID | 3022 | 4 | 9/32 |
| http://216.243.112.30:3128 | ID | 3964 | 4 | 13/31 |
| http://124.108.19.6:9292 | IN | 6292 | 4 | 8/30 |
| http://161.49.87.222:8095 | PH | 5687 | 4 | 26/100 |
| http://192.203.0.142:999 | PR | 3861 | 4 | 27/132 |
| http://167.172.76.176:9090 | SG | 1342 | 4 | 121/165 |
| http://38.51.206.73:999 | VE | 3879 | 4 | 11/25 |
| http://154.59.56.72:999 | VE | 2823 | 4 | 120/163 |
| http://181.225.53.141:999 | VE | 2177 | 4 | 36/173 |
| http://45.66.156.107:8081 | ?? | 2844 | 4 | 4/4 |
| http://49.151.179.5:8082 | ?? | 2734 | 4 | 4/4 |
| http://114.253.7.197:8888 | ?? | 3016 | 4 | 4/4 |
| http://119.94.185.43:8082 | ?? | 5230 | 4 | 4/4 |
| http://125.25.53.180:8080 | ?? | 5947 | 4 | 4/4 |
| http://147.161.246.34:10002 | ?? | 6059 | 4 | 4/4 |
| http://147.161.246.34:10109 | ?? | 6485 | 4 | 4/4 |
| http://147.161.246.34:10704 | ?? | 6496 | 4 | 4/4 |
| http://147.161.246.34:10800 | ?? | 6441 | 4 | 4/4 |
| http://147.161.246.34:10935 | ?? | 6275 | 4 | 4/4 |
| http://147.161.246.34:11111 | ?? | 6319 | 4 | 4/4 |
| http://147.161.246.34:11368 | ?? | 6524 | 4 | 4/4 |
| http://147.161.246.34:11629 | ?? | 6202 | 4 | 4/4 |
| http://147.161.246.34:12010 | ?? | 6617 | 4 | 4/4 |
| http://147.161.246.34:12544 | ?? | 6530 | 4 | 4/4 |
| http://147.161.246.34:12702 | ?? | 5862 | 4 | 4/4 |
| http://147.161.246.34:80 | ?? | 6096 | 4 | 4/4 |
| http://154.3.76.16:999 | ?? | 5240 | 4 | 10/12 |
| http://160.191.198.178:8082 | ?? | 3766 | 4 | 4/4 |
| socks5://172.81.111.156:10001 | HK | 1003 | 4 | 11/32 |
| socks5://209.50.255.91:1080 | US | 1579 | 4 | 57/121 |
| socks5://103.248.228.166:5555 | ?? | 1151 | 4 | 6/7 |
| http://13.239.253.213:29050 | AU | 3296 | 3 | 30/116 |
| http://27.147.153.179:12051 | BD | 6223 | 3 | 15/24 |
| http://179.48.11.6:8085 | BR | 5404 | 3 | 18/73 |
| http://181.191.14.5:8080 | BR | 2576 | 3 | 28/194 |
| http://3.96.141.200:15392 | CA | 4044 | 3 | 12/28 |
| http://56.112.92.32:4904 | CA | 1741 | 3 | 36/114 |
| http://190.93.229.1:18080 | CL | 6540 | 3 | 10/54 |
| http://123.121.122.125:8888 | CN | 1677 | 3 | 17/27 |
