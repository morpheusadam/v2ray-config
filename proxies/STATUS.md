# Proxy status

Generated 2026-08-25T13:54:47Z by `harvest.py`.

- **451** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1390** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13127** endpoints on record
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
| http | 1159 |
| socks5 | 216 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 371 |
| US | 63 |
| PH | 62 |
| CO | 60 |
| BD | 52 |
| RU | 49 |
| BR | 44 |
| MX | 39 |
| NL | 38 |
| CN | 36 |
| DE | 34 |
| IN | 32 |
| TR | 32 |
| VE | 31 |
| EC | 30 |
| VN | 29 |
| FR | 23 |
| SG | 20 |
| DO | 19 |
| AR | 16 |
| KH | 15 |
| PK | 15 |
| TH | 15 |
| HK | 14 |
| CL | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 1 | 2026-08-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 63 | 63 | 36 | 2026-08-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 95 | 95 | 52 | 2026-08-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 106 | 106 | 21 | 2026-08-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 112 | 112 | 14 | 2026-08-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 121 | 121 | 20 | 2026-08-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 129 | 129 | 38 | 2026-08-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 132 | 132 | 55 | 2026-08-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-08-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 345 | 345 | 126 | 2026-08-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-08-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-08-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1314 | 1310 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1422 | 1420 | 180 | 2026-08-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1150 | 2026-08-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1604 | 2026-08-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1855 | 1853 | 713 | 2026-08-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 1976 | 1974 | 1533 | 2026-08-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2072 | 2072 | 1704 | 2026-08-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 1141 | 27 | 29/30 |
| http://34.43.46.91:443 | US | 1439 | 22 | 27/30 |
| http://34.43.46.91:80 | US | 549 | 22 | 27/30 |
| http://181.78.74.252:999 | CO | 705 | 21 | 21/21 |
| http://181.78.74.253:999 | CO | 671 | 21 | 21/21 |
| http://190.97.236.128:999 | VE | 1686 | 20 | 20/20 |
| http://190.97.236.129:999 | VE | 1669 | 20 | 20/20 |
| http://103.237.102.191:11111 | DE | 644 | 16 | 29/30 |
| http://1.231.81.166:3128 | KR | 1712 | 16 | 29/30 |
| http://95.211.174.135:3128 | NL | 711 | 16 | 29/30 |
| http://204.76.203.9:3128 | NL | 644 | 16 | 29/30 |
| http://204.76.203.9:8080 | NL | 550 | 16 | 22/23 |
| http://185.200.188.234:10001 | RU | 1755 | 16 | 29/30 |
| http://130.110.103.245:3128 | SA | 3090 | 16 | 28/30 |
| http://95.3.69.222:8080 | TR | 1260 | 16 | 29/30 |
| http://199.7.149.90:3128 | US | 25 | 13 | 13/13 |
| socks5://103.75.118.84:1080 | JP | 3765 | 13 | 19/25 |
| http://199.7.149.96:3128 | US | 19 | 9 | 9/9 |
| http://45.186.6.104:3128 | EC | 654 | 8 | 8/8 |
| http://64.112.184.210:3128 | US | 408 | 8 | 29/30 |
| socks5://123.58.219.171:10808 | HK | 2131 | 8 | 24/30 |
| http://175.139.255.25:8181 | MY | 4200 | 7 | 23/30 |
| http://5.129.228.92:443 | NL | 793 | 7 | 13/15 |
| socks5://43.162.94.99:1080 | US | 931 | 7 | 23/30 |
| http://190.0.246.210:4040 | CO | 2177 | 6 | 26/29 |
| http://47.81.56.193:8888 | TH | 2216 | 6 | 14/30 |
| http://120.232.115.170:17981 | CN | 1958 | 5 | 16/29 |
| http://186.33.45.218:999 | EC | 7488 | 5 | 11/19 |
| http://103.130.61.61:8081 | ID | 1438 | 5 | 25/30 |
| http://103.157.200.126:3128 | PK | 3038 | 5 | 6/7 |
| http://44.193.20.213:8081 | US | 2073 | 5 | 5/5 |
| http://45.66.249.187:3128 | US | 3217 | 5 | 18/21 |
| http://115.231.181.40:8128 | CN | 5622 | 4 | 15/29 |
| http://159.69.45.217:1083 | DE | 3537 | 4 | 4/4 |
| http://175.136.239.173:8181 | MY | 4950 | 4 | 23/30 |
| http://175.136.239.174:8181 | MY | 4864 | 4 | 18/30 |
| http://45.66.249.187:8080 | US | 1583 | 4 | 18/25 |
| http://42.96.18.62:1311 | VN | 2565 | 4 | 19/29 |
| socks5://59.152.97.233:1080 | BD | 3527 | 4 | 19/28 |
| socks5://185.128.104.152:8443 | DE | 924 | 4 | 5/11 |
| socks5://144.91.121.61:1088 | FR | 2327 | 4 | 28/30 |
| socks5://101.36.104.239:10808 | JP | 2371 | 4 | 24/30 |
| socks5://67.207.92.87:1088 | US | 1472 | 4 | 15/29 |
| socks5://193.25.215.182:22222 | US | 1194 | 4 | 27/30 |
| http://181.78.208.227:999 | CO | 3289 | 3 | 5/17 |
| http://186.33.45.219:999 | EC | 7569 | 3 | 14/19 |
| http://190.12.150.244:999 | EC | 2823 | 3 | 19/26 |
| http://176.111.37.5:39811 | HK | 2723 | 3 | 25/30 |
| http://176.111.37.216:39811 | HK | 874 | 3 | 26/30 |
| http://157.66.3.20:1111 | ID | 7322 | 3 | 5/28 |
| http://64.176.171.202:2001 | IL | 7353 | 3 | 6/7 |
| http://117.236.124.166:3128 | IN | 1400 | 3 | 20/30 |
| http://212.154.169.90:3128 | KZ | 1081 | 3 | 7/9 |
| http://205.164.192.115:999 | MX | 4365 | 3 | 16/28 |
| http://64.76.73.131:999 | PE | 4909 | 3 | 3/3 |
| http://205.209.66.132:3128 | SY | 3125 | 3 | 9/28 |
| http://45.66.249.187:8181 | US | 6433 | 3 | 17/21 |
| socks5://103.210.161.8:1080 | CN | 3317 | 3 | 3/3 |
| socks5://45.144.54.40:1080 | DE | 5400 | 3 | 22/30 |
| socks5://152.89.104.11:1080 | DE | 6926 | 3 | 8/30 |
| socks5://45.192.9.27:1080 | ES | 892 | 3 | 8/28 |
| socks5://185.185.80.58:1088 | FR | 2997 | 3 | 19/29 |
| socks5://152.32.168.221:10808 | HK | 6287 | 3 | 13/19 |
| socks5://5.130.50.118:1080 | RU | 1229 | 3 | 3/3 |
| socks5://43.156.70.98:8080 | SG | 4968 | 3 | 6/7 |
| socks5://93.123.118.15:1080 | UA | 713 | 3 | 12/28 |
| socks5://173.224.219.31:1080 | US | 422 | 3 | 3/3 |
| socks5://173.224.219.64:1080 | US | 6063 | 3 | 3/3 |
| socks5://160.22.17.4:9988 | VN | 1707 | 3 | 9/26 |
| http://179.41.11.138:8080 | AR | 758 | 2 | 2/2 |
| http://181.114.230.37:8080 | AR | 4836 | 2 | 4/16 |
| http://16.51.148.102:8181 | AU | 3498 | 2 | 2/2 |
| http://103.150.49.90:8090 | BD | 2548 | 2 | 9/23 |
| http://151.237.84.9:8080 | BG | 5408 | 2 | 3/7 |
| http://191.160.36.7:8080 | BR | 1965 | 2 | 5/19 |
| http://201.65.173.178:8080 | BR | 1644 | 2 | 5/13 |
| http://185.191.239.248:3128 | CH | 1181 | 2 | 19/29 |
| http://38.7.195.49:999 | CL | 4017 | 2 | 3/4 |
| http://122.246.3.12:17981 | CN | 3586 | 2 | 13/24 |
| http://219.142.66.245:9090 | CN | 1664 | 2 | 4/5 |
| http://190.0.246.211:4040 | CO | 776 | 2 | 25/30 |
| http://159.69.45.217:1082 | DE | 2171 | 2 | 2/2 |
| http://217.160.249.182:8888 | DE | 2518 | 2 | 2/2 |
| http://38.75.82.213:999 | DO | 6164 | 2 | 7/24 |
| http://197.164.101.14:1976 | EG | 6143 | 2 | 2/2 |
| http://18.170.25.193:57422 | GB | 3991 | 2 | 9/26 |
| http://81.168.119.85:443 | GB | 2628 | 2 | 9/21 |
| http://85.117.56.82:8080 | GE | 2073 | 2 | 7/28 |
| http://47.57.69.227:3128 | HK | 2483 | 2 | 2/2 |
| http://103.211.103.170:3128 | HK | 487 | 2 | 2/2 |
| http://36.50.56.148:8080 | ID | 7877 | 2 | 2/2 |
| http://49.0.26.215:8087 | ID | 5112 | 2 | 2/2 |
| http://101.255.107.33:8080 | ID | 3519 | 2 | 5/20 |
| http://103.155.65.192:8181 | ID | 6294 | 2 | 2/2 |
| http://103.174.122.98:3128 | ID | 7306 | 2 | 2/2 |
| http://157.15.0.144:8112 | ID | 4104 | 2 | 7/28 |
| http://157.66.36.130:8080 | ID | 4476 | 2 | 7/25 |
| http://160.19.18.127:8181 | ID | 2560 | 2 | 2/2 |
| http://163.223.112.42:8080 | ID | 4738 | 2 | 4/27 |
| http://168.144.210.164:3128 | IN | 7624 | 2 | 2/2 |
