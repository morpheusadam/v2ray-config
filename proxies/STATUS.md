# Proxy status

Generated 2026-10-24T21:51:40Z by `harvest.py`.

- **1747** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5136** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39811** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 132/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2565 |
| http | 2557 |
| socks4 | 14 |

| country | entries |
|---|---|
| NL | 2352 |
| ID | 783 |
| ?? | 159 |
| PH | 143 |
| MX | 130 |
| CO | 122 |
| US | 112 |
| RU | 87 |
| VE | 76 |
| BD | 75 |
| BR | 61 |
| CN | 60 |
| TR | 59 |
| VN | 57 |
| IN | 52 |
| EC | 51 |
| TH | 44 |
| SG | 41 |
| AR | 40 |
| DO | 40 |
| PK | 40 |
| PE | 38 |
| DE | 35 |
| EG | 32 |
| SY | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 5 | 2026-10-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 102 | 102 | 44 | 2026-10-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 148 | 148 | 60 | 2026-10-24 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 82 | 2026-10-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 195 | 195 | 59 | 2026-10-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 264 | 264 | 65 | 2026-10-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 384 | 384 | 159 | 2026-10-24 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-24 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 448 | 448 | 17 | 2026-10-24 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-24 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-24 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 985 | 985 | 468 | 2026-10-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1137 | 2026-10-24 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1698 | 1694 | 129 | 2026-10-24 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-10-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2412 | 2410 | 785 | 2026-10-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2802 | 2800 | 1900 | 2026-10-24 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3764 | 3762 | 1440 | 2026-10-24 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 77989 | 77989 | 63108 | 2026-10-24 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 84831 | 84830 | 2261 | 2026-10-24 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1372 | 70 | 137/150 |
| http://149.130.173.58:9443 | CO | 565 | 61 | 61/61 |
| http://190.0.246.213:4040 | CO | 605 | 44 | 107/115 |
| http://197.224.185.3:3128 | MU | 2041 | 42 | 111/118 |
| http://103.237.102.191:11111 | DE | 1312 | 37 | 143/150 |
| http://203.252.142.217:80 | KR | 1055 | 32 | 32/32 |
| http://45.186.6.104:3128 | EC | 725 | 31 | 121/128 |
| http://103.133.26.72:8080 | ID | 1448 | 26 | 31/76 |
| http://103.133.26.73:3128 | ID | 1394 | 26 | 46/128 |
| http://103.133.26.119:8080 | ID | 1589 | 26 | 30/60 |
| http://176.111.37.5:39811 | HK | 1242 | 21 | 131/150 |
| http://34.43.46.91:80 | US | 1264 | 20 | 144/150 |
| socks5://43.245.199.34:1080 | HK | 1771 | 19 | 19/19 |
| http://4.144.146.21:80 | SG | 1916 | 18 | 35/42 |
| http://190.0.246.210:4040 | CO | 1309 | 17 | 136/149 |
| http://43.155.62.157:443 | HK | 2063 | 17 | 45/53 |
| http://102.244.78.61:8081 | CM | 2094 | 16 | 29/36 |
| http://186.5.94.206:999 | EC | 1047 | 15 | 103/112 |
| http://205.164.192.115:999 | MX | 2344 | 15 | 100/148 |
| socks5://103.100.158.115:10809 | JP | 955 | 15 | 30/38 |
| http://184.75.221.82:3118 | CA | 540 | 14 | 101/115 |
| http://189.51.168.165:999 | MX | 480 | 14 | 57/62 |
| http://130.110.103.245:3128 | SA | 1826 | 14 | 134/150 |
| http://176.111.37.216:39811 | HK | 1258 | 13 | 122/150 |
| http://103.130.61.61:8081 | ID | 1549 | 12 | 120/150 |
| http://185.191.239.248:3128 | CH | 2789 | 10 | 106/149 |
| http://103.133.26.50:8080 | ID | 1469 | 10 | 29/51 |
| http://45.125.64.215:443 | HK | 7535 | 9 | 19/20 |
| http://34.43.46.91:443 | US | 1480 | 9 | 140/150 |
| socks5://101.36.104.239:10808 | JP | 2260 | 9 | 127/150 |
| socks5://143.198.90.221:1088 | SG | 4543 | 9 | 16/18 |
| http://200.59.191.27:999 | VE | 7856 | 8 | 99/145 |
| socks5://121.169.46.116:1090 | KR | 7179 | 8 | 103/150 |
| http://45.65.138.48:999 | CO | 4446 | 7 | 62/150 |
| http://82.152.138.127:999 | MX | 2489 | 7 | 31/112 |
| http://88.210.37.30:3128 | US | 262 | 7 | 7/7 |
| socks5://123.58.219.171:10808 | HK | 1626 | 7 | 119/150 |
| socks5://171.25.158.95:1080 | SE | 2921 | 7 | 56/65 |
| socks5://129.146.121.2:10808 | US | 4188 | 7 | 7/7 |
| socks5://209.50.255.91:1080 | US | 1003 | 7 | 35/67 |
| http://38.57.65.195:999 | DO | 7633 | 6 | 12/35 |
| http://181.78.195.136:999 | EC | 6704 | 6 | 6/6 |
| http://198.244.254.77:3128 | GB | 3560 | 6 | 31/34 |
| http://103.130.61.60:8081 | ID | 1939 | 6 | 6/6 |
| http://168.144.121.183:3129 | IN | 1610 | 6 | 47/101 |
| http://162.214.159.94:3128 | US | 1268 | 6 | 6/6 |
| socks5://213.199.47.140:1080 | FR | 1723 | 6 | 91/116 |
| http://123.121.132.234:8888 | CN | 2676 | 5 | 9/11 |
| http://8.215.25.3:2080 | ID | 1673 | 5 | 41/150 |
| http://8.215.25.3:2081 | ID | 1593 | 5 | 37/148 |
| http://41.216.191.154:8080 | ID | 2799 | 5 | 5/5 |
| http://51.17.99.116:40013 | IL | 2629 | 5 | 15/38 |
| http://45.177.178.23:999 | MX | 4889 | 5 | 5/5 |
| http://51.15.20.32:3129 | NL | 1610 | 5 | 11/14 |
| http://146.190.80.158:9090 | SG | 1096 | 5 | 54/76 |
| socks4://103.71.23.31:1080 | FI | 5095 | 5 | 5/5 |
| socks5://103.178.121.234:1080 | PK | 6103 | 5 | 9/30 |
| socks5://67.207.92.87:1088 | US | 1109 | 5 | 91/149 |
| socks5://69.55.49.177:38182 | US | 1001 | 5 | 5/5 |
| http://186.211.194.21:8080 | BR | 6506 | 4 | 6/7 |
| http://221.221.162.6:8888 | CN | 2320 | 4 | 25/48 |
| http://89.58.42.118:3129 | DE | 1916 | 4 | 16/39 |
| http://177.234.211.151:999 | EC | 4041 | 4 | 24/140 |
| http://41.33.60.42:8081 | EG | 2580 | 4 | 50/148 |
| http://18.175.170.244:23666 | GB | 2945 | 4 | 21/62 |
| http://102.164.252.150:8080 | GQ | 5014 | 4 | 41/109 |
| http://18.166.56.240:39593 | HK | 3975 | 4 | 23/72 |
| http://103.68.215.46:8080 | ID | 3908 | 4 | 16/102 |
| http://103.156.17.83:8818 | ID | 6774 | 4 | 11/62 |
| http://103.172.71.5:9191 | ID | 2560 | 4 | 12/50 |
| http://187.251.224.167:8081 | MX | 4115 | 4 | 33/110 |
| http://5.129.254.5:8888 | RU | 1371 | 4 | 89/105 |
| http://5.129.254.49:8888 | RU | 1317 | 4 | 90/105 |
| http://5.129.254.51:8888 | RU | 1301 | 4 | 90/105 |
| http://5.129.254.60:8888 | RU | 1440 | 4 | 89/104 |
| http://5.129.254.70:8888 | RU | 1358 | 4 | 90/105 |
| http://5.129.254.129:8888 | RU | 1272 | 4 | 95/111 |
| http://5.129.254.154:8888 | RU | 1294 | 4 | 86/101 |
| http://5.129.254.215:8888 | RU | 2588 | 4 | 39/47 |
| http://5.129.254.243:8888 | RU | 1677 | 4 | 39/46 |
| http://147.45.164.178:8888 | RU | 2002 | 4 | 19/24 |
| http://43.156.66.78:12345 | SG | 3718 | 4 | 10/25 |
| http://1.20.178.208:80 | TH | 6608 | 4 | 8/38 |
| http://64.118.155.2:22222 | US | 2079 | 4 | 4/4 |
| http://195.158.8.123:3128 | UZ | 2602 | 4 | 99/148 |
| http://38.41.0.116:999 | VE | 4701 | 4 | 14/52 |
| http://38.51.220.64:999 | VE | 2819 | 4 | 25/127 |
| socks5://31.58.144.19:1080 | DE | 962 | 4 | 9/11 |
| socks5://101.36.104.46:10808 | JP | 3057 | 4 | 129/150 |
| socks5://5.255.103.55:1080 | NL | 1864 | 4 | 19/45 |
| socks5://178.252.74.29:1081 | RU | 3457 | 4 | 17/23 |
| socks5://45.61.129.165:9050 | US | 1784 | 4 | 113/150 |
| socks5://193.25.215.182:22222 | US | 596 | 4 | 126/150 |
| http://16.26.208.68:18596 | AU | 4098 | 3 | 38/115 |
| http://103.135.139.89:8080 | BD | 2835 | 3 | 13/60 |
| http://15.229.149.81:3128 | BR | 6466 | 3 | 31/60 |
| http://45.228.89.114:8666 | BR | 6911 | 3 | 8/23 |
| http://16.18.22.211:9090 | CH | 1646 | 3 | 31/110 |
| http://119.188.131.55:17981 | CN | 2318 | 3 | 76/150 |
| http://123.115.226.82:8888 | CN | 1320 | 3 | 35/96 |
