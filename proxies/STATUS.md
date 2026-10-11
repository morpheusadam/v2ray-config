# Proxy status

Generated 2026-10-11T23:08:11Z by `harvest.py`.

- **1388** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2547** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **38837** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 171/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1371 |
| socks5 | 1168 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 941 |
| ID | 353 |
| RU | 79 |
| MX | 77 |
| US | 77 |
| ?? | 74 |
| CN | 68 |
| PH | 65 |
| CO | 63 |
| BD | 51 |
| EC | 44 |
| VE | 42 |
| BR | 38 |
| DE | 38 |
| IN | 38 |
| VN | 37 |
| AR | 33 |
| DO | 30 |
| EG | 30 |
| SG | 25 |
| TR | 24 |
| PK | 23 |
| KH | 17 |
| TH | 16 |
| HK | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 3 | 2026-10-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 114 | 114 | 45 | 2026-10-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 145 | 145 | 76 | 2026-10-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-10-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 159 | 159 | 44 | 2026-10-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 370 | 370 | 136 | 2026-10-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 374 | 374 | 149 | 2026-10-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 780 | 780 | 320 | 2026-10-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 968 | 968 | 604 | 2026-10-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-10-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1781 | 1777 | 64 | 2026-10-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1593 | 2026-10-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2408 | 2406 | 741 | 2026-10-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2819 | 2817 | 858 | 2026-10-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2956 | 2954 | 2032 | 2026-10-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 51904 | 51904 | 36036 | 2026-10-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 57793 | 57792 | 2444 | 2026-10-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1251 | 44 | 111/124 |
| http://34.43.46.91:80 | US | 2551 | 41 | 120/124 |
| http://190.0.246.210:4040 | CO | 825 | 40 | 112/123 |
| http://149.130.173.58:9443 | CO | 424 | 35 | 35/35 |
| http://43.173.120.13:8899 | US | 220 | 35 | 35/35 |
| http://190.0.246.213:4040 | CO | 509 | 18 | 81/89 |
| http://144.124.251.24:10366 | NL | 662 | 18 | 47/70 |
| http://144.124.251.24:10689 | NL | 723 | 18 | 47/60 |
| http://144.124.251.24:10829 | NL | 680 | 18 | 44/56 |
| http://144.124.251.24:11108 | NL | 856 | 18 | 47/71 |
| http://197.224.185.3:3128 | MU | 1876 | 16 | 85/92 |
| http://176.111.37.5:39811 | HK | 1144 | 14 | 106/124 |
| http://189.51.168.165:999 | MX | 384 | 12 | 34/36 |
| http://103.237.102.191:11111 | DE | 1137 | 11 | 117/124 |
| http://128.199.116.219:9090 | SG | 1054 | 11 | 36/43 |
| http://61.91.162.126:8080 | TH | 1375 | 11 | 53/67 |
| http://103.10.231.189:8080 | TH | 1434 | 11 | 78/109 |
| socks5://101.36.104.239:10808 | JP | 1111 | 11 | 106/124 |
| http://186.5.94.206:999 | EC | 1001 | 9 | 79/86 |
| http://154.59.56.72:999 | VE | 2822 | 9 | 59/83 |
| socks5://45.155.71.236:1080 | AT | 3160 | 9 | 17/29 |
| http://198.244.254.77:3128 | GB | 3828 | 8 | 8/8 |
| socks5://36.155.23.163:10808 | CN | 1131 | 8 | 32/61 |
| socks5://171.25.158.95:1080 | SE | 5229 | 8 | 33/39 |
| http://200.59.191.27:999 | VE | 5013 | 7 | 80/119 |
| socks4://45.81.154.75:1080 | CA | 2066 | 7 | 16/31 |
| http://190.12.150.244:999 | EC | 2540 | 6 | 86/120 |
| http://203.252.142.217:80 | KR | 988 | 6 | 6/6 |
| http://104.248.151.93:9090 | SG | 1020 | 6 | 22/25 |
| http://146.190.80.158:9090 | SG | 1056 | 6 | 34/50 |
| http://159.223.41.216:9090 | SG | 1050 | 6 | 61/84 |
| http://190.97.241.106:999 | VE | 1450 | 6 | 76/108 |
| socks5://38.79.114.43:8885 | US | 368 | 6 | 6/6 |
| http://184.75.221.82:3118 | CA | 378 | 5 | 78/89 |
| http://45.186.6.104:3128 | EC | 593 | 5 | 95/102 |
| http://144.124.251.24:10605 | NL | 779 | 5 | 45/56 |
| http://130.110.103.245:3128 | SA | 7246 | 5 | 115/124 |
| http://34.43.46.91:443 | US | 2495 | 5 | 117/124 |
| http://193.104.179.115:3128 | UZ | 1484 | 5 | 62/89 |
| socks5://101.36.104.46:10808 | JP | 1574 | 5 | 108/124 |
| socks5://195.13.182.212:8080 | LV | 3350 | 5 | 5/5 |
| http://187.102.219.34:999 | AR | 2087 | 4 | 38/75 |
| http://187.102.219.64:999 | AR | 1176 | 4 | 36/63 |
| http://123.121.122.247:8888 | CN | 1844 | 4 | 4/4 |
| http://103.119.19.218:3128 | CZ | 729 | 4 | 30/37 |
| http://45.240.232.61:8080 | EG | 2707 | 4 | 43/104 |
| http://213.131.85.30:1976 | EG | 5824 | 4 | 12/41 |
| http://144.124.251.24:10000 | NL | 719 | 4 | 48/70 |
| http://185.238.238.49:58080 | PL | 4135 | 4 | 36/118 |
| http://128.199.121.61:9090 | SG | 1073 | 4 | 36/44 |
| http://167.99.74.174:9090 | SG | 1054 | 4 | 57/84 |
| http://3.211.120.181:443 | US | 248 | 4 | 18/35 |
| http://165.154.162.73:8888 | US | 4743 | 4 | 77/124 |
| socks5://156.225.20.83:1080 | HK | 3796 | 4 | 13/41 |
| socks5://220.158.232.118:1080 | KH | 4964 | 4 | 33/123 |
| socks5://5.255.103.55:1080 | NL | 4566 | 4 | 7/19 |
| socks5://143.198.239.45:10012 | US | 2949 | 4 | 6/11 |
| http://172.86.76.137:3128 | AE | 2963 | 3 | 14/37 |
| http://181.209.39.90:999 | AR | 5592 | 3 | 5/11 |
| http://102.244.78.61:8082 | CM | 1235 | 3 | 10/13 |
| http://102.244.78.61:8083 | CM | 1221 | 3 | 9/12 |
| http://102.244.78.61:8084 | CM | 1218 | 3 | 9/12 |
| http://102.244.78.61:8086 | CM | 1219 | 3 | 9/12 |
| http://114.254.48.23:8888 | CN | 7270 | 3 | 38/77 |
| http://123.119.25.143:8888 | CN | 1346 | 3 | 37/89 |
| http://123.121.132.32:8888 | CN | 1346 | 3 | 42/85 |
| http://179.1.241.200:999 | CO | 2347 | 3 | 25/75 |
| http://186.96.111.214:999 | CO | 1556 | 3 | 44/113 |
| http://45.71.186.211:999 | EC | 3816 | 3 | 28/77 |
| http://164.163.133.158:999 | EC | 1698 | 3 | 3/3 |
| http://177.234.221.202:999 | EC | 1355 | 3 | 16/28 |
| http://41.128.90.54:1981 | EG | 4396 | 3 | 4/5 |
| http://41.196.16.231:1976 | EG | 1238 | 3 | 4/5 |
| http://41.196.16.231:1981 | EG | 1077 | 3 | 8/40 |
| http://45.245.208.182:8080 | EG | 1367 | 3 | 9/13 |
| http://154.236.179.229:1976 | EG | 1516 | 3 | 9/41 |
| http://103.130.61.61:8081 | ID | 4304 | 3 | 95/124 |
| http://157.20.122.98:8080 | ID | 2423 | 3 | 10/23 |
| http://45.194.41.43:8080 | IN | 1115 | 3 | 11/70 |
| http://112.216.54.226:12121 | KR | 1159 | 3 | 41/118 |
| http://187.190.58.152:8081 | MX | 5225 | 3 | 24/97 |
| http://187.251.224.167:80 | MX | 5654 | 3 | 32/120 |
| http://144.124.251.24:10007 | NL | 868 | 3 | 48/73 |
| http://144.124.251.24:10261 | NL | 808 | 3 | 45/56 |
| http://144.124.251.24:10628 | NL | 730 | 3 | 43/56 |
| http://144.124.251.24:10771 | NL | 656 | 3 | 45/56 |
| http://144.124.251.24:11180 | NL | 855 | 3 | 44/55 |
| http://144.124.251.24:11480 | NL | 673 | 3 | 43/56 |
| http://124.217.10.191:8081 | PH | 3437 | 3 | 4/8 |
| http://203.177.217.222:8082 | PH | 2335 | 3 | 40/69 |
| http://43.159.54.178:80 | SG | 1049 | 3 | 27/44 |
| http://47.254.36.25:11080 | US | 5499 | 3 | 24/66 |
| http://113.160.155.121:19132 | VN | 5905 | 3 | 11/61 |
| http://180.148.4.74:8080 | VN | 5503 | 3 | 5/24 |
| http://210.211.113.34:80 | VN | 3876 | 3 | 63/96 |
| socks5://27.131.14.9:1088 | BD | 6041 | 3 | 3/3 |
| socks5://203.76.123.6:1080 | BD | 4245 | 3 | 24/72 |
| socks5://144.217.107.25:1080 | CA | 5005 | 3 | 18/34 |
| socks5://144.24.111.128:1088 | IN | 1834 | 3 | 92/124 |
| socks5://103.100.158.115:10809 | JP | 1514 | 3 | 8/12 |
