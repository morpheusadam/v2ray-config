# Proxy status

Generated 2026-10-16T17:28:52Z by `harvest.py`.

- **1504** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3730** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39513** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 103/600 (17%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2031 |
| socks5 | 1694 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 1521 |
| ID | 640 |
| PH | 110 |
| US | 97 |
| CO | 88 |
| MX | 86 |
| CN | 83 |
| RU | 70 |
| ?? | 62 |
| VE | 57 |
| BR | 56 |
| IN | 53 |
| BD | 49 |
| EC | 47 |
| VN | 45 |
| DO | 44 |
| TR | 42 |
| AR | 40 |
| SG | 32 |
| JP | 31 |
| EG | 28 |
| DE | 26 |
| PE | 22 |
| TH | 21 |
| CL | 19 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 2 | 2 | 1 | 2026-10-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 103 | 103 | 43 | 2026-10-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 121 | 121 | 42 | 2026-10-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 124 | 124 | 30 | 2026-10-16 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-10-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 234 | 234 | 81 | 2026-10-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 275 | 275 | 100 | 2026-10-16 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-16 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-16 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 447 | 2026-10-16 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 877 | 877 | 622 | 2026-10-16 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 901 | 901 | 348 | 2026-10-16 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1452 | 1448 | 194 | 2026-10-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-10-16 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1595 | 2026-10-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2307 | 2305 | 648 | 2026-10-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2448 | 2446 | 658 | 2026-10-16 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3035 | 3033 | 2078 | 2026-10-16 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 62930 | 62930 | 48981 | 2026-10-16 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 69449 | 69448 | 2158 | 2026-10-16 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2804 | 53 | 120/133 |
| http://149.130.173.58:9443 | CO | 411 | 44 | 44/44 |
| http://190.0.246.213:4040 | CO | 2709 | 27 | 90/98 |
| http://197.224.185.3:3128 | MU | 1912 | 25 | 94/101 |
| http://103.237.102.191:11111 | DE | 973 | 20 | 126/133 |
| http://203.252.142.217:80 | KR | 832 | 15 | 15/15 |
| http://45.186.6.104:3128 | EC | 679 | 14 | 104/111 |
| socks5://101.36.104.46:10808 | JP | 1631 | 14 | 117/133 |
| http://3.211.120.181:443 | US | 299 | 13 | 27/44 |
| http://165.154.162.73:8888 | US | 1857 | 13 | 86/133 |
| http://102.244.78.61:8083 | CM | 1278 | 12 | 18/21 |
| http://103.130.61.61:8081 | ID | 3224 | 12 | 104/133 |
| http://102.244.78.61:8088 | CM | 1323 | 10 | 17/21 |
| http://5.129.254.5:8888 | RU | 1376 | 10 | 77/88 |
| http://5.129.254.49:8888 | RU | 1385 | 10 | 78/88 |
| http://5.129.254.51:8888 | RU | 1307 | 10 | 78/88 |
| http://5.129.254.60:8888 | RU | 1231 | 10 | 77/87 |
| http://5.129.254.70:8888 | RU | 1269 | 10 | 78/88 |
| http://5.129.254.129:8888 | RU | 1431 | 10 | 83/94 |
| http://5.129.254.154:8888 | RU | 1239 | 10 | 74/84 |
| http://5.129.254.215:8888 | RU | 1308 | 10 | 27/30 |
| http://5.129.254.243:8888 | RU | 1424 | 10 | 27/29 |
| http://34.88.38.81:9443 | FI | 963 | 9 | 68/98 |
| http://35.228.49.168:9443 | FI | 779 | 9 | 49/70 |
| http://103.133.26.50:8080 | ID | 1384 | 9 | 13/34 |
| http://103.133.26.72:8080 | ID | 2572 | 9 | 14/59 |
| http://103.133.26.73:3128 | ID | 1480 | 9 | 29/111 |
| http://103.133.26.119:8080 | ID | 1690 | 9 | 13/43 |
| socks5://67.207.92.87:1088 | US | 1306 | 9 | 77/132 |
| socks5://193.25.215.182:22222 | US | 800 | 9 | 112/133 |
| http://184.75.221.82:3118 | CA | 373 | 8 | 86/98 |
| http://121.46.226.221:10808 | CN | 4535 | 7 | 9/10 |
| http://147.45.164.178:8888 | RU | 1544 | 7 | 7/7 |
| http://13.215.184.250:3128 | SG | 5026 | 7 | 11/19 |
| http://152.42.177.32:8888 | SG | 1037 | 7 | 57/93 |
| socks5://45.61.129.165:9050 | US | 3041 | 7 | 100/133 |
| http://123.121.142.252:8888 | CN | 1687 | 6 | 27/55 |
| socks5://209.50.255.91:1080 | US | 342 | 6 | 26/50 |
| http://56.112.92.32:16486 | CA | 1676 | 5 | 7/18 |
| http://222.128.173.231:8888 | CN | 3268 | 5 | 41/101 |
| http://56.68.116.64:15932 | MY | 3630 | 5 | 15/73 |
| http://128.199.121.61:9090 | SG | 1071 | 5 | 43/53 |
| socks5://144.24.111.128:1088 | IN | 4180 | 5 | 100/133 |
| socks5://45.74.31.41:8941 | NL | 6644 | 5 | 5/5 |
| socks5://185.73.115.43:2080 | NL | 5986 | 5 | 7/9 |
| socks5://171.25.158.95:1080 | SE | 2890 | 5 | 40/48 |
| socks5://47.87.97.94:1080 | TH | 1471 | 5 | 8/9 |
| socks5://45.61.188.134:44499 | US | 483 | 5 | 42/100 |
| http://16.51.53.116:23517 | AU | 2865 | 4 | 14/49 |
| http://38.7.195.51:999 | CL | 4259 | 4 | 51/124 |
| http://102.244.78.61:8082 | CM | 1310 | 4 | 17/22 |
| http://102.244.78.61:8086 | CM | 1273 | 4 | 16/21 |
| http://102.244.78.61:8089 | CM | 1368 | 4 | 15/21 |
| http://190.12.150.244:999 | EC | 3788 | 4 | 94/129 |
| http://205.237.105.49:3129 | FR | 675 | 4 | 4/4 |
| http://198.244.254.77:3128 | GB | 3490 | 4 | 15/17 |
| http://176.111.37.5:39811 | HK | 2552 | 4 | 114/133 |
| http://51.16.4.39:1461 | IL | 4477 | 4 | 26/117 |
| http://101.32.94.127:8089 | JP | 5701 | 4 | 12/21 |
| http://47.129.130.0:9898 | SG | 2637 | 4 | 13/50 |
| http://54.255.249.161:10 | SG | 2875 | 4 | 33/117 |
| http://34.43.46.91:443 | US | 678 | 4 | 124/133 |
| socks5://173.249.24.121:1080 | FR | 1180 | 4 | 4/4 |
| socks5://43.156.154.226:12345 | SG | 2786 | 4 | 5/9 |
| http://38.7.195.53:999 | CL | 2726 | 3 | 45/132 |
| http://200.39.137.137:999 | CL | 5506 | 3 | 9/33 |
| http://102.244.78.61:8085 | CM | 1311 | 3 | 15/23 |
| http://102.244.78.61:8087 | CM | 1263 | 3 | 16/23 |
| http://114.244.221.178:8888 | CN | 2503 | 3 | 27/56 |
| http://123.119.177.72:8888 | CN | 3501 | 3 | 29/78 |
| http://123.121.123.115:8888 | CN | 2155 | 3 | 33/57 |
| http://18.157.159.247:13401 | DE | 2849 | 3 | 19/93 |
| http://31.76.127.171:3128 | DE | 3747 | 3 | 11/18 |
| http://38.57.65.195:999 | DO | 2519 | 3 | 6/18 |
| http://38.75.82.217:999 | DO | 3865 | 3 | 20/60 |
| http://41.128.77.76:1976 | EG | 3010 | 3 | 38/99 |
| http://45.140.165.128:40001 | FR | 7670 | 3 | 3/3 |
| http://45.125.64.215:443 | HK | 2770 | 3 | 3/3 |
| http://176.111.37.216:39811 | HK | 1202 | 3 | 106/133 |
| http://38.226.241.242:8080 | ID | 4314 | 3 | 23/121 |
| http://103.151.23.89:8082 | ID | 7767 | 3 | 11/31 |
| http://103.171.183.148:7777 | ID | 4750 | 3 | 22/125 |
| http://103.184.180.2:1111 | ID | 6274 | 3 | 15/75 |
| http://160.191.56.1:8082 | ID | 1403 | 3 | 27/79 |
| http://163.223.78.125:8080 | ID | 3073 | 3 | 11/21 |
| http://223.25.110.76:3125 | ID | 4028 | 3 | 9/39 |
| http://13.208.246.143:46557 | JP | 3241 | 3 | 21/93 |
| http://140.238.32.108:3128 | JP | 2414 | 3 | 66/132 |
| http://31.192.248.55:8080 | KG | 7722 | 3 | 26/101 |
| http://38.252.145.15:999 | MX | 6698 | 3 | 7/33 |
| http://189.51.168.165:999 | MX | 389 | 3 | 41/45 |
| http://180.191.121.220:8181 | PH | 3821 | 3 | 3/3 |
| http://1.20.101.19:8080 | TH | 1490 | 3 | 8/19 |
| http://18.222.28.236:1256 | US | 4643 | 3 | 4/5 |
| http://34.43.46.91:80 | US | 693 | 3 | 127/133 |
| http://154.59.56.73:999 | VE | 2982 | 3 | 77/105 |
| http://161.22.32.31:8080 | VE | 5594 | 3 | 7/11 |
| http://116.104.251.199:2080 | VN | 2364 | 3 | 4/6 |
| http://16.28.29.244:44017 | ZA | 5643 | 3 | 22/97 |
| http://16.28.29.244:4744 | ZA | 2792 | 3 | 8/47 |
