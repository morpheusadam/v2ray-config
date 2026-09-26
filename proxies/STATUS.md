# Proxy status

Generated 2026-09-26T17:07:42Z by `harvest.py`.

- **3167** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5196** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 218/600 (36%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3167 |
| http | 2019 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 2929 |
| ID | 469 |
| ?? | 425 |
| US | 142 |
| CN | 112 |
| RU | 82 |
| MX | 66 |
| CO | 60 |
| DE | 56 |
| PH | 56 |
| VE | 50 |
| IN | 48 |
| BD | 45 |
| BR | 43 |
| FR | 32 |
| JP | 32 |
| EC | 31 |
| SG | 31 |
| VN | 31 |
| EG | 27 |
| HK | 23 |
| KH | 23 |
| DO | 22 |
| TR | 20 |
| CL | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-09-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 41 | 41 | 15 | 2026-09-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 113 | 113 | 29 | 2026-09-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 118 | 118 | 47 | 2026-09-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-09-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 249 | 249 | 86 | 2026-09-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 380 | 380 | 144 | 2026-09-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 421 | 421 | 169 | 2026-09-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-09-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1125 | 2026-09-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1582 | 2026-09-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1820 | 1820 | 1057 | 2026-09-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1933 | 1929 | 0 | 2026-09-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2756 | 2754 | 1125 | 2026-09-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3160 | 3158 | 2219 | 2026-09-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3694 | 3692 | 850 | 2026-09-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 23636 | 23636 | 11908 | 2026-09-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 29577 | 29576 | 2649 | 2026-09-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1214 | 80 | 93/94 |
| http://130.110.103.245:3128 | SA | 1720 | 80 | 92/94 |
| http://190.97.236.128:999 | VE | 948 | 51 | 82/84 |
| http://190.97.236.129:999 | VE | 1002 | 51 | 82/84 |
| http://95.3.69.222:8080 | TR | 1678 | 49 | 91/94 |
| http://38.51.207.104:8080 | VE | 716 | 27 | 34/35 |
| http://193.104.179.115:3128 | UZ | 1422 | 24 | 42/59 |
| http://190.0.246.213:4040 | CO | 754 | 23 | 52/59 |
| http://213.111.146.36:18080 | NL | 784 | 23 | 26/31 |
| http://153.51.201.35:999 | VE | 1019 | 21 | 21/21 |
| http://144.124.251.24:10007 | NL | 828 | 18 | 25/43 |
| http://144.124.251.24:10008 | NL | 792 | 18 | 21/25 |
| http://144.124.251.24:10104 | NL | 856 | 18 | 21/26 |
| http://144.124.251.24:10176 | NL | 789 | 18 | 25/42 |
| http://144.124.251.24:10185 | NL | 789 | 18 | 22/26 |
| http://144.124.251.24:10216 | NL | 799 | 18 | 26/43 |
| http://144.124.251.24:10226 | NL | 806 | 18 | 20/25 |
| http://144.124.251.24:10333 | NL | 822 | 18 | 24/43 |
| http://144.124.251.24:10346 | NL | 1750 | 18 | 22/26 |
| http://144.124.251.24:10366 | NL | 1097 | 18 | 23/40 |
| http://144.124.251.24:10372 | NL | 795 | 18 | 25/38 |
| http://144.124.251.24:10431 | NL | 1095 | 18 | 27/42 |
| http://144.124.251.24:10453 | NL | 992 | 18 | 24/31 |
| http://144.124.251.24:10551 | NL | 974 | 18 | 26/42 |
| http://144.124.251.24:10574 | NL | 813 | 18 | 26/43 |
| http://144.124.251.24:10771 | NL | 812 | 18 | 21/26 |
| http://144.124.251.24:10953 | NL | 804 | 18 | 22/26 |
| http://144.124.251.24:11011 | NL | 826 | 18 | 22/26 |
| http://144.124.251.24:11265 | NL | 811 | 18 | 25/42 |
| http://144.124.251.24:11266 | NL | 920 | 18 | 22/26 |
| http://144.124.251.24:11274 | NL | 1020 | 18 | 25/42 |
| http://144.124.251.24:11480 | NL | 796 | 18 | 20/26 |
| http://144.124.251.24:11491 | NL | 1357 | 18 | 25/42 |
| socks5://83.147.217.103:1080 | US | 511 | 17 | 17/17 |
| http://144.124.251.24:10801 | NL | 825 | 16 | 22/42 |
| socks5://185.87.255.54:1080 | GB | 978 | 15 | 15/15 |
| socks5://101.36.104.239:10808 | JP | 1900 | 15 | 78/94 |
| http://190.0.246.211:4040 | CO | 971 | 14 | 81/94 |
| http://167.172.76.176:9090 | SG | 950 | 14 | 36/55 |
| socks5://103.75.118.84:1080 | JP | 2995 | 14 | 68/89 |
| http://144.124.251.24:10261 | NL | 762 | 13 | 21/26 |
| http://128.199.116.219:9090 | SG | 1027 | 13 | 13/13 |
| socks5://101.36.104.46:10808 | JP | 3687 | 13 | 84/94 |
| http://154.59.56.76:999 | VE | 2887 | 12 | 43/54 |
| http://144.124.251.24:10084 | NL | 956 | 11 | 21/26 |
| http://144.124.251.24:10088 | NL | 839 | 11 | 20/26 |
| http://144.124.251.24:10412 | NL | 4892 | 11 | 21/26 |
| http://144.124.251.24:10471 | NL | 973 | 11 | 25/41 |
| http://144.124.251.24:10566 | NL | 964 | 11 | 22/27 |
| http://144.124.251.24:10605 | NL | 788 | 11 | 21/26 |
| http://144.124.251.24:10610 | NL | 939 | 11 | 21/26 |
| http://144.124.251.24:10631 | NL | 894 | 11 | 21/26 |
| http://144.124.251.24:10658 | NL | 820 | 11 | 21/26 |
| http://144.124.251.24:10689 | NL | 1131 | 11 | 22/30 |
| http://144.124.251.24:10800 | NL | 958 | 11 | 21/26 |
| http://144.124.251.24:10811 | NL | 936 | 11 | 21/26 |
| http://144.124.251.24:10818 | NL | 999 | 11 | 18/26 |
| http://144.124.251.24:11450 | NL | 828 | 11 | 19/26 |
| http://34.43.46.91:80 | US | 711 | 11 | 90/94 |
| http://190.0.246.210:4040 | CO | 860 | 10 | 82/93 |
| http://103.237.102.191:11111 | DE | 904 | 10 | 88/94 |
| http://154.59.56.73:999 | VE | 2975 | 10 | 53/66 |
| http://190.97.236.130:999 | VE | 1098 | 10 | 20/23 |
| http://200.229.65.172:3128 | BR | 1216 | 9 | 9/9 |
| http://18.157.123.132:3128 | DE | 808 | 9 | 41/55 |
| http://3.216.199.128:3128 | US | 441 | 9 | 9/9 |
| socks5://109.205.182.143:1088 | FR | 1181 | 9 | 9/9 |
| socks5://107.167.18.122:443 | US | 102 | 9 | 44/46 |
| http://140.238.32.108:3128 | JP | 1874 | 8 | 45/93 |
| socks5://144.91.121.61:1088 | FR | 3224 | 8 | 80/94 |
| http://91.233.223.147:3128 | RU | 1292 | 7 | 21/68 |
| http://34.43.46.91:443 | US | 740 | 7 | 88/94 |
| http://123.121.132.32:8888 | CN | 2092 | 6 | 24/55 |
| http://125.33.195.27:8888 | CN | 2089 | 6 | 18/40 |
| http://134.199.191.115:3128 | DE | 4113 | 6 | 6/6 |
| http://189.51.168.165:999 | MX | 1059 | 6 | 6/6 |
| http://144.124.251.24:10000 | NL | 815 | 6 | 25/40 |
| http://144.124.251.24:10187 | NL | 835 | 6 | 21/40 |
| http://144.124.251.24:10230 | NL | 811 | 6 | 24/41 |
| http://144.124.251.24:10829 | NL | 2616 | 6 | 20/26 |
| http://144.124.251.24:11108 | NL | 1004 | 6 | 22/41 |
| http://144.124.251.24:11124 | NL | 1075 | 6 | 23/43 |
| http://144.124.251.24:11180 | NL | 827 | 6 | 20/25 |
| socks5://23.239.30.204:1088 | US | 5680 | 6 | 6/6 |
| http://101.251.204.174:8080 | CN | 2813 | 5 | 42/80 |
| http://222.128.173.231:8888 | CN | 1581 | 5 | 27/62 |
| http://45.65.138.48:999 | CO | 5001 | 5 | 33/94 |
| http://149.130.173.58:9443 | CO | 571 | 5 | 5/5 |
| http://91.134.141.4:3128 | FR | 771 | 5 | 49/55 |
| http://146.196.40.146:8080 | ID | 7781 | 5 | 21/87 |
| http://43.173.120.13:8899 | US | 77 | 5 | 5/5 |
| http://161.22.39.58:999 | VE | 905 | 5 | 5/5 |
| http://201.71.2.25:999 | VE | 2390 | 5 | 33/81 |
| socks5://34.84.162.206:38081 | JP | 931 | 5 | 22/84 |
| socks5://45.74.31.50:9702 | NL | 2893 | 5 | 6/7 |
| socks5://45.151.102.248:10808 | RU | 5302 | 5 | 5/5 |
| socks5://45.61.129.165:9050 | US | 1276 | 5 | 75/94 |
| http://187.102.219.42:999 | AR | 1352 | 4 | 46/89 |
| http://38.7.195.52:999 | CL | 3314 | 4 | 35/76 |
| http://200.10.30.5:8083 | CO | 5747 | 4 | 27/83 |
