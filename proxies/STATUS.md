# Proxy status

Generated 2026-09-03T17:12:12Z by `harvest.py`.

- **763** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2136** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **15875** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 124/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1802 |
| socks5 | 313 |
| socks4 | 21 |

| country | entries |
|---|---|
| ID | 421 |
| US | 162 |
| CN | 119 |
| MX | 80 |
| CO | 79 |
| BD | 71 |
| RU | 62 |
| PH | 59 |
| SG | 54 |
| VE | 54 |
| FR | 51 |
| DE | 48 |
| HK | 45 |
| TH | 45 |
| BR | 42 |
| EC | 38 |
| NL | 38 |
| VN | 33 |
| AU | 32 |
| EG | 29 |
| IN | 29 |
| DO | 28 |
| KR | 27 |
| CA | 26 |
| ZA | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-09-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-09-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 104 | 104 | 20 | 2026-09-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 114 | 114 | 63 | 2026-09-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 135 | 135 | 42 | 2026-09-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-09-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 154 | 154 | 75 | 2026-09-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 158 | 158 | 11 | 2026-09-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 217 | 217 | 39 | 2026-09-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 248 | 248 | 90 | 2026-09-03 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 620 | 620 | 268 | 2026-09-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-09-03 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1420 | 1416 | 316 | 2026-09-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1122 | 2026-09-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-09-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1944 | 1942 | 190 | 2026-09-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2386 | 2384 | 722 | 2026-09-03 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2576 | 2576 | 1823 | 2026-09-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2861 | 2859 | 2172 | 2026-09-03 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 593 | 40 | 45/48 |
| http://34.43.46.91:80 | US | 706 | 40 | 45/48 |
| http://95.211.174.135:3128 | NL | 1266 | 34 | 47/48 |
| http://204.76.203.9:3128 | NL | 1099 | 34 | 47/48 |
| http://204.76.203.9:8080 | NL | 810 | 34 | 40/41 |
| http://185.200.188.234:10001 | RU | 1334 | 34 | 47/48 |
| http://130.110.103.245:3128 | SA | 1878 | 34 | 46/48 |
| http://199.7.149.96:3128 | US | 354 | 27 | 27/27 |
| http://45.186.6.104:3128 | EC | 821 | 26 | 26/26 |
| http://64.112.184.210:3128 | US | 654 | 26 | 47/48 |
| http://103.211.103.170:3128 | HK | 2287 | 20 | 20/20 |
| http://68.178.174.239:3128 | US | 889 | 16 | 16/16 |
| http://68.178.174.239:8888 | US | 893 | 16 | 16/16 |
| http://190.0.246.213:4040 | CO | 3736 | 13 | 13/13 |
| http://1.231.81.166:3128 | KR | 1126 | 13 | 45/48 |
| http://189.51.168.164:999 | MX | 551 | 13 | 13/13 |
| socks5://47.250.211.53:1080 | MY | 1487 | 13 | 29/48 |
| socks5://193.25.215.182:22222 | US | 1265 | 11 | 44/48 |
| http://3.211.120.181:443 | US | 397 | 10 | 10/10 |
| http://18.157.123.132:3128 | DE | 852 | 9 | 9/9 |
| http://116.202.172.187:11000 | DE | 874 | 9 | 9/9 |
| http://91.134.141.4:3128 | FR | 767 | 9 | 9/9 |
| http://173.212.240.48:8888 | FR | 1417 | 9 | 9/9 |
| http://5.129.254.129:8888 | RU | 1324 | 9 | 9/9 |
| socks5://171.25.158.95:1080 | SE | 3978 | 9 | 25/47 |
| http://176.111.37.5:39811 | HK | 1963 | 8 | 42/48 |
| http://47.81.56.193:8888 | TH | 1658 | 8 | 30/48 |
| http://14.251.13.20:8080 | VN | 1130 | 8 | 19/20 |
| http://40.177.104.199:48086 | CA | 1758 | 7 | 10/15 |
| http://39.106.170.168:8080 | CN | 1734 | 7 | 18/46 |
| http://34.88.38.81:9443 | FI | 1098 | 7 | 8/13 |
| http://16.174.6.134:3128 | CA | 2927 | 6 | 6/6 |
| http://37.59.125.131:8888 | FR | 1590 | 6 | 35/48 |
| http://154.59.56.73:999 | VE | 5946 | 6 | 17/20 |
| socks5://101.36.104.46:10808 | JP | 1441 | 6 | 44/48 |
| socks5://5.255.117.250:1080 | NL | 1996 | 6 | 12/33 |
| http://40.177.104.199:22203 | CA | 7481 | 5 | 7/8 |
| http://120.232.115.170:17981 | CN | 1774 | 5 | 30/47 |
| http://181.78.23.187:999 | CO | 835 | 5 | 15/17 |
| http://181.78.74.252:999 | CO | 885 | 5 | 37/39 |
| http://181.78.74.253:999 | CO | 878 | 5 | 37/39 |
| http://177.234.217.235:999 | EC | 5709 | 5 | 11/17 |
| http://175.143.76.177:8181 | MY | 2401 | 5 | 36/48 |
| http://190.97.236.128:999 | VE | 781 | 5 | 36/38 |
| http://190.97.236.129:999 | VE | 781 | 5 | 36/38 |
| socks5://49.13.22.249:10801 | DE | 1684 | 5 | 10/17 |
| socks5://165.22.243.171:1080 | SG | 1076 | 5 | 5/5 |
| http://15.220.121.140:3128 | AR | 1193 | 4 | 4/4 |
| http://16.26.154.68:53546 | AU | 5484 | 4 | 17/44 |
| http://103.177.118.145:8118 | BD | 1405 | 4 | 27/29 |
| http://16.174.124.173:3851 | CA | 2044 | 4 | 7/12 |
| http://185.191.239.248:3128 | CH | 3813 | 4 | 35/47 |
| http://123.121.122.126:8888 | CN | 1417 | 4 | 11/16 |
| http://217.76.245.80:999 | DO | 893 | 4 | 4/4 |
| http://186.5.94.206:999 | EC | 3070 | 4 | 9/10 |
| http://190.12.150.244:999 | EC | 3961 | 4 | 29/44 |
| http://197.164.101.13:1981 | EG | 5017 | 4 | 9/37 |
| http://175.136.239.173:8181 | MY | 4339 | 4 | 37/48 |
| http://58.69.182.53:8085 | PH | 5444 | 4 | 7/11 |
| http://85.198.100.232:13100 | RU | 1110 | 4 | 4/4 |
| http://16.192.185.227:46981 | SE | 3168 | 4 | 5/8 |
| http://34.224.98.75:7741 | US | 1416 | 4 | 6/12 |
| http://154.59.56.72:999 | VE | 3675 | 4 | 5/7 |
| http://154.59.56.74:999 | VE | 5225 | 4 | 6/11 |
| http://210.211.113.34:80 | VN | 2032 | 4 | 17/20 |
| socks5://5.75.133.113:10801 | DE | 1661 | 4 | 9/14 |
| socks5://5.75.133.113:10811 | DE | 3306 | 4 | 12/19 |
| socks5://144.126.197.184:1088 | GB | 1848 | 4 | 4/4 |
| socks5://101.36.104.239:10808 | JP | 1586 | 4 | 39/48 |
| socks5://5.255.99.75:1080 | NL | 6543 | 4 | 8/23 |
| socks5://5.255.117.127:1080 | NL | 1338 | 4 | 11/24 |
| socks5://147.45.60.124:1082 | US | 2044 | 4 | 24/48 |
| socks5://178.130.47.21:1082 | US | 590 | 4 | 20/47 |
| http://187.102.219.42:999 | AR | 3356 | 3 | 22/43 |
| http://62.60.239.29:3128 | AT | 963 | 3 | 3/3 |
| http://16.26.180.163:8083 | AU | 4296 | 3 | 7/8 |
| http://16.51.62.173:583 | AU | 2512 | 3 | 12/44 |
| http://27.147.153.179:3128 | BD | 4427 | 3 | 8/21 |
| http://40.177.99.164:31822 | CA | 3177 | 3 | 17/48 |
| http://111.192.21.92:8888 | CN | 2012 | 3 | 10/12 |
| http://114.236.137.41:21000 | CN | 1659 | 3 | 32/48 |
| http://114.245.149.247:8888 | CN | 6405 | 3 | 4/6 |
| http://114.250.195.182:8888 | CN | 2805 | 3 | 8/13 |
| http://123.57.213.24:3539 | CN | 1252 | 3 | 22/47 |
| http://123.121.121.123:8888 | CN | 1309 | 3 | 11/13 |
| http://123.121.129.198:8888 | CN | 1474 | 3 | 8/13 |
| http://123.121.131.112:8888 | CN | 1554 | 3 | 8/11 |
| http://181.39.25.196:8118 | EC | 1310 | 3 | 46/48 |
| http://181.188.203.112:999 | EC | 1109 | 3 | 13/40 |
| http://41.128.90.50:1976 | EG | 3562 | 3 | 19/33 |
| http://197.164.101.10:1976 | EG | 2182 | 3 | 3/3 |
| http://65.108.48.176:3128 | FI | 1096 | 3 | 3/3 |
| http://194.163.175.167:40000 | FR | 1152 | 3 | 12/13 |
| http://18.170.25.193:57422 | GB | 1751 | 3 | 19/44 |
| http://81.168.119.85:5443 | GB | 1003 | 3 | 15/36 |
| http://45.5.116.151:8080 | GT | 4873 | 3 | 3/3 |
| http://176.111.37.216:39811 | HK | 2311 | 3 | 36/48 |
| http://38.46.214.177:8085 | ID | 1494 | 3 | 10/24 |
| http://103.111.99.6:3125 | ID | 5132 | 3 | 4/12 |
| http://140.238.32.108:3128 | JP | 3679 | 3 | 21/47 |
