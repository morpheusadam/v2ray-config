# Proxy status

Generated 2026-10-27T18:54:10Z by `harvest.py`.

- **1771** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4326** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39680** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 140/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2271 |
| http | 2049 |
| socks4 | 6 |

| country | entries |
|---|---|
| NL | 2046 |
| ID | 616 |
| ?? | 162 |
| US | 97 |
| CO | 94 |
| PH | 88 |
| MX | 83 |
| RU | 82 |
| CN | 65 |
| BD | 64 |
| BR | 62 |
| TH | 62 |
| VE | 55 |
| EC | 54 |
| VN | 47 |
| IN | 45 |
| AR | 38 |
| SG | 35 |
| DO | 33 |
| JP | 29 |
| DE | 28 |
| TR | 28 |
| PK | 26 |
| EG | 23 |
| CA | 20 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-10-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 109 | 109 | 52 | 2026-10-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 118 | 118 | 61 | 2026-10-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 128 | 128 | 13 | 2026-10-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 86 | 2026-10-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 157 | 157 | 46 | 2026-10-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-10-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 343 | 343 | 132 | 2026-10-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 346 | 346 | 131 | 2026-10-27 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 579 | 579 | 335 | 2026-10-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-10-27 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1292 | 1292 | 78 | 2026-10-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1120 | 2026-10-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1722 | 1722 | 211 | 2026-10-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1592 | 2026-10-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2228 | 2228 | 707 | 2026-10-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2657 | 2657 | 1765 | 2026-10-27 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 79665 | 79665 | 65820 | 2026-10-27 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 86829 | 86828 | 3061 | 2026-10-27 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1090 | 75 | 142/155 |
| http://149.130.173.58:9443 | CO | 498 | 66 | 66/66 |
| http://190.0.246.213:4040 | CO | 625 | 49 | 112/120 |
| http://103.237.102.191:11111 | DE | 999 | 42 | 148/155 |
| http://45.186.6.104:3128 | EC | 803 | 36 | 126/133 |
| http://103.133.26.72:8080 | ID | 1252 | 31 | 36/81 |
| http://103.133.26.73:3128 | ID | 1399 | 31 | 51/133 |
| http://103.133.26.119:8080 | ID | 1729 | 31 | 35/65 |
| http://176.111.37.5:39811 | HK | 896 | 26 | 136/155 |
| http://34.43.46.91:80 | US | 1522 | 25 | 149/155 |
| socks5://43.245.199.34:1080 | HK | 1191 | 24 | 24/24 |
| http://4.144.146.21:80 | SG | 991 | 23 | 40/47 |
| http://190.0.246.210:4040 | CO | 861 | 22 | 141/154 |
| http://43.155.62.157:443 | HK | 6405 | 22 | 50/58 |
| http://102.244.78.61:8081 | CM | 1337 | 21 | 34/41 |
| http://186.5.94.206:999 | EC | 1103 | 20 | 108/117 |
| http://184.75.221.82:3118 | CA | 3415 | 19 | 106/120 |
| http://189.51.168.165:999 | MX | 490 | 19 | 62/67 |
| http://176.111.37.216:39811 | HK | 1053 | 18 | 127/155 |
| http://103.130.61.61:8081 | ID | 5610 | 17 | 125/155 |
| http://185.191.239.248:3128 | CH | 3433 | 15 | 111/154 |
| http://103.133.26.50:8080 | ID | 1322 | 15 | 34/56 |
| socks5://129.146.121.2:10808 | US | 441 | 12 | 12/12 |
| http://103.130.61.60:8081 | ID | 3104 | 11 | 11/11 |
| http://123.121.132.234:8888 | CN | 1331 | 10 | 14/16 |
| http://146.190.80.158:9090 | SG | 1006 | 10 | 59/81 |
| socks5://67.207.92.87:1088 | US | 542 | 10 | 96/154 |
| socks5://69.55.49.177:38182 | US | 455 | 10 | 10/10 |
| socks5://101.36.104.46:10808 | JP | 3489 | 9 | 134/155 |
| http://15.229.149.81:3128 | BR | 2439 | 8 | 36/65 |
| http://89.167.124.218:8888 | DE | 1383 | 8 | 8/8 |
| http://45.65.224.74:999 | AR | 1701 | 7 | 15/20 |
| http://102.244.78.61:8080 | CM | 1328 | 7 | 36/44 |
| http://102.244.78.61:8082 | CM | 1334 | 7 | 36/44 |
| http://102.244.78.61:8083 | CM | 1293 | 7 | 36/43 |
| http://102.244.78.61:8084 | CM | 1331 | 7 | 34/43 |
| http://102.244.78.61:8085 | CM | 1388 | 7 | 34/45 |
| http://102.244.78.61:8086 | CM | 1316 | 7 | 35/43 |
| http://102.244.78.61:8087 | CM | 1381 | 7 | 33/45 |
| http://102.244.78.61:8088 | CM | 1354 | 7 | 35/43 |
| http://102.244.78.61:8089 | CM | 1359 | 7 | 34/43 |
| http://103.119.19.218:3128 | CZ | 787 | 7 | 55/68 |
| http://43.202.114.177:7428 | KR | 3740 | 6 | 29/69 |
| http://187.102.219.42:999 | AR | 1482 | 5 | 84/150 |
| http://51.85.44.162:8089 | IL | 1805 | 5 | 5/5 |
| http://159.223.41.216:9090 | SG | 956 | 5 | 82/115 |
| http://49.229.100.235:8080 | TH | 1339 | 5 | 67/103 |
| http://61.91.162.126:8080 | TH | 1345 | 5 | 74/98 |
| http://103.10.231.189:8080 | TH | 1689 | 5 | 101/140 |
| socks5://107.191.47.162:1081 | FR | 891 | 5 | 5/5 |
| socks5://47.238.126.208:1080 | HK | 1059 | 5 | 31/60 |
| socks5://51.15.20.32:1088 | NL | 800 | 5 | 16/19 |
| socks5://47.251.127.154:1080 | US | 6789 | 5 | 33/108 |
| socks5://166.1.90.114:1090 | US | 366 | 5 | 11/14 |
| http://179.43.10.233:8874 | BR | 4135 | 4 | 23/147 |
| http://45.161.112.227:999 | CL | 5128 | 4 | 42/148 |
| http://122.246.3.12:17981 | CN | 6822 | 4 | 68/149 |
| http://45.65.137.218:999 | CO | 2858 | 4 | 48/120 |
| http://179.1.221.26:3128 | CO | 795 | 4 | 32/95 |
| http://45.71.186.211:999 | EC | 2465 | 4 | 47/108 |
| http://177.234.217.235:999 | EC | 6184 | 4 | 57/124 |
| http://190.12.150.244:999 | EC | 1660 | 4 | 109/151 |
| http://36.50.56.105:8818 | ID | 6945 | 4 | 25/151 |
| http://36.64.193.226:8080 | ID | 5854 | 4 | 26/150 |
| http://103.144.54.71:8082 | ID | 1571 | 4 | 33/91 |
| http://46.209.30.11:8080 | IR | 1926 | 4 | 16/18 |
| http://116.80.65.235:3128 | JP | 1709 | 4 | 4/4 |
| http://51.15.20.32:3129 | NL | 5860 | 4 | 15/19 |
| http://128.199.116.219:9090 | SG | 964 | 4 | 58/74 |
| http://195.226.213.251:8888 | UA | 3134 | 4 | 56/149 |
| http://34.43.46.91:443 | US | 536 | 4 | 144/155 |
| http://34.207.102.197:5512 | US | 2018 | 4 | 11/55 |
| http://152.70.198.2:1080 | US | 810 | 4 | 25/75 |
| http://195.158.8.123:3128 | UZ | 3226 | 4 | 103/153 |
| http://82.86.112.48:999 | VE | 7104 | 4 | 35/145 |
| http://45.65.226.169:999 | AR | 3337 | 3 | 12/17 |
| http://123.200.8.170:10000 | BD | 6540 | 3 | 63/153 |
| http://111.192.30.229:8888 | CN | 1680 | 3 | 5/7 |
| http://111.192.31.170:8888 | CN | 2685 | 3 | 8/28 |
| http://123.121.123.115:8888 | CN | 1317 | 3 | 46/79 |
| http://123.121.134.141:8888 | CN | 1415 | 3 | 10/16 |
| http://123.121.140.72:8888 | CN | 2347 | 3 | 6/7 |
| http://190.7.138.78:8080 | CO | 7350 | 3 | 39/84 |
| http://177.234.221.197:999 | EC | 3272 | 3 | 29/60 |
| http://34.88.38.81:9443 | FI | 1002 | 3 | 82/120 |
| http://35.228.49.168:9443 | FI | 861 | 3 | 63/92 |
| http://198.244.254.77:3128 | GB | 4183 | 3 | 35/39 |
| http://18.166.56.240:39593 | HK | 3730 | 3 | 26/77 |
| http://103.146.38.107:1111 | ID | 4125 | 3 | 20/89 |
| http://103.194.47.53:8082 | ID | 5991 | 3 | 34/124 |
| http://160.22.198.17:8082 | ID | 5394 | 3 | 35/147 |
| http://140.238.32.108:3128 | JP | 691 | 3 | 82/154 |
| http://200.94.38.45:2604 | MX | 4518 | 3 | 21/44 |
| http://185.238.238.21:58080 | PL | 1556 | 3 | 36/119 |
| http://217.142.24.106:8085 | SY | 6874 | 3 | 5/10 |
| http://47.254.36.25:11080 | US | 7699 | 3 | 41/97 |
| http://158.101.23.103:40002 | US | 4093 | 3 | 3/3 |
| http://154.59.56.72:999 | VE | 3854 | 3 | 82/114 |
| http://16.28.32.67:48907 | ZA | 3625 | 3 | 21/67 |
| socks5://148.251.68.232:8888 | DE | 2025 | 3 | 18/34 |
