# Proxy status

Generated 2026-10-17T21:43:11Z by `harvest.py`.

- **1062** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3234** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 113/600 (19%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1706 |
| http | 1519 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1467 |
| ID | 438 |
| ?? | 103 |
| RU | 84 |
| US | 79 |
| MX | 67 |
| CO | 64 |
| BD | 61 |
| PH | 61 |
| CN | 58 |
| VE | 49 |
| IN | 45 |
| EC | 37 |
| DE | 36 |
| VN | 35 |
| SG | 31 |
| BR | 30 |
| AR | 29 |
| TR | 29 |
| DO | 28 |
| TH | 26 |
| KH | 25 |
| EG | 23 |
| PK | 22 |
| HK | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-10-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 83 | 83 | 16 | 2026-10-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 124 | 124 | 50 | 2026-10-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 67 | 2026-10-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 208 | 208 | 96 | 2026-10-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 247 | 247 | 32 | 2026-10-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 304 | 304 | 114 | 2026-10-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 313 | 313 | 92 | 2026-10-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-10-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 947 | 947 | 658 | 2026-10-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1603 | 1601 | 288 | 2026-10-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1137 | 2026-10-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1601 | 2026-10-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1959 | 1958 | 746 | 2026-10-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2341 | 2339 | 1637 | 2026-10-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3131 | 3130 | 1472 | 2026-10-17 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 67593 | 67593 | 53548 | 2026-10-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 73314 | 73313 | 2051 | 2026-10-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1745 | 56 | 123/136 |
| http://149.130.173.58:9443 | CO | 679 | 47 | 47/47 |
| http://190.0.246.213:4040 | CO | 783 | 30 | 93/101 |
| http://197.224.185.3:3128 | MU | 2059 | 28 | 97/104 |
| http://103.237.102.191:11111 | DE | 1430 | 23 | 129/136 |
| http://203.252.142.217:80 | KR | 1319 | 18 | 18/18 |
| http://45.186.6.104:3128 | EC | 959 | 17 | 107/114 |
| http://3.211.120.181:443 | US | 392 | 16 | 30/47 |
| http://165.154.162.73:8888 | US | 1055 | 16 | 89/136 |
| http://103.130.61.61:8081 | ID | 3751 | 15 | 107/136 |
| http://5.129.254.5:8888 | RU | 1435 | 13 | 80/91 |
| http://5.129.254.49:8888 | RU | 2117 | 13 | 81/91 |
| http://5.129.254.51:8888 | RU | 1515 | 13 | 81/91 |
| http://5.129.254.60:8888 | RU | 2982 | 13 | 80/90 |
| http://5.129.254.70:8888 | RU | 1578 | 13 | 81/91 |
| http://5.129.254.129:8888 | RU | 3795 | 13 | 86/97 |
| http://5.129.254.154:8888 | RU | 3689 | 13 | 77/87 |
| http://5.129.254.215:8888 | RU | 1542 | 13 | 30/33 |
| http://5.129.254.243:8888 | RU | 7150 | 13 | 30/32 |
| http://103.133.26.50:8080 | ID | 1182 | 12 | 16/37 |
| http://103.133.26.72:8080 | ID | 1672 | 12 | 17/62 |
| http://103.133.26.73:3128 | ID | 1229 | 12 | 32/114 |
| http://103.133.26.119:8080 | ID | 1631 | 12 | 16/46 |
| socks5://67.207.92.87:1088 | US | 1378 | 12 | 80/135 |
| http://147.45.164.178:8888 | RU | 3653 | 10 | 10/10 |
| http://128.199.121.61:9090 | SG | 1085 | 8 | 46/56 |
| socks5://171.25.158.95:1080 | SE | 2377 | 8 | 43/51 |
| socks5://47.87.97.94:1080 | TH | 1244 | 8 | 11/12 |
| http://205.237.105.49:3129 | FR | 1025 | 7 | 7/7 |
| http://198.244.254.77:3128 | GB | 5128 | 7 | 18/20 |
| http://176.111.37.5:39811 | HK | 1334 | 7 | 117/136 |
| http://34.43.46.91:443 | US | 1651 | 7 | 127/136 |
| http://45.125.64.215:443 | HK | 1033 | 6 | 6/6 |
| http://176.111.37.216:39811 | HK | 1457 | 6 | 109/136 |
| http://140.238.32.108:3128 | JP | 1021 | 6 | 69/135 |
| http://34.43.46.91:80 | US | 758 | 6 | 130/136 |
| socks5://47.238.126.208:1080 | HK | 990 | 6 | 24/41 |
| socks5://101.36.104.239:10808 | JP | 2282 | 6 | 115/136 |
| http://221.221.157.102:8888 | CN | 7553 | 5 | 37/88 |
| http://181.78.194.249:999 | EC | 6866 | 5 | 43/119 |
| http://45.245.208.180:8080 | EG | 1512 | 5 | 8/9 |
| http://80.65.211.149:8888 | FR | 1417 | 5 | 8/15 |
| http://152.67.191.232:6800 | IN | 1056 | 5 | 5/5 |
| http://49.229.100.235:8080 | TH | 1193 | 5 | 53/84 |
| http://61.91.162.126:8080 | TH | 1583 | 5 | 62/79 |
| http://103.10.231.189:8080 | TH | 1607 | 5 | 88/121 |
| socks5://94.183.170.105:1080 | EE | 1345 | 5 | 5/5 |
| socks5://43.245.199.34:1080 | HK | 1010 | 5 | 5/5 |
| http://221.221.159.97:8888 | CN | 7095 | 4 | 42/89 |
| http://221.221.163.25:8888 | CN | 2158 | 4 | 34/90 |
| http://177.234.221.197:999 | EC | 5072 | 4 | 21/41 |
| http://177.234.221.201:999 | EC | 4841 | 4 | 14/39 |
| http://41.196.16.226:1976 | EG | 1599 | 4 | 4/4 |
| http://206.135.47.110:999 | MX | 2275 | 4 | 6/7 |
| http://4.144.146.21:80 | SG | 858 | 4 | 21/28 |
| http://146.190.80.158:9090 | SG | 855 | 4 | 45/62 |
| http://167.172.76.176:9090 | SG | 852 | 4 | 67/97 |
| http://200.59.191.27:999 | VE | 2163 | 4 | 87/131 |
| socks5://62.83.34.101:1080 | AT | 1242 | 4 | 4/4 |
| socks5://103.239.201.50:58765 | PH | 2552 | 4 | 37/121 |
| socks5://52.128.241.106:1080 | US | 347 | 4 | 9/18 |
| socks5://113.22.224.63:1083 | VN | 1648 | 4 | 4/4 |
| http://168.227.239.66:10000 | BR | 1298 | 3 | 3/3 |
| http://120.232.115.170:17981 | CN | 1646 | 3 | 96/135 |
| http://24.152.58.124:999 | CO | 4844 | 3 | 6/17 |
| http://190.0.246.210:4040 | CO | 861 | 3 | 122/135 |
| http://200.10.31.42:8081 | CO | 2427 | 3 | 5/9 |
| http://177.234.221.200:999 | EC | 5568 | 3 | 20/40 |
| http://41.128.90.54:1981 | EG | 4065 | 3 | 7/17 |
| http://34.105.252.3:3128 | GB | 1056 | 3 | 11/18 |
| http://43.155.62.157:443 | HK | 2737 | 3 | 31/39 |
| http://159.138.24.221:3128 | HK | 1212 | 3 | 3/3 |
| http://103.3.59.251:8080 | ID | 7607 | 3 | 15/102 |
| http://103.122.0.52:8181 | ID | 6831 | 3 | 12/48 |
| http://103.208.102.1:8080 | ID | 6257 | 3 | 23/129 |
| http://160.19.18.165:8181 | ID | 5844 | 3 | 19/36 |
| http://45.5.94.243:999 | MX | 4958 | 3 | 6/10 |
| http://187.251.224.167:8081 | MX | 2453 | 3 | 24/96 |
| http://122.54.139.32:5050 | PH | 6312 | 3 | 6/10 |
| http://43.156.55.191:5001 | SG | 854 | 3 | 3/3 |
| http://104.248.151.93:9090 | SG | 858 | 3 | 30/37 |
| http://159.223.41.216:9090 | SG | 883 | 3 | 69/96 |
| http://47.254.36.25:11080 | US | 2773 | 3 | 31/78 |
| http://38.172.181.0:999 | VE | 4333 | 3 | 20/43 |
| http://154.59.56.72:999 | VE | 2425 | 3 | 68/95 |
| http://103.82.20.76:8080 | VN | 4664 | 3 | 38/134 |
| socks4://143.198.239.45:10000 | US | 1582 | 3 | 14/26 |
| socks5://148.251.68.232:8888 | DE | 1956 | 3 | 10/15 |
| socks5://45.149.92.160:1080 | HK | 1059 | 3 | 3/3 |
| socks5://45.194.33.12:30001 | HK | 1085 | 3 | 5/12 |
| socks5://103.163.244.106:1080 | IN | 6091 | 3 | 24/132 |
| socks5://31.129.107.119:443 | RU | 3353 | 3 | 11/15 |
| socks5://77.82.83.181:1080 | RU | 2605 | 3 | 3/3 |
| socks5://64.176.221.15:1080 | US | 1499 | 3 | 3/3 |
| http://88.218.92.64:3128 | AM | 6554 | 2 | 5/24 |
| http://45.172.142.38:999 | AR | 7795 | 2 | 14/84 |
| http://187.102.219.32:999 | AR | 3105 | 2 | 41/135 |
| http://187.102.219.42:999 | AR | 2385 | 2 | 71/131 |
| http://103.133.201.243:8080 | BD | 4322 | 2 | 8/17 |
| http://103.150.49.90:8090 | BD | 7300 | 2 | 25/129 |
