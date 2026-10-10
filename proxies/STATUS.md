# Proxy status

Generated 2026-10-10T17:54:48Z by `harvest.py`.

- **1104** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3056** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 108/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1930 |
| socks5 | 1111 |
| socks4 | 15 |

| country | entries |
|---|---|
| NL | 906 |
| ID | 620 |
| PH | 110 |
| CO | 97 |
| US | 97 |
| MX | 87 |
| CN | 82 |
| RU | 82 |
| BR | 61 |
| VE | 58 |
| EC | 55 |
| BD | 51 |
| IN | 47 |
| VN | 45 |
| DO | 37 |
| PK | 37 |
| TR | 37 |
| SG | 32 |
| AR | 31 |
| DE | 30 |
| TH | 29 |
| EG | 26 |
| CL | 22 |
| PE | 21 |
| ZA | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-10-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 57 | 57 | 22 | 2026-10-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 92 | 92 | 18 | 2026-10-10 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 109 | 109 | 26 | 2026-10-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 120 | 120 | 56 | 2026-10-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-10-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 185 | 185 | 78 | 2026-10-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-10-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 336 | 336 | 66 | 2026-10-10 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-10-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 688 | 688 | 493 | 2026-10-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-10-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1602 | 2026-10-10 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1874 | 1870 | 0 | 2026-10-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2643 | 2641 | 677 | 2026-10-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2676 | 2674 | 1953 | 2026-10-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3522 | 3520 | 1188 | 2026-10-10 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 49384 | 49384 | 33434 | 2026-10-10 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 55209 | 55208 | 1986 | 2026-10-10 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 3022 | 41 | 108/121 |
| http://34.43.46.91:80 | US | 3255 | 38 | 117/121 |
| http://190.0.246.210:4040 | CO | 3158 | 37 | 109/120 |
| http://149.130.173.58:9443 | CO | 546 | 32 | 32/32 |
| http://43.173.120.13:8899 | US | 297 | 32 | 32/32 |
| http://190.0.246.213:4040 | CO | 2795 | 15 | 78/86 |
| http://144.124.251.24:10008 | NL | 789 | 15 | 43/52 |
| http://144.124.251.24:10176 | NL | 849 | 15 | 47/69 |
| http://144.124.251.24:10185 | NL | 749 | 15 | 44/53 |
| http://144.124.251.24:10216 | NL | 866 | 15 | 48/70 |
| http://144.124.251.24:10230 | NL | 654 | 15 | 46/68 |
| http://144.124.251.24:10299 | NL | 741 | 15 | 42/53 |
| http://144.124.251.24:10333 | NL | 788 | 15 | 46/70 |
| http://144.124.251.24:10337 | NL | 858 | 15 | 41/53 |
| http://144.124.251.24:10366 | NL | 865 | 15 | 44/67 |
| http://144.124.251.24:10372 | NL | 1245 | 15 | 47/65 |
| http://144.124.251.24:10551 | NL | 692 | 15 | 48/69 |
| http://144.124.251.24:10574 | NL | 683 | 15 | 48/70 |
| http://144.124.251.24:10601 | NL | 693 | 15 | 41/68 |
| http://144.124.251.24:10631 | NL | 718 | 15 | 43/53 |
| http://144.124.251.24:10689 | NL | 760 | 15 | 44/57 |
| http://144.124.251.24:10829 | NL | 925 | 15 | 41/53 |
| http://144.124.251.24:11011 | NL | 672 | 15 | 44/53 |
| http://144.124.251.24:11108 | NL | 810 | 15 | 44/68 |
| http://144.124.251.24:11124 | NL | 717 | 15 | 45/70 |
| http://144.124.251.24:11265 | NL | 742 | 15 | 47/69 |
| http://197.224.185.3:3128 | MU | 2039 | 13 | 82/89 |
| socks5://160.187.0.89:1080 | VN | 1528 | 12 | 27/34 |
| http://176.111.37.5:39811 | HK | 975 | 11 | 103/121 |
| http://176.111.37.216:39811 | HK | 986 | 11 | 100/121 |
| http://189.51.168.165:999 | MX | 6419 | 9 | 31/33 |
| http://5.129.254.5:8888 | RU | 1169 | 9 | 66/76 |
| http://5.129.254.49:8888 | RU | 1182 | 9 | 67/76 |
| http://5.129.254.51:8888 | RU | 1607 | 9 | 67/76 |
| http://5.129.254.60:8888 | RU | 1153 | 9 | 66/75 |
| http://5.129.254.70:8888 | RU | 2257 | 9 | 67/76 |
| http://5.129.254.129:8888 | RU | 1382 | 9 | 72/82 |
| http://5.129.254.154:8888 | RU | 1334 | 9 | 63/72 |
| http://5.129.254.215:8888 | RU | 1157 | 9 | 16/18 |
| http://5.129.254.243:8888 | RU | 1137 | 9 | 16/17 |
| http://49.229.100.235:8080 | TH | 1695 | 9 | 41/69 |
| http://103.237.102.191:11111 | DE | 914 | 8 | 114/121 |
| http://43.155.62.157:443 | HK | 7670 | 8 | 21/24 |
| http://128.199.116.219:9090 | SG | 1049 | 8 | 33/40 |
| http://61.91.162.126:8080 | TH | 1419 | 8 | 50/64 |
| http://103.10.231.189:8080 | TH | 1777 | 8 | 75/106 |
| socks5://101.36.104.239:10808 | JP | 3068 | 8 | 103/121 |
| http://144.124.251.24:10084 | NL | 700 | 7 | 41/53 |
| socks5://164.68.114.118:1080 | FR | 869 | 7 | 7/7 |
| http://186.5.94.206:999 | EC | 4152 | 6 | 76/83 |
| http://152.42.177.32:8888 | SG | 1124 | 6 | 48/81 |
| http://154.59.56.72:999 | VE | 2650 | 6 | 56/80 |
| http://154.59.56.78:999 | VE | 6668 | 6 | 54/77 |
| socks5://45.155.71.236:1080 | AT | 2153 | 6 | 14/26 |
| socks5://103.75.118.84:1080 | JP | 3051 | 6 | 85/116 |
| socks5://129.153.11.56:1080 | US | 226 | 6 | 19/26 |
| http://200.128.84.82:3128 | BR | 905 | 5 | 10/14 |
| http://221.221.162.6:8888 | CN | 3359 | 5 | 10/19 |
| http://181.78.195.137:999 | EC | 7488 | 5 | 32/121 |
| http://198.244.254.77:3128 | GB | 4130 | 5 | 5/5 |
| http://65.20.79.228:40002 | IN | 3447 | 5 | 7/9 |
| http://38.172.160.16:999 | VE | 5962 | 5 | 44/72 |
| socks5://36.155.23.163:10808 | CN | 1718 | 5 | 29/58 |
| socks5://212.77.75.25:1088 | IT | 2046 | 5 | 19/21 |
| socks5://171.25.158.95:1080 | SE | 4915 | 5 | 30/36 |
| http://41.128.90.54:1976 | EG | 3185 | 4 | 12/42 |
| http://62.193.104.29:1981 | EG | 5270 | 4 | 11/20 |
| http://203.175.102.54:3125 | ID | 2783 | 4 | 12/81 |
| http://38.194.246.34:999 | MX | 4029 | 4 | 67/112 |
| http://200.94.38.46:2604 | MX | 3327 | 4 | 11/17 |
| http://190.94.232.180:999 | VE | 2088 | 4 | 6/16 |
| http://200.59.191.27:999 | VE | 6304 | 4 | 77/116 |
| socks4://45.81.154.75:1080 | CA | 5585 | 4 | 13/28 |
| http://181.114.62.1:8085 | AR | 3258 | 3 | 13/97 |
| http://190.14.32.231:1080 | AR | 1913 | 3 | 7/16 |
| http://123.200.8.170:10000 | BD | 3738 | 3 | 42/119 |
| http://182.252.89.130:8080 | BD | 7988 | 3 | 13/60 |
| http://45.70.52.248:8080 | BR | 3245 | 3 | 15/61 |
| http://38.7.195.55:999 | CL | 3412 | 3 | 39/95 |
| http://114.246.203.194:8888 | CN | 1362 | 3 | 13/44 |
| http://123.121.122.28:8888 | CN | 1416 | 3 | 43/70 |
| http://181.78.174.14:8080 | CO | 3586 | 3 | 13/84 |
| http://177.234.221.204:999 | EC | 2873 | 3 | 13/24 |
| http://190.12.150.244:999 | EC | 7048 | 3 | 83/117 |
| http://41.33.245.138:1981 | EG | 2170 | 3 | 22/51 |
| http://181.78.44.63:999 | HN | 5033 | 3 | 16/45 |
| http://49.0.0.26:8080 | ID | 1376 | 3 | 6/31 |
| http://103.61.234.186:8180 | ID | 6246 | 3 | 48/118 |
| http://103.97.141.85:8080 | ID | 7424 | 3 | 8/35 |
| http://103.144.102.231:8080 | ID | 5149 | 3 | 6/17 |
| http://103.147.135.35:8082 | ID | 1422 | 3 | 20/57 |
| http://103.179.218.14:8080 | ID | 4411 | 3 | 15/66 |
| http://113.192.31.90:8080 | ID | 6648 | 3 | 12/109 |
| http://160.19.19.102:8080 | ID | 2773 | 3 | 12/65 |
| http://203.252.142.217:80 | KR | 1037 | 3 | 3/3 |
| http://45.168.239.58:999 | MX | 6591 | 3 | 23/104 |
| http://45.174.243.160:999 | MX | 2549 | 3 | 13/65 |
| http://131.196.246.4:999 | MX | 5995 | 3 | 15/63 |
| http://116.90.234.106:8080 | NP | 5187 | 3 | 12/66 |
| http://177.67.250.222:8080 | PE | 6171 | 3 | 14/76 |
