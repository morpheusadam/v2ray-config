# Proxy status

Generated 2026-10-18T16:40:21Z by `harvest.py`.

- **2520** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4444** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **38924** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 161/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2565 |
| http | 1872 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 2284 |
| ID | 610 |
| RU | 109 |
| PH | 107 |
| CO | 90 |
| MX | 89 |
| BD | 73 |
| VN | 72 |
| CN | 65 |
| US | 64 |
| VE | 58 |
| EC | 54 |
| IN | 52 |
| TR | 45 |
| DE | 43 |
| AR | 42 |
| DO | 42 |
| BR | 41 |
| TH | 37 |
| SG | 33 |
| PK | 30 |
| EG | 25 |
| CL | 23 |
| HK | 23 |
| PE | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-10-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 107 | 107 | 35 | 2026-10-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 109 | 109 | 63 | 2026-10-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 148 | 148 | 52 | 2026-10-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-10-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 272 | 272 | 93 | 2026-10-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 587 | 587 | 211 | 2026-10-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 457 | 2026-10-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 804 | 804 | 124 | 2026-10-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1170 | 1170 | 785 | 2026-10-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-10-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1599 | 2026-10-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1839 | 1839 | 120 | 2026-10-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2260 | 2258 | 776 | 2026-10-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2622 | 2620 | 1799 | 2026-10-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2701 | 2699 | 841 | 2026-10-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 69470 | 69470 | 55444 | 2026-10-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 76162 | 76161 | 2374 | 2026-10-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 833 | 57 | 124/137 |
| http://149.130.173.58:9443 | CO | 523 | 48 | 48/48 |
| http://190.0.246.213:4040 | CO | 598 | 31 | 94/102 |
| http://197.224.185.3:3128 | MU | 1910 | 29 | 98/105 |
| http://103.237.102.191:11111 | DE | 868 | 24 | 130/137 |
| http://203.252.142.217:80 | KR | 869 | 19 | 19/19 |
| http://45.186.6.104:3128 | EC | 760 | 18 | 108/115 |
| http://3.211.120.181:443 | US | 248 | 17 | 31/48 |
| http://103.130.61.61:8081 | ID | 3475 | 16 | 108/137 |
| http://5.129.254.5:8888 | RU | 1108 | 14 | 81/92 |
| http://5.129.254.49:8888 | RU | 1182 | 14 | 82/92 |
| http://5.129.254.51:8888 | RU | 1156 | 14 | 82/92 |
| http://5.129.254.60:8888 | RU | 1217 | 14 | 81/91 |
| http://5.129.254.70:8888 | RU | 1165 | 14 | 82/92 |
| http://5.129.254.129:8888 | RU | 1150 | 14 | 87/98 |
| http://5.129.254.154:8888 | RU | 1830 | 14 | 78/88 |
| http://5.129.254.215:8888 | RU | 1070 | 14 | 31/34 |
| http://5.129.254.243:8888 | RU | 1161 | 14 | 31/33 |
| http://103.133.26.50:8080 | ID | 1367 | 13 | 17/38 |
| http://103.133.26.72:8080 | ID | 1402 | 13 | 18/63 |
| http://103.133.26.73:3128 | ID | 1428 | 13 | 33/115 |
| http://103.133.26.119:8080 | ID | 4242 | 13 | 17/47 |
| socks5://67.207.92.87:1088 | US | 533 | 13 | 81/136 |
| http://147.45.164.178:8888 | RU | 1167 | 11 | 11/11 |
| http://128.199.121.61:9090 | SG | 1038 | 9 | 47/57 |
| socks5://171.25.158.95:1080 | SE | 4126 | 9 | 44/52 |
| socks5://47.87.97.94:1080 | TH | 1473 | 9 | 12/13 |
| http://205.237.105.49:3129 | FR | 708 | 8 | 8/8 |
| http://198.244.254.77:3128 | GB | 4140 | 8 | 19/21 |
| http://176.111.37.5:39811 | HK | 4018 | 8 | 118/137 |
| http://34.43.46.91:443 | US | 4376 | 8 | 128/137 |
| http://45.125.64.215:443 | HK | 1129 | 7 | 7/7 |
| http://140.238.32.108:3128 | JP | 863 | 7 | 70/136 |
| http://34.43.46.91:80 | US | 5373 | 7 | 131/137 |
| socks5://47.238.126.208:1080 | HK | 1220 | 7 | 25/42 |
| socks5://101.36.104.239:10808 | JP | 1789 | 7 | 116/137 |
| http://221.221.157.102:8888 | CN | 2356 | 6 | 38/89 |
| http://45.245.208.180:8080 | EG | 3214 | 6 | 9/10 |
| http://152.67.191.232:6800 | IN | 1204 | 6 | 6/6 |
| socks5://80.65.211.149:8888 | FR | 3677 | 6 | 9/16 |
| socks5://43.245.199.34:1080 | HK | 1218 | 6 | 6/6 |
| http://221.221.159.97:8888 | CN | 2328 | 5 | 43/90 |
| http://221.221.163.25:8888 | CN | 1450 | 5 | 35/91 |
| http://177.234.221.197:999 | EC | 6033 | 5 | 22/42 |
| http://177.234.221.201:999 | EC | 3921 | 5 | 15/40 |
| http://41.196.16.226:1976 | EG | 1014 | 5 | 5/5 |
| http://4.144.146.21:80 | SG | 1034 | 5 | 22/29 |
| http://146.190.80.158:9090 | SG | 2528 | 5 | 46/63 |
| http://200.59.191.27:999 | VE | 5828 | 5 | 88/132 |
| socks5://62.83.34.101:1080 | AT | 1028 | 5 | 5/5 |
| socks5://52.128.241.106:1080 | US | 383 | 5 | 10/19 |
| socks5://113.22.224.63:1083 | VN | 6874 | 5 | 5/5 |
| http://168.227.239.66:10000 | BR | 908 | 4 | 4/4 |
| http://190.0.246.210:4040 | CO | 765 | 4 | 123/136 |
| http://34.105.252.3:3128 | GB | 615 | 4 | 12/19 |
| http://43.155.62.157:443 | HK | 5106 | 4 | 32/40 |
| http://103.208.102.1:8080 | ID | 7975 | 4 | 24/130 |
| http://187.251.224.167:8081 | MX | 5756 | 4 | 25/97 |
| http://43.156.55.191:5001 | SG | 1292 | 4 | 4/4 |
| http://104.248.151.93:9090 | SG | 1070 | 4 | 31/38 |
| http://154.59.56.72:999 | VE | 6407 | 4 | 69/96 |
| http://103.82.20.76:8080 | VN | 3451 | 4 | 39/135 |
| socks4://143.198.239.45:10000 | US | 4184 | 4 | 15/27 |
| socks5://148.251.68.232:8888 | DE | 1902 | 4 | 11/16 |
| socks5://31.129.107.119:443 | RU | 1975 | 4 | 12/16 |
| http://187.102.219.32:999 | AR | 2276 | 3 | 42/136 |
| http://118.179.45.194:81 | BD | 6701 | 3 | 18/79 |
| http://102.244.78.61:8081 | CM | 1321 | 3 | 16/23 |
| http://102.244.78.61:8085 | CM | 1325 | 3 | 18/27 |
| http://102.244.78.61:8090 | CM | 1338 | 3 | 19/29 |
| http://121.46.226.221:10808 | CN | 4294 | 3 | 12/14 |
| http://123.121.75.126:8888 | CN | 1384 | 3 | 6/8 |
| http://123.121.134.192:8888 | CN | 7797 | 3 | 3/3 |
| http://45.65.137.218:999 | CO | 4335 | 3 | 35/102 |
| http://103.119.19.218:3128 | CZ | 1241 | 3 | 38/50 |
| http://38.50.165.123:999 | DO | 2173 | 3 | 33/122 |
| http://41.65.55.27:1976 | EG | 5234 | 3 | 30/119 |
| http://41.128.77.76:1981 | EG | 1578 | 3 | 37/91 |
| http://45.245.208.182:8080 | EG | 1129 | 3 | 16/26 |
| http://47.242.218.151:9009 | HK | 3750 | 3 | 3/3 |
| http://103.26.176.25:8080 | ID | 1442 | 3 | 13/61 |
| http://103.80.88.77:8080 | ID | 3518 | 3 | 7/50 |
| http://103.125.116.126:8080 | ID | 6837 | 3 | 19/102 |
| http://103.180.118.122:1080 | ID | 6229 | 3 | 3/3 |
| http://139.255.94.123:39635 | ID | 5398 | 3 | 5/47 |
| http://202.136.82.219:8080 | ID | 1670 | 3 | 41/135 |
| http://111.92.88.27:3128 | IN | 7134 | 3 | 20/106 |
| http://31.192.248.55:8080 | KG | 2543 | 3 | 29/105 |
| http://103.25.220.42:8084 | PH | 2943 | 3 | 9/62 |
| http://161.49.90.70:1337 | PH | 5876 | 3 | 12/75 |
| http://95.81.107.187:3128 | SE | 1597 | 3 | 3/3 |
| http://129.226.89.151:80 | SG | 1036 | 3 | 53/84 |
| http://152.42.177.32:8888 | SG | 1063 | 3 | 60/97 |
| http://212.175.50.76:8085 | TR | 2210 | 3 | 10/56 |
| http://195.226.213.251:8888 | UA | 5848 | 3 | 46/131 |
| http://44.216.83.206:3128 | US | 198 | 3 | 7/10 |
| http://38.51.207.117:999 | VE | 5663 | 3 | 31/114 |
| http://185.226.194.226:999 | VE | 647 | 3 | 10/33 |
| socks5://103.189.218.76:6969 | BD | 2103 | 3 | 44/135 |
| socks5://93.99.104.47:1080 | CZ | 881 | 3 | 3/3 |
