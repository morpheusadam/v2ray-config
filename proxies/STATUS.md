# Proxy status

Generated 2026-11-15T19:38:39Z by `harvest.py`.

- **1140** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3250** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34154** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 138/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2443 |
| socks5 | 796 |
| socks4 | 11 |

| country | entries |
|---|---|
| ID | 762 |
| NL | 557 |
| ?? | 166 |
| PH | 138 |
| US | 129 |
| CO | 105 |
| MX | 101 |
| IN | 74 |
| BR | 73 |
| TH | 70 |
| VE | 64 |
| CN | 62 |
| RU | 62 |
| TR | 62 |
| BD | 58 |
| AR | 48 |
| EC | 46 |
| VN | 45 |
| DO | 43 |
| ZA | 33 |
| PE | 32 |
| PK | 31 |
| SG | 31 |
| DE | 28 |
| JP | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-11-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 82 | 82 | 11 | 2026-11-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 90 | 90 | 21 | 2026-11-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-11-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 111 | 111 | 13 | 2026-11-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-11-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 213 | 213 | 146 | 2026-11-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 246 | 246 | 91 | 2026-11-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 267 | 267 | 94 | 2026-11-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 377 | 377 | 52 | 2026-11-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-11-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-11-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1709 | 1709 | 111 | 2026-11-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2263 | 2263 | 676 | 2026-11-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2283 | 2283 | 490 | 2026-11-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2390 | 2390 | 1440 | 2026-11-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5386 | 5386 | 4096 | 2026-11-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10867 | 10867 | 1963 | 2026-11-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 4173 | 64 | 174/193 |
| http://34.43.46.91:80 | US | 5322 | 63 | 187/193 |
| http://130.110.103.245:3128 | SA | 2316 | 39 | 175/193 |
| http://45.189.57.114:3129 | EC | 1271 | 35 | 35/35 |
| http://45.186.6.104:3128 | EC | 1012 | 23 | 162/171 |
| http://38.180.18.103:3128 | BE | 996 | 22 | 22/22 |
| http://27.147.155.206:12051 | BD | 3373 | 13 | 13/13 |
| http://167.172.76.176:9090 | SG | 2323 | 9 | 113/154 |
| http://128.199.121.61:9090 | SG | 3878 | 8 | 87/113 |
| http://101.251.204.174:8080 | CN | 2415 | 7 | 100/179 |
| http://177.234.217.235:999 | EC | 4495 | 7 | 83/162 |
| http://57.182.226.41:3128 | JP | 943 | 7 | 7/7 |
| http://104.129.203.85:9480 | US | 317 | 7 | 7/7 |
| http://54.36.150.233:3128 | FR | 1798 | 5 | 11/15 |
| http://141.94.22.37:3128 | FR | 1302 | 5 | 8/9 |
| http://34.100.244.79:80 | IN | 1366 | 5 | 5/5 |
| http://185.238.238.29:58080 | PL | 2602 | 5 | 82/185 |
| http://45.177.16.131:999 | PY | 6932 | 5 | 47/189 |
| http://188.166.178.163:3129 | SG | 4503 | 5 | 5/5 |
| http://200.59.191.27:999 | VE | 3919 | 5 | 128/188 |
| socks5://37.18.73.60:5566 | RU | 1710 | 5 | 41/90 |
| socks5://188.166.178.163:1088 | SG | 3716 | 5 | 5/5 |
| socks5://116.101.73.52:1057 | VN | 6862 | 5 | 5/5 |
| socks5://116.101.73.161:1057 | VN | 5258 | 5 | 5/5 |
| http://190.123.83.137:999 | AR | 3425 | 4 | 26/30 |
| http://15.229.149.81:1080 | BR | 3542 | 4 | 51/95 |
| http://201.28.86.18:61804 | BR | 3349 | 4 | 12/14 |
| http://177.234.217.45:999 | EC | 7829 | 4 | 48/124 |
| http://45.245.208.180:8080 | EG | 2221 | 4 | 45/66 |
| http://103.148.45.175:8080 | ID | 4478 | 4 | 7/19 |
| socks4://116.101.73.52:1082 | VN | 3855 | 4 | 7/8 |
| http://109.236.45.95:8989 | AL | 3224 | 3 | 57/189 |
| http://184.75.221.82:3118 | CA | 460 | 3 | 137/158 |
| http://181.74.82.91:999 | CL | 2190 | 3 | 31/152 |
| http://45.65.138.48:999 | CO | 3571 | 3 | 93/193 |
| http://181.129.183.19:53281 | CO | 7124 | 3 | 42/188 |
| http://190.71.72.85:2525 | CO | 1459 | 3 | 36/78 |
| http://103.237.102.191:11111 | DE | 2444 | 3 | 182/193 |
| http://177.234.217.43:999 | EC | 3683 | 3 | 57/166 |
| http://217.52.247.88:1981 | EG | 3303 | 3 | 3/3 |
| http://18.175.170.244:23666 | GB | 1762 | 3 | 38/105 |
| http://103.144.54.53:8082 | ID | 4365 | 3 | 22/75 |
| http://103.151.23.89:8082 | ID | 2924 | 3 | 33/91 |
| http://103.156.17.125:8818 | ID | 4705 | 3 | 33/177 |
| http://103.179.252.235:8080 | ID | 3600 | 3 | 37/178 |
| http://163.223.37.71:7777 | ID | 7467 | 3 | 9/22 |
| http://45.174.243.160:999 | MX | 6679 | 3 | 32/137 |
| http://189.51.168.165:999 | MX | 5279 | 3 | 96/105 |
| http://139.5.75.83:8080 | NP | 7089 | 3 | 23/165 |
| http://38.158.83.65:999 | PE | 3113 | 3 | 27/135 |
| http://190.237.238.94:999 | PE | 7644 | 3 | 5/7 |
| http://126.209.53.149:8181 | PH | 4107 | 3 | 16/87 |
| http://13.215.184.250:3128 | SG | 7858 | 3 | 34/79 |
| http://89.43.135.9:8080 | SY | 7584 | 3 | 3/3 |
| http://45.86.72.52:8080 | US | 4820 | 3 | 5/7 |
| http://38.172.181.0:999 | VE | 2064 | 3 | 53/100 |
| http://154.59.56.78:999 | VE | 3198 | 3 | 102/149 |
| http://14.224.183.185:8080 | VN | 7147 | 3 | 22/57 |
| http://16.28.29.244:8689 | ZA | 3629 | 3 | 8/32 |
| socks5://118.179.93.24:9090 | BD | 1832 | 3 | 41/141 |
| socks5://216.144.231.107:1080 | CA | 7792 | 3 | 3/3 |
| socks5://27.219.186.8:1081 | CN | 5130 | 3 | 8/20 |
| socks5://5.75.133.113:10802 | DE | 6655 | 3 | 53/118 |
| socks5://138.124.66.203:1080 | DE | 2621 | 3 | 5/21 |
| socks5://43.155.215.149:20000 | KR | 1782 | 3 | 14/69 |
| socks5://45.74.31.47:4817 | NL | 4581 | 3 | 3/3 |
| socks5://107.174.30.92:1080 | US | 4437 | 3 | 49/89 |
| socks5://116.101.73.52:1081 | VN | 4304 | 3 | 4/6 |
| http://38.226.251.66:999 | AR | 7426 | 2 | 16/103 |
| http://45.65.226.170:999 | AR | 3028 | 2 | 23/44 |
| http://45.65.226.171:999 | AR | 7758 | 2 | 17/31 |
| http://190.210.62.131:8080 | AR | 5929 | 2 | 12/66 |
| http://27.147.156.174:12051 | BD | 3371 | 2 | 5/9 |
| http://143.0.203.173:8080 | BR | 5151 | 2 | 37/183 |
| http://187.102.14.135:8888 | BR | 5694 | 2 | 4/5 |
| http://102.244.78.61:8083 | CM | 1714 | 2 | 64/81 |
| http://102.244.78.61:8084 | CM | 1637 | 2 | 62/81 |
| http://102.244.78.61:8086 | CM | 1975 | 2 | 63/81 |
| http://102.244.78.61:8089 | CM | 1773 | 2 | 65/81 |
| http://106.14.104.209:8080 | CN | 3536 | 2 | 6/23 |
| http://114.244.221.178:8888 | CN | 1639 | 2 | 59/116 |
| http://114.252.13.224:8888 | CN | 7349 | 2 | 58/157 |
| http://8.242.153.166:999 | CO | 5222 | 2 | 7/51 |
| http://24.152.58.22:999 | CO | 4023 | 2 | 19/168 |
| http://24.152.58.107:999 | CO | 7380 | 2 | 28/162 |
| http://24.152.58.125:999 | CO | 5801 | 2 | 23/78 |
| http://64.204.90.17:999 | CO | 7095 | 2 | 9/12 |
| http://181.119.67.133:999 | CO | 3601 | 2 | 25/122 |
| http://181.174.231.152:999 | CO | 5038 | 2 | 7/19 |
| http://181.204.81.179:999 | CO | 6508 | 2 | 24/124 |
| http://38.156.23.99:999 | DO | 4655 | 2 | 4/23 |
| http://152.0.60.100:999 | DO | 6611 | 2 | 8/17 |
| http://154.59.207.8:999 | DO | 4014 | 2 | 7/13 |
| http://45.185.163.111:999 | EC | 2446 | 2 | 9/13 |
| http://177.234.217.44:999 | EC | 5062 | 2 | 35/93 |
| http://177.234.217.46:999 | EC | 6655 | 2 | 53/140 |
| http://186.33.41.48:999 | EC | 6351 | 2 | 21/66 |
| http://190.12.150.244:999 | EC | 5140 | 2 | 139/189 |
| http://80.78.128.94:8080 | ES | 5952 | 2 | 32/182 |
| http://178.134.242.26:8080 | GE | 1728 | 2 | 4/8 |
