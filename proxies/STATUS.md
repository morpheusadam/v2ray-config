# Proxy status

Generated 2026-11-08T18:41:03Z by `harvest.py`.

- **2973** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5899** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **36705** endpoints on record
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
| http | 3355 |
| socks5 | 2527 |
| socks4 | 17 |

| country | entries |
|---|---|
| NL | 2338 |
| ID | 1022 |
| ?? | 528 |
| CO | 155 |
| PH | 147 |
| US | 131 |
| MX | 112 |
| TH | 108 |
| TR | 94 |
| VE | 84 |
| BR | 76 |
| IN | 76 |
| BD | 68 |
| AR | 61 |
| DO | 58 |
| RU | 55 |
| CN | 54 |
| EC | 53 |
| PK | 38 |
| VN | 38 |
| EG | 36 |
| DE | 34 |
| JP | 34 |
| ZA | 33 |
| PE | 31 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-11-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 89 | 89 | 17 | 2026-11-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 100 | 100 | 12 | 2026-11-08 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 37 | 2026-11-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-11-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 175 | 175 | 104 | 2026-11-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 221 | 221 | 32 | 2026-11-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-08 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 444 | 444 | 199 | 2026-11-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-11-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1022 | 1022 | 178 | 2026-11-08 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1264 | 1264 | 76 | 2026-11-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1148 | 2026-11-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1581 | 2026-11-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2174 | 2174 | 665 | 2026-11-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2794 | 2794 | 1423 | 2026-11-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3920 | 3920 | 1100 | 2026-11-08 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5143 | 5143 | 3900 | 2026-11-08 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11782 | 11782 | 1924 | 2026-11-08 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 551 | 90 | 90/90 |
| http://103.133.26.73:3128 | ID | 1301 | 55 | 75/157 |
| http://176.111.37.5:39811 | HK | 1147 | 50 | 160/179 |
| http://34.43.46.91:80 | US | 498 | 49 | 173/179 |
| http://4.144.146.21:80 | SG | 997 | 47 | 64/71 |
| http://176.111.37.216:39811 | HK | 974 | 42 | 151/179 |
| http://34.43.46.91:443 | US | 424 | 28 | 168/179 |
| http://130.110.103.245:3128 | SA | 1400 | 25 | 161/179 |
| http://103.133.26.72:8080 | ID | 1319 | 22 | 59/105 |
| http://45.189.57.114:3129 | EC | 2179 | 21 | 21/21 |
| socks5://69.55.49.177:38182 | US | 1483 | 18 | 33/34 |
| http://190.123.83.137:999 | AR | 1812 | 16 | 16/16 |
| http://190.0.246.213:4040 | CO | 2392 | 16 | 134/144 |
| http://103.133.26.119:8080 | ID | 1719 | 15 | 58/89 |
| http://189.51.168.164:999 | MX | 1892 | 15 | 15/15 |
| http://49.229.100.235:8080 | TH | 1346 | 15 | 87/127 |
| http://171.100.254.137:8080 | TH | 2207 | 15 | 15/15 |
| http://43.161.254.16:3128 | HK | 2461 | 14 | 16/19 |
| http://103.130.61.61:8081 | ID | 1587 | 14 | 148/179 |
| http://184.75.221.82:3118 | CA | 441 | 13 | 126/144 |
| http://103.133.26.50:8080 | ID | 1426 | 13 | 53/80 |
| http://41.128.77.76:1981 | EG | 1246 | 11 | 62/133 |
| http://102.244.78.61:8086 | CM | 1521 | 10 | 55/67 |
| http://102.244.78.61:8089 | CM | 1356 | 10 | 54/67 |
| http://45.186.6.104:3128 | EC | 731 | 9 | 148/157 |
| http://38.180.18.103:3128 | BE | 789 | 8 | 8/8 |
| http://45.65.138.48:999 | CO | 3844 | 8 | 83/179 |
| http://45.65.224.74:999 | AR | 4736 | 7 | 36/44 |
| http://190.71.72.85:2525 | CO | 795 | 7 | 23/64 |
| http://103.130.61.60:8081 | ID | 1494 | 7 | 25/35 |
| http://128.199.113.85:9090 | SG | 1395 | 7 | 9/10 |
| http://201.190.178.191:8080 | AR | 1921 | 6 | 32/112 |
| http://102.244.78.61:8090 | CM | 1699 | 6 | 55/71 |
| http://34.105.252.3:3128 | GB | 830 | 6 | 38/61 |
| http://200.52.148.212:999 | HN | 5502 | 6 | 20/41 |
| http://1.10.133.83:8081 | TH | 6335 | 6 | 21/41 |
| http://18.224.94.46:18058 | US | 3509 | 6 | 16/25 |
| http://109.127.9.99:8080 | ?? | 3187 | 6 | 6/6 |
| socks5://45.74.31.42:7492 | NL | 5443 | 6 | 6/6 |
| http://179.1.213.233:999 | CO | 7650 | 5 | 7/11 |
| http://190.0.246.211:4040 | CO | 3723 | 5 | 164/179 |
| http://36.50.112.174:8070 | ID | 4229 | 5 | 21/77 |
| http://45.198.20.224:8080 | ID | 3093 | 5 | 21/97 |
| http://49.156.22.238:1080 | ID | 7885 | 5 | 6/7 |
| http://103.51.205.114:8082 | ID | 1344 | 5 | 36/115 |
| http://103.176.94.178:8080 | ID | 6231 | 5 | 18/32 |
| http://165.99.239.90:3125 | ID | 4742 | 5 | 22/101 |
| http://103.25.220.246:8086 | PH | 5963 | 5 | 22/80 |
| http://167.172.76.176:9090 | SG | 1015 | 5 | 100/140 |
| http://181.174.231.152:999 | ?? | 6823 | 5 | 5/5 |
| socks5://121.169.46.116:1090 | KR | 1539 | 5 | 125/179 |
| socks5://121.46.226.221:10808 | ?? | 2898 | 5 | 5/5 |
| http://221.221.159.97:8888 | CN | 1962 | 4 | 63/132 |
| http://45.172.223.190:999 | CO | 7208 | 4 | 5/10 |
| http://45.179.200.65:999 | CO | 7818 | 4 | 33/136 |
| http://131.221.40.131:4040 | CO | 4148 | 4 | 16/18 |
| http://177.234.217.46:999 | EC | 4747 | 4 | 45/126 |
| http://103.46.8.85:8080 | ID | 2928 | 4 | 29/79 |
| http://103.51.205.94:8080 | ID | 6952 | 4 | 7/16 |
| http://103.90.67.44:8087 | ID | 6890 | 4 | 18/79 |
| http://103.97.141.142:8080 | ID | 2475 | 4 | 9/15 |
| http://103.124.139.170:8080 | ID | 5534 | 4 | 17/79 |
| http://103.157.58.49:8080 | ID | 1359 | 4 | 34/178 |
| http://103.157.79.58:8080 | ID | 4924 | 4 | 18/93 |
| http://103.158.210.27:8090 | ID | 6623 | 4 | 16/79 |
| http://103.160.41.8:8080 | ID | 6552 | 4 | 31/144 |
| http://103.162.61.49:8080 | ID | 6786 | 4 | 12/53 |
| http://103.171.83.49:8080 | ID | 2192 | 4 | 18/76 |
| http://203.210.85.215:3128 | ID | 4612 | 4 | 9/11 |
| http://102.216.85.18:8080 | KE | 5948 | 4 | 31/142 |
| http://144.124.251.24:11180 | NL | 805 | 4 | 72/110 |
| http://126.209.13.13:8087 | PH | 5201 | 4 | 27/131 |
| http://180.191.143.157:8081 | PH | 3912 | 4 | 34/177 |
| http://82.213.29.53:19000 | PS | 2909 | 4 | 16/52 |
| http://154.59.56.76:999 | VE | 3603 | 4 | 100/139 |
| http://154.59.56.78:999 | VE | 2161 | 4 | 94/135 |
| http://190.97.227.9:999 | VE | 2616 | 4 | 7/10 |
| http://118.69.182.184:8082 | VN | 5879 | 4 | 6/7 |
| http://38.80.12.251:999 | ?? | 1445 | 4 | 4/4 |
| http://47.87.9.77:443 | ?? | 5006 | 4 | 5/6 |
| http://81.85.1.221:8081 | ?? | 1029 | 4 | 4/4 |
| http://200.126.94.179:999 | ?? | 3896 | 4 | 4/4 |
| socks5://5.75.133.113:10811 | DE | 2035 | 4 | 59/150 |
| socks5://91.107.179.68:10809 | DE | 1340 | 4 | 59/112 |
| socks5://45.74.31.42:7002 | NL | 2911 | 4 | 4/4 |
| socks5://45.74.31.42:7037 | NL | 6379 | 4 | 4/4 |
| socks5://45.74.31.42:7555 | NL | 5023 | 4 | 9/23 |
| socks5://45.74.31.42:8292 | NL | 3802 | 4 | 4/4 |
| http://181.209.109.173:3128 | AR | 3255 | 3 | 8/13 |
| http://114.130.153.122:58080 | BD | 7081 | 3 | 7/8 |
| http://15.229.149.81:1080 | BR | 3298 | 3 | 41/81 |
| http://123.121.140.72:8888 | CN | 5558 | 3 | 17/31 |
| http://45.167.126.43:999 | CO | 2777 | 3 | 8/29 |
| http://177.234.217.43:999 | EC | 3372 | 3 | 50/152 |
| http://177.234.217.44:999 | EC | 1577 | 3 | 26/79 |
| http://84.36.141.180:1981 | EG | 5660 | 3 | 30/130 |
| http://15.217.107.97:45779 | ES | 1893 | 3 | 22/89 |
| http://186.33.0.203:999 | GT | 7686 | 3 | 17/53 |
| http://103.97.140.17:8080 | ID | 6529 | 3 | 9/20 |
| http://103.109.173.170:80 | ID | 4580 | 3 | 19/65 |
