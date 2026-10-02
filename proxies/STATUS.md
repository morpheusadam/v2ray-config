# Proxy status

Generated 2026-10-02T23:14:06Z by `harvest.py`.

- **3185** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5222** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39566** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 202/600 (34%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 3044 |
| http | 2174 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 2709 |
| ID | 591 |
| ?? | 284 |
| US | 138 |
| PH | 94 |
| CN | 89 |
| RU | 86 |
| MX | 84 |
| CO | 81 |
| IN | 56 |
| BR | 53 |
| TR | 53 |
| BD | 51 |
| EC | 48 |
| VE | 46 |
| SG | 43 |
| DE | 41 |
| VN | 38 |
| JP | 36 |
| DO | 34 |
| CA | 32 |
| KH | 27 |
| AR | 26 |
| HK | 26 |
| EG | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-10-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 41 | 41 | 16 | 2026-10-02 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 78 | 2026-10-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 115 | 115 | 38 | 2026-10-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 66 | 2026-10-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 185 | 185 | 44 | 2026-10-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 209 | 209 | 56 | 2026-10-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 399 | 399 | 165 | 2026-10-02 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 550 | 550 | 243 | 2026-10-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-10-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1043 | 1043 | 266 | 2026-10-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1142 | 2026-10-02 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1764 | 1760 | 0 | 2026-10-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1584 | 2026-10-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2368 | 2366 | 688 | 2026-10-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2546 | 2544 | 1762 | 2026-10-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2996 | 2994 | 806 | 2026-10-02 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 38200 | 38200 | 22664 | 2026-10-02 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 44737 | 44736 | 2399 | 2026-10-02 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 994 | 93 | 106/107 |
| http://95.3.69.222:8080 | TR | 1777 | 62 | 104/107 |
| http://213.111.146.36:18080 | NL | 520 | 36 | 39/44 |
| http://190.0.246.211:4040 | CO | 1029 | 27 | 94/107 |
| http://34.43.46.91:80 | US | 501 | 24 | 103/107 |
| http://190.0.246.210:4040 | CO | 825 | 23 | 95/106 |
| http://103.237.102.191:11111 | DE | 883 | 23 | 101/107 |
| http://18.157.123.132:3128 | DE | 530 | 22 | 54/68 |
| http://34.43.46.91:443 | US | 724 | 20 | 101/107 |
| http://149.130.173.58:9443 | CO | 441 | 18 | 18/18 |
| http://43.173.120.13:8899 | US | 677 | 18 | 18/18 |
| http://185.195.71.218:18080 | CH | 612 | 15 | 35/44 |
| http://107.150.41.226:18080 | US | 392 | 15 | 43/44 |
| http://197.224.185.3:3128 | MU | 1998 | 13 | 69/75 |
| http://45.186.6.104:3128 | EC | 613 | 12 | 80/85 |
| http://185.191.239.248:3128 | CH | 7071 | 11 | 77/106 |
| socks5://101.36.104.239:10808 | JP | 1878 | 11 | 90/107 |
| http://34.88.38.81:9443 | FI | 803 | 10 | 50/72 |
| http://35.228.49.168:9443 | FI | 601 | 10 | 31/44 |
| http://190.97.241.106:999 | VE | 2908 | 10 | 63/91 |
| http://222.128.172.158:8888 | CN | 1520 | 9 | 35/72 |
| http://5.129.254.5:8888 | RU | 970 | 8 | 53/62 |
| http://5.129.254.49:8888 | RU | 1023 | 8 | 54/62 |
| http://5.129.254.51:8888 | RU | 1061 | 8 | 54/62 |
| http://5.129.254.60:8888 | RU | 969 | 8 | 53/61 |
| http://5.129.254.70:8888 | RU | 1001 | 8 | 54/62 |
| http://5.129.254.129:8888 | RU | 995 | 8 | 59/68 |
| http://5.129.254.154:8888 | RU | 973 | 8 | 50/58 |
| http://104.248.151.93:9090 | SG | 1176 | 8 | 8/8 |
| http://154.59.56.78:999 | VE | 4547 | 8 | 43/63 |
| http://159.223.41.216:9090 | SG | 1147 | 7 | 46/67 |
| http://154.59.56.74:999 | VE | 6507 | 7 | 49/70 |
| socks5://212.77.75.25:1088 | IT | 985 | 7 | 7/7 |
| http://189.84.157.245:3126 | BR | 3531 | 6 | 6/6 |
| http://122.246.3.12:17981 | CN | 2194 | 6 | 48/101 |
| http://128.199.121.61:9090 | SG | 1209 | 6 | 22/27 |
| socks5://109.205.182.143:1088 | FR | 6568 | 6 | 20/22 |
| socks5://101.36.104.46:10808 | JP | 1957 | 6 | 94/107 |
| http://187.102.219.64:999 | AR | 1122 | 5 | 22/46 |
| http://120.232.115.170:17981 | CN | 2318 | 5 | 77/106 |
| http://103.162.54.18:8181 | ID | 3033 | 5 | 5/5 |
| http://202.59.75.5:8080 | PK | 3862 | 5 | 14/25 |
| http://128.199.254.13:9090 | SG | 1252 | 5 | 28/36 |
| http://129.226.89.151:80 | SG | 1146 | 5 | 36/54 |
| socks5://59.152.97.233:1080 | BD | 3273 | 5 | 62/105 |
| socks5://141.148.206.170:1088 | IN | 3445 | 5 | 18/27 |
| socks5://43.155.143.227:1080 | KR | 2675 | 5 | 13/16 |
| socks5://5.255.113.177:1080 | NL | 1623 | 5 | 5/5 |
| socks5://5.255.123.162:1080 | NL | 2633 | 5 | 29/90 |
| socks5://171.25.158.95:1080 | SE | 1768 | 5 | 17/22 |
| http://120.232.115.57:17981 | CN | 3023 | 4 | 25/32 |
| http://221.221.150.127:8888 | CN | 1185 | 4 | 22/53 |
| http://221.221.159.97:8888 | CN | 1872 | 4 | 28/60 |
| http://103.20.191.118:8080 | ID | 5181 | 4 | 20/72 |
| http://175.111.96.161:3128 | ID | 2913 | 4 | 4/4 |
| http://189.51.168.165:999 | MX | 637 | 4 | 18/19 |
| http://98.81.204.137:32859 | US | 964 | 4 | 7/21 |
| http://98.94.14.234:36508 | US | 2301 | 4 | 16/67 |
| http://178.128.146.125:10000 | US | 459 | 4 | 4/4 |
| socks4://185.112.83.80:1080 | FI | 873 | 4 | 11/12 |
| socks5://213.199.47.140:1080 | FR | 1644 | 4 | 59/73 |
| socks5://47.238.126.208:1080 | HK | 1347 | 4 | 11/12 |
| socks5://45.74.31.23:7494 | NL | 4366 | 4 | 5/23 |
| socks5://45.74.31.25:5542 | NL | 5642 | 4 | 4/4 |
| socks5://45.74.31.30:4873 | NL | 5836 | 4 | 6/32 |
| socks5://45.74.31.30:6455 | NL | 7854 | 4 | 4/4 |
| socks5://45.74.31.42:8998 | NL | 1946 | 4 | 4/4 |
| socks5://45.74.31.50:8701 | NL | 5057 | 4 | 4/4 |
| socks5://85.209.156.148:1080 | US | 2092 | 4 | 41/78 |
| http://18.230.23.72:25761 | BR | 3481 | 3 | 16/67 |
| http://16.18.22.211:36560 | CH | 4130 | 3 | 18/57 |
| http://101.206.186.99:8080 | CN | 5489 | 3 | 43/107 |
| http://101.251.204.174:8080 | CN | 1977 | 3 | 50/93 |
| http://111.196.31.158:8888 | CN | 1580 | 3 | 28/53 |
| http://113.45.195.147:3128 | CN | 1928 | 3 | 46/72 |
| http://114.246.207.184:8888 | CN | 2138 | 3 | 16/29 |
| http://114.249.225.156:8888 | CN | 2315 | 3 | 15/29 |
| http://123.119.176.120:8888 | CN | 1363 | 3 | 25/72 |
| http://123.121.113.161:8888 | CN | 1910 | 3 | 24/72 |
| http://221.221.157.102:8888 | CN | 7270 | 3 | 24/59 |
| http://222.128.173.38:8888 | CN | 2335 | 3 | 20/67 |
| http://190.7.214.134:8080 | CR | 3790 | 3 | 6/16 |
| http://103.119.19.218:3128 | CZ | 1891 | 3 | 18/20 |
| http://177.234.221.202:999 | EC | 5549 | 3 | 8/11 |
| http://177.234.221.204:999 | EC | 5503 | 3 | 7/10 |
| http://15.217.107.97:45779 | ES | 2309 | 3 | 7/17 |
| http://15.217.214.40:30561 | ES | 986 | 3 | 3/3 |
| http://185.73.39.118:9999 | GB | 452 | 3 | 3/3 |
| http://43.155.62.157:443 | HK | 1099 | 3 | 9/10 |
| http://103.144.54.73:8082 | ID | 1493 | 3 | 27/52 |
| http://103.156.14.54:8080 | ID | 1537 | 3 | 6/20 |
| http://103.167.170.70:1111 | ID | 4587 | 3 | 17/105 |
| http://103.188.168.207:8080 | ID | 2508 | 3 | 6/22 |
| http://103.195.65.138:8080 | ID | 1989 | 3 | 6/15 |
| http://110.76.144.119:8082 | ID | 5558 | 3 | 6/8 |
| http://146.196.40.155:3127 | ID | 1510 | 3 | 5/17 |
| http://160.22.206.154:8082 | ID | 1452 | 3 | 6/8 |
| http://165.101.43.43:8080 | ID | 4940 | 3 | 17/80 |
| http://202.51.121.59:8080 | ID | 6358 | 3 | 5/7 |
| http://202.58.77.131:7777 | ID | 6799 | 3 | 4/7 |
