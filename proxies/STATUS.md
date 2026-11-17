# Proxy status

Generated 2026-11-17T02:36:37Z by `harvest.py`.

- **1614** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3600** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **31786** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 105/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2578 |
| socks5 | 1009 |
| socks4 | 13 |

| country | entries |
|---|---|
| ID | 812 |
| NL | 780 |
| ?? | 264 |
| CO | 118 |
| PH | 118 |
| US | 116 |
| MX | 114 |
| TR | 85 |
| BR | 77 |
| VE | 69 |
| TH | 67 |
| BD | 63 |
| RU | 59 |
| IN | 55 |
| EC | 44 |
| DO | 40 |
| CN | 39 |
| AR | 37 |
| SG | 34 |
| VN | 34 |
| CA | 33 |
| ZA | 32 |
| PK | 31 |
| DE | 29 |
| EG | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 11 | 11 | 5 | 2026-11-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 106 | 106 | 20 | 2026-11-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 113 | 113 | 22 | 2026-11-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 122 | 122 | 50 | 2026-11-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 130 | 130 | 31 | 2026-11-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 59 | 2026-11-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 156 | 156 | 16 | 2026-11-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 313 | 313 | 208 | 2026-11-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 578 | 578 | 89 | 2026-11-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-11-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1132 | 2026-11-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1808 | 1808 | 666 | 2026-11-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1842 | 1842 | 336 | 2026-11-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2223 | 2223 | 1252 | 2026-11-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2251 | 2251 | 726 | 2026-11-17 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5437 | 5437 | 4227 | 2026-11-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11685 | 11685 | 2008 | 2026-11-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1833 | 67 | 177/196 |
| http://130.110.103.245:3128 | SA | 1788 | 42 | 178/196 |
| http://45.186.6.104:3128 | EC | 913 | 26 | 165/174 |
| http://38.180.18.103:3128 | BE | 848 | 25 | 25/25 |
| http://27.147.155.206:12051 | BD | 1898 | 16 | 16/16 |
| http://177.234.217.235:999 | EC | 2541 | 10 | 86/165 |
| http://104.129.203.85:9480 | US | 247 | 10 | 10/10 |
| http://141.94.22.37:3128 | FR | 784 | 8 | 11/12 |
| http://188.166.178.163:3129 | SG | 950 | 8 | 8/8 |
| socks5://37.18.73.60:5566 | RU | 1464 | 8 | 44/93 |
| socks5://188.166.178.163:1088 | SG | 1663 | 8 | 8/8 |
| socks5://116.101.73.52:1057 | VN | 3987 | 8 | 8/8 |
| http://45.65.138.48:999 | CO | 3852 | 6 | 96/196 |
| http://190.71.72.85:2525 | CO | 842 | 6 | 39/81 |
| socks5://107.174.30.92:1080 | US | 566 | 6 | 52/92 |
| http://102.244.78.61:8083 | CM | 1424 | 5 | 67/84 |
| http://102.244.78.61:8084 | CM | 1460 | 5 | 65/84 |
| http://102.244.78.61:8086 | CM | 1439 | 5 | 66/84 |
| http://102.244.78.61:8089 | CM | 1457 | 5 | 68/84 |
| http://190.12.150.244:999 | EC | 5863 | 5 | 142/192 |
| http://45.155.226.177:3128 | HK | 3094 | 5 | 10/12 |
| http://103.176.96.32:8082 | ID | 5491 | 5 | 47/189 |
| http://148.230.4.146:999 | MX | 4975 | 5 | 54/188 |
| http://211.188.50.146:80 | ?? | 671 | 5 | 5/5 |
| http://211.188.53.248:80 | ?? | 5886 | 5 | 5/5 |
| http://211.188.55.218:80 | ?? | 686 | 5 | 5/5 |
| http://211.188.59.191:80 | ?? | 2150 | 5 | 5/5 |
| http://211.188.60.84:80 | ?? | 729 | 5 | 5/5 |
| socks5://193.218.118.128:1080 | UA | 3003 | 5 | 37/52 |
| socks5://47.251.166.203:1080 | US | 165 | 5 | 9/14 |
| http://102.244.78.61:8080 | CM | 1428 | 4 | 69/85 |
| http://102.244.78.61:8088 | CM | 1467 | 4 | 66/84 |
| http://120.28.200.84:5050 | PH | 4766 | 4 | 27/116 |
| http://126.209.110.120:8087 | PH | 5179 | 4 | 28/164 |
| http://180.191.228.36:8082 | PH | 3836 | 4 | 21/106 |
| socks5://101.36.104.46:10808 | JP | 1187 | 4 | 163/196 |
| http://102.244.78.61:8081 | CM | 1457 | 3 | 66/82 |
| http://102.244.78.61:8082 | CM | 1436 | 3 | 67/85 |
| http://102.244.78.61:8085 | CM | 1461 | 3 | 67/86 |
| http://102.244.78.61:8087 | CM | 1458 | 3 | 64/86 |
| http://102.244.78.61:8090 | CM | 1468 | 3 | 70/88 |
| http://123.121.122.125:8888 | CN | 1888 | 3 | 12/19 |
| http://124.128.149.84:8090 | CN | 3724 | 3 | 14/30 |
| http://177.234.217.82:999 | EC | 6704 | 3 | 30/93 |
| http://177.234.217.85:999 | EC | 4166 | 3 | 27/51 |
| http://177.234.217.89:999 | EC | 2934 | 3 | 11/21 |
| http://183.178.50.58:8080 | HK | 4645 | 3 | 7/30 |
| http://181.78.44.63:999 | HN | 4740 | 3 | 46/120 |
| http://103.51.205.114:8082 | ID | 5876 | 3 | 42/132 |
| http://103.80.82.7:8181 | ID | 7372 | 3 | 31/165 |
| http://103.146.38.107:1111 | ID | 3792 | 3 | 32/130 |
| http://103.191.165.171:8181 | ID | 7855 | 3 | 35/155 |
| http://165.101.231.22:8080 | ID | 2074 | 3 | 12/38 |
| http://15.152.38.117:48871 | JP | 2989 | 3 | 41/160 |
| http://43.165.169.48:80 | JP | 844 | 3 | 8/13 |
| http://88.119.139.237:53281 | LT | 2044 | 3 | 5/18 |
| http://45.174.242.145:999 | MX | 7341 | 3 | 43/151 |
| http://82.152.138.127:999 | MX | 747 | 3 | 69/158 |
| http://209.14.108.59:999 | PE | 5857 | 3 | 9/57 |
| http://119.93.207.214:8082 | PH | 6775 | 3 | 49/188 |
| http://91.234.96.45:9001 | RU | 4710 | 3 | 36/186 |
| http://4.144.146.21:80 | SG | 861 | 3 | 79/88 |
| http://128.199.254.13:9090 | SG | 903 | 3 | 78/125 |
| http://167.99.74.174:9090 | SG | 956 | 3 | 103/156 |
| http://1.10.248.239:80 | TH | 6030 | 3 | 16/42 |
| http://49.229.100.235:8080 | TH | 1385 | 3 | 102/144 |
| http://171.100.254.137:8080 | TH | 1178 | 3 | 30/32 |
| http://18.222.28.236:46232 | US | 2488 | 3 | 25/67 |
| http://216.152.149.246:80 | US | 2965 | 3 | 7/8 |
| http://38.7.17.83:999 | ?? | 5988 | 3 | 5/10 |
| http://103.136.200.129:8080 | ?? | 4873 | 3 | 3/3 |
| http://116.101.73.52:2045 | ?? | 2618 | 3 | 3/3 |
| socks4://188.226.27.24:1080 | RU | 4452 | 3 | 23/32 |
| socks5://45.194.33.12:30002 | HK | 1060 | 3 | 23/40 |
| socks5://102.0.14.42:1080 | KE | 4084 | 3 | 19/104 |
| socks5://5.255.99.75:1080 | NL | 916 | 3 | 60/171 |
| socks5://209.50.255.91:1080 | US | 3002 | 3 | 52/113 |
| socks5://116.101.73.161:1085 | VN | 5844 | 3 | 6/7 |
| socks5://27.74.14.60:5001 | ?? | 4253 | 3 | 3/3 |
| socks5://95.216.45.44:10353 | ?? | 2695 | 3 | 3/3 |
| http://79.106.79.154:8989 | AL | 1351 | 2 | 39/152 |
| http://79.106.229.115:8989 | AL | 4552 | 2 | 10/30 |
| http://168.194.34.196:9001 | AR | 4022 | 2 | 74/194 |
| http://187.102.219.32:999 | AR | 3798 | 2 | 75/195 |
| http://16.51.53.116:1011 | AU | 5546 | 2 | 8/25 |
| http://159.196.182.72:8080 | AU | 2834 | 2 | 19/103 |
| http://27.147.152.50:12051 | BD | 5480 | 2 | 6/14 |
| http://103.76.44.175:8090 | BD | 5619 | 2 | 10/30 |
| http://103.150.49.90:8090 | BD | 6139 | 2 | 41/189 |
| http://87.126.65.11:1388 | BG | 6482 | 2 | 10/32 |
| http://15.229.149.81:3128 | BR | 2280 | 2 | 68/106 |
| http://18.231.126.121:1082 | BR | 3563 | 2 | 20/136 |
| http://45.233.90.10:443 | BR | 6404 | 2 | 38/183 |
| http://131.0.120.162:9292 | BR | 6563 | 2 | 21/85 |
| http://138.0.143.120:8080 | BR | 5167 | 2 | 30/150 |
| http://170.245.120.179:3128 | BR | 5827 | 2 | 34/192 |
| http://179.48.25.1:8095 | BR | 7095 | 2 | 39/191 |
| http://179.125.61.201:8080 | BR | 2122 | 2 | 9/27 |
| http://200.182.232.34:80 | BR | 1877 | 2 | 5/29 |
| http://16.52.81.236:30468 | CA | 2745 | 2 | 22/108 |
