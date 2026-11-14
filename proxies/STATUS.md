# Proxy status

Generated 2026-11-14T00:27:36Z by `harvest.py`.

- **1594** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3341** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34372** endpoints on record
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
| http | 2704 |
| socks5 | 620 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 741 |
| NL | 465 |
| ?? | 235 |
| PH | 144 |
| US | 135 |
| MX | 124 |
| CO | 123 |
| CN | 96 |
| BR | 87 |
| TH | 81 |
| VE | 79 |
| TR | 72 |
| BD | 59 |
| RU | 54 |
| AR | 51 |
| IN | 50 |
| EC | 49 |
| VN | 36 |
| ZA | 34 |
| CA | 33 |
| SG | 32 |
| DE | 31 |
| DO | 31 |
| PE | 30 |
| PK | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 82 | 82 | 6 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 87 | 87 | 9 | 2026-11-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 145 | 145 | 69 | 2026-11-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 34 | 2026-11-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 62 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 168 | 168 | 23 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 377 | 377 | 261 | 2026-11-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 529 | 529 | 77 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 444 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1122 | 2026-11-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1719 | 1719 | 135 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2182 | 2182 | 412 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2236 | 2236 | 669 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2545 | 2545 | 1374 | 2026-11-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5338 | 5338 | 4089 | 2026-11-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11214 | 11214 | 1873 | 2026-11-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 2684 | 61 | 171/190 |
| http://34.43.46.91:80 | US | 713 | 60 | 184/190 |
| http://4.144.146.21:80 | SG | 1457 | 58 | 75/82 |
| http://176.111.37.216:39811 | HK | 1428 | 53 | 162/190 |
| http://130.110.103.245:3128 | SA | 1524 | 36 | 172/190 |
| http://45.189.57.114:3129 | EC | 3174 | 32 | 32/32 |
| http://45.186.6.104:3128 | EC | 891 | 20 | 159/168 |
| http://38.180.18.103:3128 | BE | 1881 | 19 | 19/19 |
| http://102.244.78.61:8090 | CM | 1820 | 17 | 66/82 |
| socks5://121.46.226.221:10808 | CN | 3187 | 16 | 16/16 |
| http://43.155.62.157:443 | HK | 3640 | 13 | 80/93 |
| http://185.191.239.248:3128 | CH | 2526 | 11 | 139/189 |
| http://27.147.155.206:12051 | BD | 1780 | 10 | 10/10 |
| http://51.85.44.162:31819 | IL | 6023 | 9 | 27/42 |
| http://45.65.224.74:999 | AR | 3882 | 8 | 46/55 |
| http://140.238.32.108:3128 | JP | 2078 | 8 | 110/189 |
| http://144.124.251.24:10605 | NL | 513 | 8 | 77/122 |
| http://144.124.251.24:11266 | NL | 576 | 8 | 79/122 |
| http://128.199.116.219:9090 | SG | 1295 | 6 | 85/109 |
| http://167.172.76.176:9090 | SG | 1294 | 6 | 110/151 |
| http://35.43.85.195:443 | ?? | 4641 | 6 | 6/6 |
| http://85.132.108.42:3128 | AZ | 6092 | 5 | 7/8 |
| http://102.244.78.61:8085 | CM | 2090 | 5 | 63/80 |
| http://102.244.78.61:8088 | CM | 1507 | 5 | 62/78 |
| http://123.121.73.146:8888 | CN | 2202 | 5 | 8/12 |
| http://198.244.254.77:3128 | GB | 5976 | 5 | 62/74 |
| http://185.166.27.208:2020 | IQ | 6798 | 5 | 17/24 |
| http://180.191.121.186:8181 | PH | 3863 | 5 | 16/27 |
| http://128.199.121.61:9090 | SG | 1569 | 5 | 84/110 |
| http://89.104.102.209:58080 | UZ | 7443 | 5 | 26/134 |
| http://38.63.98.32:999 | VE | 5793 | 5 | 29/78 |
| http://16.26.208.68:1256 | AU | 2986 | 4 | 31/130 |
| http://102.244.78.61:8081 | CM | 1636 | 4 | 62/76 |
| http://102.244.78.61:8083 | CM | 2006 | 4 | 62/78 |
| http://102.244.78.61:8087 | CM | 1532 | 4 | 60/80 |
| http://101.251.204.174:8080 | CN | 1935 | 4 | 97/176 |
| http://111.192.30.181:8888 | CN | 2915 | 4 | 6/10 |
| http://221.221.164.42:8888 | CN | 3463 | 4 | 8/13 |
| http://177.234.217.235:999 | EC | 7607 | 4 | 80/159 |
| http://103.158.210.80:8082 | ID | 6968 | 4 | 57/180 |
| http://103.227.187.3:6090 | ID | 6176 | 4 | 23/100 |
| http://144.124.251.24:10412 | NL | 589 | 4 | 68/122 |
| http://144.124.251.24:10453 | NL | 680 | 4 | 78/127 |
| http://144.124.251.24:10610 | NL | 610 | 4 | 73/122 |
| http://144.124.251.24:10631 | NL | 583 | 4 | 74/122 |
| http://112.208.174.83:8080 | PH | 5275 | 4 | 31/76 |
| http://82.138.122.43:80 | TR | 6373 | 4 | 40/154 |
| http://161.22.32.31:8080 | VE | 7749 | 4 | 35/68 |
| http://51.68.102.5:3128 | ?? | 3646 | 4 | 4/4 |
| http://57.182.226.41:3128 | ?? | 2480 | 4 | 4/4 |
| http://104.129.203.85:9480 | ?? | 2032 | 4 | 4/4 |
| http://119.12.161.248:3128 | ?? | 1619 | 4 | 4/4 |
| http://154.0.157.196:8080 | ?? | 4055 | 4 | 4/4 |
| http://172.235.147.5:3128 | ?? | 7393 | 4 | 4/4 |
| socks5://45.194.33.12:30002 | HK | 3495 | 4 | 18/34 |
| socks5://95.31.115.101:9150 | RU | 2367 | 4 | 9/10 |
| socks5://202.61.239.148:8383 | ?? | 990 | 4 | 4/4 |
| http://103.187.136.9:3838 | BD | 7273 | 3 | 5/13 |
| http://102.244.78.61:8080 | CM | 1621 | 3 | 65/79 |
| http://102.244.78.61:8082 | CM | 1957 | 3 | 64/79 |
| http://102.244.78.61:8086 | CM | 1825 | 3 | 61/78 |
| http://114.249.209.219:8888 | CN | 7466 | 3 | 57/148 |
| http://114.249.226.92:8888 | CN | 1891 | 3 | 8/12 |
| http://123.112.162.30:8888 | CN | 6303 | 3 | 9/19 |
| http://123.119.24.241:8888 | CN | 2406 | 3 | 50/125 |
| http://123.119.25.143:8888 | CN | 1584 | 3 | 70/155 |
| http://123.121.114.234:8888 | CN | 2570 | 3 | 44/149 |
| http://221.221.156.167:8888 | CN | 2968 | 3 | 8/14 |
| http://24.152.58.101:999 | CO | 4799 | 3 | 25/84 |
| http://181.188.203.40:999 | EC | 2363 | 3 | 40/87 |
| http://186.33.41.48:999 | EC | 2052 | 3 | 19/63 |
| http://154.236.179.229:1981 | EG | 2239 | 3 | 38/108 |
| http://13.38.27.183:26602 | FR | 2068 | 3 | 41/190 |
| http://138.118.107.29:999 | GT | 4644 | 3 | 10/52 |
| http://103.39.51.157:1080 | ID | 2900 | 3 | 31/120 |
| http://103.97.140.17:8080 | ID | 5869 | 3 | 17/31 |
| http://103.125.212.28:8080 | ID | 6427 | 3 | 23/147 |
| http://103.147.134.203:8080 | ID | 7331 | 3 | 6/8 |
| http://103.237.134.242:7777 | ID | 4710 | 3 | 5/15 |
| http://151.158.133.145:8080 | ID | 3495 | 3 | 10/23 |
| http://151.158.133.147:8080 | ID | 4187 | 3 | 18/43 |
| http://157.10.97.101:8181 | ID | 4772 | 3 | 37/168 |
| http://111.118.149.40:8080 | KH | 5064 | 3 | 18/53 |
| http://82.152.138.127:999 | MX | 523 | 3 | 64/152 |
| http://206.135.47.110:999 | MX | 6197 | 3 | 33/61 |
| http://144.124.251.24:10216 | NL | 746 | 3 | 83/139 |
| http://144.124.251.24:10299 | NL | 607 | 3 | 70/122 |
| http://144.124.251.24:10333 | NL | 676 | 3 | 76/139 |
| http://144.124.251.24:10590 | NL | 673 | 3 | 13/41 |
| http://144.124.251.24:11124 | NL | 1023 | 3 | 76/139 |
| http://144.124.251.24:11480 | NL | 490 | 3 | 71/122 |
| http://58.69.124.137:8080 | PH | 5793 | 3 | 50/189 |
| http://115.147.16.205:5050 | PH | 6733 | 3 | 34/155 |
| http://146.190.80.158:9090 | SG | 1318 | 3 | 82/116 |
| http://61.19.30.194:8188 | TH | 4668 | 3 | 12/51 |
| http://184.22.3.3:8080 | TH | 7810 | 3 | 5/8 |
| http://201.7.31.43:8080 | TR | 4137 | 3 | 11/43 |
| http://90.156.160.234:3128 | UZ | 3429 | 3 | 34/78 |
| http://13.245.183.150:43236 | ZA | 4417 | 3 | 7/20 |
| http://185.145.4.8:8080 | ?? | 4639 | 3 | 4/6 |
