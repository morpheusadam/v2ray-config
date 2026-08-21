# Proxy status

Generated 2026-08-21T13:49:47Z by `harvest.py`.

- **623** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1037** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13792** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 188/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 792 |
| socks5 | 229 |
| socks4 | 16 |

| country | entries |
|---|---|
| ID | 242 |
| US | 83 |
| RU | 44 |
| CO | 43 |
| CN | 39 |
| BD | 36 |
| PH | 34 |
| FR | 28 |
| MX | 28 |
| NL | 27 |
| BR | 26 |
| TR | 24 |
| SG | 23 |
| VE | 22 |
| DE | 21 |
| EG | 21 |
| IN | 21 |
| EC | 16 |
| HK | 16 |
| VN | 14 |
| JP | 12 |
| KH | 12 |
| PK | 12 |
| AU | 10 |
| DO | 10 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 2 | 2026-08-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 59 | 59 | 30 | 2026-08-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 77 | 77 | 17 | 2026-08-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 94 | 94 | 39 | 2026-08-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 114 | 114 | 15 | 2026-08-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 135 | 135 | 28 | 2026-08-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 149 | 149 | 68 | 2026-08-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 67 | 2026-08-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 150 | 150 | 15 | 2026-08-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 330 | 330 | 120 | 2026-08-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-08-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-08-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-08-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1605 | 2026-08-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1898 | 1898 | 0 | 2026-08-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2012 | 2010 | 226 | 2026-08-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2446 | 2446 | 1920 | 2026-08-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2499 | 2499 | 1050 | 2026-08-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3001 | 2999 | 2295 | 2026-08-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1177 | 19 | 21/22 |
| http://34.43.46.91:443 | US | 576 | 14 | 19/22 |
| http://34.43.46.91:80 | US | 562 | 14 | 19/22 |
| http://181.78.74.252:999 | CO | 905 | 13 | 13/13 |
| http://181.78.74.253:999 | CO | 932 | 13 | 13/13 |
| http://190.97.236.128:999 | VE | 906 | 12 | 12/12 |
| http://190.97.236.129:999 | VE | 890 | 12 | 12/12 |
| http://47.107.82.96:30051 | CN | 1941 | 8 | 13/15 |
| http://103.237.102.191:11111 | DE | 934 | 8 | 21/22 |
| http://212.58.132.5:8888 | GB | 1793 | 8 | 17/21 |
| http://1.231.81.166:3128 | KR | 937 | 8 | 21/22 |
| http://95.211.174.135:3128 | NL | 1560 | 8 | 21/22 |
| http://204.76.203.9:3128 | NL | 1119 | 8 | 21/22 |
| http://204.76.203.9:8080 | NL | 807 | 8 | 14/15 |
| http://185.200.188.234:10001 | RU | 1394 | 8 | 21/22 |
| http://130.110.103.245:3128 | SA | 1486 | 8 | 20/22 |
| http://202.28.194.139:31280 | TH | 1952 | 8 | 21/22 |
| http://95.3.69.222:8080 | TR | 1498 | 8 | 21/22 |
| http://45.66.249.187:3128 | US | 7892 | 8 | 12/13 |
| http://45.66.249.187:8181 | US | 818 | 8 | 12/13 |
| socks5://45.144.54.40:1080 | DE | 6189 | 8 | 16/22 |
| socks5://144.91.121.61:1088 | FR | 2447 | 8 | 21/22 |
| socks5://212.58.132.5:1080 | GB | 2485 | 8 | 21/22 |
| socks5://144.24.111.128:1088 | IN | 1657 | 8 | 17/22 |
| socks5://178.128.82.131:10808 | SG | 2368 | 8 | 13/22 |
| http://87.251.77.29:3128 | DE | 1006 | 7 | 20/22 |
| http://80.241.214.192:3128 | FR | 5883 | 6 | 6/6 |
| http://195.158.8.123:3128 | UZ | 5239 | 6 | 16/20 |
| http://185.191.239.248:3128 | CH | 1658 | 5 | 13/21 |
| http://116.196.150.180:17981 | CN | 1863 | 5 | 9/22 |
| http://13.221.202.200:3128 | US | 1975 | 5 | 5/5 |
| http://98.83.197.228:3128 | US | 1000 | 5 | 5/5 |
| http://199.7.149.90:3128 | US | 366 | 5 | 5/5 |
| socks5://101.36.104.46:10808 | JP | 1015 | 5 | 20/22 |
| socks5://103.75.118.84:1080 | JP | 5159 | 5 | 11/17 |
| socks5://121.169.46.116:1090 | KR | 1767 | 5 | 15/22 |
| socks5://45.43.63.37:10808 | SG | 2698 | 5 | 19/22 |
| http://45.71.0.121:999 | EC | 4567 | 4 | 6/9 |
| http://41.65.236.37:8080 | EG | 1522 | 4 | 4/4 |
| http://185.78.113.230:81 | RU | 6574 | 4 | 7/18 |
| socks4://89.169.168.25:6101 | RU | 3448 | 4 | 10/22 |
| socks5://203.189.150.44:1080 | KH | 2826 | 4 | 8/22 |
| socks5://193.25.215.182:22222 | US | 1491 | 4 | 20/22 |
| http://103.161.69.252:2698 | BD | 7005 | 3 | 10/22 |
| http://103.177.118.145:8118 | BD | 1391 | 3 | 3/3 |
| http://190.12.150.244:999 | EC | 4283 | 3 | 13/18 |
| http://41.196.16.233:1981 | EG | 1272 | 3 | 5/7 |
| http://84.36.141.180:1976 | EG | 1976 | 3 | 4/8 |
| socks5://195.133.65.238:10909 | DE | 2284 | 3 | 8/21 |
| socks5://81.0.49.104:18500 | ES | 3609 | 3 | 5/19 |
| socks5://47.250.115.134:1080 | MY | 1252 | 3 | 6/20 |
| socks5://103.239.201.50:58765 | PH | 1375 | 3 | 4/7 |
| http://168.196.227.203:999 | AR | 5970 | 2 | 6/16 |
| http://101.206.186.99:8080 | CN | 2302 | 2 | 15/22 |
| http://190.0.246.210:4040 | CO | 1003 | 2 | 19/21 |
| http://190.0.246.211:4040 | CO | 894 | 2 | 21/22 |
| http://41.128.90.50:1976 | EG | 1299 | 2 | 6/7 |
| http://45.240.232.61:8080 | EG | 2495 | 2 | 2/2 |
| http://156.200.116.67:8080 | EG | 1351 | 2 | 4/21 |
| http://196.219.64.253:8080 | EG | 7620 | 2 | 4/14 |
| http://37.58.221.247:3128 | FR | 2913 | 2 | 5/14 |
| http://101.255.107.122:1111 | ID | 6721 | 2 | 2/2 |
| http://103.13.204.84:8082 | ID | 4724 | 2 | 4/16 |
| http://103.130.61.61:8081 | ID | 5001 | 2 | 18/22 |
| http://103.153.190.42:8080 | ID | 6453 | 2 | 3/20 |
| http://103.154.53.67:1111 | ID | 3695 | 2 | 5/21 |
| http://103.156.15.73:8080 | ID | 3777 | 2 | 5/19 |
| http://103.203.234.103:8080 | ID | 5133 | 2 | 5/21 |
| http://203.175.103.25:3125 | ID | 5809 | 2 | 4/20 |
| http://14.139.235.82:3128 | IN | 1884 | 2 | 16/22 |
| http://103.230.150.58:8080 | IN | 4322 | 2 | 6/20 |
| http://43.206.240.252:36055 | JP | 4860 | 2 | 2/2 |
| http://38.194.246.34:999 | MX | 2843 | 2 | 8/13 |
| http://187.175.168.26:8080 | MX | 6213 | 2 | 4/5 |
| http://49.144.31.164:8082 | PH | 1042 | 2 | 4/6 |
| http://202.6.206.78:8082 | PH | 1209 | 2 | 3/4 |
| http://131.222.251.61:8080 | TR | 6099 | 2 | 6/20 |
| http://195.226.213.251:8888 | UA | 4334 | 2 | 6/16 |
| http://34.69.61.247:80 | US | 381 | 2 | 14/21 |
| http://156.238.250.51:8080 | US | 1135 | 2 | 10/17 |
| socks4://157.90.113.23:9052 | DE | 1404 | 2 | 3/4 |
| socks5://38.49.210.79:40000 | CA | 2947 | 2 | 11/22 |
| socks5://45.95.232.35:1080 | CH | 2401 | 2 | 9/22 |
| socks5://112.74.165.243:1011 | CN | 3773 | 2 | 2/2 |
| socks5://193.222.99.32:1080 | DE | 3082 | 2 | 5/7 |
| socks5://65.21.252.66:10811 | FI | 3189 | 2 | 6/10 |
| socks5://144.91.111.48:1088 | FR | 2962 | 2 | 18/22 |
| socks5://152.228.237.108:1080 | FR | 2426 | 2 | 4/7 |
| socks5://223.25.109.146:8199 | ID | 5866 | 2 | 5/13 |
| socks5://13.215.27.14:1080 | SG | 1068 | 2 | 7/14 |
| socks5://140.245.36.86:1080 | SG | 3144 | 2 | 3/22 |
| socks5://43.164.3.124:1080 | TH | 3935 | 2 | 13/21 |
| socks5://64.83.12.6:1080 | US | 176 | 2 | 9/17 |
| socks5://107.191.44.214:1081 | US | 3966 | 2 | 11/22 |
| socks5://141.148.158.143:1080 | US | 2408 | 2 | 10/21 |
| socks5://147.45.60.124:1082 | US | 2625 | 2 | 12/22 |
| socks5://147.45.60.250:1082 | US | 1613 | 2 | 9/22 |
| socks5://150.136.58.221:1080 | US | 3058 | 2 | 9/22 |
| socks5://216.106.179.216:49231 | US | 3518 | 2 | 2/2 |
| http://84.22.42.41:8080 | AL | 3254 | 1 | 1/1 |
