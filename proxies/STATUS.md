# Proxy status

Generated 2026-08-16T13:33:32Z by `harvest.py`.

- **673** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1035** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **12695** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 215/600 (36%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 756 |
| socks5 | 261 |
| socks4 | 18 |

| country | entries |
|---|---|
| ID | 198 |
| US | 77 |
| RU | 64 |
| CN | 44 |
| VN | 44 |
| CO | 43 |
| NL | 37 |
| MX | 33 |
| PH | 30 |
| BR | 28 |
| BD | 24 |
| FR | 24 |
| TR | 24 |
| DE | 23 |
| IN | 23 |
| VE | 22 |
| HK | 21 |
| JP | 20 |
| EC | 19 |
| SG | 18 |
| FI | 16 |
| DO | 14 |
| GB | 10 |
| PE | 10 |
| PL | 10 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-08-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 69 | 69 | 37 | 2026-08-16 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-08-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 129 | 129 | 19 | 2026-08-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 149 | 149 | 64 | 2026-08-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 76 | 2026-08-16 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 161 | 161 | 30 | 2026-08-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 204 | 204 | 10 | 2026-08-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 214 | 214 | 122 | 2026-08-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 299 | 299 | 124 | 2026-08-16 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 468 | 468 | 215 | 2026-08-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 533 | 2026-08-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-08-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-08-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1624 | 2026-08-16 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1857 | 1853 | 167 | 2026-08-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2123 | 2121 | 182 | 2026-08-16 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2481 | 2481 | 1906 | 2026-08-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2625 | 2623 | 717 | 2026-08-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2942 | 2940 | 2440 | 2026-08-16 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1618 | 12 | 12/12 |
| http://87.251.77.29:3128 | DE | 1065 | 12 | 12/12 |
| http://103.237.102.191:11111 | DE | 1223 | 12 | 12/12 |
| http://176.111.37.5:39811 | HK | 1796 | 12 | 12/12 |
| http://1.231.81.166:3128 | KR | 1480 | 12 | 12/12 |
| http://95.211.64.139:8889 | NL | 749 | 12 | 12/12 |
| http://95.211.174.135:3128 | NL | 1197 | 12 | 12/12 |
| http://204.76.203.9:3128 | NL | 824 | 12 | 12/12 |
| http://185.200.188.234:10001 | RU | 1623 | 12 | 12/12 |
| http://152.42.167.241:3128 | SG | 1661 | 12 | 12/12 |
| http://202.28.194.139:31280 | TH | 3203 | 12 | 12/12 |
| http://95.3.69.222:8080 | TR | 1505 | 12 | 12/12 |
| http://64.112.184.210:3128 | US | 522 | 12 | 12/12 |
| socks5://144.91.121.61:1088 | FR | 3505 | 12 | 12/12 |
| socks5://212.58.132.5:1080 | GB | 2167 | 12 | 12/12 |
| socks5://66.163.119.55:10006 | IT | 1326 | 12 | 12/12 |
| socks5://101.36.104.46:10808 | JP | 4671 | 12 | 12/12 |
| socks5://193.233.218.213:1080 | RU | 1648 | 12 | 12/12 |
| socks5://69.55.49.177:38182 | US | 665 | 12 | 12/12 |
| socks5://193.25.215.182:22222 | US | 1154 | 12 | 12/12 |
| http://95.211.64.139:8887 | NL | 1184 | 11 | 11/11 |
| socks5://45.43.63.37:10808 | SG | 1833 | 10 | 11/12 |
| http://181.39.25.196:8118 | EC | 1126 | 9 | 11/12 |
| http://130.110.103.245:3128 | SA | 1530 | 9 | 11/12 |
| socks5://51.159.97.242:10006 | FR | 5620 | 9 | 11/12 |
| socks5://109.199.105.194:1080 | FR | 3997 | 9 | 9/9 |
| http://190.0.246.210:4040 | CO | 2339 | 8 | 10/11 |
| http://95.211.64.139:8886 | NL | 488 | 8 | 8/8 |
| http://216.106.182.177:3128 | US | 623 | 8 | 11/12 |
| socks4://151.115.99.193:10006 | PL | 2017 | 8 | 10/12 |
| socks4://45.61.129.165:9050 | US | 1848 | 8 | 10/12 |
| http://159.195.49.27:8888 | DE | 3395 | 7 | 9/12 |
| socks5://59.152.97.233:1080 | BD | 2097 | 7 | 9/10 |
| socks5://144.91.111.48:1088 | FR | 6740 | 7 | 10/12 |
| http://201.116.64.226:7734 | MX | 3621 | 6 | 7/8 |
| http://109.94.1.23:4050 | RU | 3066 | 6 | 11/12 |
| socks5://59.38.113.185:20000 | CN | 4444 | 6 | 10/12 |
| socks5://112.90.88.102:20000 | CN | 3417 | 6 | 6/6 |
| socks5://89.208.106.37:32712 | NL | 895 | 6 | 7/8 |
| socks5://62.113.113.114:1080 | RU | 3609 | 6 | 8/12 |
| socks5://144.24.47.42:1080 | US | 3542 | 6 | 7/8 |
| http://204.76.203.9:8080 | NL | 501 | 5 | 5/5 |
| http://79.137.192.65:30081 | RU | 3361 | 5 | 8/12 |
| http://195.158.8.123:3128 | UZ | 6746 | 5 | 9/10 |
| socks5://45.194.33.12:30001 | HK | 1538 | 5 | 7/8 |
| socks5://80.93.61.39:1080 | RU | 927 | 5 | 5/5 |
| socks5://34.229.113.62:1080 | US | 2881 | 5 | 5/5 |
| http://187.102.219.42:999 | AR | 1081 | 4 | 5/7 |
| http://101.206.186.99:8080 | CN | 2685 | 4 | 8/12 |
| http://212.58.132.5:8888 | GB | 3252 | 4 | 8/11 |
| http://49.156.22.42:8082 | ID | 6694 | 4 | 5/10 |
| http://165.99.194.184:8080 | ID | 6785 | 4 | 6/10 |
| http://14.139.235.82:3128 | IN | 2275 | 4 | 9/12 |
| http://95.211.64.139:8888 | NL | 961 | 4 | 11/12 |
| http://144.124.227.88:3128 | NL | 3176 | 4 | 5/6 |
| http://34.43.46.91:443 | US | 1640 | 4 | 9/12 |
| http://34.43.46.91:80 | US | 1520 | 4 | 9/12 |
| http://34.69.61.247:80 | US | 244 | 4 | 6/11 |
| http://8.138.217.152:21001 | CN | 4130 | 3 | 7/12 |
| http://181.78.74.252:999 | CO | 675 | 3 | 3/3 |
| http://181.78.74.253:999 | CO | 671 | 3 | 3/3 |
| http://190.7.138.78:8080 | CO | 6194 | 3 | 4/6 |
| http://43.133.128.153:16012 | ID | 4312 | 3 | 8/12 |
| http://117.236.124.166:3128 | IN | 3568 | 3 | 6/12 |
| http://38.194.246.34:999 | MX | 4607 | 3 | 3/3 |
| http://43.160.242.118:3128 | SG | 1159 | 3 | 8/9 |
| http://45.66.249.187:3128 | US | 465 | 3 | 3/3 |
| http://45.66.249.187:8080 | US | 416 | 3 | 5/7 |
| http://45.66.249.187:8181 | US | 755 | 3 | 3/3 |
| http://157.230.178.216:40000 | US | 941 | 3 | 10/11 |
| http://165.154.162.73:8888 | US | 1534 | 3 | 7/12 |
| socks5://119.148.20.109:22122 | BD | 5128 | 3 | 3/3 |
| socks5://123.58.219.171:10808 | HK | 4894 | 3 | 11/12 |
| socks5://185.125.200.80:1090 | NL | 897 | 3 | 3/3 |
| socks5://89.189.132.154:1080 | RU | 1643 | 3 | 3/3 |
| socks5://95.31.16.116:1081 | RU | 876 | 3 | 3/3 |
| socks5://130.193.43.183:1080 | RU | 908 | 3 | 3/3 |
| socks5://43.162.94.99:1080 | US | 5731 | 3 | 10/12 |
| socks5://45.76.164.255:1085 | US | 193 | 3 | 6/8 |
| socks5://129.151.9.55:10808 | US | 880 | 3 | 9/12 |
| socks5://147.45.60.139:1082 | US | 150 | 3 | 3/3 |
| socks5://178.130.47.21:1082 | US | 1637 | 3 | 6/11 |
| http://103.147.230.130:8090 | BD | 7019 | 2 | 2/2 |
| http://138.0.143.119:8080 | BR | 4308 | 2 | 2/2 |
| http://168.228.176.30:3139 | BR | 3314 | 2 | 2/2 |
| http://186.226.167.191:3128 | BR | 5561 | 2 | 2/2 |
| http://112.74.101.87:9999 | CN | 2485 | 2 | 2/2 |
| http://120.232.115.170:17981 | CN | 2737 | 2 | 5/11 |
| http://121.41.109.117:8888 | CN | 2119 | 2 | 3/6 |
| http://122.246.3.12:17981 | CN | 2981 | 2 | 3/6 |
| http://123.57.94.90:8888 | CN | 4385 | 2 | 4/10 |
| http://38.19.40.9:8083 | CO | 4699 | 2 | 3/4 |
| http://45.172.218.67:3028 | CO | 7115 | 2 | 2/2 |
| http://186.148.162.155:999 | CO | 5866 | 2 | 4/5 |
| http://38.44.17.142:999 | DO | 7589 | 2 | 4/5 |
| http://38.75.82.212:999 | DO | 6375 | 2 | 3/6 |
| http://181.78.200.27:999 | EC | 7358 | 2 | 3/8 |
| http://196.204.83.229:8080 | EG | 4693 | 2 | 4/9 |
| http://45.144.53.63:6015 | FI | 1835 | 2 | 2/2 |
| http://37.187.109.70:10111 | FR | 4051 | 2 | 6/12 |
