# Proxy status

Generated 2026-08-26T13:57:48Z by `harvest.py`.

- **892** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1455** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13567** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 107/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1207 |
| socks5 | 231 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 343 |
| PH | 75 |
| US | 65 |
| CO | 63 |
| BD | 55 |
| RU | 50 |
| IN | 46 |
| MX | 44 |
| NL | 42 |
| BR | 39 |
| DE | 37 |
| CN | 36 |
| VE | 35 |
| VN | 33 |
| EC | 32 |
| FR | 32 |
| TR | 30 |
| SG | 26 |
| AR | 19 |
| EG | 19 |
| JP | 19 |
| CL | 18 |
| DO | 17 |
| TH | 17 |
| KE | 16 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-08-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 60 | 60 | 36 | 2026-08-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 76 | 76 | 44 | 2026-08-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 98 | 98 | 14 | 2026-08-26 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-08-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 132 | 132 | 15 | 2026-08-26 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 95 | 2026-08-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 151 | 151 | 65 | 2026-08-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 173 | 173 | 29 | 2026-08-26 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 240 | 240 | 97 | 2026-08-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-26 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 399 | 399 | 139 | 2026-08-26 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-26 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-08-26 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 458 | 2026-08-26 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1606 | 1602 | 0 | 2026-08-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-08-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1782 | 1780 | 228 | 2026-08-26 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1607 | 2026-08-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2017 | 2015 | 712 | 2026-08-26 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2214 | 2214 | 1691 | 2026-08-26 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2316 | 2314 | 1748 | 2026-08-26 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 946 | 29 | 31/32 |
| http://34.43.46.91:443 | US | 3881 | 24 | 29/32 |
| http://34.43.46.91:80 | US | 615 | 24 | 29/32 |
| http://181.78.74.252:999 | CO | 786 | 23 | 23/23 |
| http://181.78.74.253:999 | CO | 797 | 23 | 23/23 |
| http://190.97.236.128:999 | VE | 726 | 22 | 22/22 |
| http://190.97.236.129:999 | VE | 714 | 22 | 22/22 |
| http://103.237.102.191:11111 | DE | 838 | 18 | 31/32 |
| http://1.231.81.166:3128 | KR | 1293 | 18 | 31/32 |
| http://95.211.174.135:3128 | NL | 1367 | 18 | 31/32 |
| http://204.76.203.9:3128 | NL | 1015 | 18 | 31/32 |
| http://204.76.203.9:8080 | NL | 724 | 18 | 24/25 |
| http://185.200.188.234:10001 | RU | 1866 | 18 | 31/32 |
| http://130.110.103.245:3128 | SA | 1232 | 18 | 30/32 |
| http://95.3.69.222:8080 | TR | 1805 | 18 | 31/32 |
| http://199.7.149.90:3128 | US | 237 | 15 | 15/15 |
| http://199.7.149.96:3128 | US | 260 | 11 | 11/11 |
| http://45.186.6.104:3128 | EC | 915 | 10 | 10/10 |
| http://64.112.184.210:3128 | US | 323 | 10 | 31/32 |
| socks5://123.58.219.171:10808 | HK | 1653 | 10 | 26/32 |
| socks5://43.162.94.99:1080 | US | 5801 | 9 | 25/32 |
| http://190.0.246.210:4040 | CO | 962 | 8 | 28/31 |
| http://47.81.56.193:8888 | TH | 1966 | 8 | 16/32 |
| http://120.232.115.170:17981 | CN | 2596 | 7 | 18/31 |
| http://103.130.61.61:8081 | ID | 2537 | 7 | 27/32 |
| http://45.66.249.187:3128 | US | 2968 | 7 | 20/23 |
| http://42.96.18.62:1311 | VN | 7541 | 6 | 21/31 |
| socks5://185.128.104.152:8443 | DE | 1186 | 6 | 7/13 |
| socks5://144.91.121.61:1088 | FR | 3598 | 6 | 30/32 |
| socks5://101.36.104.239:10808 | JP | 2425 | 6 | 26/32 |
| socks5://67.207.92.87:1088 | US | 597 | 6 | 17/31 |
| socks5://193.25.215.182:22222 | US | 947 | 6 | 29/32 |
| http://181.78.208.227:999 | CO | 7323 | 5 | 7/19 |
| http://186.33.45.219:999 | EC | 1215 | 5 | 16/21 |
| http://176.111.37.5:39811 | HK | 1076 | 5 | 27/32 |
| http://212.154.169.90:3128 | KZ | 1410 | 5 | 9/11 |
| socks5://152.89.104.11:1080 | DE | 7025 | 5 | 10/32 |
| socks5://152.32.168.221:10808 | HK | 7589 | 5 | 15/21 |
| socks5://5.130.50.118:1080 | RU | 6503 | 5 | 5/5 |
| http://179.41.11.138:8080 | AR | 877 | 4 | 4/4 |
| http://185.191.239.248:3128 | CH | 1852 | 4 | 21/31 |
| http://190.0.246.211:4040 | CO | 1986 | 4 | 27/32 |
| http://18.170.25.193:57422 | GB | 5324 | 4 | 11/28 |
| http://47.57.69.227:3128 | HK | 965 | 4 | 4/4 |
| http://103.211.103.170:3128 | HK | 665 | 4 | 4/4 |
| http://109.94.1.23:4050 | RU | 5398 | 4 | 23/32 |
| http://202.28.194.139:31280 | TH | 2099 | 4 | 30/32 |
| http://154.59.56.73:999 | VE | 6164 | 4 | 4/4 |
| http://14.251.13.20:8080 | VN | 1153 | 4 | 4/4 |
| http://210.211.113.34:80 | VN | 3118 | 4 | 4/4 |
| http://13.246.6.135:37535 | ZA | 2662 | 4 | 4/4 |
| socks4://112.28.149.152:8443 | CN | 6573 | 4 | 15/32 |
| socks4://45.61.129.165:9050 | US | 2025 | 4 | 24/32 |
| socks5://101.36.104.46:10808 | JP | 1161 | 4 | 29/32 |
| socks5://121.169.46.116:1090 | KR | 1072 | 4 | 21/32 |
| socks5://43.164.3.124:1080 | TH | 4035 | 4 | 21/31 |
| socks5://185.118.143.141:1080 | TR | 3314 | 4 | 4/4 |
| http://91.149.142.139:8080 | BY | 3633 | 3 | 5/16 |
| http://87.251.77.29:3128 | DE | 1211 | 3 | 29/32 |
| http://152.53.136.178:10000 | DE | 5140 | 3 | 4/7 |
| http://38.50.165.122:999 | DO | 7616 | 3 | 6/20 |
| http://38.75.82.211:999 | DO | 3058 | 3 | 6/10 |
| http://173.212.245.136:8888 | FR | 5831 | 3 | 6/22 |
| http://151.185.41.195:8080 | IN | 1713 | 3 | 5/6 |
| http://102.0.25.184:8080 | KE | 7151 | 3 | 6/26 |
| http://153.80.240.37:8080 | NL | 2965 | 3 | 21/32 |
| http://85.237.39.139:8080 | RU | 7196 | 3 | 6/10 |
| http://95.190.193.74:3128 | RU | 1336 | 3 | 3/3 |
| http://1.10.236.214:8080 | TH | 3745 | 3 | 3/3 |
| http://103.218.122.183:8080 | VN | 1288 | 3 | 3/3 |
| socks5://65.21.252.66:10811 | FI | 6442 | 3 | 11/20 |
| socks5://213.136.92.91:1080 | FR | 6539 | 3 | 21/32 |
| socks5://45.194.33.12:30001 | HK | 1184 | 3 | 21/28 |
| socks5://45.194.33.12:30002 | HK | 1274 | 3 | 5/6 |
| socks5://163.53.204.178:9813 | IN | 3888 | 3 | 8/31 |
| socks5://130.255.94.39:5080 | IQ | 1729 | 3 | 3/3 |
| http://45.232.0.2:8080 | AR | 4251 | 2 | 7/30 |
| http://181.209.96.157:999 | AR | 3115 | 2 | 5/28 |
| http://187.102.219.32:999 | AR | 6408 | 2 | 8/31 |
| http://27.147.153.179:3128 | BD | 2776 | 2 | 3/5 |
| http://103.177.118.145:8118 | BD | 2582 | 2 | 12/13 |
| http://118.179.81.91:81 | BD | 4557 | 2 | 3/8 |
| http://138.122.140.194:3128 | BR | 1212 | 2 | 9/26 |
| http://186.216.208.98:3128 | BR | 1761 | 2 | 8/30 |
| http://200.95.184.50:999 | CL | 7700 | 2 | 6/24 |
| http://8.138.217.152:21001 | CN | 3544 | 2 | 20/32 |
| http://39.101.175.37:17691 | CN | 4696 | 2 | 6/31 |
| http://114.236.137.41:21000 | CN | 2464 | 2 | 20/32 |
| http://181.129.158.131:999 | CO | 5783 | 2 | 5/30 |
| http://181.129.183.19:53281 | CO | 7570 | 2 | 6/27 |
| http://190.60.61.42:8080 | CO | 3431 | 2 | 2/2 |
| http://200.10.31.45:8081 | CO | 5798 | 2 | 12/29 |
| http://195.62.49.101:59061 | DE | 815 | 2 | 2/2 |
| http://38.44.17.142:999 | DO | 5021 | 2 | 13/25 |
| http://205.235.1.38:999 | EC | 7841 | 2 | 7/18 |
| http://41.196.16.233:1976 | EG | 1144 | 2 | 5/10 |
| http://45.245.208.180:8080 | EG | 6122 | 2 | 5/8 |
| http://83.45.174.91:8080 | ES | 5650 | 2 | 3/5 |
| http://194.113.38.196:3128 | FI | 3849 | 2 | 5/11 |
| http://13.38.27.183:9824 | FR | 2255 | 2 | 9/28 |
