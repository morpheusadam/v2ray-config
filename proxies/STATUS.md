# Proxy status

Generated 2026-11-18T21:21:09Z by `harvest.py`.

- **1321** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3514** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **28943** endpoints on record
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
| http | 2744 |
| socks5 | 750 |
| socks4 | 20 |

| country | entries |
|---|---|
| ID | 857 |
| NL | 489 |
| ?? | 227 |
| PH | 163 |
| CO | 126 |
| MX | 123 |
| US | 118 |
| TR | 89 |
| VE | 88 |
| IN | 77 |
| TH | 77 |
| RU | 73 |
| BR | 71 |
| BD | 65 |
| EC | 52 |
| AR | 51 |
| VN | 50 |
| CN | 45 |
| DO | 43 |
| DE | 33 |
| EG | 33 |
| ZA | 30 |
| LY | 28 |
| SG | 28 |
| PK | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 5 | 2026-11-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 83 | 83 | 17 | 2026-11-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 36 | 2026-11-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 67 | 2026-11-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 210 | 210 | 56 | 2026-11-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 273 | 273 | 24 | 2026-11-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 299 | 299 | 192 | 2026-11-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 309 | 309 | 79 | 2026-11-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 498 | 498 | 76 | 2026-11-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-11-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1130 | 2026-11-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1742 | 1742 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2211 | 2211 | 444 | 2026-11-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2313 | 2313 | 717 | 2026-11-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2553 | 2553 | 1480 | 2026-11-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5523 | 5523 | 4318 | 2026-11-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11561 | 11561 | 1855 | 2026-11-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1081 | 70 | 180/199 |
| http://130.110.103.245:3128 | SA | 1412 | 45 | 181/199 |
| http://38.180.18.103:3128 | BE | 838 | 28 | 28/28 |
| http://27.147.155.206:12051 | BD | 2135 | 19 | 19/19 |
| http://177.234.217.235:999 | EC | 4344 | 13 | 89/168 |
| http://141.94.22.37:3128 | FR | 851 | 11 | 14/15 |
| socks5://37.18.73.60:5566 | RU | 1938 | 11 | 47/96 |
| http://45.65.138.48:999 | CO | 3908 | 9 | 99/199 |
| socks5://107.174.30.92:1080 | US | 4904 | 9 | 55/95 |
| http://102.244.78.61:8084 | CM | 1388 | 8 | 68/87 |
| http://102.244.78.61:8089 | CM | 1422 | 8 | 71/87 |
| http://45.155.226.177:3128 | HK | 1015 | 8 | 13/15 |
| http://102.244.78.61:8080 | CM | 1380 | 7 | 72/88 |
| http://102.244.78.61:8088 | CM | 1387 | 7 | 69/87 |
| http://102.244.78.61:8081 | CM | 1416 | 6 | 69/85 |
| http://102.244.78.61:8082 | CM | 1393 | 6 | 70/88 |
| http://102.244.78.61:8085 | CM | 1409 | 6 | 70/89 |
| http://102.244.78.61:8087 | CM | 1422 | 6 | 67/89 |
| http://102.244.78.61:8090 | CM | 1411 | 6 | 73/91 |
| http://177.234.217.89:999 | EC | 5261 | 6 | 14/24 |
| http://43.165.169.48:80 | JP | 2244 | 6 | 11/16 |
| http://4.144.146.21:80 | SG | 893 | 6 | 82/91 |
| http://167.99.74.174:9090 | SG | 891 | 6 | 106/159 |
| http://216.152.149.246:80 | US | 4070 | 6 | 10/11 |
| http://15.229.149.81:3128 | BR | 3352 | 5 | 71/109 |
| http://35.43.85.195:443 | ES | 1071 | 5 | 12/15 |
| http://43.161.254.16:3128 | HK | 780 | 5 | 33/39 |
| http://52.128.238.98:18080 | HK | 100 | 5 | 10/14 |
| http://103.156.75.89:1717 | ID | 2810 | 5 | 12/23 |
| http://185.238.236.226:58080 | PL | 4397 | 5 | 58/121 |
| http://128.199.121.61:9090 | SG | 895 | 5 | 92/119 |
| http://216.152.152.44:80 | US | 4845 | 5 | 8/11 |
| socks5://193.25.215.182:22222 | US | 398 | 5 | 164/199 |
| http://77.242.21.133:8080 | AL | 4401 | 4 | 20/111 |
| http://201.28.86.18:61804 | BR | 4041 | 4 | 16/20 |
| http://184.75.221.82:3118 | CA | 535 | 4 | 142/164 |
| http://103.130.61.61:8081 | ID | 4732 | 4 | 164/199 |
| http://103.203.234.105:3127 | ID | 1233 | 4 | 9/28 |
| http://192.147.114.23:3127 | ID | 3554 | 4 | 39/133 |
| http://192.232.48.21:8181 | ID | 1553 | 4 | 19/105 |
| http://180.191.142.241:8081 | PH | 7469 | 4 | 11/38 |
| http://146.190.80.158:9090 | SG | 889 | 4 | 89/125 |
| http://34.43.46.91:443 | US | 3425 | 4 | 184/199 |
| http://34.43.46.91:80 | US | 2939 | 4 | 192/199 |
| http://161.22.32.31:8080 | VE | 4855 | 4 | 41/77 |
| http://154.3.76.16:999 | ?? | 786 | 4 | 6/7 |
| http://195.154.176.34:3128 | ?? | 909 | 4 | 4/4 |
| socks5://45.61.129.165:9050 | US | 1335 | 4 | 151/199 |
| socks5://46.246.12.31:1080 | ?? | 3301 | 4 | 4/4 |
| http://185.196.182.22:8080 | AL | 7151 | 3 | 45/178 |
| http://187.102.219.42:999 | AR | 1742 | 3 | 109/194 |
| http://190.123.83.137:999 | AR | 4662 | 3 | 30/36 |
| http://103.92.218.121:9514 | BD | 5543 | 3 | 32/135 |
| http://15.229.149.81:1080 | BR | 2074 | 3 | 55/101 |
| http://187.86.161.2:8080 | BR | 6139 | 3 | 20/35 |
| http://38.199.66.11:999 | CO | 4833 | 3 | 28/106 |
| http://91.107.186.23:8081 | DE | 3281 | 3 | 8/25 |
| http://177.234.217.93:999 | EC | 3636 | 3 | 41/58 |
| http://43.155.62.157:443 | HK | 797 | 3 | 86/102 |
| http://36.50.56.237:8080 | ID | 4067 | 3 | 26/106 |
| http://103.20.191.118:8080 | ID | 3975 | 3 | 48/164 |
| http://103.90.27.98:8080 | ID | 5961 | 3 | 10/29 |
| http://103.98.117.26:8080 | ID | 4048 | 3 | 13/33 |
| http://103.124.137.171:8080 | ID | 4347 | 3 | 32/141 |
| http://103.155.198.163:8080 | ID | 3718 | 3 | 27/141 |
| http://103.156.75.215:9980 | ID | 4167 | 3 | 14/91 |
| http://103.158.127.17:57413 | ID | 4010 | 3 | 43/177 |
| http://103.166.158.193:1080 | ID | 7077 | 3 | 35/122 |
| http://103.172.120.94:8080 | ID | 6691 | 3 | 29/172 |
| http://103.176.96.225:8082 | ID | 4271 | 3 | 49/144 |
| http://103.231.236.217:8182 | ID | 2156 | 3 | 8/22 |
| http://121.101.133.96:8080 | ID | 6440 | 3 | 27/107 |
| http://154.19.39.220:8090 | ID | 5891 | 3 | 19/105 |
| http://157.66.16.63:8181 | ID | 4509 | 3 | 7/28 |
| http://160.22.198.17:8082 | ID | 4336 | 3 | 52/191 |
| http://160.22.206.154:8082 | ID | 3061 | 3 | 31/100 |
| http://163.61.112.245:8080 | ID | 5725 | 3 | 6/29 |
| http://203.175.103.9:3125 | ID | 3003 | 3 | 22/99 |
| http://103.48.69.25:83 | IN | 4253 | 3 | 6/22 |
| http://185.166.27.208:2020 | IQ | 5351 | 3 | 23/33 |
| http://45.188.125.235:9991 | MX | 5314 | 3 | 32/175 |
| http://89.42.71.98:8097 | MX | 5858 | 3 | 14/75 |
| http://187.251.224.167:80 | MX | 6265 | 3 | 58/195 |
| http://189.51.168.164:999 | MX | 1330 | 3 | 31/35 |
| http://189.51.168.165:999 | MX | 3760 | 3 | 100/111 |
| http://218.100.23.130:8080 | NZ | 5081 | 3 | 28/96 |
| http://49.149.24.144:8082 | PH | 5928 | 3 | 18/38 |
| http://49.157.158.178:8084 | PH | 4061 | 3 | 28/168 |
| http://58.69.61.79:8082 | PH | 4176 | 3 | 25/100 |
| http://103.239.201.50:1 | PH | 6185 | 3 | 8/28 |
| http://119.93.178.99:8081 | PH | 6072 | 3 | 12/105 |
| http://67.206.213.202:3120 | PR | 6108 | 3 | 29/112 |
| http://31.57.178.195:8080 | SG | 7266 | 3 | 7/26 |
| http://104.248.151.93:9090 | SG | 3846 | 3 | 68/100 |
| http://128.199.116.219:9090 | SG | 901 | 3 | 92/118 |
| http://203.146.80.235:8080 | TH | 3786 | 3 | 20/106 |
| http://195.87.136.2:5331 | TR | 7520 | 3 | 5/20 |
| http://38.41.0.87:999 | VE | 7538 | 3 | 30/112 |
| http://20.98.234.24:8080 | ?? | 364 | 3 | 3/3 |
| http://132.243.174.245:5002 | ?? | 5359 | 3 | 3/3 |
