# Proxy status

Generated 2026-11-07T22:58:46Z by `harvest.py`.

- **2380** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **36317** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 212/600 (35%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3538 |
| socks5 | 2448 |
| socks4 | 14 |

| country | entries |
|---|---|
| NL | 2327 |
| ID | 1075 |
| ?? | 541 |
| PH | 160 |
| CO | 150 |
| US | 124 |
| MX | 117 |
| TH | 106 |
| TR | 99 |
| VE | 95 |
| BR | 81 |
| BD | 74 |
| IN | 74 |
| AR | 65 |
| DO | 59 |
| CN | 56 |
| EC | 52 |
| EG | 43 |
| PK | 37 |
| VN | 37 |
| RU | 35 |
| PE | 34 |
| DE | 32 |
| ZA | 32 |
| SG | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-11-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 59 | 59 | 4 | 2026-11-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 71 | 71 | 26 | 2026-11-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 94 | 94 | 16 | 2026-11-07 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 43 | 2026-11-07 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 71 | 2026-11-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 227 | 227 | 139 | 2026-11-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-07 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 270 | 270 | 43 | 2026-11-07 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-07 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-07 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-11-07 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1069 | 1069 | 177 | 2026-11-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1135 | 2026-11-07 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1630 | 1630 | 132 | 2026-11-07 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1584 | 2026-11-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2166 | 2166 | 642 | 2026-11-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2803 | 2803 | 551 | 2026-11-07 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2862 | 2862 | 1476 | 2026-11-07 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5122 | 5122 | 3895 | 2026-11-07 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11698 | 11698 | 1866 | 2026-11-07 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 584 | 89 | 89/89 |
| http://103.133.26.73:3128 | ID | 1329 | 54 | 74/156 |
| http://176.111.37.5:39811 | HK | 1190 | 49 | 159/178 |
| http://34.43.46.91:80 | US | 1806 | 48 | 172/178 |
| http://4.144.146.21:80 | SG | 904 | 46 | 63/70 |
| http://176.111.37.216:39811 | HK | 1175 | 41 | 150/178 |
| http://34.43.46.91:443 | US | 1646 | 27 | 167/178 |
| http://130.110.103.245:3128 | SA | 1314 | 24 | 160/178 |
| http://103.133.26.72:8080 | ID | 1233 | 21 | 58/104 |
| http://45.189.57.114:3129 | EC | 1194 | 20 | 20/20 |
| socks5://69.55.49.177:38182 | US | 1330 | 17 | 32/33 |
| http://190.123.83.137:999 | AR | 3186 | 15 | 15/15 |
| http://190.0.246.213:4040 | CO | 786 | 15 | 133/143 |
| http://103.133.26.119:8080 | ID | 1604 | 14 | 57/88 |
| http://189.51.168.164:999 | MX | 4950 | 14 | 14/14 |
| http://49.229.100.235:8080 | TH | 1249 | 14 | 86/126 |
| http://171.100.254.137:8080 | TH | 1431 | 14 | 14/14 |
| http://43.161.254.16:3128 | HK | 2618 | 13 | 15/18 |
| http://103.130.61.61:8081 | ID | 1425 | 13 | 147/178 |
| http://61.91.162.126:8080 | TH | 1211 | 13 | 91/121 |
| http://103.10.231.189:8080 | TH | 1613 | 13 | 118/163 |
| http://184.75.221.82:3118 | CA | 1439 | 12 | 125/143 |
| http://177.234.217.93:999 | EC | 3722 | 12 | 26/37 |
| http://103.133.26.50:8080 | ID | 1318 | 12 | 52/79 |
| http://181.78.195.137:999 | EC | 3189 | 10 | 68/178 |
| http://41.128.77.76:1981 | EG | 2500 | 10 | 61/132 |
| http://102.244.78.61:8086 | CM | 1447 | 9 | 54/66 |
| http://102.244.78.61:8089 | CM | 1459 | 9 | 53/66 |
| http://47.238.255.80:3128 | HK | 7598 | 9 | 11/12 |
| http://200.125.170.226:999 | DO | 2959 | 8 | 8/8 |
| http://45.186.6.104:3128 | EC | 968 | 8 | 147/156 |
| http://167.99.74.174:9090 | SG | 893 | 8 | 91/138 |
| http://38.180.18.103:3128 | BE | 940 | 7 | 7/7 |
| http://102.244.78.61:8081 | CM | 1471 | 7 | 52/64 |
| http://123.121.122.28:8888 | CN | 4182 | 7 | 79/127 |
| http://45.65.138.48:999 | CO | 3853 | 7 | 82/178 |
| http://45.65.224.74:999 | AR | 2451 | 6 | 35/43 |
| http://190.71.72.85:2525 | CO | 825 | 6 | 22/63 |
| http://103.130.61.60:8081 | ID | 3974 | 6 | 24/34 |
| http://165.99.192.27:1111 | ID | 6935 | 6 | 11/16 |
| http://79.52.108.2:8081 | IT | 3980 | 6 | 7/8 |
| http://128.199.113.85:9090 | SG | 931 | 6 | 8/9 |
| http://180.180.156.96:80 | TH | 3013 | 6 | 10/23 |
| http://201.190.178.191:8080 | AR | 6678 | 5 | 31/111 |
| http://103.148.83.110:8889 | BD | 4973 | 5 | 40/176 |
| http://102.244.78.61:8090 | CM | 1485 | 5 | 54/70 |
| http://41.128.72.138:1976 | EG | 2406 | 5 | 7/17 |
| http://196.204.26.243:1976 | EG | 3438 | 5 | 36/106 |
| http://34.105.252.3:3128 | GB | 781 | 5 | 37/60 |
| http://200.52.148.212:999 | HN | 3869 | 5 | 19/40 |
| http://115.178.49.115:8787 | ID | 3194 | 5 | 31/154 |
| http://192.203.0.210:999 | PR | 5835 | 5 | 32/145 |
| http://1.10.133.83:8081 | TH | 3439 | 5 | 20/40 |
| http://18.224.94.46:18058 | US | 1939 | 5 | 15/24 |
| http://161.22.33.89:999 | VE | 5841 | 5 | 11/15 |
| http://109.127.9.99:8080 | ?? | 7521 | 5 | 5/5 |
| http://110.34.1.178:7777 | ?? | 5047 | 5 | 6/8 |
| socks5://45.74.31.40:10932 | NL | 5416 | 5 | 5/5 |
| socks5://45.74.31.42:7492 | NL | 5610 | 5 | 5/5 |
| http://16.51.53.116:23517 | AU | 5660 | 4 | 35/94 |
| http://179.48.80.9:8085 | BR | 6448 | 4 | 23/90 |
| http://16.18.22.211:9090 | CH | 2450 | 4 | 44/138 |
| http://111.199.234.107:9000 | CN | 5480 | 4 | 19/116 |
| http://179.1.213.233:999 | CO | 5034 | 4 | 6/10 |
| http://186.96.111.214:999 | CO | 4119 | 4 | 85/167 |
| http://190.0.246.211:4040 | CO | 1977 | 4 | 163/178 |
| http://177.234.217.92:999 | EC | 4426 | 4 | 21/27 |
| http://41.33.245.139:1981 | EG | 1467 | 4 | 11/16 |
| http://36.50.112.174:8070 | ID | 6493 | 4 | 20/76 |
| http://45.198.20.224:8080 | ID | 4302 | 4 | 20/96 |
| http://49.156.22.238:1080 | ID | 2965 | 4 | 5/6 |
| http://103.51.205.114:8082 | ID | 7582 | 4 | 35/114 |
| http://103.146.38.89:3127 | ID | 4217 | 4 | 38/176 |
| http://103.163.231.106:3127 | ID | 5550 | 4 | 13/79 |
| http://103.172.42.123:1111 | ID | 6020 | 4 | 35/176 |
| http://103.176.94.178:8080 | ID | 5538 | 4 | 17/31 |
| http://103.176.97.221:8082 | ID | 1964 | 4 | 44/146 |
| http://103.178.194.95:8181 | ID | 7538 | 4 | 26/155 |
| http://103.250.128.8:8082 | ID | 2015 | 4 | 15/39 |
| http://144.79.241.254:3128 | ID | 2704 | 4 | 22/79 |
| http://151.158.133.151:8080 | ID | 4709 | 4 | 11/23 |
| http://160.19.145.101:3127 | ID | 6803 | 4 | 26/176 |
| http://165.99.239.90:3125 | ID | 6834 | 4 | 21/100 |
| http://198.15.30.138:8080 | ID | 6329 | 4 | 8/22 |
| http://202.47.188.187:8080 | ID | 4384 | 4 | 13/42 |
| http://160.19.41.52:80 | IN | 4595 | 4 | 17/52 |
| http://52.195.147.51:3128 | JP | 4988 | 4 | 46/142 |
| http://43.202.114.177:31192 | KR | 2328 | 4 | 31/88 |
| http://200.121.48.105:999 | PE | 7161 | 4 | 8/14 |
| http://103.25.220.246:8086 | PH | 2082 | 4 | 21/79 |
| http://161.49.219.181:8082 | PH | 3200 | 4 | 25/177 |
| http://192.92.193.18:999 | PR | 4654 | 4 | 39/133 |
| http://146.190.80.158:9090 | SG | 3382 | 4 | 74/104 |
| http://167.172.76.176:9090 | SG | 917 | 4 | 99/139 |
| http://2.139.174.29:8080 | ?? | 4001 | 4 | 4/4 |
| http://161.49.89.217:8081 | ?? | 4345 | 4 | 4/4 |
| http://181.174.231.152:999 | ?? | 4563 | 4 | 4/4 |
| socks5://202.91.41.102:1080 | BD | 4370 | 4 | 49/177 |
| socks5://172.81.111.156:10001 | HK | 1386 | 4 | 5/6 |
| socks5://122.102.52.24:1080 | ID | 2888 | 4 | 5/6 |
