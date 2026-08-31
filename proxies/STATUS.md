# Proxy status

Generated 2026-08-31T23:21:44Z by `harvest.py`.

- **1222** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2268** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15773** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 186/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1932 |
| socks5 | 311 |
| socks4 | 25 |

| country | entries |
|---|---|
| ID | 463 |
| ?? | 175 |
| US | 156 |
| CN | 109 |
| MX | 80 |
| CO | 79 |
| PH | 76 |
| BR | 68 |
| BD | 65 |
| DE | 64 |
| IN | 52 |
| RU | 52 |
| FR | 45 |
| NL | 45 |
| VE | 40 |
| VN | 39 |
| EC | 36 |
| SG | 35 |
| TH | 34 |
| HK | 32 |
| JP | 29 |
| KH | 28 |
| AU | 26 |
| KR | 25 |
| CA | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 2 | 2026-08-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 83 | 83 | 48 | 2026-08-31 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 108 | 108 | 40 | 2026-08-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 125 | 125 | 75 | 2026-08-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 142 | 142 | 47 | 2026-08-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 82 | 2026-08-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 161 | 161 | 25 | 2026-08-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 183 | 183 | 62 | 2026-08-31 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 230 | 230 | 53 | 2026-08-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-31 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-08-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-08-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 961 | 961 | 630 | 2026-08-31 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1384 | 1380 | 228 | 2026-08-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1143 | 2026-08-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1606 | 2026-08-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2198 | 2196 | 289 | 2026-08-31 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2303 | 2303 | 1693 | 2026-08-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2568 | 2566 | 676 | 2026-08-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2905 | 2903 | 2199 | 2026-08-31 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1126 | 40 | 42/43 |
| http://34.43.46.91:443 | US | 600 | 35 | 40/43 |
| http://34.43.46.91:80 | US | 630 | 35 | 40/43 |
| http://95.211.174.135:3128 | NL | 1200 | 29 | 42/43 |
| http://204.76.203.9:3128 | NL | 1041 | 29 | 42/43 |
| http://204.76.203.9:8080 | NL | 791 | 29 | 35/36 |
| http://185.200.188.234:10001 | RU | 1324 | 29 | 42/43 |
| http://130.110.103.245:3128 | SA | 1512 | 29 | 41/43 |
| http://95.3.69.222:8080 | TR | 2320 | 29 | 42/43 |
| http://199.7.149.96:3128 | US | 349 | 22 | 22/22 |
| http://45.186.6.104:3128 | EC | 839 | 21 | 21/21 |
| http://64.112.184.210:3128 | US | 373 | 21 | 42/43 |
| http://42.96.18.62:1311 | VN | 1720 | 17 | 32/42 |
| http://103.211.103.170:3128 | HK | 770 | 15 | 15/15 |
| http://202.28.194.139:31280 | TH | 2238 | 15 | 41/43 |
| socks4://45.61.129.165:9050 | US | 2735 | 15 | 35/43 |
| http://87.251.77.29:3128 | DE | 1006 | 14 | 40/43 |
| http://103.177.118.145:8118 | BD | 1314 | 13 | 23/24 |
| http://197.224.185.3:3128 | MU | 2042 | 11 | 11/11 |
| http://157.85.111.64:3128 | TH | 1021 | 11 | 11/11 |
| http://68.178.174.239:3128 | US | 851 | 11 | 11/11 |
| http://68.178.174.239:8888 | US | 857 | 11 | 11/11 |
| http://184.75.221.82:3118 | CA | 714 | 8 | 8/8 |
| http://123.121.121.123:8888 | CN | 1742 | 8 | 8/8 |
| http://190.0.246.213:4040 | CO | 747 | 8 | 8/8 |
| http://130.61.112.125:443 | DE | 921 | 8 | 8/8 |
| http://194.163.175.167:40000 | FR | 2133 | 8 | 8/8 |
| http://1.231.81.166:3128 | KR | 993 | 8 | 40/43 |
| http://189.51.168.164:999 | MX | 623 | 8 | 8/8 |
| http://43.160.242.118:3128 | SG | 3956 | 8 | 33/40 |
| http://157.85.97.204:3128 | TH | 2066 | 8 | 8/8 |
| socks4://158.220.99.85:4545 | FR | 3128 | 8 | 8/8 |
| socks5://47.250.211.53:1080 | MY | 1576 | 8 | 24/43 |
| http://111.192.21.92:8888 | CN | 1153 | 7 | 7/7 |
| socks5://85.209.156.148:1080 | US | 2005 | 7 | 11/14 |
| http://193.233.232.49:3131 | AT | 829 | 6 | 6/6 |
| http://85.193.65.88:8888 | RU | 1231 | 6 | 14/33 |
| socks5://193.25.215.182:22222 | US | 636 | 6 | 39/43 |
| http://179.41.11.138:8080 | AR | 982 | 5 | 14/15 |
| http://185.191.239.248:3128 | CH | 3960 | 5 | 31/42 |
| http://101.251.204.174:8080 | CN | 1470 | 5 | 15/29 |
| http://114.249.218.6:8888 | CN | 1143 | 5 | 6/8 |
| http://186.5.94.206:999 | EC | 4226 | 5 | 5/5 |
| http://47.57.69.227:3128 | HK | 2818 | 5 | 13/15 |
| http://3.211.120.181:443 | US | 393 | 5 | 5/5 |
| socks5://123.58.219.171:10808 | HK | 1828 | 5 | 36/43 |
| socks5://94.183.233.251:1080 | US | 2334 | 5 | 7/8 |
| http://111.192.31.242:8888 | CN | 1147 | 4 | 6/8 |
| http://123.121.122.126:8888 | CN | 1747 | 4 | 7/11 |
| http://123.121.132.32:8888 | CN | 1183 | 4 | 4/4 |
| http://18.157.123.132:3128 | DE | 847 | 4 | 4/4 |
| http://116.202.172.187:11000 | DE | 886 | 4 | 4/4 |
| http://91.134.141.4:3128 | FR | 764 | 4 | 4/4 |
| http://173.212.240.48:8888 | FR | 1078 | 4 | 4/4 |
| http://210.87.92.82:8080 | ID | 7581 | 4 | 9/29 |
| http://43.164.136.235:3128 | KR | 1696 | 4 | 4/4 |
| http://5.129.254.129:8888 | RU | 2606 | 4 | 4/4 |
| http://109.94.1.23:4050 | RU | 2076 | 4 | 31/43 |
| http://101.32.167.12:3000 | SG | 1119 | 4 | 4/4 |
| http://103.10.231.189:8080 | TH | 1573 | 4 | 17/28 |
| http://157.85.105.217:3128 | TH | 1019 | 4 | 10/11 |
| http://190.97.238.160:999 | VE | 6287 | 4 | 9/16 |
| socks5://45.144.54.40:1080 | DE | 1243 | 4 | 33/43 |
| socks5://51.178.49.241:1088 | FR | 940 | 4 | 4/4 |
| socks5://144.24.111.128:1088 | IN | 1788 | 4 | 33/43 |
| socks5://95.81.103.220:1080 | NL | 1056 | 4 | 4/4 |
| socks5://171.25.158.95:1080 | SE | 1926 | 4 | 20/42 |
| socks5://43.164.3.124:1080 | TH | 1326 | 4 | 29/42 |
| socks5://141.148.158.143:1080 | US | 5535 | 4 | 22/42 |
| socks5://147.45.60.139:1082 | US | 428 | 4 | 20/34 |
| socks5://14.225.204.32:10800 | VN | 3041 | 4 | 14/20 |
| socks5://160.22.17.4:9988 | VN | 1321 | 4 | 16/39 |
| http://16.26.180.163:8083 | AU | 2901 | 3 | 3/3 |
| http://16.26.208.68:18596 | AU | 2593 | 3 | 4/8 |
| http://16.50.48.241:23482 | AU | 4195 | 3 | 3/3 |
| http://45.115.114.41:2379 | BD | 7230 | 3 | 4/9 |
| http://103.81.175.141:22311 | BD | 5468 | 3 | 4/16 |
| http://16.174.83.123:3128 | CA | 1471 | 3 | 3/3 |
| http://40.176.90.140:3128 | CA | 1234 | 3 | 3/3 |
| http://40.177.99.164:31822 | CA | 1815 | 3 | 13/43 |
| http://61.149.134.158:8888 | CN | 2205 | 3 | 6/8 |
| http://101.206.186.99:8080 | CN | 2358 | 3 | 26/43 |
| http://111.200.191.214:8888 | CN | 1158 | 3 | 6/8 |
| http://114.254.50.97:8888 | CN | 7135 | 3 | 6/8 |
| http://122.246.3.12:17981 | CN | 2234 | 3 | 19/37 |
| http://123.119.176.134:8888 | CN | 2200 | 3 | 4/8 |
| http://123.121.123.23:8888 | CN | 1976 | 3 | 3/3 |
| http://123.121.209.61:8888 | CN | 1212 | 3 | 6/8 |
| http://139.159.97.82:10900 | CN | 1126 | 3 | 8/12 |
| http://190.0.246.210:4040 | CO | 948 | 3 | 38/42 |
| http://3.122.224.70:38675 | DE | 1946 | 3 | 3/3 |
| http://18.157.159.247:13401 | DE | 2278 | 3 | 3/3 |
| http://63.181.83.210:4358 | DE | 1471 | 3 | 9/29 |
| http://38.75.82.215:999 | DO | 3988 | 3 | 5/24 |
| http://13.38.72.189:8080 | FR | 2030 | 3 | 7/11 |
| http://35.180.138.2:5050 | FR | 4147 | 3 | 3/3 |
| http://52.47.115.41:7898 | FR | 1478 | 3 | 5/10 |
| http://18.170.45.5:47098 | GB | 3980 | 3 | 3/3 |
| http://18.175.218.194:58617 | GB | 2416 | 3 | 3/3 |
| http://91.103.120.49:443 | HK | 1053 | 3 | 3/3 |
