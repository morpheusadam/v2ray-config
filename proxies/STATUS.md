# Proxy status

Generated 2026-11-20T01:25:58Z by `harvest.py`.

- **1863** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3994** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **27938** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 148/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3434 |
| socks5 | 549 |
| socks4 | 11 |

| country | entries |
|---|---|
| ID | 1016 |
| ?? | 530 |
| NL | 316 |
| PH | 172 |
| MX | 145 |
| CO | 138 |
| US | 119 |
| TH | 113 |
| BR | 101 |
| VE | 86 |
| TR | 85 |
| IN | 82 |
| BD | 81 |
| RU | 67 |
| EC | 61 |
| AR | 55 |
| DO | 49 |
| PK | 42 |
| CN | 40 |
| VN | 39 |
| EG | 38 |
| ZA | 36 |
| SG | 33 |
| CL | 31 |
| HK | 30 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-11-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 97 | 97 | 24 | 2026-11-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 111 | 111 | 18 | 2026-11-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 35 | 2026-11-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-11-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 176 | 176 | 35 | 2026-11-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 266 | 266 | 38 | 2026-11-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 416 | 416 | 284 | 2026-11-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 444 | 2026-11-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 960 | 960 | 191 | 2026-11-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-11-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1996 | 1996 | 279 | 2026-11-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2080 | 2080 | 295 | 2026-11-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2350 | 2350 | 689 | 2026-11-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2860 | 2860 | 1523 | 2026-11-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5567 | 5567 | 4347 | 2026-11-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12125 | 12125 | 2247 | 2026-11-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 742 | 73 | 183/202 |
| http://130.110.103.245:3128 | SA | 1264 | 48 | 184/202 |
| http://27.147.155.206:12051 | BD | 3250 | 22 | 22/22 |
| http://141.94.22.37:3128 | FR | 499 | 14 | 17/18 |
| http://45.65.138.48:999 | CO | 4410 | 12 | 102/202 |
| http://45.155.226.177:3128 | HK | 616 | 11 | 16/18 |
| http://102.244.78.61:8080 | CM | 2513 | 10 | 75/91 |
| http://102.244.78.61:8081 | CM | 1194 | 9 | 72/88 |
| http://4.144.146.21:80 | SG | 1149 | 9 | 85/94 |
| http://216.152.149.246:80 | US | 2751 | 9 | 13/14 |
| http://15.229.149.81:3128 | BR | 2037 | 8 | 74/112 |
| http://43.161.254.16:3128 | HK | 5137 | 8 | 36/42 |
| http://52.128.238.98:18080 | HK | 373 | 8 | 13/17 |
| http://185.238.236.226:58080 | PL | 5670 | 8 | 61/124 |
| http://128.199.121.61:9090 | SG | 1151 | 8 | 95/122 |
| http://216.152.152.44:80 | US | 983 | 8 | 11/14 |
| socks5://193.25.215.182:22222 | US | 1838 | 8 | 167/202 |
| http://184.75.221.82:3118 | CA | 172 | 7 | 145/167 |
| http://103.130.61.61:8081 | ID | 1544 | 7 | 167/202 |
| http://34.43.46.91:443 | US | 287 | 7 | 187/202 |
| http://34.43.46.91:80 | US | 556 | 7 | 195/202 |
| http://161.22.32.31:8080 | VE | 2565 | 7 | 44/80 |
| socks5://45.61.129.165:9050 | US | 1688 | 7 | 154/202 |
| socks5://46.246.12.31:1080 | ?? | 4039 | 7 | 7/7 |
| http://190.123.83.137:999 | AR | 1386 | 6 | 33/39 |
| http://15.229.149.81:1080 | BR | 1998 | 6 | 58/104 |
| http://177.234.217.93:999 | EC | 2392 | 6 | 44/61 |
| http://43.155.62.157:443 | HK | 1075 | 6 | 89/105 |
| http://103.176.96.225:8082 | ID | 3167 | 6 | 52/147 |
| http://103.231.236.217:8182 | ID | 7136 | 6 | 11/25 |
| http://189.51.168.164:999 | MX | 491 | 6 | 34/38 |
| http://189.51.168.165:999 | MX | 1608 | 6 | 103/114 |
| http://49.149.24.144:8082 | PH | 1552 | 6 | 21/41 |
| http://104.248.151.93:9090 | SG | 1149 | 6 | 71/103 |
| http://20.98.234.24:8080 | ?? | 105 | 6 | 6/6 |
| socks5://103.13.19.219:10808 | JP | 2566 | 6 | 12/19 |
| socks5://69.55.49.177:38182 | US | 1307 | 6 | 46/57 |
| http://186.96.111.214:999 | CO | 4190 | 5 | 97/191 |
| http://103.237.102.191:11111 | DE | 750 | 5 | 189/202 |
| http://198.244.254.77:3128 | GB | 1868 | 5 | 69/86 |
| http://36.95.245.7:8090 | ID | 7820 | 5 | 15/40 |
| http://103.61.234.186:8180 | ID | 2748 | 5 | 90/199 |
| http://103.132.54.42:8080 | ID | 6561 | 5 | 31/111 |
| http://210.87.74.189:3125 | ID | 7338 | 5 | 10/26 |
| http://36.37.251.137:8080 | KH | 5378 | 5 | 20/88 |
| http://201.46.86.37:8080 | MX | 3851 | 5 | 12/36 |
| http://206.135.76.38:8080 | MX | 1056 | 5 | 15/30 |
| http://49.146.48.103:8082 | PH | 2254 | 5 | 22/40 |
| http://90.156.160.234:3128 | UZ | 1467 | 5 | 41/90 |
| http://200.59.191.27:999 | VE | 3959 | 5 | 135/197 |
| http://172.235.157.127:3128 | ?? | 374 | 5 | 5/5 |
| socks5://45.194.33.12:30001 | HK | 1570 | 5 | 29/78 |
| socks5://45.194.33.12:30002 | HK | 2955 | 5 | 28/46 |
| http://103.150.49.90:8090 | BD | 4435 | 4 | 45/195 |
| http://2.28.105.45:8888 | DE | 3208 | 4 | 28/103 |
| http://45.186.6.104:3128 | EC | 650 | 4 | 170/180 |
| http://177.234.226.83:1994 | EC | 2608 | 4 | 36/160 |
| http://197.164.101.10:1981 | EG | 2423 | 4 | 9/29 |
| http://197.164.101.11:1981 | EG | 3988 | 4 | 6/19 |
| http://18.163.182.106:18452 | HK | 3640 | 4 | 42/169 |
| http://49.213.59.105:8082 | ID | 5438 | 4 | 52/161 |
| http://103.133.26.50:8080 | ID | 1516 | 4 | 68/103 |
| http://103.133.26.72:8080 | ID | 3430 | 4 | 76/128 |
| http://103.133.26.73:3128 | ID | 1569 | 4 | 92/180 |
| http://103.133.26.119:8080 | ID | 1950 | 4 | 73/112 |
| http://103.156.249.112:8085 | ID | 4289 | 4 | 41/152 |
| http://103.158.210.80:8082 | ID | 1561 | 4 | 63/192 |
| http://103.184.180.135:2021 | ID | 7262 | 4 | 25/109 |
| http://103.195.65.243:8080 | ID | 7911 | 4 | 14/54 |
| http://103.248.9.229:8090 | ID | 4554 | 4 | 23/96 |
| http://157.10.90.65:8088 | ID | 3534 | 4 | 13/34 |
| http://160.187.174.71:8080 | ID | 7662 | 4 | 13/32 |
| http://51.85.44.162:8089 | IL | 2063 | 4 | 29/52 |
| http://46.209.15.187:8080 | IR | 4296 | 4 | 15/40 |
| http://110.74.195.34:25 | KH | 4778 | 4 | 66/195 |
| http://185.238.238.165:58080 | PL | 876 | 4 | 48/92 |
| http://159.223.41.216:9090 | SG | 1161 | 4 | 118/162 |
| http://3.21.247.154:59330 | US | 1725 | 4 | 37/158 |
| http://69.87.216.54:7989 | US | 332 | 4 | 75/147 |
| http://68.183.226.190:9090 | ?? | 1181 | 4 | 6/10 |
| http://91.134.141.4:3128 | ?? | 486 | 4 | 4/4 |
| http://114.246.207.179:8888 | ?? | 1635 | 4 | 4/4 |
| http://195.142.250.38:8080 | ?? | 1696 | 4 | 5/6 |
| http://222.128.176.152:8888 | ?? | 1693 | 4 | 4/4 |
| socks5://49.13.22.249:10805 | DE | 6102 | 4 | 67/120 |
| socks5://103.119.1.160:5555 | HK | 1531 | 4 | 12/17 |
| socks5://193.218.118.128:1080 | UA | 2014 | 4 | 42/58 |
| socks5://45.61.188.134:44499 | US | 237 | 4 | 91/169 |
| socks5://103.124.172.134:1080 | ?? | 1582 | 4 | 4/4 |
| http://103.204.211.48:32255 | BD | 7149 | 3 | 31/197 |
| http://202.4.127.89:81 | BD | 2012 | 3 | 13/43 |
| http://170.84.145.76:8088 | BR | 6361 | 3 | 18/75 |
| http://177.130.104.106:33333 | BR | 4148 | 3 | 8/27 |
| http://83.143.24.66:80 | BW | 2634 | 3 | 41/148 |
| http://35.183.78.223:58093 | CA | 1205 | 3 | 33/100 |
| http://56.112.93.245:32650 | CA | 2522 | 3 | 29/101 |
| http://102.244.78.61:8083 | CM | 2223 | 3 | 72/90 |
| http://111.196.24.150:8888 | CN | 1796 | 3 | 25/52 |
| http://123.112.214.167:9000 | CN | 4102 | 3 | 19/113 |
| http://123.121.142.252:8888 | CN | 7042 | 3 | 54/124 |
