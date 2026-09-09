# Proxy status

Generated 2026-09-09T21:56:35Z by `harvest.py`.

- **1022** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2003** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **17155** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 130/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1687 |
| socks5 | 297 |
| socks4 | 19 |

| country | entries |
|---|---|
| ID | 409 |
| US | 165 |
| CO | 85 |
| MX | 77 |
| CN | 70 |
| PH | 61 |
| RU | 59 |
| BD | 57 |
| IN | 53 |
| BR | 51 |
| NL | 49 |
| DE | 43 |
| FR | 43 |
| HK | 40 |
| JP | 40 |
| VE | 39 |
| SG | 38 |
| CA | 32 |
| VN | 31 |
| TH | 30 |
| AU | 29 |
| EC | 29 |
| PK | 24 |
| CL | 23 |
| SE | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 81 | 81 | 48 | 2026-09-09 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 113 | 113 | 20 | 2026-09-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 114 | 114 | 42 | 2026-09-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-09-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 171 | 171 | 99 | 2026-09-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 218 | 218 | 12 | 2026-09-09 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 243 | 243 | 49 | 2026-09-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-09 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 524 | 524 | 215 | 2026-09-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-09-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 766 | 766 | 465 | 2026-09-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1114 | 2026-09-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-09-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1924 | 1922 | 218 | 2026-09-09 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1978 | 1974 | 767 | 2026-09-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2388 | 2386 | 739 | 2026-09-09 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2625 | 2625 | 1759 | 2026-09-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2695 | 2693 | 2002 | 2026-09-09 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 1066 | 53 | 58/61 |
| http://34.43.46.91:80 | US | 1103 | 53 | 58/61 |
| http://95.211.174.135:3128 | NL | 1784 | 47 | 60/61 |
| http://185.200.188.234:10001 | RU | 1701 | 47 | 60/61 |
| http://130.110.103.245:3128 | SA | 1799 | 47 | 59/61 |
| http://199.7.149.96:3128 | US | 367 | 40 | 40/40 |
| http://64.112.184.210:3128 | US | 1185 | 39 | 60/61 |
| http://1.231.81.166:3128 | KR | 1304 | 26 | 58/61 |
| http://189.51.168.164:999 | MX | 505 | 26 | 26/26 |
| socks5://193.25.215.182:22222 | US | 727 | 24 | 57/61 |
| http://116.202.172.187:11000 | DE | 2868 | 22 | 22/22 |
| http://176.111.37.5:39811 | HK | 3516 | 21 | 55/61 |
| http://14.251.13.20:8080 | VN | 1245 | 21 | 32/33 |
| http://181.78.23.187:999 | CO | 747 | 18 | 28/30 |
| http://181.78.74.252:999 | CO | 840 | 18 | 50/52 |
| http://181.78.74.253:999 | CO | 799 | 18 | 50/52 |
| http://190.97.236.128:999 | VE | 731 | 18 | 49/51 |
| http://190.97.236.129:999 | VE | 806 | 18 | 49/51 |
| http://103.177.118.145:8118 | BD | 1602 | 17 | 40/42 |
| http://186.5.94.206:999 | EC | 6809 | 17 | 22/23 |
| http://176.111.37.216:39811 | HK | 1678 | 16 | 49/61 |
| http://5.129.254.49:8888 | RU | 3900 | 16 | 16/16 |
| http://5.129.254.51:8888 | RU | 1470 | 16 | 16/16 |
| http://5.129.254.70:8888 | RU | 2674 | 16 | 16/16 |
| http://95.3.69.222:8080 | TR | 2232 | 16 | 58/61 |
| http://5.129.254.60:8888 | RU | 1371 | 15 | 15/15 |
| http://5.129.254.5:8888 | RU | 1450 | 14 | 15/16 |
| http://202.28.194.139:31280 | TH | 2495 | 14 | 58/61 |
| http://190.97.241.106:999 | VE | 1774 | 13 | 22/45 |
| http://5.129.254.154:8888 | RU | 1871 | 12 | 12/12 |
| http://161.35.181.96:999 | US | 478 | 10 | 10/10 |
| socks5://108.174.152.80:1080 | MX | 1815 | 10 | 10/10 |
| http://45.186.6.104:3128 | EC | 2771 | 9 | 38/39 |
| http://43.99.60.244:8089 | HK | 1241 | 9 | 10/11 |
| http://52.21.158.119:3128 | US | 411 | 9 | 13/14 |
| socks5://213.165.38.49:1080 | NL | 3138 | 9 | 11/28 |
| socks5://58.187.162.191:1083 | VN | 7396 | 9 | 9/9 |
| http://190.0.246.211:4040 | CO | 1937 | 8 | 52/61 |
| http://103.157.200.126:3128 | PK | 1488 | 8 | 14/38 |
| http://101.79.26.53:80 | KR | 729 | 7 | 7/7 |
| http://213.131.85.29:1981 | EG | 1165 | 6 | 6/6 |
| http://34.88.38.81:9443 | FI | 914 | 6 | 17/26 |
| http://37.59.125.131:8888 | FR | 3119 | 6 | 47/61 |
| http://43.207.239.56:3128 | JP | 599 | 6 | 6/6 |
| http://203.177.217.222:8082 | PH | 2532 | 6 | 6/6 |
| http://107.167.18.122:443 | US | 4276 | 6 | 12/13 |
| http://210.211.113.34:80 | VN | 3300 | 6 | 28/33 |
| socks5://147.45.60.139:1082 | US | 304 | 6 | 33/52 |
| http://39.106.170.168:8080 | CN | 1709 | 5 | 29/59 |
| http://47.121.139.13:3128 | CN | 3100 | 5 | 27/60 |
| http://103.237.102.191:11111 | DE | 1771 | 5 | 57/61 |
| http://205.164.192.115:999 | MX | 5436 | 5 | 35/59 |
| http://43.134.141.85:80 | SG | 970 | 5 | 21/59 |
| socks5://49.13.22.249:10801 | DE | 2819 | 5 | 20/30 |
| socks5://83.147.216.208:1080 | FI | 1325 | 5 | 11/29 |
| socks5://51.178.49.241:1088 | FR | 7114 | 5 | 18/22 |
| socks5://47.76.175.249:1080 | HK | 1191 | 5 | 11/12 |
| socks5://5.255.99.75:1080 | NL | 868 | 5 | 18/36 |
| socks5://147.45.60.110:1082 | US | 1274 | 5 | 21/60 |
| http://111.192.19.39:8888 | CN | 1313 | 4 | 15/25 |
| http://197.164.101.14:1981 | EG | 1823 | 4 | 7/31 |
| http://187.172.186.75:999 | MX | 1488 | 4 | 4/4 |
| http://61.91.162.126:8080 | TH | 1367 | 4 | 4/4 |
| http://103.10.231.189:8080 | TH | 1422 | 4 | 29/46 |
| http://69.87.216.54:7989 | US | 109 | 4 | 5/6 |
| http://154.59.56.74:999 | VE | 3039 | 4 | 15/24 |
| socks5://59.152.97.233:1080 | BD | 3882 | 4 | 39/59 |
| socks5://51.210.5.144:1088 | FR | 5602 | 4 | 4/4 |
| socks5://109.172.55.227:1082 | FR | 1914 | 4 | 26/59 |
| socks5://144.126.197.184:1088 | GB | 1027 | 4 | 13/17 |
| socks5://178.150.77.204:10801 | UA | 2419 | 4 | 18/39 |
| http://45.183.11.194:8080 | BR | 4448 | 3 | 13/42 |
| http://16.54.225.12:9812 | CA | 2414 | 3 | 5/17 |
| http://16.18.37.186:35431 | CH | 2453 | 3 | 9/29 |
| http://190.0.246.213:4040 | CO | 3539 | 3 | 23/26 |
| http://185.248.179.99:8080 | CZ | 6940 | 3 | 17/60 |
| http://167.233.169.253:1084 | DE | 3334 | 3 | 9/10 |
| http://38.44.17.142:999 | DO | 6062 | 3 | 27/54 |
| http://38.75.82.213:999 | DO | 5974 | 3 | 16/55 |
| http://177.234.217.46:999 | EC | 5490 | 3 | 4/8 |
| http://177.234.217.235:999 | EC | 6570 | 3 | 18/30 |
| http://213.131.85.29:1976 | EG | 1173 | 3 | 5/6 |
| http://173.212.240.48:8888 | FR | 4964 | 3 | 21/22 |
| http://160.25.222.41:7979 | ID | 7514 | 3 | 11/43 |
| http://3.250.220.74:3128 | IE | 934 | 3 | 6/17 |
| http://151.185.59.40:8080 | IN | 1687 | 3 | 9/33 |
| http://15.160.67.144:37288 | IT | 1229 | 3 | 3/3 |
| http://15.160.145.162:1994 | IT | 2255 | 3 | 8/19 |
| http://203.81.75.202:8080 | MM | 5197 | 3 | 14/39 |
| http://153.51.241.50:999 | MX | 4019 | 3 | 33/58 |
| http://43.216.195.95:15834 | MY | 3098 | 3 | 6/15 |
| http://13.49.41.94:59541 | SE | 4394 | 3 | 6/19 |
| http://13.51.44.23:3128 | SE | 2639 | 3 | 5/21 |
| http://13.60.60.167:3128 | SE | 987 | 3 | 9/19 |
| http://13.60.163.108:39409 | SE | 3952 | 3 | 17/61 |
| http://51.21.132.197:3128 | SE | 1443 | 3 | 11/21 |
| http://43.156.236.238:80 | SG | 998 | 3 | 26/59 |
| http://167.99.74.174:9090 | SG | 1037 | 3 | 11/21 |
| http://167.172.76.176:9090 | SG | 1300 | 3 | 9/22 |
| http://43.208.248.110:3128 | TH | 3037 | 3 | 7/19 |
