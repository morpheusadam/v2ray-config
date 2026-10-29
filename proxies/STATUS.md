# Proxy status

Generated 2026-10-29T23:34:14Z by `harvest.py`.

- **2759** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4804** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39780** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 189/600 (32%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2448 |
| http | 2353 |
| socks4 | 3 |

| country | entries |
|---|---|
| NL | 2266 |
| ID | 745 |
| ?? | 221 |
| PH | 117 |
| CO | 112 |
| US | 90 |
| MX | 85 |
| RU | 72 |
| CN | 63 |
| TH | 60 |
| VE | 57 |
| BD | 54 |
| TR | 54 |
| BR | 53 |
| IN | 46 |
| EC | 45 |
| AR | 38 |
| DO | 38 |
| SG | 34 |
| VN | 31 |
| PE | 29 |
| EG | 28 |
| PK | 27 |
| JP | 26 |
| KH | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-10-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 98 | 98 | 40 | 2026-10-29 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-10-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 159 | 159 | 94 | 2026-10-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 247 | 247 | 81 | 2026-10-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 281 | 281 | 68 | 2026-10-29 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-10-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 724 | 724 | 260 | 2026-10-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 762 | 762 | 231 | 2026-10-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1601 | 1601 | 26 | 2026-10-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-10-29 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1632 | 1632 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1595 | 2026-10-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2242 | 2242 | 698 | 2026-10-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2757 | 2757 | 1793 | 2026-10-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3135 | 3135 | 990 | 2026-10-29 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 80161 | 80161 | 66185 | 2026-10-29 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 86969 | 86968 | 2903 | 2026-10-29 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2782 | 80 | 147/160 |
| http://149.130.173.58:9443 | CO | 699 | 71 | 71/71 |
| http://103.237.102.191:11111 | DE | 977 | 47 | 153/160 |
| http://45.186.6.104:3128 | EC | 2839 | 41 | 131/138 |
| http://103.133.26.73:3128 | ID | 1303 | 36 | 56/138 |
| http://103.133.26.119:8080 | ID | 1541 | 36 | 40/70 |
| http://176.111.37.5:39811 | HK | 929 | 31 | 141/160 |
| http://34.43.46.91:80 | US | 795 | 30 | 154/160 |
| http://4.144.146.21:80 | SG | 897 | 28 | 45/52 |
| http://190.0.246.210:4040 | CO | 2742 | 27 | 146/159 |
| http://43.155.62.157:443 | HK | 796 | 27 | 55/63 |
| http://186.5.94.206:999 | EC | 5012 | 25 | 113/122 |
| http://189.51.168.165:999 | MX | 580 | 24 | 67/72 |
| http://176.111.37.216:39811 | HK | 1051 | 23 | 132/160 |
| http://103.130.61.61:8081 | ID | 1663 | 22 | 130/160 |
| http://103.133.26.50:8080 | ID | 1246 | 20 | 39/61 |
| socks5://67.207.92.87:1088 | US | 623 | 15 | 101/159 |
| socks5://69.55.49.177:38182 | US | 578 | 15 | 15/15 |
| socks5://47.238.126.208:1080 | HK | 1367 | 10 | 36/65 |
| http://51.15.20.32:3129 | NL | 867 | 9 | 20/24 |
| http://34.43.46.91:443 | US | 793 | 9 | 149/160 |
| http://34.88.38.81:9443 | FI | 1077 | 8 | 87/125 |
| http://35.228.49.168:9443 | FI | 870 | 8 | 68/97 |
| http://154.59.56.72:999 | VE | 3525 | 8 | 87/119 |
| socks5://103.100.158.115:10809 | JP | 946 | 8 | 39/48 |
| http://101.251.204.174:8080 | CN | 2079 | 7 | 81/146 |
| http://167.172.76.176:9090 | SG | 897 | 7 | 84/121 |
| socks5://101.36.104.239:10808 | JP | 1917 | 7 | 136/160 |
| socks5://193.218.118.128:1080 | UA | 2403 | 7 | 13/16 |
| http://114.244.221.178:8888 | CN | 4215 | 6 | 41/83 |
| http://103.122.0.52:8181 | ID | 7651 | 6 | 22/72 |
| http://51.16.4.39:1461 | IL | 5564 | 6 | 36/144 |
| http://130.110.103.245:3128 | SA | 1520 | 6 | 142/160 |
| http://154.59.56.74:999 | VE | 3278 | 6 | 81/123 |
| socks5://49.13.22.249:10805 | DE | 3343 | 6 | 46/78 |
| socks5://45.61.129.165:9050 | US | 1678 | 6 | 120/160 |
| socks5://45.61.188.134:44499 | US | 1428 | 6 | 62/127 |
| socks5://193.25.215.182:22222 | US | 523 | 6 | 133/160 |
| http://118.179.213.183:81 | BD | 2411 | 5 | 27/146 |
| http://114.248.179.223:8888 | CN | 2289 | 5 | 54/128 |
| http://148.230.27.77:999 | GT | 4718 | 5 | 28/137 |
| http://157.66.192.114:8080 | ID | 3537 | 5 | 11/25 |
| http://160.22.207.95:8082 | ID | 7284 | 5 | 34/138 |
| http://51.85.44.162:31819 | IL | 3777 | 5 | 10/12 |
| http://82.152.138.127:999 | MX | 359 | 5 | 38/122 |
| http://185.238.236.226:58080 | PL | 2778 | 5 | 32/82 |
| http://167.99.74.174:9090 | SG | 886 | 5 | 79/120 |
| http://188.132.221.186:8080 | TR | 1443 | 5 | 21/98 |
| http://45.65.226.170:999 | ?? | 2052 | 5 | 7/11 |
| http://123.121.142.43:8888 | ?? | 2762 | 5 | 6/7 |
| socks5://45.149.92.160:1080 | HK | 1329 | 5 | 18/27 |
| socks5://45.74.31.47:5304 | NL | 4606 | 5 | 7/22 |
| http://45.65.226.174:999 | AR | 4341 | 4 | 11/21 |
| http://123.121.134.192:8888 | CN | 2010 | 4 | 11/26 |
| http://177.234.217.92:999 | EC | 2239 | 4 | 6/9 |
| http://18.175.170.244:51141 | GB | 4181 | 4 | 5/8 |
| http://103.146.38.89:3127 | ID | 2261 | 4 | 30/158 |
| http://103.158.210.80:8082 | ID | 5413 | 4 | 41/150 |
| http://103.172.42.161:1111 | ID | 3233 | 4 | 13/94 |
| http://103.208.103.30:8080 | ID | 1707 | 4 | 7/15 |
| http://51.17.99.135:42052 | IL | 1762 | 4 | 16/62 |
| http://128.199.254.13:9090 | SG | 1267 | 4 | 54/89 |
| http://156.200.116.67:8080 | ?? | 1327 | 4 | 5/6 |
| http://180.180.156.74:80 | ?? | 3624 | 4 | 4/4 |
| socks5://160.22.200.60:69 | ID | 4473 | 4 | 41/150 |
| socks5://124.248.177.44:1080 | KH | 1497 | 4 | 35/149 |
| socks5://45.74.31.41:10239 | NL | 2214 | 4 | 6/13 |
| socks5://45.74.31.41:10724 | NL | 3939 | 4 | 4/4 |
| socks5://45.74.31.41:4104 | NL | 4987 | 4 | 8/42 |
| socks5://45.74.31.41:6997 | NL | 2749 | 4 | 9/29 |
| socks5://45.74.31.42:10305 | NL | 2375 | 4 | 7/23 |
| socks5://45.74.31.46:6463 | NL | 4851 | 4 | 6/7 |
| socks5://45.74.31.46:7333 | NL | 7189 | 4 | 4/4 |
| socks5://45.74.31.46:7495 | NL | 7247 | 4 | 4/4 |
| socks5://45.74.31.46:7881 | NL | 2759 | 4 | 6/16 |
| socks5://45.74.31.46:8037 | NL | 5014 | 4 | 10/36 |
| socks5://45.74.31.46:8143 | NL | 1393 | 4 | 5/6 |
| socks5://45.74.31.47:5691 | NL | 2792 | 4 | 11/28 |
| socks5://45.74.31.47:6629 | NL | 5433 | 4 | 6/29 |
| socks5://45.74.31.47:8898 | NL | 2502 | 4 | 4/4 |
| socks5://45.74.31.47:8950 | NL | 2377 | 4 | 4/4 |
| socks5://88.201.248.85:1080 | RU | 1175 | 4 | 9/15 |
| socks5://149.248.18.106:1080 | US | 7730 | 4 | 14/26 |
| socks5://171.236.130.227:56967 | VN | 5056 | 4 | 9/16 |
| socks5://68.233.8.123:1080 | ?? | 905 | 4 | 5/7 |
| http://190.188.131.87:8080 | AR | 5536 | 3 | 16/74 |
| http://13.239.253.213:29050 | AU | 2484 | 3 | 14/72 |
| http://15.229.149.81:3128 | BR | 3303 | 3 | 40/70 |
| http://168.181.151.168:8081 | BR | 7034 | 3 | 31/152 |
| http://35.183.78.223:35766 | CA | 6267 | 3 | 3/3 |
| http://114.249.209.219:8888 | CN | 3935 | 3 | 42/118 |
| http://114.249.232.222:8888 | CN | 1533 | 3 | 47/125 |
| http://123.121.140.72:8888 | CN | 1359 | 3 | 10/12 |
| http://217.76.245.80:999 | DO | 628 | 3 | 29/116 |
| http://177.234.217.85:999 | EC | 4868 | 3 | 6/15 |
| http://177.234.217.235:999 | EC | 3892 | 3 | 61/129 |
| http://181.188.203.40:999 | EC | 3691 | 3 | 24/57 |
| http://41.33.60.42:8081 | EG | 3198 | 3 | 54/158 |
| http://15.232.45.244:4746 | ID | 6952 | 3 | 4/19 |
| http://38.103.250.205:8080 | ID | 6354 | 3 | 21/123 |
