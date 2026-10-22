# Proxy status

Generated 2026-10-22T18:07:47Z by `harvest.py`.

- **2171** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4052** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39512** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 146/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2392 |
| socks5 | 1655 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 1468 |
| ID | 733 |
| CO | 137 |
| MX | 127 |
| PH | 124 |
| US | 105 |
| VE | 85 |
| BD | 82 |
| BR | 72 |
| RU | 72 |
| CN | 71 |
| IN | 62 |
| TH | 59 |
| EC | 54 |
| TR | 51 |
| DO | 49 |
| AR | 48 |
| VN | 47 |
| SG | 40 |
| PK | 33 |
| DE | 32 |
| PE | 31 |
| EG | 30 |
| CL | 27 |
| KH | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 5 | 2026-10-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 131 | 131 | 46 | 2026-10-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 133 | 133 | 59 | 2026-10-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 139 | 139 | 70 | 2026-10-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-10-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 190 | 190 | 60 | 2026-10-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 241 | 241 | 83 | 2026-10-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-22 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 424 | 424 | 94 | 2026-10-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-10-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1121 | 1121 | 751 | 2026-10-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1154 | 2026-10-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-10-22 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1921 | 1917 | 250 | 2026-10-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2402 | 2400 | 764 | 2026-10-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2677 | 2675 | 1842 | 2026-10-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4086 | 4084 | 1783 | 2026-10-22 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 75691 | 75691 | 61657 | 2026-10-22 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 82101 | 82100 | 2214 | 2026-10-22 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 816 | 65 | 132/145 |
| http://149.130.173.58:9443 | CO | 467 | 56 | 56/56 |
| http://190.0.246.213:4040 | CO | 708 | 39 | 102/110 |
| http://197.224.185.3:3128 | MU | 1856 | 37 | 106/113 |
| http://103.237.102.191:11111 | DE | 980 | 32 | 138/145 |
| http://203.252.142.217:80 | KR | 873 | 27 | 27/27 |
| http://45.186.6.104:3128 | EC | 822 | 26 | 116/123 |
| http://3.211.120.181:443 | US | 255 | 25 | 39/56 |
| http://103.133.26.72:8080 | ID | 1389 | 21 | 26/71 |
| http://103.133.26.73:3128 | ID | 1430 | 21 | 41/123 |
| http://103.133.26.119:8080 | ID | 2819 | 21 | 25/55 |
| http://176.111.37.5:39811 | HK | 1006 | 16 | 126/145 |
| http://34.43.46.91:80 | US | 1331 | 15 | 139/145 |
| socks5://43.245.199.34:1080 | HK | 1248 | 14 | 14/14 |
| http://4.144.146.21:80 | SG | 1033 | 13 | 30/37 |
| http://190.0.246.210:4040 | CO | 759 | 12 | 131/144 |
| http://43.155.62.157:443 | HK | 1259 | 12 | 40/48 |
| http://102.244.78.61:8081 | CM | 1331 | 11 | 24/31 |
| http://102.244.78.61:8090 | CM | 1329 | 11 | 27/37 |
| http://103.119.19.218:3128 | CZ | 2989 | 11 | 46/58 |
| http://186.5.94.206:999 | EC | 959 | 10 | 98/107 |
| http://49.156.44.115:8080 | KH | 5203 | 10 | 41/111 |
| http://205.164.192.115:999 | MX | 2316 | 10 | 95/143 |
| socks5://103.100.158.115:10809 | JP | 1281 | 10 | 25/33 |
| http://184.75.221.82:3118 | CA | 1242 | 9 | 96/110 |
| http://45.71.186.212:999 | EC | 5981 | 9 | 53/132 |
| http://189.51.168.165:999 | MX | 475 | 9 | 52/57 |
| http://130.110.103.245:3128 | SA | 1112 | 9 | 129/145 |
| http://102.244.78.61:8086 | CM | 1339 | 8 | 26/33 |
| http://181.78.195.137:999 | EC | 2221 | 8 | 47/145 |
| http://176.111.37.216:39811 | HK | 1099 | 8 | 117/145 |
| http://46.209.30.11:8080 | IR | 1683 | 8 | 8/8 |
| http://45.65.224.125:999 | AR | 2038 | 7 | 7/7 |
| http://102.244.78.61:8082 | CM | 1378 | 7 | 27/34 |
| http://34.88.38.81:9443 | FI | 950 | 7 | 76/110 |
| http://35.228.49.168:9443 | FI | 800 | 7 | 57/82 |
| http://103.130.61.61:8081 | ID | 3702 | 7 | 115/145 |
| http://102.244.78.61:8083 | CM | 1306 | 6 | 27/33 |
| http://102.244.78.61:8085 | CM | 1329 | 6 | 25/35 |
| http://102.244.78.61:8089 | CM | 1287 | 6 | 25/33 |
| http://177.234.217.88:999 | EC | 3541 | 6 | 57/137 |
| http://190.12.150.244:999 | EC | 2813 | 6 | 102/141 |
| http://205.237.105.49:3129 | FR | 691 | 6 | 15/16 |
| http://34.105.252.3:3128 | GB | 751 | 6 | 18/27 |
| socks5://51.15.20.32:1088 | NL | 799 | 6 | 8/9 |
| http://185.191.239.248:3128 | CH | 2623 | 5 | 101/144 |
| http://120.232.115.170:17981 | CN | 1859 | 5 | 103/144 |
| http://103.133.26.50:8080 | ID | 1400 | 5 | 24/46 |
| http://123.176.126.95:8080 | ID | 6685 | 5 | 27/91 |
| http://38.183.212.8:999 | VE | 2546 | 5 | 5/5 |
| socks5://101.36.104.46:10808 | JP | 2522 | 5 | 125/145 |
| http://185.196.182.29:8080 | AL | 2890 | 4 | 8/17 |
| http://179.48.11.6:8085 | BR | 5796 | 4 | 6/14 |
| http://102.244.78.61:8080 | CM | 1300 | 4 | 27/34 |
| http://170.254.228.90:999 | CO | 3960 | 4 | 30/128 |
| http://181.205.205.170:999 | CO | 5735 | 4 | 18/102 |
| http://186.96.111.214:999 | CO | 6059 | 4 | 60/134 |
| http://181.78.194.249:999 | EC | 2164 | 4 | 49/128 |
| http://41.128.90.54:1976 | EG | 4008 | 4 | 23/66 |
| http://45.125.64.215:443 | HK | 1118 | 4 | 14/15 |
| http://116.254.118.180:80 | ID | 4614 | 4 | 11/18 |
| http://102.36.133.62:8080 | NG | 7927 | 4 | 11/51 |
| http://34.142.210.154:40001 | SG | 3206 | 4 | 4/4 |
| http://167.172.76.176:9090 | SG | 1738 | 4 | 73/106 |
| http://34.43.46.91:443 | US | 1249 | 4 | 135/145 |
| http://165.154.162.73:8888 | US | 411 | 4 | 94/145 |
| http://38.172.160.16:999 | VE | 764 | 4 | 54/96 |
| socks5://116.237.180.55:7001 | CN | 1806 | 4 | 4/4 |
| socks5://31.58.144.19:1080 | DE | 735 | 4 | 5/6 |
| socks5://45.149.92.160:1080 | HK | 3694 | 4 | 9/12 |
| socks5://101.36.104.239:10808 | JP | 2523 | 4 | 122/145 |
| socks5://143.198.90.221:1088 | SG | 1380 | 4 | 11/13 |
| socks5://45.61.188.134:44499 | US | 5164 | 4 | 51/112 |
| socks5://193.25.215.182:22222 | US | 650 | 4 | 122/145 |
| socks5://113.22.224.63:1083 | VN | 1870 | 4 | 12/13 |
| http://103.245.109.70:21458 | BD | 1614 | 3 | 15/50 |
| http://168.195.168.182:8080 | BR | 4319 | 3 | 33/140 |
| http://186.26.92.180:58339 | BR | 4523 | 3 | 14/63 |
| http://15.223.187.219:55865 | CA | 2058 | 3 | 17/59 |
| http://207.248.0.193:999 | CL | 2150 | 3 | 23/140 |
| http://36.111.33.167:13128 | CN | 1836 | 3 | 33/108 |
| http://38.19.41.225:999 | CO | 627 | 3 | 3/3 |
| http://186.180.20.18:8080 | CO | 2445 | 3 | 6/19 |
| http://190.60.34.250:999 | CO | 5055 | 3 | 37/122 |
| http://89.58.42.118:3129 | DE | 787 | 3 | 12/34 |
| http://67.215.226.71:999 | DO | 6648 | 3 | 30/137 |
| http://45.71.186.210:999 | EC | 6215 | 3 | 42/119 |
| http://177.234.217.42:999 | EC | 2083 | 3 | 15/42 |
| http://41.128.72.140:1976 | EG | 7096 | 3 | 27/131 |
| http://41.128.77.76:1976 | EG | 2050 | 3 | 46/111 |
| http://81.19.210.10:80 | GB | 1302 | 3 | 5/6 |
| http://95.104.123.18:8080 | GE | 1311 | 3 | 9/39 |
| http://18.163.182.106:18452 | HK | 3903 | 3 | 25/112 |
| http://41.216.191.85:8080 | ID | 4266 | 3 | 17/38 |
| http://103.39.51.140:8181 | ID | 6558 | 3 | 18/80 |
| http://103.56.205.84:8080 | ID | 3538 | 3 | 23/122 |
| http://103.61.234.186:8180 | ID | 4005 | 3 | 60/142 |
| http://103.86.117.23:8080 | ID | 5257 | 3 | 15/65 |
| http://103.90.66.186:3128 | ID | 3057 | 3 | 4/7 |
| http://103.172.71.151:1111 | ID | 3562 | 3 | 3/3 |
