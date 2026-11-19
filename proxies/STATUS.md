# Proxy status

Generated 2026-11-19T01:28:17Z by `harvest.py`.

- **1939** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3725** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **27927** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 140/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2967 |
| socks5 | 740 |
| socks4 | 18 |

| country | entries |
|---|---|
| ID | 933 |
| NL | 519 |
| ?? | 330 |
| PH | 167 |
| CO | 133 |
| MX | 128 |
| US | 113 |
| TR | 82 |
| TH | 79 |
| BR | 77 |
| VE | 77 |
| IN | 73 |
| BD | 64 |
| RU | 61 |
| VN | 56 |
| EC | 51 |
| AR | 50 |
| CN | 49 |
| DO | 37 |
| ZA | 35 |
| PK | 34 |
| EG | 30 |
| SG | 29 |
| DE | 28 |
| KH | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 1 | 2026-11-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 140 | 140 | 18 | 2026-11-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 32 | 2026-11-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 56 | 2026-11-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 305 | 305 | 205 | 2026-11-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 321 | 321 | 89 | 2026-11-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 354 | 354 | 39 | 2026-11-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 361 | 361 | 140 | 2026-11-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-11-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 809 | 809 | 96 | 2026-11-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1423 | 1423 | 134 | 2026-11-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1128 | 2026-11-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2211 | 2211 | 420 | 2026-11-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2313 | 2313 | 714 | 2026-11-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2553 | 2553 | 1478 | 2026-11-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5523 | 5523 | 4309 | 2026-11-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11561 | 11561 | 1856 | 2026-11-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 977 | 71 | 181/200 |
| http://130.110.103.245:3128 | SA | 1344 | 46 | 182/200 |
| http://38.180.18.103:3128 | BE | 772 | 29 | 29/29 |
| http://27.147.155.206:12051 | BD | 2022 | 20 | 20/20 |
| http://141.94.22.37:3128 | FR | 804 | 12 | 15/16 |
| socks5://37.18.73.60:5566 | RU | 1289 | 12 | 48/97 |
| http://45.65.138.48:999 | CO | 5163 | 10 | 100/200 |
| http://102.244.78.61:8084 | CM | 1351 | 9 | 69/88 |
| http://102.244.78.61:8089 | CM | 1384 | 9 | 72/88 |
| http://45.155.226.177:3128 | HK | 749 | 9 | 14/16 |
| http://102.244.78.61:8080 | CM | 1310 | 8 | 73/89 |
| http://102.244.78.61:8088 | CM | 1342 | 8 | 70/88 |
| http://102.244.78.61:8081 | CM | 1353 | 7 | 70/86 |
| http://102.244.78.61:8082 | CM | 1371 | 7 | 71/89 |
| http://102.244.78.61:8085 | CM | 1341 | 7 | 71/90 |
| http://102.244.78.61:8087 | CM | 1336 | 7 | 68/90 |
| http://102.244.78.61:8090 | CM | 1306 | 7 | 74/92 |
| http://177.234.217.89:999 | EC | 7228 | 7 | 15/25 |
| http://43.165.169.48:80 | JP | 2342 | 7 | 12/17 |
| http://4.144.146.21:80 | SG | 1308 | 7 | 83/92 |
| http://167.99.74.174:9090 | SG | 940 | 7 | 107/160 |
| http://216.152.149.246:80 | US | 4102 | 7 | 11/12 |
| http://15.229.149.81:3128 | BR | 2400 | 6 | 72/110 |
| http://43.161.254.16:3128 | HK | 1277 | 6 | 34/40 |
| http://52.128.238.98:18080 | HK | 127 | 6 | 11/15 |
| http://103.156.75.89:1717 | ID | 6258 | 6 | 13/24 |
| http://185.238.236.226:58080 | PL | 1880 | 6 | 59/122 |
| http://128.199.121.61:9090 | SG | 957 | 6 | 93/120 |
| http://216.152.152.44:80 | US | 2403 | 6 | 9/12 |
| socks5://193.25.215.182:22222 | US | 567 | 6 | 165/200 |
| http://184.75.221.82:3118 | CA | 429 | 5 | 143/165 |
| http://103.130.61.61:8081 | ID | 1491 | 5 | 165/200 |
| http://192.147.114.23:3127 | ID | 4798 | 5 | 40/134 |
| http://192.232.48.21:8181 | ID | 6507 | 5 | 20/106 |
| http://34.43.46.91:443 | US | 1142 | 5 | 185/200 |
| http://34.43.46.91:80 | US | 1246 | 5 | 193/200 |
| http://161.22.32.31:8080 | VE | 3218 | 5 | 42/78 |
| http://195.154.176.34:3128 | ?? | 711 | 5 | 5/5 |
| socks5://45.61.129.165:9050 | US | 1687 | 5 | 152/200 |
| socks5://46.246.12.31:1080 | ?? | 6001 | 5 | 5/5 |
| http://190.123.83.137:999 | AR | 1142 | 4 | 31/37 |
| http://103.92.218.121:9514 | BD | 3437 | 4 | 33/136 |
| http://15.229.149.81:1080 | BR | 2036 | 4 | 56/102 |
| http://177.234.217.93:999 | EC | 6040 | 4 | 42/59 |
| http://43.155.62.157:443 | HK | 1148 | 4 | 87/103 |
| http://36.50.56.237:8080 | ID | 2076 | 4 | 27/107 |
| http://103.20.191.118:8080 | ID | 7192 | 4 | 49/165 |
| http://103.98.117.26:8080 | ID | 4044 | 4 | 14/34 |
| http://103.158.127.17:57413 | ID | 3818 | 4 | 44/178 |
| http://103.176.96.225:8082 | ID | 1211 | 4 | 50/145 |
| http://103.231.236.217:8182 | ID | 5454 | 4 | 9/23 |
| http://121.101.133.96:8080 | ID | 2542 | 4 | 28/108 |
| http://157.66.16.63:8181 | ID | 3514 | 4 | 8/29 |
| http://160.22.198.17:8082 | ID | 6788 | 4 | 53/192 |
| http://187.251.224.167:80 | MX | 1265 | 4 | 59/196 |
| http://189.51.168.164:999 | MX | 2335 | 4 | 32/36 |
| http://189.51.168.165:999 | MX | 2034 | 4 | 101/112 |
| http://49.149.24.144:8082 | PH | 3549 | 4 | 19/39 |
| http://103.239.201.50:1 | PH | 1862 | 4 | 9/29 |
| http://119.93.178.99:8081 | PH | 7569 | 4 | 13/106 |
| http://104.248.151.93:9090 | SG | 948 | 4 | 69/101 |
| http://20.98.234.24:8080 | ?? | 363 | 4 | 4/4 |
| http://132.243.174.245:5002 | ?? | 769 | 4 | 4/4 |
| socks4://103.13.19.219:10808 | JP | 1322 | 4 | 10/17 |
| socks5://45.74.31.47:4586 | NL | 6678 | 4 | 4/4 |
| socks5://69.55.49.177:38182 | US | 506 | 4 | 44/55 |
| http://27.147.142.156:12051 | BD | 3190 | 3 | 15/28 |
| http://27.147.153.179:12051 | BD | 3872 | 3 | 12/20 |
| http://103.79.183.109:8080 | BD | 4692 | 3 | 24/57 |
| http://138.59.233.59:8080 | BR | 6419 | 3 | 23/106 |
| http://123.121.140.72:8888 | CN | 1509 | 3 | 30/52 |
| http://38.19.43.184:999 | CO | 4866 | 3 | 52/184 |
| http://186.96.111.214:999 | CO | 3017 | 3 | 95/189 |
| http://103.237.102.191:11111 | DE | 761 | 3 | 187/200 |
| http://38.253.84.67:999 | DO | 6916 | 3 | 7/16 |
| http://177.234.217.43:999 | EC | 2119 | 3 | 61/173 |
| http://51.94.221.175:1857 | ES | 1423 | 3 | 40/141 |
| http://34.105.252.3:3128 | GB | 726 | 3 | 49/82 |
| http://198.244.254.77:3128 | GB | 2316 | 3 | 67/84 |
| http://102.164.252.150:8080 | GQ | 4599 | 3 | 64/159 |
| http://36.95.245.7:8090 | ID | 4339 | 3 | 13/38 |
| http://103.61.234.186:8180 | ID | 2963 | 3 | 88/197 |
| http://103.76.107.2:8085 | ID | 7660 | 3 | 10/97 |
| http://103.132.54.42:8080 | ID | 4774 | 3 | 29/109 |
| http://103.133.24.5:8080 | ID | 4088 | 3 | 23/98 |
| http://103.146.38.53:1080 | ID | 4254 | 3 | 23/110 |
| http://103.147.134.79:8082 | ID | 7251 | 3 | 18/40 |
| http://103.156.75.42:8989 | ID | 4029 | 3 | 14/33 |
| http://103.210.119.155:1080 | ID | 6605 | 3 | 17/50 |
| http://154.18.255.118:1111 | ID | 6392 | 3 | 18/40 |
| http://160.22.198.19:8082 | ID | 7248 | 3 | 22/55 |
| http://163.227.168.130:8080 | ID | 5065 | 3 | 9/28 |
| http://202.154.19.119:8090 | ID | 2872 | 3 | 12/87 |
| http://210.87.74.189:3125 | ID | 2548 | 3 | 8/24 |
| http://51.85.44.162:31819 | IL | 4513 | 3 | 32/52 |
| http://103.137.218.113:83 | IN | 5760 | 3 | 17/113 |
| http://140.227.61.201:3128 | JP | 3766 | 3 | 61/192 |
| http://36.37.251.137:8080 | KH | 4575 | 3 | 18/86 |
| http://38.123.74.98:999 | MX | 3708 | 3 | 19/62 |
| http://201.46.86.37:8080 | MX | 1818 | 3 | 10/34 |
