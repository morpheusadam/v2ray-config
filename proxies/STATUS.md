# Proxy status

Generated 2026-11-26T22:21:18Z by `harvest.py`.

- **1729** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3564** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25952** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 151/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3180 |
| socks5 | 373 |
| socks4 | 11 |

| country | entries |
|---|---|
| ID | 969 |
| ?? | 235 |
| PH | 176 |
| NL | 150 |
| MX | 149 |
| CO | 148 |
| CN | 108 |
| IN | 102 |
| US | 102 |
| BR | 96 |
| TR | 94 |
| VE | 83 |
| CH | 76 |
| TH | 67 |
| EC | 66 |
| RU | 64 |
| BD | 59 |
| AR | 53 |
| DO | 44 |
| PK | 40 |
| DE | 36 |
| PE | 34 |
| ZA | 34 |
| SG | 30 |
| VN | 30 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 3 | 2026-11-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 106 | 106 | 11 | 2026-11-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 36 | 2026-11-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 60 | 2026-11-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 154 | 154 | 39 | 2026-11-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 224 | 224 | 42 | 2026-11-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 301 | 301 | 36 | 2026-11-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 561 | 561 | 409 | 2026-11-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-11-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1559 | 1559 | 255 | 2026-11-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1114 | 2026-11-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1933 | 1933 | 228 | 2026-11-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2325 | 2325 | 208 | 2026-11-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2592 | 2592 | 769 | 2026-11-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2879 | 2879 | 1641 | 2026-11-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5759 | 5759 | 4562 | 2026-11-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 13005 | 13005 | 2378 | 2026-11-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 912 | 86 | 196/215 |
| http://130.110.103.245:3128 | SA | 1314 | 61 | 197/215 |
| http://141.94.22.37:3128 | FR | 718 | 27 | 30/31 |
| http://45.155.226.177:3128 | HK | 633 | 24 | 29/31 |
| http://4.144.146.21:80 | SG | 970 | 22 | 98/107 |
| http://34.43.46.91:80 | US | 566 | 20 | 208/215 |
| http://189.51.168.164:999 | MX | 2780 | 19 | 47/51 |
| http://20.98.234.24:8080 | US | 302 | 19 | 19/19 |
| socks5://69.55.49.177:38182 | US | 1427 | 19 | 59/70 |
| http://103.237.102.191:11111 | DE | 807 | 18 | 202/215 |
| http://45.186.6.104:3128 | EC | 736 | 17 | 183/193 |
| http://103.133.26.50:8080 | ID | 1281 | 17 | 81/116 |
| http://103.133.26.73:3128 | ID | 1332 | 17 | 105/193 |
| http://147.161.246.34:80 | CH | 5717 | 15 | 15/15 |
| http://45.135.95.185:3128 | RU | 2471 | 13 | 13/13 |
| http://128.199.113.85:9090 | SG | 954 | 13 | 33/46 |
| socks5://123.58.219.171:10808 | HK | 1263 | 13 | 157/215 |
| http://190.123.83.137:999 | AR | 2897 | 12 | 45/52 |
| http://103.163.80.181:8085 | ID | 1300 | 11 | 11/11 |
| http://50.238.106.26:3128 | US | 278 | 11 | 11/11 |
| http://158.247.125.5:9443 | CO | 2536 | 10 | 10/10 |
| http://34.43.46.91:443 | US | 362 | 10 | 199/215 |
| http://216.125.18.67:3128 | US | 892 | 10 | 10/10 |
| http://103.21.150.15:3128 | VN | 1108 | 9 | 11/27 |
| http://185.191.239.248:3128 | CH | 1012 | 8 | 151/214 |
| http://45.136.253.145:3128 | TH | 1070 | 8 | 13/19 |
| http://102.244.78.61:8082 | CM | 6432 | 7 | 81/104 |
| http://102.244.78.61:8083 | CM | 7306 | 7 | 81/103 |
| http://45.65.138.48:999 | CO | 2843 | 7 | 112/215 |
| http://177.234.217.89:999 | EC | 3444 | 7 | 26/40 |
| http://157.66.16.45:7789 | ID | 2346 | 7 | 12/35 |
| http://31.130.153.132:3128 | KZ | 1511 | 7 | 7/7 |
| http://129.153.97.250:9443 | US | 305 | 7 | 7/7 |
| http://154.59.56.78:999 | VE | 7123 | 7 | 117/171 |
| http://103.81.86.170:8888 | VN | 2513 | 7 | 7/7 |
| socks5://59.11.209.162:1080 | KR | 977 | 7 | 7/7 |
| http://190.12.150.244:999 | EC | 4787 | 6 | 157/211 |
| http://128.199.116.219:9090 | SG | 990 | 6 | 104/134 |
| http://114.246.197.205:8888 | CN | 1508 | 5 | 9/11 |
| http://114.249.228.162:8888 | CN | 6951 | 5 | 5/5 |
| http://123.113.149.18:8888 | CN | 1829 | 5 | 5/5 |
| http://123.121.120.25:8888 | CN | 7056 | 5 | 9/11 |
| http://45.65.137.218:999 | CO | 1653 | 5 | 92/180 |
| http://197.164.101.14:1976 | EG | 2041 | 5 | 66/187 |
| http://197.164.101.14:1981 | EG | 1396 | 5 | 55/185 |
| http://173.212.207.102:1214 | FR | 1131 | 5 | 5/5 |
| http://189.187.131.201:999 | MX | 6608 | 5 | 5/5 |
| http://16.5.7.5:8118 | BR | 1891 | 4 | 9/14 |
| http://102.244.78.61:8080 | CM | 6682 | 4 | 83/104 |
| http://114.246.192.19:8888 | CN | 4783 | 4 | 5/11 |
| http://114.249.212.245:8888 | CN | 1836 | 4 | 4/4 |
| http://123.115.143.194:8888 | CN | 2311 | 4 | 8/14 |
| http://197.164.101.11:1981 | EG | 2426 | 4 | 13/32 |
| http://213.131.85.28:1976 | EG | 1182 | 4 | 19/29 |
| http://103.156.15.73:8080 | ID | 7154 | 4 | 44/212 |
| http://103.158.210.80:8082 | ID | 4410 | 4 | 72/205 |
| socks5://61.247.178.146:1080 | BD | 3843 | 4 | 21/55 |
| socks5://49.13.22.249:10802 | DE | 2237 | 4 | 54/142 |
| socks5://46.37.59.97:1080 | GB | 6238 | 4 | 15/29 |
| socks5://171.253.90.204:1080 | VN | 2075 | 4 | 4/4 |
| http://45.177.147.152:999 | AR | 7655 | 3 | 7/19 |
| http://64.76.33.108:999 | AR | 2850 | 3 | 19/68 |
| http://131.221.65.109:8090 | AR | 2858 | 3 | 23/87 |
| http://187.102.219.42:999 | AR | 1842 | 3 | 122/210 |
| http://200.110.218.11:999 | AR | 6806 | 3 | 38/175 |
| http://3.26.199.107:1234 | AU | 2787 | 3 | 38/128 |
| http://103.245.109.70:21458 | BD | 6313 | 3 | 36/120 |
| http://182.160.110.154:9898 | BD | 3134 | 3 | 21/90 |
| http://38.76.228.240:8088 | BR | 2688 | 3 | 26/104 |
| http://45.161.144.16:6666 | BR | 6136 | 3 | 21/85 |
| http://177.37.167.172:3900 | BR | 3332 | 3 | 18/80 |
| http://186.250.202.104:8080 | BR | 4285 | 3 | 45/192 |
| http://201.71.24.65:8082 | BR | 5510 | 3 | 38/204 |
| http://181.74.82.91:999 | CL | 2681 | 3 | 39/174 |
| http://111.196.24.150:8888 | CN | 1972 | 3 | 31/65 |
| http://114.244.208.65:8888 | CN | 3465 | 3 | 3/3 |
| http://114.246.200.14:8888 | CN | 7579 | 3 | 5/6 |
| http://114.246.201.118:8888 | CN | 1716 | 3 | 9/11 |
| http://114.246.207.138:8888 | CN | 5640 | 3 | 4/11 |
| http://114.249.219.234:8888 | CN | 1641 | 3 | 7/11 |
| http://114.249.221.91:8888 | CN | 2494 | 3 | 4/10 |
| http://114.249.226.144:8888 | CN | 2797 | 3 | 7/11 |
| http://123.121.130.181:8888 | CN | 3522 | 3 | 5/9 |
| http://64.204.90.177:999 | CO | 4969 | 3 | 6/11 |
| http://177.73.155.246:999 | CO | 3760 | 3 | 33/214 |
| http://190.2.214.147:999 | CO | 7404 | 3 | 21/69 |
| http://141.147.19.47:12345 | DE | 726 | 3 | 24/76 |
| http://38.41.184.73:999 | DO | 2261 | 3 | 20/88 |
| http://177.234.217.45:999 | EC | 4134 | 3 | 59/146 |
| http://177.234.217.84:999 | EC | 4601 | 3 | 38/62 |
| http://41.65.55.27:1981 | EG | 2272 | 3 | 58/155 |
| http://41.196.16.231:1976 | EG | 1215 | 3 | 7/42 |
| http://45.245.208.180:8080 | EG | 1256 | 3 | 62/88 |
| http://81.10.102.153:8080 | EG | 1295 | 3 | 3/3 |
| http://217.52.247.75:1976 | EG | 1174 | 3 | 3/3 |
| http://51.94.221.175:3047 | ES | 1416 | 3 | 24/99 |
| http://51.68.102.5:3128 | FR | 711 | 3 | 8/29 |
| http://198.244.254.77:3128 | GB | 747 | 3 | 79/99 |
| http://45.5.119.17:999 | GT | 7099 | 3 | 27/123 |
| http://192.141.165.131:999 | HN | 3399 | 3 | 34/157 |
