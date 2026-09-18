# Proxy status

Generated 2026-09-18T21:50:48Z by `harvest.py`.

- **1233** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2658** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **27468** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 165/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1475 |
| socks5 | 1182 |
| socks4 | 1 |

| country | entries |
|---|---|
| NL | 950 |
| ID | 281 |
| US | 157 |
| CN | 126 |
| RU | 80 |
| MX | 61 |
| DE | 60 |
| IN | 56 |
| SG | 56 |
| BD | 53 |
| PH | 53 |
| VE | 42 |
| CO | 39 |
| FR | 36 |
| TH | 35 |
| VN | 35 |
| JP | 34 |
| HK | 33 |
| BR | 31 |
| EG | 31 |
| EC | 28 |
| FI | 22 |
| CA | 19 |
| ZA | 19 |
| DO | 18 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 67 | 67 | 30 | 2026-09-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 80 | 80 | 21 | 2026-09-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 84 | 84 | 22 | 2026-09-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 90 | 90 | 52 | 2026-09-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-09-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 153 | 153 | 26 | 2026-09-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 250 | 250 | 107 | 2026-09-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 349 | 349 | 172 | 2026-09-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-09-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1146 | 2026-09-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1605 | 2026-09-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1843 | 1841 | 486 | 2026-09-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2618 | 2616 | 624 | 2026-09-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2792 | 2790 | 2076 | 2026-09-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2819 | 2817 | 536 | 2026-09-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 11956 | 11956 | 6951 | 2026-09-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 18320 | 18319 | 2504 | 2026-09-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 827 | 71 | 76/79 |
| http://34.43.46.91:80 | US | 776 | 71 | 76/79 |
| http://95.211.174.135:3128 | NL | 1052 | 65 | 78/79 |
| http://185.200.188.234:10001 | RU | 6420 | 65 | 78/79 |
| http://130.110.103.245:3128 | SA | 1539 | 65 | 77/79 |
| http://1.231.81.166:3128 | KR | 1621 | 44 | 76/79 |
| http://190.97.236.128:999 | VE | 1689 | 36 | 67/69 |
| http://190.97.236.129:999 | VE | 681 | 36 | 67/69 |
| http://95.3.69.222:8080 | TR | 1395 | 34 | 76/79 |
| socks5://107.167.18.122:443 | US | 382 | 24 | 30/31 |
| socks5://83.147.216.208:1080 | FI | 900 | 23 | 29/47 |
| http://184.75.221.82:3118 | CA | 237 | 20 | 41/44 |
| http://91.134.141.4:3128 | FR | 513 | 18 | 38/40 |
| http://186.5.94.206:999 | EC | 1834 | 16 | 39/41 |
| http://107.150.41.226:18080 | US | 600 | 16 | 16/16 |
| http://190.0.246.210:4040 | CO | 790 | 12 | 69/78 |
| http://186.33.45.219:999 | EC | 3826 | 12 | 42/68 |
| http://38.51.207.104:8080 | VE | 1508 | 12 | 19/20 |
| socks5://103.162.30.189:10808 | VN | 2230 | 11 | 13/14 |
| http://34.88.38.81:9443 | FI | 785 | 10 | 31/44 |
| http://35.228.49.168:9443 | FI | 640 | 10 | 12/16 |
| http://197.224.185.3:3128 | MU | 2011 | 10 | 43/47 |
| http://189.51.168.164:999 | MX | 323 | 10 | 43/44 |
| http://45.132.252.25:49156 | RU | 882 | 10 | 10/10 |
| http://5.129.254.5:8888 | RU | 2068 | 9 | 32/34 |
| http://5.129.254.49:8888 | RU | 1068 | 9 | 33/34 |
| http://5.129.254.51:8888 | RU | 2798 | 9 | 33/34 |
| http://5.129.254.60:8888 | RU | 1317 | 9 | 32/33 |
| http://5.129.254.70:8888 | RU | 2001 | 9 | 33/34 |
| http://5.129.254.129:8888 | RU | 1022 | 9 | 38/40 |
| http://5.129.254.154:8888 | RU | 2116 | 9 | 29/30 |
| http://193.104.179.115:3128 | UZ | 1172 | 9 | 27/44 |
| http://120.232.115.170:17981 | CN | 2936 | 8 | 57/78 |
| http://190.0.246.211:4040 | CO | 809 | 8 | 67/79 |
| http://190.0.246.213:4040 | CO | 485 | 8 | 37/44 |
| http://213.111.146.36:18080 | NL | 1501 | 8 | 11/16 |
| http://157.85.108.47:3128 | TH | 1336 | 8 | 36/47 |
| socks5://101.36.104.46:10808 | JP | 1943 | 8 | 70/79 |
| socks5://144.24.47.42:1080 | US | 5509 | 8 | 43/75 |
| http://221.221.159.97:8888 | CN | 4004 | 7 | 14/32 |
| http://167.172.76.176:9090 | SG | 1237 | 7 | 22/40 |
| socks5://121.169.46.116:1090 | KR | 4335 | 7 | 52/79 |
| http://39.106.170.168:8080 | CN | 3116 | 6 | 40/77 |
| http://45.186.6.104:3128 | EC | 683 | 6 | 55/57 |
| http://186.33.45.220:999 | EC | 4897 | 6 | 24/48 |
| http://194.31.108.109:2080 | IR | 1167 | 6 | 25/39 |
| http://77.73.68.222:65000 | RU | 811 | 6 | 6/6 |
| http://61.91.162.126:8080 | TH | 1570 | 6 | 19/22 |
| http://103.10.231.189:8080 | TH | 1628 | 6 | 44/64 |
| http://153.51.201.35:999 | VE | 749 | 6 | 6/6 |
| http://154.3.76.14:999 | VE | 4516 | 6 | 23/32 |
| http://210.211.113.33:80 | VN | 2769 | 6 | 28/49 |
| http://187.102.219.42:999 | AR | 1367 | 5 | 39/74 |
| http://8.138.217.152:21001 | CN | 3343 | 5 | 54/79 |
| http://123.121.123.216:8888 | CN | 1553 | 5 | 14/39 |
| http://152.53.183.107:8081 | DE | 1622 | 5 | 21/32 |
| http://190.12.150.244:999 | EC | 4043 | 5 | 49/75 |
| http://65.109.217.164:3128 | FI | 657 | 5 | 11/12 |
| http://176.111.37.216:39811 | HK | 951 | 5 | 65/79 |
| http://38.194.246.34:999 | MX | 2170 | 5 | 42/70 |
| http://206.135.56.50:8080 | MX | 2226 | 5 | 14/38 |
| http://152.42.177.32:8888 | SG | 1163 | 5 | 21/39 |
| http://201.71.2.24:999 | VE | 4609 | 5 | 24/67 |
| http://201.71.2.25:999 | VE | 7189 | 5 | 20/66 |
| http://201.71.2.27:999 | VE | 3094 | 5 | 26/77 |
| socks5://36.155.23.163:10808 | CN | 7941 | 5 | 10/16 |
| http://47.107.82.96:30051 | CN | 1778 | 4 | 42/72 |
| http://61.149.135.125:8888 | CN | 1916 | 4 | 19/39 |
| http://114.252.13.224:8888 | CN | 1279 | 4 | 16/43 |
| http://123.115.177.103:8888 | CN | 1655 | 4 | 4/4 |
| http://123.119.179.101:8888 | CN | 1195 | 4 | 16/37 |
| http://123.119.179.161:8888 | CN | 1218 | 4 | 19/44 |
| http://123.121.209.61:8888 | CN | 2376 | 4 | 12/44 |
| http://221.221.163.25:8888 | CN | 1234 | 4 | 13/33 |
| http://222.128.173.231:8888 | CN | 1640 | 4 | 18/47 |
| http://18.157.123.132:3128 | DE | 540 | 4 | 28/40 |
| http://177.234.217.237:999 | EC | 2564 | 4 | 21/52 |
| http://41.33.245.138:1981 | EG | 977 | 4 | 5/9 |
| http://213.136.72.147:3128 | FR | 1067 | 4 | 4/4 |
| http://94.43.164.242:8080 | GE | 7646 | 4 | 8/13 |
| http://203.177.217.222:8082 | PH | 4899 | 4 | 13/24 |
| http://43.128.112.151:80 | SG | 1160 | 4 | 10/18 |
| http://43.153.195.69:80 | SG | 1176 | 4 | 12/19 |
| http://43.156.153.104:8080 | SG | 4195 | 4 | 7/8 |
| http://43.163.120.171:8080 | SG | 2308 | 4 | 4/4 |
| http://43.163.124.191:8080 | SG | 1643 | 4 | 4/4 |
| http://124.156.194.52:8081 | SG | 1627 | 4 | 11/14 |
| http://129.226.89.151:80 | SG | 1179 | 4 | 17/26 |
| http://157.85.97.204:3128 | TH | 4408 | 4 | 33/44 |
| http://172.210.12.8:3128 | US | 400 | 4 | 5/15 |
| http://190.97.229.118:999 | VE | 1951 | 4 | 34/69 |
| http://190.97.236.130:999 | VE | 648 | 4 | 7/8 |
| http://190.97.241.106:999 | VE | 2585 | 4 | 39/63 |
| http://200.8.54.44:999 | VE | 6754 | 4 | 6/17 |
| http://103.102.131.30:3128 | VN | 3841 | 4 | 4/4 |
| http://103.218.122.183:8080 | VN | 1361 | 4 | 22/50 |
| socks5://59.152.97.233:1080 | BD | 2155 | 4 | 49/77 |
| socks5://5.45.119.70:1080 | EE | 753 | 4 | 43/77 |
| socks5://45.74.31.41:15538 | NL | 1667 | 4 | 4/4 |
| socks5://193.233.223.47:1080 | RU | 1133 | 4 | 4/4 |
