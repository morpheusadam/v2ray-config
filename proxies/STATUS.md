# Proxy status

Generated 2026-11-10T02:22:42Z by `harvest.py`.

- **1831** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4890** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35978** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 106/600 (18%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3237 |
| socks5 | 1636 |
| socks4 | 17 |

| country | entries |
|---|---|
| NL | 1405 |
| ID | 933 |
| ?? | 628 |
| PH | 152 |
| CO | 128 |
| US | 124 |
| MX | 113 |
| TH | 96 |
| BR | 81 |
| TR | 77 |
| CN | 75 |
| VE | 74 |
| IN | 67 |
| RU | 64 |
| BD | 63 |
| AR | 57 |
| DO | 55 |
| EC | 48 |
| PK | 43 |
| VN | 37 |
| EG | 33 |
| PE | 30 |
| SG | 28 |
| ZA | 28 |
| CL | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-11-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-11-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 111 | 111 | 21 | 2026-11-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 139 | 139 | 12 | 2026-11-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 145 | 145 | 30 | 2026-11-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-11-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 301 | 301 | 63 | 2026-11-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 347 | 347 | 128 | 2026-11-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 361 | 361 | 242 | 2026-11-10 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 427 | 427 | 62 | 2026-11-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-11-10 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1403 | 1403 | 91 | 2026-11-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-11-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2232 | 2232 | 689 | 2026-11-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2330 | 2330 | 1357 | 2026-11-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2785 | 2785 | 639 | 2026-11-10 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5163 | 5163 | 3922 | 2026-11-10 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10817 | 10817 | 1952 | 2026-11-10 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1219 | 58 | 78/160 |
| http://176.111.37.5:39811 | HK | 1397 | 53 | 163/182 |
| http://34.43.46.91:80 | US | 495 | 52 | 176/182 |
| http://4.144.146.21:80 | SG | 859 | 50 | 67/74 |
| http://176.111.37.216:39811 | HK | 1916 | 45 | 154/182 |
| http://34.43.46.91:443 | US | 562 | 31 | 171/182 |
| http://130.110.103.245:3128 | SA | 1297 | 28 | 164/182 |
| http://103.133.26.72:8080 | ID | 1170 | 25 | 62/108 |
| http://45.189.57.114:3129 | EC | 1203 | 24 | 24/24 |
| http://190.123.83.137:999 | AR | 2996 | 19 | 19/19 |
| http://190.0.246.213:4040 | CO | 2720 | 19 | 137/147 |
| http://103.133.26.119:8080 | ID | 1545 | 18 | 61/92 |
| http://189.51.168.164:999 | MX | 4592 | 18 | 18/18 |
| http://49.229.100.235:8080 | TH | 1199 | 18 | 90/130 |
| http://171.100.254.137:8080 | TH | 1214 | 18 | 18/18 |
| http://43.161.254.16:3128 | HK | 1515 | 17 | 19/22 |
| http://103.130.61.61:8081 | ID | 3045 | 17 | 151/182 |
| http://184.75.221.82:3118 | CA | 385 | 16 | 129/147 |
| http://103.133.26.50:8080 | ID | 1228 | 16 | 56/83 |
| http://102.244.78.61:8089 | CM | 1466 | 13 | 57/70 |
| http://45.186.6.104:3128 | EC | 996 | 12 | 151/160 |
| http://38.180.18.103:3128 | BE | 760 | 11 | 11/11 |
| http://190.71.72.85:2525 | CO | 804 | 10 | 26/67 |
| http://103.130.61.60:8081 | ID | 1469 | 10 | 28/38 |
| http://102.244.78.61:8090 | CM | 1465 | 9 | 58/74 |
| http://167.172.76.176:9090 | SG | 867 | 8 | 103/143 |
| socks5://121.46.226.221:10808 | ?? | 1568 | 8 | 8/8 |
| http://131.221.40.131:4040 | CO | 3451 | 7 | 19/21 |
| http://177.234.217.44:999 | EC | 3972 | 6 | 29/82 |
| http://84.36.141.180:1981 | EG | 6032 | 6 | 33/133 |
| http://49.149.24.144:8082 | PH | 1855 | 6 | 13/21 |
| http://104.248.151.93:9090 | SG | 855 | 6 | 61/83 |
| http://1.20.178.212:80 | TH | 3754 | 6 | 21/46 |
| http://69.87.216.54:7989 | US | 153 | 6 | 66/127 |
| http://172.239.170.24:3128 | US | 90 | 6 | 11/16 |
| http://90.156.160.234:3128 | UZ | 6393 | 6 | 29/70 |
| http://190.115.15.100:8080 | ?? | 4082 | 6 | 6/6 |
| socks5://45.194.33.12:30002 | HK | 4687 | 6 | 12/26 |
| socks5://193.25.215.182:22222 | US | 2356 | 6 | 154/182 |
| http://45.65.224.125:999 | AR | 1195 | 5 | 32/44 |
| http://102.244.78.61:8083 | CM | 1422 | 5 | 56/70 |
| http://102.244.78.61:8084 | CM | 1418 | 5 | 56/70 |
| http://102.244.78.61:8088 | CM | 1445 | 5 | 55/70 |
| http://123.121.108.22:8888 | CN | 1222 | 5 | 23/33 |
| http://123.121.132.234:8888 | CN | 1465 | 5 | 29/43 |
| http://103.237.102.191:11111 | DE | 882 | 5 | 173/182 |
| http://43.155.62.157:443 | HK | 1064 | 5 | 72/85 |
| http://160.25.155.85:8080 | ID | 5548 | 5 | 11/28 |
| http://160.19.41.37:80 | IN | 3985 | 5 | 24/58 |
| http://38.194.246.34:999 | MX | 5300 | 5 | 102/173 |
| http://82.152.138.127:999 | MX | 4948 | 5 | 57/144 |
| http://189.51.168.165:999 | MX | 2646 | 5 | 87/94 |
| http://144.124.251.24:10216 | NL | 903 | 5 | 78/131 |
| http://144.124.251.24:10811 | NL | 969 | 5 | 69/114 |
| http://165.154.162.73:8888 | US | 1509 | 5 | 124/182 |
| http://41.196.16.226:1976 | ?? | 1275 | 5 | 5/5 |
| http://204.199.106.226:999 | ?? | 2868 | 5 | 5/5 |
| socks5://5.255.113.177:1080 | NL | 2982 | 5 | 31/80 |
| http://3.26.199.107:1234 | AU | 2579 | 4 | 26/95 |
| http://182.252.89.134:8080 | BD | 6817 | 4 | 15/41 |
| http://15.223.187.219:55865 | CA | 1518 | 4 | 36/96 |
| http://102.244.78.61:8080 | CM | 1435 | 4 | 59/71 |
| http://102.244.78.61:8082 | CM | 1406 | 4 | 59/71 |
| http://102.244.78.61:8085 | CM | 1452 | 4 | 57/72 |
| http://123.119.24.241:8888 | CN | 2810 | 4 | 44/117 |
| http://221.221.144.98:8888 | CN | 7971 | 4 | 15/39 |
| http://45.65.137.218:999 | CO | 1885 | 4 | 67/147 |
| http://190.0.246.210:4040 | CO | 5188 | 4 | 166/181 |
| http://181.78.195.136:999 | EC | 3135 | 4 | 25/38 |
| http://45.245.208.180:8080 | EG | 1329 | 4 | 37/55 |
| http://51.94.221.175:1857 | ES | 2993 | 4 | 32/123 |
| http://15.232.45.244:3127 | ID | 3606 | 4 | 37/142 |
| http://103.147.134.179:8080 | ID | 6687 | 4 | 16/44 |
| http://103.189.223.19:7557 | ID | 5091 | 4 | 6/11 |
| http://117.18.21.53:8081 | ID | 4497 | 4 | 10/24 |
| http://157.66.192.114:8080 | ID | 7670 | 4 | 17/47 |
| http://202.58.77.131:7777 | ID | 5326 | 4 | 12/22 |
| http://206.135.53.53:999 | MX | 699 | 4 | 11/23 |
| http://144.124.251.24:10771 | NL | 842 | 4 | 71/114 |
| http://45.177.16.133:999 | PY | 6744 | 4 | 20/76 |
| http://128.199.254.13:9090 | SG | 881 | 4 | 68/111 |
| http://3.21.129.156:2085 | US | 1148 | 4 | 26/66 |
| http://209.255.132.243:8080 | US | 6293 | 4 | 6/10 |
| http://195.158.8.123:3128 | UZ | 2951 | 4 | 119/180 |
| http://13.245.183.150:8182 | ZA | 2302 | 4 | 41/150 |
| http://54.36.150.233:3128 | ?? | 914 | 4 | 4/4 |
| http://114.249.226.92:8888 | ?? | 1801 | 4 | 4/4 |
| http://123.121.99.174:8888 | ?? | 2230 | 4 | 4/4 |
| http://152.53.81.29:8888 | ?? | 3777 | 4 | 4/4 |
| http://152.53.120.85:8080 | ?? | 5566 | 4 | 4/4 |
| http://188.128.254.4:3128 | ?? | 1035 | 4 | 4/4 |
| http://194.31.107.138:3128 | ?? | 7944 | 4 | 5/8 |
| http://206.135.80.74:999 | ?? | 2683 | 4 | 4/4 |
| http://206.135.80.194:999 | ?? | 4323 | 4 | 4/4 |
| socks5://101.36.104.46:10808 | JP | 1875 | 4 | 155/182 |
| socks5://143.198.239.45:10020 | US | 2619 | 4 | 4/4 |
| socks5://31.41.228.112:2080 | ?? | 5587 | 4 | 4/4 |
| http://38.226.251.67:999 | AR | 1584 | 3 | 29/180 |
| http://45.232.0.2:8080 | AR | 1565 | 3 | 57/180 |
| http://181.114.225.224:8080 | AR | 5860 | 3 | 6/29 |
