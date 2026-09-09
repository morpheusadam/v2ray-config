# Proxy status

Generated 2026-09-09T17:18:07Z by `harvest.py`.

- **996** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1682** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16406** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 228/600 (38%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1340 |
| socks5 | 323 |
| socks4 | 19 |

| country | entries |
|---|---|
| ID | 321 |
| US | 147 |
| CN | 69 |
| CO | 62 |
| MX | 62 |
| NL | 61 |
| RU | 54 |
| PH | 47 |
| BD | 46 |
| DE | 44 |
| IN | 44 |
| FR | 36 |
| JP | 34 |
| SG | 32 |
| BR | 31 |
| HK | 30 |
| TH | 30 |
| VN | 29 |
| VE | 28 |
| CA | 27 |
| KH | 27 |
| EC | 25 |
| CL | 20 |
| PK | 20 |
| TR | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 11 | 11 | 2 | 2026-09-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 78 | 78 | 38 | 2026-09-09 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 111 | 111 | 38 | 2026-09-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 116 | 116 | 63 | 2026-09-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 81 | 2026-09-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 155 | 155 | 60 | 2026-09-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 183 | 183 | 52 | 2026-09-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 209 | 209 | 32 | 2026-09-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-09 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 490 | 490 | 233 | 2026-09-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 523 | 523 | 290 | 2026-09-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-09 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1427 | 1423 | 324 | 2026-09-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1125 | 2026-09-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1601 | 2026-09-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2018 | 2016 | 199 | 2026-09-09 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2355 | 2355 | 1662 | 2026-09-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2445 | 2443 | 718 | 2026-09-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2837 | 2835 | 2073 | 2026-09-09 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 328 | 52 | 57/60 |
| http://34.43.46.91:80 | US | 463 | 52 | 57/60 |
| http://95.211.174.135:3128 | NL | 1548 | 46 | 59/60 |
| http://185.200.188.234:10001 | RU | 1237 | 46 | 59/60 |
| http://130.110.103.245:3128 | SA | 1102 | 46 | 58/60 |
| http://199.7.149.96:3128 | US | 202 | 39 | 39/39 |
| http://64.112.184.210:3128 | US | 277 | 38 | 59/60 |
| http://103.211.103.170:3128 | HK | 900 | 32 | 32/32 |
| http://1.231.81.166:3128 | KR | 1918 | 25 | 57/60 |
| http://189.51.168.164:999 | MX | 465 | 25 | 25/25 |
| socks5://193.25.215.182:22222 | US | 3576 | 23 | 56/60 |
| http://116.202.172.187:11000 | DE | 997 | 21 | 21/21 |
| http://176.111.37.5:39811 | HK | 2181 | 20 | 54/60 |
| http://14.251.13.20:8080 | VN | 1230 | 20 | 31/32 |
| http://181.78.23.187:999 | CO | 748 | 17 | 27/29 |
| http://181.78.74.252:999 | CO | 811 | 17 | 49/51 |
| http://181.78.74.253:999 | CO | 774 | 17 | 49/51 |
| http://190.97.236.128:999 | VE | 1829 | 17 | 48/50 |
| http://190.97.236.129:999 | VE | 2727 | 17 | 48/50 |
| http://103.177.118.145:8118 | BD | 1581 | 16 | 39/41 |
| http://186.5.94.206:999 | EC | 887 | 16 | 21/22 |
| http://176.111.37.216:39811 | HK | 1034 | 15 | 48/60 |
| http://5.129.254.49:8888 | RU | 1298 | 15 | 15/15 |
| http://5.129.254.51:8888 | RU | 1156 | 15 | 15/15 |
| http://5.129.254.70:8888 | RU | 1222 | 15 | 15/15 |
| http://95.3.69.222:8080 | TR | 2545 | 15 | 57/60 |
| http://5.129.254.60:8888 | RU | 1175 | 14 | 14/14 |
| http://5.129.254.5:8888 | RU | 1168 | 13 | 14/15 |
| http://202.28.194.139:31280 | TH | 3247 | 13 | 57/60 |
| socks5://185.222.138.237:1080 | XK | 1042 | 13 | 13/13 |
| http://190.97.241.106:999 | VE | 7071 | 12 | 21/44 |
| http://185.191.239.248:3128 | CH | 5107 | 11 | 46/59 |
| http://5.129.254.154:8888 | RU | 1107 | 11 | 11/11 |
| http://157.85.108.47:3128 | TH | 4338 | 9 | 22/28 |
| http://161.35.181.96:999 | US | 252 | 9 | 9/9 |
| socks5://108.174.152.80:1080 | MX | 2718 | 9 | 9/9 |
| socks5://107.181.252.58:1081 | US | 485 | 9 | 9/9 |
| http://45.186.6.104:3128 | EC | 836 | 8 | 37/38 |
| http://43.99.60.244:8089 | HK | 1056 | 8 | 9/10 |
| http://52.21.158.119:3128 | US | 5063 | 8 | 12/13 |
| http://107.181.252.58:1082 | US | 443 | 8 | 8/8 |
| socks5://5.255.113.177:1080 | NL | 4985 | 8 | 18/59 |
| socks5://213.165.38.49:1080 | NL | 1555 | 8 | 10/27 |
| socks5://58.187.162.191:1083 | VN | 1904 | 8 | 8/8 |
| http://190.0.246.211:4040 | CO | 1971 | 7 | 51/60 |
| http://103.157.200.126:3128 | PK | 1241 | 7 | 13/37 |
| http://101.79.26.53:80 | KR | 1409 | 6 | 6/6 |
| http://154.59.56.76:999 | VE | 4519 | 6 | 16/20 |
| socks5://118.179.102.168:9090 | BD | 1933 | 6 | 6/6 |
| http://196.204.3.21:1981 | EG | 5892 | 5 | 10/39 |
| http://213.131.85.29:1981 | EG | 3129 | 5 | 5/5 |
| http://34.88.38.81:9443 | FI | 745 | 5 | 16/25 |
| http://37.59.125.131:8888 | FR | 7686 | 5 | 46/60 |
| http://43.207.239.56:3128 | JP | 742 | 5 | 5/5 |
| http://203.177.217.222:8082 | PH | 4154 | 5 | 5/5 |
| http://107.167.18.122:443 | US | 6306 | 5 | 11/12 |
| http://210.211.113.34:80 | VN | 5312 | 5 | 27/32 |
| socks5://5.255.123.162:1080 | NL | 2820 | 5 | 20/43 |
| socks5://85.143.254.38:1080 | RU | 5680 | 5 | 19/54 |
| socks5://147.45.60.139:1082 | US | 2241 | 5 | 32/51 |
| http://39.106.170.168:8080 | CN | 1583 | 4 | 28/58 |
| http://47.121.139.13:3128 | CN | 2756 | 4 | 26/59 |
| http://103.237.102.191:11111 | DE | 858 | 4 | 56/60 |
| http://205.164.192.115:999 | MX | 2333 | 4 | 34/58 |
| http://43.134.141.85:80 | SG | 1024 | 4 | 20/58 |
| socks5://49.13.22.249:10801 | DE | 4886 | 4 | 19/29 |
| socks5://83.147.216.208:1080 | FI | 1382 | 4 | 10/28 |
| socks5://51.178.49.241:1088 | FR | 3310 | 4 | 17/21 |
| socks5://47.76.175.249:1080 | HK | 1206 | 4 | 10/11 |
| socks5://5.255.99.75:1080 | NL | 715 | 4 | 17/35 |
| socks5://147.45.60.110:1082 | US | 4349 | 4 | 20/59 |
| http://111.192.19.39:8888 | CN | 1077 | 3 | 14/24 |
| http://123.121.122.28:8888 | CN | 1441 | 3 | 7/9 |
| http://181.78.17.131:999 | CO | 6854 | 3 | 15/57 |
| http://45.71.186.210:999 | EC | 7015 | 3 | 7/34 |
| http://41.196.16.232:1981 | EG | 1108 | 3 | 5/7 |
| http://197.164.101.13:1981 | EG | 2053 | 3 | 18/49 |
| http://197.164.101.14:1981 | EG | 2758 | 3 | 6/30 |
| http://18.163.182.106:21128 | HK | 4197 | 3 | 14/28 |
| http://103.147.247.65:8080 | ID | 3922 | 3 | 6/36 |
| http://103.227.187.3:6090 | ID | 7593 | 3 | 10/58 |
| http://187.172.186.75:999 | MX | 4241 | 3 | 3/3 |
| http://159.223.41.216:9090 | SG | 2546 | 3 | 12/20 |
| http://61.91.162.126:8080 | TH | 1741 | 3 | 3/3 |
| http://103.10.231.189:8080 | TH | 1765 | 3 | 28/45 |
| http://69.87.216.54:7989 | US | 245 | 3 | 4/5 |
| http://154.59.56.74:999 | VE | 2760 | 3 | 14/23 |
| socks4://18.220.132.36:10001 | US | 3639 | 3 | 4/6 |
| socks5://59.152.97.233:1080 | BD | 2926 | 3 | 38/58 |
| socks5://51.210.5.144:1088 | FR | 7059 | 3 | 3/3 |
| socks5://109.172.55.227:1082 | FR | 4896 | 3 | 25/58 |
| socks5://144.126.197.184:1088 | GB | 1765 | 3 | 12/16 |
| socks5://195.135.255.98:1080 | LV | 7177 | 3 | 22/60 |
| socks5://77.110.104.9:1080 | RU | 2203 | 3 | 3/3 |
| socks5://178.150.77.204:10801 | UA | 4339 | 3 | 17/38 |
| socks5://147.45.60.250:1082 | US | 5388 | 3 | 24/60 |
| http://103.111.116.233:81 | BD | 2152 | 2 | 6/36 |
| http://45.183.11.194:8080 | BR | 3293 | 2 | 12/41 |
| http://3.99.158.157:8079 | CA | 1655 | 2 | 10/44 |
| http://16.52.81.236:10735 | CA | 2062 | 2 | 9/40 |
