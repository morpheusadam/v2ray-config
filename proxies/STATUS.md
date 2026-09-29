# Proxy status

Generated 2026-09-29T18:41:27Z by `harvest.py`.

- **2136** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4173** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39735** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 135/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2201 |
| http | 1966 |
| socks4 | 6 |

| country | entries |
|---|---|
| NL | 1935 |
| ID | 531 |
| US | 174 |
| CN | 126 |
| PH | 81 |
| MX | 80 |
| CO | 78 |
| RU | 76 |
| IN | 65 |
| VE | 63 |
| DE | 56 |
| BD | 54 |
| EC | 51 |
| VN | 47 |
| BR | 46 |
| PK | 43 |
| TR | 42 |
| SG | 36 |
| FR | 34 |
| ZA | 33 |
| JP | 30 |
| HK | 29 |
| DO | 26 |
| CA | 23 |
| PE | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-09-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 64 | 64 | 16 | 2026-09-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 66 | 66 | 34 | 2026-09-29 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 102 | 102 | 43 | 2026-09-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 85 | 2026-09-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 201 | 201 | 71 | 2026-09-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 369 | 369 | 186 | 2026-09-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 387 | 387 | 197 | 2026-09-29 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 496 | 496 | 212 | 2026-09-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1134 | 2026-09-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-09-29 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1947 | 1943 | 410 | 2026-09-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2239 | 2238 | 693 | 2026-09-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2818 | 2816 | 1986 | 2026-09-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3044 | 3043 | 882 | 2026-09-29 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 31153 | 31153 | 17094 | 2026-09-29 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 39348 | 39347 | 4638 | 2026-09-29 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1683 | 86 | 99/100 |
| http://95.3.69.222:8080 | TR | 2720 | 55 | 97/100 |
| http://190.0.246.213:4040 | CO | 2468 | 29 | 58/65 |
| http://213.111.146.36:18080 | NL | 646 | 29 | 32/37 |
| socks5://83.147.217.103:1080 | US | 1950 | 23 | 23/23 |
| http://190.0.246.211:4040 | CO | 2531 | 20 | 87/100 |
| http://167.172.76.176:9090 | SG | 1229 | 20 | 42/61 |
| http://34.43.46.91:80 | US | 2502 | 17 | 96/100 |
| http://190.0.246.210:4040 | CO | 3296 | 16 | 88/99 |
| http://103.237.102.191:11111 | DE | 2112 | 16 | 94/100 |
| http://18.157.123.132:3128 | DE | 734 | 15 | 47/61 |
| http://107.167.18.122:443 | US | 304 | 15 | 50/52 |
| socks5://144.91.121.61:1088 | FR | 2221 | 14 | 86/100 |
| http://34.43.46.91:443 | US | 2924 | 13 | 94/100 |
| http://189.51.168.165:999 | MX | 566 | 12 | 12/12 |
| http://149.130.173.58:9443 | CO | 520 | 11 | 11/11 |
| http://43.173.120.13:8899 | US | 474 | 11 | 11/11 |
| http://3.212.18.54:3128 | US | 1142 | 10 | 10/10 |
| socks5://171.25.158.95:1080 | SE | 2814 | 10 | 11/15 |
| http://36.137.204.11:8002 | CN | 5848 | 9 | 12/16 |
| http://185.195.71.218:18080 | CH | 1428 | 8 | 28/37 |
| http://103.119.19.218:3128 | CZ | 964 | 8 | 12/13 |
| http://186.5.94.206:999 | EC | 6265 | 8 | 59/62 |
| http://37.59.125.131:8888 | FR | 3528 | 8 | 79/100 |
| http://3.1.100.245:3128 | SG | 1120 | 8 | 9/12 |
| http://43.159.54.178:80 | SG | 1293 | 8 | 15/20 |
| http://107.150.41.226:18080 | US | 271 | 8 | 36/37 |
| http://172.236.242.244:3128 | US | 287 | 8 | 8/8 |
| socks5://144.76.61.252:1080 | DE | 3070 | 7 | 10/13 |
| socks5://154.201.71.12:2080 | HK | 1460 | 7 | 8/9 |
| http://45.232.0.2:8080 | AR | 5403 | 6 | 30/98 |
| http://113.45.195.147:3128 | CN | 1922 | 6 | 41/65 |
| http://120.232.115.57:17981 | CN | 1524 | 6 | 20/25 |
| http://123.121.210.208:8888 | CN | 7021 | 6 | 24/52 |
| http://197.224.185.3:3128 | MU | 1969 | 6 | 62/68 |
| http://128.199.254.13:9090 | SG | 1416 | 6 | 22/29 |
| http://129.226.89.151:80 | SG | 1077 | 6 | 30/47 |
| socks5://138.124.66.226:1080 | DE | 4682 | 6 | 6/6 |
| socks5://121.169.46.116:1090 | KR | 2574 | 6 | 67/100 |
| socks5://174.138.189.26:2001 | US | 257 | 6 | 6/6 |
| http://184.75.221.82:3118 | CA | 4428 | 5 | 57/65 |
| http://144.76.61.252:3128 | DE | 4475 | 5 | 11/13 |
| http://45.186.6.104:3128 | EC | 1145 | 5 | 73/78 |
| http://49.147.104.23:8082 | PH | 4894 | 5 | 5/5 |
| http://24.52.147.103:5999 | US | 3402 | 5 | 7/8 |
| socks4://185.112.83.80:1080 | FI | 6770 | 5 | 5/5 |
| socks5://5.75.133.113:10801 | DE | 2502 | 5 | 38/66 |
| socks5://47.238.126.208:1080 | HK | 1465 | 5 | 5/5 |
| http://187.102.219.34:999 | AR | 5365 | 4 | 22/51 |
| http://185.191.239.248:3128 | CH | 3845 | 4 | 70/99 |
| http://1.15.53.214:8888 | CN | 3670 | 4 | 23/94 |
| http://47.103.30.64:8080 | CN | 1807 | 4 | 12/33 |
| http://111.192.24.82:8888 | CN | 2257 | 4 | 6/19 |
| http://111.196.31.158:8888 | CN | 2049 | 4 | 24/46 |
| http://114.252.13.224:8888 | CN | 1516 | 4 | 27/64 |
| http://114.254.50.97:8888 | CN | 1419 | 4 | 34/65 |
| http://123.121.122.28:8888 | CN | 1881 | 4 | 29/49 |
| http://123.121.208.55:8888 | CN | 1804 | 4 | 19/53 |
| http://221.221.144.75:8888 | CN | 5728 | 4 | 24/62 |
| http://221.221.154.156:8888 | CN | 1449 | 4 | 20/60 |
| http://221.221.159.97:8888 | CN | 6414 | 4 | 23/53 |
| http://113.192.1.170:8181 | ID | 1444 | 4 | 18/55 |
| http://153.51.241.50:999 | MX | 885 | 4 | 51/97 |
| http://49.229.100.235:8080 | TH | 1484 | 4 | 24/48 |
| http://61.91.162.126:8080 | TH | 1440 | 4 | 34/43 |
| http://103.10.231.189:8080 | TH | 1645 | 4 | 59/85 |
| http://3.235.0.113:29303 | US | 1981 | 4 | 8/16 |
| http://193.104.179.115:3128 | UZ | 1945 | 4 | 47/65 |
| socks5://101.36.104.239:10808 | JP | 7925 | 4 | 83/100 |
| socks5://43.135.176.121:1080 | US | 1070 | 4 | 33/55 |
| http://16.26.208.68:18596 | AU | 5742 | 3 | 18/65 |
| http://170.247.200.138:8088 | BR | 5680 | 3 | 6/15 |
| http://190.124.252.129:6666 | BR | 7499 | 3 | 15/78 |
| http://15.223.187.219:35507 | CA | 1120 | 3 | 4/13 |
| http://38.7.195.55:999 | CL | 7398 | 3 | 27/74 |
| http://47.107.107.24:80 | CN | 1793 | 3 | 40/68 |
| http://47.121.139.13:3128 | CN | 2836 | 3 | 50/99 |
| http://114.244.214.18:8888 | CN | 2871 | 3 | 12/23 |
| http://114.244.223.68:8888 | CN | 1950 | 3 | 32/63 |
| http://123.121.209.108:8888 | CN | 2307 | 3 | 21/50 |
| http://221.221.154.122:8888 | CN | 2249 | 3 | 18/53 |
| http://67.207.78.208:3128 | DE | 6053 | 3 | 10/13 |
| http://129.212.171.38:3128 | DE | 1057 | 3 | 3/3 |
| http://134.199.191.115:3128 | DE | 5110 | 3 | 11/12 |
| http://209.38.115.253:3128 | DE | 5709 | 3 | 9/12 |
| http://34.88.38.81:9443 | FI | 829 | 3 | 43/65 |
| http://35.228.49.168:9443 | FI | 913 | 3 | 24/37 |
| http://91.134.141.4:3128 | FR | 3813 | 3 | 53/61 |
| http://43.155.62.157:443 | HK | 2399 | 3 | 3/3 |
| http://176.111.37.216:39811 | HK | 4396 | 3 | 81/100 |
| http://103.77.206.114:3128 | ID | 1405 | 3 | 3/3 |
| http://103.144.54.73:8082 | ID | 1409 | 3 | 22/45 |
| http://103.171.255.170:8080 | ID | 6176 | 3 | 7/39 |
| http://103.180.123.47:8080 | ID | 7184 | 3 | 5/6 |
| http://160.22.206.83:8082 | ID | 5751 | 3 | 17/68 |
| http://160.22.207.95:8082 | ID | 1408 | 3 | 14/78 |
| http://163.227.252.3:8080 | ID | 4562 | 3 | 16/38 |
| http://202.154.19.50:3125 | ID | 4732 | 3 | 12/69 |
| http://51.84.101.19:9506 | IL | 2401 | 3 | 6/12 |
| http://34.131.37.209:40001 | IN | 3830 | 3 | 3/3 |
