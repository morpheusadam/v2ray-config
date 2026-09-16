# Proxy status

Generated 2026-09-16T22:18:31Z by `harvest.py`.

- **983** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1896** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **23846** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 133/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1077 |
| socks5 | 809 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 603 |
| ID | 231 |
| CN | 86 |
| RU | 77 |
| US | 73 |
| CO | 54 |
| MX | 51 |
| VN | 51 |
| BD | 44 |
| DE | 43 |
| SG | 40 |
| VE | 37 |
| PH | 34 |
| FR | 33 |
| IN | 28 |
| JP | 28 |
| EC | 26 |
| EG | 26 |
| BR | 24 |
| CA | 17 |
| FI | 17 |
| KH | 16 |
| KR | 16 |
| SE | 16 |
| HK | 15 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 3 | 3 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 64 | 64 | 36 | 2026-09-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 85 | 85 | 42 | 2026-09-16 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 125 | 125 | 36 | 2026-09-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 70 | 2026-09-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 163 | 163 | 62 | 2026-09-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 190 | 190 | 92 | 2026-09-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 204 | 204 | 36 | 2026-09-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 294 | 294 | 123 | 2026-09-16 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-09-16 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1447 | 1443 | 356 | 2026-09-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1142 | 2026-09-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1600 | 2026-09-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2135 | 2133 | 1642 | 2026-09-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2200 | 2198 | 712 | 2026-09-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2549 | 2547 | 699 | 2026-09-16 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 9193 | 9193 | 5787 | 2026-09-16 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 14213 | 14212 | 2041 | 2026-09-16 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 857 | 67 | 72/75 |
| http://34.43.46.91:80 | US | 771 | 67 | 72/75 |
| http://95.211.174.135:3128 | NL | 1227 | 61 | 74/75 |
| http://185.200.188.234:10001 | RU | 1212 | 61 | 74/75 |
| http://130.110.103.245:3128 | SA | 1218 | 61 | 73/75 |
| http://1.231.81.166:3128 | KR | 1437 | 40 | 72/75 |
| http://176.111.37.5:39811 | HK | 928 | 35 | 69/75 |
| http://190.97.236.128:999 | VE | 818 | 32 | 63/65 |
| http://190.97.236.129:999 | VE | 812 | 32 | 63/65 |
| http://95.3.69.222:8080 | TR | 1707 | 30 | 72/75 |
| socks5://107.167.18.122:443 | US | 1307 | 20 | 26/27 |
| http://103.237.102.191:11111 | DE | 954 | 19 | 71/75 |
| socks5://83.147.216.208:1080 | FI | 1255 | 19 | 25/43 |
| socks5://144.91.111.48:1088 | FR | 3216 | 17 | 45/75 |
| http://184.75.221.82:3118 | CA | 287 | 16 | 37/40 |
| socks5://144.91.121.61:1088 | FR | 4258 | 16 | 66/75 |
| http://91.134.141.4:3128 | FR | 681 | 14 | 34/36 |
| http://186.5.94.206:999 | EC | 2601 | 12 | 35/37 |
| http://107.150.41.226:18080 | US | 412 | 12 | 12/12 |
| socks5://213.199.47.140:1080 | FR | 3008 | 12 | 34/41 |
| http://103.177.118.145:8118 | BD | 3877 | 8 | 52/56 |
| http://190.0.246.210:4040 | CO | 824 | 8 | 65/74 |
| http://186.33.45.219:999 | EC | 6786 | 8 | 38/64 |
| http://84.8.216.230:2001 | MA | 2891 | 8 | 8/8 |
| http://43.156.199.63:8080 | SG | 2699 | 8 | 9/10 |
| http://38.51.207.104:8080 | VE | 1998 | 8 | 15/16 |
| http://172.104.56.95:8888 | SG | 2173 | 7 | 7/7 |
| socks5://103.162.30.189:10808 | VN | 4114 | 7 | 9/10 |
| socks5://160.22.17.4:9988 | VN | 1698 | 7 | 32/71 |
| http://34.88.38.81:9443 | FI | 907 | 6 | 27/40 |
| http://35.228.49.168:9443 | FI | 809 | 6 | 8/12 |
| http://197.224.185.3:3128 | MU | 2104 | 6 | 39/43 |
| http://189.51.168.164:999 | MX | 449 | 6 | 39/40 |
| http://45.132.252.25:49156 | RU | 1489 | 6 | 6/6 |
| http://108.61.213.218:80 | AU | 1254 | 5 | 13/16 |
| http://113.45.195.147:3128 | CN | 1673 | 5 | 27/40 |
| http://115.231.181.40:8128 | CN | 2181 | 5 | 33/74 |
| http://153.80.240.2:1080 | NL | 863 | 5 | 5/5 |
| http://5.129.254.5:8888 | RU | 1383 | 5 | 28/30 |
| http://5.129.254.49:8888 | RU | 1761 | 5 | 29/30 |
| http://5.129.254.51:8888 | RU | 2322 | 5 | 29/30 |
| http://5.129.254.60:8888 | RU | 1168 | 5 | 28/29 |
| http://5.129.254.70:8888 | RU | 1343 | 5 | 29/30 |
| http://5.129.254.129:8888 | RU | 2174 | 5 | 34/36 |
| http://5.129.254.154:8888 | RU | 1217 | 5 | 25/26 |
| http://43.128.76.140:8081 | SG | 3450 | 5 | 5/5 |
| http://193.104.179.115:3128 | UZ | 1349 | 5 | 23/40 |
| http://154.59.56.74:999 | VE | 6943 | 5 | 26/38 |
| socks5://57.128.231.218:1004 | PL | 1262 | 5 | 6/9 |
| socks5://45.32.160.61:1088 | US | 449 | 5 | 26/28 |
| http://185.195.71.218:18080 | CH | 707 | 4 | 6/12 |
| http://47.121.139.13:3128 | CN | 1826 | 4 | 35/74 |
| http://111.230.27.213:3128 | CN | 3551 | 4 | 30/75 |
| http://120.232.115.170:17981 | CN | 2409 | 4 | 53/74 |
| http://190.0.246.211:4040 | CO | 926 | 4 | 63/75 |
| http://190.0.246.213:4040 | CO | 570 | 4 | 33/40 |
| http://37.59.125.131:8888 | FR | 1867 | 4 | 59/75 |
| http://213.111.146.36:18080 | NL | 636 | 4 | 7/12 |
| http://157.85.108.47:3128 | TH | 1210 | 4 | 32/43 |
| socks5://193.233.139.106:1080 | FI | 1063 | 4 | 18/33 |
| socks5://101.36.104.46:10808 | JP | 2369 | 4 | 66/75 |
| socks5://95.220.142.90:1080 | RU | 1333 | 4 | 4/4 |
| socks5://144.24.47.42:1080 | US | 555 | 4 | 39/71 |
| socks5://193.25.215.182:22222 | US | 1502 | 4 | 69/75 |
| http://147.182.156.27:8080 | CA | 630 | 3 | 3/3 |
| http://47.110.226.74:19991 | CN | 2652 | 3 | 32/73 |
| http://114.249.237.87:8888 | CN | 1761 | 3 | 20/39 |
| http://123.121.211.160:8888 | CN | 1112 | 3 | 8/21 |
| http://221.221.159.97:8888 | CN | 6728 | 3 | 10/28 |
| http://41.128.72.140:1981 | EG | 1557 | 3 | 13/57 |
| http://197.164.101.13:1981 | EG | 1479 | 3 | 28/64 |
| http://85.235.150.219:3128 | IT | 5952 | 3 | 3/3 |
| http://38.19.111.74:8080 | MX | 5262 | 3 | 9/40 |
| http://13.212.214.47:8090 | SG | 3506 | 3 | 12/33 |
| http://34.87.80.221:30000 | SG | 1607 | 3 | 14/73 |
| http://167.99.74.174:9090 | SG | 1035 | 3 | 19/35 |
| http://167.172.76.176:9090 | SG | 1026 | 3 | 18/36 |
| http://154.59.56.73:999 | VE | 3250 | 3 | 37/47 |
| http://154.59.56.78:999 | VE | 4855 | 3 | 19/31 |
| http://163.181.207.169:9999 | VN | 1272 | 3 | 22/73 |
| socks5://135.125.232.151:1080 | DE | 1613 | 3 | 5/6 |
| socks5://51.178.49.241:1088 | FR | 1080 | 3 | 30/36 |
| socks5://123.58.219.171:10808 | HK | 2907 | 3 | 60/75 |
| socks5://144.24.111.128:1088 | IN | 2447 | 3 | 57/75 |
| socks5://130.255.94.32:5080 | IQ | 5637 | 3 | 18/45 |
| socks5://202.62.52.20:1080 | KH | 2777 | 3 | 17/42 |
| socks5://203.189.150.44:1080 | KH | 3002 | 3 | 29/75 |
| socks5://115.136.121.54:9050 | KR | 4677 | 3 | 20/72 |
| socks5://121.169.46.116:1090 | KR | 2917 | 3 | 48/75 |
| socks5://45.74.31.42:11479 | NL | 1426 | 3 | 3/3 |
| socks5://43.135.176.121:1080 | US | 1488 | 3 | 26/30 |
| socks5://45.61.129.165:9050 | US | 2825 | 3 | 62/75 |
| socks5://93.127.133.109:1081 | US | 1132 | 3 | 4/6 |
| http://27.147.138.166:8158 | BD | 4749 | 2 | 2/2 |
| http://203.76.117.226:8118 | BD | 2743 | 2 | 2/2 |
| http://35.182.12.78:57895 | CA | 1484 | 2 | 4/29 |
| http://35.183.29.62:8181 | CA | 2268 | 2 | 7/43 |
| http://39.106.170.168:8080 | CN | 4100 | 2 | 36/73 |
| http://47.97.114.99:13357 | CN | 4808 | 2 | 3/4 |
| http://122.246.3.12:17981 | CN | 6547 | 2 | 33/69 |
