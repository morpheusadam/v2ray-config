# Proxy status

Generated 2026-10-19T23:04:18Z by `harvest.py`.

- **2920** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5111** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 245/600 (41%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3180 |
| socks5 | 1923 |
| socks4 | 8 |

| country | entries |
|---|---|
| NL | 1637 |
| ID | 943 |
| ?? | 265 |
| PH | 163 |
| CO | 152 |
| MX | 142 |
| RU | 130 |
| US | 113 |
| BR | 86 |
| VE | 83 |
| EC | 81 |
| TR | 79 |
| BD | 77 |
| CN | 72 |
| IN | 69 |
| DO | 63 |
| TH | 56 |
| AR | 52 |
| VN | 51 |
| DE | 47 |
| PK | 41 |
| CL | 38 |
| SG | 38 |
| PE | 33 |
| SY | 33 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-10-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 103 | 103 | 47 | 2026-10-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 56 | 2026-10-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 86 | 2026-10-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 184 | 184 | 59 | 2026-10-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 389 | 389 | 168 | 2026-10-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 439 | 439 | 128 | 2026-10-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-10-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 751 | 751 | 161 | 2026-10-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1072 | 1072 | 692 | 2026-10-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-10-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1733 | 1733 | 0 | 2026-10-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-10-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2333 | 2333 | 752 | 2026-10-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2923 | 2923 | 1024 | 2026-10-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3305 | 3305 | 2036 | 2026-10-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 71595 | 71595 | 58725 | 2026-10-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 79036 | 79035 | 2833 | 2026-10-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 962 | 60 | 127/140 |
| http://149.130.173.58:9443 | CO | 493 | 51 | 51/51 |
| http://190.0.246.213:4040 | CO | 653 | 34 | 97/105 |
| http://197.224.185.3:3128 | MU | 1925 | 32 | 101/108 |
| http://103.237.102.191:11111 | DE | 1103 | 27 | 133/140 |
| http://203.252.142.217:80 | KR | 802 | 22 | 22/22 |
| http://45.186.6.104:3128 | EC | 781 | 21 | 111/118 |
| http://3.211.120.181:443 | US | 310 | 20 | 34/51 |
| http://103.133.26.72:8080 | ID | 1715 | 16 | 21/66 |
| http://103.133.26.73:3128 | ID | 1684 | 16 | 36/118 |
| http://103.133.26.119:8080 | ID | 2874 | 16 | 20/50 |
| socks5://67.207.92.87:1088 | US | 795 | 16 | 84/139 |
| http://128.199.121.61:9090 | SG | 1140 | 12 | 50/60 |
| socks5://171.25.158.95:1080 | SE | 7735 | 12 | 47/55 |
| socks5://47.87.97.94:1080 | TH | 2662 | 12 | 15/16 |
| http://198.244.254.77:3128 | GB | 4650 | 11 | 22/24 |
| http://176.111.37.5:39811 | HK | 1083 | 11 | 121/140 |
| http://34.43.46.91:443 | US | 1172 | 11 | 131/140 |
| http://45.125.64.215:443 | HK | 938 | 10 | 10/10 |
| http://140.238.32.108:3128 | JP | 1027 | 10 | 73/139 |
| http://34.43.46.91:80 | US | 3167 | 10 | 134/140 |
| http://152.67.191.232:6800 | IN | 1163 | 9 | 9/9 |
| socks5://43.245.199.34:1080 | HK | 1128 | 9 | 9/9 |
| http://4.144.146.21:80 | SG | 968 | 8 | 25/32 |
| http://200.59.191.27:999 | VE | 2131 | 8 | 91/135 |
| socks5://113.22.224.63:1083 | VN | 5037 | 8 | 8/8 |
| http://190.0.246.210:4040 | CO | 840 | 7 | 126/139 |
| http://43.155.62.157:443 | HK | 868 | 7 | 35/43 |
| http://187.251.224.167:8081 | MX | 2123 | 7 | 28/100 |
| http://43.156.55.191:5001 | SG | 7294 | 7 | 7/7 |
| http://154.59.56.72:999 | VE | 1672 | 7 | 72/99 |
| socks5://148.251.68.232:8888 | DE | 1989 | 7 | 14/19 |
| http://187.102.219.32:999 | AR | 2112 | 6 | 45/139 |
| http://118.179.45.194:81 | BD | 4179 | 6 | 21/82 |
| http://102.244.78.61:8081 | CM | 1614 | 6 | 19/26 |
| http://102.244.78.61:8090 | CM | 1358 | 6 | 22/32 |
| http://45.65.137.218:999 | CO | 4850 | 6 | 38/105 |
| http://103.119.19.218:3128 | CZ | 1906 | 6 | 41/53 |
| http://161.49.90.70:1337 | PH | 2320 | 6 | 15/78 |
| http://44.216.83.206:3128 | US | 309 | 6 | 10/13 |
| socks5://121.46.226.221:10808 | CN | 1493 | 6 | 15/17 |
| socks5://213.199.47.140:1080 | FR | 999 | 6 | 83/106 |
| socks5://123.58.219.171:10808 | HK | 1411 | 6 | 110/140 |
| socks5://212.77.75.25:1088 | IT | 2025 | 6 | 34/40 |
| socks5://143.198.90.221:1088 | SG | 1161 | 6 | 7/8 |
| socks5://193.25.215.182:22222 | US | 744 | 6 | 118/140 |
| http://45.65.224.74:999 | AR | 3102 | 5 | 5/5 |
| http://187.102.219.34:999 | AR | 1211 | 5 | 49/91 |
| http://187.102.219.64:999 | AR | 1260 | 5 | 48/79 |
| http://123.121.209.108:8888 | CN | 1585 | 5 | 31/90 |
| http://186.96.111.214:999 | CO | 1739 | 5 | 56/129 |
| http://91.107.247.193:7001 | DE | 948 | 5 | 5/5 |
| http://179.60.189.81:999 | EC | 2062 | 5 | 8/12 |
| http://181.188.203.40:999 | EC | 3388 | 5 | 18/37 |
| http://186.5.94.206:999 | EC | 1075 | 5 | 93/102 |
| http://31.14.124.45:8080 | IR | 2540 | 5 | 20/103 |
| http://185.142.156.203:80 | IR | 1444 | 5 | 5/5 |
| http://49.156.44.115:8080 | KH | 1455 | 5 | 36/106 |
| http://205.164.192.115:999 | MX | 1235 | 5 | 90/138 |
| http://49.145.53.55:8080 | PH | 3442 | 5 | 5/5 |
| http://152.32.77.213:8095 | PH | 2270 | 5 | 5/5 |
| http://195.158.8.123:3128 | UZ | 2469 | 5 | 92/138 |
| http://38.51.207.119:999 | VE | 2860 | 5 | 31/137 |
| http://154.59.56.74:999 | VE | 2431 | 5 | 70/103 |
| http://190.97.229.118:999 | VE | 5539 | 5 | 72/130 |
| socks5://103.100.158.115:10809 | JP | 5418 | 5 | 20/28 |
| http://123.200.8.170:10000 | BD | 2023 | 4 | 53/138 |
| http://184.75.221.82:3118 | CA | 281 | 4 | 91/105 |
| http://38.7.195.49:999 | CL | 3126 | 4 | 51/114 |
| http://38.7.195.52:999 | CL | 4024 | 4 | 57/122 |
| http://38.7.195.55:999 | CL | 6076 | 4 | 49/114 |
| http://190.110.110.154:999 | CL | 3032 | 4 | 4/4 |
| http://102.244.78.61:8080 | CM | 1293 | 4 | 23/29 |
| http://119.188.131.55:17981 | CN | 2004 | 4 | 68/140 |
| http://123.119.25.143:8888 | CN | 5578 | 4 | 44/105 |
| http://8.243.73.66:8080 | CO | 3562 | 4 | 15/50 |
| http://45.179.200.65:999 | CO | 2700 | 4 | 18/97 |
| http://45.71.186.212:999 | EC | 2028 | 4 | 48/127 |
| http://45.71.186.214:999 | EC | 4188 | 4 | 35/86 |
| http://177.234.217.235:999 | EC | 6540 | 4 | 50/109 |
| http://177.234.217.236:999 | EC | 3054 | 4 | 42/113 |
| http://177.234.221.195:999 | EC | 2815 | 4 | 19/42 |
| http://45.240.232.62:8080 | EG | 1275 | 4 | 48/126 |
| http://213.131.85.28:1981 | EG | 1141 | 4 | 4/4 |
| http://176.57.189.138:3128 | FR | 1387 | 4 | 6/24 |
| http://213.136.72.147:3128 | FR | 985 | 4 | 4/4 |
| http://49.0.2.166:8080 | ID | 4691 | 4 | 6/23 |
| http://103.14.111.188:3128 | ID | 2362 | 4 | 6/10 |
| http://103.61.234.186:8180 | ID | 4863 | 4 | 57/137 |
| http://103.155.196.83:8082 | ID | 4350 | 4 | 19/53 |
| http://103.157.79.5:8080 | ID | 4665 | 4 | 19/73 |
| http://103.158.210.80:8082 | ID | 2477 | 4 | 34/130 |
| http://103.175.237.36:8080 | ID | 6152 | 4 | 23/116 |
| http://103.176.97.107:8082 | ID | 4837 | 4 | 10/76 |
| http://192.42.85.14:8080 | ID | 7926 | 4 | 5/6 |
| http://198.15.30.162:8080 | ID | 1332 | 4 | 11/53 |
| http://94.183.6.226:9090 | IR | 7466 | 4 | 9/60 |
| http://89.213.106.25:999 | MX | 5068 | 4 | 19/121 |
| http://189.51.168.165:999 | MX | 494 | 4 | 47/52 |
| http://206.135.72.8:999 | MX | 2747 | 4 | 4/4 |
