# Proxy status

Generated 2026-10-12T21:52:50Z by `harvest.py`.

- **1539** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2794** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39577** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 176/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1739 |
| socks5 | 1042 |
| socks4 | 13 |

| country | entries |
|---|---|
| NL | 785 |
| ID | 555 |
| RU | 99 |
| US | 91 |
| PH | 88 |
| MX | 86 |
| CO | 83 |
| BD | 68 |
| CN | 68 |
| EC | 53 |
| VE | 51 |
| IN | 50 |
| VN | 46 |
| BR | 40 |
| DE | 40 |
| TR | 39 |
| AR | 34 |
| EG | 34 |
| PK | 31 |
| DO | 30 |
| SG | 23 |
| PE | 22 |
| TH | 22 |
| KH | 20 |
| CL | 17 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-10-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-12 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 126 | 126 | 51 | 2026-10-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 127 | 127 | 73 | 2026-10-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-10-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 295 | 295 | 96 | 2026-10-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 332 | 332 | 118 | 2026-10-12 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 432 | 432 | 199 | 2026-10-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 616 | 616 | 384 | 2026-10-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-10-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 647 | 647 | 148 | 2026-10-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1143 | 2026-10-12 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1798 | 1794 | 394 | 2026-10-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1593 | 2026-10-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2300 | 2298 | 782 | 2026-10-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2795 | 2793 | 1906 | 2026-10-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2898 | 2896 | 1056 | 2026-10-12 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 53554 | 53554 | 38391 | 2026-10-12 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 60451 | 60450 | 2318 | 2026-10-12 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1001 | 45 | 112/125 |
| http://34.43.46.91:80 | US | 2724 | 42 | 121/125 |
| http://190.0.246.210:4040 | CO | 584 | 41 | 113/124 |
| http://149.130.173.58:9443 | CO | 591 | 36 | 36/36 |
| http://43.173.120.13:8899 | US | 300 | 36 | 36/36 |
| http://190.0.246.213:4040 | CO | 515 | 19 | 82/90 |
| http://144.124.251.24:10366 | NL | 530 | 19 | 48/71 |
| http://144.124.251.24:10689 | NL | 576 | 19 | 48/61 |
| http://144.124.251.24:10829 | NL | 599 | 19 | 45/57 |
| http://197.224.185.3:3128 | MU | 2064 | 17 | 86/93 |
| http://176.111.37.5:39811 | HK | 1778 | 15 | 107/125 |
| http://189.51.168.165:999 | MX | 385 | 13 | 35/37 |
| http://103.237.102.191:11111 | DE | 1013 | 12 | 118/125 |
| http://103.10.231.189:8080 | TH | 1665 | 12 | 79/110 |
| http://186.5.94.206:999 | EC | 1108 | 10 | 80/87 |
| http://154.59.56.72:999 | VE | 2695 | 10 | 60/84 |
| http://198.244.254.77:3128 | GB | 4625 | 9 | 9/9 |
| socks5://36.155.23.163:10808 | CN | 1593 | 9 | 33/62 |
| http://200.59.191.27:999 | VE | 3962 | 8 | 81/120 |
| http://190.12.150.244:999 | EC | 2572 | 7 | 87/121 |
| http://203.252.142.217:80 | KR | 916 | 7 | 7/7 |
| http://104.248.151.93:9090 | SG | 1095 | 7 | 23/26 |
| http://146.190.80.158:9090 | SG | 1094 | 7 | 35/51 |
| http://159.223.41.216:9090 | SG | 1088 | 7 | 62/85 |
| http://190.97.241.106:999 | VE | 1517 | 7 | 77/109 |
| socks5://38.79.114.43:8885 | US | 605 | 7 | 7/7 |
| http://45.186.6.104:3128 | EC | 715 | 6 | 96/103 |
| http://144.124.251.24:10605 | NL | 845 | 6 | 46/57 |
| http://130.110.103.245:3128 | SA | 1392 | 6 | 116/125 |
| http://34.43.46.91:443 | US | 3272 | 6 | 118/125 |
| socks5://101.36.104.46:10808 | JP | 1617 | 6 | 109/125 |
| socks5://195.13.182.212:8080 | LV | 3810 | 6 | 6/6 |
| http://187.102.219.34:999 | AR | 2973 | 5 | 39/76 |
| http://187.102.219.64:999 | AR | 5297 | 5 | 37/64 |
| http://103.119.19.218:3128 | CZ | 1319 | 5 | 31/38 |
| http://45.240.232.61:8080 | EG | 5177 | 5 | 44/105 |
| http://144.124.251.24:10000 | NL | 542 | 5 | 49/71 |
| http://167.99.74.174:9090 | SG | 1088 | 5 | 58/85 |
| http://3.211.120.181:443 | US | 155 | 5 | 19/36 |
| http://165.154.162.73:8888 | US | 3076 | 5 | 78/125 |
| socks5://156.225.20.83:1080 | HK | 5637 | 5 | 14/42 |
| socks5://220.158.232.118:1080 | KH | 2620 | 5 | 34/124 |
| socks5://5.255.103.55:1080 | NL | 2337 | 5 | 8/20 |
| http://172.86.76.137:3128 | AE | 1649 | 4 | 15/38 |
| http://102.244.78.61:8082 | CM | 1264 | 4 | 11/14 |
| http://102.244.78.61:8083 | CM | 1266 | 4 | 10/13 |
| http://102.244.78.61:8084 | CM | 1291 | 4 | 10/13 |
| http://102.244.78.61:8086 | CM | 1216 | 4 | 10/13 |
| http://186.96.111.214:999 | CO | 1949 | 4 | 45/114 |
| http://164.163.133.158:999 | EC | 6947 | 4 | 4/4 |
| http://177.234.221.202:999 | EC | 3494 | 4 | 17/29 |
| http://45.245.208.182:8080 | EG | 1202 | 4 | 10/14 |
| http://154.236.179.229:1976 | EG | 1677 | 4 | 10/42 |
| http://103.130.61.61:8081 | ID | 1430 | 4 | 96/125 |
| http://187.190.58.152:8081 | MX | 2275 | 4 | 25/98 |
| http://144.124.251.24:10007 | NL | 551 | 4 | 49/74 |
| http://144.124.251.24:10261 | NL | 595 | 4 | 46/57 |
| http://144.124.251.24:10628 | NL | 690 | 4 | 44/57 |
| http://144.124.251.24:10771 | NL | 590 | 4 | 46/57 |
| http://144.124.251.24:11180 | NL | 742 | 4 | 45/56 |
| http://203.177.217.222:8082 | PH | 2685 | 4 | 41/70 |
| http://210.211.113.34:80 | VN | 4000 | 4 | 64/97 |
| socks5://144.217.107.25:1080 | CA | 3598 | 4 | 19/35 |
| socks5://144.24.111.128:1088 | IN | 1960 | 4 | 93/125 |
| socks5://103.100.158.115:10809 | JP | 3538 | 4 | 9/13 |
| http://123.200.8.170:10000 | BD | 6848 | 3 | 45/123 |
| http://102.244.78.61:8085 | CM | 1259 | 3 | 10/15 |
| http://102.244.78.61:8087 | CM | 1265 | 3 | 10/15 |
| http://102.244.78.61:8090 | CM | 1239 | 3 | 11/17 |
| http://101.206.186.99:8080 | CN | 2932 | 3 | 51/125 |
| http://114.249.225.156:8888 | CN | 1694 | 3 | 27/47 |
| http://119.188.131.55:17981 | CN | 1605 | 3 | 62/125 |
| http://221.221.162.6:8888 | CN | 2234 | 3 | 13/23 |
| http://181.78.17.131:999 | CO | 2900 | 3 | 36/122 |
| http://38.75.82.216:999 | DO | 5730 | 3 | 18/94 |
| http://41.128.72.142:1976 | EG | 4691 | 3 | 3/3 |
| http://2.139.41.14:3128 | ES | 6914 | 3 | 10/35 |
| http://38.226.243.97:8080 | ID | 7149 | 3 | 8/26 |
| http://41.216.186.41:8080 | ID | 2896 | 3 | 21/51 |
| http://103.143.105.138:8080 | ID | 4186 | 3 | 6/23 |
| http://103.155.190.130:8080 | ID | 4719 | 3 | 6/31 |
| http://160.22.206.83:8082 | ID | 1502 | 3 | 23/93 |
| http://38.194.246.34:999 | MX | 2426 | 3 | 70/116 |
| http://38.210.177.61:999 | MX | 5864 | 3 | 16/113 |
| http://45.174.168.16:999 | MX | 4649 | 3 | 14/78 |
| http://187.190.114.40:999 | MX | 6516 | 3 | 19/49 |
| http://187.245.209.253:999 | MX | 7744 | 3 | 3/3 |
| http://187.249.112.221:999 | MX | 2521 | 3 | 20/102 |
| http://144.124.251.24:10811 | NL | 705 | 3 | 45/57 |
| http://190.108.82.251:999 | PE | 6439 | 3 | 4/6 |
| http://175.107.30.110:8080 | PK | 5271 | 3 | 3/3 |
| http://129.226.89.151:80 | SG | 1087 | 3 | 47/72 |
| http://34.196.85.244:3128 | US | 182 | 3 | 3/3 |
| http://104.225.162.20:8082 | US | 251 | 3 | 3/3 |
| http://113.161.93.6:8080 | VN | 5662 | 3 | 21/49 |
| http://210.211.113.33:80 | VN | 6044 | 3 | 61/95 |
| socks5://31.77.19.92:443 | DE | 1111 | 3 | 3/3 |
| socks5://49.13.22.249:10811 | DE | 3651 | 3 | 41/97 |
| socks5://91.107.179.68:10809 | DE | 2607 | 3 | 33/58 |
| socks5://45.74.31.41:6076 | NL | 4554 | 3 | 3/3 |
