# Proxy status

Generated 2026-10-19T19:24:52Z by `harvest.py`.

- **2677** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5054** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **38542** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 172/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2794 |
| socks5 | 2251 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1987 |
| ID | 831 |
| ?? | 174 |
| PH | 148 |
| CO | 134 |
| MX | 130 |
| RU | 123 |
| US | 105 |
| VE | 81 |
| BR | 79 |
| EC | 79 |
| CN | 76 |
| BD | 71 |
| VN | 63 |
| DO | 58 |
| IN | 58 |
| TR | 56 |
| DE | 46 |
| TH | 45 |
| AR | 44 |
| PK | 37 |
| SG | 33 |
| CL | 32 |
| SY | 32 |
| PE | 30 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-10-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 144 | 144 | 75 | 2026-10-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 59 | 2026-10-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-10-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 200 | 200 | 66 | 2026-10-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 338 | 338 | 144 | 2026-10-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 568 | 568 | 202 | 2026-10-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-10-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1091 | 1091 | 272 | 2026-10-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1296 | 1296 | 958 | 2026-10-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1353 | 1349 | 153 | 2026-10-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1117 | 2026-10-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1589 | 2026-10-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2533 | 2531 | 727 | 2026-10-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2628 | 2626 | 601 | 2026-10-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2808 | 2806 | 1954 | 2026-10-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 71310 | 71310 | 57792 | 2026-10-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 78222 | 78221 | 2826 | 2026-10-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 911 | 59 | 126/139 |
| http://149.130.173.58:9443 | CO | 423 | 50 | 50/50 |
| http://190.0.246.213:4040 | CO | 540 | 33 | 96/104 |
| http://197.224.185.3:3128 | MU | 1743 | 31 | 100/107 |
| http://103.237.102.191:11111 | DE | 763 | 26 | 132/139 |
| http://203.252.142.217:80 | KR | 981 | 21 | 21/21 |
| http://45.186.6.104:3128 | EC | 2636 | 20 | 110/117 |
| http://3.211.120.181:443 | US | 172 | 19 | 33/50 |
| http://5.129.254.5:8888 | RU | 960 | 16 | 83/94 |
| http://5.129.254.49:8888 | RU | 951 | 16 | 84/94 |
| http://5.129.254.51:8888 | RU | 969 | 16 | 84/94 |
| http://5.129.254.60:8888 | RU | 979 | 16 | 83/93 |
| http://5.129.254.70:8888 | RU | 977 | 16 | 84/94 |
| http://5.129.254.129:8888 | RU | 969 | 16 | 89/100 |
| http://5.129.254.154:8888 | RU | 980 | 16 | 80/90 |
| http://5.129.254.215:8888 | RU | 961 | 16 | 33/36 |
| http://5.129.254.243:8888 | RU | 951 | 16 | 33/35 |
| http://103.133.26.50:8080 | ID | 1622 | 15 | 19/40 |
| http://103.133.26.72:8080 | ID | 1487 | 15 | 20/65 |
| http://103.133.26.73:3128 | ID | 1561 | 15 | 35/117 |
| http://103.133.26.119:8080 | ID | 2022 | 15 | 19/49 |
| socks5://67.207.92.87:1088 | US | 322 | 15 | 83/138 |
| http://147.45.164.178:8888 | RU | 970 | 13 | 13/13 |
| http://128.199.121.61:9090 | SG | 1183 | 11 | 49/59 |
| socks5://171.25.158.95:1080 | SE | 1691 | 11 | 46/54 |
| socks5://47.87.97.94:1080 | TH | 2174 | 11 | 14/15 |
| http://198.244.254.77:3128 | GB | 972 | 10 | 21/23 |
| http://176.111.37.5:39811 | HK | 912 | 10 | 120/139 |
| http://34.43.46.91:443 | US | 1790 | 10 | 130/139 |
| http://45.125.64.215:443 | HK | 1353 | 9 | 9/9 |
| http://140.238.32.108:3128 | JP | 1244 | 9 | 72/138 |
| http://34.43.46.91:80 | US | 820 | 9 | 133/139 |
| http://152.67.191.232:6800 | IN | 1063 | 8 | 8/8 |
| socks5://43.245.199.34:1080 | HK | 1402 | 8 | 8/8 |
| http://221.221.163.25:8888 | CN | 7564 | 7 | 37/93 |
| http://177.234.221.201:999 | EC | 3084 | 7 | 17/42 |
| http://4.144.146.21:80 | SG | 1173 | 7 | 24/31 |
| http://200.59.191.27:999 | VE | 1570 | 7 | 90/134 |
| socks5://62.83.34.101:1080 | AT | 974 | 7 | 7/7 |
| socks5://113.22.224.63:1083 | VN | 1882 | 7 | 7/7 |
| http://190.0.246.210:4040 | CO | 930 | 6 | 125/138 |
| http://43.155.62.157:443 | HK | 6978 | 6 | 34/42 |
| http://187.251.224.167:8081 | MX | 1171 | 6 | 27/99 |
| http://43.156.55.191:5001 | SG | 2041 | 6 | 6/6 |
| http://104.248.151.93:9090 | SG | 1177 | 6 | 33/40 |
| http://154.59.56.72:999 | VE | 2823 | 6 | 71/98 |
| http://103.82.20.76:8080 | VN | 1613 | 6 | 41/137 |
| socks5://148.251.68.232:8888 | DE | 3705 | 6 | 13/18 |
| http://187.102.219.32:999 | AR | 3323 | 5 | 44/138 |
| http://118.179.45.194:81 | BD | 2794 | 5 | 20/81 |
| http://102.244.78.61:8081 | CM | 1214 | 5 | 18/25 |
| http://102.244.78.61:8090 | CM | 1205 | 5 | 21/31 |
| http://45.65.137.218:999 | CO | 5615 | 5 | 37/104 |
| http://103.119.19.218:3128 | CZ | 3795 | 5 | 40/52 |
| http://41.65.55.27:1976 | EG | 6524 | 5 | 32/121 |
| http://161.49.90.70:1337 | PH | 4052 | 5 | 14/77 |
| http://95.81.107.187:3128 | SE | 3720 | 5 | 5/5 |
| http://152.42.177.32:8888 | SG | 1178 | 5 | 62/99 |
| http://44.216.83.206:3128 | US | 1332 | 5 | 9/12 |
| http://38.51.207.117:999 | VE | 3647 | 5 | 33/116 |
| socks4://121.46.226.221:10808 | CN | 1360 | 5 | 14/16 |
| socks5://213.199.47.140:1080 | FR | 3666 | 5 | 82/105 |
| socks5://123.58.219.171:10808 | HK | 3121 | 5 | 109/139 |
| socks5://212.77.75.25:1088 | IT | 824 | 5 | 33/39 |
| socks5://143.198.90.221:1088 | SG | 1471 | 5 | 6/7 |
| socks5://147.93.172.241:5555 | SG | 4506 | 5 | 20/50 |
| socks5://45.61.129.165:9050 | US | 1454 | 5 | 105/139 |
| socks5://193.25.215.182:22222 | US | 847 | 5 | 117/139 |
| http://45.65.224.74:999 | AR | 1935 | 4 | 4/4 |
| http://187.102.219.34:999 | AR | 1053 | 4 | 48/90 |
| http://187.102.219.64:999 | AR | 1086 | 4 | 47/78 |
| http://185.191.239.248:3128 | CH | 2090 | 4 | 96/138 |
| http://61.149.134.158:8888 | CN | 1854 | 4 | 40/104 |
| http://123.121.209.108:8888 | CN | 1896 | 4 | 30/89 |
| http://186.96.111.214:999 | CO | 4335 | 4 | 55/128 |
| http://190.7.138.78:8080 | CO | 1839 | 4 | 31/68 |
| http://91.107.247.193:7001 | DE | 962 | 4 | 4/4 |
| http://38.156.233.173:999 | DO | 1727 | 4 | 20/128 |
| http://179.60.189.81:999 | EC | 1118 | 4 | 7/11 |
| http://181.188.203.40:999 | EC | 4731 | 4 | 17/36 |
| http://186.5.94.206:999 | EC | 737 | 4 | 92/101 |
| http://103.22.99.43:8085 | ID | 4547 | 4 | 4/4 |
| http://116.254.118.180:80 | ID | 5091 | 4 | 7/12 |
| http://31.14.124.45:8080 | IR | 5473 | 4 | 19/102 |
| http://185.142.156.203:80 | IR | 1751 | 4 | 4/4 |
| http://45.43.60.220:8080 | JP | 2035 | 4 | 72/138 |
| http://49.156.44.115:8080 | KH | 1628 | 4 | 35/105 |
| http://205.164.192.115:999 | MX | 862 | 4 | 89/137 |
| http://49.145.53.55:8080 | PH | 4633 | 4 | 4/4 |
| http://152.32.77.213:8095 | PH | 3059 | 4 | 4/4 |
| http://203.177.217.222:8082 | PH | 1648 | 4 | 51/84 |
| http://101.53.238.37:8080 | PK | 4090 | 4 | 4/4 |
| http://93.177.126.101:8088 | RU | 5062 | 4 | 4/4 |
| http://128.199.116.219:9090 | SG | 1171 | 4 | 46/58 |
| http://195.158.8.123:3128 | UZ | 2441 | 4 | 91/137 |
| http://38.51.207.119:999 | VE | 7967 | 4 | 30/136 |
| http://154.59.56.74:999 | VE | 3096 | 4 | 69/102 |
| http://190.97.229.118:999 | VE | 1724 | 4 | 71/129 |
| socks5://103.100.158.115:10809 | JP | 2550 | 4 | 19/27 |
| socks5://80.79.241.118:1080 | RU | 4070 | 4 | 17/51 |
