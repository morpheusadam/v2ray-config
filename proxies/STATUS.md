# Proxy status

Generated 2026-11-20T21:13:26Z by `harvest.py`.

- **1450** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3605** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **27176** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 143/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3182 |
| socks5 | 422 |
| socks4 | 1 |

| country | entries |
|---|---|
| ID | 973 |
| ?? | 425 |
| NL | 162 |
| PH | 157 |
| MX | 147 |
| CO | 135 |
| US | 109 |
| TH | 99 |
| BR | 95 |
| TR | 93 |
| VE | 79 |
| BD | 76 |
| IN | 71 |
| RU | 68 |
| EC | 58 |
| AR | 51 |
| DO | 51 |
| CN | 39 |
| ZA | 39 |
| EG | 36 |
| PK | 34 |
| DE | 33 |
| SG | 32 |
| CL | 29 |
| PE | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 9 | 9 | 2 | 2026-11-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 35 | 35 | 1 | 2026-11-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 71 | 71 | 10 | 2026-11-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 71 | 71 | 10 | 2026-11-20 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 34 | 2026-11-20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 65 | 2026-11-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-20 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 249 | 249 | 32 | 2026-11-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 272 | 272 | 188 | 2026-11-20 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-20 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-20 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-20 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 663 | 663 | 115 | 2026-11-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1137 | 2026-11-20 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-20 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 2055 | 2055 | 0 | 2026-11-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2458 | 2458 | 252 | 2026-11-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2817 | 2817 | 673 | 2026-11-20 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3153 | 3153 | 1833 | 2026-11-20 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5601 | 5601 | 4331 | 2026-11-20 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12234 | 12234 | 2246 | 2026-11-20 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 2005 | 74 | 184/203 |
| http://130.110.103.245:3128 | SA | 1255 | 49 | 185/203 |
| http://27.147.155.206:12051 | BD | 4133 | 23 | 23/23 |
| http://141.94.22.37:3128 | FR | 497 | 15 | 18/19 |
| http://45.65.138.48:999 | CO | 6489 | 13 | 103/203 |
| http://45.155.226.177:3128 | HK | 2337 | 12 | 17/19 |
| http://102.244.78.61:8080 | CM | 1199 | 11 | 76/92 |
| http://102.244.78.61:8081 | CM | 1197 | 10 | 73/89 |
| http://4.144.146.21:80 | SG | 1161 | 10 | 86/95 |
| http://216.152.149.246:80 | US | 5854 | 10 | 14/15 |
| http://15.229.149.81:3128 | BR | 1727 | 9 | 75/113 |
| http://43.161.254.16:3128 | HK | 4020 | 9 | 37/43 |
| http://52.128.238.98:18080 | HK | 425 | 9 | 14/18 |
| http://185.238.236.226:58080 | PL | 1006 | 9 | 62/125 |
| http://128.199.121.61:9090 | SG | 1167 | 9 | 96/123 |
| socks5://193.25.215.182:22222 | US | 778 | 9 | 168/203 |
| http://103.130.61.61:8081 | ID | 4159 | 8 | 168/203 |
| http://34.43.46.91:443 | US | 2658 | 8 | 188/203 |
| http://34.43.46.91:80 | US | 3076 | 8 | 196/203 |
| socks5://45.61.129.165:9050 | US | 1517 | 8 | 155/203 |
| socks5://46.246.12.31:1080 | ?? | 2768 | 8 | 8/8 |
| http://15.229.149.81:1080 | BR | 1864 | 7 | 59/105 |
| http://43.155.62.157:443 | HK | 3130 | 7 | 90/106 |
| http://103.176.96.225:8082 | ID | 6626 | 7 | 53/148 |
| http://189.51.168.164:999 | MX | 3960 | 7 | 35/39 |
| http://189.51.168.165:999 | MX | 6347 | 7 | 104/115 |
| http://104.248.151.93:9090 | SG | 1174 | 7 | 72/104 |
| http://20.98.234.24:8080 | ?? | 81 | 7 | 7/7 |
| socks5://69.55.49.177:38182 | US | 350 | 7 | 47/58 |
| http://186.96.111.214:999 | CO | 470 | 6 | 98/192 |
| http://103.237.102.191:11111 | DE | 1538 | 6 | 190/203 |
| http://103.61.234.186:8180 | ID | 4242 | 6 | 91/200 |
| http://210.87.74.189:3125 | ID | 7598 | 6 | 11/27 |
| http://201.46.86.37:8080 | MX | 3705 | 6 | 13/37 |
| http://172.235.157.127:3128 | ?? | 926 | 6 | 6/6 |
| http://45.186.6.104:3128 | EC | 561 | 5 | 171/181 |
| http://49.213.59.105:8082 | ID | 7358 | 5 | 53/162 |
| http://103.133.26.50:8080 | ID | 1533 | 5 | 69/104 |
| http://103.133.26.72:8080 | ID | 1485 | 5 | 77/129 |
| http://103.133.26.73:3128 | ID | 1550 | 5 | 93/181 |
| http://103.133.26.119:8080 | ID | 1886 | 5 | 74/113 |
| http://103.158.210.80:8082 | ID | 3729 | 5 | 64/193 |
| http://110.74.195.34:25 | KH | 3942 | 5 | 67/196 |
| http://159.223.41.216:9090 | SG | 1162 | 5 | 119/163 |
| http://3.21.247.154:59330 | US | 1202 | 5 | 38/159 |
| http://68.183.226.190:9090 | ?? | 1157 | 5 | 7/11 |
| http://91.134.141.4:3128 | ?? | 494 | 5 | 5/5 |
| http://195.142.250.38:8080 | ?? | 1577 | 5 | 6/7 |
| socks5://103.119.1.160:5555 | HK | 3664 | 5 | 13/18 |
| socks5://45.61.188.134:44499 | US | 317 | 5 | 92/170 |
| socks5://103.124.172.134:1080 | ?? | 3429 | 5 | 5/5 |
| http://177.130.104.106:33333 | BR | 4530 | 4 | 9/28 |
| http://35.183.78.223:58093 | CA | 2356 | 4 | 34/101 |
| http://102.244.78.61:8083 | CM | 1178 | 4 | 73/91 |
| http://123.121.142.252:8888 | CN | 7287 | 4 | 55/125 |
| http://45.65.137.218:999 | CO | 1594 | 4 | 82/168 |
| http://200.10.29.73:999 | CO | 1697 | 4 | 26/103 |
| http://38.57.65.195:999 | DO | 2738 | 4 | 26/88 |
| http://181.78.195.136:999 | EC | 2828 | 4 | 33/59 |
| http://45.245.208.180:8080 | EG | 1055 | 4 | 52/76 |
| http://193.38.224.169:8081 | ES | 2746 | 4 | 18/73 |
| http://181.115.67.3:999 | HN | 4273 | 4 | 27/80 |
| http://38.226.241.242:8080 | ID | 7733 | 4 | 42/191 |
| http://103.86.117.23:8080 | ID | 5009 | 4 | 37/123 |
| http://103.144.54.35:8082 | ID | 7922 | 4 | 48/126 |
| http://103.216.104.6:1080 | ID | 7489 | 4 | 7/15 |
| http://103.217.173.142:8080 | ID | 2227 | 4 | 9/34 |
| http://175.111.96.154:3128 | ID | 6661 | 4 | 26/116 |
| http://198.15.30.198:3125 | ID | 4695 | 4 | 30/69 |
| http://185.142.156.203:80 | IR | 3869 | 4 | 32/68 |
| http://140.238.32.108:3128 | JP | 975 | 4 | 119/202 |
| http://41.209.57.199:80 | KE | 5480 | 4 | 28/112 |
| http://206.135.47.107:999 | MX | 2867 | 4 | 39/73 |
| http://126.209.53.149:8181 | PH | 5716 | 4 | 20/97 |
| http://185.238.238.49:58080 | PL | 1233 | 4 | 78/197 |
| http://185.238.238.169:58080 | PL | 1211 | 4 | 64/125 |
| http://43.159.54.178:80 | SG | 1145 | 4 | 51/123 |
| http://195.226.213.254:8888 | UA | 2909 | 4 | 74/201 |
| http://165.154.162.73:8888 | US | 3213 | 4 | 134/203 |
| http://154.59.56.76:999 | VE | 4415 | 4 | 117/163 |
| http://190.94.213.5:999 | VE | 4442 | 4 | 14/65 |
| http://181.79.89.140:999 | ?? | 5173 | 4 | 4/4 |
| http://190.112.193.64:999 | ?? | 4993 | 4 | 6/8 |
| http://217.142.139.207:8085 | ?? | 2747 | 4 | 5/6 |
| socks5://212.3.127.242:10801 | UA | 4140 | 4 | 45/194 |
| http://187.102.219.32:999 | AR | 1345 | 3 | 78/202 |
| http://45.115.114.41:2379 | BD | 6512 | 3 | 46/169 |
| http://123.253.145.165:8080 | BD | 4473 | 3 | 23/89 |
| http://38.76.228.240:8088 | BR | 3294 | 3 | 22/92 |
| http://179.48.25.1:8095 | BR | 1374 | 3 | 42/198 |
| http://123.115.226.82:8888 | CN | 1703 | 3 | 56/149 |
| http://45.167.125.217:999 | CO | 3823 | 3 | 19/79 |
| http://45.173.7.10:999 | CO | 4778 | 3 | 40/198 |
| http://200.10.30.5:8083 | CO | 2218 | 3 | 62/192 |
| http://63.180.203.233:37086 | DE | 2042 | 3 | 50/163 |
| http://177.234.217.42:999 | EC | 6147 | 3 | 37/100 |
| http://177.234.217.83:999 | EC | 1329 | 3 | 35/50 |
| http://200.24.138.73:999 | EC | 5912 | 3 | 10/67 |
| http://197.164.101.11:1976 | EG | 7868 | 3 | 3/3 |
| http://15.217.107.97:9675 | ES | 4527 | 3 | 25/102 |
