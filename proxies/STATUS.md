# Proxy status

Generated 2026-10-29T19:16:04Z by `harvest.py`.

- **1743** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4294** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39336** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 93/600 (16%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2276 |
| socks5 | 2015 |
| socks4 | 3 |

| country | entries |
|---|---|
| NL | 1816 |
| ID | 727 |
| ?? | 209 |
| PH | 121 |
| CO | 96 |
| MX | 85 |
| US | 85 |
| VE | 70 |
| RU | 68 |
| TH | 59 |
| BR | 57 |
| CN | 57 |
| TR | 52 |
| EC | 51 |
| BD | 50 |
| IN | 45 |
| DO | 41 |
| AR | 36 |
| SG | 30 |
| PE | 28 |
| VN | 28 |
| ZA | 27 |
| EG | 24 |
| JP | 24 |
| SY | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 2 | 2026-10-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 86 | 86 | 43 | 2026-10-29 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 149 | 149 | 40 | 2026-10-29 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 66 | 2026-10-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 167 | 167 | 104 | 2026-10-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 331 | 331 | 103 | 2026-10-29 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 504 | 504 | 169 | 2026-10-29 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-29 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-10-29 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 693 | 693 | 15 | 2026-10-29 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 721 | 721 | 264 | 2026-10-29 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1295 | 1295 | 73 | 2026-10-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-10-29 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1593 | 2026-10-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2082 | 2082 | 645 | 2026-10-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2288 | 2288 | 1557 | 2026-10-29 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2945 | 2945 | 878 | 2026-10-29 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 80116 | 80116 | 65908 | 2026-10-29 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 87225 | 87224 | 3141 | 2026-10-29 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 3637 | 79 | 146/159 |
| http://149.130.173.58:9443 | CO | 590 | 70 | 70/70 |
| http://190.0.246.213:4040 | CO | 2874 | 53 | 116/124 |
| http://103.237.102.191:11111 | DE | 877 | 46 | 152/159 |
| http://45.186.6.104:3128 | EC | 713 | 40 | 130/137 |
| http://103.133.26.73:3128 | ID | 1329 | 35 | 55/137 |
| http://103.133.26.119:8080 | ID | 1589 | 35 | 39/69 |
| http://176.111.37.5:39811 | HK | 996 | 30 | 140/159 |
| http://34.43.46.91:80 | US | 2556 | 29 | 153/159 |
| http://4.144.146.21:80 | SG | 928 | 27 | 44/51 |
| http://190.0.246.210:4040 | CO | 4567 | 26 | 145/158 |
| http://43.155.62.157:443 | HK | 2662 | 26 | 54/62 |
| http://186.5.94.206:999 | EC | 1160 | 24 | 112/121 |
| http://189.51.168.165:999 | MX | 472 | 23 | 66/71 |
| http://176.111.37.216:39811 | HK | 1019 | 22 | 131/159 |
| http://103.130.61.61:8081 | ID | 1620 | 21 | 129/159 |
| http://103.133.26.50:8080 | ID | 1282 | 19 | 38/60 |
| socks5://67.207.92.87:1088 | US | 540 | 14 | 100/158 |
| socks5://69.55.49.177:38182 | US | 803 | 14 | 14/14 |
| http://43.202.114.177:7428 | KR | 3067 | 10 | 33/73 |
| socks5://47.238.126.208:1080 | HK | 3159 | 9 | 35/64 |
| http://51.15.20.32:3129 | NL | 706 | 8 | 19/23 |
| http://34.43.46.91:443 | US | 3897 | 8 | 148/159 |
| http://123.200.8.170:10000 | BD | 1681 | 7 | 67/157 |
| http://34.88.38.81:9443 | FI | 1000 | 7 | 86/124 |
| http://35.228.49.168:9443 | FI | 876 | 7 | 67/96 |
| http://103.194.47.53:8082 | ID | 6354 | 7 | 38/128 |
| http://154.59.56.72:999 | VE | 5416 | 7 | 86/118 |
| socks5://213.199.47.140:1080 | FR | 3758 | 7 | 99/125 |
| socks5://103.100.158.115:10809 | JP | 3309 | 7 | 38/47 |
| socks5://103.182.22.221:9000 | ?? | 5304 | 7 | 8/11 |
| http://45.65.226.173:999 | AR | 5974 | 6 | 10/20 |
| http://101.251.204.174:8080 | CN | 1803 | 6 | 80/145 |
| http://123.119.25.143:8888 | CN | 6252 | 6 | 55/124 |
| http://167.172.76.176:9090 | SG | 3223 | 6 | 83/120 |
| socks5://101.36.104.239:10808 | JP | 1419 | 6 | 135/159 |
| socks5://193.218.118.128:1080 | UA | 1350 | 6 | 12/15 |
| http://114.244.221.178:8888 | CN | 1209 | 5 | 40/82 |
| http://103.38.101.194:1111 | ID | 5554 | 5 | 37/153 |
| http://103.122.0.52:8181 | ID | 4451 | 5 | 21/71 |
| http://103.176.96.84:8082 | ID | 1280 | 5 | 25/97 |
| http://51.16.4.39:1461 | IL | 1488 | 5 | 35/143 |
| http://200.94.38.42:2604 | MX | 2805 | 5 | 26/52 |
| http://130.110.103.245:3128 | SA | 1302 | 5 | 141/159 |
| http://154.59.56.74:999 | VE | 3373 | 5 | 80/122 |
| http://154.59.56.76:999 | VE | 3841 | 5 | 86/119 |
| http://49.149.195.243:8081 | ?? | 7736 | 5 | 5/5 |
| socks5://49.13.22.249:10805 | DE | 3040 | 5 | 45/77 |
| socks5://45.61.129.165:9050 | US | 3883 | 5 | 119/159 |
| socks5://45.61.188.134:44499 | US | 558 | 5 | 61/126 |
| socks5://193.25.215.182:22222 | US | 452 | 5 | 132/159 |
| http://118.179.213.183:81 | BD | 2461 | 4 | 26/145 |
| http://114.248.179.223:8888 | CN | 1749 | 4 | 53/127 |
| http://45.71.186.213:999 | EC | 2025 | 4 | 58/143 |
| http://41.33.245.138:1976 | EG | 6444 | 4 | 25/84 |
| http://41.128.72.142:1981 | EG | 4490 | 4 | 19/78 |
| http://45.240.232.62:8080 | EG | 5665 | 4 | 59/145 |
| http://148.230.27.77:999 | GT | 4935 | 4 | 27/136 |
| http://103.22.98.69:8080 | ID | 3275 | 4 | 25/131 |
| http://103.61.234.186:8180 | ID | 2304 | 4 | 65/156 |
| http://103.172.42.93:1111 | ID | 3993 | 4 | 13/53 |
| http://115.85.88.18:8080 | ID | 5303 | 4 | 16/66 |
| http://157.66.192.114:8080 | ID | 4522 | 4 | 10/24 |
| http://160.22.207.95:8082 | ID | 1194 | 4 | 33/137 |
| http://51.85.44.162:31819 | IL | 3026 | 4 | 9/11 |
| http://82.152.138.127:999 | MX | 1272 | 4 | 37/121 |
| http://115.147.58.42:5050 | PH | 1319 | 4 | 28/138 |
| http://185.238.236.226:58080 | PL | 3447 | 4 | 31/81 |
| http://167.99.74.174:9090 | SG | 2013 | 4 | 78/119 |
| http://93.184.72.130:8080 | SK | 3192 | 4 | 20/83 |
| http://188.132.221.186:8080 | TR | 5122 | 4 | 20/97 |
| http://200.59.191.27:999 | VE | 4886 | 4 | 104/154 |
| http://45.65.226.170:999 | ?? | 4137 | 4 | 6/10 |
| http://123.121.142.43:8888 | ?? | 1612 | 4 | 5/6 |
| socks5://45.149.92.160:1080 | HK | 1094 | 4 | 17/26 |
| socks5://110.76.144.112:1080 | ID | 3681 | 4 | 16/41 |
| socks5://45.74.31.46:9408 | NL | 2797 | 4 | 6/23 |
| socks5://45.74.31.47:5304 | NL | 4517 | 4 | 6/21 |
| socks5://171.25.158.95:1080 | SE | 4042 | 4 | 63/74 |
| http://45.65.226.174:999 | AR | 3421 | 3 | 10/20 |
| http://16.51.5.77:1011 | AU | 3623 | 3 | 4/18 |
| http://18.231.126.121:33769 | BR | 5380 | 3 | 5/10 |
| http://123.121.134.192:8888 | CN | 6755 | 3 | 10/25 |
| http://201.219.218.4:8080 | CO | 6792 | 3 | 6/11 |
| http://103.119.19.218:3128 | CZ | 4217 | 3 | 58/72 |
| http://177.234.217.92:999 | EC | 7377 | 3 | 5/8 |
| http://18.175.170.244:51141 | GB | 1942 | 3 | 4/7 |
| http://36.89.56.169:8080 | ID | 5854 | 3 | 14/65 |
| http://45.198.32.207:8080 | ID | 1334 | 3 | 30/148 |
| http://103.97.141.40:8080 | ID | 4793 | 3 | 29/115 |
| http://103.144.54.71:8082 | ID | 6519 | 3 | 36/95 |
| http://103.146.38.89:3127 | ID | 7568 | 3 | 29/157 |
| http://103.154.76.18:8080 | ID | 3446 | 3 | 15/63 |
| http://103.158.210.80:8082 | ID | 3351 | 3 | 40/149 |
| http://103.169.133.118:8080 | ID | 7865 | 3 | 16/78 |
| http://103.172.42.161:1111 | ID | 5980 | 3 | 12/93 |
| http://103.175.238.206:8082 | ID | 1303 | 3 | 22/96 |
| http://103.176.96.123:8082 | ID | 3394 | 3 | 28/104 |
| http://103.176.96.225:8082 | ID | 3178 | 3 | 31/104 |
| http://103.195.65.150:8080 | ID | 7128 | 3 | 14/71 |
