# Proxy status

Generated 2026-10-31T22:48:40Z by `harvest.py`.

- **1876** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4714** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33591** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 169/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2665 |
| socks5 | 2044 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 1811 |
| ID | 716 |
| ?? | 562 |
| CO | 115 |
| PH | 110 |
| MX | 103 |
| US | 89 |
| TH | 73 |
| BR | 65 |
| RU | 65 |
| VE | 64 |
| CN | 54 |
| BD | 53 |
| IN | 52 |
| TR | 48 |
| EC | 43 |
| AR | 41 |
| DO | 40 |
| PK | 39 |
| PE | 31 |
| SG | 29 |
| ZA | 29 |
| CA | 24 |
| DE | 24 |
| EG | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 5 | 2026-10-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 55 | 55 | 7 | 2026-10-31 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 144 | 144 | 79 | 2026-10-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 56 | 2026-10-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-10-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 179 | 179 | 29 | 2026-10-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-31 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 436 | 436 | 293 | 2026-10-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 523 | 523 | 198 | 2026-10-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-10-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 968 | 968 | 305 | 2026-10-31 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1416 | 1416 | 70 | 2026-10-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1144 | 2026-10-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1582 | 2026-10-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2287 | 2287 | 668 | 2026-10-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2755 | 2755 | 1632 | 2026-10-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3165 | 3165 | 996 | 2026-10-31 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4897 | 4897 | 3698 | 2026-10-31 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11330 | 11329 | 2685 | 2026-10-31 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 4964 | 84 | 151/164 |
| http://149.130.173.58:9443 | CO | 7855 | 75 | 75/75 |
| http://103.237.102.191:11111 | DE | 1055 | 51 | 157/164 |
| http://103.133.26.73:3128 | ID | 1290 | 40 | 60/142 |
| http://176.111.37.5:39811 | HK | 1440 | 35 | 145/164 |
| http://34.43.46.91:80 | US | 674 | 34 | 158/164 |
| http://4.144.146.21:80 | SG | 894 | 32 | 49/56 |
| http://190.0.246.210:4040 | CO | 5282 | 31 | 150/163 |
| http://176.111.37.216:39811 | HK | 1247 | 27 | 136/164 |
| http://103.130.61.61:8081 | ID | 6360 | 26 | 134/164 |
| socks5://67.207.92.87:1088 | US | 1197 | 19 | 105/163 |
| http://34.43.46.91:443 | US | 646 | 13 | 153/164 |
| http://167.172.76.176:9090 | SG | 904 | 11 | 88/125 |
| socks5://101.36.104.239:10808 | JP | 1796 | 11 | 140/164 |
| socks5://193.218.118.128:1080 | UA | 1764 | 11 | 17/20 |
| http://130.110.103.245:3128 | SA | 2002 | 10 | 146/164 |
| socks5://49.13.22.249:10805 | DE | 5791 | 10 | 50/82 |
| socks5://45.61.188.134:44499 | US | 642 | 10 | 66/131 |
| socks5://193.25.215.182:22222 | US | 901 | 10 | 137/164 |
| http://185.238.236.226:58080 | PL | 2629 | 9 | 36/86 |
| http://123.121.134.192:8888 | CN | 1643 | 8 | 15/30 |
| http://35.183.78.223:35766 | CA | 1013 | 7 | 7/7 |
| http://177.234.217.85:999 | EC | 2470 | 7 | 10/19 |
| http://103.133.26.72:8080 | ID | 1234 | 7 | 44/90 |
| http://128.199.121.61:9090 | SG | 890 | 7 | 67/84 |
| http://36.213.79.159:1081 | CN | 4458 | 6 | 11/24 |
| http://123.121.209.108:8888 | CN | 6932 | 6 | 42/114 |
| http://81.19.210.10:80 | GB | 1105 | 6 | 17/25 |
| http://154.18.255.43:8080 | ID | 4775 | 6 | 17/69 |
| http://154.59.56.78:999 | VE | 4982 | 6 | 83/120 |
| http://45.189.57.114:3129 | ?? | 861 | 6 | 6/6 |
| http://104.194.146.9:80 | ?? | 1344 | 6 | 9/10 |
| http://191.5.126.28:8080 | ?? | 3504 | 6 | 7/9 |
| socks5://202.62.42.92:1080 | KH | 2634 | 6 | 34/146 |
| socks5://107.174.30.92:1080 | US | 496 | 6 | 31/60 |
| http://187.102.219.64:999 | AR | 1914 | 5 | 62/103 |
| http://15.229.149.81:1080 | BR | 2940 | 5 | 29/66 |
| http://102.244.78.61:8080 | CM | 1434 | 5 | 43/53 |
| http://102.244.78.61:8083 | CM | 1431 | 5 | 43/52 |
| http://102.244.78.61:8084 | CM | 1429 | 5 | 41/52 |
| http://102.244.78.61:8085 | CM | 1422 | 5 | 42/54 |
| http://102.244.78.61:8086 | CM | 1389 | 5 | 42/52 |
| http://102.244.78.61:8087 | CM | 1427 | 5 | 41/54 |
| http://181.78.195.137:999 | EC | 7977 | 5 | 57/164 |
| http://103.97.141.85:8080 | ID | 4113 | 5 | 18/78 |
| http://45.43.60.220:8080 | JP | 1243 | 5 | 89/163 |
| http://102.68.76.247:5566 | KE | 5085 | 5 | 40/117 |
| http://45.174.242.145:999 | MX | 1841 | 5 | 26/119 |
| http://49.145.58.197:8082 | PH | 2467 | 5 | 23/38 |
| http://122.53.48.41:8080 | PH | 7271 | 5 | 23/86 |
| http://128.199.116.219:9090 | SG | 891 | 5 | 65/83 |
| http://159.223.41.216:9090 | SG | 907 | 5 | 89/124 |
| socks5://5.75.133.113:10805 | DE | 5310 | 5 | 40/82 |
| socks5://37.18.73.60:5566 | RU | 4291 | 5 | 21/61 |
| socks5://23.141.116.9:9000 | ?? | 6447 | 5 | 8/16 |
| http://184.75.221.82:3118 | CA | 1489 | 4 | 113/129 |
| http://102.244.78.61:8081 | CM | 1432 | 4 | 41/50 |
| http://102.244.78.61:8090 | CM | 1420 | 4 | 42/56 |
| http://38.156.238.32:999 | DO | 5668 | 4 | 21/104 |
| http://101.255.209.166:8080 | ID | 6605 | 4 | 10/25 |
| http://103.76.109.123:8090 | ID | 7030 | 4 | 17/74 |
| http://115.178.50.122:8080 | ID | 7015 | 4 | 7/14 |
| http://158.140.181.116:8080 | ID | 7850 | 4 | 22/89 |
| http://203.175.103.193:8080 | ID | 4365 | 4 | 6/17 |
| http://35.78.252.142:56698 | JP | 3099 | 4 | 36/144 |
| http://115.147.254.250:6040 | PH | 7218 | 4 | 20/113 |
| http://120.28.200.84:5050 | PH | 3726 | 4 | 12/84 |
| http://103.253.18.6:8080 | PK | 7226 | 4 | 14/74 |
| http://185.238.238.165:58080 | PL | 2619 | 4 | 26/54 |
| http://38.172.160.16:999 | VE | 4995 | 4 | 67/115 |
| http://200.59.191.27:999 | VE | 2944 | 4 | 108/159 |
| http://103.131.19.42:8181 | ?? | 6978 | 4 | 10/19 |
| http://103.156.222.1:8090 | ?? | 4934 | 4 | 4/4 |
| http://130.127.204.197:8080 | ?? | 403 | 4 | 4/4 |
| http://172.212.125.72:3128 | ?? | 7613 | 4 | 4/4 |
| socks5://65.21.252.66:10805 | FI | 3291 | 4 | 43/78 |
| socks5://42.115.72.145:1083 | ?? | 3613 | 4 | 4/4 |
| socks5://42.115.72.145:1088 | ?? | 7103 | 4 | 4/4 |
| socks5://61.247.178.146:1080 | ?? | 2665 | 4 | 4/4 |
| socks5://207.180.217.98:1088 | ?? | 2688 | 4 | 4/4 |
| http://45.65.224.74:999 | AR | 5215 | 3 | 22/29 |
| http://181.168.156.192:8080 | AR | 4876 | 3 | 17/71 |
| http://103.127.92.161:8090 | BD | 5207 | 3 | 15/85 |
| http://123.200.8.170:10000 | BD | 2717 | 3 | 70/162 |
| http://201.28.68.138:8080 | BR | 2941 | 3 | 15/54 |
| http://102.244.78.61:8082 | CM | 1424 | 3 | 42/53 |
| http://102.244.78.61:8088 | CM | 1421 | 3 | 41/52 |
| http://102.244.78.61:8089 | CM | 1420 | 3 | 40/52 |
| http://111.196.30.74:8888 | CN | 3910 | 3 | 6/13 |
| http://123.121.132.234:8888 | CN | 1661 | 3 | 19/25 |
| http://190.60.58.236:999 | CO | 2019 | 3 | 28/117 |
| http://38.75.82.212:999 | DO | 5198 | 3 | 55/158 |
| http://38.156.14.138:999 | DO | 7984 | 3 | 15/78 |
| http://217.76.245.80:999 | DO | 1239 | 3 | 32/120 |
| http://190.12.150.244:999 | EC | 6820 | 3 | 116/160 |
| http://41.33.126.136:1981 | EG | 1391 | 3 | 11/23 |
| http://43.199.29.225:34588 | HK | 2675 | 3 | 13/74 |
| http://38.46.214.243:1111 | ID | 6874 | 3 | 15/53 |
| http://103.46.186.57:8080 | ID | 3479 | 3 | 12/50 |
| http://103.82.246.19:6080 | ID | 5982 | 3 | 27/100 |
