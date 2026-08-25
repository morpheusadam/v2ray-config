# Proxy status

Generated 2026-08-25T19:59:52Z by `harvest.py`.

- **670** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1404** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **13666** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 136/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 1174 |
| socks5 | 216 |
| socks4 | 14 |

| country | entries |
|---|---|
| ID | 323 |
| CO | 60 |
| PH | 60 |
| US | 58 |
| RU | 51 |
| BD | 50 |
| BR | 47 |
| MX | 41 |
| NL | 40 |
| DE | 38 |
| IN | 37 |
| CN | 36 |
| VE | 35 |
| TR | 34 |
| EC | 31 |
| VN | 31 |
| FR | 25 |
| SG | 25 |
| DO | 20 |
| TH | 19 |
| AR | 18 |
| HK | 18 |
| JP | 17 |
| KH | 17 |
| EG | 15 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-08-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 77 | 77 | 38 | 2026-08-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 95 | 95 | 13 | 2026-08-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 100 | 100 | 55 | 2026-08-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-08-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 139 | 139 | 28 | 2026-08-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 81 | 2026-08-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 152 | 152 | 12 | 2026-08-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 188 | 188 | 71 | 2026-08-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 202 | 202 | 69 | 2026-08-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 330 | 330 | 112 | 2026-08-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-08-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-08-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-08-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-08-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1762 | 1758 | 86 | 2026-08-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1601 | 2026-08-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1978 | 1976 | 161 | 2026-08-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2105 | 2105 | 1646 | 2026-08-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2490 | 2488 | 633 | 2026-08-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2812 | 2810 | 2066 | 2026-08-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://181.39.25.196:8118 | EC | 796 | 28 | 30/31 |
| http://34.43.46.91:443 | US | 1262 | 23 | 28/31 |
| http://34.43.46.91:80 | US | 846 | 23 | 28/31 |
| http://181.78.74.252:999 | CO | 663 | 22 | 22/22 |
| http://181.78.74.253:999 | CO | 654 | 22 | 22/22 |
| http://190.97.236.128:999 | VE | 654 | 21 | 21/21 |
| http://190.97.236.129:999 | VE | 1686 | 21 | 21/21 |
| http://103.237.102.191:11111 | DE | 748 | 17 | 30/31 |
| http://1.231.81.166:3128 | KR | 1727 | 17 | 30/31 |
| http://95.211.174.135:3128 | NL | 942 | 17 | 30/31 |
| http://204.76.203.9:3128 | NL | 1132 | 17 | 30/31 |
| http://204.76.203.9:8080 | NL | 531 | 17 | 23/24 |
| http://185.200.188.234:10001 | RU | 1647 | 17 | 30/31 |
| http://130.110.103.245:3128 | SA | 1362 | 17 | 29/31 |
| http://95.3.69.222:8080 | TR | 1758 | 17 | 30/31 |
| http://199.7.149.90:3128 | US | 37 | 14 | 14/14 |
| http://199.7.149.96:3128 | US | 37 | 10 | 10/10 |
| http://45.186.6.104:3128 | EC | 610 | 9 | 9/9 |
| http://64.112.184.210:3128 | US | 327 | 9 | 30/31 |
| socks5://123.58.219.171:10808 | HK | 3540 | 9 | 25/31 |
| http://5.129.228.92:443 | NL | 732 | 8 | 14/16 |
| socks5://43.162.94.99:1080 | US | 4284 | 8 | 24/31 |
| http://190.0.246.210:4040 | CO | 6082 | 7 | 27/30 |
| http://47.81.56.193:8888 | TH | 1971 | 7 | 15/31 |
| http://120.232.115.170:17981 | CN | 1990 | 6 | 17/30 |
| http://103.130.61.61:8081 | ID | 1890 | 6 | 26/31 |
| http://45.66.249.187:3128 | US | 5932 | 6 | 19/22 |
| http://115.231.181.40:8128 | CN | 2722 | 5 | 16/30 |
| http://159.69.45.217:1083 | DE | 615 | 5 | 5/5 |
| http://175.136.239.173:8181 | MY | 3795 | 5 | 24/31 |
| http://42.96.18.62:1311 | VN | 2826 | 5 | 20/30 |
| socks5://59.152.97.233:1080 | BD | 3995 | 5 | 20/29 |
| socks5://185.128.104.152:8443 | DE | 3012 | 5 | 6/12 |
| socks5://144.91.121.61:1088 | FR | 3655 | 5 | 29/31 |
| socks5://101.36.104.239:10808 | JP | 3398 | 5 | 25/31 |
| socks5://67.207.92.87:1088 | US | 2426 | 5 | 16/30 |
| socks5://193.25.215.182:22222 | US | 2958 | 5 | 28/31 |
| http://181.78.208.227:999 | CO | 7638 | 4 | 6/18 |
| http://186.33.45.219:999 | EC | 2161 | 4 | 15/20 |
| http://190.12.150.244:999 | EC | 7999 | 4 | 20/27 |
| http://176.111.37.5:39811 | HK | 1026 | 4 | 26/31 |
| http://212.154.169.90:3128 | KZ | 1076 | 4 | 8/10 |
| http://64.76.73.131:999 | PE | 7828 | 4 | 4/4 |
| http://45.66.249.187:8181 | US | 4953 | 4 | 18/22 |
| socks5://152.89.104.11:1080 | DE | 2141 | 4 | 9/31 |
| socks5://152.32.168.221:10808 | HK | 5683 | 4 | 14/20 |
| socks5://5.130.50.118:1080 | RU | 2195 | 4 | 4/4 |
| socks5://93.123.118.15:1080 | UA | 733 | 4 | 13/29 |
| http://179.41.11.138:8080 | AR | 743 | 3 | 3/3 |
| http://16.51.148.102:8181 | AU | 2518 | 3 | 3/3 |
| http://185.191.239.248:3128 | CH | 7201 | 3 | 20/30 |
| http://190.0.246.211:4040 | CO | 2925 | 3 | 26/31 |
| http://159.69.45.217:1082 | DE | 1023 | 3 | 3/3 |
| http://217.160.249.182:8888 | DE | 855 | 3 | 3/3 |
| http://18.170.25.193:57422 | GB | 1805 | 3 | 10/27 |
| http://47.57.69.227:3128 | HK | 2746 | 3 | 3/3 |
| http://103.211.103.170:3128 | HK | 531 | 3 | 3/3 |
| http://103.174.122.98:3128 | ID | 4994 | 3 | 3/3 |
| http://168.144.210.164:3128 | IN | 1397 | 3 | 3/3 |
| http://153.51.241.50:999 | MX | 7773 | 3 | 16/28 |
| http://87.236.23.201:3128 | RU | 2478 | 3 | 3/3 |
| http://109.94.1.23:4050 | RU | 2865 | 3 | 22/31 |
| http://202.28.194.139:31280 | TH | 2662 | 3 | 29/31 |
| http://154.59.56.73:999 | VE | 7523 | 3 | 3/3 |
| http://200.59.191.27:999 | VE | 6153 | 3 | 16/26 |
| http://14.251.13.20:8080 | VN | 1406 | 3 | 3/3 |
| http://210.211.113.34:80 | VN | 6232 | 3 | 3/3 |
| http://13.246.6.135:37535 | ZA | 3177 | 3 | 3/3 |
| socks4://112.28.149.152:8443 | CN | 4782 | 3 | 14/31 |
| socks4://45.61.129.165:9050 | US | 2061 | 3 | 23/31 |
| socks5://45.95.233.128:1082 | FR | 618 | 3 | 12/30 |
| socks5://109.172.55.177:1082 | FR | 999 | 3 | 15/31 |
| socks5://101.36.104.46:10808 | JP | 3328 | 3 | 28/31 |
| socks5://110.235.246.62:1080 | KH | 1880 | 3 | 9/29 |
| socks5://121.169.46.116:1090 | KR | 3135 | 3 | 20/31 |
| socks5://43.164.3.124:1080 | TH | 3092 | 3 | 20/30 |
| socks5://185.118.143.141:1080 | TR | 1029 | 3 | 3/3 |
| socks5://45.76.164.255:1085 | US | 183 | 3 | 17/27 |
| socks5://147.45.60.246:1082 | US | 4284 | 3 | 7/30 |
| http://180.94.91.170:8080 | AF | 3562 | 2 | 2/2 |
| http://91.149.142.139:8080 | BY | 4243 | 2 | 4/15 |
| http://186.148.47.254:999 | CL | 5621 | 2 | 6/20 |
| http://179.1.182.23:999 | CO | 4951 | 2 | 3/13 |
| http://90.181.120.18:8082 | CZ | 7930 | 2 | 2/2 |
| http://87.251.77.29:3128 | DE | 1230 | 2 | 28/31 |
| http://152.53.136.178:10000 | DE | 6072 | 2 | 3/6 |
| http://38.50.165.122:999 | DO | 4095 | 2 | 5/19 |
| http://38.75.82.211:999 | DO | 2259 | 2 | 5/9 |
| http://177.234.217.84:999 | EC | 5797 | 2 | 9/26 |
| http://173.212.245.136:8888 | FR | 6490 | 2 | 5/21 |
| http://18.170.25.193:53656 | GB | 1131 | 2 | 9/31 |
| http://43.99.100.108:3128 | HK | 1522 | 2 | 24/31 |
| http://103.66.197.4:8080 | ID | 2558 | 2 | 3/15 |
| http://103.120.76.45:8080 | ID | 2589 | 2 | 3/7 |
| http://103.155.198.138:3125 | ID | 4983 | 2 | 4/21 |
| http://103.176.96.195:1111 | ID | 6559 | 2 | 3/9 |
| http://103.179.252.170:3127 | ID | 5021 | 2 | 5/11 |
| http://157.15.67.181:80 | ID | 7141 | 2 | 2/2 |
| http://165.99.194.32:8085 | ID | 7244 | 2 | 2/2 |
| http://202.47.185.35:8080 | ID | 4916 | 2 | 2/2 |
