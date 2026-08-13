# Proxy status

Generated 2026-08-13T14:24:36Z by `harvest.py`.

- **525** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **781** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **11588** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 223/600 (37%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 574 |
| socks5 | 194 |
| socks4 | 13 |

| country | entries |
|---|---|
| ID | 158 |
| US | 73 |
| CN | 41 |
| RU | 38 |
| VN | 35 |
| PH | 27 |
| FR | 26 |
| NL | 25 |
| CO | 22 |
| SG | 22 |
| BD | 21 |
| DE | 20 |
| VE | 20 |
| IN | 18 |
| BR | 17 |
| JP | 15 |
| MX | 15 |
| TR | 14 |
| FI | 11 |
| HK | 10 |
| EC | 9 |
| KR | 8 |
| TH | 8 |
| CL | 7 |
| PE | 7 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 4 | 2026-08-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 79 | 79 | 51 | 2026-08-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 95 | 95 | 57 | 2026-08-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 96 | 96 | 30 | 2026-08-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 149 | 149 | 30 | 2026-08-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 80 | 2026-08-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 171 | 171 | 38 | 2026-08-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 183 | 183 | 74 | 2026-08-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 190 | 190 | 127 | 2026-08-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 353 | 353 | 187 | 2026-08-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 534 | 2026-08-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-08-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1137 | 2026-08-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1634 | 2026-08-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1942 | 1942 | 0 | 2026-08-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2162 | 2162 | 184 | 2026-08-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2517 | 2517 | 2034 | 2026-08-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2619 | 2619 | 687 | 2026-08-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2787 | 2785 | 2466 | 2026-08-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2434 | 6 | 6/6 |
| http://87.251.77.29:3128 | DE | 884 | 6 | 6/6 |
| http://103.237.102.191:11111 | DE | 779 | 6 | 6/6 |
| http://43.99.100.108:3128 | HK | 1572 | 6 | 6/6 |
| http://176.111.37.5:39811 | HK | 835 | 6 | 6/6 |
| http://176.111.37.216:39811 | HK | 1079 | 6 | 6/6 |
| http://103.130.61.61:8081 | ID | 1803 | 6 | 6/6 |
| http://1.231.81.166:3128 | KR | 1584 | 6 | 6/6 |
| http://88.210.11.216:8989 | NL | 2552 | 6 | 6/6 |
| http://95.211.64.139:8888 | NL | 655 | 6 | 6/6 |
| http://95.211.64.139:8889 | NL | 927 | 6 | 6/6 |
| http://95.211.174.135:3128 | NL | 1466 | 6 | 6/6 |
| http://147.45.166.120:3333 | NL | 716 | 6 | 6/6 |
| http://204.76.203.9:3128 | NL | 855 | 6 | 6/6 |
| http://185.200.188.234:10001 | RU | 1137 | 6 | 6/6 |
| http://143.198.87.117:8888 | SG | 1280 | 6 | 6/6 |
| http://152.42.167.241:3128 | SG | 1611 | 6 | 6/6 |
| http://202.28.194.139:31280 | TH | 2003 | 6 | 6/6 |
| http://95.3.69.222:8080 | TR | 1373 | 6 | 6/6 |
| http://43.153.82.179:8888 | US | 797 | 6 | 6/6 |
| http://64.112.184.210:3128 | US | 182 | 6 | 6/6 |
| socks5://66.163.118.99:10006 | ES | 7814 | 6 | 6/6 |
| socks5://144.91.121.61:1088 | FR | 1639 | 6 | 6/6 |
| socks5://212.58.132.5:1080 | GB | 1690 | 6 | 6/6 |
| socks5://123.58.219.171:10808 | HK | 2037 | 6 | 6/6 |
| socks5://66.163.119.55:10006 | IT | 1788 | 6 | 6/6 |
| socks5://149.62.186.244:1080 | IT | 6240 | 6 | 6/6 |
| socks5://101.36.104.46:10808 | JP | 1929 | 6 | 6/6 |
| socks5://101.36.104.239:10808 | JP | 1900 | 6 | 6/6 |
| socks5://193.233.218.213:1080 | RU | 3406 | 6 | 6/6 |
| socks5://43.134.58.45:1080 | SG | 1651 | 6 | 6/6 |
| socks5://43.156.84.41:10808 | SG | 5757 | 6 | 6/6 |
| socks5://69.55.49.177:38182 | US | 1019 | 6 | 6/6 |
| socks5://129.151.9.55:10808 | US | 786 | 6 | 6/6 |
| socks5://193.25.215.182:22222 | US | 2425 | 6 | 6/6 |
| http://185.191.239.248:3128 | CH | 857 | 5 | 5/5 |
| http://38.7.195.53:999 | CL | 4686 | 5 | 5/5 |
| http://95.211.64.139:8887 | NL | 784 | 5 | 5/5 |
| http://178.18.207.85:8888 | TR | 970 | 5 | 5/5 |
| http://157.230.178.216:40000 | US | 5134 | 5 | 5/5 |
| http://162.214.74.29:3128 | US | 4763 | 5 | 5/5 |
| http://162.214.159.94:3128 | US | 5167 | 5 | 5/5 |
| http://174.137.134.182:2999 | US | 910 | 5 | 5/5 |
| socks5://171.25.158.95:1080 | SE | 7751 | 5 | 5/5 |
| http://152.53.20.190:20000 | DE | 829 | 4 | 5/6 |
| http://210.131.214.36:80 | JP | 1473 | 4 | 5/6 |
| http://153.80.240.37:8080 | NL | 6685 | 4 | 5/6 |
| http://34.94.46.8:80 | US | 377 | 4 | 4/4 |
| http://195.158.8.123:3128 | UZ | 2507 | 4 | 4/4 |
| http://38.51.207.116:999 | VE | 7865 | 4 | 4/4 |
| socks5://161.35.90.93:1081 | NL | 1223 | 4 | 5/6 |
| socks5://161.35.90.93:1082 | NL | 2133 | 4 | 5/6 |
| socks5://185.209.29.226:1080 | RU | 1228 | 4 | 5/6 |
| socks5://45.43.63.37:10808 | SG | 4613 | 4 | 5/6 |
| http://59.36.210.211:13552 | CN | 2915 | 3 | 3/3 |
| http://181.39.25.196:8118 | EC | 1055 | 3 | 5/6 |
| http://103.179.183.153:8080 | ID | 5546 | 3 | 3/3 |
| http://223.25.110.77:8090 | ID | 2545 | 3 | 4/5 |
| http://116.90.224.50:8080 | NP | 3190 | 3 | 3/3 |
| http://103.162.136.23:8080 | PK | 3611 | 3 | 3/3 |
| http://130.110.103.245:3128 | SA | 1670 | 3 | 5/6 |
| http://43.160.242.118:3128 | SG | 3222 | 3 | 3/3 |
| http://104.154.186.48:80 | US | 285 | 3 | 4/5 |
| socks5://191.44.118.236:1080 | DE | 584 | 3 | 3/3 |
| socks5://45.95.233.88:1082 | FR | 1639 | 3 | 3/3 |
| socks5://51.159.97.242:10006 | FR | 898 | 3 | 5/6 |
| socks5://109.199.105.194:1080 | FR | 2658 | 3 | 3/3 |
| socks5://152.228.134.176:48080 | FR | 1500 | 3 | 4/5 |
| socks5://43.164.136.189:1080 | KR | 1469 | 3 | 4/6 |
| socks5://121.169.46.116:1090 | KR | 1490 | 3 | 5/6 |
| socks5://45.10.42.68:1080 | NL | 1029 | 3 | 3/3 |
| socks5://5.249.165.195:20000 | US | 1284 | 3 | 3/3 |
| socks5://47.85.195.135:1080 | US | 4172 | 3 | 5/6 |
| socks5://107.191.44.214:1081 | US | 2941 | 3 | 5/6 |
| socks5://147.45.60.136:1082 | US | 5282 | 3 | 3/3 |
| socks5://204.152.192.13:1080 | US | 1745 | 3 | 3/3 |
| http://181.13.221.155:999 | AR | 3513 | 2 | 2/2 |
| http://103.136.107.60:100 | BD | 1823 | 2 | 2/2 |
| http://203.76.220.126:16464 | BD | 6946 | 2 | 2/2 |
| http://201.186.41.170:999 | CL | 4436 | 2 | 2/2 |
| http://8.130.52.254:21056 | CN | 7461 | 2 | 2/2 |
| http://61.155.3.26:3128 | CN | 3345 | 2 | 2/2 |
| http://114.94.148.37:18080 | CN | 3214 | 2 | 4/5 |
| http://116.62.202.70:17900 | CN | 3138 | 2 | 2/2 |
| http://123.60.155.1:3128 | CN | 3059 | 2 | 3/4 |
| http://45.65.138.48:999 | CO | 3560 | 2 | 4/6 |
| http://186.180.19.122:8080 | CO | 4661 | 2 | 3/4 |
| http://190.0.246.210:4040 | CO | 1861 | 2 | 4/5 |
| http://85.234.100.149:8080 | DE | 3598 | 2 | 2/2 |
| http://200.107.206.10:999 | DO | 4523 | 2 | 3/4 |
| http://190.12.150.244:999 | EC | 3498 | 2 | 2/2 |
| http://45.144.53.63:6019 | FI | 6049 | 2 | 2/2 |
| http://45.144.53.63:6020 | FI | 6614 | 2 | 2/2 |
| http://37.59.125.131:8888 | FR | 703 | 2 | 5/6 |
| http://18.170.25.193:57422 | GB | 571 | 2 | 2/2 |
| http://82.102.11.164:3460 | GB | 1015 | 2 | 5/6 |
| http://212.58.132.5:8888 | GB | 1390 | 2 | 3/5 |
| http://181.189.27.163:999 | GT | 1762 | 2 | 2/2 |
| http://27.112.66.122:8181 | ID | 5070 | 2 | 2/2 |
| http://36.50.56.105:8818 | ID | 2680 | 2 | 2/2 |
