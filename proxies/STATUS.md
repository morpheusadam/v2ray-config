# Proxy status

Generated 2026-11-01T18:39:29Z by `harvest.py`.

- **2871** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5647** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33545** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 198/600 (33%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2831 |
| http | 2806 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 2585 |
| ID | 729 |
| ?? | 658 |
| CO | 117 |
| MX | 112 |
| PH | 110 |
| US | 90 |
| BR | 78 |
| TH | 71 |
| VE | 69 |
| RU | 67 |
| BD | 64 |
| CN | 55 |
| TR | 54 |
| EC | 50 |
| IN | 49 |
| AR | 44 |
| DO | 39 |
| PK | 35 |
| SG | 31 |
| DE | 28 |
| PE | 27 |
| CA | 25 |
| EG | 24 |
| JP | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 5 | 2026-11-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 79 | 79 | 14 | 2026-11-01 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 51 | 2026-11-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 62 | 2026-11-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 255 | 255 | 58 | 2026-11-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 340 | 340 | 206 | 2026-11-01 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 546 | 546 | 230 | 2026-11-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-11-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-11-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1179 | 1179 | 358 | 2026-11-01 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1413 | 1413 | 207 | 2026-11-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1581 | 1581 | 804 | 2026-11-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-11-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1585 | 2026-11-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1946 | 1946 | 760 | 2026-11-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2293 | 2293 | 1358 | 2026-11-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2725 | 2725 | 935 | 2026-11-01 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4918 | 4918 | 3704 | 2026-11-01 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10776 | 10775 | 2418 | 2026-11-01 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2072 | 85 | 152/165 |
| http://149.130.173.58:9443 | CO | 494 | 76 | 76/76 |
| http://103.237.102.191:11111 | DE | 724 | 52 | 158/165 |
| http://103.133.26.73:3128 | ID | 2223 | 41 | 61/143 |
| http://176.111.37.5:39811 | HK | 1079 | 36 | 146/165 |
| http://34.43.46.91:80 | US | 3495 | 35 | 159/165 |
| http://4.144.146.21:80 | SG | 1094 | 33 | 50/57 |
| http://190.0.246.210:4040 | CO | 4002 | 32 | 151/164 |
| http://176.111.37.216:39811 | HK | 972 | 28 | 137/165 |
| http://34.43.46.91:443 | US | 779 | 14 | 154/165 |
| http://167.172.76.176:9090 | SG | 1091 | 12 | 89/126 |
| socks5://101.36.104.239:10808 | JP | 2179 | 12 | 141/165 |
| socks5://193.218.118.128:1080 | UA | 3873 | 12 | 18/21 |
| http://130.110.103.245:3128 | SA | 2113 | 11 | 147/165 |
| socks5://45.61.188.134:44499 | US | 968 | 11 | 67/132 |
| socks5://193.25.215.182:22222 | US | 952 | 11 | 138/165 |
| http://123.121.134.192:8888 | CN | 5052 | 9 | 16/31 |
| http://177.234.217.85:999 | EC | 5491 | 8 | 11/20 |
| http://103.133.26.72:8080 | ID | 1419 | 8 | 45/91 |
| http://123.121.209.108:8888 | CN | 4405 | 7 | 43/115 |
| http://81.19.210.10:80 | GB | 702 | 7 | 18/26 |
| http://154.59.56.78:999 | VE | 2392 | 7 | 84/121 |
| http://45.189.57.114:3129 | ?? | 714 | 7 | 7/7 |
| http://104.194.146.9:80 | ?? | 894 | 7 | 10/11 |
| socks5://202.62.42.92:1080 | KH | 1989 | 7 | 35/147 |
| socks5://107.174.30.92:1080 | US | 1253 | 7 | 32/61 |
| http://15.229.149.81:1080 | BR | 1958 | 6 | 30/67 |
| http://102.244.78.61:8085 | CM | 1366 | 6 | 43/55 |
| http://102.244.78.61:8087 | CM | 1452 | 6 | 42/55 |
| http://181.78.195.137:999 | EC | 3354 | 6 | 58/165 |
| http://45.43.60.220:8080 | JP | 1670 | 6 | 90/164 |
| http://102.68.76.247:5566 | KE | 4021 | 6 | 41/118 |
| http://159.223.41.216:9090 | SG | 1100 | 6 | 90/125 |
| socks5://37.18.73.60:5566 | RU | 1327 | 6 | 22/62 |
| socks5://23.141.116.9:9000 | ?? | 6156 | 6 | 9/17 |
| http://102.244.78.61:8090 | CM | 1238 | 5 | 43/57 |
| http://38.156.238.32:999 | DO | 3072 | 5 | 22/105 |
| http://101.255.209.166:8080 | ID | 6024 | 5 | 11/26 |
| http://115.147.254.250:6040 | PH | 4584 | 5 | 21/114 |
| http://120.28.200.84:5050 | PH | 5565 | 5 | 13/85 |
| http://103.253.18.6:8080 | PK | 5187 | 5 | 15/75 |
| http://185.238.238.165:58080 | PL | 4020 | 5 | 27/55 |
| http://38.172.160.16:999 | VE | 7289 | 5 | 68/116 |
| http://200.59.191.27:999 | VE | 4642 | 5 | 109/160 |
| http://130.127.204.197:8080 | ?? | 178 | 5 | 5/5 |
| socks5://65.21.252.66:10805 | FI | 2510 | 5 | 44/79 |
| socks5://207.180.217.98:1088 | ?? | 6299 | 5 | 5/5 |
| http://45.65.224.74:999 | AR | 5091 | 4 | 23/30 |
| http://123.200.8.170:10000 | BD | 7108 | 4 | 71/163 |
| http://102.244.78.61:8082 | CM | 1570 | 4 | 43/54 |
| http://102.244.78.61:8089 | CM | 1308 | 4 | 41/53 |
| http://111.196.30.74:8888 | CN | 7578 | 4 | 7/14 |
| http://217.76.245.80:999 | DO | 4344 | 4 | 33/121 |
| http://190.12.150.244:999 | EC | 1420 | 4 | 117/161 |
| http://103.82.246.19:6080 | ID | 2724 | 4 | 28/101 |
| http://111.95.161.133:8080 | ID | 6990 | 4 | 11/28 |
| http://144.124.251.24:10000 | NL | 629 | 4 | 69/111 |
| http://144.124.251.24:10574 | NL | 747 | 4 | 67/114 |
| http://144.124.251.24:11011 | NL | 591 | 4 | 60/97 |
| http://144.124.251.24:11265 | NL | 800 | 4 | 68/113 |
| http://119.159.233.2:8080 | PK | 5963 | 4 | 11/48 |
| http://185.238.238.21:58080 | PL | 4282 | 4 | 43/129 |
| http://185.238.238.49:58080 | PL | 5194 | 4 | 53/159 |
| http://185.238.238.113:58080 | PL | 4976 | 4 | 43/134 |
| http://152.42.177.32:8888 | SG | 1070 | 4 | 81/125 |
| http://1.20.101.24:80 | TH | 6859 | 4 | 11/34 |
| http://1.20.101.34:80 | TH | 3776 | 4 | 12/21 |
| http://47.254.36.25:11080 | US | 4330 | 4 | 46/107 |
| http://154.59.56.72:999 | VE | 5135 | 4 | 91/124 |
| http://154.59.56.73:999 | VE | 2438 | 4 | 96/137 |
| http://196.251.213.192:8081 | ZA | 4285 | 4 | 22/117 |
| http://46.34.166.251:18080 | ?? | 2385 | 4 | 4/4 |
| http://103.156.74.231:8080 | ?? | 4878 | 4 | 4/4 |
| socks5://213.199.47.140:1080 | FR | 2290 | 4 | 103/131 |
| socks5://110.235.240.223:1080 | KH | 1877 | 4 | 36/164 |
| socks5://37.193.218.66:1080 | RU | 7908 | 4 | 16/77 |
| socks5://69.55.49.177:38182 | US | 872 | 4 | 19/20 |
| socks5://14.225.205.152:1082 | ?? | 2713 | 4 | 4/4 |
| socks5://82.180.146.251:10800 | ?? | 1325 | 4 | 4/4 |
| socks5://192.3.7.110:1080 | ?? | 276 | 4 | 4/4 |
| http://181.209.114.220:8080 | AR | 3359 | 3 | 17/109 |
| http://187.102.219.32:999 | AR | 1453 | 3 | 54/164 |
| http://138.0.143.120:8080 | BR | 2462 | 3 | 22/119 |
| http://181.191.14.5:8080 | BR | 1955 | 3 | 20/155 |
| http://35.183.29.62:13595 | CA | 2747 | 3 | 3/3 |
| http://221.221.162.6:8888 | CN | 2113 | 3 | 32/63 |
| http://38.211.76.65:999 | CO | 7093 | 3 | 15/86 |
| http://45.167.124.30:999 | CO | 890 | 3 | 11/41 |
| http://181.78.175.66:999 | CO | 5739 | 3 | 28/155 |
| http://181.78.234.82:999 | CO | 4267 | 3 | 22/117 |
| http://186.96.111.214:999 | CO | 1221 | 3 | 73/154 |
| http://154.88.136.182:999 | DO | 5883 | 3 | 8/38 |
| http://204.157.251.178:999 | DO | 2980 | 3 | 8/19 |
| http://45.186.6.104:3128 | EC | 631 | 3 | 135/143 |
| http://177.234.217.82:999 | EC | 4533 | 3 | 13/62 |
| http://181.188.203.40:999 | EC | 7409 | 3 | 27/62 |
| http://41.33.89.100:1976 | EG | 1729 | 3 | 6/27 |
| http://197.164.101.13:1981 | EG | 4576 | 3 | 53/154 |
| http://15.217.214.40:41371 | ES | 1779 | 3 | 33/129 |
| http://102.164.252.150:8080 | GQ | 1856 | 3 | 47/124 |
