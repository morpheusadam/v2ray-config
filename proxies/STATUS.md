# Proxy status

Generated 2026-08-17T19:56:57Z by `harvest.py`.

- **696** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **1038** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **12849** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 201/600 (34%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 779 |
| socks5 | 244 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 219 |
| US | 89 |
| CN | 50 |
| RU | 48 |
| CO | 47 |
| PH | 35 |
| BD | 28 |
| BR | 28 |
| NL | 28 |
| VN | 25 |
| VE | 24 |
| FR | 23 |
| MX | 23 |
| SG | 23 |
| DE | 22 |
| TR | 21 |
| EC | 19 |
| HK | 19 |
| IN | 18 |
| KH | 15 |
| TH | 13 |
| CL | 12 |
| GB | 12 |
| DO | 11 |
| IR | 11 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-08-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 65 | 65 | 40 | 2026-08-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 94 | 94 | 45 | 2026-08-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-08-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 110 | 110 | 31 | 2026-08-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 121 | 121 | 51 | 2026-08-17 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 134 | 134 | 27 | 2026-08-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 137 | 137 | 29 | 2026-08-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-08-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 179 | 179 | 12 | 2026-08-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 163 | 2026-08-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 531 | 2026-08-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 581 | 581 | 287 | 2026-08-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 457 | 2026-08-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-08-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1618 | 2026-08-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1809 | 1805 | 172 | 2026-08-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2005 | 2003 | 188 | 2026-08-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2370 | 2370 | 1913 | 2026-08-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2498 | 2496 | 704 | 2026-08-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2768 | 2766 | 2254 | 2026-08-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 3999 | 15 | 15/15 |
| http://64.112.184.210:3128 | US | 736 | 15 | 15/15 |
| socks5://69.55.49.177:38182 | US | 1134 | 15 | 15/15 |
| http://181.39.25.196:8118 | EC | 896 | 12 | 14/15 |
| http://190.0.246.210:4040 | CO | 1657 | 11 | 13/14 |
| http://14.139.235.82:3128 | IN | 6790 | 7 | 12/15 |
| http://34.43.46.91:443 | US | 368 | 7 | 12/15 |
| http://34.43.46.91:80 | US | 501 | 7 | 12/15 |
| http://181.78.74.252:999 | CO | 807 | 6 | 6/6 |
| http://181.78.74.253:999 | CO | 812 | 6 | 6/6 |
| http://157.230.178.216:40000 | US | 1356 | 6 | 13/14 |
| socks5://147.45.60.139:1082 | US | 310 | 6 | 6/6 |
| http://174.137.134.182:2999 | US | 1131 | 5 | 13/14 |
| http://190.97.229.118:999 | VE | 3259 | 5 | 5/5 |
| http://190.97.236.128:999 | VE | 804 | 5 | 5/5 |
| http://190.97.236.129:999 | VE | 784 | 5 | 5/5 |
| http://200.10.30.5:8083 | CO | 5721 | 4 | 4/4 |
| http://186.33.45.219:999 | EC | 1585 | 4 | 4/4 |
| http://200.59.191.27:999 | VE | 4982 | 4 | 8/10 |
| socks5://5.249.165.195:20000 | US | 421 | 4 | 11/12 |
| http://38.75.82.213:999 | DO | 6488 | 3 | 4/9 |
| http://213.136.77.119:8888 | FR | 1222 | 3 | 3/3 |
| socks5://103.96.233.10:1080 | AF | 3499 | 3 | 4/13 |
| socks5://147.45.60.124:1082 | US | 3787 | 3 | 9/15 |
| http://177.93.33.55:999 | CO | 5337 | 2 | 2/2 |
| http://181.78.7.222:8080 | CO | 4636 | 2 | 3/4 |
| http://181.78.74.171:999 | CO | 791 | 2 | 2/2 |
| http://181.78.74.174:999 | CO | 802 | 2 | 2/2 |
| http://45.176.99.58:999 | DO | 1547 | 2 | 6/10 |
| http://45.71.0.121:999 | EC | 7167 | 2 | 2/2 |
| http://45.71.186.212:999 | EC | 6417 | 2 | 2/2 |
| http://181.78.203.148:999 | EC | 5778 | 2 | 3/13 |
| http://190.12.150.244:999 | EC | 3650 | 2 | 7/11 |
| http://153.51.241.50:999 | MX | 7152 | 2 | 7/12 |
| http://200.39.153.1:999 | PE | 3527 | 2 | 3/9 |
| http://49.51.253.118:8888 | US | 385 | 2 | 2/2 |
| http://104.194.8.103:40001 | US | 125 | 2 | 2/2 |
| socks4://163.192.14.135:50161 | US | 390 | 2 | 8/14 |
| socks5://45.76.164.255:1085 | US | 1503 | 2 | 8/11 |
| socks5://147.45.60.110:1082 | US | 2408 | 2 | 5/14 |
| socks5://147.45.60.250:1082 | US | 5421 | 2 | 5/15 |
| socks5://178.130.47.50:1082 | US | 365 | 2 | 4/5 |
| socks5://216.106.179.216:49473 | US | 5107 | 2 | 3/11 |
| http://168.194.34.196:9001 | AR | 2577 | 1 | 4/13 |
| http://179.43.103.97:8080 | AR | 5676 | 1 | 1/1 |
| http://181.114.230.37:8080 | AR | 6948 | 1 | 1/1 |
| http://186.38.100.130:999 | AR | 7803 | 1 | 2/11 |
| http://187.102.219.42:999 | AR | 5348 | 1 | 6/10 |
| http://16.26.143.154:30001 | AU | 5133 | 1 | 1/1 |
| http://16.26.154.68:53546 | AU | 2748 | 1 | 4/11 |
| http://43.246.200.252:8090 | BD | 7269 | 1 | 2/9 |
| http://103.106.241.74:8080 | BD | 2119 | 1 | 2/3 |
| http://103.133.201.243:8080 | BD | 6559 | 1 | 2/13 |
| http://103.134.27.129:8080 | BD | 7965 | 1 | 2/3 |
| http://103.134.242.121:8080 | BD | 5484 | 1 | 2/11 |
| http://103.142.69.62:8080 | BD | 4876 | 1 | 4/13 |
| http://103.245.96.161:3214 | BD | 6785 | 1 | 2/7 |
| http://113.11.120.105:30226 | BD | 3665 | 1 | 4/14 |
| http://118.179.213.183:81 | BD | 6310 | 1 | 1/1 |
| http://123.200.8.170:10000 | BD | 3606 | 1 | 4/13 |
| http://182.160.124.153:12331 | BD | 2977 | 1 | 3/7 |
| http://190.181.59.147:999 | BO | 6408 | 1 | 3/5 |
| http://45.175.171.4:8085 | BR | 5264 | 1 | 1/1 |
| http://131.255.227.104:3128 | BR | 5543 | 1 | 2/9 |
| http://168.194.146.179:8080 | BR | 5521 | 1 | 1/1 |
| http://170.81.131.70:3128 | BR | 5670 | 1 | 2/9 |
| http://177.85.7.122:8080 | BR | 3682 | 1 | 3/14 |
| http://177.177.59.253:8080 | BR | 5518 | 1 | 3/9 |
| http://177.190.145.161:8080 | BR | 4768 | 1 | 1/1 |
| http://179.160.71.58:8085 | BR | 1058 | 1 | 1/1 |
| http://186.216.208.98:3128 | BR | 6922 | 1 | 4/13 |
| http://189.50.45.46:1995 | BR | 7922 | 1 | 2/10 |
| http://191.252.219.129:8889 | BR | 1128 | 1 | 1/1 |
| http://201.20.42.46:3127 | BR | 7084 | 1 | 3/13 |
| http://201.71.24.65:8082 | BR | 7058 | 1 | 2/4 |
| http://201.140.209.33:3128 | BR | 6230 | 1 | 1/1 |
| http://40.176.175.23:26204 | CA | 4431 | 1 | 1/1 |
| http://38.7.206.186:999 | CL | 7317 | 1 | 3/12 |
| http://45.4.0.12:999 | CL | 7722 | 1 | 2/3 |
| http://45.225.207.183:999 | CL | 6664 | 1 | 1/1 |
| http://45.239.208.5:999 | CL | 6349 | 1 | 4/7 |
| http://152.230.60.66:999 | CL | 3505 | 1 | 1/1 |
| http://186.148.47.254:999 | CL | 1956 | 1 | 2/4 |
| http://200.95.184.50:999 | CL | 3069 | 1 | 2/7 |
| http://207.248.0.193:999 | CL | 2897 | 1 | 3/10 |
| http://1.15.53.214:8888 | CN | 3691 | 1 | 4/9 |
| http://8.138.217.152:21001 | CN | 2188 | 1 | 8/15 |
| http://27.185.218.213:17981 | CN | 2238 | 1 | 7/15 |
| http://39.106.165.196:8080 | CN | 1710 | 1 | 5/11 |
| http://39.106.170.168:8080 | CN | 1231 | 1 | 5/13 |
| http://47.101.182.85:13443 | CN | 1889 | 1 | 1/1 |
| http://47.107.82.96:30051 | CN | 1713 | 1 | 6/8 |
| http://47.121.139.13:3128 | CN | 1420 | 1 | 6/14 |
| http://49.233.205.10:3128 | CN | 5451 | 1 | 3/14 |
| http://101.5.200.193:6789 | CN | 2011 | 1 | 1/1 |
| http://101.206.186.99:8080 | CN | 2489 | 1 | 10/15 |
| http://101.251.204.174:8080 | CN | 1913 | 1 | 1/1 |
| http://112.74.101.87:9999 | CN | 3563 | 1 | 4/5 |
| http://114.94.148.37:18080 | CN | 2112 | 1 | 11/14 |
| http://116.62.202.70:17900 | CN | 3688 | 1 | 4/11 |
