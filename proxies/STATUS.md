# Proxy status

Generated 2026-11-22T20:27:48Z by `harvest.py`.

- **1616** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4237** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **26407** endpoints on record
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
| http | 3601 |
| socks5 | 628 |
| socks4 | 8 |

| country | entries |
|---|---|
| ID | 1059 |
| ?? | 722 |
| NL | 423 |
| PH | 181 |
| MX | 156 |
| CO | 139 |
| US | 99 |
| TH | 98 |
| VE | 98 |
| BR | 91 |
| IN | 77 |
| TR | 76 |
| BD | 73 |
| EC | 60 |
| RU | 57 |
| AR | 56 |
| DO | 52 |
| PK | 47 |
| CN | 35 |
| EG | 35 |
| PE | 35 |
| VN | 35 |
| ZA | 35 |
| CL | 26 |
| SG | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-11-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-22 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 102 | 102 | 14 | 2026-11-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 136 | 136 | 20 | 2026-11-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 35 | 2026-11-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 59 | 2026-11-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 159 | 159 | 30 | 2026-11-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 252 | 252 | 59 | 2026-11-22 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 441 | 441 | 290 | 2026-11-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-11-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 679 | 679 | 128 | 2026-11-22 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1509 | 1509 | 0 | 2026-11-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1113 | 2026-11-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1577 | 2026-11-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2142 | 2142 | 313 | 2026-11-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2378 | 2378 | 720 | 2026-11-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2683 | 2683 | 1615 | 2026-11-22 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5677 | 5677 | 4393 | 2026-11-22 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12173 | 12173 | 2124 | 2026-11-22 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 867 | 78 | 188/207 |
| http://130.110.103.245:3128 | SA | 1298 | 53 | 189/207 |
| http://141.94.22.37:3128 | FR | 682 | 19 | 22/23 |
| http://45.155.226.177:3128 | HK | 616 | 16 | 21/23 |
| http://4.144.146.21:80 | SG | 1036 | 14 | 90/99 |
| http://15.229.149.81:3128 | BR | 3227 | 13 | 79/117 |
| http://128.199.121.61:9090 | SG | 1157 | 13 | 100/127 |
| socks5://193.25.215.182:22222 | US | 743 | 13 | 172/207 |
| http://34.43.46.91:80 | US | 656 | 12 | 200/207 |
| socks5://46.246.12.31:1080 | ?? | 2799 | 12 | 12/12 |
| http://15.229.149.81:1080 | BR | 3130 | 11 | 63/109 |
| http://189.51.168.164:999 | MX | 943 | 11 | 39/43 |
| http://104.248.151.93:9090 | SG | 1028 | 11 | 76/108 |
| http://20.98.234.24:8080 | ?? | 217 | 11 | 11/11 |
| socks5://69.55.49.177:38182 | US | 362 | 11 | 51/62 |
| http://103.237.102.191:11111 | DE | 768 | 10 | 194/207 |
| http://45.186.6.104:3128 | EC | 744 | 9 | 175/185 |
| http://103.133.26.50:8080 | ID | 1519 | 9 | 73/108 |
| http://103.133.26.72:8080 | ID | 1371 | 9 | 81/133 |
| http://103.133.26.73:3128 | ID | 1429 | 9 | 97/185 |
| http://103.158.210.80:8082 | ID | 1422 | 9 | 68/197 |
| http://91.134.141.4:3128 | ?? | 651 | 9 | 9/9 |
| http://45.245.208.180:8080 | EG | 2302 | 8 | 56/80 |
| http://140.238.32.108:3128 | JP | 5862 | 8 | 123/206 |
| http://154.59.56.76:999 | VE | 5156 | 8 | 121/167 |
| http://217.142.139.207:8085 | ?? | 4457 | 8 | 9/10 |
| http://54.36.150.233:3128 | FR | 686 | 7 | 20/29 |
| http://38.199.88.1:999 | GT | 4841 | 7 | 18/27 |
| http://154.59.56.72:999 | VE | 5518 | 7 | 123/166 |
| http://147.161.246.34:80 | ?? | 6826 | 7 | 7/7 |
| socks5://103.248.228.166:5555 | ?? | 1202 | 7 | 9/10 |
| http://45.240.232.61:8080 | EG | 4434 | 6 | 81/187 |
| http://103.120.175.243:9191 | ID | 1583 | 6 | 15/70 |
| http://146.190.80.158:9090 | SG | 1026 | 6 | 95/133 |
| http://102.222.240.10:9999 | ?? | 6679 | 6 | 6/6 |
| socks5://101.36.104.46:10808 | JP | 1025 | 6 | 171/207 |
| socks5://101.36.104.239:10808 | JP | 1021 | 6 | 169/207 |
| http://187.102.219.42:999 | AR | 6694 | 5 | 115/202 |
| http://177.87.15.141:8080 | BR | 5504 | 5 | 13/40 |
| http://190.7.138.78:8080 | CO | 3514 | 5 | 54/136 |
| http://177.234.217.235:999 | EC | 3941 | 5 | 95/176 |
| http://190.12.150.244:999 | EC | 2298 | 5 | 150/203 |
| http://103.124.137.150:20 | ID | 6590 | 5 | 34/148 |
| http://103.173.138.236:1111 | ID | 3741 | 5 | 43/207 |
| http://160.22.45.114:8080 | ID | 1997 | 5 | 43/66 |
| http://5.181.178.46:8080 | JP | 6778 | 5 | 21/83 |
| http://49.156.44.116:8080 | KH | 4491 | 5 | 19/41 |
| http://124.105.86.222:8090 | PH | 4483 | 5 | 33/159 |
| http://128.199.113.85:9090 | SG | 1073 | 5 | 25/38 |
| http://167.99.74.174:9090 | SG | 1029 | 5 | 112/167 |
| http://195.226.213.251:8888 | UA | 6265 | 5 | 82/201 |
| http://152.70.198.2:1080 | US | 7858 | 5 | 49/127 |
| http://38.172.181.0:999 | VE | 590 | 5 | 60/114 |
| http://190.97.249.30:999 | VE | 4611 | 5 | 11/35 |
| http://45.135.95.185:3128 | ?? | 1200 | 5 | 5/5 |
| http://191.44.125.14:8080 | ?? | 2262 | 5 | 6/7 |
| socks4://188.226.27.24:1080 | RU | 2301 | 5 | 32/43 |
| socks5://91.107.179.68:10809 | DE | 1072 | 5 | 74/140 |
| socks5://123.58.219.171:10808 | HK | 2048 | 5 | 149/207 |
| socks5://47.251.249.48:7777 | ?? | 251 | 5 | 7/9 |
| socks5://89.106.84.72:1080 | ?? | 3715 | 5 | 5/5 |
| http://186.22.246.60:3128 | AR | 6383 | 4 | 8/15 |
| http://190.123.83.137:999 | AR | 6759 | 4 | 37/44 |
| http://103.79.183.109:8080 | BD | 3704 | 4 | 29/64 |
| http://201.28.86.18:61804 | BR | 4179 | 4 | 22/28 |
| http://101.251.204.174:8080 | CN | 1873 | 4 | 106/193 |
| http://111.192.28.24:8888 | CN | 1622 | 4 | 14/29 |
| http://114.244.221.178:8888 | CN | 1280 | 4 | 67/130 |
| http://181.232.191.248:999 | DO | 4128 | 4 | 22/96 |
| http://177.234.217.44:999 | EC | 7115 | 4 | 44/107 |
| http://41.33.89.100:1981 | EG | 4984 | 4 | 16/63 |
| http://198.244.254.77:3128 | GB | 3471 | 4 | 73/91 |
| http://45.190.13.12:999 | HN | 2620 | 4 | 6/28 |
| http://58.147.186.31:3125 | ID | 5492 | 4 | 28/134 |
| http://103.153.149.59:8034 | ID | 3890 | 4 | 24/120 |
| http://103.180.127.116:8080 | ID | 7998 | 4 | 33/127 |
| http://139.255.94.123:39635 | ID | 3981 | 4 | 16/117 |
| http://45.43.60.220:8080 | JP | 2605 | 4 | 113/206 |
| http://45.168.239.59:999 | MX | 2599 | 4 | 6/17 |
| http://187.251.130.143:80 | MX | 4486 | 4 | 19/35 |
| http://206.135.47.110:999 | MX | 4061 | 4 | 40/78 |
| http://144.124.251.24:10000 | NL | 774 | 4 | 87/153 |
| http://144.124.251.24:10007 | NL | 848 | 4 | 80/156 |
| http://144.124.251.24:10082 | NL | 747 | 4 | 78/155 |
| http://144.124.251.24:10084 | NL | 734 | 4 | 77/139 |
| http://144.124.251.24:10088 | NL | 821 | 4 | 73/139 |
| http://144.124.251.24:10104 | NL | 769 | 4 | 76/139 |
| http://144.124.251.24:10176 | NL | 937 | 4 | 89/155 |
| http://144.124.251.24:10185 | NL | 765 | 4 | 78/139 |
| http://144.124.251.24:10187 | NL | 825 | 4 | 85/153 |
| http://144.124.251.24:10216 | NL | 868 | 4 | 91/156 |
| http://144.124.251.24:10230 | NL | 742 | 4 | 84/154 |
| http://144.124.251.24:10261 | NL | 707 | 4 | 81/139 |
| http://144.124.251.24:10333 | NL | 859 | 4 | 85/156 |
| http://144.124.251.24:10337 | NL | 932 | 4 | 78/139 |
| http://144.124.251.24:10346 | NL | 805 | 4 | 79/139 |
| http://144.124.251.24:10366 | NL | 805 | 4 | 83/153 |
| http://144.124.251.24:10372 | NL | 809 | 4 | 89/151 |
| http://144.124.251.24:10431 | NL | 759 | 4 | 82/155 |
| http://144.124.251.24:10453 | NL | 2408 | 4 | 85/144 |
