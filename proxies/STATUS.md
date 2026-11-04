# Proxy status

Generated 2026-11-04T20:36:00Z by `harvest.py`.

- **4698** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **37567** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 265/600 (44%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 4113 |
| socks5 | 1882 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 1738 |
| ID | 1197 |
| ?? | 700 |
| CO | 182 |
| PH | 174 |
| MX | 150 |
| US | 141 |
| TH | 126 |
| TR | 109 |
| BR | 95 |
| IN | 79 |
| RU | 79 |
| BD | 74 |
| DO | 71 |
| CN | 69 |
| AR | 67 |
| EC | 66 |
| VE | 61 |
| PE | 49 |
| PK | 48 |
| EG | 42 |
| SG | 39 |
| DE | 38 |
| CL | 33 |
| SY | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-11-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 40 | 2026-11-04 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 66 | 2026-11-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 374 | 374 | 219 | 2026-11-04 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 479 | 479 | 144 | 2026-11-04 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 580 | 580 | 140 | 2026-11-04 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 444 | 2026-11-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1119 | 2026-11-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1608 | 1608 | 737 | 2026-11-04 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-04 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1897 | 1897 | 0 | 2026-11-04 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1954 | 1954 | 549 | 2026-11-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2696 | 2696 | 660 | 2026-11-04 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 3326 | 3326 | 1304 | 2026-11-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3728 | 3728 | 1944 | 2026-11-04 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4514 | 4514 | 1465 | 2026-11-04 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5000 | 5000 | 3754 | 2026-11-04 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12214 | 12213 | 2423 | 2026-11-04 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 454 | 82 | 82/82 |
| http://103.237.102.191:11111 | DE | 1192 | 58 | 164/171 |
| http://103.133.26.73:3128 | ID | 1595 | 47 | 67/149 |
| http://176.111.37.5:39811 | HK | 1500 | 42 | 152/171 |
| http://34.43.46.91:80 | US | 3655 | 41 | 165/171 |
| http://4.144.146.21:80 | SG | 1178 | 39 | 56/63 |
| http://176.111.37.216:39811 | HK | 881 | 34 | 143/171 |
| http://34.43.46.91:443 | US | 543 | 20 | 160/171 |
| socks5://101.36.104.239:10808 | JP | 1181 | 18 | 147/171 |
| http://130.110.103.245:3128 | SA | 1544 | 17 | 153/171 |
| socks5://193.25.215.182:22222 | US | 872 | 17 | 144/171 |
| http://103.133.26.72:8080 | ID | 2218 | 14 | 51/97 |
| http://45.189.57.114:3129 | EC | 670 | 13 | 13/13 |
| http://102.244.78.61:8085 | CM | 1206 | 12 | 49/61 |
| http://38.172.160.16:999 | VE | 4649 | 11 | 74/122 |
| http://45.65.224.74:999 | AR | 1890 | 10 | 29/36 |
| http://123.200.8.170:10000 | BD | 1996 | 10 | 77/169 |
| http://102.244.78.61:8082 | CM | 1204 | 10 | 49/60 |
| http://190.12.150.244:999 | EC | 1428 | 10 | 123/167 |
| http://154.59.56.72:999 | VE | 2573 | 10 | 97/130 |
| socks5://69.55.49.177:38182 | US | 136 | 10 | 25/26 |
| http://186.96.111.214:999 | CO | 6953 | 9 | 79/160 |
| http://195.226.213.251:8888 | UA | 1613 | 9 | 69/165 |
| http://165.154.162.73:8888 | US | 975 | 9 | 114/171 |
| socks5://45.61.129.165:9050 | US | 6447 | 9 | 130/171 |
| http://190.123.83.137:999 | AR | 1052 | 8 | 8/8 |
| http://190.0.246.213:4040 | CO | 1437 | 8 | 126/136 |
| http://189.51.168.165:999 | MX | 333 | 8 | 77/83 |
| http://154.59.56.74:999 | VE | 6921 | 8 | 91/134 |
| socks5://101.36.104.46:10808 | JP | 1211 | 8 | 147/171 |
| http://128.201.30.222:8666 | BR | 1871 | 7 | 10/17 |
| http://8.243.167.51:999 | CO | 5633 | 7 | 17/58 |
| http://45.65.137.218:999 | CO | 5770 | 7 | 59/136 |
| http://131.221.40.131:4040 | CO | 486 | 7 | 9/10 |
| http://177.234.217.83:999 | EC | 3320 | 7 | 14/18 |
| http://177.234.217.92:999 | EC | 2591 | 7 | 15/20 |
| http://103.133.26.119:8080 | ID | 1995 | 7 | 50/81 |
| http://160.19.146.221:2022 | ID | 4107 | 7 | 40/136 |
| http://160.22.45.114:8080 | ID | 5053 | 7 | 19/30 |
| http://202.47.185.153:8090 | ID | 3366 | 7 | 29/126 |
| http://140.238.32.108:3128 | JP | 3060 | 7 | 96/170 |
| http://82.152.138.127:999 | MX | 333 | 7 | 47/133 |
| http://189.51.168.164:999 | MX | 339 | 7 | 7/7 |
| http://152.42.170.187:9090 | SG | 2571 | 7 | 7/7 |
| http://49.229.100.235:8080 | TH | 1607 | 7 | 79/119 |
| http://171.100.254.137:8080 | TH | 1557 | 7 | 7/7 |
| socks5://176.124.206.150:8443 | FI | 826 | 7 | 7/7 |
| http://187.102.219.64:999 | AR | 1124 | 6 | 68/110 |
| http://185.191.239.248:3128 | CH | 839 | 6 | 122/170 |
| http://102.244.78.61:8080 | CM | 1186 | 6 | 49/60 |
| http://102.244.78.61:8084 | CM | 1214 | 6 | 47/59 |
| http://114.244.221.178:8888 | CN | 1756 | 6 | 49/94 |
| http://41.33.245.139:1976 | EG | 1214 | 6 | 9/10 |
| http://43.161.254.16:3128 | HK | 1721 | 6 | 8/11 |
| http://103.130.61.61:8081 | ID | 1908 | 6 | 140/171 |
| http://103.172.42.123:1111 | ID | 2482 | 6 | 31/169 |
| http://103.193.145.51:8080 | ID | 1572 | 6 | 6/6 |
| http://161.248.176.2:8080 | IN | 6397 | 6 | 25/100 |
| http://128.199.116.219:9090 | SG | 1172 | 6 | 71/90 |
| http://61.91.162.126:8080 | TH | 1592 | 6 | 84/114 |
| http://103.10.231.189:8080 | TH | 1932 | 6 | 111/156 |
| http://38.172.181.0:999 | VE | 7279 | 6 | 38/78 |
| socks5://84.200.89.140:1080 | DE | 621 | 6 | 6/6 |
| socks5://103.191.218.119:69 | ID | 4604 | 6 | 44/157 |
| http://45.65.224.125:999 | AR | 1909 | 5 | 23/33 |
| http://103.134.56.148:8080 | BD | 5624 | 5 | 36/113 |
| http://184.75.221.82:3118 | CA | 271 | 5 | 118/136 |
| http://192.18.158.84:3128 | CA | 7158 | 5 | 5/5 |
| http://27.185.218.213:17981 | CN | 2199 | 5 | 67/171 |
| http://123.121.122.142:8888 | CN | 3958 | 5 | 10/17 |
| http://190.0.246.210:4040 | CO | 997 | 5 | 156/170 |
| http://38.50.165.126:999 | DO | 5032 | 5 | 26/94 |
| http://177.234.217.93:999 | EC | 4852 | 5 | 19/30 |
| http://41.33.89.100:1976 | EG | 2979 | 5 | 11/33 |
| http://37.59.138.176:8080 | ES | 5992 | 5 | 31/113 |
| http://34.88.38.81:9443 | FI | 853 | 5 | 94/136 |
| http://35.228.49.168:9443 | FI | 641 | 5 | 75/108 |
| http://47.86.97.230:18080 | HK | 3057 | 5 | 6/14 |
| http://164.163.73.5:999 | HN | 5791 | 5 | 51/171 |
| http://181.78.44.63:999 | HN | 6494 | 5 | 36/95 |
| http://200.52.148.212:999 | HN | 4051 | 5 | 14/33 |
| http://36.95.245.7:8090 | ID | 3285 | 5 | 7/9 |
| http://103.98.117.98:8080 | ID | 3152 | 5 | 8/11 |
| http://103.133.26.50:8080 | ID | 1578 | 5 | 45/72 |
| http://103.144.54.73:8082 | ID | 1525 | 5 | 55/116 |
| http://103.145.34.112:1111 | ID | 1513 | 5 | 31/143 |
| http://103.147.134.65:8082 | ID | 2653 | 5 | 30/108 |
| http://103.168.254.198:8080 | ID | 3851 | 5 | 22/35 |
| http://103.175.238.110:8082 | ID | 5606 | 5 | 28/127 |
| http://103.208.103.30:8080 | ID | 2847 | 5 | 14/26 |
| http://151.158.133.147:8080 | ID | 5250 | 5 | 12/24 |
| http://160.22.207.73:8082 | ID | 5000 | 5 | 20/47 |
| http://203.175.103.193:8080 | ID | 3391 | 5 | 11/24 |
| http://18.61.230.250:36925 | IN | 3828 | 5 | 37/138 |
| http://93.118.120.60:8080 | IR | 2321 | 5 | 13/38 |
| http://103.167.116.166:8087 | PH | 6027 | 5 | 7/10 |
| http://152.42.177.32:8888 | SG | 1172 | 5 | 86/131 |
| http://159.138.84.187:3128 | SG | 1188 | 5 | 5/5 |
| http://195.142.25.185:8080 | TR | 4504 | 5 | 6/7 |
| http://18.217.248.118:5050 | US | 2681 | 5 | 6/7 |
