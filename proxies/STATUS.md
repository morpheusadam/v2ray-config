# Proxy status

Generated 2026-09-07T22:15:38Z by `harvest.py`.

- **598** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2102** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16146** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 111/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1764 |
| socks5 | 323 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 515 |
| CN | 118 |
| US | 116 |
| CO | 101 |
| PH | 90 |
| MX | 80 |
| BD | 73 |
| RU | 72 |
| VE | 62 |
| SG | 56 |
| BR | 51 |
| NL | 51 |
| DE | 50 |
| VN | 45 |
| EC | 43 |
| IN | 41 |
| TR | 32 |
| FR | 29 |
| DO | 28 |
| CL | 24 |
| AR | 23 |
| EG | 22 |
| HK | 22 |
| KH | 22 |
| TH | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 2 | 2 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 66 | 66 | 33 | 2026-09-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 90 | 90 | 8 | 2026-09-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 93 | 93 | 28 | 2026-09-07 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 123 | 123 | 9 | 2026-09-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 141 | 141 | 77 | 2026-09-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 70 | 2026-09-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 198 | 198 | 28 | 2026-09-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-07 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 406 | 406 | 170 | 2026-09-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 552 | 552 | 165 | 2026-09-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-07 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1421 | 1417 | 286 | 2026-09-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1128 | 2026-09-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1602 | 2026-09-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2119 | 2117 | 154 | 2026-09-07 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2253 | 2253 | 1564 | 2026-09-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2621 | 2619 | 732 | 2026-09-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3145 | 3143 | 2296 | 2026-09-07 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 378 | 49 | 54/57 |
| http://34.43.46.91:80 | US | 1364 | 49 | 54/57 |
| http://95.211.174.135:3128 | NL | 1861 | 43 | 56/57 |
| http://185.200.188.234:10001 | RU | 5387 | 43 | 56/57 |
| http://130.110.103.245:3128 | SA | 2050 | 43 | 55/57 |
| http://199.7.149.96:3128 | US | 251 | 36 | 36/36 |
| http://64.112.184.210:3128 | US | 1470 | 35 | 56/57 |
| http://103.211.103.170:3128 | HK | 4113 | 29 | 29/29 |
| http://68.178.174.239:3128 | US | 956 | 25 | 25/25 |
| http://68.178.174.239:8888 | US | 961 | 25 | 25/25 |
| http://1.231.81.166:3128 | KR | 1649 | 22 | 54/57 |
| http://189.51.168.164:999 | MX | 1214 | 22 | 22/22 |
| socks5://193.25.215.182:22222 | US | 1554 | 20 | 53/57 |
| http://116.202.172.187:11000 | DE | 799 | 18 | 18/18 |
| http://91.134.141.4:3128 | FR | 678 | 18 | 18/18 |
| http://173.212.240.48:8888 | FR | 6321 | 18 | 18/18 |
| http://5.129.254.129:8888 | RU | 1308 | 18 | 18/18 |
| http://176.111.37.5:39811 | HK | 1474 | 17 | 51/57 |
| http://14.251.13.20:8080 | VN | 1230 | 17 | 28/29 |
| http://154.59.56.73:999 | VE | 7109 | 15 | 26/29 |
| http://120.232.115.170:17981 | CN | 1620 | 14 | 39/56 |
| http://181.78.23.187:999 | CO | 854 | 14 | 24/26 |
| http://181.78.74.252:999 | CO | 832 | 14 | 46/48 |
| http://181.78.74.253:999 | CO | 884 | 14 | 46/48 |
| http://190.97.236.128:999 | VE | 828 | 14 | 45/47 |
| http://190.97.236.129:999 | VE | 772 | 14 | 45/47 |
| http://103.177.118.145:8118 | BD | 4693 | 13 | 36/38 |
| http://186.5.94.206:999 | EC | 1084 | 13 | 18/19 |
| socks5://147.45.60.124:1082 | US | 660 | 13 | 33/57 |
| http://176.111.37.216:39811 | HK | 1556 | 12 | 45/57 |
| http://197.224.185.3:3128 | MU | 1963 | 12 | 23/25 |
| http://5.129.254.49:8888 | RU | 1345 | 12 | 12/12 |
| http://5.129.254.51:8888 | RU | 2922 | 12 | 12/12 |
| http://5.129.254.70:8888 | RU | 1315 | 12 | 12/12 |
| http://95.3.69.222:8080 | TR | 3089 | 12 | 54/57 |
| socks4://45.61.129.165:9050 | US | 1872 | 12 | 48/57 |
| socks5://43.135.176.121:1080 | US | 1072 | 12 | 12/12 |
| http://5.129.254.60:8888 | RU | 1237 | 11 | 11/11 |
| http://157.85.97.204:3128 | TH | 3308 | 11 | 19/22 |
| http://5.129.254.5:8888 | RU | 2473 | 10 | 11/12 |
| http://202.28.194.139:31280 | TH | 3884 | 10 | 54/57 |
| socks5://45.32.160.61:1088 | US | 534 | 10 | 10/10 |
| socks5://185.222.138.237:1080 | XK | 1076 | 10 | 10/10 |
| http://167.233.148.141:1083 | DE | 1301 | 9 | 9/9 |
| http://167.233.169.253:1083 | DE | 1879 | 9 | 9/9 |
| http://190.97.241.106:999 | VE | 2116 | 9 | 18/41 |
| socks5://103.210.161.8:1080 | CN | 1195 | 9 | 22/30 |
| http://185.191.239.248:3128 | CH | 6221 | 8 | 43/56 |
| http://117.236.124.166:3128 | IN | 1870 | 8 | 37/57 |
| http://5.129.254.154:8888 | RU | 1256 | 8 | 8/8 |
| http://42.96.18.62:1311 | VN | 1667 | 7 | 43/56 |
| socks5://65.109.196.122:2091 | FI | 6650 | 7 | 10/11 |
| socks5://147.45.60.246:1082 | US | 701 | 7 | 21/56 |
| http://167.233.169.253:1082 | DE | 1730 | 6 | 6/6 |
| http://167.233.169.253:1084 | DE | 1826 | 6 | 6/6 |
| http://157.85.108.47:3128 | TH | 2486 | 6 | 19/25 |
| http://161.35.181.96:999 | US | 609 | 6 | 6/6 |
| socks5://117.244.114.54:1080 | IN | 4998 | 6 | 14/52 |
| socks5://108.174.152.80:1080 | MX | 575 | 6 | 6/6 |
| socks5://107.181.252.58:1081 | US | 668 | 6 | 6/6 |
| http://113.45.195.147:3128 | CN | 1753 | 5 | 13/22 |
| http://114.249.237.87:8888 | CN | 3998 | 5 | 12/21 |
| http://114.252.12.211:8888 | CN | 1765 | 5 | 11/22 |
| http://190.0.246.210:4040 | CO | 1817 | 5 | 50/56 |
| http://190.0.246.213:4040 | CO | 3392 | 5 | 20/22 |
| http://45.186.6.104:3128 | EC | 846 | 5 | 34/35 |
| http://144.31.185.62:8080 | FI | 6772 | 5 | 17/27 |
| http://43.99.60.244:8089 | HK | 1293 | 5 | 6/7 |
| http://103.130.61.61:8081 | ID | 3836 | 5 | 46/57 |
| http://52.21.158.119:3128 | US | 318 | 5 | 9/10 |
| http://107.181.252.58:1082 | US | 397 | 5 | 5/5 |
| http://154.3.76.14:999 | VE | 4252 | 5 | 8/10 |
| socks5://5.255.113.177:1080 | NL | 951 | 5 | 15/56 |
| socks5://213.165.38.49:1080 | NL | 7200 | 5 | 7/24 |
| socks5://58.187.162.191:1083 | VN | 6697 | 5 | 5/5 |
| http://201.20.42.46:3127 | BR | 5315 | 4 | 15/55 |
| http://184.75.221.82:3118 | CA | 1130 | 4 | 20/22 |
| http://38.7.195.50:999 | CL | 2919 | 4 | 7/16 |
| http://114.254.49.43:8888 | CN | 6322 | 4 | 4/4 |
| http://190.0.246.211:4040 | CO | 4054 | 4 | 48/57 |
| http://144.31.185.67:8080 | FI | 5201 | 4 | 10/25 |
| http://47.57.69.227:3128 | HK | 1355 | 4 | 18/29 |
| http://168.144.117.43:3129 | IN | 1731 | 4 | 5/7 |
| http://168.144.121.183:3129 | IN | 1782 | 4 | 5/8 |
| http://140.238.32.108:3128 | JP | 1831 | 4 | 28/56 |
| http://103.157.200.126:3128 | PK | 1750 | 4 | 10/34 |
| http://129.226.89.151:80 | SG | 1007 | 4 | 4/4 |
| http://116.204.182.120:80 | TH | 1158 | 4 | 8/9 |
| http://195.158.8.123:3128 | UZ | 1413 | 4 | 37/55 |
| http://171.245.11.176:18080 | VN | 1241 | 4 | 4/4 |
| socks5://193.233.139.106:1080 | FI | 1771 | 4 | 6/15 |
| socks5://220.158.232.118:1080 | KH | 7578 | 4 | 19/56 |
| socks5://18.138.10.216:1090 | SG | 1790 | 4 | 4/4 |
| socks5://43.153.61.90:40000 | US | 963 | 4 | 4/4 |
| socks5://49.51.250.24:1080 | US | 998 | 4 | 4/4 |
| http://77.244.249.95:3128 | AT | 750 | 3 | 3/3 |
| http://38.7.195.52:999 | CL | 7896 | 3 | 14/39 |
| http://114.236.137.41:21000 | CN | 3069 | 3 | 40/57 |
| http://114.244.223.68:8888 | CN | 5812 | 3 | 12/20 |
| http://177.93.33.55:999 | CO | 895 | 3 | 12/44 |
