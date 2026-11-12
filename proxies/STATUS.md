# Proxy status

Generated 2026-11-12T01:40:06Z by `harvest.py`.

- **2269** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4830** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35378** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 128/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3095 |
| socks5 | 1724 |
| socks4 | 11 |

| country | entries |
|---|---|
| NL | 1553 |
| ID | 887 |
| ?? | 339 |
| PH | 156 |
| MX | 135 |
| US | 134 |
| CO | 115 |
| CN | 99 |
| TH | 98 |
| TR | 84 |
| VE | 79 |
| BR | 78 |
| BD | 73 |
| IN | 67 |
| EC | 62 |
| AR | 58 |
| RU | 51 |
| DO | 49 |
| PE | 42 |
| PK | 40 |
| VN | 40 |
| EG | 37 |
| SG | 33 |
| JP | 32 |
| DE | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-11-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 77 | 77 | 10 | 2026-11-12 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 39 | 2026-11-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 61 | 2026-11-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 236 | 236 | 31 | 2026-11-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 292 | 292 | 131 | 2026-11-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 297 | 297 | 81 | 2026-11-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 329 | 329 | 220 | 2026-11-12 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 442 | 2026-11-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 790 | 790 | 104 | 2026-11-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-11-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-12 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1932 | 1932 | 157 | 2026-11-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2283 | 2283 | 233 | 2026-11-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2628 | 2628 | 620 | 2026-11-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2808 | 2808 | 1712 | 2026-11-12 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5246 | 5246 | 3998 | 2026-11-12 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11399 | 11399 | 1824 | 2026-11-12 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1462 | 62 | 82/164 |
| http://176.111.37.5:39811 | HK | 1172 | 57 | 167/186 |
| http://34.43.46.91:80 | US | 1017 | 56 | 180/186 |
| http://4.144.146.21:80 | SG | 908 | 54 | 71/78 |
| http://176.111.37.216:39811 | HK | 1321 | 49 | 158/186 |
| http://34.43.46.91:443 | US | 1797 | 35 | 175/186 |
| http://130.110.103.245:3128 | SA | 2155 | 32 | 168/186 |
| http://103.133.26.72:8080 | ID | 1314 | 29 | 66/112 |
| http://45.189.57.114:3129 | EC | 2100 | 28 | 28/28 |
| http://103.133.26.119:8080 | ID | 1538 | 22 | 65/96 |
| http://189.51.168.164:999 | MX | 4496 | 22 | 22/22 |
| http://49.229.100.235:8080 | TH | 1280 | 22 | 94/134 |
| http://171.100.254.137:8080 | TH | 2573 | 22 | 22/22 |
| http://43.161.254.16:3128 | HK | 4388 | 21 | 23/26 |
| http://103.130.61.61:8081 | ID | 5871 | 21 | 155/186 |
| http://184.75.221.82:3118 | CA | 886 | 20 | 133/151 |
| http://102.244.78.61:8089 | CM | 1542 | 17 | 61/74 |
| http://45.186.6.104:3128 | EC | 1004 | 16 | 155/164 |
| http://38.180.18.103:3128 | BE | 1044 | 15 | 15/15 |
| http://190.71.72.85:2525 | CO | 912 | 14 | 30/71 |
| http://102.244.78.61:8090 | CM | 1443 | 13 | 62/78 |
| socks5://121.46.226.221:10808 | CN | 4870 | 12 | 12/12 |
| http://177.234.217.44:999 | EC | 2986 | 10 | 33/86 |
| http://45.65.224.125:999 | AR | 2715 | 9 | 36/48 |
| http://103.237.102.191:11111 | DE | 1512 | 9 | 177/186 |
| http://43.155.62.157:443 | HK | 1726 | 9 | 76/89 |
| http://82.152.138.127:999 | MX | 2239 | 9 | 61/148 |
| http://45.245.208.180:8080 | EG | 1450 | 8 | 41/59 |
| http://144.124.251.24:10771 | NL | 796 | 8 | 75/118 |
| http://15.223.187.219:35507 | CA | 5247 | 7 | 25/99 |
| http://185.191.239.248:3128 | CH | 1292 | 7 | 135/185 |
| http://123.121.109.207:8888 | CN | 2433 | 7 | 7/7 |
| http://177.234.217.92:999 | EC | 3056 | 7 | 28/35 |
| http://206.135.47.107:999 | MX | 7139 | 7 | 34/56 |
| http://61.91.162.126:8080 | TH | 1236 | 7 | 98/129 |
| http://103.10.231.189:8080 | TH | 1635 | 7 | 125/171 |
| socks5://171.25.158.95:1080 | SE | 7017 | 7 | 80/101 |
| http://45.65.226.171:999 | AR | 3582 | 6 | 14/24 |
| http://27.147.155.206:12051 | BD | 1988 | 6 | 6/6 |
| http://160.22.45.114:8080 | ID | 3034 | 6 | 29/45 |
| http://43.128.144.133:18080 | KR | 2080 | 6 | 6/6 |
| socks5://37.18.73.60:5566 | RU | 1778 | 6 | 35/83 |
| http://15.229.149.81:3128 | BR | 2240 | 5 | 61/96 |
| http://123.115.226.82:8888 | CN | 7539 | 5 | 49/132 |
| http://221.221.162.6:8888 | CN | 1506 | 5 | 44/84 |
| http://64.204.90.17:999 | CO | 3245 | 5 | 5/5 |
| http://177.234.217.45:999 | EC | 5085 | 5 | 44/117 |
| http://177.234.217.46:999 | EC | 6513 | 5 | 50/133 |
| http://213.131.85.26:1976 | EG | 1529 | 5 | 13/17 |
| http://103.167.170.70:1111 | ID | 3735 | 5 | 38/184 |
| http://103.171.182.80:8080 | ID | 1998 | 5 | 6/8 |
| http://51.85.44.162:31819 | IL | 5783 | 5 | 23/38 |
| http://34.229.190.39:33893 | US | 783 | 5 | 33/127 |
| http://38.41.0.60:11201 | VE | 1454 | 5 | 42/112 |
| socks5://54.198.53.191:1080 | US | 6707 | 5 | 5/5 |
| http://45.65.224.74:999 | AR | 4436 | 4 | 42/51 |
| http://187.102.219.32:999 | AR | 1812 | 4 | 70/185 |
| http://111.192.48.62:8888 | CN | 1943 | 4 | 4/4 |
| http://114.248.179.223:8888 | CN | 2574 | 4 | 70/154 |
| http://123.121.140.72:8888 | CN | 2378 | 4 | 23/38 |
| http://177.234.217.83:999 | EC | 1831 | 4 | 24/33 |
| http://41.196.16.227:1981 | EG | 1321 | 4 | 4/4 |
| http://217.52.247.84:1976 | EG | 1486 | 4 | 4/4 |
| http://103.46.11.160:8080 | ID | 2734 | 4 | 19/60 |
| http://103.97.140.17:8080 | ID | 4418 | 4 | 14/27 |
| http://103.199.117.121:7777 | ID | 7137 | 4 | 11/20 |
| http://13.233.172.115:57644 | IN | 2975 | 4 | 4/4 |
| http://140.238.32.108:3128 | JP | 1364 | 4 | 106/185 |
| http://206.135.47.109:999 | MX | 3223 | 4 | 6/7 |
| http://144.124.251.24:10574 | NL | 915 | 4 | 78/135 |
| http://144.124.251.24:10605 | NL | 747 | 4 | 73/118 |
| http://144.124.251.24:11266 | NL | 789 | 4 | 75/118 |
| http://180.191.122.190:8181 | PH | 5634 | 4 | 6/17 |
| http://103.86.135.98:8080 | PK | 4524 | 4 | 18/60 |
| http://180.180.156.70:80 | TH | 4597 | 4 | 20/43 |
| socks5://45.74.31.46:5997 | NL | 5165 | 4 | 7/56 |
| socks5://46.246.12.13:1080 | SE | 4075 | 4 | 7/8 |
| socks5://193.218.118.128:1080 | UA | 3987 | 4 | 31/42 |
| socks5://209.50.255.91:1080 | US | 4887 | 4 | 46/103 |
| http://45.232.0.2:8080 | AR | 2634 | 3 | 60/184 |
| http://187.102.219.42:999 | AR | 7071 | 3 | 104/181 |
| http://16.51.5.77:16637 | AU | 2956 | 3 | 32/126 |
| http://103.204.211.48:32255 | BD | 5992 | 3 | 27/181 |
| http://111.196.24.150:8888 | CN | 3913 | 3 | 19/36 |
| http://111.196.30.74:8888 | CN | 2774 | 3 | 17/35 |
| http://123.119.25.143:8888 | CN | 2822 | 3 | 67/151 |
| http://123.119.179.161:8888 | CN | 1626 | 3 | 64/151 |
| http://123.121.122.125:8888 | CN | 2014 | 3 | 6/9 |
| http://123.121.122.142:8888 | CN | 2123 | 3 | 20/32 |
| http://221.221.154.253:8888 | CN | 1724 | 3 | 22/47 |
| http://45.167.125.62:999 | CO | 6898 | 3 | 28/185 |
| http://190.61.46.162:999 | CO | 5115 | 3 | 14/47 |
| http://41.128.77.76:1976 | EG | 4374 | 3 | 66/152 |
| http://41.128.90.52:1981 | EG | 1580 | 3 | 3/3 |
| http://43.99.60.244:8089 | HK | 811 | 3 | 70/136 |
| http://45.126.250.34:8080 | ID | 4949 | 3 | 7/18 |
| http://49.213.59.108:8082 | ID | 7112 | 3 | 32/87 |
| http://103.102.12.67:8080 | ID | 6322 | 3 | 14/41 |
| http://103.120.174.75:1818 | ID | 2249 | 3 | 39/170 |
| http://103.150.12.175:8080 | ID | 2978 | 3 | 11/23 |
