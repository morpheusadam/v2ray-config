# Proxy status

Generated 2026-10-13T23:25:24Z by `harvest.py`.

- **2805** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4179** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39218** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 237/600 (40%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2519 |
| socks5 | 1649 |
| socks4 | 11 |

| country | entries |
|---|---|
| NL | 1373 |
| ID | 760 |
| PH | 136 |
| MX | 135 |
| RU | 127 |
| CO | 124 |
| US | 120 |
| BD | 89 |
| CN | 84 |
| VE | 80 |
| BR | 74 |
| IN | 74 |
| VN | 67 |
| TR | 61 |
| EC | 56 |
| DO | 48 |
| SG | 43 |
| TH | 43 |
| DE | 40 |
| AR | 35 |
| JP | 32 |
| PK | 32 |
| EG | 30 |
| ZA | 30 |
| CA | 28 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 2 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 124 | 124 | 33 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 136 | 136 | 61 | 2026-10-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 60 | 2026-10-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 88 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 195 | 195 | 62 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-10-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 576 | 576 | 237 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 660 | 660 | 210 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1146 | 1146 | 787 | 2026-10-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1474 | 1474 | 90 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1140 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1590 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2385 | 2383 | 738 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2857 | 2855 | 846 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2953 | 2951 | 1893 | 2026-10-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 55738 | 55738 | 40939 | 2026-10-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 63361 | 63360 | 2666 | 2026-10-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 806 | 48 | 115/128 |
| http://34.43.46.91:80 | US | 1549 | 45 | 124/128 |
| http://190.0.246.210:4040 | CO | 1465 | 44 | 116/127 |
| http://149.130.173.58:9443 | CO | 555 | 39 | 39/39 |
| http://190.0.246.213:4040 | CO | 629 | 22 | 85/93 |
| http://144.124.251.24:10366 | NL | 1066 | 22 | 51/74 |
| http://197.224.185.3:3128 | MU | 2338 | 20 | 89/96 |
| http://176.111.37.5:39811 | HK | 1322 | 18 | 110/128 |
| http://189.51.168.165:999 | MX | 480 | 16 | 38/40 |
| http://103.237.102.191:11111 | DE | 1108 | 15 | 121/128 |
| http://186.5.94.206:999 | EC | 874 | 13 | 83/90 |
| socks5://36.155.23.163:10808 | CN | 1324 | 12 | 36/65 |
| http://190.12.150.244:999 | EC | 2785 | 10 | 90/124 |
| http://203.252.142.217:80 | KR | 887 | 10 | 10/10 |
| http://104.248.151.93:9090 | SG | 1037 | 10 | 26/29 |
| http://146.190.80.158:9090 | SG | 1053 | 10 | 38/54 |
| http://45.186.6.104:3128 | EC | 2739 | 9 | 99/106 |
| http://144.124.251.24:10605 | NL | 808 | 9 | 49/60 |
| socks5://101.36.104.46:10808 | JP | 3015 | 9 | 112/128 |
| socks5://195.13.182.212:8080 | LV | 1401 | 9 | 9/9 |
| http://187.102.219.64:999 | AR | 3701 | 8 | 40/67 |
| http://144.124.251.24:10000 | NL | 807 | 8 | 52/74 |
| http://3.211.120.181:443 | US | 285 | 8 | 22/39 |
| http://165.154.162.73:8888 | US | 4938 | 8 | 81/128 |
| http://102.244.78.61:8083 | CM | 1311 | 7 | 13/16 |
| http://103.130.61.61:8081 | ID | 3204 | 7 | 99/128 |
| http://144.124.251.24:10261 | NL | 830 | 7 | 49/60 |
| http://144.124.251.24:10628 | NL | 751 | 7 | 47/60 |
| http://144.124.251.24:10771 | NL | 811 | 7 | 49/60 |
| http://144.124.251.24:11180 | NL | 755 | 7 | 48/59 |
| http://101.206.186.99:8080 | CN | 6858 | 6 | 54/128 |
| http://144.124.251.24:10811 | NL | 1369 | 6 | 48/60 |
| http://34.196.85.244:3128 | US | 342 | 6 | 6/6 |
| socks5://52.128.241.109:1080 | US | 391 | 6 | 7/9 |
| socks5://107.174.30.94:1080 | US | 6427 | 6 | 12/22 |
| http://186.235.255.220:8080 | BR | 3983 | 5 | 11/29 |
| http://102.244.78.61:8080 | CM | 1305 | 5 | 13/17 |
| http://102.244.78.61:8088 | CM | 1325 | 5 | 12/16 |
| http://45.238.56.249:2010 | EC | 2492 | 5 | 15/77 |
| http://103.133.26.17:3128 | ID | 1804 | 5 | 11/69 |
| http://102.68.76.247:5566 | KE | 1926 | 5 | 24/81 |
| http://144.124.251.24:10082 | NL | 1280 | 5 | 48/76 |
| http://144.124.251.24:10187 | NL | 755 | 5 | 48/74 |
| http://144.124.251.24:10412 | NL | 786 | 5 | 47/60 |
| http://144.124.251.24:10601 | NL | 835 | 5 | 47/75 |
| http://144.124.251.24:11265 | NL | 809 | 5 | 53/76 |
| http://5.129.254.5:8888 | RU | 1156 | 5 | 72/83 |
| http://5.129.254.49:8888 | RU | 1229 | 5 | 73/83 |
| http://5.129.254.51:8888 | RU | 1633 | 5 | 73/83 |
| http://5.129.254.60:8888 | RU | 2670 | 5 | 72/82 |
| http://5.129.254.70:8888 | RU | 1120 | 5 | 73/83 |
| http://5.129.254.129:8888 | RU | 2643 | 5 | 78/89 |
| http://5.129.254.154:8888 | RU | 1286 | 5 | 69/79 |
| http://5.129.254.215:8888 | RU | 1629 | 5 | 22/25 |
| http://5.129.254.243:8888 | RU | 1357 | 5 | 22/24 |
| http://44.216.27.249:3128 | US | 203 | 5 | 21/25 |
| socks5://110.38.233.122:1080 | PK | 4202 | 5 | 7/8 |
| socks5://116.101.14.169:1089 | VN | 1815 | 5 | 5/5 |
| http://179.185.75.94:8080 | BR | 1472 | 4 | 7/40 |
| http://38.7.195.49:999 | CL | 4950 | 4 | 45/102 |
| http://38.7.195.52:999 | CL | 2868 | 4 | 50/110 |
| http://38.7.195.55:999 | CL | 1928 | 4 | 44/102 |
| http://38.50.165.122:999 | DO | 4948 | 4 | 24/116 |
| http://41.65.55.27:1981 | EG | 4776 | 4 | 23/68 |
| http://34.88.38.81:9443 | FI | 896 | 4 | 63/93 |
| http://35.228.49.168:9443 | FI | 724 | 4 | 44/65 |
| http://34.105.252.3:3128 | GB | 565 | 4 | 7/10 |
| http://43.155.62.157:443 | HK | 5152 | 4 | 26/31 |
| http://103.124.137.171:8080 | ID | 1386 | 4 | 17/70 |
| http://103.133.26.50:8080 | ID | 1392 | 4 | 8/29 |
| http://103.133.26.72:8080 | ID | 2271 | 4 | 9/54 |
| http://103.133.26.73:3128 | ID | 1454 | 4 | 24/106 |
| http://103.133.26.119:8080 | ID | 1748 | 4 | 8/38 |
| http://111.92.88.27:3128 | IN | 1964 | 4 | 17/97 |
| http://164.52.219.64:8080 | IN | 1412 | 4 | 4/4 |
| http://144.124.251.24:10084 | NL | 748 | 4 | 47/60 |
| http://144.124.251.24:10176 | NL | 678 | 4 | 52/76 |
| http://144.124.251.24:10185 | NL | 692 | 4 | 49/60 |
| http://144.124.251.24:10299 | NL | 831 | 4 | 47/60 |
| http://144.124.251.24:10566 | NL | 962 | 4 | 48/61 |
| http://144.124.251.24:10801 | NL | 748 | 4 | 47/76 |
| http://144.124.251.24:11274 | NL | 758 | 4 | 50/76 |
| http://144.124.251.24:11491 | NL | 643 | 4 | 52/76 |
| http://185.238.238.169:58080 | PL | 990 | 4 | 22/50 |
| http://82.47.161.152:8443 | TR | 985 | 4 | 4/4 |
| http://31.220.54.93:8080 | US | 1383 | 4 | 4/4 |
| http://66.210.33.34:8080 | US | 6280 | 4 | 9/36 |
| http://104.129.203.85:9480 | US | 324 | 4 | 4/4 |
| socks5://5.75.133.113:10814 | DE | 2188 | 4 | 27/53 |
| socks5://213.199.47.140:1080 | FR | 1598 | 4 | 74/94 |
| socks5://123.58.219.171:10808 | HK | 2512 | 4 | 100/128 |
| socks5://212.77.75.25:1088 | IT | 1784 | 4 | 25/28 |
| socks5://124.248.191.83:1080 | KH | 5957 | 4 | 30/108 |
| socks5://217.12.209.4:1080 | NL | 814 | 4 | 10/69 |
| socks5://104.245.245.218:1080 | PL | 931 | 4 | 4/4 |
| socks5://82.196.69.34:1080 | RU | 2163 | 4 | 12/35 |
| socks5://67.207.92.87:1088 | US | 1415 | 4 | 72/127 |
| socks5://150.136.58.221:1080 | US | 3446 | 4 | 32/128 |
| socks5://193.25.215.182:22222 | US | 1009 | 4 | 107/128 |
| http://138.117.14.237:9090 | AR | 4525 | 3 | 16/66 |
