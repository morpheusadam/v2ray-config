# Proxy status

Generated 2026-11-11T00:13:19Z by `harvest.py`.

- **2290** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4584** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35586** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 151/600 (25%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2637 |
| socks5 | 1927 |
| socks4 | 20 |

| country | entries |
|---|---|
| NL | 1694 |
| ID | 763 |
| ?? | 144 |
| US | 141 |
| PH | 140 |
| CO | 125 |
| MX | 120 |
| CN | 106 |
| TH | 88 |
| TR | 80 |
| BR | 76 |
| RU | 75 |
| BD | 69 |
| VE | 68 |
| IN | 63 |
| EC | 56 |
| DO | 47 |
| AR | 46 |
| PK | 46 |
| VN | 40 |
| DE | 34 |
| PE | 34 |
| SG | 33 |
| EG | 32 |
| ZA | 30 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 3 | 2026-11-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 87 | 87 | 10 | 2026-11-11 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 41 | 2026-11-11 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-11-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 187 | 187 | 24 | 2026-11-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 248 | 248 | 72 | 2026-11-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 323 | 323 | 228 | 2026-11-11 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 346 | 346 | 115 | 2026-11-11 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-11 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-11 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 444 | 2026-11-11 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 799 | 799 | 102 | 2026-11-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1128 | 2026-11-11 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1710 | 1710 | 98 | 2026-11-11 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2202 | 2202 | 631 | 2026-11-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2539 | 2539 | 514 | 2026-11-11 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2621 | 2621 | 1454 | 2026-11-11 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5199 | 5199 | 3946 | 2026-11-11 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11804 | 11804 | 1877 | 2026-11-11 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1602 | 60 | 80/162 |
| http://176.111.37.5:39811 | HK | 829 | 55 | 165/184 |
| http://34.43.46.91:80 | US | 435 | 54 | 178/184 |
| http://4.144.146.21:80 | SG | 1192 | 52 | 69/76 |
| http://176.111.37.216:39811 | HK | 921 | 47 | 156/184 |
| http://34.43.46.91:443 | US | 362 | 33 | 173/184 |
| http://130.110.103.245:3128 | SA | 1151 | 30 | 166/184 |
| http://103.133.26.72:8080 | ID | 1590 | 27 | 64/110 |
| http://45.189.57.114:3129 | EC | 1895 | 26 | 26/26 |
| http://103.133.26.119:8080 | ID | 1862 | 20 | 63/94 |
| http://189.51.168.164:999 | MX | 1869 | 20 | 20/20 |
| http://49.229.100.235:8080 | TH | 1600 | 20 | 92/132 |
| http://171.100.254.137:8080 | TH | 1551 | 20 | 20/20 |
| http://43.161.254.16:3128 | HK | 1863 | 19 | 21/24 |
| http://103.130.61.61:8081 | ID | 4133 | 19 | 153/184 |
| http://184.75.221.82:3118 | CA | 214 | 18 | 131/149 |
| http://102.244.78.61:8089 | CM | 1235 | 15 | 59/72 |
| http://45.186.6.104:3128 | EC | 575 | 14 | 153/162 |
| http://38.180.18.103:3128 | BE | 516 | 13 | 13/13 |
| http://190.71.72.85:2525 | CO | 551 | 12 | 28/69 |
| http://102.244.78.61:8090 | CM | 1237 | 11 | 60/76 |
| socks5://121.46.226.221:10808 | CN | 1626 | 10 | 10/10 |
| http://177.234.217.44:999 | EC | 1524 | 8 | 31/84 |
| http://84.36.141.180:1981 | EG | 5153 | 8 | 35/135 |
| http://104.248.151.93:9090 | SG | 1177 | 8 | 63/85 |
| http://172.239.170.24:3128 | US | 1234 | 8 | 13/18 |
| http://45.65.224.125:999 | AR | 913 | 7 | 34/46 |
| http://102.244.78.61:8083 | CM | 1193 | 7 | 58/72 |
| http://102.244.78.61:8088 | CM | 1239 | 7 | 57/72 |
| http://123.121.108.22:8888 | CN | 1903 | 7 | 25/35 |
| http://204.199.106.226:999 | CO | 6217 | 7 | 7/7 |
| http://103.237.102.191:11111 | DE | 666 | 7 | 175/184 |
| http://43.155.62.157:443 | HK | 2647 | 7 | 74/87 |
| http://82.152.138.127:999 | MX | 325 | 7 | 59/146 |
| http://189.51.168.165:999 | MX | 450 | 7 | 89/96 |
| socks5://5.255.113.177:1080 | NL | 1132 | 7 | 33/82 |
| http://15.223.187.219:55865 | CA | 900 | 6 | 38/98 |
| http://102.244.78.61:8080 | CM | 1225 | 6 | 61/73 |
| http://123.119.24.241:8888 | CN | 6303 | 6 | 46/119 |
| http://123.121.99.174:8888 | CN | 1713 | 6 | 6/6 |
| http://221.221.144.98:8888 | CN | 3005 | 6 | 17/41 |
| http://45.65.137.218:999 | CO | 652 | 6 | 69/149 |
| http://45.245.208.180:8080 | EG | 3128 | 6 | 39/57 |
| http://202.58.77.131:7777 | ID | 3255 | 6 | 14/24 |
| http://206.135.80.74:999 | MX | 4340 | 6 | 6/6 |
| http://144.124.251.24:10771 | NL | 605 | 6 | 73/116 |
| http://195.158.8.123:3128 | UZ | 2024 | 6 | 121/182 |
| socks5://101.36.104.46:10808 | JP | 3456 | 6 | 157/184 |
| http://15.223.187.219:35507 | CA | 1071 | 5 | 23/97 |
| http://185.191.239.248:3128 | CH | 1182 | 5 | 133/183 |
| http://102.244.78.61:8081 | CM | 1238 | 5 | 57/70 |
| http://123.121.109.207:8888 | CN | 2221 | 5 | 5/5 |
| http://177.234.217.92:999 | EC | 2821 | 5 | 26/33 |
| http://177.234.217.93:999 | EC | 2970 | 5 | 31/43 |
| http://38.226.242.83:8080 | ID | 7734 | 5 | 11/29 |
| http://45.174.241.224:999 | MX | 1297 | 5 | 5/5 |
| http://206.135.47.107:999 | MX | 2536 | 5 | 32/54 |
| http://38.210.106.24:999 | PE | 3834 | 5 | 12/39 |
| http://180.191.0.205:8081 | PH | 3405 | 5 | 11/24 |
| http://61.91.162.126:8080 | TH | 1550 | 5 | 96/127 |
| http://103.10.231.189:8080 | TH | 1860 | 5 | 123/169 |
| http://195.142.250.34:8080 | TR | 6251 | 5 | 16/42 |
| http://13.143.240.243:999 | VE | 5992 | 5 | 5/5 |
| socks5://157.254.223.42:1080 | IN | 2517 | 5 | 6/13 |
| socks5://171.25.158.95:1080 | SE | 4144 | 5 | 78/99 |
| http://45.65.226.171:999 | AR | 1888 | 4 | 12/22 |
| http://27.147.155.206:12051 | BD | 1714 | 4 | 4/4 |
| http://1.15.53.214:8888 | CN | 1807 | 4 | 52/178 |
| http://111.192.28.24:8888 | CN | 1948 | 4 | 5/6 |
| http://45.65.138.48:999 | CO | 2325 | 4 | 87/184 |
| http://41.33.245.139:1981 | EG | 3235 | 4 | 15/22 |
| http://168.228.44.66:999 | HN | 3528 | 4 | 24/96 |
| http://103.139.98.118:8080 | ID | 5247 | 4 | 25/168 |
| http://160.22.45.114:8080 | ID | 4749 | 4 | 27/43 |
| http://160.22.198.19:8082 | ID | 2771 | 4 | 14/39 |
| http://51.17.99.116:37158 | IL | 1640 | 4 | 23/70 |
| http://40.192.70.191:11223 | IN | 3247 | 4 | 9/28 |
| http://43.128.144.133:18080 | KR | 1719 | 4 | 4/4 |
| http://206.135.47.110:999 | MX | 1764 | 4 | 29/55 |
| http://144.124.251.24:10226 | NL | 626 | 4 | 72/115 |
| http://144.124.251.24:10337 | NL | 525 | 4 | 69/116 |
| http://144.124.251.24:10800 | NL | 631 | 4 | 70/116 |
| http://180.191.153.75:2020 | PH | 5865 | 4 | 9/21 |
| http://152.42.177.32:8888 | SG | 1162 | 4 | 95/144 |
| http://159.223.41.216:9090 | SG | 1309 | 4 | 105/144 |
| http://1.2.248.41:80 | TH | 4708 | 4 | 11/29 |
| http://138.59.11.65:999 | VE | 4572 | 4 | 7/18 |
| socks5://37.18.73.60:5566 | RU | 2001 | 4 | 33/81 |
| socks5://95.31.115.101:9150 | RU | 1898 | 4 | 4/4 |
| socks5://43.156.152.110:1080 | SG | 3181 | 4 | 4/4 |
| socks5://4.255.114.124:3000 | US | 807 | 4 | 4/4 |
| socks5://13.90.182.199:3000 | US | 1168 | 4 | 4/4 |
| socks5://13.90.182.199:3001 | US | 1169 | 4 | 4/4 |
| socks5://20.121.252.238:3000 | US | 731 | 4 | 4/4 |
| socks5://45.61.129.165:9050 | US | 2587 | 4 | 141/184 |
| socks5://69.55.49.177:38182 | US | 523 | 4 | 37/39 |
| socks5://172.171.169.205:3000 | US | 1128 | 4 | 4/4 |
| http://181.209.110.27:999 | AR | 7285 | 3 | 20/93 |
| http://187.102.219.64:999 | AR | 6441 | 3 | 76/123 |
| http://103.113.152.73:14158 | BD | 6200 | 3 | 46/178 |
