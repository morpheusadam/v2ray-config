# Proxy status

Generated 2026-11-05T20:53:26Z by `harvest.py`.

- **3390** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **6000** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **37065** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 171/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 4154 |
| socks5 | 1839 |
| socks4 | 7 |

| country | entries |
|---|---|
| NL | 1781 |
| ID | 1311 |
| CO | 202 |
| PH | 202 |
| CH | 176 |
| US | 167 |
| MX | 166 |
| TH | 157 |
| TR | 135 |
| BR | 121 |
| IN | 111 |
| VE | 81 |
| DO | 78 |
| CN | 76 |
| EC | 74 |
| AR | 73 |
| BD | 71 |
| RU | 68 |
| PE | 50 |
| PK | 50 |
| SG | 49 |
| DE | 42 |
| EG | 41 |
| JP | 35 |
| CL | 34 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 3 | 2026-11-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 38 | 2026-11-05 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 80 | 2026-11-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 167 | 167 | 24 | 2026-11-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 243 | 243 | 51 | 2026-11-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 275 | 275 | 185 | 2026-11-05 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-05 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-05 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1155 | 1155 | 301 | 2026-11-05 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1255 | 1255 | 0 | 2026-11-05 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1395 | 1395 | 540 | 2026-11-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-11-05 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1581 | 2026-11-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1817 | 1817 | 659 | 2026-11-05 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1966 | 1966 | 947 | 2026-11-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2429 | 2429 | 1280 | 2026-11-05 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4116 | 4116 | 1655 | 2026-11-05 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5012 | 5012 | 3799 | 2026-11-05 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12677 | 12677 | 2584 | 2026-11-05 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 470 | 84 | 84/84 |
| http://103.237.102.191:11111 | DE | 912 | 60 | 166/173 |
| http://103.133.26.73:3128 | ID | 1458 | 49 | 69/151 |
| http://176.111.37.5:39811 | HK | 1266 | 44 | 154/173 |
| http://34.43.46.91:80 | US | 2193 | 43 | 167/173 |
| http://4.144.146.21:80 | SG | 1041 | 41 | 58/65 |
| http://176.111.37.216:39811 | HK | 2472 | 36 | 145/173 |
| http://34.43.46.91:443 | US | 1509 | 22 | 162/173 |
| socks5://101.36.104.239:10808 | JP | 2116 | 20 | 149/173 |
| http://130.110.103.245:3128 | SA | 1214 | 19 | 155/173 |
| socks5://193.25.215.182:22222 | US | 770 | 19 | 146/173 |
| http://103.133.26.72:8080 | ID | 1563 | 16 | 53/99 |
| http://45.189.57.114:3129 | EC | 1021 | 15 | 15/15 |
| http://123.200.8.170:10000 | BD | 3312 | 12 | 79/171 |
| http://102.244.78.61:8082 | CM | 1391 | 12 | 51/62 |
| http://190.12.150.244:999 | EC | 3314 | 12 | 125/169 |
| http://154.59.56.72:999 | VE | 968 | 12 | 99/132 |
| socks5://69.55.49.177:38182 | US | 1401 | 12 | 27/28 |
| http://186.96.111.214:999 | CO | 4067 | 11 | 81/162 |
| http://165.154.162.73:8888 | US | 1005 | 11 | 116/173 |
| socks5://45.61.129.165:9050 | US | 1339 | 11 | 132/173 |
| http://190.123.83.137:999 | AR | 2613 | 10 | 10/10 |
| http://190.0.246.213:4040 | CO | 574 | 10 | 128/138 |
| http://189.51.168.165:999 | MX | 477 | 10 | 79/85 |
| http://154.59.56.74:999 | VE | 697 | 10 | 93/136 |
| http://128.201.30.222:8666 | BR | 7862 | 9 | 12/19 |
| http://45.65.137.218:999 | CO | 4212 | 9 | 61/138 |
| http://131.221.40.131:4040 | CO | 1206 | 9 | 11/12 |
| http://177.234.217.83:999 | EC | 4762 | 9 | 16/20 |
| http://177.234.217.92:999 | EC | 2839 | 9 | 17/22 |
| http://103.133.26.119:8080 | ID | 2160 | 9 | 52/83 |
| http://202.47.185.153:8090 | ID | 7650 | 9 | 31/128 |
| http://140.238.32.108:3128 | JP | 1924 | 9 | 98/172 |
| http://82.152.138.127:999 | MX | 310 | 9 | 49/135 |
| http://189.51.168.164:999 | MX | 1319 | 9 | 9/9 |
| http://152.42.170.187:9090 | SG | 1041 | 9 | 9/9 |
| http://49.229.100.235:8080 | TH | 1373 | 9 | 81/121 |
| http://171.100.254.137:8080 | TH | 1421 | 9 | 9/9 |
| http://185.191.239.248:3128 | CH | 1991 | 8 | 124/172 |
| http://102.244.78.61:8080 | CM | 1395 | 8 | 51/62 |
| http://41.33.245.139:1976 | EG | 2238 | 8 | 11/12 |
| http://43.161.254.16:3128 | HK | 978 | 8 | 10/13 |
| http://103.130.61.61:8081 | ID | 1694 | 8 | 142/173 |
| http://61.91.162.126:8080 | TH | 1396 | 8 | 86/116 |
| http://103.10.231.189:8080 | TH | 1845 | 8 | 113/158 |
| socks5://84.200.89.140:1080 | DE | 1476 | 8 | 8/8 |
| http://45.65.224.125:999 | AR | 4028 | 7 | 25/35 |
| http://184.75.221.82:3118 | CA | 295 | 7 | 120/138 |
| http://123.121.122.142:8888 | CN | 2279 | 7 | 12/19 |
| http://190.0.246.210:4040 | CO | 694 | 7 | 158/172 |
| http://177.234.217.93:999 | EC | 5883 | 7 | 21/32 |
| http://34.88.38.81:9443 | FI | 943 | 7 | 96/138 |
| http://35.228.49.168:9443 | FI | 714 | 7 | 77/110 |
| http://103.133.26.50:8080 | ID | 1436 | 7 | 47/74 |
| http://103.145.34.112:1111 | ID | 6476 | 7 | 33/145 |
| http://103.167.116.166:8087 | PH | 4745 | 7 | 9/12 |
| http://152.42.177.32:8888 | SG | 1024 | 7 | 88/133 |
| http://18.217.248.118:5050 | US | 1455 | 7 | 8/9 |
| socks4://188.226.27.24:1080 | RU | 5073 | 7 | 8/9 |
| http://200.10.31.42:8081 | CO | 2547 | 6 | 24/46 |
| http://84.36.141.180:1981 | EG | 6220 | 6 | 26/124 |
| http://36.94.27.65:8080 | ID | 4570 | 6 | 9/25 |
| http://103.18.79.197:8085 | ID | 6290 | 6 | 34/109 |
| http://103.194.47.53:8082 | ID | 4440 | 6 | 46/142 |
| http://160.19.146.117:2022 | ID | 5422 | 6 | 31/136 |
| http://45.174.242.145:999 | MX | 3739 | 6 | 32/128 |
| http://159.223.41.216:9090 | SG | 1033 | 6 | 97/133 |
| http://38.63.98.32:999 | VE | 3756 | 6 | 20/61 |
| socks5://5.255.117.250:1080 | NL | 2846 | 6 | 54/158 |
| socks5://43.156.137.7:10808 | SG | 2386 | 6 | 6/6 |
| http://168.194.34.196:9001 | AR | 4525 | 5 | 66/171 |
| http://190.0.246.211:4040 | CO | 1080 | 5 | 159/173 |
| http://177.234.217.46:999 | EC | 4401 | 5 | 41/120 |
| http://181.78.195.137:999 | EC | 3649 | 5 | 63/173 |
| http://181.188.203.112:999 | EC | 3866 | 5 | 56/165 |
| http://41.128.77.76:1981 | EG | 1039 | 5 | 56/127 |
| http://102.164.252.150:8080 | GQ | 7021 | 5 | 54/132 |
| http://103.61.234.186:8180 | ID | 6943 | 5 | 74/170 |
| http://103.80.215.100:8080 | ID | 3870 | 5 | 28/140 |
| http://115.178.55.219:8080 | ID | 4956 | 5 | 15/61 |
| http://154.18.255.118:1111 | ID | 4507 | 5 | 9/13 |
| http://157.10.90.65:8088 | ID | 4228 | 5 | 5/5 |
| http://162.4.78.55:8080 | ID | 6798 | 5 | 31/112 |
| http://139.135.65.158:8082 | PH | 1305 | 5 | 28/103 |
| http://180.191.234.194:5050 | PH | 4025 | 5 | 18/91 |
| http://210.213.99.36:8081 | PH | 4159 | 5 | 11/47 |
| http://1.20.101.20:80 | TH | 5839 | 5 | 8/13 |
| http://1.20.178.200:80 | TH | 5448 | 5 | 7/13 |
| http://125.27.241.98:8080 | TH | 5134 | 5 | 10/19 |
| http://154.59.56.73:999 | VE | 803 | 5 | 103/145 |
| socks5://5.75.133.113:10808 | DE | 7728 | 5 | 14/63 |
| socks5://121.169.46.116:1090 | KR | 1571 | 5 | 120/173 |
| socks5://45.74.31.42:7722 | NL | 6715 | 5 | 5/5 |
| socks5://149.248.18.106:1081 | US | 4340 | 5 | 18/34 |
| http://45.65.226.170:999 | AR | 1200 | 4 | 15/24 |
| http://187.102.219.34:999 | AR | 1220 | 4 | 69/124 |
| http://187.86.161.2:8080 | BR | 3946 | 4 | 8/9 |
| http://102.244.78.61:8086 | CM | 1342 | 4 | 49/61 |
| http://102.244.78.61:8089 | CM | 1386 | 4 | 48/61 |
| http://38.19.50.74:999 | CO | 1604 | 4 | 6/9 |
