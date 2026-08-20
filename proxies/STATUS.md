# Proxy status

Generated 2026-08-20T20:00:27Z by `harvest.py`.

- **452** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1220** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13250** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 118/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 961 |
| socks5 | 241 |
| socks4 | 18 |

| country | entries |
|---|---|
| ID | 262 |
| US | 95 |
| RU | 56 |
| CO | 47 |
| CN | 43 |
| PH | 40 |
| BR | 39 |
| BD | 37 |
| FR | 35 |
| MX | 33 |
| NL | 33 |
| DE | 26 |
| HK | 25 |
| TR | 25 |
| EC | 24 |
| IN | 23 |
| SG | 23 |
| VE | 22 |
| EG | 20 |
| JP | 20 |
| VN | 16 |
| AU | 14 |
| IR | 13 |
| PK | 13 |
| PL | 12 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-08-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 83 | 83 | 45 | 2026-08-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 93 | 93 | 42 | 2026-08-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 115 | 115 | 30 | 2026-08-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 118 | 118 | 32 | 2026-08-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 141 | 141 | 69 | 2026-08-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 141 | 141 | 3 | 2026-08-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 91 | 2026-08-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 190 | 190 | 70 | 2026-08-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 201 | 201 | 67 | 2026-08-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-08-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-08-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-08-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1607 | 2026-08-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1934 | 1930 | 195 | 2026-08-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1969 | 1967 | 163 | 2026-08-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2221 | 2221 | 1853 | 2026-08-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2457 | 2455 | 663 | 2026-08-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2631 | 2629 | 2096 | 2026-08-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://64.112.184.210:3128 | US | 216 | 21 | 21/21 |
| http://181.39.25.196:8118 | EC | 723 | 18 | 20/21 |
| http://34.43.46.91:443 | US | 471 | 13 | 18/21 |
| http://34.43.46.91:80 | US | 611 | 13 | 18/21 |
| http://181.78.74.252:999 | CO | 719 | 12 | 12/12 |
| http://181.78.74.253:999 | CO | 705 | 12 | 12/12 |
| http://190.97.236.128:999 | VE | 1676 | 11 | 11/11 |
| http://190.97.236.129:999 | VE | 632 | 11 | 11/11 |
| http://49.51.253.118:8888 | US | 3807 | 8 | 8/8 |
| http://47.107.82.96:30051 | CN | 1919 | 7 | 12/14 |
| http://103.237.102.191:11111 | DE | 2060 | 7 | 20/21 |
| http://212.58.132.5:8888 | GB | 5006 | 7 | 16/20 |
| http://176.111.37.216:39811 | HK | 2573 | 7 | 19/21 |
| http://1.231.81.166:3128 | KR | 1812 | 7 | 20/21 |
| http://95.211.174.135:3128 | NL | 1250 | 7 | 20/21 |
| http://204.76.203.9:3128 | NL | 2575 | 7 | 20/21 |
| http://204.76.203.9:8080 | NL | 547 | 7 | 13/14 |
| http://185.141.26.131:3128 | RO | 511 | 7 | 7/7 |
| http://185.200.188.234:10001 | RU | 2175 | 7 | 20/21 |
| http://130.110.103.245:3128 | SA | 2779 | 7 | 19/21 |
| http://202.28.194.139:31280 | TH | 2496 | 7 | 20/21 |
| http://95.3.69.222:8080 | TR | 2785 | 7 | 20/21 |
| http://45.66.249.187:3128 | US | 544 | 7 | 11/12 |
| http://45.66.249.187:8181 | US | 558 | 7 | 11/12 |
| socks4://45.61.129.165:9050 | US | 1996 | 7 | 18/21 |
| socks5://45.144.54.40:1080 | DE | 2760 | 7 | 15/21 |
| socks5://144.91.121.61:1088 | FR | 1679 | 7 | 20/21 |
| socks5://150.241.91.238:7777 | FR | 7395 | 7 | 7/7 |
| socks5://212.58.132.5:1080 | GB | 2500 | 7 | 20/21 |
| socks5://144.24.111.128:1088 | IN | 1906 | 7 | 16/21 |
| socks5://178.128.82.131:10808 | SG | 5264 | 7 | 12/21 |
| http://87.251.77.29:3128 | DE | 705 | 6 | 19/21 |
| http://216.106.182.177:3128 | US | 453 | 6 | 18/21 |
| socks5://103.111.136.82:8199 | ID | 6090 | 6 | 8/16 |
| http://45.176.99.58:999 | DO | 3079 | 5 | 11/16 |
| http://80.241.214.192:3128 | FR | 5750 | 5 | 5/5 |
| http://46.247.41.222:443 | KZ | 4985 | 5 | 8/11 |
| http://195.158.8.123:3128 | UZ | 3933 | 5 | 15/19 |
| socks5://85.209.120.145:1080 | TR | 6559 | 5 | 6/7 |
| http://185.191.239.248:3128 | CH | 2006 | 4 | 12/20 |
| http://116.196.150.180:17981 | CN | 2263 | 4 | 8/21 |
| http://95.40.233.164:3128 | HK | 2138 | 4 | 4/4 |
| http://43.160.242.118:3128 | SG | 2210 | 4 | 15/18 |
| http://13.221.202.200:3128 | US | 79 | 4 | 4/4 |
| http://98.83.197.228:3128 | US | 80 | 4 | 4/4 |
| http://199.7.149.90:3128 | US | 40 | 4 | 4/4 |
| socks5://185.185.80.58:1088 | FR | 5115 | 4 | 14/20 |
| socks5://101.36.104.46:10808 | JP | 2197 | 4 | 19/21 |
| socks5://101.36.104.239:10808 | JP | 6020 | 4 | 17/21 |
| socks5://103.75.118.84:1080 | JP | 3294 | 4 | 10/16 |
| socks5://121.169.46.116:1090 | KR | 5398 | 4 | 14/21 |
| socks5://45.43.63.37:10808 | SG | 3157 | 4 | 18/21 |
| http://123.57.213.24:3539 | CN | 2495 | 3 | 12/20 |
| http://152.0.51.69:8080 | DO | 7234 | 3 | 6/14 |
| http://45.71.0.121:999 | EC | 4236 | 3 | 5/8 |
| http://41.65.236.37:8080 | EG | 5017 | 3 | 3/3 |
| http://103.180.118.150:8080 | ID | 5285 | 3 | 4/6 |
| http://185.78.113.230:81 | RU | 1182 | 3 | 6/17 |
| socks4://89.169.168.25:6101 | RU | 3643 | 3 | 9/21 |
| socks5://65.21.252.66:10801 | FI | 4153 | 3 | 6/9 |
| socks5://203.189.150.44:1080 | KH | 5038 | 3 | 7/21 |
| socks5://67.210.146.50:11080 | US | 1562 | 3 | 7/17 |
| socks5://193.25.215.182:22222 | US | 1423 | 3 | 19/21 |
| http://103.161.69.252:2698 | BD | 5720 | 2 | 9/21 |
| http://103.177.118.145:8118 | BD | 1474 | 2 | 2/2 |
| http://122.246.3.210:17981 | CN | 2086 | 2 | 10/21 |
| http://200.10.28.13:999 | CO | 7066 | 2 | 4/20 |
| http://38.75.82.220:999 | DO | 6894 | 2 | 2/2 |
| http://177.234.217.84:999 | EC | 5663 | 2 | 7/16 |
| http://190.12.150.244:999 | EC | 6204 | 2 | 12/17 |
| http://41.196.16.233:1981 | EG | 2260 | 2 | 4/6 |
| http://84.36.141.180:1976 | EG | 3561 | 2 | 3/7 |
| http://176.111.37.5:39811 | HK | 2681 | 2 | 19/21 |
| http://45.198.10.227:3128 | ID | 5019 | 2 | 2/2 |
| http://103.61.16.9:8097 | ID | 5499 | 2 | 5/17 |
| http://103.167.68.84:8080 | ID | 3595 | 2 | 8/19 |
| http://157.66.51.201:8080 | ID | 5645 | 2 | 5/18 |
| http://164.52.216.153:8080 | IN | 1646 | 2 | 5/16 |
| http://112.216.54.226:12121 | KR | 2270 | 2 | 6/15 |
| http://89.213.106.25:999 | MX | 1407 | 2 | 2/2 |
| http://201.46.86.37:8080 | MX | 6604 | 2 | 6/19 |
| http://175.136.239.174:8181 | MY | 5740 | 2 | 12/21 |
| http://72.56.109.88:3128 | NL | 1540 | 2 | 3/19 |
| http://185.238.238.137:58080 | PL | 7160 | 2 | 6/17 |
| socks5://147.45.66.116:1082 | DE | 5001 | 2 | 9/20 |
| socks5://195.133.65.238:10909 | DE | 5840 | 2 | 7/20 |
| socks5://81.0.49.104:18500 | ES | 4993 | 2 | 4/18 |
| socks5://109.172.55.177:1082 | FR | 2897 | 2 | 10/21 |
| socks5://134.209.18.113:1088 | GB | 1889 | 2 | 2/2 |
| socks5://43.164.136.189:1080 | KR | 1932 | 2 | 12/21 |
| socks5://150.230.249.50:1080 | KR | 1326 | 2 | 2/2 |
| socks5://47.250.115.134:1080 | MY | 1686 | 2 | 5/19 |
| socks5://66.151.32.105:1080 | NL | 752 | 2 | 2/2 |
| socks5://144.124.232.204:443 | NL | 714 | 2 | 4/15 |
| socks5://103.239.201.50:58765 | PH | 5850 | 2 | 3/6 |
| socks5://147.45.60.139:1082 | US | 138 | 2 | 9/12 |
| socks5://216.106.179.216:49398 | US | 4342 | 2 | 3/14 |
| http://168.196.227.203:999 | AR | 6337 | 1 | 5/15 |
| http://191.97.96.86:8080 | AR | 6943 | 1 | 2/4 |
| http://15.135.215.62:7028 | AU | 7083 | 1 | 1/1 |
