# Proxy status

Generated 2026-11-21T23:55:22Z by `harvest.py`.

- **2173** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4412** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **27533** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 156/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3762 |
| socks5 | 644 |
| socks4 | 6 |

| country | entries |
|---|---|
| ID | 1104 |
| ?? | 740 |
| NL | 430 |
| PH | 186 |
| MX | 161 |
| CO | 158 |
| VE | 105 |
| US | 102 |
| BR | 96 |
| TH | 96 |
| TR | 93 |
| IN | 81 |
| RU | 72 |
| BD | 70 |
| EC | 62 |
| AR | 59 |
| DO | 52 |
| ZA | 42 |
| PK | 40 |
| EG | 37 |
| CN | 35 |
| PE | 35 |
| VN | 35 |
| CL | 27 |
| DE | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 97 | 97 | 18 | 2026-11-21 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 35 | 2026-11-21 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 60 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 287 | 287 | 22 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 372 | 372 | 115 | 2026-11-21 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 396 | 396 | 89 | 2026-11-21 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 401 | 401 | 254 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-21 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-21 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-21 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1014 | 1014 | 150 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1125 | 2026-11-21 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-21 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2005 | 2005 | 289 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2724 | 2724 | 760 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2732 | 2732 | 371 | 2026-11-21 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3186 | 3186 | 1706 | 2026-11-21 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5643 | 5643 | 4388 | 2026-11-21 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12435 | 12435 | 2183 | 2026-11-21 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1049 | 77 | 187/206 |
| http://130.110.103.245:3128 | SA | 2431 | 52 | 188/206 |
| http://141.94.22.37:3128 | FR | 779 | 18 | 21/22 |
| http://45.155.226.177:3128 | HK | 782 | 15 | 20/22 |
| http://4.144.146.21:80 | SG | 856 | 13 | 89/98 |
| http://15.229.149.81:3128 | BR | 2219 | 12 | 78/116 |
| http://128.199.121.61:9090 | SG | 851 | 12 | 99/126 |
| socks5://193.25.215.182:22222 | US | 880 | 12 | 171/206 |
| http://34.43.46.91:80 | US | 931 | 11 | 199/206 |
| socks5://45.61.129.165:9050 | US | 1787 | 11 | 158/206 |
| socks5://46.246.12.31:1080 | ?? | 4486 | 11 | 11/11 |
| http://15.229.149.81:1080 | BR | 2123 | 10 | 62/108 |
| http://189.51.168.164:999 | MX | 2963 | 10 | 38/42 |
| http://104.248.151.93:9090 | SG | 856 | 10 | 75/107 |
| http://20.98.234.24:8080 | ?? | 404 | 10 | 10/10 |
| socks5://69.55.49.177:38182 | US | 587 | 10 | 50/61 |
| http://103.237.102.191:11111 | DE | 861 | 9 | 193/206 |
| http://172.235.157.127:3128 | ?? | 432 | 9 | 9/9 |
| http://45.186.6.104:3128 | EC | 916 | 8 | 174/184 |
| http://103.133.26.50:8080 | ID | 1200 | 8 | 72/107 |
| http://103.133.26.72:8080 | ID | 1584 | 8 | 80/132 |
| http://103.133.26.73:3128 | ID | 1217 | 8 | 96/184 |
| http://103.158.210.80:8082 | ID | 2237 | 8 | 67/196 |
| http://110.74.195.34:25 | KH | 2118 | 8 | 70/199 |
| http://91.134.141.4:3128 | ?? | 781 | 8 | 8/8 |
| socks5://103.124.172.134:1080 | ?? | 1501 | 8 | 8/8 |
| http://181.78.195.136:999 | EC | 2873 | 7 | 36/62 |
| http://45.245.208.180:8080 | EG | 1342 | 7 | 55/79 |
| http://103.86.117.23:8080 | ID | 7895 | 7 | 40/126 |
| http://140.238.32.108:3128 | JP | 769 | 7 | 122/205 |
| http://185.238.238.49:58080 | PL | 4800 | 7 | 81/200 |
| http://154.59.56.76:999 | VE | 3402 | 7 | 120/166 |
| http://217.142.139.207:8085 | ?? | 1482 | 7 | 8/9 |
| http://200.10.30.5:8083 | CO | 4897 | 6 | 65/195 |
| http://54.36.150.233:3128 | FR | 813 | 6 | 19/28 |
| http://38.199.88.1:999 | GT | 6016 | 6 | 17/26 |
| http://161.49.87.222:8095 | PH | 1738 | 6 | 28/102 |
| http://154.59.56.72:999 | VE | 3945 | 6 | 122/165 |
| http://119.94.185.43:8082 | ?? | 5119 | 6 | 6/6 |
| http://125.25.53.180:8080 | ?? | 6022 | 6 | 6/6 |
| http://147.161.246.34:12544 | ?? | 2672 | 6 | 6/6 |
| http://147.161.246.34:80 | ?? | 2409 | 6 | 6/6 |
| socks5://209.50.255.91:1080 | US | 522 | 6 | 59/123 |
| socks5://103.248.228.166:5555 | ?? | 1005 | 6 | 8/9 |
| http://41.65.55.10:1976 | EG | 3442 | 5 | 17/65 |
| http://45.240.232.61:8080 | EG | 2545 | 5 | 80/186 |
| http://49.0.2.166:8080 | ID | 7324 | 5 | 26/89 |
| http://103.120.175.243:9191 | ID | 2600 | 5 | 14/69 |
| http://163.61.245.26:1452 | ID | 3040 | 5 | 14/36 |
| http://38.252.228.2:999 | MX | 2035 | 5 | 10/23 |
| http://103.167.229.147:8080 | NP | 3255 | 5 | 9/21 |
| http://47.129.130.0:9898 | SG | 2707 | 5 | 43/123 |
| http://146.190.80.158:9090 | SG | 860 | 5 | 94/132 |
| http://101.96.122.196:8080 | VN | 5164 | 5 | 12/46 |
| http://20.33.10.132:80 | ZA | 6113 | 5 | 28/80 |
| http://16.5.7.5:8118 | ?? | 2016 | 5 | 5/5 |
| http://102.222.240.10:9999 | ?? | 6968 | 5 | 5/5 |
| http://114.244.212.147:8888 | ?? | 2076 | 5 | 5/5 |
| http://147.161.246.34:11588 | ?? | 2730 | 5 | 5/5 |
| http://147.161.246.34:12673 | ?? | 2641 | 5 | 5/5 |
| socks5://101.36.104.46:10808 | JP | 3285 | 5 | 170/206 |
| socks5://101.36.104.239:10808 | JP | 1637 | 5 | 168/206 |
| http://187.102.219.42:999 | AR | 1622 | 4 | 114/201 |
| http://177.87.15.141:8080 | BR | 5113 | 4 | 12/39 |
| http://190.7.138.78:8080 | CO | 2974 | 4 | 53/135 |
| http://190.144.238.66:8080 | CO | 2470 | 4 | 34/156 |
| http://177.234.217.235:999 | EC | 5588 | 4 | 94/175 |
| http://190.12.150.244:999 | EC | 2439 | 4 | 149/202 |
| http://165.154.7.156:8888 | HK | 3077 | 4 | 23/65 |
| http://36.50.184.90:8080 | ID | 4385 | 4 | 18/107 |
| http://36.94.39.146:8080 | ID | 4551 | 4 | 18/100 |
| http://103.124.137.150:20 | ID | 5773 | 4 | 33/147 |
| http://103.166.254.220:3124 | ID | 3779 | 4 | 19/93 |
| http://103.173.138.236:1111 | ID | 1750 | 4 | 42/206 |
| http://157.15.40.252:7777 | ID | 1571 | 4 | 39/205 |
| http://160.22.45.114:8080 | ID | 1402 | 4 | 42/65 |
| http://160.22.198.19:8082 | ID | 2562 | 4 | 26/61 |
| http://31.24.252.97:8080 | IQ | 7592 | 4 | 20/39 |
| http://5.181.178.46:8080 | JP | 3541 | 4 | 20/82 |
| http://178.217.168.164:55443 | KG | 6735 | 4 | 47/186 |
| http://49.156.44.116:8080 | KH | 6651 | 4 | 18/40 |
| http://43.202.114.177:7428 | KR | 3126 | 4 | 52/120 |
| http://187.245.202.17:999 | MX | 4703 | 4 | 7/29 |
| http://124.105.86.222:8090 | PH | 2292 | 4 | 32/158 |
| http://128.199.113.85:9090 | SG | 856 | 4 | 24/37 |
| http://167.99.74.174:9090 | SG | 855 | 4 | 111/166 |
| http://201.7.31.170:8080 | TR | 4999 | 4 | 32/149 |
| http://195.226.213.251:8888 | UA | 2608 | 4 | 81/200 |
| http://40.160.36.112:999 | US | 2462 | 4 | 24/77 |
| http://152.70.198.2:1080 | US | 608 | 4 | 48/126 |
| http://38.172.181.0:999 | VE | 2891 | 4 | 59/113 |
| http://190.97.249.30:999 | VE | 887 | 4 | 10/34 |
| http://200.36.152.6:999 | VE | 4508 | 4 | 26/103 |
| http://38.210.179.8:999 | ?? | 5036 | 4 | 4/4 |
| http://45.135.95.185:3128 | ?? | 1538 | 4 | 4/4 |
| http://103.20.108.51:8080 | ?? | 5417 | 4 | 5/6 |
| http://103.84.210.30:8080 | ?? | 6564 | 4 | 6/10 |
| http://191.44.125.14:8080 | ?? | 1327 | 4 | 5/6 |
| http://222.111.130.73:8080 | ?? | 1968 | 4 | 4/4 |
| socks4://188.226.27.24:1080 | RU | 2641 | 4 | 31/42 |
