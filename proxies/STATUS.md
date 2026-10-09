# Proxy status

Generated 2026-10-09T23:28:38Z by `harvest.py`.

- **1876** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3541** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39575** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 162/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2139 |
| socks5 | 1388 |
| socks4 | 14 |

| country | entries |
|---|---|
| NL | 1177 |
| ID | 624 |
| ?? | 205 |
| PH | 104 |
| US | 94 |
| CO | 92 |
| MX | 83 |
| RU | 81 |
| CN | 74 |
| BR | 62 |
| BD | 60 |
| VE | 55 |
| EC | 52 |
| IN | 50 |
| TR | 43 |
| VN | 42 |
| DO | 37 |
| DE | 35 |
| SG | 35 |
| AR | 30 |
| EG | 28 |
| PK | 28 |
| ZA | 23 |
| JP | 22 |
| PE | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 2 | 2026-10-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 105 | 105 | 44 | 2026-10-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 147 | 147 | 73 | 2026-10-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 80 | 2026-10-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 202 | 202 | 94 | 2026-10-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 273 | 273 | 90 | 2026-10-09 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 446 | 446 | 176 | 2026-10-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-10-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 692 | 692 | 403 | 2026-10-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 939 | 939 | 212 | 2026-10-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1123 | 2026-10-09 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1729 | 1725 | 0 | 2026-10-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1595 | 2026-10-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2356 | 2354 | 1714 | 2026-10-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2403 | 2401 | 749 | 2026-10-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2437 | 2435 | 475 | 2026-10-09 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 47498 | 47498 | 31820 | 2026-10-09 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 54319 | 54318 | 2951 | 2026-10-09 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1085 | 40 | 107/120 |
| http://34.43.46.91:80 | US | 876 | 37 | 116/120 |
| http://190.0.246.210:4040 | CO | 1147 | 36 | 108/119 |
| http://149.130.173.58:9443 | CO | 650 | 31 | 31/31 |
| http://43.173.120.13:8899 | US | 494 | 31 | 31/31 |
| http://190.0.246.213:4040 | CO | 711 | 14 | 77/85 |
| http://144.124.251.24:10008 | NL | 825 | 14 | 42/51 |
| http://144.124.251.24:10088 | NL | 783 | 14 | 41/52 |
| http://144.124.251.24:10176 | NL | 944 | 14 | 46/68 |
| http://144.124.251.24:10185 | NL | 931 | 14 | 43/52 |
| http://144.124.251.24:10216 | NL | 791 | 14 | 47/69 |
| http://144.124.251.24:10226 | NL | 820 | 14 | 41/51 |
| http://144.124.251.24:10230 | NL | 820 | 14 | 45/67 |
| http://144.124.251.24:10261 | NL | 799 | 14 | 42/52 |
| http://144.124.251.24:10299 | NL | 827 | 14 | 41/52 |
| http://144.124.251.24:10333 | NL | 1073 | 14 | 45/69 |
| http://144.124.251.24:10337 | NL | 816 | 14 | 40/52 |
| http://144.124.251.24:10366 | NL | 1013 | 14 | 43/66 |
| http://144.124.251.24:10372 | NL | 802 | 14 | 46/64 |
| http://144.124.251.24:10453 | NL | 837 | 14 | 45/57 |
| http://144.124.251.24:10471 | NL | 799 | 14 | 46/67 |
| http://144.124.251.24:10551 | NL | 843 | 14 | 47/68 |
| http://144.124.251.24:10574 | NL | 799 | 14 | 47/69 |
| http://144.124.251.24:10601 | NL | 2463 | 14 | 40/67 |
| http://144.124.251.24:10628 | NL | 826 | 14 | 40/52 |
| http://144.124.251.24:10631 | NL | 830 | 14 | 42/52 |
| http://144.124.251.24:10689 | NL | 825 | 14 | 43/56 |
| http://144.124.251.24:10771 | NL | 978 | 14 | 42/52 |
| http://144.124.251.24:10811 | NL | 773 | 14 | 42/52 |
| http://144.124.251.24:10829 | NL | 800 | 14 | 40/52 |
| http://144.124.251.24:11011 | NL | 788 | 14 | 43/52 |
| http://144.124.251.24:11108 | NL | 949 | 14 | 43/67 |
| http://144.124.251.24:11124 | NL | 783 | 14 | 44/69 |
| http://144.124.251.24:11180 | NL | 845 | 14 | 41/51 |
| http://144.124.251.24:11265 | NL | 776 | 14 | 46/68 |
| http://197.224.185.3:3128 | MU | 2081 | 12 | 81/88 |
| socks5://160.187.0.89:1080 | VN | 1959 | 11 | 26/33 |
| http://176.111.37.5:39811 | HK | 1156 | 10 | 102/120 |
| http://176.111.37.216:39811 | HK | 1227 | 10 | 99/120 |
| http://34.88.38.81:9443 | FI | 871 | 9 | 59/85 |
| http://35.228.49.168:9443 | FI | 874 | 9 | 40/57 |
| http://195.158.8.123:3128 | UZ | 2100 | 9 | 79/118 |
| http://189.51.168.165:999 | MX | 565 | 8 | 30/32 |
| http://5.129.254.5:8888 | RU | 1364 | 8 | 65/75 |
| http://5.129.254.49:8888 | RU | 1446 | 8 | 66/75 |
| http://5.129.254.51:8888 | RU | 1432 | 8 | 66/75 |
| http://5.129.254.60:8888 | RU | 1261 | 8 | 65/74 |
| http://5.129.254.70:8888 | RU | 1446 | 8 | 66/75 |
| http://5.129.254.129:8888 | RU | 1371 | 8 | 71/81 |
| http://5.129.254.154:8888 | RU | 1304 | 8 | 62/71 |
| http://5.129.254.215:8888 | RU | 1332 | 8 | 15/17 |
| http://5.129.254.243:8888 | RU | 1392 | 8 | 15/16 |
| http://49.229.100.235:8080 | TH | 1233 | 8 | 40/68 |
| http://114.244.214.18:8888 | CN | 1047 | 7 | 23/43 |
| http://103.237.102.191:11111 | DE | 1136 | 7 | 113/120 |
| http://43.155.62.157:443 | HK | 1554 | 7 | 20/23 |
| http://128.199.116.219:9090 | SG | 884 | 7 | 32/39 |
| http://61.91.162.126:8080 | TH | 1211 | 7 | 49/63 |
| http://103.10.231.189:8080 | TH | 1220 | 7 | 74/105 |
| socks5://101.36.104.239:10808 | JP | 6692 | 7 | 102/120 |
| http://102.244.78.61:8081 | CM | 1562 | 6 | 6/6 |
| http://85.239.156.66:5555 | CZ | 1143 | 6 | 7/9 |
| http://144.124.251.24:10084 | NL | 961 | 6 | 40/52 |
| socks5://164.68.114.118:1080 | FR | 1221 | 6 | 6/6 |
| socks5://67.207.92.87:1088 | US | 675 | 6 | 66/119 |
| http://101.251.204.174:8080 | CN | 1429 | 5 | 59/106 |
| http://186.5.94.206:999 | EC | 1859 | 5 | 75/82 |
| http://187.201.225.188:999 | MX | 465 | 5 | 5/5 |
| http://152.42.177.32:8888 | SG | 895 | 5 | 47/80 |
| http://154.59.56.72:999 | VE | 4202 | 5 | 55/79 |
| http://154.59.56.78:999 | VE | 5259 | 5 | 53/76 |
| socks5://45.155.71.236:1080 | AT | 1020 | 5 | 13/25 |
| socks5://103.75.118.84:1080 | JP | 1807 | 5 | 84/115 |
| socks5://45.74.31.41:12929 | NL | 3682 | 5 | 9/35 |
| socks5://79.137.198.71:7777 | NL | 4258 | 5 | 15/20 |
| socks5://85.209.156.148:1080 | US | 2578 | 5 | 53/91 |
| socks5://129.153.11.56:1080 | US | 3495 | 5 | 18/25 |
| http://18.230.23.72:25761 | BR | 2120 | 4 | 21/80 |
| http://200.128.84.82:3128 | BR | 890 | 4 | 9/13 |
| http://221.221.162.6:8888 | CN | 1293 | 4 | 9/18 |
| http://181.78.195.137:999 | EC | 5856 | 4 | 31/120 |
| http://200.24.153.151:999 | EC | 1681 | 4 | 16/102 |
| http://198.244.254.77:3128 | GB | 2454 | 4 | 4/4 |
| http://65.20.79.228:40002 | IN | 1328 | 4 | 6/8 |
| http://38.172.160.16:999 | VE | 5094 | 4 | 43/71 |
| socks4://27.69.68.185:1033 | VN | 1823 | 4 | 4/4 |
| socks4://27.69.77.5:1033 | VN | 4550 | 4 | 4/4 |
| socks5://36.155.23.163:10808 | CN | 1268 | 4 | 28/57 |
| socks5://49.13.22.249:10805 | DE | 2166 | 4 | 23/38 |
| socks5://212.77.75.25:1088 | IT | 1616 | 4 | 18/20 |
| socks5://45.74.31.40:6300 | NL | 4553 | 4 | 4/4 |
| socks5://45.74.31.40:6308 | NL | 3555 | 4 | 4/4 |
| socks5://62.245.48.172:1080 | RU | 5455 | 4 | 8/34 |
| socks5://171.25.158.95:1080 | SE | 3398 | 4 | 29/35 |
| http://18.230.23.72:26881 | BR | 4332 | 3 | 10/36 |
| http://18.231.214.206:14559 | BR | 2274 | 3 | 22/98 |
| http://54.20.46.218:3128 | BR | 3902 | 3 | 16/30 |
| http://38.7.195.49:999 | CL | 6272 | 3 | 40/94 |
| http://113.45.195.147:3128 | CN | 2599 | 3 | 55/85 |
| http://186.31.197.3:8080 | CO | 6924 | 3 | 6/31 |
