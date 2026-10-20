# Proxy status

Generated 2026-10-20T22:38:32Z by `harvest.py`.

- **1928** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4438** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39786** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 140/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2757 |
| socks5 | 1674 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 1437 |
| ID | 826 |
| ?? | 210 |
| PH | 149 |
| CO | 136 |
| MX | 122 |
| RU | 107 |
| US | 98 |
| BR | 81 |
| BD | 76 |
| VE | 75 |
| TR | 70 |
| CN | 66 |
| IN | 65 |
| EC | 64 |
| DO | 57 |
| TH | 46 |
| AR | 45 |
| DE | 41 |
| PK | 38 |
| SG | 38 |
| CL | 34 |
| PE | 28 |
| SY | 28 |
| ZA | 28 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 3 | 2026-10-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 88 | 88 | 25 | 2026-10-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 118 | 118 | 62 | 2026-10-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 57 | 2026-10-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 80 | 2026-10-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 251 | 251 | 78 | 2026-10-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 332 | 332 | 41 | 2026-10-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 345 | 345 | 107 | 2026-10-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-10-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1151 | 1151 | 737 | 2026-10-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1235 | 1231 | 112 | 2026-10-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1145 | 2026-10-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1590 | 2026-10-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2382 | 2380 | 745 | 2026-10-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2860 | 2858 | 1947 | 2026-10-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3032 | 3030 | 1047 | 2026-10-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 73309 | 73309 | 60260 | 2026-10-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 80218 | 80217 | 2346 | 2026-10-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1075 | 62 | 129/142 |
| http://149.130.173.58:9443 | CO | 420 | 53 | 53/53 |
| http://190.0.246.213:4040 | CO | 498 | 36 | 99/107 |
| http://197.224.185.3:3128 | MU | 1738 | 34 | 103/110 |
| http://103.237.102.191:11111 | DE | 804 | 29 | 135/142 |
| http://203.252.142.217:80 | KR | 1010 | 24 | 24/24 |
| http://45.186.6.104:3128 | EC | 656 | 23 | 113/120 |
| http://3.211.120.181:443 | US | 105 | 22 | 36/53 |
| http://103.133.26.72:8080 | ID | 3924 | 18 | 23/68 |
| http://103.133.26.73:3128 | ID | 1609 | 18 | 38/120 |
| http://103.133.26.119:8080 | ID | 5194 | 18 | 22/52 |
| http://128.199.121.61:9090 | SG | 2528 | 14 | 52/62 |
| socks5://171.25.158.95:1080 | SE | 3015 | 14 | 49/57 |
| socks5://47.87.97.94:1080 | TH | 1666 | 14 | 17/18 |
| http://198.244.254.77:3128 | GB | 1181 | 13 | 24/26 |
| http://176.111.37.5:39811 | HK | 878 | 13 | 123/142 |
| http://34.43.46.91:80 | US | 729 | 12 | 136/142 |
| http://152.67.191.232:6800 | IN | 1039 | 11 | 11/11 |
| socks5://43.245.199.34:1080 | HK | 1400 | 11 | 11/11 |
| http://4.144.146.21:80 | SG | 1236 | 10 | 27/34 |
| http://190.0.246.210:4040 | CO | 711 | 9 | 128/141 |
| http://43.155.62.157:443 | HK | 1320 | 9 | 37/45 |
| http://154.59.56.72:999 | VE | 2244 | 9 | 74/101 |
| http://102.244.78.61:8081 | CM | 1242 | 8 | 21/28 |
| http://102.244.78.61:8090 | CM | 1213 | 8 | 24/34 |
| http://103.119.19.218:3128 | CZ | 7227 | 8 | 43/55 |
| http://44.216.83.206:3128 | US | 85 | 8 | 12/15 |
| socks5://213.199.47.140:1080 | FR | 5411 | 8 | 85/108 |
| socks5://123.58.219.171:10808 | HK | 2652 | 8 | 112/142 |
| http://186.5.94.206:999 | EC | 2002 | 7 | 95/104 |
| http://185.142.156.203:80 | IR | 2974 | 7 | 7/7 |
| http://49.156.44.115:8080 | KH | 3137 | 7 | 38/108 |
| http://205.164.192.115:999 | MX | 1943 | 7 | 92/140 |
| socks5://103.100.158.115:10809 | JP | 5425 | 7 | 22/30 |
| http://184.75.221.82:3118 | CA | 185 | 6 | 93/107 |
| http://38.7.195.49:999 | CL | 3538 | 6 | 53/116 |
| http://38.7.195.52:999 | CL | 2473 | 6 | 59/124 |
| http://38.7.195.55:999 | CL | 3620 | 6 | 51/116 |
| http://119.188.131.55:17981 | CN | 1774 | 6 | 70/142 |
| http://123.119.25.143:8888 | CN | 3249 | 6 | 46/107 |
| http://45.71.186.212:999 | EC | 5958 | 6 | 50/129 |
| http://189.51.168.165:999 | MX | 326 | 6 | 49/54 |
| http://130.110.103.245:3128 | SA | 1072 | 6 | 126/142 |
| http://201.4.65.102:8080 | TR | 2470 | 6 | 7/13 |
| http://102.244.78.61:8084 | CM | 1169 | 5 | 23/30 |
| http://102.244.78.61:8086 | CM | 1157 | 5 | 23/30 |
| http://102.244.78.61:8088 | CM | 1205 | 5 | 24/30 |
| http://190.121.157.41:999 | CO | 7630 | 5 | 19/114 |
| http://181.78.195.137:999 | EC | 5886 | 5 | 44/142 |
| http://176.111.37.216:39811 | HK | 853 | 5 | 114/142 |
| http://103.156.57.135:9988 | ID | 7722 | 5 | 19/82 |
| http://46.209.30.11:8080 | IR | 3422 | 5 | 5/5 |
| http://122.3.77.27:8082 | PH | 2780 | 5 | 19/131 |
| http://222.127.206.145:8085 | PH | 6244 | 5 | 11/82 |
| http://94.179.153.218:8081 | UA | 2874 | 5 | 25/122 |
| socks5://144.217.107.25:1080 | CA | 2177 | 5 | 29/52 |
| socks5://14.36.232.55:1080 | KR | 1986 | 5 | 5/5 |
| http://3.26.199.107:9904 | AU | 2979 | 4 | 13/52 |
| http://16.51.53.116:23517 | AU | 4311 | 4 | 19/58 |
| http://103.109.96.180:1994 | BD | 4370 | 4 | 6/11 |
| http://18.228.228.159:52664 | BR | 2498 | 4 | 13/44 |
| http://18.231.214.206:14559 | BR | 1850 | 4 | 31/120 |
| http://38.7.195.51:999 | CL | 7462 | 4 | 56/133 |
| http://102.244.78.61:8082 | CM | 1235 | 4 | 24/31 |
| http://101.206.186.99:8080 | CN | 5092 | 4 | 61/142 |
| http://223.85.21.195:8080 | CN | 5708 | 4 | 58/140 |
| http://181.78.79.11:999 | CO | 7010 | 4 | 21/137 |
| http://177.234.221.194:999 | EC | 2417 | 4 | 24/41 |
| http://34.88.38.81:9443 | FI | 792 | 4 | 73/107 |
| http://35.228.49.168:9443 | FI | 601 | 4 | 54/79 |
| http://164.163.74.97:999 | HN | 3473 | 4 | 19/64 |
| http://38.183.146.29:7080 | ID | 4664 | 4 | 17/93 |
| http://103.130.61.61:8081 | ID | 2490 | 4 | 112/142 |
| http://103.132.52.189:8080 | ID | 2684 | 4 | 23/119 |
| http://103.172.17.14:8080 | ID | 6999 | 4 | 14/53 |
| http://51.85.44.149:1081 | IL | 4585 | 4 | 27/138 |
| http://160.19.41.43:80 | IN | 4215 | 4 | 9/15 |
| http://206.135.38.38:999 | MX | 4707 | 4 | 20/111 |
| http://58.69.124.137:8080 | PH | 5762 | 4 | 34/141 |
| http://18.142.95.213:8095 | SG | 5762 | 4 | 20/102 |
| http://159.223.41.216:9090 | SG | 1194 | 4 | 73/102 |
| http://45.65.224.125:999 | ?? | 3970 | 4 | 4/4 |
| http://45.65.226.169:999 | ?? | 2914 | 4 | 4/4 |
| http://45.198.11.193:8282 | ?? | 4662 | 4 | 4/4 |
| http://62.146.180.4:3000 | ?? | 317 | 4 | 4/4 |
| http://111.192.26.109:8888 | ?? | 1310 | 4 | 4/4 |
| http://189.196.45.158:999 | ?? | 5088 | 4 | 4/4 |
| socks4://47.251.127.154:1080 | US | 6943 | 4 | 23/95 |
| socks5://129.151.128.225:1080 | AE | 2945 | 4 | 35/141 |
| socks5://65.21.252.66:10805 | FI | 1011 | 4 | 32/56 |
| socks5://220.158.232.118:1080 | KH | 2506 | 4 | 44/141 |
| socks5://103.88.234.239:40016 | MX | 505 | 4 | 16/43 |
| socks5://45.74.31.46:4610 | NL | 5552 | 4 | 4/4 |
| socks5://95.170.122.80:2080 | RU | 3315 | 4 | 13/27 |
| socks5://52.128.241.108:1080 | US | 485 | 4 | 5/6 |
| http://138.117.13.65:999 | AR | 7207 | 3 | 29/138 |
| http://103.113.152.73:14158 | BD | 6110 | 3 | 31/136 |
| http://103.134.56.148:8080 | BD | 3588 | 3 | 25/84 |
| http://213.169.52.101:8185 | BG | 1682 | 3 | 9/44 |
| http://177.20.167.139:8080 | BR | 4287 | 3 | 4/15 |
