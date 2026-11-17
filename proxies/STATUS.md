# Proxy status

Generated 2026-11-17T21:52:07Z by `harvest.py`.

- **1736** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3971** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **31011** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 131/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2941 |
| socks5 | 1013 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 951 |
| NL | 726 |
| ?? | 164 |
| PH | 155 |
| CO | 146 |
| MX | 134 |
| US | 127 |
| VE | 96 |
| TR | 95 |
| TH | 91 |
| BR | 87 |
| RU | 84 |
| BD | 80 |
| IN | 78 |
| EC | 57 |
| VN | 50 |
| AR | 49 |
| DO | 45 |
| CN | 40 |
| EG | 39 |
| DE | 36 |
| PK | 35 |
| ZA | 35 |
| SG | 32 |
| CA | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-11-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 102 | 102 | 16 | 2026-11-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 30 | 2026-11-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 57 | 2026-11-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 178 | 178 | 44 | 2026-11-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 220 | 220 | 22 | 2026-11-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 349 | 349 | 134 | 2026-11-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 358 | 358 | 235 | 2026-11-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 443 | 2026-11-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 718 | 718 | 131 | 2026-11-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-11-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1722 | 1722 | 123 | 2026-11-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1582 | 2026-11-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2208 | 2208 | 441 | 2026-11-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2262 | 2262 | 679 | 2026-11-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2587 | 2587 | 1527 | 2026-11-17 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5471 | 5471 | 4266 | 2026-11-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11212 | 11212 | 2038 | 2026-11-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1413 | 68 | 178/197 |
| http://130.110.103.245:3128 | SA | 1487 | 43 | 179/197 |
| http://45.186.6.104:3128 | EC | 672 | 27 | 166/175 |
| http://38.180.18.103:3128 | BE | 666 | 26 | 26/26 |
| http://27.147.155.206:12051 | BD | 1666 | 17 | 17/17 |
| http://177.234.217.235:999 | EC | 2082 | 11 | 87/166 |
| http://141.94.22.37:3128 | FR | 630 | 9 | 12/13 |
| http://188.166.178.163:3129 | SG | 1112 | 9 | 9/9 |
| socks5://37.18.73.60:5566 | RU | 1366 | 9 | 45/94 |
| socks5://188.166.178.163:1088 | SG | 1267 | 9 | 9/9 |
| http://45.65.138.48:999 | CO | 3419 | 7 | 97/197 |
| socks5://107.174.30.92:1080 | US | 367 | 7 | 53/93 |
| http://102.244.78.61:8083 | CM | 1291 | 6 | 68/85 |
| http://102.244.78.61:8084 | CM | 1273 | 6 | 66/85 |
| http://102.244.78.61:8086 | CM | 1300 | 6 | 67/85 |
| http://102.244.78.61:8089 | CM | 1335 | 6 | 69/85 |
| http://45.155.226.177:3128 | HK | 1965 | 6 | 11/13 |
| http://211.188.50.146:80 | KR | 828 | 6 | 6/6 |
| http://211.188.53.248:80 | KR | 834 | 6 | 6/6 |
| http://211.188.55.218:80 | KR | 1323 | 6 | 6/6 |
| http://211.188.59.191:80 | KR | 2927 | 6 | 6/6 |
| http://211.188.60.84:80 | KR | 826 | 6 | 6/6 |
| socks5://193.218.118.128:1080 | UA | 5874 | 6 | 38/53 |
| socks5://47.251.166.203:1080 | US | 385 | 6 | 10/15 |
| http://102.244.78.61:8080 | CM | 1289 | 5 | 70/86 |
| http://102.244.78.61:8088 | CM | 1324 | 5 | 67/85 |
| http://126.209.110.120:8087 | PH | 4946 | 5 | 29/165 |
| http://180.191.228.36:8082 | PH | 7574 | 5 | 22/107 |
| socks5://101.36.104.46:10808 | JP | 3114 | 5 | 164/197 |
| http://102.244.78.61:8081 | CM | 1319 | 4 | 67/83 |
| http://102.244.78.61:8082 | CM | 1289 | 4 | 68/86 |
| http://102.244.78.61:8085 | CM | 1316 | 4 | 68/87 |
| http://102.244.78.61:8087 | CM | 1268 | 4 | 65/87 |
| http://102.244.78.61:8090 | CM | 1325 | 4 | 71/89 |
| http://177.234.217.82:999 | EC | 3650 | 4 | 31/94 |
| http://177.234.217.85:999 | EC | 6815 | 4 | 28/52 |
| http://177.234.217.89:999 | EC | 1446 | 4 | 12/22 |
| http://181.78.44.63:999 | HN | 4940 | 4 | 47/121 |
| http://103.80.82.7:8181 | ID | 5412 | 4 | 32/166 |
| http://103.146.38.107:1111 | ID | 7785 | 4 | 33/131 |
| http://103.191.165.171:8181 | ID | 4506 | 4 | 36/156 |
| http://43.165.169.48:80 | JP | 2640 | 4 | 9/14 |
| http://38.7.17.83:999 | MX | 4452 | 4 | 6/11 |
| http://82.152.138.127:999 | MX | 1353 | 4 | 70/159 |
| http://4.144.146.21:80 | SG | 1031 | 4 | 80/89 |
| http://167.99.74.174:9090 | SG | 1036 | 4 | 104/157 |
| http://49.229.100.235:8080 | TH | 1411 | 4 | 103/145 |
| http://171.100.254.137:8080 | TH | 1389 | 4 | 31/33 |
| http://216.152.149.246:80 | US | 3568 | 4 | 8/9 |
| http://116.101.73.52:2045 | VN | 1349 | 4 | 4/4 |
| socks5://95.216.45.44:10353 | FI | 2079 | 4 | 4/4 |
| socks5://188.226.27.24:1080 | RU | 5387 | 4 | 24/33 |
| http://168.194.34.196:9001 | AR | 1718 | 3 | 75/195 |
| http://15.229.149.81:3128 | BR | 3243 | 3 | 69/107 |
| http://200.182.232.34:80 | BR | 3185 | 3 | 6/30 |
| http://16.52.81.236:30468 | CA | 2231 | 3 | 23/109 |
| http://185.191.239.248:3128 | CH | 913 | 3 | 142/196 |
| http://114.244.223.68:8888 | CN | 1950 | 3 | 11/22 |
| http://123.121.101.115:8888 | CN | 1705 | 3 | 11/18 |
| http://123.121.123.216:8888 | CN | 7880 | 3 | 13/21 |
| http://38.19.41.208:999 | CO | 2866 | 3 | 31/162 |
| http://177.93.33.55:999 | CO | 4826 | 3 | 6/18 |
| http://191.103.216.234:8085 | CO | 930 | 3 | 8/30 |
| http://38.156.233.173:999 | DO | 6732 | 3 | 32/186 |
| http://154.88.136.182:999 | DO | 2896 | 3 | 17/70 |
| http://45.245.208.180:8080 | EG | 1155 | 3 | 48/70 |
| http://35.43.85.195:443 | ES | 938 | 3 | 10/13 |
| http://43.161.254.16:3128 | HK | 2640 | 3 | 31/37 |
| http://52.128.238.98:18080 | HK | 647 | 3 | 8/12 |
| http://31.58.57.74:1111 | ID | 6670 | 3 | 40/155 |
| http://36.64.86.11:8080 | ID | 5316 | 3 | 18/120 |
| http://45.198.11.147:8080 | ID | 2545 | 3 | 11/37 |
| http://103.102.12.105:8080 | ID | 6122 | 3 | 5/22 |
| http://103.125.50.234:8080 | ID | 4232 | 3 | 12/119 |
| http://103.126.86.239:9000 | ID | 7999 | 3 | 25/101 |
| http://103.147.134.137:8080 | ID | 7075 | 3 | 12/47 |
| http://103.154.231.123:8090 | ID | 6748 | 3 | 33/190 |
| http://103.156.75.89:1717 | ID | 7058 | 3 | 10/21 |
| http://103.171.241.18:1000 | ID | 4127 | 3 | 25/108 |
| http://103.171.255.204:8080 | ID | 6716 | 3 | 26/107 |
| http://103.172.42.177:1111 | ID | 7620 | 3 | 28/108 |
| http://103.178.171.113:8181 | ID | 3589 | 3 | 28/121 |
| http://103.234.35.147:3128 | ID | 5358 | 3 | 47/186 |
| http://103.238.232.50:8080 | ID | 7434 | 3 | 14/36 |
| http://157.15.62.173:8080 | ID | 7212 | 3 | 30/166 |
| http://160.22.45.6:8080 | ID | 4284 | 3 | 19/78 |
| http://203.128.69.230:8080 | ID | 3831 | 3 | 44/194 |
| http://210.87.125.58:1080 | ID | 2313 | 3 | 29/170 |
| http://18.61.230.250:9898 | IN | 5292 | 3 | 35/147 |
| http://140.238.32.108:3128 | JP | 5254 | 3 | 115/196 |
| http://102.0.28.78:8083 | KE | 7238 | 3 | 24/122 |
| http://102.208.166.30:8082 | KE | 1916 | 3 | 32/168 |
| http://165.16.17.189:8080 | LY | 5206 | 3 | 13/30 |
| http://38.194.246.34:999 | MX | 4669 | 3 | 111/188 |
| http://187.245.202.244:999 | MX | 6779 | 3 | 7/19 |
| http://187.251.230.15:8080 | MX | 4545 | 3 | 40/165 |
| http://201.139.183.210:999 | MX | 3718 | 3 | 40/182 |
| http://204.199.201.133:999 | MX | 5443 | 3 | 39/170 |
| http://206.135.56.50:8080 | MX | 5999 | 3 | 54/156 |
| http://124.105.196.148:8081 | PH | 6836 | 3 | 21/59 |
