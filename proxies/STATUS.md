# Proxy status

Generated 2026-11-14T23:22:27Z by `harvest.py`.

- **1797** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3525** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34363** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 138/600 (23%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2724 |
| socks5 | 790 |
| socks4 | 11 |

| country | entries |
|---|---|
| ID | 835 |
| NL | 583 |
| PH | 144 |
| US | 138 |
| CO | 129 |
| ?? | 121 |
| MX | 115 |
| CN | 91 |
| TH | 89 |
| BR | 87 |
| VE | 74 |
| IN | 72 |
| TR | 69 |
| RU | 62 |
| BD | 59 |
| AR | 53 |
| EC | 49 |
| DO | 46 |
| VN | 45 |
| PE | 37 |
| PK | 36 |
| ZA | 32 |
| SG | 31 |
| CA | 30 |
| DE | 28 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 3 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 94 | 94 | 12 | 2026-11-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 83 | 2026-11-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 118 | 118 | 25 | 2026-11-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 53 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 212 | 212 | 54 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 235 | 235 | 68 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 286 | 286 | 185 | 2026-11-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 292 | 292 | 34 | 2026-11-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 450 | 2026-11-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 647 | 647 | 92 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1132 | 2026-11-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1701 | 1701 | 267 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1776 | 1776 | 364 | 2026-11-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1932 | 1932 | 662 | 2026-11-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2125 | 2125 | 1318 | 2026-11-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5371 | 5371 | 4132 | 2026-11-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10828 | 10828 | 1854 | 2026-11-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 1955 | 63 | 173/192 |
| http://34.43.46.91:80 | US | 1585 | 62 | 186/192 |
| http://130.110.103.245:3128 | SA | 2526 | 38 | 174/192 |
| http://45.189.57.114:3129 | EC | 748 | 34 | 34/34 |
| http://45.186.6.104:3128 | EC | 712 | 22 | 161/170 |
| http://38.180.18.103:3128 | BE | 908 | 21 | 21/21 |
| socks5://121.46.226.221:10808 | CN | 2967 | 18 | 18/18 |
| http://43.155.62.157:443 | HK | 1797 | 15 | 82/95 |
| http://27.147.155.206:12051 | BD | 1944 | 12 | 12/12 |
| http://51.85.44.162:31819 | IL | 4209 | 11 | 29/44 |
| http://140.238.32.108:3128 | JP | 1068 | 10 | 112/191 |
| http://167.172.76.176:9090 | SG | 1094 | 8 | 112/153 |
| http://123.121.73.146:8888 | CN | 1756 | 7 | 10/14 |
| http://185.166.27.208:2020 | IQ | 4549 | 7 | 19/26 |
| http://128.199.121.61:9090 | SG | 1078 | 7 | 86/112 |
| http://101.251.204.174:8080 | CN | 2007 | 6 | 99/178 |
| http://177.234.217.235:999 | EC | 1709 | 6 | 82/161 |
| http://119.12.161.248:3128 | HK | 969 | 6 | 6/6 |
| http://57.182.226.41:3128 | JP | 3451 | 6 | 6/6 |
| http://82.138.122.43:80 | TR | 2081 | 6 | 42/156 |
| http://104.129.203.85:9480 | US | 369 | 6 | 6/6 |
| socks5://45.194.33.12:30002 | HK | 2782 | 6 | 20/36 |
| http://114.249.209.219:8888 | CN | 2778 | 5 | 59/150 |
| http://24.152.58.101:999 | CO | 5022 | 5 | 27/86 |
| http://82.152.138.127:999 | MX | 3356 | 5 | 66/154 |
| http://58.69.124.137:8080 | PH | 4328 | 5 | 52/191 |
| http://146.190.80.158:9090 | SG | 1085 | 5 | 84/118 |
| socks5://82.180.146.251:10800 | IN | 1643 | 5 | 19/31 |
| socks5://188.226.27.24:1080 | RU | 2404 | 5 | 20/28 |
| http://45.175.59.17:61950 | BR | 7337 | 4 | 11/52 |
| http://45.226.130.66:3128 | BR | 1302 | 4 | 7/8 |
| http://35.183.29.62:8181 | CA | 3044 | 4 | 46/160 |
| http://123.121.102.115:8888 | CN | 1603 | 4 | 37/152 |
| http://123.121.123.216:8888 | CN | 2323 | 4 | 10/16 |
| http://221.221.144.98:8888 | CN | 3497 | 4 | 23/49 |
| http://45.65.137.218:999 | CO | 3157 | 4 | 74/157 |
| http://54.36.150.233:3128 | FR | 586 | 4 | 10/14 |
| http://141.94.22.37:3128 | FR | 570 | 4 | 7/8 |
| http://157.173.113.88:3128 | FR | 725 | 4 | 4/4 |
| http://103.120.174.75:1818 | ID | 4886 | 4 | 43/176 |
| http://34.100.244.79:80 | IN | 1473 | 4 | 4/4 |
| http://102.68.76.247:5566 | KE | 1470 | 4 | 56/145 |
| http://201.163.152.54:999 | MX | 3491 | 4 | 25/79 |
| http://124.105.86.222:8090 | PH | 4011 | 4 | 26/144 |
| http://185.238.238.21:58080 | PL | 6612 | 4 | 55/156 |
| http://185.238.238.29:58080 | PL | 6849 | 4 | 81/184 |
| http://185.238.238.49:58080 | PL | 1392 | 4 | 71/186 |
| http://45.177.16.131:999 | PY | 5029 | 4 | 46/188 |
| http://128.199.254.13:9090 | SG | 4782 | 4 | 75/121 |
| http://188.166.178.163:3129 | SG | 5805 | 4 | 4/4 |
| http://193.33.157.195:8080 | SY | 3243 | 4 | 6/22 |
| http://216.152.149.246:80 | US | 2133 | 4 | 4/4 |
| http://38.63.98.16:999 | VE | 5029 | 4 | 27/81 |
| http://200.59.191.27:999 | VE | 4708 | 4 | 127/187 |
| socks5://45.194.33.12:30001 | HK | 2537 | 4 | 22/68 |
| socks5://37.18.73.60:5566 | RU | 3156 | 4 | 40/89 |
| socks5://188.166.178.163:1088 | SG | 5850 | 4 | 4/4 |
| socks5://116.101.73.52:1057 | VN | 2158 | 4 | 4/4 |
| socks5://116.101.73.161:1057 | VN | 5202 | 4 | 4/4 |
| http://186.38.100.130:999 | AR | 6588 | 3 | 23/67 |
| http://187.102.219.34:999 | AR | 4532 | 3 | 83/143 |
| http://190.123.83.137:999 | AR | 4713 | 3 | 25/29 |
| http://16.26.208.68:18596 | AU | 4314 | 3 | 54/157 |
| http://15.229.149.81:1080 | BR | 2836 | 3 | 50/94 |
| http://201.28.86.18:61804 | BR | 2710 | 3 | 11/13 |
| http://111.192.19.3:8888 | CN | 2460 | 3 | 4/6 |
| http://111.192.61.254:8888 | CN | 3650 | 3 | 9/38 |
| http://186.194.161.201:999 | CO | 7017 | 3 | 10/48 |
| http://149.2.82.131:999 | DO | 5189 | 3 | 4/7 |
| http://154.88.164.160:999 | DO | 7224 | 3 | 12/25 |
| http://177.234.217.45:999 | EC | 1544 | 3 | 47/123 |
| http://177.234.217.83:999 | EC | 6110 | 3 | 29/39 |
| http://45.245.208.180:8080 | EG | 2016 | 3 | 44/65 |
| http://197.164.101.13:1976 | EG | 1777 | 3 | 10/26 |
| http://37.152.91.187:8080 | ES | 4279 | 3 | 7/24 |
| http://43.161.254.16:3128 | HK | 2395 | 3 | 28/32 |
| http://38.226.242.71:8080 | ID | 5757 | 3 | 38/131 |
| http://103.148.45.175:8080 | ID | 3880 | 3 | 6/18 |
| http://157.15.64.181:8080 | ID | 5965 | 3 | 6/23 |
| http://160.22.134.77:1111 | ID | 5630 | 3 | 20/98 |
| http://163.61.55.173:1111 | ID | 6447 | 3 | 17/65 |
| http://182.253.151.24:3128 | ID | 6184 | 3 | 4/5 |
| http://203.28.53.54:8090 | ID | 7030 | 3 | 7/14 |
| http://31.24.252.97:8080 | IQ | 7470 | 3 | 13/25 |
| http://203.81.69.126:1248 | MM | 4028 | 3 | 8/27 |
| http://170.78.208.32:999 | MX | 1611 | 3 | 16/60 |
| http://102.212.104.129:8082 | NG | 7761 | 3 | 7/22 |
| http://38.158.83.193:999 | PE | 6625 | 3 | 18/56 |
| http://180.191.52.90:5050 | PH | 4468 | 3 | 20/102 |
| http://152.42.170.187:9090 | SG | 1091 | 3 | 20/28 |
| http://103.136.250.154:8080 | TW | 4459 | 3 | 3/3 |
| http://152.70.198.2:1080 | US | 5365 | 3 | 40/112 |
| http://154.59.56.72:999 | VE | 4847 | 3 | 113/151 |
| http://181.233.161.50:999 | VE | 6223 | 3 | 43/170 |
| http://116.101.73.52:2095 | VN | 3708 | 3 | 3/3 |
| socks4://116.101.73.52:1082 | VN | 5913 | 3 | 6/7 |
| socks5://46.37.59.97:1080 | GB | 5542 | 3 | 4/6 |
| socks5://45.74.31.40:9830 | NL | 7070 | 3 | 17/97 |
| socks5://45.74.31.47:4474 | NL | 6579 | 3 | 7/17 |
| socks5://66.231.128.103:1080 | US | 3217 | 3 | 9/24 |
