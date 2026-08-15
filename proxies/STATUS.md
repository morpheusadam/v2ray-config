# Proxy status

Generated 2026-08-15T13:30:52Z by `harvest.py`.

- **488** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **841** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11988** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 170/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 603 |
| socks5 | 221 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 145 |
| US | 64 |
| RU | 49 |
| VN | 41 |
| CN | 39 |
| NL | 33 |
| CO | 32 |
| PH | 26 |
| BD | 24 |
| MX | 24 |
| FR | 23 |
| DE | 21 |
| SG | 21 |
| BR | 18 |
| HK | 18 |
| TR | 18 |
| IN | 17 |
| JP | 15 |
| VE | 15 |
| EC | 11 |
| TH | 11 |
| GB | 10 |
| KH | 10 |
| DO | 8 |
| FI | 8 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 4 | 2026-08-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 49 | 49 | 33 | 2026-08-15 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 119 | 119 | 67 | 2026-08-15 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 83 | 2026-08-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 157 | 157 | 62 | 2026-08-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 157 | 157 | 29 | 2026-08-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 179 | 179 | 15 | 2026-08-15 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 229 | 229 | 77 | 2026-08-15 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 240 | 240 | 43 | 2026-08-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-15 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 323 | 323 | 160 | 2026-08-15 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-15 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 535 | 2026-08-15 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-08-15 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1378 | 1374 | 114 | 2026-08-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1129 | 2026-08-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1776 | 1774 | 197 | 2026-08-15 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1625 | 2026-08-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2308 | 2306 | 725 | 2026-08-15 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2505 | 2505 | 1888 | 2026-08-15 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2652 | 2650 | 2232 | 2026-08-15 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 3816 | 10 | 10/10 |
| http://87.251.77.29:3128 | DE | 1038 | 10 | 10/10 |
| http://103.237.102.191:11111 | DE | 1335 | 10 | 10/10 |
| http://176.111.37.5:39811 | HK | 978 | 10 | 10/10 |
| http://176.111.37.216:39811 | HK | 912 | 10 | 10/10 |
| http://103.130.61.61:8081 | ID | 1482 | 10 | 10/10 |
| http://1.231.81.166:3128 | KR | 1089 | 10 | 10/10 |
| http://95.211.64.139:8889 | NL | 2035 | 10 | 10/10 |
| http://95.211.174.135:3128 | NL | 1202 | 10 | 10/10 |
| http://204.76.203.9:3128 | NL | 781 | 10 | 10/10 |
| http://185.200.188.234:10001 | RU | 1084 | 10 | 10/10 |
| http://152.42.167.241:3128 | SG | 1815 | 10 | 10/10 |
| http://202.28.194.139:31280 | TH | 2709 | 10 | 10/10 |
| http://95.3.69.222:8080 | TR | 1479 | 10 | 10/10 |
| http://43.153.82.179:8888 | US | 426 | 10 | 10/10 |
| http://64.112.184.210:3128 | US | 408 | 10 | 10/10 |
| socks5://66.163.118.99:10006 | ES | 3302 | 10 | 10/10 |
| socks5://144.91.121.61:1088 | FR | 2132 | 10 | 10/10 |
| socks5://212.58.132.5:1080 | GB | 1809 | 10 | 10/10 |
| socks5://66.163.119.55:10006 | IT | 1032 | 10 | 10/10 |
| socks5://149.62.186.244:1080 | IT | 2273 | 10 | 10/10 |
| socks5://101.36.104.46:10808 | JP | 1242 | 10 | 10/10 |
| socks5://193.233.218.213:1080 | RU | 2540 | 10 | 10/10 |
| socks5://69.55.49.177:38182 | US | 516 | 10 | 10/10 |
| socks5://193.25.215.182:22222 | US | 924 | 10 | 10/10 |
| http://95.211.64.139:8887 | NL | 937 | 9 | 9/9 |
| http://153.80.240.37:8080 | NL | 7859 | 8 | 9/10 |
| http://34.94.46.8:80 | US | 193 | 8 | 8/8 |
| socks5://45.43.63.37:10808 | SG | 1596 | 8 | 9/10 |
| http://181.39.25.196:8118 | EC | 1101 | 7 | 9/10 |
| http://130.110.103.245:3128 | SA | 1200 | 7 | 9/10 |
| socks5://51.159.97.242:10006 | FR | 5912 | 7 | 9/10 |
| socks5://109.199.105.194:1080 | FR | 2309 | 7 | 7/7 |
| socks5://43.164.136.189:1080 | KR | 4424 | 7 | 8/10 |
| socks5://45.10.42.68:1080 | NL | 4339 | 7 | 7/7 |
| socks5://5.249.165.195:20000 | US | 5013 | 7 | 7/7 |
| http://114.94.148.37:18080 | CN | 5558 | 6 | 8/9 |
| http://190.0.246.210:4040 | CO | 3900 | 6 | 8/9 |
| http://37.59.125.131:8888 | FR | 1031 | 6 | 9/10 |
| http://95.211.64.139:8886 | NL | 734 | 6 | 6/6 |
| http://216.106.182.177:3128 | US | 479 | 6 | 9/10 |
| socks5://47.250.211.53:1080 | MY | 1482 | 6 | 9/10 |
| socks5://151.115.99.193:10006 | PL | 6510 | 6 | 8/10 |
| socks5://45.61.129.165:9050 | US | 4591 | 6 | 8/10 |
| http://123.57.213.24:3539 | CN | 2691 | 5 | 6/9 |
| http://159.195.49.27:8888 | DE | 1471 | 5 | 7/10 |
| http://175.136.239.173:8181 | MY | 4573 | 5 | 8/10 |
| http://175.143.76.177:8181 | MY | 7026 | 5 | 9/10 |
| socks5://59.152.97.233:1080 | BD | 2919 | 5 | 7/8 |
| socks5://144.91.111.48:1088 | FR | 1595 | 5 | 8/10 |
| http://201.116.64.226:7734 | MX | 2232 | 4 | 5/6 |
| http://109.94.1.23:4050 | RU | 5092 | 4 | 9/10 |
| http://5.161.50.82:8118 | US | 864 | 4 | 5/9 |
| socks4://89.169.168.25:6101 | RU | 2443 | 4 | 5/10 |
| socks5://59.38.113.185:20000 | CN | 5645 | 4 | 8/10 |
| socks5://112.90.88.102:20000 | CN | 2018 | 4 | 4/4 |
| socks5://151.243.224.12:1080 | DE | 2462 | 4 | 4/4 |
| socks5://144.24.111.128:1088 | IN | 1567 | 4 | 8/10 |
| socks5://89.208.106.37:32712 | NL | 7595 | 4 | 5/6 |
| socks5://62.113.113.114:1080 | RU | 6817 | 4 | 6/10 |
| socks5://144.24.47.42:1080 | US | 3362 | 4 | 5/6 |
| http://47.107.82.96:30051 | CN | 5105 | 3 | 3/3 |
| http://45.176.99.58:999 | DO | 7679 | 3 | 4/5 |
| http://152.0.51.69:8080 | DO | 6060 | 3 | 3/3 |
| http://18.170.25.193:53656 | GB | 5608 | 3 | 5/10 |
| http://103.80.214.108:8080 | ID | 4111 | 3 | 3/3 |
| http://103.106.216.231:8097 | ID | 4089 | 3 | 4/5 |
| http://103.169.38.186:8080 | ID | 3796 | 3 | 3/3 |
| http://103.175.202.182:8090 | ID | 7226 | 3 | 5/6 |
| http://103.246.194.251:3128 | IN | 3148 | 3 | 4/8 |
| http://185.191.106.0:8081 | IT | 3231 | 3 | 5/10 |
| http://140.238.32.108:3128 | JP | 4827 | 3 | 7/9 |
| http://204.76.203.9:8080 | NL | 691 | 3 | 3/3 |
| http://79.137.192.65:30081 | RU | 3395 | 3 | 6/10 |
| http://95.189.35.234:81 | RU | 1798 | 3 | 5/8 |
| http://43.156.236.238:80 | SG | 961 | 3 | 5/8 |
| http://195.158.8.123:3128 | UZ | 7831 | 3 | 7/8 |
| socks5://147.45.221.111:1082 | AL | 2850 | 3 | 3/3 |
| socks5://147.45.221.115:1082 | AL | 3871 | 3 | 6/10 |
| socks5://204.168.225.35:9082 | FI | 3109 | 3 | 5/9 |
| socks5://45.194.33.12:30001 | HK | 3686 | 3 | 5/6 |
| socks5://154.203.132.81:5080 | HK | 1508 | 3 | 3/3 |
| socks5://121.169.46.116:1090 | KR | 1286 | 3 | 8/10 |
| socks5://87.239.251.202:1081 | NL | 7526 | 3 | 5/8 |
| socks5://139.28.240.201:1082 | NL | 831 | 3 | 5/9 |
| socks5://80.93.61.39:1080 | RU | 1154 | 3 | 3/3 |
| socks5://109.172.7.42:1080 | RU | 1486 | 3 | 3/3 |
| socks5://34.229.113.62:1080 | US | 2344 | 3 | 3/3 |
| http://187.102.219.42:999 | AR | 1219 | 2 | 3/5 |
| http://54.253.183.151:26543 | AU | 3206 | 2 | 3/4 |
| http://54.253.183.151:443 | AU | 2484 | 2 | 2/2 |
| http://45.168.244.10:9090 | BR | 5170 | 2 | 2/2 |
| http://179.48.25.1:8095 | BR | 7199 | 2 | 3/5 |
| http://179.48.80.9:8085 | BR | 4650 | 2 | 2/2 |
| http://184.70.113.34:3128 | CA | 7629 | 2 | 4/8 |
| http://101.206.186.99:8080 | CN | 2398 | 2 | 6/10 |
| http://115.231.181.40:8128 | CN | 3740 | 2 | 5/9 |
| http://219.142.66.244:9090 | CN | 3097 | 2 | 5/10 |
| http://223.85.21.195:8080 | CN | 7851 | 2 | 4/8 |
| http://181.204.81.178:999 | CO | 3057 | 2 | 2/2 |
