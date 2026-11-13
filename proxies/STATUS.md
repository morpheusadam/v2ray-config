# Proxy status

Generated 2026-11-13T00:40:30Z by `harvest.py`.

- **1379** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4098** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **35184** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 128/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3176 |
| socks5 | 905 |
| socks4 | 17 |

| country | entries |
|---|---|
| ID | 919 |
| NL | 722 |
| ?? | 400 |
| PH | 148 |
| US | 145 |
| MX | 128 |
| CO | 121 |
| CN | 96 |
| TH | 96 |
| BR | 82 |
| TR | 82 |
| VE | 76 |
| BD | 74 |
| IN | 64 |
| EC | 62 |
| AR | 61 |
| RU | 49 |
| DO | 43 |
| PK | 41 |
| PE | 39 |
| VN | 37 |
| EG | 34 |
| DE | 31 |
| ZA | 31 |
| SG | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 2 | 2026-11-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 97 | 97 | 13 | 2026-11-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 141 | 141 | 20 | 2026-11-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 41 | 2026-11-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 63 | 2026-11-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 161 | 161 | 59 | 2026-11-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 210 | 210 | 36 | 2026-11-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 425 | 425 | 285 | 2026-11-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 547 | 547 | 90 | 2026-11-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 442 | 2026-11-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1135 | 2026-11-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1579 | 2026-11-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1955 | 1955 | 293 | 2026-11-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2280 | 2280 | 401 | 2026-11-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2327 | 2327 | 672 | 2026-11-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2645 | 2645 | 1507 | 2026-11-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5274 | 5274 | 3986 | 2026-11-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11874 | 11874 | 1949 | 2026-11-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1312 | 64 | 84/166 |
| http://176.111.37.5:39811 | HK | 1610 | 59 | 169/188 |
| http://34.43.46.91:80 | US | 3929 | 58 | 182/188 |
| http://4.144.146.21:80 | SG | 976 | 56 | 73/80 |
| http://176.111.37.216:39811 | HK | 2645 | 51 | 160/188 |
| http://130.110.103.245:3128 | SA | 1457 | 34 | 170/188 |
| http://103.133.26.72:8080 | ID | 1312 | 31 | 68/114 |
| http://45.189.57.114:3129 | EC | 1254 | 30 | 30/30 |
| http://189.51.168.164:999 | MX | 1102 | 24 | 24/24 |
| http://49.229.100.235:8080 | TH | 1287 | 24 | 96/136 |
| http://171.100.254.137:8080 | TH | 1281 | 24 | 24/24 |
| http://43.161.254.16:3128 | HK | 2238 | 23 | 25/28 |
| http://103.130.61.61:8081 | ID | 4314 | 23 | 157/188 |
| http://45.186.6.104:3128 | EC | 715 | 18 | 157/166 |
| http://38.180.18.103:3128 | BE | 776 | 17 | 17/17 |
| http://190.71.72.85:2525 | CO | 666 | 16 | 32/73 |
| http://102.244.78.61:8090 | CM | 1519 | 15 | 64/80 |
| socks5://121.46.226.221:10808 | CN | 1928 | 14 | 14/14 |
| http://103.237.102.191:11111 | DE | 1305 | 11 | 179/188 |
| http://43.155.62.157:443 | HK | 826 | 11 | 78/91 |
| http://15.223.187.219:35507 | CA | 2391 | 9 | 27/101 |
| http://185.191.239.248:3128 | CH | 1715 | 9 | 137/187 |
| http://61.91.162.126:8080 | TH | 1413 | 9 | 100/131 |
| http://103.10.231.189:8080 | TH | 1720 | 9 | 127/173 |
| http://27.147.155.206:12051 | BD | 1682 | 8 | 8/8 |
| http://43.128.144.133:18080 | KR | 1777 | 8 | 8/8 |
| http://51.85.44.162:31819 | IL | 1841 | 7 | 25/40 |
| http://38.41.0.60:11201 | VE | 6436 | 7 | 44/114 |
| http://45.65.224.74:999 | AR | 7113 | 6 | 44/53 |
| http://177.234.217.83:999 | EC | 6332 | 6 | 26/35 |
| http://103.199.117.121:7777 | ID | 6124 | 6 | 13/22 |
| http://140.238.32.108:3128 | JP | 1923 | 6 | 108/187 |
| http://144.124.251.24:10574 | NL | 779 | 6 | 80/137 |
| http://144.124.251.24:10605 | NL | 936 | 6 | 75/120 |
| http://144.124.251.24:11266 | NL | 820 | 6 | 77/120 |
| http://16.51.5.77:16637 | AU | 6219 | 5 | 34/128 |
| http://111.196.24.150:8888 | CN | 5131 | 5 | 21/38 |
| http://111.196.30.74:8888 | CN | 1978 | 5 | 19/37 |
| http://123.121.122.125:8888 | CN | 3323 | 5 | 8/11 |
| http://43.99.60.244:8089 | HK | 1057 | 5 | 72/138 |
| http://144.124.251.24:10566 | NL | 788 | 5 | 77/121 |
| http://167.99.74.174:9090 | SG | 963 | 5 | 98/148 |
| http://180.191.232.182:3128 | ?? | 6726 | 5 | 5/5 |
| http://187.102.219.34:999 | AR | 1673 | 4 | 80/139 |
| http://200.49.99.78:9991 | AR | 5919 | 4 | 7/18 |
| http://201.28.86.18:61804 | BR | 6952 | 4 | 8/9 |
| http://114.244.221.178:8888 | CN | 2762 | 4 | 57/111 |
| http://123.121.101.115:8888 | CN | 2317 | 4 | 7/9 |
| http://181.205.204.19:999 | CO | 7209 | 4 | 13/61 |
| http://38.76.251.244:999 | DO | 3521 | 4 | 5/6 |
| http://103.20.191.118:8080 | ID | 3541 | 4 | 44/153 |
| http://103.133.26.50:8080 | ID | 1261 | 4 | 60/89 |
| http://103.148.44.139:8080 | ID | 4641 | 4 | 11/27 |
| http://157.66.36.86:8080 | ID | 7128 | 4 | 5/6 |
| http://202.62.57.235:8080 | KH | 7365 | 4 | 28/137 |
| http://38.210.179.25:999 | MX | 5532 | 4 | 18/54 |
| http://206.135.47.108:999 | MX | 2841 | 4 | 29/56 |
| http://144.124.251.24:10658 | NL | 848 | 4 | 72/120 |
| http://144.124.251.24:10819 | NL | 1102 | 4 | 16/58 |
| http://144.124.251.24:11011 | NL | 816 | 4 | 73/120 |
| http://180.191.137.111:8082 | PH | 4341 | 4 | 44/172 |
| http://185.238.238.165:58080 | PL | 6584 | 4 | 41/78 |
| http://128.199.116.219:9090 | SG | 943 | 4 | 83/107 |
| http://167.172.76.176:9090 | SG | 954 | 4 | 108/149 |
| http://23.177.184.175:3128 | US | 723 | 4 | 21/40 |
| http://38.51.220.64:999 | VE | 7780 | 4 | 37/165 |
| http://38.76.9.1:999 | VE | 3114 | 4 | 27/51 |
| http://154.59.56.72:999 | VE | 7642 | 4 | 110/147 |
| http://154.59.56.74:999 | VE | 4719 | 4 | 103/151 |
| http://13.245.161.189:51292 | ZA | 3007 | 4 | 38/148 |
| http://20.249.202.171:443 | ?? | 739 | 4 | 4/4 |
| http://35.43.85.195:443 | ?? | 2818 | 4 | 4/4 |
| http://42.96.18.62:1311 | ?? | 1532 | 4 | 4/4 |
| http://45.155.226.177:3128 | ?? | 686 | 4 | 4/4 |
| http://103.152.238.39:1080 | ?? | 5611 | 4 | 7/13 |
| http://123.121.125.219:8888 | ?? | 1625 | 4 | 4/4 |
| socks5://143.198.239.45:10020 | US | 2023 | 4 | 8/10 |
| socks5://143.198.239.45:10046 | US | 4577 | 4 | 4/4 |
| http://190.109.126.44:1010 | AR | 3814 | 3 | 16/127 |
| http://16.176.232.186:1222 | AU | 2423 | 3 | 38/104 |
| http://85.132.108.42:3128 | AZ | 1505 | 3 | 5/6 |
| http://83.143.24.66:80 | BW | 4463 | 3 | 35/134 |
| http://179.57.172.172:999 | CL | 5609 | 3 | 34/187 |
| http://102.244.78.61:8085 | CM | 1447 | 3 | 61/78 |
| http://102.244.78.61:8088 | CM | 1438 | 3 | 60/76 |
| http://114.252.202.38:8888 | CN | 2083 | 3 | 13/23 |
| http://123.121.73.146:8888 | CN | 1709 | 3 | 6/10 |
| http://125.33.195.27:8888 | CN | 5787 | 3 | 54/134 |
| http://38.211.76.65:999 | CO | 3708 | 3 | 25/109 |
| http://190.60.60.37:8080 | CO | 7408 | 3 | 9/60 |
| http://204.199.106.226:999 | CO | 3561 | 3 | 10/11 |
| http://45.224.22.63:999 | EC | 3181 | 3 | 25/116 |
| http://194.31.107.138:3128 | EC | 3805 | 3 | 8/14 |
| http://197.164.101.14:1981 | EG | 4035 | 3 | 44/158 |
| http://15.217.107.97:9675 | ES | 5778 | 3 | 19/87 |
| http://198.244.254.77:3128 | GB | 2933 | 3 | 60/72 |
| http://38.199.88.1:999 | GT | 3571 | 3 | 5/8 |
| http://15.232.45.244:3127 | ID | 3928 | 3 | 41/148 |
| http://38.183.146.25:8090 | ID | 6455 | 3 | 9/28 |
| http://103.122.64.156:8080 | ID | 3639 | 3 | 30/130 |
