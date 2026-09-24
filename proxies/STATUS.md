# Proxy status

Generated 2026-09-24T22:43:41Z by `harvest.py`.

- **2184** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4228** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35976** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 208/600 (35%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2393 |
| socks5 | 1821 |
| socks4 | 14 |

| country | entries |
|---|---|
| NL | 1575 |
| ID | 597 |
| ?? | 277 |
| US | 157 |
| CN | 132 |
| RU | 108 |
| CO | 81 |
| MX | 81 |
| PH | 80 |
| IN | 71 |
| BR | 69 |
| BD | 64 |
| DE | 55 |
| VE | 55 |
| VN | 54 |
| SG | 45 |
| TR | 39 |
| DO | 38 |
| JP | 38 |
| EC | 35 |
| FR | 31 |
| EG | 29 |
| TH | 28 |
| CA | 26 |
| PK | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 1 | 2026-09-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 48 | 48 | 26 | 2026-09-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 98 | 98 | 44 | 2026-09-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 113 | 113 | 36 | 2026-09-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 148 | 148 | 49 | 2026-09-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 86 | 2026-09-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 263 | 263 | 23 | 2026-09-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 305 | 305 | 118 | 2026-09-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 336 | 336 | 158 | 2026-09-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-09-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-09-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1145 | 2026-09-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1593 | 2026-09-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1872 | 1868 | 452 | 2026-09-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2505 | 2503 | 683 | 2026-09-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2742 | 2740 | 1913 | 2026-09-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3025 | 3023 | 550 | 2026-09-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 20495 | 20495 | 10511 | 2026-09-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 26822 | 26821 | 2512 | 2026-09-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1150 | 77 | 90/91 |
| http://130.110.103.245:3128 | SA | 1437 | 77 | 89/91 |
| http://1.231.81.166:3128 | KR | 1166 | 56 | 88/91 |
| http://190.97.236.128:999 | VE | 914 | 48 | 79/81 |
| http://190.97.236.129:999 | VE | 848 | 48 | 79/81 |
| http://95.3.69.222:8080 | TR | 1454 | 46 | 88/91 |
| http://186.5.94.206:999 | EC | 1080 | 28 | 51/53 |
| http://107.150.41.226:18080 | US | 386 | 28 | 28/28 |
| http://38.51.207.104:8080 | VE | 3715 | 24 | 31/32 |
| http://193.104.179.115:3128 | UZ | 1390 | 21 | 39/56 |
| http://190.0.246.213:4040 | CO | 1934 | 20 | 49/56 |
| http://213.111.146.36:18080 | NL | 663 | 20 | 23/28 |
| http://153.51.201.35:999 | VE | 883 | 18 | 18/18 |
| http://144.124.251.24:10007 | NL | 814 | 15 | 22/40 |
| http://144.124.251.24:10008 | NL | 713 | 15 | 18/22 |
| http://144.124.251.24:10104 | NL | 801 | 15 | 18/23 |
| http://144.124.251.24:10176 | NL | 4734 | 15 | 22/39 |
| http://144.124.251.24:10185 | NL | 924 | 15 | 19/23 |
| http://144.124.251.24:10216 | NL | 814 | 15 | 23/40 |
| http://144.124.251.24:10226 | NL | 679 | 15 | 17/22 |
| http://144.124.251.24:10333 | NL | 691 | 15 | 21/40 |
| http://144.124.251.24:10346 | NL | 844 | 15 | 19/23 |
| http://144.124.251.24:10366 | NL | 825 | 15 | 20/37 |
| http://144.124.251.24:10372 | NL | 1028 | 15 | 22/35 |
| http://144.124.251.24:10431 | NL | 1149 | 15 | 24/39 |
| http://144.124.251.24:10453 | NL | 650 | 15 | 21/28 |
| http://144.124.251.24:10551 | NL | 674 | 15 | 23/39 |
| http://144.124.251.24:10574 | NL | 652 | 15 | 23/40 |
| http://144.124.251.24:10628 | NL | 674 | 15 | 18/23 |
| http://144.124.251.24:10771 | NL | 1159 | 15 | 18/23 |
| http://144.124.251.24:10953 | NL | 3161 | 15 | 19/23 |
| http://144.124.251.24:11011 | NL | 1365 | 15 | 19/23 |
| http://144.124.251.24:11265 | NL | 671 | 15 | 22/39 |
| http://144.124.251.24:11266 | NL | 835 | 15 | 19/23 |
| http://144.124.251.24:11274 | NL | 782 | 15 | 22/39 |
| http://144.124.251.24:11480 | NL | 793 | 15 | 17/23 |
| http://144.124.251.24:11491 | NL | 661 | 15 | 22/39 |
| socks5://83.147.217.103:1080 | US | 408 | 14 | 14/14 |
| http://144.124.251.24:10801 | NL | 725 | 13 | 19/39 |
| socks5://213.199.47.140:1080 | FR | 3093 | 13 | 49/57 |
| socks5://185.87.255.54:1080 | GB | 877 | 12 | 12/12 |
| socks5://101.36.104.239:10808 | JP | 1908 | 12 | 75/91 |
| http://190.0.246.211:4040 | CO | 2064 | 11 | 78/91 |
| http://144.124.251.24:10082 | NL | 1727 | 11 | 21/39 |
| http://167.172.76.176:9090 | SG | 1004 | 11 | 33/52 |
| socks5://103.75.118.84:1080 | JP | 961 | 11 | 65/86 |
| http://185.195.71.218:18080 | CH | 759 | 10 | 20/28 |
| http://144.124.251.24:10261 | NL | 916 | 10 | 18/23 |
| http://128.199.116.219:9090 | SG | 1018 | 10 | 10/10 |
| socks5://101.36.104.46:10808 | JP | 4796 | 10 | 81/91 |
| http://213.32.70.99:3128 | FR | 721 | 9 | 9/9 |
| http://154.59.56.76:999 | VE | 2977 | 9 | 40/51 |
| http://181.119.224.25:8080 | EC | 879 | 8 | 8/8 |
| http://197.224.185.3:3128 | MU | 2286 | 8 | 54/59 |
| http://144.124.251.24:10084 | NL | 839 | 8 | 18/23 |
| http://144.124.251.24:10088 | NL | 901 | 8 | 17/23 |
| http://144.124.251.24:10299 | NL | 1833 | 8 | 18/23 |
| http://144.124.251.24:10337 | NL | 781 | 8 | 18/23 |
| http://144.124.251.24:10412 | NL | 819 | 8 | 18/23 |
| http://144.124.251.24:10471 | NL | 749 | 8 | 22/38 |
| http://144.124.251.24:10566 | NL | 739 | 8 | 19/24 |
| http://144.124.251.24:10605 | NL | 890 | 8 | 18/23 |
| http://144.124.251.24:10610 | NL | 4308 | 8 | 18/23 |
| http://144.124.251.24:10631 | NL | 816 | 8 | 18/23 |
| http://144.124.251.24:10658 | NL | 1121 | 8 | 18/23 |
| http://144.124.251.24:10689 | NL | 1248 | 8 | 19/27 |
| http://144.124.251.24:10800 | NL | 806 | 8 | 18/23 |
| http://144.124.251.24:10811 | NL | 2208 | 8 | 18/23 |
| http://144.124.251.24:10818 | NL | 788 | 8 | 15/23 |
| http://144.124.251.24:11450 | NL | 910 | 8 | 16/23 |
| http://34.43.46.91:80 | US | 373 | 8 | 87/91 |
| http://172.210.12.8:3128 | US | 308 | 8 | 13/27 |
| http://190.0.246.210:4040 | CO | 2880 | 7 | 79/90 |
| http://103.237.102.191:11111 | DE | 1010 | 7 | 85/91 |
| http://35.78.212.217:32053 | JP | 3584 | 7 | 17/73 |
| http://154.59.56.72:999 | VE | 4434 | 7 | 33/50 |
| http://154.59.56.73:999 | VE | 3971 | 7 | 50/63 |
| http://190.97.236.130:999 | VE | 798 | 7 | 17/20 |
| http://200.229.65.172:3128 | BR | 1554 | 6 | 6/6 |
| http://38.7.195.50:999 | CL | 7174 | 6 | 25/50 |
| http://18.157.123.132:3128 | DE | 706 | 6 | 38/52 |
| http://103.130.61.61:8081 | ID | 3424 | 6 | 73/91 |
| http://3.216.199.128:3128 | US | 284 | 6 | 6/6 |
| http://195.158.8.123:3128 | UZ | 4741 | 6 | 61/89 |
| socks5://109.205.182.143:1088 | FR | 841 | 6 | 6/6 |
| socks5://123.58.219.171:10808 | HK | 3205 | 6 | 73/91 |
| socks5://107.167.18.122:443 | US | 229 | 6 | 41/43 |
| http://200.229.76.160:3128 | BR | 4779 | 5 | 9/11 |
| http://184.75.221.82:3118 | CA | 2365 | 5 | 50/56 |
| http://38.7.195.49:999 | CL | 3522 | 5 | 23/65 |
| http://114.252.12.211:8888 | CN | 1256 | 5 | 27/56 |
| http://120.232.115.57:17981 | CN | 1392 | 5 | 12/16 |
| http://123.121.208.63:8888 | CN | 1657 | 5 | 17/37 |
| http://222.128.172.158:8888 | CN | 2918 | 5 | 22/56 |
| http://177.93.33.55:999 | CO | 3179 | 5 | 22/78 |
| http://31.31.74.185:9898 | CZ | 1166 | 5 | 11/12 |
| http://34.88.38.81:9443 | FI | 810 | 5 | 38/56 |
| http://35.228.49.168:9443 | FI | 819 | 5 | 19/28 |
| http://196.61.42.26:3128 | GH | 2463 | 5 | 25/59 |
| http://176.111.37.216:39811 | HK | 1254 | 5 | 75/91 |
