# Proxy status

Generated 2026-10-20T18:04:32Z by `harvest.py`.

- **1702** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4783** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39194** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 109/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2862 |
| socks5 | 1912 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 1633 |
| ID | 869 |
| ?? | 180 |
| PH | 153 |
| CO | 145 |
| MX | 120 |
| RU | 119 |
| US | 105 |
| BR | 85 |
| VE | 77 |
| CN | 76 |
| EC | 75 |
| TR | 75 |
| BD | 73 |
| DO | 61 |
| IN | 61 |
| TH | 52 |
| AR | 46 |
| DE | 43 |
| PK | 42 |
| SG | 38 |
| CL | 36 |
| VN | 32 |
| KH | 30 |
| SY | 30 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-10-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 115 | 115 | 62 | 2026-10-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 140 | 140 | 38 | 2026-10-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 58 | 2026-10-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 88 | 2026-10-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 303 | 303 | 92 | 2026-10-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 351 | 351 | 41 | 2026-10-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 376 | 376 | 125 | 2026-10-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-10-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1105 | 1105 | 840 | 2026-10-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-10-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1593 | 2026-10-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1944 | 1940 | 0 | 2026-10-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2617 | 2615 | 700 | 2026-10-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2630 | 2628 | 552 | 2026-10-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2769 | 2767 | 1880 | 2026-10-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 73091 | 73091 | 60047 | 2026-10-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 79915 | 79914 | 2143 | 2026-10-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2711 | 61 | 128/141 |
| http://149.130.173.58:9443 | CO | 508 | 52 | 52/52 |
| http://190.0.246.213:4040 | CO | 2294 | 35 | 98/106 |
| http://197.224.185.3:3128 | MU | 1949 | 33 | 102/109 |
| http://103.237.102.191:11111 | DE | 1145 | 28 | 134/141 |
| http://203.252.142.217:80 | KR | 790 | 23 | 23/23 |
| http://45.186.6.104:3128 | EC | 776 | 22 | 112/119 |
| http://3.211.120.181:443 | US | 299 | 21 | 35/52 |
| http://103.133.26.72:8080 | ID | 1301 | 17 | 22/67 |
| http://103.133.26.73:3128 | ID | 1336 | 17 | 37/119 |
| http://103.133.26.119:8080 | ID | 1689 | 17 | 21/51 |
| http://128.199.121.61:9090 | SG | 1083 | 13 | 51/61 |
| socks5://171.25.158.95:1080 | SE | 1626 | 13 | 48/56 |
| socks5://47.87.97.94:1080 | TH | 2032 | 13 | 16/17 |
| http://198.244.254.77:3128 | GB | 3949 | 12 | 23/25 |
| http://176.111.37.5:39811 | HK | 1882 | 12 | 122/141 |
| http://140.238.32.108:3128 | JP | 1839 | 11 | 74/140 |
| http://34.43.46.91:80 | US | 3837 | 11 | 135/141 |
| http://152.67.191.232:6800 | IN | 2186 | 10 | 10/10 |
| socks5://43.245.199.34:1080 | HK | 1184 | 10 | 10/10 |
| http://4.144.146.21:80 | SG | 985 | 9 | 26/33 |
| http://190.0.246.210:4040 | CO | 3856 | 8 | 127/140 |
| http://43.155.62.157:443 | HK | 3076 | 8 | 36/44 |
| http://154.59.56.72:999 | VE | 7614 | 8 | 73/100 |
| http://187.102.219.32:999 | AR | 3589 | 7 | 46/140 |
| http://102.244.78.61:8081 | CM | 1356 | 7 | 20/27 |
| http://102.244.78.61:8090 | CM | 1364 | 7 | 23/33 |
| http://45.65.137.218:999 | CO | 2712 | 7 | 39/106 |
| http://103.119.19.218:3128 | CZ | 1638 | 7 | 42/54 |
| http://161.49.90.70:1337 | PH | 4671 | 7 | 16/79 |
| http://44.216.83.206:3128 | US | 1306 | 7 | 11/14 |
| socks5://213.199.47.140:1080 | FR | 3620 | 7 | 84/107 |
| socks5://123.58.219.171:10808 | HK | 3931 | 7 | 111/141 |
| http://187.102.219.64:999 | AR | 5389 | 6 | 49/80 |
| http://186.5.94.206:999 | EC | 1071 | 6 | 94/103 |
| http://185.142.156.203:80 | IR | 5039 | 6 | 6/6 |
| http://49.156.44.115:8080 | KH | 6195 | 6 | 37/107 |
| http://205.164.192.115:999 | MX | 2272 | 6 | 91/139 |
| http://152.32.77.213:8095 | PH | 7282 | 6 | 6/6 |
| socks5://103.100.158.115:10809 | JP | 7713 | 6 | 21/29 |
| http://123.200.8.170:10000 | BD | 3009 | 5 | 54/139 |
| http://184.75.221.82:3118 | CA | 869 | 5 | 92/106 |
| http://38.7.195.49:999 | CL | 2508 | 5 | 52/115 |
| http://38.7.195.52:999 | CL | 4321 | 5 | 58/123 |
| http://38.7.195.55:999 | CL | 6151 | 5 | 50/115 |
| http://119.188.131.55:17981 | CN | 1492 | 5 | 69/141 |
| http://123.119.25.143:8888 | CN | 5587 | 5 | 45/106 |
| http://45.179.200.65:999 | CO | 2399 | 5 | 19/98 |
| http://45.71.186.212:999 | EC | 4238 | 5 | 49/128 |
| http://45.71.186.214:999 | EC | 3662 | 5 | 36/87 |
| http://213.131.85.28:1981 | EG | 3170 | 5 | 5/5 |
| http://103.155.196.83:8082 | ID | 4485 | 5 | 20/54 |
| http://103.158.210.80:8082 | ID | 1379 | 5 | 35/131 |
| http://189.51.168.165:999 | MX | 489 | 5 | 48/53 |
| http://112.202.247.74:8082 | PH | 4257 | 5 | 13/38 |
| http://181.78.216.93:999 | PY | 7177 | 5 | 15/75 |
| http://130.110.103.245:3128 | SA | 1600 | 5 | 125/141 |
| http://201.4.65.102:8080 | TR | 2253 | 5 | 6/12 |
| http://201.7.31.230:8080 | TR | 4841 | 5 | 16/79 |
| socks5://89.58.42.118:3129 | DE | 968 | 5 | 9/30 |
| socks5://160.187.0.89:1080 | VN | 4510 | 5 | 41/54 |
| http://102.244.78.61:8084 | CM | 1361 | 4 | 22/29 |
| http://102.244.78.61:8086 | CM | 1304 | 4 | 22/29 |
| http://102.244.78.61:8088 | CM | 1361 | 4 | 23/29 |
| http://181.225.68.73:999 | CO | 6646 | 4 | 23/123 |
| http://190.60.34.250:999 | CO | 6348 | 4 | 34/118 |
| http://190.121.157.41:999 | CO | 5905 | 4 | 18/113 |
| http://157.100.12.149:999 | EC | 3884 | 4 | 8/24 |
| http://181.78.195.137:999 | EC | 4209 | 4 | 43/141 |
| http://79.130.240.61:18080 | GR | 7605 | 4 | 11/48 |
| http://176.111.37.216:39811 | HK | 2648 | 4 | 113/141 |
| http://103.31.232.110:8080 | ID | 3746 | 4 | 9/22 |
| http://103.156.57.135:9988 | ID | 6020 | 4 | 18/81 |
| http://46.209.30.11:8080 | IR | 1602 | 4 | 4/4 |
| http://102.165.58.199:8080 | KH | 5429 | 4 | 4/4 |
| http://206.135.12.153:999 | MX | 4472 | 4 | 12/42 |
| http://122.3.77.27:8082 | PH | 3998 | 4 | 18/130 |
| http://222.127.206.145:8085 | PH | 1862 | 4 | 10/81 |
| http://110.93.218.62:8080 | PK | 4260 | 4 | 8/20 |
| http://185.238.238.29:58080 | PL | 5426 | 4 | 52/133 |
| http://94.179.153.218:8081 | UA | 7525 | 4 | 24/121 |
| http://195.226.213.254:8888 | UA | 4863 | 4 | 51/139 |
| socks5://144.217.107.25:1080 | CA | 3927 | 4 | 28/51 |
| socks5://14.36.232.55:1080 | KR | 4069 | 4 | 4/4 |
| socks5://31.41.227.175:2080 | RU | 3818 | 4 | 9/24 |
| socks5://52.128.241.109:1080 | US | 271 | 4 | 13/22 |
| http://109.236.45.95:8989 | AL | 5690 | 3 | 38/137 |
| http://181.209.114.220:8080 | AR | 1918 | 3 | 11/85 |
| http://3.26.199.107:9904 | AU | 3971 | 3 | 12/51 |
| http://16.51.5.77:16637 | AU | 3471 | 3 | 19/81 |
| http://16.51.53.116:23517 | AU | 6619 | 3 | 18/57 |
| http://27.147.153.179:9249 | BD | 2185 | 3 | 5/8 |
| http://103.109.96.180:1994 | BD | 3952 | 3 | 5/10 |
| http://118.179.152.122:81 | BD | 7855 | 3 | 29/119 |
| http://213.169.33.3:8001 | BG | 4521 | 3 | 10/57 |
| http://18.228.228.159:52664 | BR | 4487 | 3 | 12/43 |
| http://18.231.214.206:14559 | BR | 2404 | 3 | 30/119 |
| http://164.163.237.196:9091 | BR | 4128 | 3 | 8/34 |
| http://201.91.248.67:20183 | BR | 5584 | 3 | 14/81 |
| http://201.157.235.197:8080 | BR | 5327 | 3 | 13/80 |
