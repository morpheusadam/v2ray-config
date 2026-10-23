# Proxy status

Generated 2026-10-23T17:59:26Z by `harvest.py`.

- **1923** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4579** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39777** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 158/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2658 |
| socks5 | 1912 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1707 |
| ID | 819 |
| CO | 144 |
| PH | 138 |
| MX | 134 |
| US | 112 |
| RU | 106 |
| VE | 89 |
| CN | 79 |
| BD | 75 |
| BR | 74 |
| IN | 70 |
| TH | 66 |
| TR | 64 |
| DO | 62 |
| EC | 61 |
| VN | 54 |
| AR | 50 |
| PK | 40 |
| EG | 38 |
| SG | 38 |
| DE | 32 |
| PE | 29 |
| KH | 27 |
| ZA | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-10-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 111 | 111 | 54 | 2026-10-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 59 | 2026-10-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 85 | 2026-10-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 236 | 236 | 82 | 2026-10-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 289 | 289 | 115 | 2026-10-23 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 459 | 459 | 172 | 2026-10-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-10-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 634 | 634 | 63 | 2026-10-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 726 | 726 | 452 | 2026-10-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-10-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-10-23 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1943 | 1939 | 201 | 2026-10-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2345 | 2343 | 718 | 2026-10-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2769 | 2767 | 861 | 2026-10-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3059 | 3057 | 1974 | 2026-10-23 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 76836 | 76836 | 63388 | 2026-10-23 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 83841 | 83840 | 2332 | 2026-10-23 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1207 | 67 | 134/147 |
| http://149.130.173.58:9443 | CO | 472 | 58 | 58/58 |
| http://190.0.246.213:4040 | CO | 693 | 41 | 104/112 |
| http://197.224.185.3:3128 | MU | 1889 | 39 | 108/115 |
| http://103.237.102.191:11111 | DE | 1086 | 34 | 140/147 |
| http://203.252.142.217:80 | KR | 885 | 29 | 29/29 |
| http://45.186.6.104:3128 | EC | 2739 | 28 | 118/125 |
| http://103.133.26.72:8080 | ID | 1463 | 23 | 28/73 |
| http://103.133.26.73:3128 | ID | 1427 | 23 | 43/125 |
| http://103.133.26.119:8080 | ID | 1820 | 23 | 27/57 |
| http://176.111.37.5:39811 | HK | 1206 | 18 | 128/147 |
| http://34.43.46.91:80 | US | 268 | 17 | 141/147 |
| socks5://43.245.199.34:1080 | HK | 1203 | 16 | 16/16 |
| http://4.144.146.21:80 | SG | 1042 | 15 | 32/39 |
| http://190.0.246.210:4040 | CO | 635 | 14 | 133/146 |
| http://43.155.62.157:443 | HK | 2614 | 14 | 42/50 |
| http://102.244.78.61:8081 | CM | 1305 | 13 | 26/33 |
| http://102.244.78.61:8090 | CM | 1339 | 13 | 29/39 |
| http://103.119.19.218:3128 | CZ | 710 | 13 | 48/60 |
| http://186.5.94.206:999 | EC | 919 | 12 | 100/109 |
| http://49.156.44.115:8080 | KH | 5765 | 12 | 43/113 |
| http://205.164.192.115:999 | MX | 1639 | 12 | 97/145 |
| socks5://103.100.158.115:10809 | JP | 1124 | 12 | 27/35 |
| http://184.75.221.82:3118 | CA | 255 | 11 | 98/112 |
| http://45.71.186.212:999 | EC | 3931 | 11 | 55/134 |
| http://189.51.168.165:999 | MX | 439 | 11 | 54/59 |
| http://130.110.103.245:3128 | SA | 1330 | 11 | 131/147 |
| http://102.244.78.61:8086 | CM | 1309 | 10 | 28/35 |
| http://176.111.37.216:39811 | HK | 1206 | 10 | 119/147 |
| http://46.209.30.11:8080 | IR | 3578 | 10 | 10/10 |
| http://102.244.78.61:8082 | CM | 1363 | 9 | 29/36 |
| http://34.88.38.81:9443 | FI | 980 | 9 | 78/112 |
| http://35.228.49.168:9443 | FI | 841 | 9 | 59/84 |
| http://103.130.61.61:8081 | ID | 3303 | 9 | 117/147 |
| http://102.244.78.61:8083 | CM | 1346 | 8 | 29/35 |
| http://102.244.78.61:8085 | CM | 1353 | 8 | 27/37 |
| http://102.244.78.61:8089 | CM | 1343 | 8 | 27/35 |
| http://177.234.217.88:999 | EC | 2599 | 8 | 59/139 |
| http://205.237.105.49:3129 | FR | 1612 | 8 | 17/18 |
| socks5://51.15.20.32:1088 | NL | 740 | 8 | 10/11 |
| http://185.191.239.248:3128 | CH | 942 | 7 | 103/146 |
| http://103.133.26.50:8080 | ID | 1421 | 7 | 26/48 |
| http://102.244.78.61:8080 | CM | 1343 | 6 | 29/36 |
| http://170.254.228.90:999 | CO | 1192 | 6 | 32/130 |
| http://186.96.111.214:999 | CO | 1991 | 6 | 62/136 |
| http://45.125.64.215:443 | HK | 1208 | 6 | 16/17 |
| http://34.43.46.91:443 | US | 251 | 6 | 137/147 |
| http://165.154.162.73:8888 | US | 2380 | 6 | 96/147 |
| http://38.172.160.16:999 | VE | 2852 | 6 | 56/98 |
| socks5://101.36.104.239:10808 | JP | 1728 | 6 | 124/147 |
| socks5://143.198.90.221:1088 | SG | 1274 | 6 | 13/15 |
| http://67.215.226.71:999 | DO | 3516 | 5 | 32/139 |
| http://45.71.186.210:999 | EC | 4023 | 5 | 44/121 |
| http://177.234.217.42:999 | EC | 3420 | 5 | 17/44 |
| http://81.19.210.10:80 | GB | 790 | 5 | 7/8 |
| http://45.43.60.220:8080 | JP | 1012 | 5 | 77/146 |
| http://152.42.177.32:8888 | SG | 1035 | 5 | 68/107 |
| http://1.20.101.15:80 | TH | 5174 | 5 | 5/5 |
| http://103.22.181.107:3128 | TH | 1326 | 5 | 5/5 |
| http://195.142.250.34:8080 | TR | 3167 | 5 | 5/5 |
| http://144.202.78.114:1234 | US | 3477 | 5 | 5/5 |
| http://38.41.0.60:11201 | VE | 7224 | 5 | 26/73 |
| http://200.59.191.27:999 | VE | 5598 | 5 | 96/142 |
| socks5://121.169.46.116:1090 | KR | 1776 | 5 | 100/147 |
| http://102.244.78.61:8084 | CM | 1365 | 4 | 27/35 |
| http://102.244.78.61:8088 | CM | 1378 | 4 | 28/35 |
| http://114.248.179.223:8888 | CN | 2092 | 4 | 45/115 |
| http://123.121.118.107:8888 | CN | 2962 | 4 | 5/13 |
| http://123.121.123.115:8888 | CN | 2087 | 4 | 43/71 |
| http://45.65.138.48:999 | CO | 5353 | 4 | 59/147 |
| http://156.200.116.69:8080 | EG | 1084 | 4 | 4/4 |
| http://103.147.134.65:8082 | ID | 1499 | 4 | 19/84 |
| http://103.194.47.53:8082 | ID | 5524 | 4 | 30/116 |
| http://160.19.19.100:8080 | ID | 5426 | 4 | 19/78 |
| http://152.67.191.232:6800 | IN | 1229 | 4 | 15/16 |
| http://102.209.0.138:8080 | LY | 2881 | 4 | 9/51 |
| http://82.152.138.127:999 | MX | 1308 | 4 | 28/109 |
| http://148.245.75.54:999 | MX | 6401 | 4 | 13/36 |
| http://187.251.224.167:80 | MX | 1608 | 4 | 42/143 |
| http://203.177.217.222:8082 | PH | 3522 | 4 | 57/92 |
| http://45.177.16.130:999 | PY | 7739 | 4 | 32/145 |
| http://180.180.156.70:80 | TH | 5835 | 4 | 4/4 |
| http://88.210.37.30:3128 | US | 204 | 4 | 4/4 |
| http://104.219.55.50:8118 | US | 337 | 4 | 5/9 |
| socks5://123.58.219.171:10808 | HK | 1995 | 4 | 116/147 |
| socks5://212.77.75.25:1088 | IT | 1674 | 4 | 39/47 |
| socks5://171.25.158.95:1080 | SE | 1999 | 4 | 53/62 |
| socks5://129.146.121.2:10808 | US | 415 | 4 | 4/4 |
| socks5://209.50.255.91:1080 | US | 941 | 4 | 32/64 |
| http://45.65.226.169:999 | AR | 4343 | 3 | 8/9 |
| http://186.38.100.130:999 | AR | 6256 | 3 | 12/22 |
| http://27.147.153.179:9249 | BD | 3927 | 3 | 8/14 |
| http://123.200.8.170:10000 | BD | 7745 | 3 | 58/145 |
| http://47.110.226.74:19991 | CN | 4682 | 3 | 57/145 |
| http://101.251.204.174:8080 | CN | 1937 | 3 | 71/133 |
| http://38.51.233.97:999 | CO | 4249 | 3 | 17/72 |
| http://45.172.223.179:999 | CO | 5825 | 3 | 16/66 |
| http://179.1.196.133:999 | CO | 4090 | 3 | 3/3 |
| http://179.49.160.94:999 | CO | 7741 | 3 | 16/85 |
| http://38.57.65.195:999 | DO | 4175 | 3 | 9/32 |
