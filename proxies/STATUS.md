# Proxy status

Generated 2026-11-23T00:28:09Z by `harvest.py`.

- **1701** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3909** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **26186** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 118/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3286 |
| socks5 | 618 |
| socks4 | 5 |

| country | entries |
|---|---|
| ID | 961 |
| ?? | 749 |
| NL | 406 |
| PH | 158 |
| MX | 124 |
| CO | 112 |
| TH | 87 |
| US | 79 |
| VE | 79 |
| BR | 78 |
| BD | 72 |
| IN | 71 |
| TR | 66 |
| RU | 53 |
| EC | 49 |
| AR | 44 |
| PK | 43 |
| CN | 42 |
| DO | 40 |
| ZA | 33 |
| EG | 32 |
| PE | 31 |
| SG | 26 |
| VN | 26 |
| DE | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 2 | 2026-11-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 91 | 91 | 13 | 2026-11-23 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 132 | 132 | 9 | 2026-11-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 25 | 2026-11-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 50 | 2026-11-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 163 | 163 | 27 | 2026-11-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 336 | 336 | 40 | 2026-11-23 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 442 | 442 | 297 | 2026-11-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-11-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 841 | 841 | 128 | 2026-11-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1123 | 2026-11-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-23 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1961 | 1961 | 372 | 2026-11-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2142 | 2142 | 293 | 2026-11-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2378 | 2378 | 720 | 2026-11-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2683 | 2683 | 1595 | 2026-11-23 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5680 | 5680 | 4438 | 2026-11-23 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12096 | 12096 | 2158 | 2026-11-23 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 999 | 79 | 189/208 |
| http://130.110.103.245:3128 | SA | 1248 | 54 | 190/208 |
| http://141.94.22.37:3128 | FR | 759 | 20 | 23/24 |
| http://45.155.226.177:3128 | HK | 744 | 17 | 22/24 |
| http://4.144.146.21:80 | SG | 857 | 15 | 91/100 |
| socks5://193.25.215.182:22222 | US | 1439 | 14 | 173/208 |
| http://34.43.46.91:80 | US | 480 | 13 | 201/208 |
| socks5://46.246.12.31:1080 | ?? | 3944 | 13 | 13/13 |
| http://189.51.168.164:999 | MX | 6485 | 12 | 40/44 |
| http://104.248.151.93:9090 | SG | 864 | 12 | 77/109 |
| http://20.98.234.24:8080 | ?? | 406 | 12 | 12/12 |
| socks5://69.55.49.177:38182 | US | 660 | 12 | 52/63 |
| http://103.237.102.191:11111 | DE | 840 | 11 | 195/208 |
| http://45.186.6.104:3128 | EC | 1070 | 10 | 176/186 |
| http://103.133.26.50:8080 | ID | 1190 | 10 | 74/109 |
| http://103.133.26.72:8080 | ID | 1204 | 10 | 82/134 |
| http://103.133.26.73:3128 | ID | 1245 | 10 | 98/186 |
| http://91.134.141.4:3128 | ?? | 787 | 10 | 10/10 |
| http://45.245.208.180:8080 | EG | 7252 | 9 | 57/81 |
| http://140.238.32.108:3128 | JP | 731 | 9 | 124/207 |
| http://217.142.139.207:8085 | ?? | 6557 | 9 | 10/11 |
| http://54.36.150.233:3128 | FR | 821 | 8 | 21/30 |
| http://154.59.56.72:999 | VE | 3504 | 8 | 124/167 |
| http://147.161.246.34:80 | ?? | 4536 | 8 | 8/8 |
| socks5://103.248.228.166:5555 | ?? | 982 | 8 | 10/11 |
| http://45.240.232.61:8080 | EG | 6472 | 7 | 82/188 |
| http://103.120.175.243:9191 | ID | 6986 | 7 | 16/71 |
| http://146.190.80.158:9090 | SG | 852 | 7 | 96/134 |
| socks5://101.36.104.46:10808 | JP | 791 | 7 | 172/208 |
| socks5://101.36.104.239:10808 | JP | 869 | 7 | 170/208 |
| http://187.102.219.42:999 | AR | 1550 | 6 | 116/203 |
| http://190.7.138.78:8080 | CO | 1055 | 6 | 55/137 |
| http://177.234.217.235:999 | EC | 6340 | 6 | 96/177 |
| http://190.12.150.244:999 | EC | 2929 | 6 | 151/204 |
| http://160.22.45.114:8080 | ID | 4055 | 6 | 44/67 |
| http://49.156.44.116:8080 | KH | 4108 | 6 | 20/42 |
| http://128.199.113.85:9090 | SG | 910 | 6 | 26/39 |
| http://167.99.74.174:9090 | SG | 862 | 6 | 113/168 |
| http://195.226.213.251:8888 | UA | 6941 | 6 | 83/202 |
| http://38.172.181.0:999 | VE | 2728 | 6 | 61/115 |
| http://45.135.95.185:3128 | ?? | 2488 | 6 | 6/6 |
| http://191.44.125.14:8080 | ?? | 6460 | 6 | 7/8 |
| socks4://188.226.27.24:1080 | RU | 2404 | 6 | 33/44 |
| socks5://91.107.179.68:10809 | DE | 1089 | 6 | 75/141 |
| socks5://123.58.219.171:10808 | HK | 1202 | 6 | 150/208 |
| http://186.22.246.60:3128 | AR | 7082 | 5 | 9/16 |
| http://190.123.83.137:999 | AR | 5183 | 5 | 38/45 |
| http://101.251.204.174:8080 | CN | 1684 | 5 | 107/194 |
| http://111.192.28.24:8888 | CN | 1281 | 5 | 15/30 |
| http://114.244.221.178:8888 | CN | 1779 | 5 | 68/131 |
| http://198.244.254.77:3128 | GB | 3247 | 5 | 74/92 |
| http://45.43.60.220:8080 | JP | 6687 | 5 | 114/207 |
| http://144.124.251.24:10000 | NL | 985 | 5 | 88/154 |
| http://144.124.251.24:10007 | NL | 817 | 5 | 81/157 |
| http://144.124.251.24:10082 | NL | 872 | 5 | 79/156 |
| http://144.124.251.24:10084 | NL | 902 | 5 | 78/140 |
| http://144.124.251.24:10088 | NL | 879 | 5 | 74/140 |
| http://144.124.251.24:10104 | NL | 990 | 5 | 77/140 |
| http://144.124.251.24:10176 | NL | 1010 | 5 | 90/156 |
| http://144.124.251.24:10185 | NL | 819 | 5 | 79/140 |
| http://144.124.251.24:10187 | NL | 996 | 5 | 86/154 |
| http://144.124.251.24:10216 | NL | 855 | 5 | 92/157 |
| http://144.124.251.24:10230 | NL | 1004 | 5 | 85/155 |
| http://144.124.251.24:10261 | NL | 932 | 5 | 82/140 |
| http://144.124.251.24:10333 | NL | 869 | 5 | 86/157 |
| http://144.124.251.24:10346 | NL | 810 | 5 | 80/140 |
| http://144.124.251.24:10366 | NL | 863 | 5 | 84/154 |
| http://144.124.251.24:10431 | NL | 851 | 5 | 83/156 |
| http://144.124.251.24:10453 | NL | 854 | 5 | 86/145 |
| http://144.124.251.24:10471 | NL | 1044 | 5 | 82/155 |
| http://144.124.251.24:10485 | NL | 849 | 5 | 62/140 |
| http://144.124.251.24:10551 | NL | 948 | 5 | 83/156 |
| http://144.124.251.24:10566 | NL | 971 | 5 | 87/141 |
| http://144.124.251.24:10574 | NL | 901 | 5 | 87/157 |
| http://144.124.251.24:10601 | NL | 861 | 5 | 82/155 |
| http://144.124.251.24:10605 | NL | 1006 | 5 | 85/140 |
| http://144.124.251.24:10689 | NL | 1192 | 5 | 87/144 |
| http://144.124.251.24:10801 | NL | 873 | 5 | 75/156 |
| http://144.124.251.24:10818 | NL | 803 | 5 | 71/140 |
| http://144.124.251.24:11011 | NL | 863 | 5 | 81/140 |
| http://144.124.251.24:11108 | NL | 1143 | 5 | 80/155 |
| http://144.124.251.24:11124 | NL | 851 | 5 | 86/157 |
| http://144.124.251.24:11180 | NL | 949 | 5 | 87/139 |
| http://144.124.251.24:11265 | NL | 936 | 5 | 87/156 |
| http://144.124.251.24:11274 | NL | 856 | 5 | 78/156 |
| http://144.124.251.24:11450 | NL | 1043 | 5 | 74/140 |
| http://144.124.251.24:11491 | NL | 804 | 5 | 80/156 |
| http://69.87.216.54:7989 | US | 201 | 5 | 80/153 |
| http://200.59.191.27:999 | VE | 3334 | 5 | 140/203 |
| http://103.147.135.32:8082 | ?? | 2285 | 5 | 6/8 |
| http://147.161.246.34:10165 | ?? | 4874 | 5 | 5/5 |
| http://150.228.10.232:8080 | ?? | 7727 | 5 | 6/10 |
| http://195.154.176.34:3128 | ?? | 5824 | 5 | 11/13 |
| http://217.154.195.87:8888 | ?? | 1806 | 5 | 7/8 |
| socks4://103.13.19.219:10808 | JP | 1052 | 5 | 17/25 |
| socks5://45.194.33.12:30001 | HK | 3631 | 5 | 34/84 |
| socks5://103.236.190.197:1080 | ID | 2379 | 5 | 44/206 |
| socks5://121.169.46.116:1090 | KR | 4766 | 5 | 138/208 |
| socks5://88.84.204.217:1080 | RU | 6469 | 5 | 18/91 |
| socks5://79.98.32.107:1080 | ?? | 2728 | 5 | 7/12 |
