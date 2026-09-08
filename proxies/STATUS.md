# Proxy status

Generated 2026-09-08T22:00:55Z by `harvest.py`.

- **895** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1405** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16126** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 208/600 (35%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1091 |
| socks5 | 299 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 254 |
| US | 127 |
| CN | 81 |
| NL | 58 |
| CO | 52 |
| MX | 52 |
| RU | 51 |
| DE | 47 |
| PH | 37 |
| BD | 33 |
| TH | 32 |
| IN | 31 |
| FR | 30 |
| VN | 30 |
| EC | 27 |
| JP | 26 |
| VE | 25 |
| EG | 24 |
| BR | 23 |
| HK | 23 |
| SG | 20 |
| KH | 19 |
| SE | 18 |
| CL | 17 |
| FI | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 88 | 88 | 43 | 2026-09-08 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-08 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 104 | 104 | 26 | 2026-09-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 135 | 135 | 32 | 2026-09-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 81 | 2026-09-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 166 | 166 | 91 | 2026-09-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 166 | 166 | 25 | 2026-09-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 196 | 196 | 70 | 2026-09-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 321 | 321 | 122 | 2026-09-08 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 612 | 612 | 258 | 2026-09-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-09-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-09-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1707 | 1705 | 225 | 2026-09-08 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1746 | 1742 | 544 | 2026-09-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1599 | 2026-09-08 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 1923 | 1923 | 1522 | 2026-09-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2138 | 2136 | 733 | 2026-09-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2293 | 2291 | 1797 | 2026-09-08 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 2798 | 51 | 56/59 |
| http://34.43.46.91:80 | US | 2502 | 51 | 56/59 |
| http://95.211.174.135:3128 | NL | 1697 | 45 | 58/59 |
| http://185.200.188.234:10001 | RU | 983 | 45 | 58/59 |
| http://130.110.103.245:3128 | SA | 1404 | 45 | 57/59 |
| http://199.7.149.96:3128 | US | 27 | 38 | 38/38 |
| http://64.112.184.210:3128 | US | 162 | 37 | 58/59 |
| http://103.211.103.170:3128 | HK | 6912 | 31 | 31/31 |
| http://68.178.174.239:3128 | US | 1167 | 27 | 27/27 |
| http://68.178.174.239:8888 | US | 1163 | 27 | 27/27 |
| http://1.231.81.166:3128 | KR | 1606 | 24 | 56/59 |
| http://189.51.168.164:999 | MX | 369 | 24 | 24/24 |
| socks5://193.25.215.182:22222 | US | 2787 | 22 | 55/59 |
| http://116.202.172.187:11000 | DE | 683 | 20 | 20/20 |
| http://91.134.141.4:3128 | FR | 3290 | 20 | 20/20 |
| http://176.111.37.5:39811 | HK | 1610 | 19 | 53/59 |
| http://14.251.13.20:8080 | VN | 1462 | 19 | 30/31 |
| http://181.78.23.187:999 | CO | 719 | 16 | 26/28 |
| http://181.78.74.252:999 | CO | 813 | 16 | 48/50 |
| http://181.78.74.253:999 | CO | 810 | 16 | 48/50 |
| http://190.97.236.128:999 | VE | 595 | 16 | 47/49 |
| http://190.97.236.129:999 | VE | 593 | 16 | 47/49 |
| http://103.177.118.145:8118 | BD | 6232 | 15 | 38/40 |
| http://186.5.94.206:999 | EC | 1778 | 15 | 20/21 |
| socks5://147.45.60.124:1082 | US | 5281 | 15 | 35/59 |
| http://176.111.37.216:39811 | HK | 1263 | 14 | 47/59 |
| http://197.224.185.3:3128 | MU | 1751 | 14 | 25/27 |
| http://5.129.254.49:8888 | RU | 2147 | 14 | 14/14 |
| http://5.129.254.51:8888 | RU | 3746 | 14 | 14/14 |
| http://5.129.254.70:8888 | RU | 2150 | 14 | 14/14 |
| http://95.3.69.222:8080 | TR | 1968 | 14 | 56/59 |
| socks5://43.135.176.121:1080 | US | 1487 | 14 | 14/14 |
| socks5://45.61.129.165:9050 | US | 3359 | 14 | 50/59 |
| http://5.129.254.60:8888 | RU | 2473 | 13 | 13/13 |
| http://157.85.97.204:3128 | TH | 1408 | 13 | 21/24 |
| http://5.129.254.5:8888 | RU | 2037 | 12 | 13/14 |
| http://202.28.194.139:31280 | TH | 2102 | 12 | 56/59 |
| socks5://185.222.138.237:1080 | XK | 826 | 12 | 12/12 |
| http://190.97.241.106:999 | VE | 3840 | 11 | 20/43 |
| http://185.191.239.248:3128 | CH | 4100 | 10 | 45/58 |
| http://5.129.254.154:8888 | RU | 1453 | 10 | 10/10 |
| http://157.85.108.47:3128 | TH | 2672 | 8 | 21/27 |
| http://161.35.181.96:999 | US | 297 | 8 | 8/8 |
| socks5://108.174.152.80:1080 | MX | 498 | 8 | 8/8 |
| socks5://107.181.252.58:1081 | US | 1846 | 8 | 8/8 |
| http://190.0.246.210:4040 | CO | 2692 | 7 | 52/58 |
| http://45.186.6.104:3128 | EC | 642 | 7 | 36/37 |
| http://43.99.60.244:8089 | HK | 1275 | 7 | 8/9 |
| http://103.130.61.61:8081 | ID | 4792 | 7 | 48/59 |
| http://52.21.158.119:3128 | US | 120 | 7 | 11/12 |
| http://107.181.252.58:1082 | US | 1512 | 7 | 7/7 |
| socks5://5.255.113.177:1080 | NL | 777 | 7 | 17/58 |
| socks5://213.165.38.49:1080 | NL | 2455 | 7 | 9/26 |
| socks5://58.187.162.191:1083 | VN | 1917 | 7 | 7/7 |
| http://190.0.246.211:4040 | CO | 3893 | 6 | 50/59 |
| http://103.157.200.126:3128 | PK | 3171 | 6 | 12/36 |
| http://129.226.89.151:80 | SG | 1759 | 6 | 6/6 |
| http://101.79.26.53:80 | KR | 988 | 5 | 5/5 |
| http://154.59.56.76:999 | VE | 3232 | 5 | 15/19 |
| socks5://118.179.102.168:9090 | BD | 4921 | 5 | 5/5 |
| http://124.128.149.84:8090 | CN | 7071 | 4 | 16/55 |
| http://196.204.3.21:1981 | EG | 5848 | 4 | 9/38 |
| http://213.131.85.29:1981 | EG | 900 | 4 | 4/4 |
| http://34.88.38.81:9443 | FI | 644 | 4 | 15/24 |
| http://37.59.125.131:8888 | FR | 1675 | 4 | 45/59 |
| http://43.207.239.56:3128 | JP | 840 | 4 | 4/4 |
| http://38.194.246.34:999 | MX | 4186 | 4 | 28/50 |
| http://203.177.217.222:8082 | PH | 1707 | 4 | 4/4 |
| http://107.167.18.122:443 | US | 3442 | 4 | 10/11 |
| http://201.71.2.24:999 | VE | 4447 | 4 | 11/47 |
| http://210.211.113.34:80 | VN | 4745 | 4 | 26/31 |
| socks5://180.165.49.4:1088 | CN | 7528 | 4 | 4/4 |
| socks5://31.76.111.88:1080 | DE | 2731 | 4 | 9/31 |
| socks5://109.123.251.109:1080 | FR | 4552 | 4 | 26/59 |
| socks5://5.255.123.162:1080 | NL | 653 | 4 | 19/42 |
| socks5://85.143.254.38:1080 | RU | 1235 | 4 | 18/53 |
| socks5://147.45.60.139:1082 | US | 2205 | 4 | 31/50 |
| http://103.141.174.38:11411 | BD | 5676 | 3 | 17/43 |
| http://39.106.170.168:8080 | CN | 1889 | 3 | 27/57 |
| http://47.121.139.13:3128 | CN | 2511 | 3 | 25/58 |
| http://103.237.102.191:11111 | DE | 961 | 3 | 55/59 |
| http://152.53.183.107:8081 | DE | 1958 | 3 | 9/12 |
| http://103.167.156.202:8084 | ID | 3337 | 3 | 5/31 |
| http://187.251.224.167:80 | MX | 6174 | 3 | 14/55 |
| http://205.164.192.115:999 | MX | 3121 | 3 | 33/57 |
| http://43.134.141.85:80 | SG | 1177 | 3 | 19/57 |
| http://104.218.199.24:16062 | US | 7717 | 3 | 3/3 |
| socks5://49.13.22.249:10801 | DE | 1310 | 3 | 18/28 |
| socks5://83.147.216.208:1080 | FI | 3944 | 3 | 9/27 |
| socks5://51.178.49.241:1088 | FR | 2229 | 3 | 16/20 |
| socks5://47.76.175.249:1080 | HK | 1394 | 3 | 9/10 |
| socks5://5.255.99.75:1080 | NL | 3687 | 3 | 16/34 |
| socks5://147.45.60.110:1082 | US | 199 | 3 | 19/58 |
| http://39.106.165.196:8080 | CN | 1867 | 2 | 27/55 |
| http://111.192.19.39:8888 | CN | 3481 | 2 | 13/23 |
| http://114.246.196.30:8888 | CN | 7030 | 2 | 12/23 |
| http://123.121.122.28:8888 | CN | 1755 | 2 | 6/8 |
| http://181.78.17.131:999 | CO | 4090 | 2 | 14/56 |
| http://38.75.82.212:999 | DO | 3690 | 2 | 18/53 |
| http://45.71.186.210:999 | EC | 4661 | 2 | 6/33 |
