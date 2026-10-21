# Proxy status

Generated 2026-10-21T22:43:18Z by `harvest.py`.

- **2129** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3993** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39755** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 146/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2204 |
| socks5 | 1779 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 1572 |
| ID | 619 |
| ?? | 255 |
| CO | 115 |
| PH | 106 |
| MX | 97 |
| RU | 92 |
| US | 90 |
| BD | 63 |
| BR | 63 |
| VE | 61 |
| CN | 58 |
| IN | 50 |
| EC | 49 |
| AR | 41 |
| TR | 41 |
| DE | 39 |
| DO | 38 |
| SG | 38 |
| TH | 35 |
| VN | 27 |
| CL | 25 |
| PK | 25 |
| ZA | 23 |
| SY | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-10-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 132 | 132 | 54 | 2026-10-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 142 | 142 | 72 | 2026-10-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-10-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 173 | 173 | 70 | 2026-10-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 325 | 325 | 98 | 2026-10-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 345 | 345 | 113 | 2026-10-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-10-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 791 | 791 | 166 | 2026-10-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1409 | 1409 | 934 | 2026-10-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-10-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1733 | 1729 | 177 | 2026-10-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1589 | 2026-10-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2353 | 2351 | 716 | 2026-10-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2645 | 2643 | 1894 | 2026-10-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3183 | 3181 | 1220 | 2026-10-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 74891 | 74891 | 61408 | 2026-10-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 81902 | 81901 | 2426 | 2026-10-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1241 | 64 | 131/144 |
| http://149.130.173.58:9443 | CO | 379 | 55 | 55/55 |
| http://190.0.246.213:4040 | CO | 3874 | 38 | 101/109 |
| http://197.224.185.3:3128 | MU | 1766 | 36 | 105/112 |
| http://103.237.102.191:11111 | DE | 654 | 31 | 137/144 |
| http://203.252.142.217:80 | KR | 990 | 26 | 26/26 |
| http://45.186.6.104:3128 | EC | 579 | 25 | 115/122 |
| http://3.211.120.181:443 | US | 104 | 24 | 38/55 |
| http://103.133.26.72:8080 | ID | 2391 | 20 | 25/70 |
| http://103.133.26.73:3128 | ID | 1622 | 20 | 40/122 |
| http://103.133.26.119:8080 | ID | 3253 | 20 | 24/54 |
| http://176.111.37.5:39811 | HK | 847 | 15 | 125/144 |
| http://34.43.46.91:80 | US | 406 | 14 | 138/144 |
| socks5://43.245.199.34:1080 | HK | 1396 | 13 | 13/13 |
| http://4.144.146.21:80 | SG | 1193 | 12 | 29/36 |
| http://190.0.246.210:4040 | CO | 1091 | 11 | 130/143 |
| http://43.155.62.157:443 | HK | 6018 | 11 | 39/47 |
| http://102.244.78.61:8081 | CM | 1212 | 10 | 23/30 |
| http://102.244.78.61:8090 | CM | 1223 | 10 | 26/36 |
| http://103.119.19.218:3128 | CZ | 657 | 10 | 45/57 |
| http://186.5.94.206:999 | EC | 768 | 9 | 97/106 |
| http://49.156.44.115:8080 | KH | 6286 | 9 | 40/110 |
| http://205.164.192.115:999 | MX | 2897 | 9 | 94/142 |
| socks5://103.100.158.115:10809 | JP | 1118 | 9 | 24/32 |
| http://184.75.221.82:3118 | CA | 227 | 8 | 95/109 |
| http://45.71.186.212:999 | EC | 1726 | 8 | 52/131 |
| http://189.51.168.165:999 | MX | 340 | 8 | 51/56 |
| http://130.110.103.245:3128 | SA | 1598 | 8 | 128/144 |
| http://102.244.78.61:8086 | CM | 1181 | 7 | 25/32 |
| http://181.78.195.137:999 | EC | 1502 | 7 | 46/144 |
| http://176.111.37.216:39811 | HK | 807 | 7 | 116/144 |
| http://46.209.30.11:8080 | IR | 1289 | 7 | 7/7 |
| socks4://14.36.232.55:1080 | KR | 2401 | 7 | 7/7 |
| http://102.244.78.61:8082 | CM | 1201 | 6 | 26/33 |
| http://223.85.21.195:8080 | CN | 5667 | 6 | 60/142 |
| http://34.88.38.81:9443 | FI | 893 | 6 | 75/109 |
| http://35.228.49.168:9443 | FI | 634 | 6 | 56/81 |
| http://103.130.61.61:8081 | ID | 1871 | 6 | 114/144 |
| http://159.223.41.216:9090 | SG | 2505 | 6 | 75/104 |
| http://45.65.224.125:999 | ?? | 1421 | 6 | 6/6 |
| http://62.146.180.4:3000 | ?? | 227 | 6 | 6/6 |
| http://102.244.78.61:8083 | CM | 1181 | 5 | 26/32 |
| http://102.244.78.61:8085 | CM | 1216 | 5 | 24/34 |
| http://102.244.78.61:8087 | CM | 1222 | 5 | 24/34 |
| http://102.244.78.61:8089 | CM | 1204 | 5 | 24/32 |
| http://111.192.23.52:8888 | CN | 2024 | 5 | 7/8 |
| http://177.234.217.88:999 | EC | 7279 | 5 | 56/136 |
| http://190.12.150.244:999 | EC | 2480 | 5 | 101/140 |
| http://205.237.105.49:3129 | FR | 535 | 5 | 14/15 |
| http://34.105.252.3:3128 | GB | 467 | 5 | 17/26 |
| http://103.168.254.198:8080 | ID | 3521 | 5 | 6/8 |
| http://134.185.85.16:3128 | SG | 1190 | 5 | 14/19 |
| socks5://51.15.20.32:1088 | NL | 595 | 5 | 7/8 |
| socks5://178.252.74.29:1081 | RU | 6559 | 5 | 13/17 |
| socks5://64.176.166.106:1080 | ?? | 4050 | 5 | 5/5 |
| http://185.191.239.248:3128 | CH | 2091 | 4 | 100/143 |
| http://120.232.115.170:17981 | CN | 1849 | 4 | 102/143 |
| http://221.221.162.6:8888 | CN | 1666 | 4 | 21/42 |
| http://179.1.182.20:999 | CO | 7705 | 4 | 11/72 |
| http://186.97.200.210:999 | CO | 6465 | 4 | 11/58 |
| http://103.133.26.50:8080 | ID | 1544 | 4 | 23/45 |
| http://123.176.126.95:8080 | ID | 2947 | 4 | 26/90 |
| http://160.191.56.1:8082 | ID | 5098 | 4 | 34/90 |
| http://163.223.105.86:5052 | PH | 5755 | 4 | 9/28 |
| http://38.183.212.8:999 | ?? | 3876 | 4 | 4/4 |
| socks5://101.36.104.46:10808 | JP | 1459 | 4 | 124/144 |
| http://185.196.182.29:8080 | AL | 1798 | 3 | 7/16 |
| http://138.117.14.237:9090 | AR | 5598 | 3 | 22/82 |
| http://103.7.120.141:8080 | BD | 3775 | 3 | 14/105 |
| http://18.231.126.121:15444 | BR | 3055 | 3 | 19/84 |
| http://147.15.126.122:28080 | BR | 6635 | 3 | 16/33 |
| http://179.48.11.6:8085 | BR | 7757 | 3 | 5/13 |
| http://102.244.78.61:8080 | CM | 1175 | 3 | 26/33 |
| http://170.254.228.90:999 | CO | 5602 | 3 | 29/127 |
| http://181.205.205.170:999 | CO | 6995 | 3 | 17/101 |
| http://186.96.111.214:999 | CO | 6629 | 3 | 59/133 |
| http://38.75.82.212:999 | DO | 1603 | 3 | 47/138 |
| http://181.78.194.249:999 | EC | 4882 | 3 | 48/127 |
| http://41.128.90.54:1976 | EG | 4455 | 3 | 22/65 |
| http://45.5.119.17:999 | GT | 5199 | 3 | 8/52 |
| http://45.125.64.215:443 | HK | 2270 | 3 | 13/14 |
| http://36.93.163.219:8080 | ID | 7566 | 3 | 13/69 |
| http://103.22.99.95:1111 | ID | 6712 | 3 | 6/17 |
| http://103.172.42.147:1111 | ID | 3219 | 3 | 26/136 |
| http://103.177.8.133:1111 | ID | 5829 | 3 | 13/57 |
| http://103.188.173.101:1080 | ID | 5744 | 3 | 12/67 |
| http://103.189.249.145:1111 | ID | 6195 | 3 | 22/144 |
| http://103.205.82.246:8080 | ID | 4417 | 3 | 13/44 |
| http://116.254.118.180:80 | ID | 6457 | 3 | 10/17 |
| http://203.201.190.33:8080 | ID | 3925 | 3 | 8/25 |
| http://112.216.54.226:12121 | KR | 1227 | 3 | 51/138 |
| http://38.194.236.106:999 | MX | 4095 | 3 | 10/18 |
| http://102.36.133.62:8080 | NG | 5358 | 3 | 10/50 |
| http://51.15.20.32:3129 | NL | 522 | 3 | 6/8 |
| http://179.63.6.239:999 | PE | 3107 | 3 | 5/8 |
| http://49.157.158.178:8084 | PH | 6627 | 3 | 17/113 |
| http://181.40.18.42:999 | PY | 4889 | 3 | 5/14 |
| http://194.87.197.21:8080 | RU | 5652 | 3 | 9/22 |
| http://167.172.76.176:9090 | SG | 1162 | 3 | 72/105 |
| http://195.226.213.251:8888 | UA | 1899 | 3 | 51/138 |
