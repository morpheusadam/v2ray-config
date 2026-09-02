# Proxy status

Generated 2026-09-02T21:58:03Z by `harvest.py`.

- **1104** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **2200** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **16330** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 187/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1875 |
| socks5 | 309 |
| socks4 | 16 |

| country | entries |
|---|---|
| ID | 424 |
| US | 171 |
| CN | 93 |
| CO | 84 |
| MX | 84 |
| NL | 68 |
| BD | 66 |
| PH | 66 |
| RU | 62 |
| VE | 58 |
| FR | 55 |
| BR | 52 |
| DE | 52 |
| IN | 46 |
| TH | 46 |
| SG | 42 |
| AU | 37 |
| EC | 37 |
| CA | 36 |
| HK | 36 |
| JP | 33 |
| DO | 29 |
| VN | 29 |
| ZA | 27 |
| EG | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-09-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-09-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 102 | 102 | 37 | 2026-09-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 112 | 112 | 47 | 2026-09-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 124 | 124 | 26 | 2026-09-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 145 | 145 | 83 | 2026-09-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-09-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 188 | 188 | 51 | 2026-09-02 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 205 | 205 | 47 | 2026-09-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 307 | 307 | 108 | 2026-09-02 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-09-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-09-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 696 | 696 | 399 | 2026-09-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-09-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1597 | 2026-09-02 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2026 | 2022 | 629 | 2026-09-02 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2251 | 2251 | 1684 | 2026-09-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2303 | 2301 | 177 | 2026-09-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2813 | 2811 | 678 | 2026-09-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3255 | 3253 | 2382 | 2026-09-02 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://34.43.46.91:443 | US | 698 | 39 | 44/47 |
| http://34.43.46.91:80 | US | 2865 | 39 | 44/47 |
| http://95.211.174.135:3128 | NL | 906 | 33 | 46/47 |
| http://204.76.203.9:3128 | NL | 717 | 33 | 46/47 |
| http://204.76.203.9:8080 | NL | 497 | 33 | 39/40 |
| http://185.200.188.234:10001 | RU | 4573 | 33 | 46/47 |
| http://130.110.103.245:3128 | SA | 1183 | 33 | 45/47 |
| http://199.7.149.96:3128 | US | 27 | 26 | 26/26 |
| http://45.186.6.104:3128 | EC | 616 | 25 | 25/25 |
| http://64.112.184.210:3128 | US | 114 | 25 | 46/47 |
| http://103.211.103.170:3128 | HK | 485 | 19 | 19/19 |
| http://68.178.174.239:3128 | US | 1177 | 15 | 15/15 |
| http://68.178.174.239:8888 | US | 1173 | 15 | 15/15 |
| http://190.0.246.213:4040 | CO | 1467 | 12 | 12/12 |
| http://1.231.81.166:3128 | KR | 1654 | 12 | 44/47 |
| http://189.51.168.164:999 | MX | 365 | 12 | 12/12 |
| socks5://47.250.211.53:1080 | MY | 2144 | 12 | 28/47 |
| socks5://193.25.215.182:22222 | US | 1690 | 10 | 43/47 |
| http://3.211.120.181:443 | US | 84 | 9 | 9/9 |
| http://18.157.123.132:3128 | DE | 506 | 8 | 8/8 |
| http://116.202.172.187:11000 | DE | 2460 | 8 | 8/8 |
| http://91.134.141.4:3128 | FR | 486 | 8 | 8/8 |
| http://173.212.240.48:8888 | FR | 1383 | 8 | 8/8 |
| http://5.129.254.129:8888 | RU | 6207 | 8 | 8/8 |
| http://103.10.231.189:8080 | TH | 1675 | 8 | 21/32 |
| socks5://171.25.158.95:1080 | SE | 4859 | 8 | 24/46 |
| http://176.111.37.5:39811 | HK | 1053 | 7 | 41/47 |
| http://16.79.110.168:3128 | ID | 3326 | 7 | 7/7 |
| http://47.81.56.193:8888 | TH | 2593 | 7 | 29/47 |
| http://14.251.13.20:8080 | VN | 1471 | 7 | 18/19 |
| http://40.177.104.199:48086 | CA | 2852 | 6 | 9/14 |
| http://39.106.170.168:8080 | CN | 2045 | 6 | 17/45 |
| http://34.88.38.81:9443 | FI | 603 | 6 | 7/12 |
| http://16.174.6.134:3128 | CA | 2266 | 5 | 5/5 |
| http://37.59.125.131:8888 | FR | 1081 | 5 | 34/47 |
| http://168.144.84.188:3129 | IN | 1282 | 5 | 5/5 |
| http://3.92.47.79:10801 | US | 1985 | 5 | 6/7 |
| http://154.59.56.73:999 | VE | 2648 | 5 | 16/19 |
| http://190.97.241.106:999 | VE | 2229 | 5 | 9/31 |
| socks5://101.36.104.46:10808 | JP | 2400 | 5 | 43/47 |
| socks5://5.255.117.250:1080 | NL | 576 | 5 | 11/32 |
| http://40.177.104.199:22203 | CA | 1212 | 4 | 6/7 |
| http://120.232.115.170:17981 | CN | 1726 | 4 | 29/46 |
| http://181.78.23.187:999 | CO | 673 | 4 | 14/16 |
| http://181.78.74.252:999 | CO | 747 | 4 | 36/38 |
| http://181.78.74.253:999 | CO | 703 | 4 | 36/38 |
| http://177.234.217.235:999 | EC | 5574 | 4 | 10/16 |
| http://51.84.101.19:80 | IL | 2298 | 4 | 12/39 |
| http://175.143.76.177:8181 | MY | 3687 | 4 | 35/47 |
| http://111.119.162.248:10916 | PK | 2154 | 4 | 6/31 |
| http://154.59.56.76:999 | VE | 1716 | 4 | 5/7 |
| http://190.97.236.128:999 | VE | 590 | 4 | 35/37 |
| http://190.97.236.129:999 | VE | 589 | 4 | 35/37 |
| http://190.97.238.14:999 | VE | 3767 | 4 | 11/16 |
| http://200.59.191.27:999 | VE | 2254 | 4 | 25/42 |
| socks5://49.13.22.249:10801 | DE | 2228 | 4 | 9/16 |
| socks5://5.255.123.162:1080 | NL | 588 | 4 | 10/30 |
| socks5://93.87.38.20:1090 | RS | 889 | 4 | 4/4 |
| socks5://165.22.243.171:1080 | SG | 1477 | 4 | 4/4 |
| http://15.220.121.140:3128 | AR | 753 | 3 | 3/3 |
| http://3.26.152.74:50741 | AU | 3801 | 3 | 4/5 |
| http://13.239.253.213:3128 | AU | 3799 | 3 | 4/12 |
| http://16.26.154.68:53546 | AU | 3208 | 3 | 16/43 |
| http://52.62.103.7:22986 | AU | 3044 | 3 | 5/11 |
| http://52.62.103.7:4311 | AU | 2699 | 3 | 6/12 |
| http://103.141.174.54:11411 | BD | 6269 | 3 | 8/42 |
| http://103.177.118.145:8118 | BD | 1583 | 3 | 26/28 |
| http://16.174.124.173:3851 | CA | 2031 | 3 | 6/11 |
| http://40.176.90.140:11111 | CA | 1533 | 3 | 3/3 |
| http://40.177.99.164:8000 | CA | 2169 | 3 | 5/7 |
| http://185.191.239.248:3128 | CH | 3583 | 3 | 34/46 |
| http://123.121.122.126:8888 | CN | 2109 | 3 | 10/15 |
| http://221.221.166.95:8888 | CN | 1504 | 3 | 8/12 |
| http://45.172.223.194:999 | CO | 4287 | 3 | 6/8 |
| http://18.185.116.137:6060 | DE | 1450 | 3 | 4/7 |
| http://38.50.165.122:999 | DO | 5529 | 3 | 10/35 |
| http://45.176.99.58:999 | DO | 5747 | 3 | 21/42 |
| http://217.76.245.80:999 | DO | 879 | 3 | 3/3 |
| http://186.5.94.206:999 | EC | 795 | 3 | 8/9 |
| http://190.12.150.244:999 | EC | 3997 | 3 | 28/43 |
| http://197.164.101.13:1981 | EG | 3176 | 3 | 8/36 |
| http://160.22.35.242:8080 | ID | 7800 | 3 | 4/18 |
| http://175.136.239.173:8181 | MY | 4425 | 3 | 36/47 |
| http://58.69.182.53:8085 | PH | 1568 | 3 | 6/10 |
| http://85.198.100.232:13100 | RU | 752 | 3 | 3/3 |
| http://16.192.185.227:46981 | SE | 4380 | 3 | 4/7 |
| http://47.129.130.0:5063 | SG | 3117 | 3 | 3/3 |
| http://34.224.98.75:7741 | US | 1715 | 3 | 5/11 |
| http://34.234.90.157:21349 | US | 3123 | 3 | 4/7 |
| http://54.196.39.29:4444 | US | 1838 | 3 | 5/6 |
| http://204.186.254.106:8080 | US | 2497 | 3 | 6/12 |
| http://154.59.56.72:999 | VE | 7188 | 3 | 4/6 |
| http://154.59.56.74:999 | VE | 2288 | 3 | 5/10 |
| http://190.97.229.118:999 | VE | 877 | 3 | 16/37 |
| http://210.211.113.34:80 | VN | 4174 | 3 | 16/19 |
| http://217.29.209.22:8865 | ZA | 7707 | 3 | 3/3 |
| socks5://5.75.133.113:10801 | DE | 1511 | 3 | 8/13 |
| socks5://5.75.133.113:10811 | DE | 1838 | 3 | 11/18 |
| socks5://45.144.54.40:1080 | DE | 2948 | 3 | 36/47 |
| socks5://77.239.106.24:1080 | DE | 2393 | 3 | 21/32 |
