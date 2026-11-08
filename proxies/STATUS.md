# Proxy status

Generated 2026-11-08T23:07:28Z by `harvest.py`.

- **2923** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **37007** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 126/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3774 |
| socks5 | 2212 |
| socks4 | 14 |

| country | entries |
|---|---|
| NL | 2063 |
| ID | 1111 |
| ?? | 603 |
| CO | 167 |
| PH | 167 |
| TH | 126 |
| MX | 117 |
| US | 116 |
| TR | 101 |
| IN | 97 |
| VE | 94 |
| BR | 88 |
| BD | 76 |
| DO | 68 |
| RU | 64 |
| CN | 62 |
| EC | 58 |
| AR | 57 |
| PK | 47 |
| DE | 39 |
| VN | 39 |
| JP | 36 |
| PE | 36 |
| ZA | 35 |
| EG | 34 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-11-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 85 | 85 | 17 | 2026-11-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 93 | 93 | 19 | 2026-11-08 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 34 | 2026-11-08 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 57 | 2026-11-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 178 | 178 | 94 | 2026-11-08 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 191 | 191 | 35 | 2026-11-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 341 | 341 | 234 | 2026-11-08 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-08 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-08 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 443 | 2026-11-08 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1261 | 1261 | 218 | 2026-11-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1143 | 2026-11-08 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1651 | 1651 | 244 | 2026-11-08 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1583 | 2026-11-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1843 | 1843 | 654 | 2026-11-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2333 | 2333 | 1243 | 2026-11-08 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3873 | 3873 | 1467 | 2026-11-08 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5147 | 5147 | 3921 | 2026-11-08 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12045 | 12045 | 1949 | 2026-11-08 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 481 | 91 | 91/91 |
| http://103.133.26.73:3128 | ID | 1492 | 56 | 76/158 |
| http://176.111.37.5:39811 | HK | 1060 | 51 | 161/180 |
| http://34.43.46.91:80 | US | 580 | 50 | 174/180 |
| http://4.144.146.21:80 | SG | 1031 | 48 | 65/72 |
| http://176.111.37.216:39811 | HK | 949 | 43 | 152/180 |
| http://34.43.46.91:443 | US | 536 | 29 | 169/180 |
| http://130.110.103.245:3128 | SA | 1102 | 26 | 162/180 |
| http://103.133.26.72:8080 | ID | 1409 | 23 | 60/106 |
| http://45.189.57.114:3129 | EC | 787 | 22 | 22/22 |
| http://190.123.83.137:999 | AR | 3237 | 17 | 17/17 |
| http://190.0.246.213:4040 | CO | 619 | 17 | 135/145 |
| http://103.133.26.119:8080 | ID | 1739 | 16 | 59/90 |
| http://189.51.168.164:999 | MX | 1250 | 16 | 16/16 |
| http://49.229.100.235:8080 | TH | 1469 | 16 | 88/128 |
| http://171.100.254.137:8080 | TH | 1426 | 16 | 16/16 |
| http://43.161.254.16:3128 | HK | 933 | 15 | 17/20 |
| http://103.130.61.61:8081 | ID | 2413 | 15 | 149/180 |
| http://184.75.221.82:3118 | CA | 259 | 14 | 127/145 |
| http://103.133.26.50:8080 | ID | 1437 | 14 | 54/81 |
| http://41.128.77.76:1981 | EG | 1084 | 12 | 63/134 |
| http://102.244.78.61:8089 | CM | 1318 | 11 | 55/68 |
| http://45.186.6.104:3128 | EC | 890 | 10 | 149/158 |
| http://38.180.18.103:3128 | BE | 654 | 9 | 9/9 |
| http://45.65.224.74:999 | AR | 1015 | 8 | 37/45 |
| http://190.71.72.85:2525 | CO | 735 | 8 | 24/65 |
| http://103.130.61.60:8081 | ID | 1433 | 8 | 26/36 |
| http://128.199.113.85:9090 | SG | 1034 | 8 | 10/11 |
| http://102.244.78.61:8090 | CM | 1322 | 7 | 56/72 |
| http://34.105.252.3:3128 | GB | 619 | 7 | 39/62 |
| http://109.127.9.99:8080 | ?? | 4574 | 7 | 7/7 |
| socks5://45.74.31.42:7492 | NL | 4178 | 7 | 7/7 |
| http://190.0.246.211:4040 | CO | 897 | 6 | 165/180 |
| http://36.50.112.174:8070 | ID | 5860 | 6 | 22/78 |
| http://45.198.20.224:8080 | ID | 2410 | 6 | 22/98 |
| http://49.156.22.238:1080 | ID | 3581 | 6 | 7/8 |
| http://103.176.94.178:8080 | ID | 4436 | 6 | 19/33 |
| http://103.25.220.246:8086 | PH | 3304 | 6 | 23/81 |
| http://167.172.76.176:9090 | SG | 1049 | 6 | 101/141 |
| socks5://121.46.226.221:10808 | ?? | 1545 | 6 | 6/6 |
| http://131.221.40.131:4040 | CO | 599 | 5 | 17/19 |
| http://103.97.141.142:8080 | ID | 3896 | 5 | 10/16 |
| http://103.158.210.27:8090 | ID | 3583 | 5 | 17/80 |
| http://144.124.251.24:11180 | NL | 698 | 5 | 73/111 |
| http://180.191.143.157:8081 | PH | 4357 | 5 | 35/178 |
| http://154.59.56.76:999 | VE | 2655 | 5 | 101/140 |
| http://154.59.56.78:999 | VE | 7451 | 5 | 95/136 |
| http://190.97.227.9:999 | VE | 2085 | 5 | 8/11 |
| http://118.69.182.184:8082 | VN | 2543 | 5 | 7/8 |
| http://38.80.12.251:999 | ?? | 3327 | 5 | 5/5 |
| http://47.87.9.77:443 | ?? | 6053 | 5 | 6/7 |
| http://81.85.1.221:8081 | ?? | 571 | 5 | 5/5 |
| http://200.126.94.179:999 | ?? | 3633 | 5 | 5/5 |
| http://114.130.153.122:58080 | BD | 2639 | 4 | 8/9 |
| http://15.229.149.81:1080 | BR | 2137 | 4 | 42/82 |
| http://123.121.140.72:8888 | CN | 1665 | 4 | 18/32 |
| http://45.167.126.43:999 | CO | 850 | 4 | 9/30 |
| http://177.234.217.44:999 | EC | 5081 | 4 | 27/80 |
| http://84.36.141.180:1981 | EG | 7279 | 4 | 31/131 |
| http://103.97.140.17:8080 | ID | 1517 | 4 | 10/21 |
| http://103.109.173.170:80 | ID | 3291 | 4 | 20/66 |
| http://103.122.64.156:8080 | ID | 4458 | 4 | 26/122 |
| http://103.131.19.51:8080 | ID | 6627 | 4 | 26/80 |
| http://103.147.77.212:8080 | ID | 3562 | 4 | 8/22 |
| http://103.171.255.60:8080 | ID | 1429 | 4 | 21/77 |
| http://103.176.96.225:8082 | ID | 6571 | 4 | 42/125 |
| http://103.231.236.133:8182 | ID | 7977 | 4 | 27/126 |
| http://160.191.173.52:8080 | ID | 4590 | 4 | 21/100 |
| http://202.58.77.73:800 | ID | 3480 | 4 | 15/54 |
| http://51.85.44.162:31819 | IL | 2722 | 4 | 18/32 |
| http://49.156.44.116:8080 | KH | 2753 | 4 | 6/14 |
| http://148.244.84.34:3128 | MX | 5041 | 4 | 9/20 |
| http://144.124.251.24:11266 | NL | 757 | 4 | 71/112 |
| http://49.149.24.144:8082 | PH | 1425 | 4 | 11/19 |
| http://180.195.99.168:8081 | PH | 2325 | 4 | 22/111 |
| http://185.238.238.165:58080 | PL | 3255 | 4 | 37/70 |
| http://45.177.16.131:999 | PY | 1331 | 4 | 40/176 |
| http://56.228.13.15:56343 | SE | 2480 | 4 | 27/78 |
| http://104.248.151.93:9090 | SG | 1039 | 4 | 59/81 |
| http://1.10.248.236:80 | TH | 5046 | 4 | 10/19 |
| http://1.20.178.212:80 | TH | 2920 | 4 | 19/44 |
| http://171.101.72.82:8080 | TH | 1468 | 4 | 15/33 |
| http://18.224.94.46:42663 | US | 1180 | 4 | 14/24 |
| http://69.87.216.54:7989 | US | 246 | 4 | 64/125 |
| http://172.239.170.24:3128 | US | 1593 | 4 | 9/14 |
| http://90.156.160.234:3128 | UZ | 1520 | 4 | 27/68 |
| http://154.59.56.73:999 | VE | 2757 | 4 | 109/152 |
| http://161.22.39.99:999 | VE | 3763 | 4 | 14/41 |
| http://20.196.34.172:3128 | ?? | 1180 | 4 | 4/4 |
| http://79.127.223.56:20856 | ?? | 2552 | 4 | 4/4 |
| http://123.121.123.216:8888 | ?? | 1347 | 4 | 4/4 |
| http://152.0.60.100:999 | ?? | 3575 | 4 | 4/4 |
| http://181.78.205.45:999 | ?? | 2553 | 4 | 4/4 |
| http://190.115.15.100:8080 | ?? | 566 | 4 | 4/4 |
| http://221.221.148.144:8888 | ?? | 1468 | 4 | 4/4 |
| socks5://45.194.33.12:30001 | HK | 1407 | 4 | 15/56 |
| socks5://45.194.33.12:30002 | HK | 2533 | 4 | 10/24 |
| socks5://195.13.182.211:8080 | LV | 1638 | 4 | 9/12 |
| socks5://45.74.31.46:4706 | NL | 7919 | 4 | 12/65 |
| socks5://45.74.31.47:21525 | NL | 4793 | 4 | 6/11 |
