# Proxy status

Generated 2026-08-23T13:35:55Z by `harvest.py`.

- **435** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1153** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13721** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 137/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 887 |
| socks5 | 244 |
| socks4 | 22 |

| country | entries |
|---|---|
| ID | 257 |
| US | 71 |
| RU | 60 |
| CO | 59 |
| BD | 45 |
| PH | 44 |
| NL | 40 |
| CN | 35 |
| TR | 32 |
| MX | 29 |
| FR | 27 |
| EC | 25 |
| BR | 23 |
| DE | 23 |
| EG | 23 |
| IN | 23 |
| SG | 22 |
| VE | 22 |
| VN | 21 |
| KH | 18 |
| IR | 17 |
| FI | 16 |
| HK | 16 |
| DO | 14 |
| AR | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-08-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 51 | 51 | 13 | 2026-08-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 59 | 59 | 31 | 2026-08-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 93 | 93 | 12 | 2026-08-23 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 103 | 103 | 48 | 2026-08-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 113 | 113 | 29 | 2026-08-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 115 | 115 | 17 | 2026-08-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-08-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 184 | 184 | 48 | 2026-08-23 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 186 | 186 | 35 | 2026-08-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-23 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-08-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 456 | 2026-08-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1141 | 2026-08-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1604 | 2026-08-23 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1855 | 1851 | 147 | 2026-08-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1957 | 1955 | 210 | 2026-08-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2392 | 2390 | 658 | 2026-08-23 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2460 | 2460 | 1958 | 2026-08-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2641 | 2639 | 2051 | 2026-08-23 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1220 | 23 | 25/26 |
| http://34.43.46.91:443 | US | 749 | 18 | 23/26 |
| http://34.43.46.91:80 | US | 495 | 18 | 23/26 |
| http://181.78.74.252:999 | CO | 711 | 17 | 17/17 |
| http://181.78.74.253:999 | CO | 683 | 17 | 17/17 |
| http://190.97.236.128:999 | VE | 1601 | 16 | 16/16 |
| http://190.97.236.129:999 | VE | 593 | 16 | 16/16 |
| http://103.237.102.191:11111 | DE | 649 | 12 | 25/26 |
| http://212.58.132.5:8888 | GB | 1239 | 12 | 21/25 |
| http://1.231.81.166:3128 | KR | 1904 | 12 | 25/26 |
| http://95.211.174.135:3128 | NL | 1014 | 12 | 25/26 |
| http://204.76.203.9:3128 | NL | 919 | 12 | 25/26 |
| http://204.76.203.9:8080 | NL | 512 | 12 | 18/19 |
| http://185.200.188.234:10001 | RU | 1522 | 12 | 25/26 |
| http://130.110.103.245:3128 | SA | 1617 | 12 | 24/26 |
| http://202.28.194.139:31280 | TH | 2866 | 12 | 25/26 |
| http://95.3.69.222:8080 | TR | 1757 | 12 | 25/26 |
| http://87.251.77.29:3128 | DE | 724 | 11 | 24/26 |
| http://13.221.202.200:3128 | US | 60 | 9 | 9/9 |
| http://199.7.149.90:3128 | US | 23 | 9 | 9/9 |
| socks5://101.36.104.46:10808 | JP | 2551 | 9 | 24/26 |
| socks5://103.75.118.84:1080 | JP | 3056 | 9 | 15/21 |
| socks5://45.43.63.37:10808 | SG | 3224 | 9 | 23/26 |
| http://103.177.118.145:8118 | BD | 3055 | 7 | 7/7 |
| http://41.128.90.50:1976 | EG | 969 | 6 | 10/11 |
| socks5://193.222.99.32:1080 | DE | 2463 | 6 | 9/11 |
| http://8.138.217.152:21001 | CN | 2754 | 5 | 17/26 |
| http://223.85.21.195:8080 | CN | 2162 | 5 | 15/24 |
| http://94.131.92.155:3128 | KZ | 3429 | 5 | 16/24 |
| http://152.42.167.241:3128 | SG | 2574 | 5 | 23/26 |
| http://34.238.165.158:3128 | US | 62 | 5 | 5/5 |
| http://165.154.162.73:8888 | US | 3036 | 5 | 17/26 |
| http://199.7.149.96:3128 | US | 19 | 5 | 5/5 |
| socks5://77.239.106.24:1080 | DE | 5107 | 5 | 10/11 |
| socks5://161.35.90.93:1082 | NL | 6244 | 5 | 13/26 |
| socks5://85.198.82.207:1080 | RU | 2650 | 5 | 10/15 |
| socks5://34.229.113.62:1080 | US | 2686 | 5 | 15/19 |
| http://45.186.6.104:3128 | EC | 594 | 4 | 4/4 |
| http://45.239.48.102:999 | EC | 4180 | 4 | 9/20 |
| http://101.47.75.240:5000 | HK | 1164 | 4 | 4/4 |
| http://176.111.37.216:39811 | HK | 878 | 4 | 23/26 |
| http://117.236.124.166:3128 | IN | 2303 | 4 | 17/26 |
| http://72.56.109.88:3128 | NL | 538 | 4 | 7/24 |
| http://153.80.240.37:8080 | NL | 1002 | 4 | 18/26 |
| http://70.34.249.28:2001 | PL | 2544 | 4 | 4/4 |
| http://47.252.52.58:8081 | US | 62 | 4 | 4/4 |
| http://64.112.184.210:3128 | US | 172 | 4 | 25/26 |
| socks5://213.136.92.91:1080 | FR | 2538 | 4 | 16/26 |
| socks5://123.58.219.171:10808 | HK | 2087 | 4 | 20/26 |
| socks5://45.95.202.92:10808 | RU | 1076 | 4 | 4/4 |
| http://38.50.165.123:999 | DO | 6306 | 3 | 7/11 |
| http://45.71.0.1:999 | EC | 2729 | 3 | 4/9 |
| http://45.239.48.100:999 | EC | 4274 | 3 | 3/3 |
| http://41.65.236.37:8080 | EG | 5022 | 3 | 7/8 |
| http://176.111.37.5:39811 | HK | 794 | 3 | 22/26 |
| http://49.0.2.54:8080 | ID | 5172 | 3 | 5/9 |
| http://64.176.171.202:2001 | IL | 6619 | 3 | 3/3 |
| http://91.228.133.191:9999 | IR | 1989 | 3 | 6/12 |
| http://175.139.255.25:8181 | MY | 4397 | 3 | 19/26 |
| http://5.129.228.92:443 | NL | 4478 | 3 | 9/11 |
| http://93.93.207.219:8088 | RU | 7557 | 3 | 3/3 |
| http://150.136.239.172:3128 | US | 5273 | 3 | 3/3 |
| socks4://115.136.121.54:9050 | KR | 2450 | 3 | 6/23 |
| socks5://186.26.95.249:61445 | BR | 4097 | 3 | 5/10 |
| socks5://110.235.252.74:1080 | KH | 1914 | 3 | 10/25 |
| socks5://161.35.90.93:1081 | NL | 6101 | 3 | 12/26 |
| socks5://31.220.163.133:1080 | RU | 2029 | 3 | 5/25 |
| socks5://43.156.70.98:8080 | SG | 2622 | 3 | 3/3 |
| socks5://43.162.94.99:1080 | US | 2207 | 3 | 19/26 |
| socks5://14.225.204.32:10800 | VN | 3253 | 3 | 3/3 |
| http://170.168.102.55:3128 | AM | 4318 | 2 | 8/17 |
| http://181.14.210.237:8080 | AR | 7051 | 2 | 5/24 |
| http://179.61.98.3:999 | CL | 7356 | 2 | 3/19 |
| http://27.185.218.213:17981 | CN | 2426 | 2 | 13/26 |
| http://47.107.82.96:30051 | CN | 3457 | 2 | 16/19 |
| http://181.78.17.131:999 | CO | 6685 | 2 | 6/23 |
| http://190.0.246.210:4040 | CO | 1695 | 2 | 22/25 |
| http://201.234.186.225:999 | CO | 4741 | 2 | 7/21 |
| http://85.234.100.149:8080 | DE | 2489 | 2 | 11/22 |
| http://45.70.236.194:999 | EC | 4059 | 2 | 7/22 |
| http://45.239.48.101:999 | EC | 6735 | 2 | 2/2 |
| http://41.128.90.50:1981 | EG | 1941 | 2 | 6/9 |
| http://45.245.208.180:8080 | EG | 4359 | 2 | 2/2 |
| http://81.168.119.85:443 | GB | 1601 | 2 | 7/17 |
| http://43.99.100.108:3128 | HK | 1402 | 2 | 20/26 |
| http://36.92.199.158:8080 | ID | 7597 | 2 | 5/20 |
| http://103.126.87.182:8080 | ID | 2802 | 2 | 6/20 |
| http://103.139.99.173:8080 | ID | 6403 | 2 | 6/20 |
| http://103.166.1.125:1111 | ID | 7010 | 2 | 3/16 |
| http://103.181.255.105:8080 | ID | 5343 | 2 | 7/14 |
| http://103.250.128.18:8082 | ID | 7445 | 2 | 8/22 |
| http://150.107.104.22:80 | ID | 6677 | 2 | 4/5 |
| http://161.248.226.7:80 | ID | 4598 | 2 | 9/25 |
| http://182.253.109.133:1256 | ID | 5967 | 2 | 7/17 |
| http://112.216.54.226:12121 | KR | 2217 | 2 | 8/20 |
| http://189.203.181.34:8080 | MX | 6924 | 2 | 2/2 |
| http://139.135.77.166:8085 | PH | 3567 | 2 | 4/21 |
| http://185.238.238.29:58080 | PL | 868 | 2 | 9/18 |
| http://89.43.132.239:8080 | SY | 5240 | 2 | 6/18 |
| http://47.81.56.193:8888 | TH | 2372 | 2 | 10/26 |
