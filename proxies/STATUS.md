# Proxy status

Generated 2026-09-27T22:32:36Z by `harvest.py`.

- **1563** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3587** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39809** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 127/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1923 |
| http | 1652 |
| socks4 | 12 |

| country | entries |
|---|---|
| NL | 1714 |
| ?? | 397 |
| ID | 381 |
| CN | 123 |
| US | 106 |
| RU | 59 |
| MX | 57 |
| CO | 55 |
| IN | 53 |
| PH | 50 |
| DE | 46 |
| VE | 37 |
| BR | 32 |
| BD | 30 |
| EC | 28 |
| VN | 26 |
| DO | 25 |
| SG | 25 |
| EG | 24 |
| AR | 22 |
| TR | 20 |
| PK | 19 |
| FR | 18 |
| JP | 18 |
| HK | 17 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 1 | 2026-09-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 28 | 28 | 5 | 2026-09-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 72 | 72 | 32 | 2026-09-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 88 | 88 | 23 | 2026-09-27 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-09-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 182 | 182 | 55 | 2026-09-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 273 | 273 | 97 | 2026-09-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 286 | 286 | 81 | 2026-09-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 327 | 327 | 51 | 2026-09-27 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-09-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-09-27 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1595 | 1592 | 233 | 2026-09-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-09-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1586 | 2026-09-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2799 | 2797 | 664 | 2026-09-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2841 | 2839 | 2049 | 2026-09-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3157 | 3155 | 470 | 2026-09-27 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 26664 | 26664 | 13500 | 2026-09-27 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 33187 | 33186 | 3281 | 2026-09-27 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1197 | 83 | 96/97 |
| http://190.97.236.128:999 | VE | 926 | 54 | 85/87 |
| http://190.97.236.129:999 | VE | 978 | 54 | 85/87 |
| http://95.3.69.222:8080 | TR | 1498 | 52 | 94/97 |
| http://38.51.207.104:8080 | VE | 1530 | 30 | 37/38 |
| http://190.0.246.213:4040 | CO | 735 | 26 | 55/62 |
| http://213.111.146.36:18080 | NL | 756 | 26 | 29/34 |
| http://153.51.201.35:999 | VE | 972 | 24 | 24/24 |
| http://144.124.251.24:10007 | NL | 888 | 21 | 28/46 |
| http://144.124.251.24:10008 | NL | 954 | 21 | 24/28 |
| http://144.124.251.24:10104 | NL | 854 | 21 | 24/29 |
| http://144.124.251.24:10176 | NL | 1021 | 21 | 28/45 |
| http://144.124.251.24:10185 | NL | 851 | 21 | 25/29 |
| http://144.124.251.24:10216 | NL | 855 | 21 | 29/46 |
| http://144.124.251.24:10226 | NL | 1053 | 21 | 23/28 |
| http://144.124.251.24:10333 | NL | 1058 | 21 | 27/46 |
| http://144.124.251.24:10346 | NL | 845 | 21 | 25/29 |
| http://144.124.251.24:10366 | NL | 911 | 21 | 26/43 |
| http://144.124.251.24:10372 | NL | 798 | 21 | 28/41 |
| http://144.124.251.24:10431 | NL | 898 | 21 | 30/45 |
| http://144.124.251.24:10453 | NL | 1279 | 21 | 27/34 |
| http://144.124.251.24:10551 | NL | 1114 | 21 | 29/45 |
| http://144.124.251.24:10574 | NL | 820 | 21 | 29/46 |
| http://144.124.251.24:10771 | NL | 1011 | 21 | 24/29 |
| http://144.124.251.24:10953 | NL | 951 | 21 | 25/29 |
| http://144.124.251.24:11011 | NL | 796 | 21 | 25/29 |
| http://144.124.251.24:11265 | NL | 787 | 21 | 28/45 |
| http://144.124.251.24:11266 | NL | 982 | 21 | 25/29 |
| http://144.124.251.24:11274 | NL | 845 | 21 | 28/45 |
| http://144.124.251.24:11480 | NL | 827 | 21 | 23/29 |
| http://144.124.251.24:11491 | NL | 915 | 21 | 28/45 |
| socks5://83.147.217.103:1080 | US | 505 | 20 | 20/20 |
| http://144.124.251.24:10801 | NL | 820 | 19 | 25/45 |
| socks5://185.87.255.54:1080 | GB | 902 | 18 | 18/18 |
| http://190.0.246.211:4040 | CO | 1165 | 17 | 84/97 |
| http://167.172.76.176:9090 | SG | 863 | 17 | 39/58 |
| http://144.124.251.24:10261 | NL | 1178 | 16 | 24/29 |
| http://154.59.56.76:999 | VE | 5155 | 15 | 46/57 |
| http://144.124.251.24:10084 | NL | 837 | 14 | 24/29 |
| http://144.124.251.24:10088 | NL | 816 | 14 | 23/29 |
| http://144.124.251.24:10412 | NL | 808 | 14 | 24/29 |
| http://144.124.251.24:10471 | NL | 830 | 14 | 28/44 |
| http://144.124.251.24:10566 | NL | 923 | 14 | 25/30 |
| http://144.124.251.24:10605 | NL | 2911 | 14 | 24/29 |
| http://144.124.251.24:10610 | NL | 1317 | 14 | 24/29 |
| http://144.124.251.24:10631 | NL | 1014 | 14 | 24/29 |
| http://144.124.251.24:10658 | NL | 863 | 14 | 24/29 |
| http://144.124.251.24:10689 | NL | 999 | 14 | 25/33 |
| http://144.124.251.24:10800 | NL | 847 | 14 | 24/29 |
| http://144.124.251.24:10811 | NL | 2950 | 14 | 24/29 |
| http://144.124.251.24:10818 | NL | 848 | 14 | 21/29 |
| http://144.124.251.24:11450 | NL | 1034 | 14 | 22/29 |
| http://34.43.46.91:80 | US | 588 | 14 | 93/97 |
| http://190.0.246.210:4040 | CO | 969 | 13 | 85/96 |
| http://103.237.102.191:11111 | DE | 958 | 13 | 91/97 |
| http://154.59.56.73:999 | VE | 5505 | 13 | 56/69 |
| http://190.97.236.130:999 | VE | 919 | 13 | 23/26 |
| http://18.157.123.132:3128 | DE | 794 | 12 | 44/58 |
| http://3.216.199.128:3128 | US | 410 | 12 | 12/12 |
| socks5://109.205.182.143:1088 | FR | 6114 | 12 | 12/12 |
| socks5://107.167.18.122:443 | US | 222 | 12 | 47/49 |
| socks5://144.91.121.61:1088 | FR | 1693 | 11 | 83/97 |
| http://34.43.46.91:443 | US | 1531 | 10 | 91/97 |
| http://123.121.132.32:8888 | CN | 5391 | 9 | 27/58 |
| http://189.51.168.165:999 | MX | 808 | 9 | 9/9 |
| http://144.124.251.24:10000 | NL | 795 | 9 | 28/43 |
| http://144.124.251.24:10187 | NL | 951 | 9 | 24/43 |
| http://144.124.251.24:10230 | NL | 840 | 9 | 27/44 |
| http://144.124.251.24:10829 | NL | 1185 | 9 | 23/29 |
| http://144.124.251.24:11108 | NL | 993 | 9 | 25/44 |
| http://144.124.251.24:11124 | NL | 856 | 9 | 26/46 |
| http://144.124.251.24:11180 | NL | 1216 | 9 | 23/28 |
| socks5://23.239.30.204:1088 | US | 1494 | 9 | 9/9 |
| http://149.130.173.58:9443 | CO | 745 | 8 | 8/8 |
| http://43.173.120.13:8899 | US | 176 | 8 | 8/8 |
| http://161.22.39.58:999 | VE | 962 | 8 | 8/8 |
| socks5://45.61.129.165:9050 | US | 3892 | 8 | 78/97 |
| http://144.124.251.24:10485 | NL | 995 | 7 | 21/29 |
| http://128.199.121.61:9090 | SG | 867 | 7 | 15/17 |
| http://3.212.18.54:3128 | ?? | 432 | 7 | 7/7 |
| socks5://43.167.166.56:1080 | JP | 1255 | 7 | 8/9 |
| socks5://171.25.158.95:1080 | SE | 2481 | 7 | 8/12 |
| http://36.137.204.11:8002 | CN | 3148 | 6 | 9/13 |
| http://190.12.150.244:999 | EC | 2668 | 6 | 64/93 |
| http://154.59.56.78:999 | VE | 7279 | 6 | 34/53 |
| http://200.59.191.27:999 | VE | 2764 | 6 | 61/92 |
| socks5://160.187.0.89:1080 | VN | 1420 | 6 | 7/10 |
| http://185.195.71.218:18080 | CH | 1753 | 5 | 25/34 |
| http://120.232.115.170:17981 | CN | 1255 | 5 | 71/96 |
| http://31.31.74.185:9898 | CZ | 945 | 5 | 16/18 |
| http://103.119.19.218:3128 | CZ | 848 | 5 | 9/10 |
| http://186.5.94.206:999 | EC | 2407 | 5 | 56/59 |
| http://37.59.125.131:8888 | FR | 1089 | 5 | 76/97 |
| http://167.86.104.220:80 | FR | 883 | 5 | 16/33 |
| http://144.124.251.24:10299 | NL | 825 | 5 | 23/29 |
| http://144.124.251.24:10337 | NL | 849 | 5 | 23/29 |
| http://3.1.100.245:3128 | SG | 933 | 5 | 6/9 |
| http://43.156.248.220:80 | SG | 860 | 5 | 13/19 |
| http://43.159.54.178:80 | SG | 866 | 5 | 12/17 |
| http://47.81.56.193:8888 | TH | 1351 | 5 | 58/97 |
