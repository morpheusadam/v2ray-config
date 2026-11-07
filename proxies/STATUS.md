# Proxy status

Generated 2026-11-07T18:22:40Z by `harvest.py`.

- **2488** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35755** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 143/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3578 |
| socks5 | 2407 |
| socks4 | 15 |

| country | entries |
|---|---|
| NL | 2285 |
| ID | 1154 |
| ?? | 406 |
| PH | 178 |
| CO | 151 |
| US | 125 |
| MX | 121 |
| TH | 118 |
| TR | 107 |
| VE | 92 |
| BR | 83 |
| BD | 81 |
| IN | 73 |
| AR | 68 |
| CN | 67 |
| EC | 57 |
| DO | 55 |
| PE | 46 |
| EG | 45 |
| VN | 39 |
| PK | 37 |
| RU | 34 |
| ZA | 33 |
| SG | 31 |
| DE | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-11-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 67 | 67 | 13 | 2026-11-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 79 | 79 | 15 | 2026-11-07 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 138 | 138 | 16 | 2026-11-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 40 | 2026-11-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 81 | 2026-11-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 195 | 195 | 148 | 2026-11-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 222 | 222 | 76 | 2026-11-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-07 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-11-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 835 | 835 | 137 | 2026-11-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1568 | 1568 | 134 | 2026-11-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-11-07 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1631 | 1631 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2130 | 2130 | 634 | 2026-11-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2562 | 2562 | 1442 | 2026-11-07 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5114 | 5114 | 3927 | 2026-11-07 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11166 | 11166 | 1749 | 2026-11-07 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 406 | 88 | 88/88 |
| http://103.133.26.73:3128 | ID | 1573 | 53 | 73/155 |
| http://176.111.37.5:39811 | HK | 815 | 48 | 158/177 |
| http://34.43.46.91:80 | US | 1567 | 47 | 171/177 |
| http://4.144.146.21:80 | SG | 1196 | 45 | 62/69 |
| http://176.111.37.216:39811 | HK | 775 | 40 | 149/177 |
| http://34.43.46.91:443 | US | 1610 | 26 | 166/177 |
| socks5://101.36.104.239:10808 | JP | 2281 | 24 | 153/177 |
| http://130.110.103.245:3128 | SA | 1283 | 23 | 159/177 |
| http://103.133.26.72:8080 | ID | 3374 | 20 | 57/103 |
| http://45.189.57.114:3129 | EC | 1308 | 19 | 19/19 |
| http://102.244.78.61:8082 | CM | 1221 | 16 | 55/66 |
| http://190.12.150.244:999 | EC | 1973 | 16 | 129/173 |
| socks5://69.55.49.177:38182 | US | 333 | 16 | 31/32 |
| socks5://45.61.129.165:9050 | US | 3306 | 15 | 136/177 |
| http://190.123.83.137:999 | AR | 4478 | 14 | 14/14 |
| http://190.0.246.213:4040 | CO | 5581 | 14 | 132/142 |
| http://103.133.26.119:8080 | ID | 1997 | 13 | 56/87 |
| http://189.51.168.164:999 | MX | 1016 | 13 | 13/13 |
| http://49.229.100.235:8080 | TH | 1583 | 13 | 85/125 |
| http://171.100.254.137:8080 | TH | 1573 | 13 | 13/13 |
| http://102.244.78.61:8080 | CM | 1221 | 12 | 55/66 |
| http://43.161.254.16:3128 | HK | 2839 | 12 | 14/17 |
| http://103.130.61.61:8081 | ID | 3069 | 12 | 146/177 |
| http://61.91.162.126:8080 | TH | 1519 | 12 | 90/120 |
| http://103.10.231.189:8080 | TH | 1806 | 12 | 117/162 |
| http://184.75.221.82:3118 | CA | 2305 | 11 | 124/142 |
| http://123.121.122.142:8888 | CN | 7130 | 11 | 16/23 |
| http://190.0.246.210:4040 | CO | 1408 | 11 | 162/176 |
| http://177.234.217.93:999 | EC | 1956 | 11 | 25/36 |
| http://103.133.26.50:8080 | ID | 1633 | 11 | 51/78 |
| http://181.78.195.137:999 | EC | 2672 | 9 | 67/177 |
| http://41.128.77.76:1981 | EG | 945 | 9 | 60/131 |
| http://102.244.78.61:8086 | CM | 1187 | 8 | 53/65 |
| http://102.244.78.61:8089 | CM | 1222 | 8 | 52/65 |
| http://47.238.255.80:3128 | HK | 3671 | 8 | 10/11 |
| http://200.125.170.226:999 | DO | 5662 | 7 | 7/7 |
| http://45.186.6.104:3128 | EC | 722 | 7 | 146/155 |
| http://103.156.57.135:9988 | ID | 6682 | 7 | 36/117 |
| http://167.99.74.174:9090 | SG | 1164 | 7 | 90/137 |
| socks5://113.249.111.67:1080 | CN | 2321 | 7 | 65/144 |
| socks5://45.61.188.134:44499 | US | 335 | 7 | 78/144 |
| http://38.180.18.103:3128 | BE | 534 | 6 | 6/6 |
| http://102.244.78.61:8081 | CM | 1227 | 6 | 51/63 |
| http://123.121.122.28:8888 | CN | 4620 | 6 | 78/126 |
| http://45.65.138.48:999 | CO | 6094 | 6 | 81/177 |
| http://41.128.77.76:1976 | EG | 4127 | 6 | 61/143 |
| http://108.137.124.195:8123 | ID | 6102 | 6 | 26/94 |
| http://190.97.250.230:999 | VE | 4923 | 6 | 18/38 |
| http://45.65.224.74:999 | AR | 3954 | 5 | 34/42 |
| http://3.26.199.107:1234 | AU | 5415 | 5 | 22/90 |
| http://221.221.154.156:8888 | CN | 1874 | 5 | 42/137 |
| http://190.71.72.85:2525 | CO | 542 | 5 | 21/62 |
| http://103.130.61.60:8081 | ID | 1346 | 5 | 23/33 |
| http://103.162.220.246:8085 | ID | 6058 | 5 | 14/71 |
| http://165.99.192.27:1111 | ID | 4079 | 5 | 10/15 |
| http://79.52.108.2:8081 | IT | 6911 | 5 | 6/7 |
| http://203.177.217.222:8082 | PH | 5155 | 5 | 68/122 |
| http://128.199.113.85:9090 | SG | 1226 | 5 | 7/8 |
| http://180.180.156.96:80 | TH | 4691 | 5 | 9/22 |
| http://44.200.234.67:17046 | US | 7586 | 5 | 37/137 |
| socks4://143.198.239.45:10009 | US | 2107 | 5 | 5/5 |
| socks5://45.74.31.42:6919 | NL | 7454 | 5 | 5/5 |
| socks5://45.74.31.46:4086 | NL | 5946 | 5 | 5/5 |
| http://201.190.178.191:8080 | AR | 4527 | 4 | 30/110 |
| http://3.26.199.107:9904 | AU | 3749 | 4 | 25/87 |
| http://103.148.83.110:8889 | BD | 1930 | 4 | 39/175 |
| http://114.130.153.46:58080 | BD | 7754 | 4 | 6/7 |
| http://102.244.78.61:8085 | CM | 1225 | 4 | 53/67 |
| http://102.244.78.61:8090 | CM | 1230 | 4 | 53/69 |
| http://125.33.195.27:8888 | CN | 6840 | 4 | 50/123 |
| http://38.50.165.126:999 | DO | 2961 | 4 | 31/100 |
| http://41.38.209.16:8080 | EG | 4172 | 4 | 15/28 |
| http://41.128.72.138:1976 | EG | 6120 | 4 | 6/16 |
| http://196.204.26.243:1976 | EG | 1060 | 4 | 35/105 |
| http://34.105.252.3:3128 | GB | 486 | 4 | 36/59 |
| http://200.52.148.212:999 | HN | 2421 | 4 | 18/39 |
| http://101.255.45.46:8080 | ID | 3929 | 4 | 20/49 |
| http://103.46.186.17:8090 | ID | 1498 | 4 | 34/169 |
| http://103.68.215.115:8181 | ID | 6091 | 4 | 20/100 |
| http://103.120.174.75:1818 | ID | 4389 | 4 | 33/161 |
| http://103.153.83.47:8080 | ID | 4432 | 4 | 11/15 |
| http://103.172.17.14:8080 | ID | 1510 | 4 | 29/88 |
| http://103.175.238.110:8082 | ID | 5711 | 4 | 32/133 |
| http://103.176.97.223:3127 | ID | 6829 | 4 | 24/154 |
| http://103.180.118.109:8090 | ID | 4341 | 4 | 6/7 |
| http://103.188.169.95:8080 | ID | 5071 | 4 | 28/144 |
| http://115.178.49.115:8787 | ID | 2536 | 4 | 30/153 |
| http://151.158.133.163:8080 | ID | 3820 | 4 | 7/20 |
| http://157.20.239.237:9090 | ID | 3652 | 4 | 6/17 |
| http://202.47.185.35:8080 | ID | 4231 | 4 | 26/148 |
| http://165.16.2.250:9999 | LY | 4200 | 4 | 7/16 |
| http://38.252.145.15:999 | MX | 5011 | 4 | 23/77 |
| http://192.203.0.210:999 | PR | 7025 | 4 | 31/144 |
| http://1.10.133.83:8081 | TH | 2680 | 4 | 19/39 |
| http://1.10.248.248:80 | TH | 2154 | 4 | 6/16 |
| http://182.52.136.59:80 | TH | 3292 | 4 | 16/34 |
| http://18.224.94.46:18058 | US | 1843 | 4 | 14/23 |
| http://38.172.181.0:999 | VE | 2676 | 4 | 43/84 |
| http://161.22.33.89:999 | VE | 3596 | 4 | 10/14 |
