# Proxy status

Generated 2026-09-21T22:48:44Z by `harvest.py`.

- **1754** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3236** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **31983** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 151/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1727 |
| http | 1501 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 1478 |
| ID | 344 |
| US | 116 |
| CN | 112 |
| RU | 95 |
| SG | 66 |
| MX | 65 |
| PH | 57 |
| DE | 56 |
| BD | 51 |
| IN | 50 |
| VE | 47 |
| CO | 43 |
| FR | 32 |
| VN | 32 |
| TR | 31 |
| BR | 29 |
| HK | 29 |
| EC | 28 |
| EG | 28 |
| JP | 25 |
| TH | 25 |
| ?? | 25 |
| PK | 23 |
| KH | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 1 | 2026-09-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 81 | 81 | 18 | 2026-09-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 89 | 89 | 37 | 2026-09-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 112 | 112 | 57 | 2026-09-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 80 | 2026-09-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 167 | 167 | 55 | 2026-09-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 306 | 306 | 174 | 2026-09-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 404 | 404 | 162 | 2026-09-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 444 | 444 | 89 | 2026-09-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-09-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-09-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1785 | 1781 | 1 | 2026-09-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1608 | 2026-09-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2191 | 2189 | 1686 | 2026-09-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2304 | 2302 | 715 | 2026-09-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2334 | 2332 | 380 | 2026-09-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 17523 | 17523 | 9796 | 2026-09-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 22933 | 22932 | 2278 | 2026-09-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1193 | 71 | 84/85 |
| http://185.200.188.234:10001 | RU | 1460 | 71 | 84/85 |
| http://130.110.103.245:3128 | SA | 1296 | 71 | 83/85 |
| http://1.231.81.166:3128 | KR | 2080 | 50 | 82/85 |
| http://190.97.236.128:999 | VE | 682 | 42 | 73/75 |
| http://190.97.236.129:999 | VE | 751 | 42 | 73/75 |
| http://95.3.69.222:8080 | TR | 1160 | 40 | 82/85 |
| http://91.134.141.4:3128 | FR | 584 | 24 | 44/46 |
| http://186.5.94.206:999 | EC | 919 | 22 | 45/47 |
| http://107.150.41.226:18080 | US | 509 | 22 | 22/22 |
| http://38.51.207.104:8080 | VE | 2819 | 18 | 25/26 |
| http://189.51.168.164:999 | MX | 397 | 16 | 49/50 |
| http://45.132.252.25:49156 | RU | 931 | 16 | 16/16 |
| http://193.104.179.115:3128 | UZ | 1488 | 15 | 33/50 |
| http://190.0.246.213:4040 | CO | 529 | 14 | 43/50 |
| http://213.111.146.36:18080 | NL | 570 | 14 | 17/22 |
| http://45.186.6.104:3128 | EC | 731 | 12 | 61/63 |
| http://61.91.162.126:8080 | TH | 1434 | 12 | 25/28 |
| http://103.10.231.189:8080 | TH | 1537 | 12 | 50/70 |
| http://153.51.201.35:999 | VE | 682 | 12 | 12/12 |
| http://201.71.2.25:999 | VE | 1416 | 11 | 26/72 |
| http://201.71.2.27:999 | VE | 1733 | 11 | 32/83 |
| http://190.97.241.106:999 | VE | 5403 | 10 | 45/69 |
| socks5://193.233.223.47:1080 | RU | 882 | 10 | 10/10 |
| http://176.111.37.5:39811 | HK | 1066 | 9 | 78/85 |
| http://144.124.251.24:10000 | NL | 783 | 9 | 17/31 |
| http://144.124.251.24:10007 | NL | 1160 | 9 | 16/34 |
| http://144.124.251.24:10008 | NL | 735 | 9 | 12/16 |
| http://144.124.251.24:10104 | NL | 583 | 9 | 12/17 |
| http://144.124.251.24:10176 | NL | 1647 | 9 | 16/33 |
| http://144.124.251.24:10185 | NL | 615 | 9 | 13/17 |
| http://144.124.251.24:10216 | NL | 1158 | 9 | 17/34 |
| http://144.124.251.24:10226 | NL | 645 | 9 | 11/16 |
| http://144.124.251.24:10333 | NL | 873 | 9 | 15/34 |
| http://144.124.251.24:10346 | NL | 658 | 9 | 13/17 |
| http://144.124.251.24:10366 | NL | 1679 | 9 | 14/31 |
| http://144.124.251.24:10372 | NL | 5806 | 9 | 16/29 |
| http://144.124.251.24:10431 | NL | 863 | 9 | 18/33 |
| http://144.124.251.24:10453 | NL | 755 | 9 | 15/22 |
| http://144.124.251.24:10551 | NL | 760 | 9 | 17/33 |
| http://144.124.251.24:10574 | NL | 844 | 9 | 17/34 |
| http://144.124.251.24:10628 | NL | 1887 | 9 | 12/17 |
| http://144.124.251.24:10771 | NL | 674 | 9 | 12/17 |
| http://144.124.251.24:10829 | NL | 581 | 9 | 12/17 |
| http://144.124.251.24:10953 | NL | 627 | 9 | 13/17 |
| http://144.124.251.24:11011 | NL | 629 | 9 | 13/17 |
| http://144.124.251.24:11108 | NL | 764 | 9 | 14/32 |
| http://144.124.251.24:11180 | NL | 621 | 9 | 12/16 |
| http://144.124.251.24:11265 | NL | 1674 | 9 | 16/33 |
| http://144.124.251.24:11266 | NL | 558 | 9 | 13/17 |
| http://144.124.251.24:11274 | NL | 1421 | 9 | 16/33 |
| http://144.124.251.24:11480 | NL | 567 | 9 | 11/17 |
| http://144.124.251.24:11491 | NL | 886 | 9 | 16/33 |
| socks5://161.35.90.93:1082 | NL | 2118 | 9 | 47/85 |
| socks5://45.32.160.61:1088 | US | 278 | 8 | 35/38 |
| socks5://83.147.217.103:1080 | US | 206 | 8 | 8/8 |
| http://62.193.104.26:1981 | EG | 3111 | 7 | 9/13 |
| http://144.124.251.24:10187 | NL | 1088 | 7 | 13/31 |
| http://144.124.251.24:10230 | NL | 2306 | 7 | 16/32 |
| http://144.124.251.24:10801 | NL | 718 | 7 | 13/33 |
| http://43.128.76.140:8080 | SG | 5700 | 7 | 14/18 |
| http://159.223.41.216:9090 | SG | 1089 | 7 | 29/45 |
| http://201.71.2.26:999 | VE | 4885 | 7 | 36/78 |
| socks5://213.199.47.140:1080 | FR | 2537 | 7 | 43/51 |
| http://31.31.74.185:9898 | CZ | 1994 | 6 | 6/6 |
| http://85.133.250.27:80 | IR | 1142 | 6 | 9/10 |
| http://43.156.199.63:8080 | SG | 1049 | 6 | 17/20 |
| socks5://95.181.160.37:1080 | DE | 748 | 6 | 6/6 |
| socks5://135.125.232.151:1080 | DE | 751 | 6 | 14/16 |
| socks5://109.123.251.109:1080 | FR | 1523 | 6 | 45/85 |
| socks5://144.91.111.48:1088 | FR | 1538 | 6 | 53/85 |
| socks5://185.87.255.54:1080 | GB | 1149 | 6 | 6/6 |
| socks5://101.36.104.239:10808 | JP | 2834 | 6 | 69/85 |
| socks5://150.109.247.86:8443 | KR | 1045 | 6 | 6/6 |
| socks5://135.148.120.20:1080 | US | 428 | 6 | 11/12 |
| socks5://193.25.215.182:22222 | US | 2192 | 6 | 78/85 |
| http://190.0.246.211:4040 | CO | 872 | 5 | 72/85 |
| http://190.12.150.244:999 | EC | 5709 | 5 | 54/81 |
| http://18.163.182.106:21128 | HK | 5768 | 5 | 24/53 |
| http://117.236.124.166:3128 | IN | 1356 | 5 | 57/85 |
| http://144.124.251.24:10082 | NL | 1698 | 5 | 15/33 |
| http://128.199.121.61:9090 | SG | 1094 | 5 | 5/5 |
| http://128.199.254.13:9090 | SG | 1108 | 5 | 10/14 |
| http://167.172.76.176:9090 | SG | 1578 | 5 | 27/46 |
| socks5://5.75.133.113:10814 | DE | 3877 | 5 | 8/10 |
| socks5://64.227.186.105:1080 | IN | 1541 | 5 | 5/5 |
| socks5://103.75.118.84:1080 | JP | 1763 | 5 | 59/80 |
| socks5://57.128.231.218:1004 | PL | 4403 | 5 | 14/19 |
| socks5://94.232.62.170:1080 | RU | 5338 | 5 | 6/8 |
| http://185.195.71.218:18080 | CH | 652 | 4 | 14/22 |
| http://47.107.107.24:80 | CN | 1863 | 4 | 30/53 |
| http://77.221.158.175:3128 | FI | 5097 | 4 | 19/44 |
| http://144.124.251.24:10261 | NL | 630 | 4 | 12/17 |
| http://128.199.116.219:9090 | SG | 1077 | 4 | 4/4 |
| http://159.65.233.169:54321 | US | 174 | 4 | 4/4 |
| http://201.71.2.24:999 | VE | 1787 | 4 | 29/73 |
| http://14.225.68.207:1337 | VN | 2410 | 4 | 4/4 |
| socks4://171.234.162.101:1083 | VN | 1537 | 4 | 4/4 |
| socks5://185.87.255.47:1080 | GB | 774 | 4 | 4/4 |
| socks5://45.194.33.12:30002 | HK | 1814 | 4 | 33/59 |
