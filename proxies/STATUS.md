# Proxy status

Generated 2026-11-27T02:23:20Z by `harvest.py`.

- **2027** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3855** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **25915** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 232/600 (39%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3400 |
| socks5 | 440 |
| socks4 | 15 |

| country | entries |
|---|---|
| ID | 1045 |
| ?? | 260 |
| NL | 207 |
| PH | 178 |
| MX | 160 |
| CO | 154 |
| US | 110 |
| IN | 108 |
| CN | 106 |
| TR | 103 |
| BR | 100 |
| VE | 91 |
| CH | 87 |
| TH | 84 |
| RU | 75 |
| BD | 61 |
| AR | 58 |
| EC | 58 |
| PK | 44 |
| DO | 42 |
| VN | 37 |
| DE | 36 |
| PE | 35 |
| ZA | 33 |
| EG | 31 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 4 | 2026-11-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 32 | 2026-11-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 60 | 2026-11-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 226 | 226 | 14 | 2026-11-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 237 | 237 | 54 | 2026-11-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 350 | 350 | 62 | 2026-11-27 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 442 | 2026-11-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 637 | 637 | 129 | 2026-11-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 673 | 673 | 438 | 2026-11-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1113 | 2026-11-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1815 | 1815 | 293 | 2026-11-27 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1957 | 1957 | 209 | 2026-11-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2325 | 2325 | 200 | 2026-11-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2592 | 2592 | 767 | 2026-11-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2879 | 2879 | 1611 | 2026-11-27 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5759 | 5759 | 4570 | 2026-11-27 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 13005 | 13005 | 2296 | 2026-11-27 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 905 | 87 | 197/216 |
| http://130.110.103.245:3128 | SA | 1244 | 62 | 198/216 |
| http://141.94.22.37:3128 | FR | 605 | 28 | 31/32 |
| http://45.155.226.177:3128 | HK | 552 | 25 | 30/32 |
| http://4.144.146.21:80 | SG | 1030 | 23 | 99/108 |
| http://34.43.46.91:80 | US | 283 | 21 | 209/216 |
| http://189.51.168.164:999 | MX | 1168 | 20 | 48/52 |
| http://20.98.234.24:8080 | US | 253 | 20 | 20/20 |
| socks5://69.55.49.177:38182 | US | 368 | 20 | 60/71 |
| http://103.237.102.191:11111 | DE | 680 | 19 | 203/216 |
| http://45.186.6.104:3128 | EC | 722 | 18 | 184/194 |
| http://103.133.26.50:8080 | ID | 1367 | 18 | 82/117 |
| http://103.133.26.73:3128 | ID | 1506 | 18 | 106/194 |
| http://147.161.246.34:80 | CH | 4146 | 16 | 16/16 |
| http://45.135.95.185:3128 | RU | 1324 | 14 | 14/14 |
| http://128.199.113.85:9090 | SG | 1034 | 14 | 34/47 |
| socks5://123.58.219.171:10808 | HK | 2168 | 14 | 158/216 |
| http://103.163.80.181:8085 | ID | 1412 | 12 | 12/12 |
| http://50.238.106.26:3128 | US | 216 | 12 | 12/12 |
| http://158.247.125.5:9443 | CO | 535 | 11 | 11/11 |
| http://34.43.46.91:443 | US | 275 | 11 | 200/216 |
| http://216.125.18.67:3128 | US | 315 | 11 | 11/11 |
| http://103.21.150.15:3128 | VN | 1263 | 10 | 12/28 |
| http://185.191.239.248:3128 | CH | 947 | 9 | 152/215 |
| http://45.136.253.145:3128 | TH | 1140 | 9 | 14/20 |
| http://102.244.78.61:8082 | CM | 1260 | 8 | 82/105 |
| http://102.244.78.61:8083 | CM | 1261 | 8 | 82/104 |
| http://45.65.138.48:999 | CO | 3547 | 8 | 113/216 |
| http://177.234.217.89:999 | EC | 2523 | 8 | 27/41 |
| http://31.130.153.132:3128 | KZ | 1301 | 8 | 8/8 |
| http://129.153.97.250:9443 | US | 343 | 8 | 8/8 |
| http://154.59.56.78:999 | VE | 2314 | 8 | 118/172 |
| http://103.81.86.170:8888 | VN | 6999 | 8 | 8/8 |
| socks5://59.11.209.162:1080 | KR | 1063 | 8 | 8/8 |
| http://190.12.150.244:999 | EC | 1176 | 7 | 158/212 |
| http://128.199.116.219:9090 | SG | 1040 | 7 | 105/135 |
| http://114.246.197.205:8888 | CN | 2059 | 6 | 10/12 |
| http://114.249.228.162:8888 | CN | 7059 | 6 | 6/6 |
| http://123.121.120.25:8888 | CN | 1973 | 6 | 10/12 |
| http://45.65.137.218:999 | CO | 4593 | 6 | 93/181 |
| http://197.164.101.14:1976 | EG | 1214 | 6 | 67/188 |
| http://197.164.101.14:1981 | EG | 1126 | 6 | 56/186 |
| http://173.212.207.102:1214 | FR | 641 | 6 | 6/6 |
| http://189.187.131.201:999 | MX | 6665 | 6 | 6/6 |
| http://16.5.7.5:8118 | BR | 1826 | 5 | 10/15 |
| http://102.244.78.61:8080 | CM | 1271 | 5 | 84/105 |
| http://123.115.143.194:8888 | CN | 1910 | 5 | 9/15 |
| http://197.164.101.11:1981 | EG | 1110 | 5 | 14/33 |
| http://213.131.85.28:1976 | EG | 1053 | 5 | 20/30 |
| socks5://49.13.22.249:10802 | DE | 2762 | 5 | 55/143 |
| socks5://46.37.59.97:1080 | GB | 6370 | 5 | 16/30 |
| http://64.76.33.108:999 | AR | 5324 | 4 | 20/69 |
| http://187.102.219.42:999 | AR | 1258 | 4 | 123/211 |
| http://200.110.218.11:999 | AR | 6244 | 4 | 39/176 |
| http://103.245.109.70:21458 | BD | 4330 | 4 | 37/121 |
| http://114.244.208.65:8888 | CN | 2781 | 4 | 4/4 |
| http://114.246.200.14:8888 | CN | 2260 | 4 | 6/7 |
| http://114.249.219.234:8888 | CN | 1575 | 4 | 8/12 |
| http://114.249.221.91:8888 | CN | 2583 | 4 | 5/11 |
| http://190.2.214.147:999 | CO | 6743 | 4 | 22/70 |
| http://38.41.184.73:999 | DO | 3034 | 4 | 21/89 |
| http://177.234.217.45:999 | EC | 1893 | 4 | 60/147 |
| http://177.234.217.84:999 | EC | 4823 | 4 | 39/63 |
| http://41.65.55.27:1981 | EG | 1125 | 4 | 59/156 |
| http://41.196.16.231:1976 | EG | 1037 | 4 | 8/43 |
| http://45.245.208.180:8080 | EG | 3163 | 4 | 63/89 |
| http://81.10.102.153:8080 | EG | 1288 | 4 | 4/4 |
| http://217.52.247.75:1976 | EG | 1052 | 4 | 4/4 |
| http://51.68.102.5:3128 | FR | 637 | 4 | 9/30 |
| http://198.244.254.77:3128 | GB | 1603 | 4 | 80/100 |
| http://9.154.240.122:8085 | ID | 5638 | 4 | 27/110 |
| http://38.188.63.115:8081 | ID | 6409 | 4 | 32/140 |
| http://49.213.59.105:8082 | ID | 3469 | 4 | 59/175 |
| http://103.98.117.126:8080 | ID | 3256 | 4 | 16/69 |
| http://103.110.10.166:8181 | ID | 7189 | 4 | 45/179 |
| http://103.122.0.52:8181 | ID | 4033 | 4 | 37/128 |
| http://103.153.62.217:8181 | ID | 7060 | 4 | 27/139 |
| http://103.172.70.27:9090 | ID | 6039 | 4 | 10/30 |
| http://103.176.96.23:8080 | ID | 1373 | 4 | 34/121 |
| http://103.176.96.32:8082 | ID | 6277 | 4 | 53/209 |
| http://103.179.252.229:1111 | ID | 3610 | 4 | 40/206 |
| http://45.43.60.220:8080 | JP | 6095 | 4 | 120/215 |
| http://102.210.125.2:8080 | KE | 1676 | 4 | 15/44 |
| http://78.14.19.3:3128 | MX | 4497 | 4 | 53/176 |
| http://115.147.47.214:3128 | PH | 3231 | 4 | 10/37 |
| http://202.154.241.199:808 | PK | 6404 | 4 | 11/37 |
| http://81.27.101.176:443 | PL | 741 | 4 | 4/4 |
| http://81.27.101.176:80 | PL | 752 | 4 | 4/4 |
| http://192.203.0.78:999 | PR | 5397 | 4 | 24/80 |
| http://128.199.121.61:9090 | SG | 1026 | 4 | 106/136 |
| http://195.226.213.251:8888 | UA | 2701 | 4 | 89/210 |
| http://45.66.156.107:8080 | US | 986 | 4 | 6/13 |
| http://45.66.156.107:8081 | US | 1532 | 4 | 11/16 |
| http://195.158.8.123:3128 | UZ | 2319 | 4 | 139/214 |
| http://154.59.56.74:999 | VE | 3319 | 4 | 122/179 |
| socks4://103.13.19.219:10808 | JP | 3036 | 4 | 24/33 |
| socks5://149.88.72.174:5555 | HK | 5026 | 4 | 4/4 |
| socks5://188.0.153.235:1080 | KZ | 5130 | 4 | 7/14 |
| socks5://193.218.118.128:1080 | UA | 7320 | 4 | 52/72 |
| socks5://172.104.210.252:1080 | US | 241 | 4 | 4/4 |
