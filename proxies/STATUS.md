# Proxy status

Generated 2026-08-29T02:26:25Z by `harvest.py`.

- **859** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1642** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **14526** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 194/600 (32%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1384 |
| socks5 | 242 |
| socks4 | 16 |

| country | entries |
|---|---|
| ID | 296 |
| US | 101 |
| CN | 99 |
| MX | 59 |
| CO | 58 |
| DE | 54 |
| PH | 49 |
| FR | 47 |
| IN | 44 |
| BR | 43 |
| RU | 42 |
| TH | 40 |
| BD | 39 |
| EC | 38 |
| TR | 37 |
| VE | 35 |
| JP | 34 |
| NL | 34 |
| HK | 31 |
| SG | 30 |
| AU | 26 |
| VN | 22 |
| CA | 21 |
| DO | 21 |
| ZA | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 416 | 0 | 0 | 0 | 2026-08-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 57 | 57 | 30 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 74 | 74 | 33 | 2026-08-29 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 107 | 107 | 25 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 113 | 113 | 26 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 121 | 121 | 8 | 2026-08-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 123 | 123 | 61 | 2026-08-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 124 | 124 | 41 | 2026-08-29 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 162 | 162 | 37 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-08-29 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 481 | 481 | 155 | 2026-08-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-08-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 458 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1489 | 1487 | 226 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1156 | 2026-08-29 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1792 | 1789 | 655 | 2026-08-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1609 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1908 | 1906 | 656 | 2026-08-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2239 | 2237 | 1729 | 2026-08-29 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2321 | 2321 | 1832 | 2026-08-29 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 3581 | 34 | 36/37 |
| http://34.43.46.91:443 | US | 483 | 29 | 34/37 |
| http://34.43.46.91:80 | US | 769 | 29 | 34/37 |
| http://103.237.102.191:11111 | DE | 655 | 23 | 36/37 |
| http://95.211.174.135:3128 | NL | 930 | 23 | 36/37 |
| http://204.76.203.9:3128 | NL | 867 | 23 | 36/37 |
| http://204.76.203.9:8080 | NL | 528 | 23 | 29/30 |
| http://185.200.188.234:10001 | RU | 1452 | 23 | 36/37 |
| http://130.110.103.245:3128 | SA | 1180 | 23 | 35/37 |
| http://95.3.69.222:8080 | TR | 1279 | 23 | 36/37 |
| http://199.7.149.90:3128 | US | 37 | 20 | 20/20 |
| http://199.7.149.96:3128 | US | 44 | 16 | 16/16 |
| http://45.186.6.104:3128 | EC | 619 | 15 | 15/15 |
| http://64.112.184.210:3128 | US | 391 | 15 | 36/37 |
| socks5://123.58.219.171:10808 | HK | 2983 | 15 | 31/37 |
| http://190.0.246.210:4040 | CO | 1383 | 13 | 33/36 |
| http://103.130.61.61:8081 | ID | 5916 | 12 | 32/37 |
| http://42.96.18.62:1311 | VN | 1575 | 11 | 26/36 |
| socks5://144.91.121.61:1088 | FR | 1459 | 11 | 35/37 |
| http://176.111.37.5:39811 | HK | 941 | 10 | 32/37 |
| socks5://152.32.168.221:10808 | HK | 2748 | 10 | 20/26 |
| http://179.41.11.138:8080 | AR | 934 | 9 | 9/9 |
| http://185.191.239.248:3128 | CH | 1000 | 9 | 26/36 |
| http://190.0.246.211:4040 | CO | 1701 | 9 | 32/37 |
| http://103.211.103.170:3128 | HK | 504 | 9 | 9/9 |
| http://202.28.194.139:31280 | TH | 2271 | 9 | 35/37 |
| http://154.59.56.73:999 | VE | 6729 | 9 | 9/9 |
| http://14.251.13.20:8080 | VN | 1394 | 9 | 9/9 |
| socks4://45.61.129.165:9050 | US | 2283 | 9 | 29/37 |
| socks5://101.36.104.46:10808 | JP | 2114 | 9 | 34/37 |
| http://87.251.77.29:3128 | DE | 771 | 8 | 34/37 |
| http://103.218.122.183:8080 | VN | 1419 | 8 | 8/8 |
| socks5://45.194.33.12:30001 | HK | 1473 | 8 | 26/33 |
| socks5://45.194.33.12:30002 | HK | 1451 | 8 | 10/11 |
| http://103.177.118.145:8118 | BD | 4641 | 7 | 17/18 |
| http://114.236.137.41:21000 | CN | 2025 | 7 | 25/37 |
| http://81.19.210.10:80 | GB | 568 | 7 | 7/7 |
| http://175.143.76.177:8181 | MY | 5617 | 7 | 27/37 |
| http://176.111.37.216:39811 | HK | 961 | 6 | 32/37 |
| http://185.28.155.163:1433 | IL | 801 | 6 | 6/6 |
| http://175.139.255.25:8181 | MY | 5872 | 6 | 29/37 |
| socks5://45.144.54.40:1080 | DE | 724 | 6 | 28/37 |
| socks5://103.75.118.84:1080 | JP | 3067 | 6 | 25/32 |
| http://15.135.215.62:7028 | AU | 3241 | 5 | 8/17 |
| http://54.206.129.120:41345 | AU | 3468 | 5 | 7/15 |
| http://87.237.15.238:7080 | BE | 527 | 5 | 5/5 |
| http://35.183.127.162:40229 | CA | 4211 | 5 | 7/17 |
| http://40.177.99.164:31822 | CA | 1889 | 5 | 10/37 |
| http://51.92.173.133:1090 | ES | 2067 | 5 | 6/15 |
| http://13.126.183.60:48293 | IN | 3465 | 5 | 5/5 |
| http://197.224.185.3:3128 | MU | 1834 | 5 | 5/5 |
| http://103.88.234.239:40013 | MX | 1449 | 5 | 7/8 |
| http://175.136.239.173:8181 | MY | 3568 | 5 | 29/37 |
| http://91.233.223.147:3128 | RU | 972 | 5 | 6/11 |
| http://157.85.97.240:3128 | TH | 1323 | 5 | 5/5 |
| http://157.85.105.217:3128 | TH | 1557 | 5 | 5/5 |
| http://157.85.108.47:3128 | TH | 1722 | 5 | 5/5 |
| http://157.85.108.62:3128 | TH | 1571 | 5 | 5/5 |
| http://157.85.108.68:3128 | TH | 2337 | 5 | 5/5 |
| http://157.85.111.64:3128 | TH | 2344 | 5 | 5/5 |
| http://18.222.132.180:54474 | US | 2326 | 5 | 9/31 |
| http://68.178.174.239:3128 | US | 1180 | 5 | 5/5 |
| http://68.178.174.239:8888 | US | 1429 | 5 | 5/5 |
| http://209.174.97.162:5999 | US | 1296 | 5 | 5/5 |
| socks5://77.239.106.24:1080 | DE | 6301 | 5 | 17/22 |
| http://16.26.154.68:53546 | AU | 3857 | 4 | 11/33 |
| http://8.138.217.152:21001 | CN | 4155 | 4 | 24/37 |
| http://115.231.181.40:8128 | CN | 1933 | 4 | 20/36 |
| http://181.78.23.187:999 | CO | 609 | 4 | 5/6 |
| http://181.78.74.252:999 | CO | 652 | 4 | 27/28 |
| http://181.78.74.253:999 | CO | 722 | 4 | 27/28 |
| http://18.157.159.247:9002 | DE | 812 | 4 | 4/4 |
| http://213.131.85.27:1976 | EG | 1359 | 4 | 6/10 |
| http://144.31.185.62:8080 | FI | 2468 | 4 | 5/7 |
| http://35.180.75.159:10645 | FR | 783 | 4 | 8/31 |
| http://47.57.69.227:3128 | HK | 2600 | 4 | 8/9 |
| http://43.218.128.7:11354 | ID | 2433 | 4 | 4/4 |
| http://15.152.34.197:55583 | JP | 2330 | 4 | 4/4 |
| http://43.207.132.28:50061 | JP | 2320 | 4 | 5/7 |
| http://43.200.179.23:41863 | KR | 3999 | 4 | 5/7 |
| http://43.216.197.62:39520 | MY | 3367 | 4 | 4/4 |
| http://109.94.1.23:4050 | RU | 6510 | 4 | 27/37 |
| http://13.60.163.108:39409 | SE | 4093 | 4 | 10/37 |
| http://47.129.166.112:49969 | SG | 5716 | 4 | 4/4 |
| http://212.115.103.200:8080 | TR | 3827 | 4 | 5/6 |
| http://100.61.113.24:4545 | US | 730 | 4 | 4/4 |
| http://190.97.236.128:999 | VE | 583 | 4 | 26/27 |
| http://190.97.236.129:999 | VE | 1609 | 4 | 26/27 |
| http://210.211.113.34:80 | VN | 3237 | 4 | 8/9 |
| http://210.211.113.35:80 | VN | 6954 | 4 | 7/9 |
| http://13.244.61.193:80 | ZA | 1842 | 4 | 4/4 |
| socks5://103.210.161.8:1080 | CN | 1374 | 4 | 8/10 |
| socks5://113.249.111.67:1080 | CN | 2853 | 4 | 4/4 |
| socks5://150.241.91.238:7777 | FR | 643 | 4 | 13/23 |
| socks5://34.84.162.206:38081 | JP | 1591 | 4 | 7/27 |
| socks5://45.12.18.106:1080 | RU | 963 | 4 | 4/4 |
| socks5://84.8.102.52:1080 | SA | 1385 | 4 | 4/4 |
| socks5://171.25.158.95:1080 | SE | 2577 | 4 | 15/36 |
| http://54.253.183.151:443 | AU | 3199 | 3 | 6/29 |
| http://47.107.82.96:30051 | CN | 3439 | 3 | 20/30 |
