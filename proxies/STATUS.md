# Proxy status

Generated 2026-11-06T00:33:00Z by `harvest.py`.

- **4088** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **36893** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 184/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3531 |
| socks5 | 2457 |
| socks4 | 12 |

| country | entries |
|---|---|
| NL | 2411 |
| ID | 1004 |
| ?? | 213 |
| PH | 174 |
| CO | 157 |
| US | 144 |
| MX | 139 |
| TH | 126 |
| TR | 123 |
| BR | 97 |
| CH | 93 |
| IN | 83 |
| EC | 72 |
| VE | 72 |
| CN | 69 |
| BD | 66 |
| AR | 63 |
| DO | 61 |
| RU | 56 |
| SG | 44 |
| PK | 40 |
| EG | 39 |
| PE | 37 |
| CA | 28 |
| SY | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 39 | 2026-11-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 69 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 197 | 197 | 41 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 198 | 198 | 21 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 228 | 228 | 164 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1200 | 1200 | 338 | 2026-11-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1235 | 1235 | 55 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1585 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1817 | 1817 | 659 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1882 | 1882 | 496 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2429 | 2429 | 1243 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 2462 | 2462 | 1085 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4116 | 4116 | 1377 | 2026-11-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5005 | 5005 | 3788 | 2026-11-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11463 | 11463 | 1974 | 2026-11-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 509 | 85 | 85/85 |
| http://103.237.102.191:11111 | DE | 1076 | 61 | 167/174 |
| http://103.133.26.73:3128 | ID | 1483 | 50 | 70/152 |
| http://176.111.37.5:39811 | HK | 1300 | 45 | 155/174 |
| http://34.43.46.91:80 | US | 1081 | 44 | 168/174 |
| http://4.144.146.21:80 | SG | 1102 | 42 | 59/66 |
| http://176.111.37.216:39811 | HK | 1031 | 37 | 146/174 |
| http://34.43.46.91:443 | US | 735 | 23 | 163/174 |
| socks5://101.36.104.239:10808 | JP | 1426 | 21 | 150/174 |
| http://130.110.103.245:3128 | SA | 1343 | 20 | 156/174 |
| socks5://193.25.215.182:22222 | US | 1009 | 20 | 147/174 |
| http://103.133.26.72:8080 | ID | 1406 | 17 | 54/100 |
| http://45.189.57.114:3129 | EC | 770 | 16 | 16/16 |
| http://123.200.8.170:10000 | BD | 3046 | 13 | 80/172 |
| http://102.244.78.61:8082 | CM | 1315 | 13 | 52/63 |
| http://190.12.150.244:999 | EC | 1790 | 13 | 126/170 |
| http://154.59.56.72:999 | VE | 1923 | 13 | 100/133 |
| socks5://69.55.49.177:38182 | US | 861 | 13 | 28/29 |
| http://165.154.162.73:8888 | US | 2724 | 12 | 117/174 |
| socks5://45.61.129.165:9050 | US | 1737 | 12 | 133/174 |
| http://190.123.83.137:999 | AR | 2192 | 11 | 11/11 |
| http://190.0.246.213:4040 | CO | 1761 | 11 | 129/139 |
| http://189.51.168.165:999 | MX | 408 | 11 | 80/86 |
| http://154.59.56.74:999 | VE | 4401 | 11 | 94/137 |
| http://45.65.137.218:999 | CO | 1562 | 10 | 62/139 |
| http://131.221.40.131:4040 | CO | 533 | 10 | 12/13 |
| http://103.133.26.119:8080 | ID | 1834 | 10 | 53/84 |
| http://140.238.32.108:3128 | JP | 1019 | 10 | 99/173 |
| http://82.152.138.127:999 | MX | 424 | 10 | 50/136 |
| http://189.51.168.164:999 | MX | 571 | 10 | 10/10 |
| http://152.42.170.187:9090 | SG | 1270 | 10 | 10/10 |
| http://49.229.100.235:8080 | TH | 1479 | 10 | 82/122 |
| http://171.100.254.137:8080 | TH | 2246 | 10 | 10/10 |
| http://185.191.239.248:3128 | CH | 1117 | 9 | 125/173 |
| http://102.244.78.61:8080 | CM | 1290 | 9 | 52/63 |
| http://41.33.245.139:1976 | EG | 1017 | 9 | 12/13 |
| http://43.161.254.16:3128 | HK | 1112 | 9 | 11/14 |
| http://103.130.61.61:8081 | ID | 2234 | 9 | 143/174 |
| http://61.91.162.126:8080 | TH | 1683 | 9 | 87/117 |
| http://103.10.231.189:8080 | TH | 2068 | 9 | 114/159 |
| http://45.65.224.125:999 | AR | 4023 | 8 | 26/36 |
| http://184.75.221.82:3118 | CA | 183 | 8 | 121/139 |
| http://123.121.122.142:8888 | CN | 2030 | 8 | 13/20 |
| http://190.0.246.210:4040 | CO | 3344 | 8 | 159/173 |
| http://177.234.217.93:999 | EC | 2305 | 8 | 22/33 |
| http://34.88.38.81:9443 | FI | 850 | 8 | 97/139 |
| http://35.228.49.168:9443 | FI | 659 | 8 | 78/111 |
| http://103.133.26.50:8080 | ID | 1472 | 8 | 48/75 |
| socks4://188.226.27.24:1080 | RU | 2540 | 8 | 9/10 |
| http://200.10.31.42:8081 | CO | 4552 | 7 | 25/47 |
| http://84.36.141.180:1981 | EG | 1408 | 7 | 27/125 |
| http://103.18.79.197:8085 | ID | 5180 | 7 | 35/110 |
| http://159.223.41.216:9090 | SG | 1082 | 7 | 98/134 |
| http://38.63.98.32:999 | VE | 7520 | 7 | 21/62 |
| socks5://5.255.117.250:1080 | NL | 704 | 7 | 55/159 |
| socks5://43.156.137.7:10808 | SG | 6201 | 7 | 7/7 |
| http://181.78.195.137:999 | EC | 6783 | 6 | 64/174 |
| http://181.188.203.112:999 | EC | 3917 | 6 | 57/166 |
| http://41.128.77.76:1981 | EG | 962 | 6 | 57/128 |
| http://103.61.234.186:8180 | ID | 5856 | 6 | 75/171 |
| http://125.27.241.98:8080 | TH | 4619 | 6 | 11/20 |
| http://154.59.56.73:999 | VE | 6007 | 6 | 104/146 |
| http://187.102.219.34:999 | AR | 4160 | 5 | 70/125 |
| http://187.86.161.2:8080 | BR | 6775 | 5 | 9/10 |
| http://102.244.78.61:8086 | CM | 1246 | 5 | 50/62 |
| http://102.244.78.61:8089 | CM | 1278 | 5 | 49/62 |
| http://38.19.50.74:999 | CO | 2461 | 5 | 7/10 |
| http://181.48.159.22:3128 | CO | 714 | 5 | 18/58 |
| http://196.204.26.243:1981 | EG | 1517 | 5 | 36/109 |
| http://198.244.254.77:3128 | GB | 3716 | 5 | 50/58 |
| http://47.238.255.80:3128 | HK | 7241 | 5 | 7/8 |
| http://45.198.32.223:8080 | ID | 4812 | 5 | 32/94 |
| http://185.166.27.208:2020 | IQ | 3974 | 5 | 7/8 |
| http://182.52.113.84:80 | TH | 5591 | 5 | 13/46 |
| http://193.164.7.235:8082 | TR | 1062 | 5 | 5/5 |
| socks5://45.74.31.46:16479 | NL | 2565 | 5 | 5/5 |
| socks5://45.74.31.46:6386 | NL | 5986 | 5 | 12/45 |
| socks5://45.74.31.46:8640 | NL | 2551 | 5 | 8/17 |
| socks5://193.218.118.128:1080 | UA | 1635 | 5 | 24/30 |
| http://45.65.226.171:999 | AR | 3980 | 4 | 8/12 |
| http://45.178.55.2:999 | AR | 6412 | 4 | 6/15 |
| http://15.229.149.81:1080 | BR | 3262 | 4 | 37/76 |
| http://45.183.236.181:8085 | BR | 2960 | 4 | 21/116 |
| http://45.161.112.227:999 | CL | 7485 | 4 | 52/167 |
| http://123.119.179.34:8888 | CN | 1909 | 4 | 55/136 |
| http://38.156.76.112:999 | CO | 3775 | 4 | 31/161 |
| http://179.1.221.26:3128 | CO | 6789 | 4 | 42/114 |
| http://190.90.21.35:999 | CO | 3791 | 4 | 15/64 |
| http://200.125.170.226:999 | DO | 4086 | 4 | 4/4 |
| http://45.186.6.104:3128 | EC | 643 | 4 | 143/152 |
| http://145.236.156.89:8080 | HU | 2199 | 4 | 4/4 |
| http://45.198.10.189:9191 | ID | 4934 | 4 | 5/13 |
| http://103.123.64.234:3128 | ID | 5544 | 4 | 7/12 |
| http://103.156.57.135:9988 | ID | 4719 | 4 | 33/114 |
| http://103.169.188.34:8080 | ID | 6348 | 4 | 6/12 |
| http://103.177.153.121:8080 | ID | 4025 | 4 | 4/4 |
| http://157.66.16.38:8070 | ID | 7869 | 4 | 13/84 |
| http://160.187.174.249:80 | ID | 5816 | 4 | 12/43 |
| http://203.210.85.215:8080 | ID | 6802 | 4 | 4/4 |
| http://40.192.70.191:4980 | IN | 3416 | 4 | 4/4 |
