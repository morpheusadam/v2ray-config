# Proxy status

Generated 2026-08-23T19:53:33Z by `harvest.py`.

- **330** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **989** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13601** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 115/600 (19%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 747 |
| socks5 | 222 |
| socks4 | 20 |

| country | entries |
|---|---|
| ID | 206 |
| US | 61 |
| RU | 54 |
| CO | 46 |
| CN | 36 |
| PH | 35 |
| NL | 34 |
| BD | 31 |
| TR | 30 |
| EC | 27 |
| BR | 23 |
| MX | 23 |
| SG | 23 |
| FR | 22 |
| DE | 21 |
| IN | 21 |
| VE | 21 |
| VN | 20 |
| EG | 17 |
| HK | 15 |
| KH | 14 |
| AR | 13 |
| DO | 13 |
| FI | 13 |
| IR | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 1 | 2026-08-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 60 | 60 | 26 | 2026-08-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 76 | 76 | 19 | 2026-08-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 78 | 78 | 7 | 2026-08-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 78 | 78 | 15 | 2026-08-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 79 | 79 | 37 | 2026-08-23 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 80 | 80 | 16 | 2026-08-23 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-08-23 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 123 | 123 | 34 | 2026-08-23 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-08-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 174 | 174 | 56 | 2026-08-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-23 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-23 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-08-23 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-08-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-08-23 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1598 | 2026-08-23 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1844 | 1840 | 154 | 2026-08-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2015 | 2013 | 229 | 2026-08-23 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2302 | 2302 | 1900 | 2026-08-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2444 | 2442 | 662 | 2026-08-23 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2590 | 2588 | 1975 | 2026-08-23 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 970 | 24 | 26/27 |
| http://34.43.46.91:443 | US | 564 | 19 | 24/27 |
| http://34.43.46.91:80 | US | 673 | 19 | 24/27 |
| http://181.78.74.252:999 | CO | 739 | 18 | 18/18 |
| http://181.78.74.253:999 | CO | 766 | 18 | 18/18 |
| http://190.97.236.128:999 | VE | 1722 | 17 | 17/17 |
| http://190.97.236.129:999 | VE | 1716 | 17 | 17/17 |
| http://103.237.102.191:11111 | DE | 760 | 13 | 26/27 |
| http://1.231.81.166:3128 | KR | 1051 | 13 | 26/27 |
| http://95.211.174.135:3128 | NL | 914 | 13 | 26/27 |
| http://204.76.203.9:3128 | NL | 931 | 13 | 26/27 |
| http://204.76.203.9:8080 | NL | 658 | 13 | 19/20 |
| http://185.200.188.234:10001 | RU | 1789 | 13 | 26/27 |
| http://130.110.103.245:3128 | SA | 1259 | 13 | 25/27 |
| http://202.28.194.139:31280 | TH | 2164 | 13 | 26/27 |
| http://95.3.69.222:8080 | TR | 1331 | 13 | 26/27 |
| http://87.251.77.29:3128 | DE | 1067 | 12 | 25/27 |
| http://13.221.202.200:3128 | US | 202 | 10 | 10/10 |
| http://199.7.149.90:3128 | US | 212 | 10 | 10/10 |
| socks5://101.36.104.46:10808 | JP | 4057 | 10 | 25/27 |
| socks5://103.75.118.84:1080 | JP | 7414 | 10 | 16/22 |
| socks5://45.43.63.37:10808 | SG | 3523 | 10 | 24/27 |
| http://103.177.118.145:8118 | BD | 1534 | 8 | 8/8 |
| http://41.128.90.50:1976 | EG | 913 | 7 | 11/12 |
| http://152.42.167.241:3128 | SG | 2251 | 6 | 24/27 |
| http://34.238.165.158:3128 | US | 190 | 6 | 6/6 |
| http://165.154.162.73:8888 | US | 1094 | 6 | 18/27 |
| http://199.7.149.96:3128 | US | 184 | 6 | 6/6 |
| socks5://77.239.106.24:1080 | DE | 2711 | 6 | 11/12 |
| socks5://85.198.82.207:1080 | RU | 2533 | 6 | 11/16 |
| socks5://34.229.113.62:1080 | US | 833 | 6 | 16/20 |
| http://45.186.6.104:3128 | EC | 926 | 5 | 5/5 |
| http://101.47.75.240:5000 | HK | 1021 | 5 | 5/5 |
| http://72.56.109.88:3128 | NL | 1576 | 5 | 8/25 |
| http://70.34.249.28:2001 | PL | 867 | 5 | 5/5 |
| http://47.252.52.58:8081 | US | 1209 | 5 | 5/5 |
| http://64.112.184.210:3128 | US | 430 | 5 | 26/27 |
| socks5://213.136.92.91:1080 | FR | 3373 | 5 | 17/27 |
| socks5://123.58.219.171:10808 | HK | 3220 | 5 | 21/27 |
| http://175.139.255.25:8181 | MY | 5177 | 4 | 20/27 |
| http://5.129.228.92:443 | NL | 787 | 4 | 10/12 |
| http://93.93.207.219:8088 | RU | 2222 | 4 | 4/4 |
| http://150.136.239.172:3128 | US | 217 | 4 | 4/4 |
| socks5://186.26.95.249:61445 | BR | 3529 | 4 | 6/11 |
| socks5://43.162.94.99:1080 | US | 4419 | 4 | 20/27 |
| http://190.0.246.210:4040 | CO | 2229 | 3 | 23/26 |
| http://45.239.48.101:999 | EC | 3761 | 3 | 3/3 |
| http://41.128.90.50:1981 | EG | 3153 | 3 | 7/10 |
| http://43.99.100.108:3128 | HK | 1290 | 3 | 21/27 |
| http://47.81.56.193:8888 | TH | 2327 | 3 | 11/27 |
| http://103.10.231.189:8080 | TH | 1380 | 3 | 9/12 |
| http://98.83.197.228:3128 | US | 583 | 3 | 9/10 |
| http://195.158.8.123:3128 | UZ | 5034 | 3 | 19/25 |
| socks5://45.194.33.12:30001 | HK | 2445 | 3 | 17/23 |
| socks5://77.110.103.146:1080 | NL | 796 | 3 | 11/20 |
| socks5://43.164.3.124:1080 | TH | 5212 | 3 | 17/26 |
| socks5://100.28.216.204:5555 | US | 236 | 3 | 3/3 |
| http://103.72.198.132:55 | BD | 3633 | 2 | 6/26 |
| http://185.191.239.248:3128 | CH | 1034 | 2 | 17/26 |
| http://38.7.195.51:999 | CL | 7559 | 2 | 5/18 |
| http://114.94.148.37:18080 | CN | 1155 | 2 | 16/26 |
| http://120.26.171.55:25125 | CN | 1756 | 2 | 7/25 |
| http://120.232.115.170:17981 | CN | 1291 | 2 | 13/26 |
| http://219.142.66.245:9090 | CN | 1725 | 2 | 2/2 |
| http://190.60.34.250:999 | CO | 4485 | 2 | 3/4 |
| http://190.131.254.134:8154 | CO | 6802 | 2 | 6/22 |
| http://181.78.195.137:999 | EC | 4526 | 2 | 8/27 |
| http://186.33.45.218:999 | EC | 3540 | 2 | 8/16 |
| http://200.24.159.146:999 | EC | 3969 | 2 | 2/2 |
| http://37.59.125.131:8888 | FR | 1394 | 2 | 21/27 |
| http://80.241.214.192:3128 | FR | 2544 | 2 | 10/11 |
| http://103.61.234.186:8180 | ID | 4540 | 2 | 13/24 |
| http://103.66.62.177:8080 | ID | 7154 | 2 | 2/2 |
| http://103.130.61.61:8081 | ID | 4153 | 2 | 22/27 |
| http://103.135.226.66:8080 | ID | 4508 | 2 | 5/15 |
| http://103.158.162.226:8080 | ID | 6518 | 2 | 8/25 |
| http://180.148.25.78:8080 | ID | 7871 | 2 | 4/9 |
| http://14.139.235.82:3128 | IN | 1832 | 2 | 19/27 |
| http://38.43.88.102:999 | MX | 7818 | 2 | 2/2 |
| http://154.27.196.2:999 | MX | 4109 | 2 | 5/10 |
| http://49.147.127.126:8082 | PH | 4362 | 2 | 2/2 |
| http://103.157.200.126:3128 | PK | 1471 | 2 | 3/4 |
| http://170.245.132.81:999 | PY | 2997 | 2 | 7/20 |
| http://5.161.50.82:8118 | US | 1860 | 2 | 9/26 |
| http://44.193.20.213:8081 | US | 1613 | 2 | 2/2 |
| http://45.66.249.187:3128 | US | 2957 | 2 | 15/18 |
| http://49.51.253.118:8888 | US | 411 | 2 | 10/14 |
| socks5://163.47.37.190:1080 | BD | 1886 | 2 | 7/19 |
| socks5://123.112.120.208:1080 | CN | 4293 | 2 | 2/2 |
| socks5://45.95.233.128:1082 | FR | 3889 | 2 | 9/26 |
| socks5://109.123.251.109:1080 | FR | 1243 | 2 | 10/27 |
| socks5://212.58.132.5:1080 | GB | 2012 | 2 | 25/27 |
| socks5://103.236.190.197:1080 | ID | 3629 | 2 | 7/25 |
| socks5://202.43.165.140:10802 | ID | 6659 | 2 | 8/27 |
| socks5://149.62.186.244:1080 | IT | 3990 | 2 | 22/27 |
| socks5://37.18.73.60:5566 | RU | 5681 | 2 | 15/27 |
| socks5://88.201.248.85:1080 | RU | 923 | 2 | 7/26 |
| socks5://185.170.10.176:1080 | RU | 6888 | 2 | 3/4 |
| socks5://45.76.164.255:1085 | US | 223 | 2 | 14/23 |
| socks5://147.45.60.136:1082 | US | 2275 | 2 | 12/24 |
