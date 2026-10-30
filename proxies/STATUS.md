# Proxy status

Generated 2026-10-30T23:11:52Z by `harvest.py`.

- **1549** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4745** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33285** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 213/600 (36%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2782 |
| socks5 | 1957 |
| socks4 | 6 |

| country | entries |
|---|---|
| NL | 1717 |
| ID | 824 |
| ?? | 510 |
| PH | 120 |
| CO | 118 |
| MX | 95 |
| US | 85 |
| TH | 77 |
| RU | 72 |
| VE | 72 |
| CN | 65 |
| BR | 59 |
| TR | 56 |
| BD | 49 |
| EC | 49 |
| IN | 45 |
| AR | 42 |
| PK | 42 |
| DO | 41 |
| PE | 37 |
| SG | 34 |
| ZA | 32 |
| SY | 29 |
| VN | 28 |
| EG | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 11 | 11 | 3 | 2026-10-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 117 | 117 | 48 | 2026-10-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 65 | 2026-10-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 190 | 190 | 44 | 2026-10-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 238 | 238 | 126 | 2026-10-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 334 | 334 | 108 | 2026-10-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 341 | 341 | 106 | 2026-10-30 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 494 | 494 | 201 | 2026-10-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 444 | 2026-10-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 706 | 706 | 203 | 2026-10-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1125 | 2026-10-30 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1650 | 1650 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1592 | 2026-10-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2261 | 2261 | 707 | 2026-10-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2643 | 2643 | 1649 | 2026-10-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3383 | 3383 | 1065 | 2026-10-30 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4867 | 4867 | 3710 | 2026-10-30 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11707 | 11706 | 2771 | 2026-10-30 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 999 | 82 | 149/162 |
| http://149.130.173.58:9443 | CO | 442 | 73 | 73/73 |
| http://103.237.102.191:11111 | DE | 693 | 49 | 155/162 |
| http://103.133.26.73:3128 | ID | 1605 | 38 | 58/140 |
| http://103.133.26.119:8080 | ID | 1865 | 38 | 42/72 |
| http://176.111.37.5:39811 | HK | 881 | 33 | 143/162 |
| http://34.43.46.91:80 | US | 508 | 32 | 156/162 |
| http://4.144.146.21:80 | SG | 1150 | 30 | 47/54 |
| http://190.0.246.210:4040 | CO | 807 | 29 | 148/161 |
| http://186.5.94.206:999 | EC | 3507 | 27 | 115/124 |
| http://189.51.168.165:999 | MX | 366 | 26 | 69/74 |
| http://176.111.37.216:39811 | HK | 942 | 25 | 134/162 |
| http://103.130.61.61:8081 | ID | 2862 | 24 | 132/162 |
| socks5://67.207.92.87:1088 | US | 299 | 17 | 103/161 |
| socks5://47.238.126.208:1080 | HK | 4161 | 12 | 38/67 |
| http://51.15.20.32:3129 | NL | 464 | 11 | 22/26 |
| http://34.43.46.91:443 | US | 488 | 11 | 151/162 |
| http://34.88.38.81:9443 | FI | 842 | 10 | 89/127 |
| http://35.228.49.168:9443 | FI | 629 | 10 | 70/99 |
| socks5://103.100.158.115:10809 | JP | 1472 | 10 | 41/50 |
| http://167.172.76.176:9090 | SG | 1145 | 9 | 86/123 |
| socks5://101.36.104.239:10808 | JP | 2122 | 9 | 138/162 |
| socks5://193.218.118.128:1080 | UA | 1374 | 9 | 15/18 |
| http://130.110.103.245:3128 | SA | 1325 | 8 | 144/162 |
| http://154.59.56.74:999 | VE | 1447 | 8 | 83/125 |
| socks5://49.13.22.249:10805 | DE | 2461 | 8 | 48/80 |
| socks5://45.61.188.134:44499 | US | 323 | 8 | 64/129 |
| socks5://193.25.215.182:22222 | US | 2568 | 8 | 135/162 |
| http://185.238.236.226:58080 | PL | 2072 | 7 | 34/84 |
| socks5://45.149.92.160:1080 | HK | 1236 | 7 | 20/29 |
| http://123.121.134.192:8888 | CN | 1835 | 6 | 13/28 |
| http://177.234.217.92:999 | EC | 6992 | 6 | 8/11 |
| http://103.172.42.161:1111 | ID | 3602 | 6 | 15/96 |
| socks5://124.248.177.44:1080 | KH | 1986 | 6 | 37/151 |
| socks5://88.201.248.85:1080 | RU | 823 | 6 | 11/17 |
| http://15.229.149.81:3128 | BR | 2803 | 5 | 42/72 |
| http://35.183.78.223:35766 | CA | 4269 | 5 | 5/5 |
| http://177.234.217.85:999 | EC | 1381 | 5 | 8/17 |
| http://177.234.217.235:999 | EC | 3019 | 5 | 63/131 |
| http://38.103.250.205:8080 | ID | 4264 | 5 | 23/125 |
| http://103.133.26.72:8080 | ID | 1520 | 5 | 42/88 |
| http://103.168.254.198:8080 | ID | 4423 | 5 | 16/26 |
| http://128.199.121.61:9090 | SG | 1176 | 5 | 65/82 |
| http://16.28.101.55:2080 | ZA | 3019 | 5 | 34/102 |
| http://38.211.68.83:999 | ?? | 3906 | 5 | 5/5 |
| http://157.15.112.14:8082 | ?? | 1609 | 5 | 5/5 |
| http://157.66.36.129:8080 | ?? | 4040 | 5 | 6/7 |
| socks5://148.251.68.232:8888 | DE | 1797 | 5 | 24/41 |
| socks5://212.77.75.25:1088 | IT | 4448 | 5 | 50/62 |
| socks5://185.9.73.44:1080 | RU | 3722 | 5 | 13/35 |
| socks5://43.155.143.227:1080 | ?? | 2562 | 5 | 5/5 |
| http://103.60.173.173:8080 | BD | 7208 | 4 | 17/117 |
| http://190.124.252.129:6666 | BR | 1691 | 4 | 30/140 |
| http://36.213.79.159:1081 | CN | 2998 | 4 | 9/22 |
| http://114.249.219.180:8888 | CN | 5652 | 4 | 51/126 |
| http://123.121.209.108:8888 | CN | 1698 | 4 | 40/112 |
| http://45.179.200.65:999 | CO | 2369 | 4 | 26/119 |
| http://181.48.159.22:3128 | CO | 3260 | 4 | 12/46 |
| http://81.19.210.10:80 | GB | 457 | 4 | 15/23 |
| http://112.121.173.84:808 | HK | 3004 | 4 | 10/14 |
| http://103.130.61.60:8081 | ID | 5529 | 4 | 17/18 |
| http://103.172.17.14:8080 | ID | 4433 | 4 | 22/73 |
| http://103.175.237.36:8080 | ID | 7728 | 4 | 31/138 |
| http://121.101.133.105:8586 | ID | 3824 | 4 | 17/71 |
| http://154.18.255.43:8080 | ID | 5572 | 4 | 15/67 |
| http://157.15.62.72:8080 | ID | 1638 | 4 | 6/11 |
| http://160.236.4.53:8080 | ID | 5912 | 4 | 9/23 |
| http://163.47.25.10:8080 | ID | 2963 | 4 | 39/160 |
| http://203.175.102.54:3125 | ID | 6161 | 4 | 19/122 |
| http://180.191.137.111:8082 | PH | 1828 | 4 | 33/146 |
| http://203.82.36.163:8082 | PH | 1433 | 4 | 29/100 |
| http://110.39.13.181:8080 | PK | 3845 | 4 | 9/26 |
| http://149.40.242.118:8080 | PK | 5739 | 4 | 7/26 |
| http://164.52.11.194:18080 | TW | 6798 | 4 | 38/115 |
| http://154.59.56.78:999 | VE | 3695 | 4 | 81/118 |
| http://45.189.57.114:3129 | ?? | 4446 | 4 | 4/4 |
| http://104.194.146.9:80 | ?? | 785 | 4 | 7/8 |
| http://191.5.126.28:8080 | ?? | 4571 | 4 | 5/7 |
| socks5://130.255.94.32:5080 | IQ | 3436 | 4 | 34/132 |
| socks5://202.62.42.92:1080 | KH | 1911 | 4 | 32/144 |
| socks5://202.62.42.167:1080 | KH | 2324 | 4 | 41/159 |
| socks5://107.174.30.92:1080 | US | 340 | 4 | 29/58 |
| socks5://208.92.216.54:1080 | US | 5461 | 4 | 6/11 |
| socks5://20.121.179.183:3001 | ?? | 5763 | 4 | 8/9 |
| http://187.102.219.64:999 | AR | 1160 | 3 | 60/101 |
| http://15.229.149.81:1080 | BR | 2451 | 3 | 27/64 |
| http://15.223.187.219:55865 | CA | 3854 | 3 | 25/76 |
| http://45.232.211.1:999 | CL | 2086 | 3 | 6/18 |
| http://102.244.78.61:8080 | CM | 1162 | 3 | 41/51 |
| http://102.244.78.61:8083 | CM | 1161 | 3 | 41/50 |
| http://102.244.78.61:8084 | CM | 1161 | 3 | 39/50 |
| http://102.244.78.61:8085 | CM | 1197 | 3 | 40/52 |
| http://102.244.78.61:8086 | CM | 1161 | 3 | 40/50 |
| http://102.244.78.61:8087 | CM | 1188 | 3 | 39/52 |
| http://61.149.134.158:8888 | CN | 2012 | 3 | 48/127 |
| http://123.121.102.115:8888 | CN | 1856 | 3 | 25/122 |
| http://123.121.108.22:8888 | CN | 1741 | 3 | 9/13 |
| http://123.121.122.28:8888 | CN | 2432 | 3 | 67/111 |
| http://123.121.142.252:8888 | CN | 1969 | 3 | 39/84 |
| http://179.1.196.133:999 | CO | 6076 | 3 | 10/18 |
