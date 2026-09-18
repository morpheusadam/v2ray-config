# Proxy status

Generated 2026-09-18T17:06:54Z by `harvest.py`.

- **1764** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3176** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **26603** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 185/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1604 |
| socks5 | 1571 |
| socks4 | 1 |

| country | entries |
|---|---|
| NL | 1348 |
| ID | 355 |
| CN | 122 |
| US | 120 |
| RU | 94 |
| MX | 68 |
| PH | 66 |
| ?? | 60 |
| DE | 58 |
| BD | 56 |
| SG | 53 |
| VE | 51 |
| CO | 50 |
| IN | 48 |
| BR | 35 |
| EG | 34 |
| VN | 34 |
| EC | 33 |
| FR | 32 |
| JP | 31 |
| TH | 29 |
| HK | 28 |
| DO | 22 |
| FI | 20 |
| TR | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-09-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 54 | 54 | 25 | 2026-09-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 67 | 67 | 31 | 2026-09-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-09-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 119 | 119 | 34 | 2026-09-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 88 | 2026-09-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 215 | 215 | 93 | 2026-09-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 224 | 224 | 87 | 2026-09-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 268 | 268 | 117 | 2026-09-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-09-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 756 | 756 | 156 | 2026-09-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-09-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1604 | 2026-09-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1941 | 1937 | 389 | 2026-09-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2444 | 2442 | 711 | 2026-09-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2453 | 2451 | 1813 | 2026-09-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2504 | 2502 | 572 | 2026-09-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 11601 | 11601 | 7169 | 2026-09-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 15121 | 15121 | 2225 | 2026-09-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 518 | 70 | 75/78 |
| http://34.43.46.91:80 | US | 586 | 70 | 75/78 |
| http://95.211.174.135:3128 | NL | 1269 | 64 | 77/78 |
| http://185.200.188.234:10001 | RU | 3405 | 64 | 77/78 |
| http://130.110.103.245:3128 | SA | 1425 | 64 | 76/78 |
| http://1.231.81.166:3128 | KR | 1385 | 43 | 75/78 |
| http://190.97.236.128:999 | VE | 1749 | 35 | 66/68 |
| http://190.97.236.129:999 | VE | 811 | 35 | 66/68 |
| http://95.3.69.222:8080 | TR | 1408 | 33 | 75/78 |
| http://107.167.18.122:443 | US | 1382 | 23 | 29/30 |
| socks5://83.147.216.208:1080 | FI | 954 | 22 | 28/46 |
| http://184.75.221.82:3118 | CA | 238 | 19 | 40/43 |
| http://91.134.141.4:3128 | FR | 502 | 17 | 37/39 |
| http://186.5.94.206:999 | EC | 811 | 15 | 38/40 |
| socks5://107.150.41.226:18080 | US | 551 | 15 | 15/15 |
| http://190.0.246.210:4040 | CO | 1860 | 11 | 68/77 |
| http://186.33.45.219:999 | EC | 1873 | 11 | 41/67 |
| http://38.51.207.104:8080 | VE | 2663 | 11 | 18/19 |
| socks5://103.162.30.189:10808 | VN | 2185 | 10 | 12/13 |
| http://34.88.38.81:9443 | FI | 606 | 9 | 30/43 |
| http://35.228.49.168:9443 | FI | 644 | 9 | 11/15 |
| http://197.224.185.3:3128 | MU | 1036 | 9 | 42/46 |
| http://189.51.168.164:999 | MX | 361 | 9 | 42/43 |
| http://45.132.252.25:49156 | RU | 791 | 9 | 9/9 |
| http://5.129.254.5:8888 | RU | 1323 | 8 | 31/33 |
| http://5.129.254.49:8888 | RU | 1027 | 8 | 32/33 |
| http://5.129.254.51:8888 | RU | 1004 | 8 | 32/33 |
| http://5.129.254.60:8888 | RU | 1006 | 8 | 31/32 |
| http://5.129.254.70:8888 | RU | 1165 | 8 | 32/33 |
| http://5.129.254.129:8888 | RU | 2366 | 8 | 37/39 |
| http://5.129.254.154:8888 | RU | 1016 | 8 | 28/29 |
| http://193.104.179.115:3128 | UZ | 1112 | 8 | 26/43 |
| socks5://57.128.231.218:1004 | PL | 827 | 8 | 9/12 |
| http://120.232.115.170:17981 | CN | 2091 | 7 | 56/77 |
| http://190.0.246.211:4040 | CO | 2403 | 7 | 66/78 |
| http://190.0.246.213:4040 | CO | 1232 | 7 | 36/43 |
| http://213.111.146.36:18080 | NL | 631 | 7 | 10/15 |
| http://157.85.108.47:3128 | TH | 1357 | 7 | 35/46 |
| socks5://101.36.104.46:10808 | JP | 2106 | 7 | 69/78 |
| socks5://144.24.47.42:1080 | US | 3471 | 7 | 42/74 |
| socks5://193.25.215.182:22222 | US | 1043 | 7 | 72/78 |
| http://221.221.159.97:8888 | CN | 3176 | 6 | 13/31 |
| http://167.172.76.176:9090 | SG | 1167 | 6 | 21/39 |
| socks5://135.125.232.151:1080 | DE | 710 | 6 | 8/9 |
| socks5://121.169.46.116:1090 | KR | 6297 | 6 | 51/78 |
| socks5://43.135.176.121:1080 | US | 815 | 6 | 29/33 |
| http://39.106.170.168:8080 | CN | 2045 | 5 | 39/76 |
| http://45.186.6.104:3128 | EC | 644 | 5 | 54/56 |
| http://186.33.45.220:999 | EC | 2715 | 5 | 23/47 |
| http://117.236.124.166:3128 | IN | 1654 | 5 | 52/78 |
| http://194.31.108.109:2080 | IR | 6374 | 5 | 24/38 |
| http://77.73.68.222:65000 | RU | 787 | 5 | 5/5 |
| http://124.156.194.52:8080 | SG | 2033 | 5 | 8/11 |
| http://61.91.162.126:8080 | TH | 1904 | 5 | 18/21 |
| http://103.10.231.189:8080 | TH | 1860 | 5 | 43/63 |
| http://153.51.201.35:999 | VE | 689 | 5 | 5/5 |
| http://154.3.76.14:999 | VE | 6158 | 5 | 22/31 |
| http://210.211.113.33:80 | VN | 7986 | 5 | 27/48 |
| http://210.211.113.35:80 | VN | 2092 | 5 | 26/50 |
| socks5://62.113.112.246:10808 | RU | 3561 | 5 | 5/5 |
| socks5://135.148.120.20:1080 | US | 692 | 5 | 5/5 |
| http://187.102.219.42:999 | AR | 1248 | 4 | 38/73 |
| http://8.138.217.152:21001 | CN | 5290 | 4 | 53/78 |
| http://36.155.23.163:10808 | CN | 5016 | 4 | 9/15 |
| http://114.252.12.211:8888 | CN | 2267 | 4 | 17/43 |
| http://123.119.25.143:8888 | CN | 5541 | 4 | 13/43 |
| http://123.121.123.216:8888 | CN | 1806 | 4 | 13/38 |
| http://222.128.172.158:8888 | CN | 1533 | 4 | 16/43 |
| http://152.53.183.107:8081 | DE | 5523 | 4 | 20/31 |
| http://190.12.150.244:999 | EC | 4026 | 4 | 48/74 |
| http://65.109.217.164:3128 | FI | 2689 | 4 | 10/11 |
| http://37.187.109.70:10111 | FR | 3835 | 4 | 31/78 |
| http://176.111.37.216:39811 | HK | 1921 | 4 | 64/78 |
| http://38.194.246.34:999 | MX | 3786 | 4 | 41/69 |
| http://206.135.56.50:8080 | MX | 1895 | 4 | 13/37 |
| http://43.156.153.104:8081 | SG | 2607 | 4 | 4/4 |
| http://152.42.177.32:8888 | SG | 1181 | 4 | 20/38 |
| http://47.81.56.193:8888 | TH | 1652 | 4 | 46/78 |
| http://201.71.2.24:999 | VE | 2009 | 4 | 23/66 |
| http://201.71.2.25:999 | VE | 6161 | 4 | 19/65 |
| http://201.71.2.27:999 | VE | 2121 | 4 | 25/76 |
| http://210.211.113.36:80 | VN | 3300 | 4 | 29/49 |
| socks4://57.128.231.218:1000 | PL | 921 | 4 | 5/13 |
| socks5://31.211.142.115:8192 | BG | 963 | 4 | 20/76 |
| socks5://45.74.31.40:14787 | NL | 2243 | 4 | 5/6 |
| socks5://45.74.31.40:16847 | NL | 7894 | 4 | 4/4 |
| socks5://45.74.31.42:17062 | NL | 3733 | 4 | 4/4 |
| socks5://161.35.90.93:1083 | NL | 1472 | 4 | 41/76 |
| http://45.70.52.248:8080 | BR | 3043 | 3 | 5/18 |
| http://1.15.53.214:8888 | CN | 1884 | 3 | 17/72 |
| http://47.95.206.224:45003 | CN | 3022 | 3 | 5/29 |
| http://47.107.82.96:30051 | CN | 3559 | 3 | 41/71 |
| http://61.149.135.125:8888 | CN | 3480 | 3 | 18/38 |
| http://114.236.137.41:21000 | CN | 1936 | 3 | 54/78 |
| http://114.252.13.224:8888 | CN | 1478 | 3 | 15/42 |
| http://123.115.177.103:8888 | CN | 6911 | 3 | 3/3 |
| http://123.119.179.101:8888 | CN | 5805 | 3 | 15/36 |
| http://123.119.179.161:8888 | CN | 2204 | 3 | 18/43 |
| http://123.121.121.123:8888 | CN | 2646 | 3 | 27/43 |
| http://123.121.209.61:8888 | CN | 1483 | 3 | 11/43 |
