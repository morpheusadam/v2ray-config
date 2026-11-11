# Proxy status

Generated 2026-11-11T20:33:43Z by `harvest.py`.

- **1736** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4547** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35582** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 133/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2757 |
| socks5 | 1777 |
| socks4 | 13 |

| country | entries |
|---|---|
| NL | 1577 |
| ID | 771 |
| ?? | 239 |
| PH | 143 |
| MX | 125 |
| US | 125 |
| CO | 116 |
| CN | 99 |
| TH | 94 |
| TR | 81 |
| BR | 77 |
| VE | 75 |
| BD | 69 |
| IN | 65 |
| RU | 64 |
| EC | 55 |
| AR | 49 |
| DO | 49 |
| PK | 46 |
| VN | 43 |
| DE | 38 |
| SG | 34 |
| EG | 33 |
| PE | 33 |
| ZA | 33 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 2 | 2026-11-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 75 | 75 | 18 | 2026-11-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 35 | 2026-11-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-11-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 255 | 255 | 27 | 2026-11-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 303 | 303 | 72 | 2026-11-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 364 | 364 | 254 | 2026-11-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 474 | 474 | 176 | 2026-11-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-11-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 643 | 643 | 106 | 2026-11-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1119 | 2026-11-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1577 | 2026-11-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1896 | 1896 | 391 | 2026-11-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2069 | 2069 | 350 | 2026-11-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2155 | 2155 | 677 | 2026-11-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2505 | 2505 | 1386 | 2026-11-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5238 | 5238 | 3959 | 2026-11-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11336 | 11336 | 1923 | 2026-11-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1325 | 61 | 81/163 |
| http://176.111.37.5:39811 | HK | 1068 | 56 | 166/185 |
| http://34.43.46.91:80 | US | 2416 | 55 | 179/185 |
| http://4.144.146.21:80 | SG | 888 | 53 | 70/77 |
| http://176.111.37.216:39811 | HK | 1017 | 48 | 157/185 |
| http://34.43.46.91:443 | US | 1348 | 34 | 174/185 |
| http://130.110.103.245:3128 | SA | 1307 | 31 | 167/185 |
| http://103.133.26.72:8080 | ID | 1229 | 28 | 65/111 |
| http://45.189.57.114:3129 | EC | 860 | 27 | 27/27 |
| http://103.133.26.119:8080 | ID | 1611 | 21 | 64/95 |
| http://189.51.168.164:999 | MX | 1844 | 21 | 21/21 |
| http://49.229.100.235:8080 | TH | 1212 | 21 | 93/133 |
| http://171.100.254.137:8080 | TH | 1223 | 21 | 21/21 |
| http://43.161.254.16:3128 | HK | 1811 | 20 | 22/25 |
| http://103.130.61.61:8081 | ID | 1335 | 20 | 154/185 |
| http://184.75.221.82:3118 | CA | 529 | 19 | 132/150 |
| http://102.244.78.61:8089 | CM | 1454 | 16 | 60/73 |
| http://45.186.6.104:3128 | EC | 790 | 15 | 154/163 |
| http://38.180.18.103:3128 | BE | 824 | 14 | 14/14 |
| http://190.71.72.85:2525 | CO | 725 | 13 | 29/70 |
| http://102.244.78.61:8090 | CM | 1418 | 12 | 61/77 |
| socks5://121.46.226.221:10808 | CN | 1637 | 11 | 11/11 |
| http://177.234.217.44:999 | EC | 2862 | 9 | 32/85 |
| http://45.65.224.125:999 | AR | 6252 | 8 | 35/47 |
| http://123.121.108.22:8888 | CN | 2164 | 8 | 26/36 |
| http://103.237.102.191:11111 | DE | 873 | 8 | 176/185 |
| http://43.155.62.157:443 | HK | 1856 | 8 | 75/88 |
| http://82.152.138.127:999 | MX | 374 | 8 | 60/147 |
| http://189.51.168.165:999 | MX | 1027 | 8 | 90/97 |
| socks5://5.255.113.177:1080 | NL | 1972 | 8 | 34/83 |
| http://45.245.208.180:8080 | EG | 2457 | 7 | 40/58 |
| http://144.124.251.24:10771 | NL | 754 | 7 | 74/117 |
| http://15.223.187.219:35507 | CA | 4491 | 6 | 24/98 |
| http://185.191.239.248:3128 | CH | 1079 | 6 | 134/184 |
| http://102.244.78.61:8081 | CM | 1407 | 6 | 58/71 |
| http://123.121.109.207:8888 | CN | 2307 | 6 | 6/6 |
| http://177.234.217.92:999 | EC | 5001 | 6 | 27/34 |
| http://177.234.217.93:999 | EC | 4567 | 6 | 32/44 |
| http://38.226.242.83:8080 | ID | 5357 | 6 | 12/30 |
| http://206.135.47.107:999 | MX | 2828 | 6 | 33/55 |
| http://38.210.106.24:999 | PE | 1847 | 6 | 13/40 |
| http://180.191.0.205:8081 | PH | 3625 | 6 | 12/25 |
| http://61.91.162.126:8080 | TH | 1245 | 6 | 97/128 |
| http://103.10.231.189:8080 | TH | 1594 | 6 | 124/170 |
| socks5://171.25.158.95:1080 | SE | 3111 | 6 | 79/100 |
| http://45.65.226.171:999 | AR | 5196 | 5 | 13/23 |
| http://27.147.155.206:12051 | BD | 1582 | 5 | 5/5 |
| http://1.15.53.214:8888 | CN | 1591 | 5 | 53/179 |
| http://41.33.245.139:1981 | EG | 7288 | 5 | 16/23 |
| http://160.22.45.114:8080 | ID | 7892 | 5 | 28/44 |
| http://40.192.70.191:11223 | IN | 2895 | 5 | 10/29 |
| http://43.128.144.133:18080 | KR | 2027 | 5 | 5/5 |
| http://206.135.47.110:999 | MX | 3891 | 5 | 30/56 |
| http://144.124.251.24:10800 | NL | 781 | 5 | 71/117 |
| http://152.42.177.32:8888 | SG | 888 | 5 | 96/145 |
| http://159.223.41.216:9090 | SG | 895 | 5 | 106/145 |
| socks5://37.18.73.60:5566 | RU | 1991 | 5 | 34/82 |
| socks5://95.31.115.101:9150 | RU | 2577 | 5 | 5/5 |
| socks5://43.156.152.110:1080 | SG | 1264 | 5 | 5/5 |
| socks5://69.55.49.177:38182 | US | 1325 | 5 | 38/40 |
| http://103.113.152.73:14158 | BD | 5496 | 4 | 47/179 |
| http://15.229.149.81:3128 | BR | 4483 | 4 | 60/95 |
| http://114.244.223.68:8888 | CN | 2451 | 4 | 6/10 |
| http://123.115.226.82:8888 | CN | 1267 | 4 | 48/131 |
| http://123.121.93.201:8888 | CN | 2242 | 4 | 5/6 |
| http://221.221.162.6:8888 | CN | 1376 | 4 | 43/83 |
| http://64.204.90.17:999 | CO | 2764 | 4 | 4/4 |
| http://177.234.217.45:999 | EC | 2575 | 4 | 43/116 |
| http://177.234.217.46:999 | EC | 4898 | 4 | 49/132 |
| http://213.131.85.26:1976 | EG | 1301 | 4 | 12/16 |
| http://103.167.170.70:1111 | ID | 3790 | 4 | 37/183 |
| http://103.171.182.80:8080 | ID | 1237 | 4 | 5/7 |
| http://51.85.44.162:31819 | IL | 2570 | 4 | 22/37 |
| http://51.85.44.162:8089 | IL | 4480 | 4 | 19/35 |
| http://34.229.190.39:33893 | US | 1319 | 4 | 32/126 |
| http://54.198.140.56:13476 | US | 1235 | 4 | 30/83 |
| http://38.41.0.60:11201 | VE | 6777 | 4 | 41/111 |
| socks4://143.198.239.45:10006 | US | 2268 | 4 | 13/47 |
| socks5://45.74.31.42:7897 | NL | 5027 | 4 | 6/11 |
| socks5://45.74.31.46:5333 | NL | 5230 | 4 | 12/60 |
| socks5://54.198.53.191:1080 | US | 4709 | 4 | 4/4 |
| socks5://116.101.73.161:1081 | VN | 2148 | 4 | 4/4 |
| http://45.65.224.74:999 | AR | 4248 | 3 | 41/50 |
| http://187.102.219.32:999 | AR | 1610 | 3 | 69/184 |
| http://15.229.149.81:1080 | BR | 2394 | 3 | 46/87 |
| http://40.177.104.199:38213 | CA | 4502 | 3 | 30/107 |
| http://101.251.204.174:8080 | CN | 1583 | 3 | 93/171 |
| http://111.192.48.62:8888 | CN | 1350 | 3 | 3/3 |
| http://114.248.179.223:8888 | CN | 5385 | 3 | 69/153 |
| http://123.121.134.141:8888 | CN | 1388 | 3 | 26/46 |
| http://123.121.140.72:8888 | CN | 1390 | 3 | 22/37 |
| http://222.128.180.15:8888 | CN | 2140 | 3 | 3/3 |
| http://222.128.181.249:8888 | CN | 7013 | 3 | 3/3 |
| http://190.29.25.245:3128 | CO | 4881 | 3 | 17/83 |
| http://154.88.164.160:999 | DO | 7995 | 3 | 8/18 |
| http://177.234.217.83:999 | EC | 2512 | 3 | 23/32 |
| http://41.196.16.227:1981 | EG | 2676 | 3 | 3/3 |
| http://217.52.247.84:1976 | EG | 2501 | 3 | 3/3 |
| http://13.38.27.183:26602 | FR | 2901 | 3 | 38/185 |
| http://81.19.210.10:80 | GB | 1121 | 3 | 30/46 |
