# Proxy status

Generated 2026-10-18T21:51:14Z by `harvest.py`.

- **2052** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3826** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39643** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 160/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2286 |
| socks5 | 1532 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 1270 |
| ID | 754 |
| PH | 130 |
| RU | 118 |
| MX | 110 |
| CO | 109 |
| US | 92 |
| VN | 82 |
| CN | 73 |
| BD | 71 |
| VE | 69 |
| EC | 66 |
| BR | 64 |
| IN | 59 |
| DO | 55 |
| DE | 48 |
| TR | 45 |
| AR | 37 |
| TH | 36 |
| SG | 31 |
| PE | 27 |
| PK | 27 |
| SY | 27 |
| CL | 25 |
| EG | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 1 | 2026-10-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 54 | 2026-10-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 85 | 2026-10-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 163 | 163 | 79 | 2026-10-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 280 | 280 | 80 | 2026-10-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 376 | 376 | 154 | 2026-10-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 456 | 456 | 161 | 2026-10-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 475 | 475 | 126 | 2026-10-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-10-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 558 | 558 | 353 | 2026-10-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-10-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-10-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1733 | 1731 | 79 | 2026-10-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-10-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2439 | 2437 | 785 | 2026-10-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2793 | 2791 | 1894 | 2026-10-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3271 | 3269 | 1249 | 2026-10-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 69935 | 69935 | 56273 | 2026-10-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 77328 | 77327 | 2505 | 2026-10-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2503 | 58 | 125/138 |
| http://149.130.173.58:9443 | CO | 478 | 49 | 49/49 |
| http://190.0.246.213:4040 | CO | 678 | 32 | 95/103 |
| http://197.224.185.3:3128 | MU | 1961 | 30 | 99/106 |
| http://103.237.102.191:11111 | DE | 927 | 25 | 131/138 |
| http://203.252.142.217:80 | KR | 973 | 20 | 20/20 |
| http://45.186.6.104:3128 | EC | 895 | 19 | 109/116 |
| http://3.211.120.181:443 | US | 277 | 18 | 32/49 |
| http://5.129.254.5:8888 | RU | 1708 | 15 | 82/93 |
| http://5.129.254.49:8888 | RU | 1247 | 15 | 83/93 |
| http://5.129.254.51:8888 | RU | 1381 | 15 | 83/93 |
| http://5.129.254.60:8888 | RU | 1357 | 15 | 82/92 |
| http://5.129.254.70:8888 | RU | 2258 | 15 | 83/93 |
| http://5.129.254.129:8888 | RU | 1306 | 15 | 88/99 |
| http://5.129.254.154:8888 | RU | 1282 | 15 | 79/89 |
| http://5.129.254.215:8888 | RU | 1249 | 15 | 32/35 |
| http://5.129.254.243:8888 | RU | 1325 | 15 | 32/34 |
| http://103.133.26.50:8080 | ID | 1546 | 14 | 18/39 |
| http://103.133.26.72:8080 | ID | 1492 | 14 | 19/64 |
| http://103.133.26.73:3128 | ID | 1550 | 14 | 34/116 |
| http://103.133.26.119:8080 | ID | 1957 | 14 | 18/48 |
| socks5://67.207.92.87:1088 | US | 446 | 14 | 82/137 |
| http://147.45.164.178:8888 | RU | 2472 | 12 | 12/12 |
| http://128.199.121.61:9090 | SG | 1118 | 10 | 48/58 |
| socks5://171.25.158.95:1080 | SE | 3626 | 10 | 45/53 |
| socks5://47.87.97.94:1080 | TH | 1833 | 10 | 13/14 |
| http://205.237.105.49:3129 | FR | 786 | 9 | 9/9 |
| http://198.244.254.77:3128 | GB | 7636 | 9 | 20/22 |
| http://176.111.37.5:39811 | HK | 822 | 9 | 119/138 |
| http://34.43.46.91:443 | US | 1334 | 9 | 129/138 |
| http://45.125.64.215:443 | HK | 1388 | 8 | 8/8 |
| http://140.238.32.108:3128 | JP | 1392 | 8 | 71/137 |
| http://34.43.46.91:80 | US | 2989 | 8 | 132/138 |
| socks5://47.238.126.208:1080 | HK | 1788 | 8 | 26/43 |
| socks5://101.36.104.239:10808 | JP | 3813 | 8 | 117/138 |
| http://45.245.208.180:8080 | EG | 1328 | 7 | 10/11 |
| http://152.67.191.232:6800 | IN | 1331 | 7 | 7/7 |
| socks5://43.245.199.34:1080 | HK | 1419 | 7 | 7/7 |
| http://221.221.159.97:8888 | CN | 1651 | 6 | 44/91 |
| http://221.221.163.25:8888 | CN | 1631 | 6 | 36/92 |
| http://177.234.221.201:999 | EC | 4039 | 6 | 16/41 |
| http://41.196.16.226:1976 | EG | 2598 | 6 | 6/6 |
| http://4.144.146.21:80 | SG | 1050 | 6 | 23/30 |
| http://146.190.80.158:9090 | SG | 1626 | 6 | 47/64 |
| http://200.59.191.27:999 | VE | 7203 | 6 | 89/133 |
| socks5://62.83.34.101:1080 | AT | 1634 | 6 | 6/6 |
| socks5://113.22.224.63:1083 | VN | 2651 | 6 | 6/6 |
| http://168.227.239.66:10000 | BR | 1406 | 5 | 5/5 |
| http://190.0.246.210:4040 | CO | 1403 | 5 | 124/137 |
| http://43.155.62.157:443 | HK | 1237 | 5 | 33/41 |
| http://187.251.224.167:8081 | MX | 5468 | 5 | 26/98 |
| http://43.156.55.191:5001 | SG | 1315 | 5 | 5/5 |
| http://104.248.151.93:9090 | SG | 1274 | 5 | 32/39 |
| http://154.59.56.72:999 | VE | 3217 | 5 | 70/97 |
| http://103.82.20.76:8080 | VN | 1649 | 5 | 40/136 |
| socks5://148.251.68.232:8888 | DE | 1858 | 5 | 12/17 |
| socks5://31.129.107.119:443 | RU | 5819 | 5 | 13/17 |
| http://187.102.219.32:999 | AR | 1971 | 4 | 43/137 |
| http://118.179.45.194:81 | BD | 6922 | 4 | 19/80 |
| http://102.244.78.61:8081 | CM | 2897 | 4 | 17/24 |
| http://102.244.78.61:8085 | CM | 7711 | 4 | 19/28 |
| http://102.244.78.61:8090 | CM | 1279 | 4 | 20/30 |
| http://123.121.75.126:8888 | CN | 1754 | 4 | 7/9 |
| http://45.65.137.218:999 | CO | 934 | 4 | 36/103 |
| http://103.119.19.218:3128 | CZ | 4465 | 4 | 39/51 |
| http://41.65.55.27:1976 | EG | 1943 | 4 | 31/120 |
| http://41.128.77.76:1981 | EG | 3047 | 4 | 38/92 |
| http://111.92.88.27:3128 | IN | 1408 | 4 | 21/107 |
| http://161.49.90.70:1337 | PH | 6337 | 4 | 13/76 |
| http://95.81.107.187:3128 | SE | 2953 | 4 | 4/4 |
| http://152.42.177.32:8888 | SG | 1178 | 4 | 61/98 |
| http://44.216.83.206:3128 | US | 332 | 4 | 8/11 |
| http://38.51.207.117:999 | VE | 4950 | 4 | 32/115 |
| http://185.226.194.226:999 | VE | 1796 | 4 | 11/34 |
| socks5://121.46.226.221:10808 | CN | 1794 | 4 | 13/15 |
| socks5://93.99.104.47:1080 | CZ | 1338 | 4 | 4/4 |
| socks5://213.199.47.140:1080 | FR | 1093 | 4 | 81/104 |
| socks5://123.58.219.171:10808 | HK | 3903 | 4 | 108/138 |
| socks5://212.77.75.25:1088 | IT | 1032 | 4 | 32/38 |
| socks5://143.198.90.221:1088 | SG | 2646 | 4 | 5/6 |
| socks5://147.93.172.241:5555 | SG | 1734 | 4 | 19/49 |
| socks5://45.61.129.165:9050 | US | 1778 | 4 | 104/138 |
| socks5://107.174.30.92:1080 | US | 483 | 4 | 19/34 |
| socks5://193.25.215.182:22222 | US | 2139 | 4 | 116/138 |
| http://45.65.224.74:999 | AR | 2216 | 3 | 3/3 |
| http://45.65.225.17:999 | AR | 4229 | 3 | 3/3 |
| http://187.102.219.34:999 | AR | 1168 | 3 | 47/89 |
| http://187.102.219.64:999 | AR | 1342 | 3 | 46/77 |
| http://177.130.25.76:8080 | BR | 3109 | 3 | 6/21 |
| http://185.191.239.248:3128 | CH | 7528 | 3 | 95/137 |
| http://1.15.53.214:8888 | CN | 1783 | 3 | 35/132 |
| http://61.149.134.158:8888 | CN | 1778 | 3 | 39/103 |
| http://114.254.50.97:8888 | CN | 3521 | 3 | 48/103 |
| http://123.121.209.108:8888 | CN | 2268 | 3 | 29/88 |
| http://186.96.111.214:999 | CO | 4218 | 3 | 54/127 |
| http://190.7.138.78:8080 | CO | 3183 | 3 | 30/67 |
| http://91.107.247.193:7001 | DE | 878 | 3 | 3/3 |
| http://38.156.233.173:999 | DO | 2527 | 3 | 19/127 |
| http://179.60.189.81:999 | EC | 5111 | 3 | 6/10 |
| http://181.188.203.40:999 | EC | 2649 | 3 | 16/35 |
