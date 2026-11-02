# Proxy status

Generated 2026-11-02T22:42:19Z by `harvest.py`.

- **2106** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4959** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33741** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 116/600 (19%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3018 |
| socks5 | 1927 |
| socks4 | 14 |

| country | entries |
|---|---|
| NL | 1696 |
| ?? | 823 |
| ID | 781 |
| PH | 120 |
| CO | 114 |
| MX | 105 |
| US | 85 |
| VE | 75 |
| TH | 74 |
| BD | 71 |
| BR | 63 |
| RU | 60 |
| TR | 58 |
| CN | 52 |
| DO | 49 |
| IN | 49 |
| AR | 45 |
| EC | 45 |
| PE | 35 |
| SG | 29 |
| DE | 28 |
| PK | 28 |
| EG | 27 |
| JP | 24 |
| ZA | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 11 | 11 | 5 | 2026-11-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 63 | 63 | 6 | 2026-11-02 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 145 | 145 | 21 | 2026-11-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 55 | 2026-11-02 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 61 | 2026-11-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-02 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 169 | 169 | 63 | 2026-11-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 309 | 309 | 177 | 2026-11-02 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-02 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-11-02 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 442 | 2026-11-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 842 | 842 | 361 | 2026-11-02 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1080 | 1080 | 417 | 2026-11-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1136 | 2026-11-02 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1584 | 2026-11-02 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1829 | 1829 | 266 | 2026-11-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2463 | 2463 | 665 | 2026-11-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2948 | 2948 | 1835 | 2026-11-02 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3346 | 3346 | 1024 | 2026-11-02 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4938 | 4938 | 3683 | 2026-11-02 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11357 | 11356 | 2639 | 2026-11-02 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1455 | 87 | 154/167 |
| http://149.130.173.58:9443 | CO | 694 | 78 | 78/78 |
| http://103.237.102.191:11111 | DE | 946 | 54 | 160/167 |
| http://103.133.26.73:3128 | ID | 1306 | 43 | 63/145 |
| http://176.111.37.5:39811 | HK | 969 | 38 | 148/167 |
| http://34.43.46.91:80 | US | 1204 | 37 | 161/167 |
| http://4.144.146.21:80 | SG | 906 | 35 | 52/59 |
| http://176.111.37.216:39811 | HK | 1083 | 30 | 139/167 |
| http://34.43.46.91:443 | US | 585 | 16 | 156/167 |
| http://167.172.76.176:9090 | SG | 946 | 14 | 91/128 |
| socks5://101.36.104.239:10808 | JP | 1328 | 14 | 143/167 |
| http://130.110.103.245:3128 | SA | 2528 | 13 | 149/167 |
| socks5://45.61.188.134:44499 | US | 6702 | 13 | 69/134 |
| socks5://193.25.215.182:22222 | US | 480 | 13 | 140/167 |
| http://103.133.26.72:8080 | ID | 2167 | 10 | 47/93 |
| http://81.19.210.10:80 | GB | 1486 | 9 | 20/28 |
| http://154.59.56.78:999 | VE | 2592 | 9 | 86/123 |
| http://45.189.57.114:3129 | ?? | 830 | 9 | 9/9 |
| http://15.229.149.81:1080 | BR | 2904 | 8 | 32/69 |
| http://102.244.78.61:8085 | CM | 1421 | 8 | 45/57 |
| http://102.244.78.61:8087 | CM | 1399 | 8 | 44/57 |
| http://102.68.76.247:5566 | KE | 4079 | 8 | 43/120 |
| http://102.244.78.61:8090 | CM | 1441 | 7 | 45/59 |
| http://38.172.160.16:999 | VE | 1516 | 7 | 70/118 |
| http://200.59.191.27:999 | VE | 4133 | 7 | 111/162 |
| http://130.127.204.197:8080 | ?? | 416 | 7 | 7/7 |
| http://45.65.224.74:999 | AR | 5202 | 6 | 25/32 |
| http://123.200.8.170:10000 | BD | 3012 | 6 | 73/165 |
| http://102.244.78.61:8082 | CM | 1404 | 6 | 45/56 |
| http://102.244.78.61:8089 | CM | 1428 | 6 | 43/55 |
| http://190.12.150.244:999 | EC | 3249 | 6 | 119/163 |
| http://185.238.238.49:58080 | PL | 5197 | 6 | 55/161 |
| http://185.238.238.113:58080 | PL | 4613 | 6 | 45/136 |
| http://154.59.56.72:999 | VE | 6255 | 6 | 93/126 |
| http://154.59.56.73:999 | VE | 4129 | 6 | 98/139 |
| socks5://69.55.49.177:38182 | US | 925 | 6 | 21/22 |
| http://187.102.219.32:999 | AR | 2967 | 5 | 56/166 |
| http://186.96.111.214:999 | CO | 2346 | 5 | 75/156 |
| http://45.186.6.104:3128 | EC | 825 | 5 | 137/145 |
| http://197.164.101.13:1981 | EG | 3803 | 5 | 55/156 |
| http://102.164.252.150:8080 | GQ | 5963 | 5 | 49/126 |
| http://164.163.74.97:999 | HN | 4981 | 5 | 28/89 |
| http://13.208.246.143:46557 | JP | 2378 | 5 | 33/127 |
| http://195.226.213.251:8888 | UA | 2770 | 5 | 65/161 |
| http://165.154.162.73:8888 | US | 890 | 5 | 110/167 |
| socks5://121.169.46.116:1090 | KR | 1380 | 5 | 115/167 |
| socks5://45.61.129.165:9050 | US | 1775 | 5 | 126/167 |
| http://35.183.29.62:8051 | CA | 1468 | 4 | 5/7 |
| http://123.121.134.141:8888 | CN | 3225 | 4 | 17/28 |
| http://190.0.246.213:4040 | CO | 730 | 4 | 122/132 |
| http://198.244.254.77:3128 | GB | 5269 | 4 | 44/51 |
| http://43.155.62.157:443 | HK | 787 | 4 | 60/70 |
| http://36.64.54.98:8080 | ID | 5067 | 4 | 26/79 |
| http://45.198.11.183:9191 | ID | 3264 | 4 | 13/48 |
| http://103.178.86.93:8080 | ID | 5210 | 4 | 11/28 |
| http://103.189.97.113:8087 | ID | 3869 | 4 | 34/159 |
| http://160.22.207.95:8082 | ID | 4016 | 4 | 38/145 |
| http://46.209.30.11:8080 | IR | 1692 | 4 | 23/30 |
| http://189.51.168.165:999 | MX | 569 | 4 | 73/79 |
| http://206.135.47.107:999 | MX | 1607 | 4 | 19/37 |
| http://179.63.6.239:999 | PE | 5817 | 4 | 14/31 |
| http://1.4.141.68:80 | TH | 2633 | 4 | 11/28 |
| http://43.251.205.146:8080 | TH | 4845 | 4 | 38/133 |
| http://45.175.39.64:8080 | VE | 5158 | 4 | 35/152 |
| http://154.59.56.74:999 | VE | 6996 | 4 | 87/130 |
| http://41.78.36.250:8005 | ZA | 5557 | 4 | 15/56 |
| http://38.19.43.108:999 | ?? | 3379 | 4 | 8/13 |
| http://38.19.213.80:999 | ?? | 5423 | 4 | 5/6 |
| http://77.104.76.230:9001 | ?? | 6614 | 4 | 7/11 |
| http://103.147.134.79:8082 | ?? | 2253 | 4 | 5/7 |
| http://103.208.101.34:8080 | ?? | 2632 | 4 | 4/4 |
| http://161.22.33.169:999 | ?? | 2583 | 4 | 4/4 |
| http://180.180.156.111:80 | ?? | 3958 | 4 | 5/7 |
| http://190.123.83.137:999 | ?? | 1296 | 4 | 4/4 |
| socks5://101.36.104.46:10808 | JP | 983 | 4 | 143/167 |
| http://168.194.34.196:9001 | AR | 2449 | 3 | 61/165 |
| http://180.211.161.26:8080 | BD | 7357 | 3 | 22/79 |
| http://15.229.149.81:3128 | BR | 3874 | 3 | 46/77 |
| http://168.195.168.182:8080 | BR | 6936 | 3 | 40/162 |
| http://119.188.131.55:17981 | CN | 1640 | 3 | 86/167 |
| http://8.243.167.51:999 | CO | 3728 | 3 | 13/54 |
| http://38.199.66.11:999 | CO | 7069 | 3 | 17/74 |
| http://45.65.137.218:999 | CO | 1786 | 3 | 55/132 |
| http://18.157.159.247:13401 | DE | 3546 | 3 | 29/127 |
| http://38.159.37.173:999 | DO | 2451 | 3 | 21/122 |
| http://38.196.176.132:999 | DO | 7428 | 3 | 9/29 |
| http://190.93.191.20:999 | DO | 6681 | 3 | 4/25 |
| http://177.234.194.173:999 | EC | 7442 | 3 | 18/112 |
| http://177.234.217.92:999 | EC | 5775 | 3 | 11/16 |
| http://177.234.217.235:999 | EC | 1505 | 3 | 67/136 |
| http://181.78.203.3:999 | EC | 7421 | 3 | 19/87 |
| http://37.187.109.70:10111 | FR | 5765 | 3 | 56/167 |
| http://85.117.56.85:8080 | GE | 7936 | 3 | 14/51 |
| http://38.183.146.122:8080 | ID | 7285 | 3 | 12/87 |
| http://41.216.190.239:8080 | ID | 4524 | 3 | 24/75 |
| http://103.133.26.119:8080 | ID | 1604 | 3 | 46/77 |
| http://103.155.196.83:8082 | ID | 3098 | 3 | 32/80 |
| http://103.158.210.80:8082 | ID | 3063 | 3 | 44/157 |
| http://103.173.162.39:8818 | ID | 5064 | 3 | 23/163 |
| http://103.176.96.225:8082 | ID | 4360 | 3 | 35/112 |
