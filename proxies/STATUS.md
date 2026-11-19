# Proxy status

Generated 2026-11-19T21:22:43Z by `harvest.py`.

- **1869** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3796** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **28009** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 153/600 (26%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3231 |
| socks5 | 555 |
| socks4 | 10 |

| country | entries |
|---|---|
| ID | 1009 |
| ?? | 467 |
| NL | 341 |
| PH | 166 |
| CO | 134 |
| MX | 134 |
| US | 104 |
| BR | 92 |
| TH | 87 |
| VE | 83 |
| TR | 81 |
| IN | 73 |
| BD | 71 |
| RU | 63 |
| EC | 58 |
| AR | 53 |
| CN | 44 |
| VN | 44 |
| PK | 38 |
| DO | 35 |
| SG | 35 |
| EG | 33 |
| ZA | 30 |
| DE | 26 |
| PE | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 2 | 2 | 1 | 2026-11-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 96 | 96 | 19 | 2026-11-19 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 30 | 2026-11-19 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 73 | 2026-11-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 240 | 240 | 65 | 2026-11-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 338 | 338 | 38 | 2026-11-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 356 | 356 | 242 | 2026-11-19 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-19 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 407 | 407 | 105 | 2026-11-19 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-19 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 446 | 2026-11-19 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 781 | 781 | 179 | 2026-11-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1129 | 2026-11-19 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1772 | 1772 | 0 | 2026-11-19 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2080 | 2080 | 315 | 2026-11-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2350 | 2350 | 689 | 2026-11-19 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2860 | 2860 | 1615 | 2026-11-19 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5556 | 5556 | 4338 | 2026-11-19 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12163 | 12163 | 2274 | 2026-11-19 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1144 | 72 | 182/201 |
| http://130.110.103.245:3128 | SA | 1049 | 47 | 183/201 |
| http://27.147.155.206:12051 | BD | 1640 | 21 | 21/21 |
| http://141.94.22.37:3128 | FR | 498 | 13 | 16/17 |
| http://45.65.138.48:999 | CO | 2446 | 11 | 101/201 |
| http://102.244.78.61:8084 | CM | 1187 | 10 | 70/89 |
| http://102.244.78.61:8089 | CM | 1221 | 10 | 73/89 |
| http://45.155.226.177:3128 | HK | 2079 | 10 | 15/17 |
| http://102.244.78.61:8080 | CM | 1192 | 9 | 74/90 |
| http://102.244.78.61:8088 | CM | 1186 | 9 | 71/89 |
| http://102.244.78.61:8081 | CM | 1189 | 8 | 71/87 |
| http://102.244.78.61:8082 | CM | 1193 | 8 | 72/90 |
| http://102.244.78.61:8085 | CM | 1227 | 8 | 72/91 |
| http://102.244.78.61:8087 | CM | 1206 | 8 | 69/91 |
| http://102.244.78.61:8090 | CM | 1224 | 8 | 75/93 |
| http://43.165.169.48:80 | JP | 1287 | 8 | 13/18 |
| http://4.144.146.21:80 | SG | 1146 | 8 | 84/93 |
| http://216.152.149.246:80 | US | 2306 | 8 | 12/13 |
| http://15.229.149.81:3128 | BR | 2039 | 7 | 73/111 |
| http://43.161.254.16:3128 | HK | 1051 | 7 | 35/41 |
| http://52.128.238.98:18080 | HK | 366 | 7 | 12/16 |
| http://185.238.236.226:58080 | PL | 820 | 7 | 60/123 |
| http://128.199.121.61:9090 | SG | 1147 | 7 | 94/121 |
| http://216.152.152.44:80 | US | 747 | 7 | 10/13 |
| socks5://193.25.215.182:22222 | US | 971 | 7 | 166/201 |
| http://184.75.221.82:3118 | CA | 362 | 6 | 144/166 |
| http://103.130.61.61:8081 | ID | 1573 | 6 | 166/201 |
| http://192.232.48.21:8181 | ID | 2504 | 6 | 21/107 |
| http://34.43.46.91:443 | US | 3522 | 6 | 186/201 |
| http://34.43.46.91:80 | US | 4845 | 6 | 194/201 |
| http://161.22.32.31:8080 | VE | 2832 | 6 | 43/79 |
| socks5://45.61.129.165:9050 | US | 1587 | 6 | 153/201 |
| socks5://46.246.12.31:1080 | ?? | 2940 | 6 | 6/6 |
| http://190.123.83.137:999 | AR | 2092 | 5 | 32/38 |
| http://15.229.149.81:1080 | BR | 2832 | 5 | 57/103 |
| http://177.234.217.93:999 | EC | 1515 | 5 | 43/60 |
| http://43.155.62.157:443 | HK | 1282 | 5 | 88/104 |
| http://103.98.117.26:8080 | ID | 7013 | 5 | 15/35 |
| http://103.176.96.225:8082 | ID | 6533 | 5 | 51/146 |
| http://103.231.236.217:8182 | ID | 6973 | 5 | 10/24 |
| http://187.251.224.167:80 | MX | 1702 | 5 | 60/197 |
| http://189.51.168.164:999 | MX | 2153 | 5 | 33/37 |
| http://189.51.168.165:999 | MX | 865 | 5 | 102/113 |
| http://49.149.24.144:8082 | PH | 4666 | 5 | 20/40 |
| http://119.93.178.99:8081 | PH | 6615 | 5 | 14/107 |
| http://104.248.151.93:9090 | SG | 1144 | 5 | 70/102 |
| http://20.98.234.24:8080 | ?? | 97 | 5 | 5/5 |
| socks5://103.13.19.219:10808 | JP | 6133 | 5 | 11/18 |
| socks5://69.55.49.177:38182 | US | 364 | 5 | 45/56 |
| http://103.79.183.109:8080 | BD | 5243 | 4 | 25/58 |
| http://123.121.140.72:8888 | CN | 3249 | 4 | 31/53 |
| http://186.96.111.214:999 | CO | 463 | 4 | 96/190 |
| http://103.237.102.191:11111 | DE | 707 | 4 | 188/201 |
| http://51.94.221.175:1857 | ES | 1897 | 4 | 41/142 |
| http://198.244.254.77:3128 | GB | 2564 | 4 | 68/85 |
| http://36.95.245.7:8090 | ID | 7586 | 4 | 14/39 |
| http://103.61.234.186:8180 | ID | 3628 | 4 | 89/198 |
| http://103.132.54.42:8080 | ID | 4610 | 4 | 30/110 |
| http://210.87.74.189:3125 | ID | 4509 | 4 | 9/25 |
| http://51.85.44.162:31819 | IL | 1158 | 4 | 33/53 |
| http://36.37.251.137:8080 | KH | 7087 | 4 | 19/87 |
| http://201.46.86.37:8080 | MX | 3809 | 4 | 11/35 |
| http://206.135.76.38:8080 | MX | 489 | 4 | 14/29 |
| http://49.146.48.103:8082 | PH | 6160 | 4 | 21/39 |
| http://56.228.13.15:443 | SE | 923 | 4 | 44/115 |
| http://152.70.198.2:1080 | US | 207 | 4 | 44/121 |
| http://90.156.160.234:3128 | UZ | 3201 | 4 | 40/89 |
| http://200.59.191.27:999 | VE | 4354 | 4 | 134/196 |
| http://45.163.199.227:8083 | ?? | 4124 | 4 | 5/6 |
| http://172.235.157.127:3128 | ?? | 1070 | 4 | 4/4 |
| http://210.213.119.28:3128 | ?? | 2235 | 4 | 4/4 |
| socks5://65.21.252.66:10805 | FI | 2361 | 4 | 58/115 |
| socks5://45.194.33.12:30001 | HK | 1779 | 4 | 28/77 |
| socks5://45.194.33.12:30002 | HK | 4373 | 4 | 27/45 |
| socks5://203.189.135.140:1080 | KH | 2834 | 4 | 18/64 |
| http://168.194.34.196:9001 | AR | 4140 | 3 | 78/199 |
| http://181.209.107.154:999 | AR | 5936 | 3 | 14/65 |
| http://187.102.219.64:999 | AR | 1111 | 3 | 84/140 |
| http://103.113.152.73:14158 | BD | 2268 | 3 | 51/195 |
| http://103.150.49.90:8090 | BD | 4803 | 3 | 44/194 |
| http://218.207.164.174:7890 | CN | 2569 | 3 | 33/123 |
| http://190.60.47.61:999 | CO | 7325 | 3 | 6/39 |
| http://200.10.31.42:8081 | CO | 2580 | 3 | 35/74 |
| http://2.28.105.45:8888 | DE | 2931 | 3 | 27/102 |
| http://154.59.206.32:999 | DO | 4627 | 3 | 20/51 |
| http://45.186.6.104:3128 | EC | 623 | 3 | 169/179 |
| http://177.234.226.83:1994 | EC | 4375 | 3 | 35/159 |
| http://190.12.150.244:999 | EC | 2098 | 3 | 145/197 |
| http://197.164.101.10:1981 | EG | 5043 | 3 | 8/28 |
| http://197.164.101.11:1981 | EG | 4359 | 3 | 5/18 |
| http://77.42.95.221:8888 | FI | 986 | 3 | 14/74 |
| http://18.163.182.106:18452 | HK | 3898 | 3 | 41/168 |
| http://41.216.190.241:8043 | ID | 3513 | 3 | 12/41 |
| http://43.241.247.43:8080 | ID | 4719 | 3 | 36/135 |
| http://45.198.11.193:8282 | ID | 1478 | 3 | 8/18 |
| http://49.213.59.105:8082 | ID | 5082 | 3 | 51/160 |
| http://101.255.209.158:8181 | ID | 3277 | 3 | 7/25 |
| http://103.4.76.237:1111 | ID | 6783 | 3 | 31/198 |
| http://103.18.79.197:8085 | ID | 2152 | 3 | 46/137 |
| http://103.66.47.9:8080 | ID | 7915 | 3 | 14/35 |
