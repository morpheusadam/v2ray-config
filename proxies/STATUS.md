# Proxy status

Generated 2026-11-06T20:17:08Z by `harvest.py`.

- **3342** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **36075** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 156/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3443 |
| socks5 | 2541 |
| socks4 | 16 |

| country | entries |
|---|---|
| NL | 2409 |
| ID | 1031 |
| ?? | 308 |
| PH | 168 |
| CO | 150 |
| US | 128 |
| MX | 118 |
| TH | 115 |
| TR | 114 |
| BR | 87 |
| VE | 87 |
| IN | 79 |
| BD | 70 |
| CH | 68 |
| CN | 68 |
| EC | 67 |
| AR | 64 |
| DO | 48 |
| VN | 44 |
| PE | 42 |
| RU | 42 |
| EG | 41 |
| ZA | 39 |
| SG | 36 |
| PK | 34 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 3 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 79 | 79 | 13 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 97 | 97 | 14 | 2026-11-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 43 | 2026-11-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 72 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 202 | 202 | 96 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 248 | 248 | 169 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 305 | 305 | 35 | 2026-11-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 864 | 864 | 190 | 2026-11-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1458 | 1458 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1582 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2009 | 2009 | 655 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2629 | 2629 | 1369 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4055 | 4055 | 1379 | 2026-11-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5034 | 5034 | 3828 | 2026-11-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11829 | 11829 | 2301 | 2026-11-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 466 | 86 | 86/86 |
| http://103.237.102.191:11111 | DE | 920 | 62 | 168/175 |
| http://103.133.26.73:3128 | ID | 1482 | 51 | 71/153 |
| http://176.111.37.5:39811 | HK | 957 | 46 | 156/175 |
| http://34.43.46.91:80 | US | 2233 | 45 | 169/175 |
| http://4.144.146.21:80 | SG | 1040 | 43 | 60/67 |
| http://176.111.37.216:39811 | HK | 891 | 38 | 147/175 |
| http://34.43.46.91:443 | US | 349 | 24 | 164/175 |
| socks5://101.36.104.239:10808 | JP | 1582 | 22 | 151/175 |
| http://130.110.103.245:3128 | SA | 1174 | 21 | 157/175 |
| socks5://193.25.215.182:22222 | US | 1531 | 21 | 148/175 |
| http://103.133.26.72:8080 | ID | 1414 | 18 | 55/101 |
| http://45.189.57.114:3129 | EC | 948 | 17 | 17/17 |
| http://123.200.8.170:10000 | BD | 4072 | 14 | 81/173 |
| http://102.244.78.61:8082 | CM | 1568 | 14 | 53/64 |
| http://190.12.150.244:999 | EC | 2158 | 14 | 127/171 |
| socks5://69.55.49.177:38182 | US | 507 | 14 | 29/30 |
| http://165.154.162.73:8888 | US | 2519 | 13 | 118/175 |
| socks5://45.61.129.165:9050 | US | 2168 | 13 | 134/175 |
| http://190.123.83.137:999 | AR | 3640 | 12 | 12/12 |
| http://190.0.246.213:4040 | CO | 610 | 12 | 130/140 |
| http://189.51.168.165:999 | MX | 479 | 12 | 81/87 |
| http://154.59.56.74:999 | VE | 2783 | 12 | 95/138 |
| http://103.133.26.119:8080 | ID | 1918 | 11 | 54/85 |
| http://82.152.138.127:999 | MX | 5364 | 11 | 51/137 |
| http://189.51.168.164:999 | MX | 2111 | 11 | 11/11 |
| http://152.42.170.187:9090 | SG | 1055 | 11 | 11/11 |
| http://49.229.100.235:8080 | TH | 1425 | 11 | 83/123 |
| http://171.100.254.137:8080 | TH | 1444 | 11 | 11/11 |
| http://185.191.239.248:3128 | CH | 1536 | 10 | 126/174 |
| http://102.244.78.61:8080 | CM | 1697 | 10 | 53/64 |
| http://41.33.245.139:1976 | EG | 2632 | 10 | 13/14 |
| http://43.161.254.16:3128 | HK | 937 | 10 | 12/15 |
| http://103.130.61.61:8081 | ID | 1584 | 10 | 144/175 |
| http://61.91.162.126:8080 | TH | 1384 | 10 | 88/118 |
| http://103.10.231.189:8080 | TH | 1635 | 10 | 115/160 |
| http://184.75.221.82:3118 | CA | 195 | 9 | 122/140 |
| http://123.121.122.142:8888 | CN | 1810 | 9 | 14/21 |
| http://190.0.246.210:4040 | CO | 1174 | 9 | 160/174 |
| http://177.234.217.93:999 | EC | 1984 | 9 | 23/34 |
| http://34.88.38.81:9443 | FI | 1032 | 9 | 98/140 |
| http://35.228.49.168:9443 | FI | 755 | 9 | 79/112 |
| http://103.133.26.50:8080 | ID | 1397 | 9 | 49/76 |
| http://103.18.79.197:8085 | ID | 5888 | 8 | 36/111 |
| http://159.223.41.216:9090 | SG | 1025 | 8 | 99/135 |
| socks5://5.255.117.250:1080 | NL | 761 | 8 | 56/160 |
| http://181.78.195.137:999 | EC | 6160 | 7 | 65/175 |
| http://181.188.203.112:999 | EC | 2186 | 7 | 58/167 |
| http://41.128.77.76:1981 | EG | 2503 | 7 | 58/129 |
| http://103.61.234.186:8180 | ID | 4864 | 7 | 76/172 |
| http://154.59.56.73:999 | VE | 1789 | 7 | 105/147 |
| http://187.102.219.34:999 | AR | 1939 | 6 | 71/126 |
| http://187.86.161.2:8080 | BR | 3195 | 6 | 10/11 |
| http://102.244.78.61:8086 | CM | 1362 | 6 | 51/63 |
| http://102.244.78.61:8089 | CM | 1622 | 6 | 50/63 |
| http://38.19.50.74:999 | CO | 7962 | 6 | 8/11 |
| http://196.204.26.243:1981 | EG | 2162 | 6 | 37/110 |
| http://198.244.254.77:3128 | GB | 6743 | 6 | 51/59 |
| http://47.238.255.80:3128 | HK | 2813 | 6 | 8/9 |
| http://185.166.27.208:2020 | IQ | 7100 | 6 | 8/9 |
| http://182.52.113.84:80 | TH | 2934 | 6 | 14/47 |
| http://15.229.149.81:1080 | BR | 6457 | 5 | 38/77 |
| http://45.183.236.181:8085 | BR | 2332 | 5 | 22/117 |
| http://38.156.76.112:999 | CO | 5209 | 5 | 32/162 |
| http://190.90.21.35:999 | CO | 3195 | 5 | 16/65 |
| http://200.125.170.226:999 | DO | 6252 | 5 | 5/5 |
| http://45.186.6.104:3128 | EC | 802 | 5 | 144/153 |
| http://45.198.10.189:9191 | ID | 4241 | 5 | 6/14 |
| http://103.156.57.135:9988 | ID | 4148 | 5 | 34/115 |
| http://103.177.153.121:8080 | ID | 7273 | 5 | 5/5 |
| http://160.187.174.249:80 | ID | 6438 | 5 | 13/44 |
| http://203.210.85.215:8080 | ID | 4906 | 5 | 5/5 |
| http://157.20.229.225:8080 | IN | 5061 | 5 | 5/5 |
| http://38.194.246.34:999 | MX | 1931 | 5 | 97/166 |
| http://206.135.47.107:999 | MX | 6394 | 5 | 26/45 |
| http://185.238.238.29:58080 | PL | 5069 | 5 | 71/167 |
| http://185.238.238.49:58080 | PL | 1806 | 5 | 62/169 |
| http://185.238.238.169:58080 | PL | 1819 | 5 | 49/97 |
| http://104.248.151.93:9090 | SG | 1036 | 5 | 55/76 |
| http://167.99.74.174:9090 | SG | 1024 | 5 | 88/135 |
| socks5://113.249.111.67:1080 | CN | 3954 | 5 | 63/142 |
| socks5://5.255.113.177:1080 | NL | 747 | 5 | 26/73 |
| socks5://45.74.31.42:7010 | NL | 2933 | 5 | 5/5 |
| socks5://171.25.158.95:1080 | SE | 2967 | 5 | 72/90 |
| socks5://45.61.188.134:44499 | US | 957 | 5 | 76/142 |
| http://114.130.153.122:58080 | BD | 5259 | 4 | 4/4 |
| http://38.180.18.103:3128 | BE | 682 | 4 | 4/4 |
| http://15.229.149.81:3128 | BR | 3059 | 4 | 52/85 |
| http://45.232.210.97:999 | CL | 4014 | 4 | 11/23 |
| http://102.244.78.61:8081 | CM | 1358 | 4 | 49/61 |
| http://102.244.78.61:8087 | CM | 1485 | 4 | 51/65 |
| http://114.249.209.219:8888 | CN | 1551 | 4 | 49/133 |
| http://123.121.122.28:8888 | CN | 1633 | 4 | 76/124 |
| http://45.65.138.48:999 | CO | 7149 | 4 | 79/175 |
| http://38.75.82.221:999 | DO | 3528 | 4 | 53/175 |
| http://186.33.41.48:999 | EC | 4921 | 4 | 14/48 |
| http://41.128.77.76:1976 | EG | 3648 | 4 | 59/141 |
| http://81.19.210.10:80 | GB | 1067 | 4 | 25/36 |
| http://104.194.146.9:80 | GB | 4275 | 4 | 15/21 |
| http://43.155.62.157:443 | HK | 6034 | 4 | 67/78 |
