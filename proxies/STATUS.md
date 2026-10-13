# Proxy status

Generated 2026-10-13T01:36:38Z by `harvest.py`.

- **1314** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2886** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39181** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 117/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1796 |
| socks5 | 1078 |
| socks4 | 12 |

| country | entries |
|---|---|
| NL | 841 |
| ID | 571 |
| RU | 106 |
| PH | 93 |
| CO | 87 |
| MX | 87 |
| US | 79 |
| CN | 77 |
| BD | 75 |
| EC | 56 |
| VE | 54 |
| IN | 50 |
| VN | 43 |
| TR | 41 |
| BR | 40 |
| DE | 34 |
| EG | 33 |
| DO | 31 |
| AR | 30 |
| PK | 27 |
| TH | 26 |
| JP | 24 |
| SG | 24 |
| PE | 23 |
| KH | 18 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 93 | 93 | 41 | 2026-10-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 46 | 2026-10-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 82 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 184 | 184 | 59 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 230 | 230 | 85 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 241 | 241 | 109 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 536 | 536 | 371 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-10-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 900 | 900 | 372 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1134 | 2026-10-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1786 | 1782 | 337 | 2026-10-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1590 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2414 | 2412 | 766 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2957 | 2955 | 1958 | 2026-10-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3049 | 3047 | 898 | 2026-10-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 53554 | 53554 | 38736 | 2026-10-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 60451 | 60450 | 2979 | 2026-10-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1676 | 46 | 113/126 |
| http://34.43.46.91:80 | US | 1695 | 43 | 122/126 |
| http://190.0.246.210:4040 | CO | 1800 | 42 | 114/125 |
| http://149.130.173.58:9443 | CO | 514 | 37 | 37/37 |
| http://43.173.120.13:8899 | US | 1082 | 37 | 37/37 |
| http://190.0.246.213:4040 | CO | 771 | 20 | 83/91 |
| http://144.124.251.24:10366 | NL | 1001 | 20 | 49/72 |
| http://197.224.185.3:3128 | MU | 2488 | 18 | 87/94 |
| http://176.111.37.5:39811 | HK | 2332 | 16 | 108/126 |
| http://189.51.168.165:999 | MX | 481 | 14 | 36/38 |
| http://103.237.102.191:11111 | DE | 2009 | 13 | 119/126 |
| http://186.5.94.206:999 | EC | 1096 | 11 | 81/88 |
| socks5://36.155.23.163:10808 | CN | 2465 | 10 | 34/63 |
| http://190.12.150.244:999 | EC | 2074 | 8 | 88/122 |
| http://203.252.142.217:80 | KR | 1082 | 8 | 8/8 |
| http://104.248.151.93:9090 | SG | 1387 | 8 | 24/27 |
| http://146.190.80.158:9090 | SG | 1088 | 8 | 36/52 |
| http://159.223.41.216:9090 | SG | 1234 | 8 | 63/86 |
| http://45.186.6.104:3128 | EC | 798 | 7 | 97/104 |
| http://144.124.251.24:10605 | NL | 909 | 7 | 47/58 |
| http://34.43.46.91:443 | US | 2675 | 7 | 119/126 |
| socks5://101.36.104.46:10808 | JP | 3085 | 7 | 110/126 |
| socks5://195.13.182.212:8080 | LV | 5153 | 7 | 7/7 |
| http://187.102.219.64:999 | AR | 1365 | 6 | 38/65 |
| http://103.119.19.218:3128 | CZ | 839 | 6 | 32/39 |
| http://144.124.251.24:10000 | NL | 1179 | 6 | 50/72 |
| http://3.211.120.181:443 | US | 288 | 6 | 20/37 |
| http://165.154.162.73:8888 | US | 4335 | 6 | 79/126 |
| socks5://156.225.20.83:1080 | HK | 6344 | 6 | 15/43 |
| socks5://220.158.232.118:1080 | KH | 3405 | 6 | 35/125 |
| http://102.244.78.61:8082 | CM | 1490 | 5 | 12/15 |
| http://102.244.78.61:8083 | CM | 1335 | 5 | 11/14 |
| http://102.244.78.61:8084 | CM | 1361 | 5 | 11/14 |
| http://102.244.78.61:8086 | CM | 1304 | 5 | 11/14 |
| http://186.96.111.214:999 | CO | 3095 | 5 | 46/115 |
| http://45.245.208.182:8080 | EG | 1348 | 5 | 11/15 |
| http://154.236.179.229:1976 | EG | 2698 | 5 | 11/43 |
| http://103.130.61.61:8081 | ID | 2857 | 5 | 97/126 |
| http://187.190.58.152:8081 | MX | 6000 | 5 | 26/99 |
| http://144.124.251.24:10261 | NL | 966 | 5 | 47/58 |
| http://144.124.251.24:10628 | NL | 756 | 5 | 45/58 |
| http://144.124.251.24:10771 | NL | 954 | 5 | 47/58 |
| http://144.124.251.24:11180 | NL | 852 | 5 | 46/57 |
| socks5://144.217.107.25:1080 | CA | 5070 | 5 | 20/36 |
| socks5://144.24.111.128:1088 | IN | 2503 | 5 | 94/126 |
| http://123.200.8.170:10000 | BD | 4071 | 4 | 46/124 |
| http://101.206.186.99:8080 | CN | 3723 | 4 | 52/126 |
| http://114.249.225.156:8888 | CN | 1429 | 4 | 28/48 |
| http://119.188.131.55:17981 | CN | 2563 | 4 | 63/126 |
| http://38.75.82.216:999 | DO | 7495 | 4 | 19/95 |
| http://160.22.206.83:8082 | ID | 5672 | 4 | 24/94 |
| http://38.194.246.34:999 | MX | 3039 | 4 | 71/117 |
| http://187.190.114.40:999 | MX | 2021 | 4 | 20/50 |
| http://144.124.251.24:10811 | NL | 707 | 4 | 46/58 |
| http://129.226.89.151:80 | SG | 1123 | 4 | 48/73 |
| http://34.196.85.244:3128 | US | 317 | 4 | 4/4 |
| http://104.225.162.20:8082 | US | 2551 | 4 | 4/4 |
| http://210.211.113.33:80 | VN | 7101 | 4 | 62/96 |
| socks5://52.128.241.109:1080 | US | 562 | 4 | 5/7 |
| socks5://107.174.30.94:1080 | US | 1048 | 4 | 10/20 |
| http://103.133.201.243:8080 | BD | 6750 | 3 | 5/7 |
| http://143.208.152.62:3180 | BR | 7621 | 3 | 23/110 |
| http://147.15.126.122:28080 | BR | 4405 | 3 | 8/15 |
| http://186.235.255.220:8080 | BR | 6819 | 3 | 9/27 |
| http://201.186.41.170:999 | CL | 4362 | 3 | 3/3 |
| http://102.244.78.61:8080 | CM | 1494 | 3 | 11/15 |
| http://102.244.78.61:8081 | CM | 1348 | 3 | 9/12 |
| http://102.244.78.61:8088 | CM | 1468 | 3 | 10/14 |
| http://102.244.78.61:8089 | CM | 1399 | 3 | 10/14 |
| http://8.243.163.58:999 | CO | 7534 | 3 | 3/3 |
| http://45.238.56.249:2010 | EC | 6287 | 3 | 13/75 |
| http://177.234.217.237:999 | EC | 2364 | 3 | 45/99 |
| http://177.234.221.194:999 | EC | 6779 | 3 | 14/25 |
| http://177.234.221.195:999 | EC | 4970 | 3 | 12/28 |
| http://177.234.221.197:999 | EC | 5179 | 3 | 15/31 |
| http://177.234.236.96:999 | EC | 5769 | 3 | 8/27 |
| http://181.119.185.194:999 | EC | 5909 | 3 | 25/114 |
| http://41.33.60.42:8081 | EG | 6106 | 3 | 40/124 |
| http://43.99.60.244:8089 | HK | 1277 | 3 | 42/76 |
| http://31.58.57.74:1111 | ID | 7892 | 3 | 17/84 |
| http://103.107.136.70:8081 | ID | 6041 | 3 | 14/36 |
| http://103.122.64.232:8080 | ID | 6540 | 3 | 12/37 |
| http://103.133.26.17:3128 | ID | 1849 | 3 | 9/67 |
| http://103.193.144.118:8082 | ID | 2744 | 3 | 19/105 |
| http://54.249.49.32:8084 | JP | 5095 | 3 | 8/16 |
| http://102.68.76.247:5566 | KE | 6691 | 3 | 22/79 |
| http://178.217.168.164:55443 | KG | 3465 | 3 | 23/106 |
| http://38.194.251.246:999 | MX | 4978 | 3 | 23/89 |
| http://205.164.192.115:999 | MX | 2683 | 3 | 79/124 |
| http://144.124.251.24:10082 | NL | 701 | 3 | 46/74 |
| http://144.124.251.24:10187 | NL | 1123 | 3 | 46/72 |
| http://144.124.251.24:10412 | NL | 1406 | 3 | 45/58 |
| http://144.124.251.24:10601 | NL | 1089 | 3 | 45/73 |
| http://144.124.251.24:11265 | NL | 752 | 3 | 51/74 |
| http://103.25.220.246:8086 | PH | 5679 | 3 | 6/27 |
| http://5.129.254.5:8888 | RU | 1116 | 3 | 70/81 |
| http://5.129.254.49:8888 | RU | 1237 | 3 | 71/81 |
| http://5.129.254.51:8888 | RU | 1354 | 3 | 71/81 |
| http://5.129.254.60:8888 | RU | 1145 | 3 | 70/80 |
| http://5.129.254.70:8888 | RU | 1314 | 3 | 71/81 |
