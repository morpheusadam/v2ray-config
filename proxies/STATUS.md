# Proxy status

Generated 2026-09-28T20:15:11Z by `harvest.py`.

- **1735** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3537** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39675** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 157/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 1995 |
| http | 1537 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 1799 |
| ?? | 390 |
| ID | 280 |
| CN | 107 |
| US | 107 |
| IN | 49 |
| RU | 49 |
| CO | 46 |
| DE | 46 |
| MX | 46 |
| VE | 37 |
| PH | 34 |
| VN | 33 |
| BD | 31 |
| BR | 30 |
| PK | 29 |
| EC | 27 |
| FR | 25 |
| HK | 25 |
| JP | 24 |
| DO | 23 |
| SG | 23 |
| AR | 19 |
| EG | 18 |
| CA | 17 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 2 | 2 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 67 | 67 | 28 | 2026-09-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 74 | 74 | 30 | 2026-09-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 74 | 74 | 18 | 2026-09-28 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 120 | 120 | 45 | 2026-09-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-09-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 193 | 193 | 84 | 2026-09-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 201 | 201 | 66 | 2026-09-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 360 | 360 | 263 | 2026-09-28 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-09-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1151 | 2026-09-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1585 | 2026-09-28 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1864 | 1860 | 275 | 2026-09-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2698 | 2696 | 672 | 2026-09-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2738 | 2736 | 1960 | 2026-09-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2924 | 2922 | 548 | 2026-09-28 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 28004 | 28004 | 14742 | 2026-09-28 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 33990 | 33989 | 2206 | 2026-09-28 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1034 | 84 | 97/98 |
| http://190.97.236.128:999 | VE | 701 | 55 | 86/88 |
| http://190.97.236.129:999 | VE | 694 | 55 | 86/88 |
| http://95.3.69.222:8080 | TR | 1251 | 53 | 95/98 |
| http://38.51.207.104:8080 | VE | 592 | 31 | 38/39 |
| http://190.0.246.213:4040 | CO | 514 | 27 | 56/63 |
| http://213.111.146.36:18080 | NL | 529 | 27 | 30/35 |
| http://153.51.201.35:999 | VE | 744 | 25 | 25/25 |
| socks5://83.147.217.103:1080 | US | 510 | 21 | 21/21 |
| http://190.0.246.211:4040 | CO | 691 | 18 | 85/98 |
| http://167.172.76.176:9090 | SG | 1133 | 18 | 40/59 |
| http://154.59.56.76:999 | VE | 2097 | 16 | 47/58 |
| http://34.43.46.91:80 | US | 599 | 15 | 94/98 |
| http://190.0.246.210:4040 | CO | 683 | 14 | 86/97 |
| http://103.237.102.191:11111 | DE | 940 | 14 | 92/98 |
| http://154.59.56.73:999 | VE | 5174 | 14 | 57/70 |
| http://18.157.123.132:3128 | DE | 593 | 13 | 45/59 |
| http://107.167.18.122:443 | US | 312 | 13 | 48/50 |
| socks5://144.91.121.61:1088 | FR | 6068 | 12 | 84/98 |
| http://34.43.46.91:443 | US | 350 | 11 | 92/98 |
| http://123.121.132.32:8888 | CN | 2368 | 10 | 28/59 |
| http://189.51.168.165:999 | MX | 552 | 10 | 10/10 |
| http://149.130.173.58:9443 | CO | 475 | 9 | 9/9 |
| http://43.173.120.13:8899 | US | 674 | 9 | 9/9 |
| http://161.22.39.58:999 | VE | 740 | 9 | 9/9 |
| http://3.212.18.54:3128 | ?? | 233 | 8 | 8/8 |
| socks5://171.25.158.95:1080 | SE | 3054 | 8 | 9/13 |
| http://36.137.204.11:8002 | CN | 6365 | 7 | 10/14 |
| http://190.12.150.244:999 | EC | 2947 | 7 | 65/94 |
| http://154.59.56.78:999 | VE | 4649 | 7 | 35/54 |
| http://200.59.191.27:999 | VE | 2946 | 7 | 62/93 |
| http://185.195.71.218:18080 | CH | 981 | 6 | 26/35 |
| http://31.31.74.185:9898 | CZ | 2224 | 6 | 17/19 |
| http://103.119.19.218:3128 | CZ | 789 | 6 | 10/11 |
| http://186.5.94.206:999 | EC | 886 | 6 | 57/60 |
| http://37.59.125.131:8888 | FR | 900 | 6 | 77/98 |
| http://167.86.104.220:80 | FR | 632 | 6 | 17/34 |
| http://3.1.100.245:3128 | SG | 1127 | 6 | 7/10 |
| http://43.159.54.178:80 | SG | 1102 | 6 | 13/18 |
| http://107.150.41.226:18080 | US | 287 | 6 | 34/35 |
| http://172.236.242.244:3128 | ?? | 296 | 6 | 6/6 |
| socks5://5.75.133.113:10802 | DE | 2987 | 6 | 18/23 |
| socks5://65.21.252.66:10805 | FI | 3251 | 6 | 10/12 |
| http://119.188.131.55:17981 | CN | 2122 | 5 | 43/98 |
| http://45.86.245.81:8080 | ?? | 5841 | 5 | 5/5 |
| socks4://144.76.61.252:1080 | DE | 5893 | 5 | 8/11 |
| socks5://154.201.71.12:2080 | ?? | 5915 | 5 | 6/7 |
| http://45.232.0.2:8080 | AR | 5660 | 4 | 28/96 |
| http://113.45.195.147:3128 | CN | 3890 | 4 | 39/63 |
| http://114.249.230.202:8888 | CN | 2842 | 4 | 13/21 |
| http://114.254.48.23:8888 | CN | 1968 | 4 | 26/51 |
| http://120.232.115.57:17981 | CN | 1544 | 4 | 18/23 |
| http://123.121.210.208:8888 | CN | 6381 | 4 | 22/50 |
| http://38.211.76.203:999 | CO | 4629 | 4 | 7/16 |
| http://62.141.38.35:3128 | DE | 568 | 4 | 6/9 |
| http://176.111.37.5:39811 | HK | 978 | 4 | 88/98 |
| http://160.19.19.227:8080 | ID | 2858 | 4 | 13/75 |
| http://197.224.185.3:3128 | MU | 1973 | 4 | 60/66 |
| http://38.194.246.34:999 | MX | 4428 | 4 | 54/89 |
| http://128.199.254.13:9090 | SG | 1186 | 4 | 20/27 |
| http://129.226.89.151:80 | SG | 1083 | 4 | 28/45 |
| http://152.42.177.32:8888 | SG | 1075 | 4 | 35/58 |
| http://154.59.56.72:999 | VE | 1862 | 4 | 38/57 |
| socks5://121.169.46.116:1090 | KR | 3843 | 4 | 65/98 |
| socks5://103.88.234.239:40002 | MX | 1055 | 4 | 16/21 |
| socks5://101.32.60.93:1080 | ?? | 4942 | 4 | 5/6 |
| socks5://138.124.66.226:1080 | ?? | 3907 | 4 | 4/4 |
| socks5://174.138.189.26:2001 | ?? | 184 | 4 | 4/4 |
| http://184.75.221.82:3118 | CA | 217 | 3 | 55/63 |
| http://36.155.23.163:10808 | CN | 5450 | 3 | 22/35 |
| http://125.33.195.27:8888 | CN | 6962 | 3 | 21/44 |
| http://144.76.61.252:3128 | DE | 4006 | 3 | 9/11 |
| http://45.186.6.104:3128 | EC | 690 | 3 | 71/76 |
| http://102.164.252.150:8080 | GQ | 1743 | 3 | 20/57 |
| http://160.25.182.6:8080 | ID | 3478 | 3 | 22/96 |
| http://51.170.133.249:80 | MA | 4008 | 3 | 10/21 |
| http://205.164.192.115:999 | MX | 4358 | 3 | 62/96 |
| http://5.129.254.5:8888 | RU | 1105 | 3 | 45/53 |
| http://5.129.254.49:8888 | RU | 1094 | 3 | 46/53 |
| http://5.129.254.51:8888 | RU | 1096 | 3 | 46/53 |
| http://5.129.254.60:8888 | RU | 1065 | 3 | 45/52 |
| http://5.129.254.70:8888 | RU | 1067 | 3 | 46/53 |
| http://5.129.254.129:8888 | RU | 1037 | 3 | 51/59 |
| http://5.129.254.154:8888 | RU | 1036 | 3 | 42/49 |
| http://167.99.74.174:9090 | SG | 1081 | 3 | 36/58 |
| http://5.128.189.112:10809 | ?? | 3412 | 3 | 5/7 |
| http://24.52.147.103:5999 | ?? | 2181 | 3 | 5/6 |
| http://34.101.184.164:3128 | ?? | 1217 | 3 | 3/3 |
| http://41.128.90.52:1976 | ?? | 1102 | 3 | 3/3 |
| http://49.147.104.23:8082 | ?? | 5629 | 3 | 3/3 |
| http://177.234.221.198:999 | ?? | 3815 | 3 | 3/3 |
| socks5://5.75.133.113:10801 | DE | 2525 | 3 | 36/64 |
| socks5://5.75.133.113:10813 | DE | 2705 | 3 | 11/25 |
| socks5://49.13.22.249:10805 | DE | 2711 | 3 | 10/16 |
| socks5://45.74.31.23:12828 | NL | 7838 | 3 | 3/3 |
| socks5://45.74.31.25:4861 | NL | 6426 | 3 | 3/3 |
| socks5://45.74.31.25:5799 | NL | 5711 | 3 | 3/3 |
| socks5://45.74.31.25:6091 | NL | 2510 | 3 | 3/3 |
| socks5://45.74.31.30:36620 | NL | 6762 | 3 | 7/32 |
| socks5://45.74.31.41:13043 | NL | 3799 | 3 | 7/20 |
