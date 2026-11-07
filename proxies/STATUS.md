# Proxy status

Generated 2026-11-06T23:48:23Z by `harvest.py`.

- **4338** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39842** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 222/600 (37%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3682 |
| socks5 | 2311 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 2214 |
| ID | 1128 |
| ?? | 392 |
| PH | 179 |
| CO | 161 |
| US | 128 |
| TH | 123 |
| TR | 123 |
| MX | 119 |
| VE | 96 |
| BR | 81 |
| BD | 74 |
| IN | 73 |
| EC | 71 |
| AR | 66 |
| CN | 66 |
| DO | 55 |
| RU | 50 |
| EG | 47 |
| PE | 43 |
| VN | 42 |
| ZA | 40 |
| PK | 38 |
| SG | 37 |
| CH | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 46 | 46 | 14 | 2026-11-06 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 39 | 2026-11-06 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 75 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 320 | 320 | 223 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 345 | 345 | 48 | 2026-11-06 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-06 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-06 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 444 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 1084 | 1084 | 414 | 2026-11-06 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1109 | 1109 | 210 | 2026-11-06 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1442 | 1442 | 97 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1106 | 2026-11-06 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1582 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2009 | 2009 | 652 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2629 | 2629 | 1337 | 2026-11-06 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4055 | 4055 | 1158 | 2026-11-06 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5028 | 5028 | 3824 | 2026-11-06 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 8995 | 8995 | 3718 | 2026-11-06 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11339 | 11339 | 1901 | 2026-11-06 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 586 | 87 | 87/87 |
| http://103.133.26.73:3128 | ID | 1305 | 52 | 72/154 |
| http://176.111.37.5:39811 | HK | 973 | 47 | 157/176 |
| http://34.43.46.91:80 | US | 1187 | 46 | 170/176 |
| http://4.144.146.21:80 | SG | 933 | 44 | 61/68 |
| http://176.111.37.216:39811 | HK | 1079 | 39 | 148/176 |
| http://34.43.46.91:443 | US | 2605 | 25 | 165/176 |
| socks5://101.36.104.239:10808 | JP | 1402 | 23 | 152/176 |
| http://130.110.103.245:3128 | SA | 1244 | 22 | 158/176 |
| http://103.133.26.72:8080 | ID | 2570 | 19 | 56/102 |
| http://45.189.57.114:3129 | EC | 792 | 18 | 18/18 |
| http://123.200.8.170:10000 | BD | 3015 | 15 | 82/174 |
| http://102.244.78.61:8082 | CM | 1364 | 15 | 54/65 |
| http://190.12.150.244:999 | EC | 2536 | 15 | 128/172 |
| socks5://69.55.49.177:38182 | US | 1167 | 15 | 30/31 |
| http://165.154.162.73:8888 | US | 2089 | 14 | 119/176 |
| socks5://45.61.129.165:9050 | US | 1763 | 14 | 135/176 |
| http://190.123.83.137:999 | AR | 4651 | 13 | 13/13 |
| http://190.0.246.213:4040 | CO | 1714 | 13 | 131/141 |
| http://189.51.168.165:999 | MX | 480 | 13 | 82/88 |
| http://103.133.26.119:8080 | ID | 1702 | 12 | 55/86 |
| http://82.152.138.127:999 | MX | 2955 | 12 | 52/138 |
| http://189.51.168.164:999 | MX | 1499 | 12 | 12/12 |
| http://49.229.100.235:8080 | TH | 1257 | 12 | 84/124 |
| http://171.100.254.137:8080 | TH | 1293 | 12 | 12/12 |
| http://185.191.239.248:3128 | CH | 1237 | 11 | 127/175 |
| http://102.244.78.61:8080 | CM | 1340 | 11 | 54/65 |
| http://41.33.245.139:1976 | EG | 1229 | 11 | 14/15 |
| http://43.161.254.16:3128 | HK | 818 | 11 | 13/16 |
| http://103.130.61.61:8081 | ID | 2440 | 11 | 145/176 |
| http://61.91.162.126:8080 | TH | 1275 | 11 | 89/119 |
| http://103.10.231.189:8080 | TH | 2029 | 11 | 116/161 |
| http://184.75.221.82:3118 | CA | 3262 | 10 | 123/141 |
| http://123.121.122.142:8888 | CN | 1458 | 10 | 15/22 |
| http://190.0.246.210:4040 | CO | 2451 | 10 | 161/175 |
| http://177.234.217.93:999 | EC | 2261 | 10 | 24/35 |
| http://34.88.38.81:9443 | FI | 1020 | 10 | 99/141 |
| http://35.228.49.168:9443 | FI | 830 | 10 | 80/113 |
| http://103.133.26.50:8080 | ID | 1411 | 10 | 50/77 |
| http://103.18.79.197:8085 | ID | 1267 | 9 | 37/112 |
| http://159.223.41.216:9090 | SG | 958 | 9 | 100/136 |
| http://181.78.195.137:999 | EC | 1759 | 8 | 66/176 |
| http://41.128.77.76:1981 | EG | 1180 | 8 | 59/130 |
| http://187.86.161.2:8080 | BR | 2564 | 7 | 11/12 |
| http://102.244.78.61:8086 | CM | 1341 | 7 | 52/64 |
| http://102.244.78.61:8089 | CM | 1361 | 7 | 51/64 |
| http://198.244.254.77:3128 | GB | 1834 | 7 | 52/60 |
| http://47.238.255.80:3128 | HK | 5604 | 7 | 9/10 |
| http://38.156.76.112:999 | CO | 6009 | 6 | 33/163 |
| http://200.125.170.226:999 | DO | 4238 | 6 | 6/6 |
| http://45.186.6.104:3128 | EC | 743 | 6 | 145/154 |
| http://103.156.57.135:9988 | ID | 3256 | 6 | 35/116 |
| http://203.210.85.215:8080 | ID | 5994 | 6 | 6/6 |
| http://185.238.238.29:58080 | PL | 2030 | 6 | 72/168 |
| http://167.99.74.174:9090 | SG | 948 | 6 | 89/136 |
| socks5://113.249.111.67:1080 | CN | 7726 | 6 | 64/143 |
| socks5://171.25.158.95:1080 | SE | 4144 | 6 | 73/91 |
| socks5://45.61.188.134:44499 | US | 585 | 6 | 77/143 |
| http://38.180.18.103:3128 | BE | 740 | 5 | 5/5 |
| http://15.229.149.81:3128 | BR | 3194 | 5 | 53/86 |
| http://102.244.78.61:8081 | CM | 1385 | 5 | 50/62 |
| http://123.121.122.28:8888 | CN | 1768 | 5 | 77/125 |
| http://45.65.138.48:999 | CO | 4782 | 5 | 80/176 |
| http://41.128.77.76:1976 | EG | 2674 | 5 | 60/142 |
| http://81.19.210.10:80 | GB | 1100 | 5 | 26/37 |
| http://104.194.146.9:80 | GB | 678 | 5 | 16/22 |
| http://108.137.124.195:8123 | ID | 5351 | 5 | 25/93 |
| http://45.174.168.16:999 | MX | 5657 | 5 | 28/129 |
| http://128.199.254.13:9090 | SG | 949 | 5 | 64/105 |
| http://190.97.250.230:999 | VE | 3633 | 5 | 17/37 |
| socks4://143.198.239.45:10015 | US | 4510 | 5 | 8/25 |
| socks5://45.74.31.42:7471 | NL | 4201 | 5 | 6/7 |
| http://45.65.224.74:999 | AR | 4213 | 4 | 33/41 |
| http://187.102.219.42:999 | AR | 2525 | 4 | 99/171 |
| http://3.26.199.107:1234 | AU | 3801 | 4 | 21/89 |
| http://102.244.78.61:8083 | CM | 1335 | 4 | 51/64 |
| http://102.244.78.61:8084 | CM | 1341 | 4 | 51/64 |
| http://102.244.78.61:8088 | CM | 1336 | 4 | 50/64 |
| http://221.221.154.156:8888 | CN | 2706 | 4 | 41/136 |
| http://190.14.224.244:999 | CO | 5131 | 4 | 18/87 |
| http://190.71.72.85:2525 | CO | 712 | 4 | 20/61 |
| http://38.75.82.219:999 | DO | 3909 | 4 | 49/105 |
| http://45.198.10.39:9191 | ID | 6585 | 4 | 19/82 |
| http://49.213.43.6:8080 | ID | 2338 | 4 | 5/6 |
| http://103.124.139.197:8181 | ID | 4221 | 4 | 18/100 |
| http://103.130.61.60:8081 | ID | 1108 | 4 | 22/32 |
| http://103.162.220.246:8085 | ID | 4311 | 4 | 13/70 |
| http://103.172.42.179:1111 | ID | 7052 | 4 | 19/74 |
| http://103.173.138.225:8080 | ID | 4923 | 4 | 8/9 |
| http://160.22.207.73:8082 | ID | 3258 | 4 | 24/52 |
| http://165.99.192.27:1111 | ID | 5367 | 4 | 9/14 |
| http://79.52.108.2:8081 | IT | 1934 | 4 | 5/6 |
| http://38.56.251.27:999 | MX | 1420 | 4 | 6/7 |
| http://190.237.238.183:999 | PE | 1197 | 4 | 5/6 |
| http://203.177.217.222:8082 | PH | 6135 | 4 | 67/121 |
| http://128.199.113.85:9090 | SG | 964 | 4 | 6/7 |
| http://125.25.167.196:80 | TH | 4814 | 4 | 16/30 |
| http://180.180.156.96:80 | TH | 4517 | 4 | 8/21 |
| http://180.180.217.53:80 | TH | 2402 | 4 | 8/9 |
| http://44.200.234.67:17046 | US | 2134 | 4 | 36/136 |
