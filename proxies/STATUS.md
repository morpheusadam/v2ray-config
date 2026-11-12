# Proxy status

Generated 2026-11-12T20:51:47Z by `harvest.py`.

- **1791** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4373** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35701** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 174/600 (29%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3284 |
| socks5 | 1073 |
| socks4 | 16 |

| country | entries |
|---|---|
| ID | 954 |
| NL | 914 |
| ?? | 385 |
| PH | 155 |
| US | 149 |
| MX | 138 |
| CO | 122 |
| TH | 107 |
| CN | 98 |
| BR | 89 |
| VE | 82 |
| TR | 81 |
| BD | 74 |
| AR | 66 |
| IN | 66 |
| EC | 65 |
| RU | 51 |
| DO | 46 |
| PK | 42 |
| PE | 40 |
| EG | 37 |
| VN | 36 |
| ZA | 33 |
| JP | 30 |
| SG | 30 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 1 | 2026-11-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 107 | 107 | 11 | 2026-11-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 43 | 2026-11-12 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-11-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 260 | 260 | 75 | 2026-11-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 272 | 272 | 200 | 2026-11-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 330 | 330 | 43 | 2026-11-12 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 340 | 340 | 126 | 2026-11-12 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-12 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-12 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-11-12 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 698 | 698 | 118 | 2026-11-12 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1562 | 1562 | 157 | 2026-11-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1139 | 2026-11-12 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1577 | 2026-11-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2633 | 2633 | 623 | 2026-11-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2923 | 2923 | 1675 | 2026-11-12 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3024 | 3024 | 669 | 2026-11-12 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5274 | 5274 | 3970 | 2026-11-12 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11937 | 11937 | 1985 | 2026-11-12 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1531 | 63 | 83/165 |
| http://176.111.37.5:39811 | HK | 1161 | 58 | 168/187 |
| http://34.43.46.91:80 | US | 4647 | 57 | 181/187 |
| http://4.144.146.21:80 | SG | 4446 | 55 | 72/79 |
| http://176.111.37.216:39811 | HK | 1004 | 50 | 159/187 |
| http://34.43.46.91:443 | US | 2973 | 36 | 176/187 |
| http://130.110.103.245:3128 | SA | 1231 | 33 | 169/187 |
| http://103.133.26.72:8080 | ID | 2263 | 30 | 67/113 |
| http://45.189.57.114:3129 | EC | 1822 | 29 | 29/29 |
| http://103.133.26.119:8080 | ID | 1789 | 23 | 66/97 |
| http://189.51.168.164:999 | MX | 5414 | 23 | 23/23 |
| http://49.229.100.235:8080 | TH | 1456 | 23 | 95/135 |
| http://171.100.254.137:8080 | TH | 1637 | 23 | 23/23 |
| http://43.161.254.16:3128 | HK | 4002 | 22 | 24/27 |
| http://103.130.61.61:8081 | ID | 3681 | 22 | 156/187 |
| http://45.186.6.104:3128 | EC | 654 | 17 | 156/165 |
| http://38.180.18.103:3128 | BE | 688 | 16 | 16/16 |
| http://190.71.72.85:2525 | CO | 693 | 15 | 31/72 |
| http://102.244.78.61:8090 | CM | 1806 | 14 | 63/79 |
| socks5://121.46.226.221:10808 | CN | 1857 | 13 | 13/13 |
| http://103.237.102.191:11111 | DE | 946 | 10 | 178/187 |
| http://43.155.62.157:443 | HK | 996 | 10 | 77/90 |
| http://144.124.251.24:10771 | NL | 591 | 9 | 76/119 |
| http://15.223.187.219:35507 | CA | 1560 | 8 | 26/100 |
| http://185.191.239.248:3128 | CH | 2589 | 8 | 136/186 |
| http://61.91.162.126:8080 | TH | 1407 | 8 | 99/130 |
| http://103.10.231.189:8080 | TH | 1868 | 8 | 126/172 |
| http://27.147.155.206:12051 | BD | 1671 | 7 | 7/7 |
| http://160.22.45.114:8080 | ID | 2709 | 7 | 30/46 |
| http://43.128.144.133:18080 | KR | 863 | 7 | 7/7 |
| socks5://37.18.73.60:5566 | RU | 2261 | 7 | 36/84 |
| http://15.229.149.81:3128 | BR | 3148 | 6 | 62/97 |
| http://64.204.90.17:999 | CO | 6196 | 6 | 6/6 |
| http://51.85.44.162:31819 | IL | 7143 | 6 | 24/39 |
| http://34.229.190.39:33893 | US | 1536 | 6 | 34/128 |
| http://38.41.0.60:11201 | VE | 3640 | 6 | 43/113 |
| http://45.65.224.74:999 | AR | 6150 | 5 | 43/52 |
| http://187.102.219.32:999 | AR | 6380 | 5 | 71/186 |
| http://123.121.140.72:8888 | CN | 2200 | 5 | 24/39 |
| http://177.234.217.83:999 | EC | 5619 | 5 | 25/34 |
| http://103.199.117.121:7777 | ID | 3089 | 5 | 12/21 |
| http://13.233.172.115:57644 | IN | 4028 | 5 | 5/5 |
| http://140.238.32.108:3128 | JP | 1382 | 5 | 107/186 |
| http://144.124.251.24:10574 | NL | 582 | 5 | 79/136 |
| http://144.124.251.24:10605 | NL | 577 | 5 | 74/119 |
| http://144.124.251.24:11266 | NL | 657 | 5 | 76/119 |
| socks5://209.50.255.91:1080 | US | 2851 | 5 | 47/104 |
| http://45.232.0.2:8080 | AR | 4420 | 4 | 61/185 |
| http://16.51.5.77:16637 | AU | 6370 | 4 | 33/127 |
| http://177.184.199.36:80 | BR | 4286 | 4 | 6/19 |
| http://111.196.24.150:8888 | CN | 4417 | 4 | 20/37 |
| http://111.196.30.74:8888 | CN | 5169 | 4 | 18/36 |
| http://123.121.122.125:8888 | CN | 2636 | 4 | 7/10 |
| http://123.121.122.142:8888 | CN | 3271 | 4 | 21/33 |
| http://221.221.154.253:8888 | CN | 3793 | 4 | 23/48 |
| http://43.99.60.244:8089 | HK | 998 | 4 | 71/137 |
| http://49.213.59.108:8082 | ID | 3197 | 4 | 33/88 |
| http://103.150.12.175:8080 | ID | 5449 | 4 | 12/24 |
| http://103.176.97.202:8082 | ID | 1545 | 4 | 8/19 |
| http://45.189.252.245:999 | MX | 7945 | 4 | 6/18 |
| http://148.230.212.70:8080 | MX | 3242 | 4 | 25/63 |
| http://219.93.111.125:9412 | MY | 6997 | 4 | 28/100 |
| http://144.124.251.24:10372 | NL | 601 | 4 | 79/131 |
| http://144.124.251.24:10566 | NL | 558 | 4 | 76/120 |
| http://167.99.74.174:9090 | SG | 1074 | 4 | 97/147 |
| http://38.137.232.153:999 | VE | 6681 | 4 | 41/185 |
| http://154.59.56.78:999 | VE | 2013 | 4 | 99/143 |
| http://38.191.166.50:999 | ?? | 2917 | 4 | 4/4 |
| http://180.191.232.182:3128 | ?? | 5897 | 4 | 4/4 |
| http://187.103.105.20:8085 | ?? | 7858 | 4 | 4/4 |
| http://187.102.219.34:999 | AR | 2408 | 3 | 79/138 |
| http://200.49.99.78:9991 | AR | 3443 | 3 | 6/17 |
| http://3.26.199.107:1234 | AU | 5138 | 3 | 29/100 |
| http://170.245.120.179:3128 | BR | 5146 | 3 | 32/183 |
| http://187.44.188.238:4040 | BR | 6798 | 3 | 14/99 |
| http://201.28.86.18:61804 | BR | 1477 | 3 | 7/8 |
| http://3.96.141.200:8084 | CA | 2944 | 3 | 8/13 |
| http://47.110.226.74:19991 | CN | 2374 | 3 | 81/185 |
| http://114.244.221.178:8888 | CN | 1819 | 3 | 56/110 |
| http://123.121.101.115:8888 | CN | 6419 | 3 | 6/8 |
| http://123.121.121.123:8888 | CN | 2606 | 3 | 7/10 |
| http://124.128.149.84:8090 | CN | 3574 | 3 | 10/21 |
| http://219.148.171.178:9445 | CN | 2973 | 3 | 12/57 |
| http://221.221.154.156:8888 | CN | 6734 | 3 | 47/147 |
| http://181.205.204.19:999 | CO | 2614 | 3 | 12/60 |
| http://38.75.82.221:999 | DO | 4892 | 3 | 58/187 |
| http://38.75.82.222:999 | DO | 7022 | 3 | 40/131 |
| http://38.76.251.244:999 | DO | 3702 | 3 | 4/5 |
| http://177.234.217.84:999 | EC | 1896 | 3 | 22/34 |
| http://41.33.60.42:8081 | EG | 2250 | 3 | 59/185 |
| http://41.33.245.139:1976 | EG | 1335 | 3 | 19/26 |
| http://45.186.106.145:3128 | GT | 4919 | 3 | 11/20 |
| http://165.154.7.156:8888 | HK | 2424 | 3 | 18/46 |
| http://38.211.24.130:8080 | ID | 7707 | 3 | 14/58 |
| http://103.20.191.118:8080 | ID | 3271 | 3 | 43/152 |
| http://103.59.44.113:1111 | ID | 4985 | 3 | 12/25 |
| http://103.76.108.63:8080 | ID | 7826 | 3 | 4/5 |
| http://103.133.26.50:8080 | ID | 1493 | 3 | 59/88 |
| http://103.148.44.139:8080 | ID | 5212 | 3 | 10/26 |
| http://103.156.75.246:8181 | ID | 6292 | 3 | 35/187 |
