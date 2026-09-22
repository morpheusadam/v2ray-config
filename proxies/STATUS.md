# Proxy status

Generated 2026-09-22T17:38:32Z by `harvest.py`.

- **1667** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3169** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **32523** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 123/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1672 |
| http | 1490 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 1452 |
| ID | 340 |
| US | 115 |
| RU | 97 |
| CN | 83 |
| MX | 63 |
| PH | 59 |
| CO | 55 |
| DE | 53 |
| SG | 53 |
| IN | 50 |
| VE | 50 |
| BD | 49 |
| ?? | 37 |
| BR | 35 |
| VN | 34 |
| EG | 29 |
| TR | 29 |
| FR | 28 |
| EC | 27 |
| AR | 24 |
| HK | 24 |
| JP | 23 |
| TH | 21 |
| ZA | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 3 | 2026-09-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 77 | 77 | 43 | 2026-09-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 99 | 99 | 50 | 2026-09-22 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 136 | 136 | 49 | 2026-09-22 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-09-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 187 | 187 | 56 | 2026-09-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 246 | 246 | 118 | 2026-09-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-22 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 314 | 314 | 127 | 2026-09-22 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-22 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-22 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 612 | 612 | 94 | 2026-09-22 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-09-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1139 | 2026-09-22 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1787 | 1783 | 421 | 2026-09-22 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-09-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1945 | 1943 | 732 | 2026-09-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2059 | 2057 | 1526 | 2026-09-22 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2418 | 2416 | 663 | 2026-09-22 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 18049 | 18049 | 9640 | 2026-09-22 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 23034 | 23033 | 2041 | 2026-09-22 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 693 | 72 | 85/86 |
| http://130.110.103.245:3128 | SA | 1354 | 72 | 84/86 |
| http://1.231.81.166:3128 | KR | 4125 | 51 | 83/86 |
| http://190.97.236.128:999 | VE | 677 | 43 | 74/76 |
| http://190.97.236.129:999 | VE | 1727 | 43 | 74/76 |
| http://95.3.69.222:8080 | TR | 1163 | 41 | 83/86 |
| http://186.5.94.206:999 | EC | 820 | 23 | 46/48 |
| http://107.150.41.226:18080 | US | 374 | 23 | 23/23 |
| http://38.51.207.104:8080 | VE | 1657 | 19 | 26/27 |
| http://193.104.179.115:3128 | UZ | 2264 | 16 | 34/51 |
| http://190.0.246.213:4040 | CO | 3766 | 15 | 44/51 |
| http://213.111.146.36:18080 | NL | 667 | 15 | 18/23 |
| http://45.186.6.104:3128 | EC | 662 | 13 | 62/64 |
| http://153.51.201.35:999 | VE | 717 | 13 | 13/13 |
| http://201.71.2.27:999 | VE | 656 | 12 | 33/84 |
| http://190.97.241.106:999 | VE | 512 | 11 | 46/70 |
| socks5://193.233.223.47:1080 | RU | 1212 | 11 | 11/11 |
| http://176.111.37.5:39811 | HK | 4007 | 10 | 79/86 |
| http://144.124.251.24:10000 | NL | 595 | 10 | 18/32 |
| http://144.124.251.24:10007 | NL | 1203 | 10 | 17/35 |
| http://144.124.251.24:10008 | NL | 702 | 10 | 13/17 |
| http://144.124.251.24:10104 | NL | 817 | 10 | 13/18 |
| http://144.124.251.24:10176 | NL | 789 | 10 | 17/34 |
| http://144.124.251.24:10185 | NL | 1143 | 10 | 14/18 |
| http://144.124.251.24:10216 | NL | 713 | 10 | 18/35 |
| http://144.124.251.24:10226 | NL | 616 | 10 | 12/17 |
| http://144.124.251.24:10333 | NL | 632 | 10 | 16/35 |
| http://144.124.251.24:10346 | NL | 1106 | 10 | 14/18 |
| http://144.124.251.24:10366 | NL | 1480 | 10 | 15/32 |
| http://144.124.251.24:10372 | NL | 528 | 10 | 17/30 |
| http://144.124.251.24:10431 | NL | 711 | 10 | 19/34 |
| http://144.124.251.24:10453 | NL | 965 | 10 | 16/23 |
| http://144.124.251.24:10551 | NL | 2698 | 10 | 18/34 |
| http://144.124.251.24:10574 | NL | 615 | 10 | 18/35 |
| http://144.124.251.24:10628 | NL | 706 | 10 | 13/18 |
| http://144.124.251.24:10771 | NL | 733 | 10 | 13/18 |
| http://144.124.251.24:10829 | NL | 1929 | 10 | 13/18 |
| http://144.124.251.24:10953 | NL | 614 | 10 | 14/18 |
| http://144.124.251.24:11011 | NL | 742 | 10 | 14/18 |
| http://144.124.251.24:11108 | NL | 640 | 10 | 15/33 |
| http://144.124.251.24:11180 | NL | 700 | 10 | 13/17 |
| http://144.124.251.24:11265 | NL | 599 | 10 | 17/34 |
| http://144.124.251.24:11266 | NL | 612 | 10 | 14/18 |
| http://144.124.251.24:11274 | NL | 539 | 10 | 17/34 |
| http://144.124.251.24:11480 | NL | 751 | 10 | 12/18 |
| http://144.124.251.24:11491 | NL | 639 | 10 | 17/34 |
| socks5://161.35.90.93:1082 | NL | 1813 | 10 | 48/86 |
| socks5://45.32.160.61:1088 | US | 278 | 9 | 36/39 |
| socks5://83.147.217.103:1080 | US | 139 | 9 | 9/9 |
| http://144.124.251.24:10187 | NL | 980 | 8 | 14/32 |
| http://144.124.251.24:10230 | NL | 522 | 8 | 17/33 |
| http://144.124.251.24:10801 | NL | 1576 | 8 | 14/34 |
| http://159.223.41.216:9090 | SG | 2163 | 8 | 30/46 |
| socks5://213.199.47.140:1080 | FR | 3474 | 8 | 44/52 |
| socks5://95.181.160.37:1080 | DE | 1859 | 7 | 7/7 |
| socks5://135.125.232.151:1080 | DE | 694 | 7 | 15/17 |
| socks5://109.123.251.109:1080 | FR | 2506 | 7 | 46/86 |
| socks5://144.91.111.48:1088 | FR | 6668 | 7 | 54/86 |
| socks5://185.87.255.54:1080 | GB | 636 | 7 | 7/7 |
| socks5://101.36.104.239:10808 | JP | 1228 | 7 | 70/86 |
| socks5://150.109.247.86:8443 | KR | 1336 | 7 | 7/7 |
| socks5://135.148.120.20:1080 | US | 335 | 7 | 12/13 |
| socks5://193.25.215.182:22222 | US | 1064 | 7 | 79/86 |
| http://190.0.246.211:4040 | CO | 2101 | 6 | 73/86 |
| http://18.163.182.106:21128 | HK | 4419 | 6 | 25/54 |
| http://144.124.251.24:10082 | NL | 742 | 6 | 16/34 |
| http://128.199.121.61:9090 | SG | 1648 | 6 | 6/6 |
| http://167.172.76.176:9090 | SG | 1218 | 6 | 28/47 |
| socks5://5.75.133.113:10814 | DE | 4327 | 6 | 9/11 |
| socks5://64.227.186.105:1080 | IN | 1613 | 6 | 6/6 |
| socks5://103.75.118.84:1080 | JP | 2920 | 6 | 60/81 |
| socks5://57.128.231.218:1004 | PL | 940 | 6 | 15/20 |
| http://185.195.71.218:18080 | CH | 1548 | 5 | 15/23 |
| http://47.107.107.24:80 | CN | 2120 | 5 | 31/54 |
| http://144.124.251.24:10261 | NL | 712 | 5 | 13/18 |
| http://128.199.116.219:9090 | SG | 1170 | 5 | 5/5 |
| http://14.225.68.207:1337 | VN | 2526 | 5 | 5/5 |
| socks4://171.234.162.101:1083 | VN | 1667 | 5 | 5/5 |
| socks5://185.87.255.47:1080 | GB | 661 | 5 | 5/5 |
| socks5://101.36.104.46:10808 | JP | 3669 | 5 | 76/86 |
| socks5://104.238.220.231:1080 | US | 4028 | 5 | 5/5 |
| socks5://144.24.15.246:1080 | US | 3515 | 5 | 7/20 |
| socks5://144.24.47.42:1080 | US | 509 | 5 | 48/82 |
| socks5://160.22.17.4:9988 | VN | 1725 | 5 | 40/82 |
| http://38.159.37.213:999 | DO | 2222 | 4 | 6/24 |
| http://213.32.70.99:3128 | FR | 3300 | 4 | 4/4 |
| http://144.124.251.24:10601 | NL | 625 | 4 | 14/33 |
| http://154.59.56.74:999 | VE | 1624 | 4 | 34/49 |
| http://154.59.56.76:999 | VE | 2864 | 4 | 35/46 |
| http://200.59.191.27:999 | VE | 2891 | 4 | 51/81 |
| socks4://85.190.106.223:1080 | DE | 2400 | 4 | 6/9 |
| socks5://121.169.46.116:1090 | KR | 5933 | 4 | 57/86 |
| socks5://161.35.90.93:1081 | NL | 1672 | 4 | 43/86 |
| socks5://104.245.245.218:1080 | PL | 1169 | 4 | 4/4 |
| socks5://45.61.129.165:9050 | US | 2498 | 4 | 68/86 |
| http://27.185.218.213:17981 | CN | 2009 | 3 | 38/86 |
| http://177.234.217.236:999 | EC | 5349 | 3 | 20/59 |
| http://181.119.224.25:8080 | EC | 684 | 3 | 3/3 |
| http://103.157.79.5:8080 | ID | 2747 | 3 | 4/19 |
| http://160.19.19.18:8080 | ID | 6659 | 3 | 8/30 |
