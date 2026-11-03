# Proxy status

Generated 2026-11-03T20:17:08Z by `harvest.py`.

- **3097** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5627** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34690** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 208/600 (35%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 3117 |
| socks5 | 2493 |
| socks4 | 17 |

| country | entries |
|---|---|
| NL | 2228 |
| ID | 878 |
| ?? | 438 |
| PH | 144 |
| CO | 133 |
| US | 127 |
| MX | 122 |
| VN | 100 |
| TH | 97 |
| VE | 94 |
| TR | 76 |
| BR | 72 |
| RU | 72 |
| BD | 67 |
| CN | 59 |
| IN | 59 |
| AR | 57 |
| EC | 57 |
| DO | 52 |
| PE | 47 |
| EG | 40 |
| DE | 38 |
| SG | 32 |
| ZA | 30 |
| PK | 29 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 3 | 2026-11-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-11-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 48 | 2026-11-03 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 82 | 2026-11-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 156 | 156 | 33 | 2026-11-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 204 | 204 | 41 | 2026-11-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 316 | 316 | 178 | 2026-11-03 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-03 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-03 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 567 | 567 | 176 | 2026-11-03 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-11-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 1140 | 1140 | 272 | 2026-11-03 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1389 | 1389 | 681 | 2026-11-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1129 | 2026-11-03 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1583 | 2026-11-03 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1837 | 1837 | 363 | 2026-11-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2272 | 2272 | 655 | 2026-11-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2896 | 2896 | 1627 | 2026-11-03 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3120 | 3120 | 935 | 2026-11-03 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4961 | 4961 | 3699 | 2026-11-03 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11464 | 11463 | 2568 | 2026-11-03 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://149.130.173.58:9443 | CO | 445 | 80 | 80/80 |
| http://103.237.102.191:11111 | DE | 737 | 56 | 162/169 |
| http://103.133.26.73:3128 | ID | 1566 | 45 | 65/147 |
| http://176.111.37.5:39811 | HK | 804 | 40 | 150/169 |
| http://34.43.46.91:80 | US | 605 | 39 | 163/169 |
| http://4.144.146.21:80 | SG | 1151 | 37 | 54/61 |
| http://176.111.37.216:39811 | HK | 1664 | 32 | 141/169 |
| http://34.43.46.91:443 | US | 379 | 18 | 158/169 |
| http://167.172.76.176:9090 | SG | 1160 | 16 | 93/130 |
| socks5://101.36.104.239:10808 | JP | 2023 | 16 | 145/169 |
| http://130.110.103.245:3128 | SA | 1246 | 15 | 151/169 |
| socks5://45.61.188.134:44499 | US | 3155 | 15 | 71/136 |
| socks5://193.25.215.182:22222 | US | 998 | 15 | 142/169 |
| http://103.133.26.72:8080 | ID | 3134 | 12 | 49/95 |
| http://45.189.57.114:3129 | EC | 1395 | 11 | 11/11 |
| http://154.59.56.78:999 | VE | 3914 | 11 | 88/125 |
| http://102.244.78.61:8085 | CM | 3762 | 10 | 47/59 |
| http://102.244.78.61:8087 | CM | 4567 | 10 | 46/59 |
| http://102.244.78.61:8090 | CM | 4041 | 9 | 47/61 |
| http://130.127.204.197:8080 | US | 126 | 9 | 9/9 |
| http://38.172.160.16:999 | VE | 1748 | 9 | 72/120 |
| http://200.59.191.27:999 | VE | 2732 | 9 | 113/164 |
| http://45.65.224.74:999 | AR | 1970 | 8 | 27/34 |
| http://123.200.8.170:10000 | BD | 5119 | 8 | 75/167 |
| http://102.244.78.61:8082 | CM | 5170 | 8 | 47/58 |
| http://190.12.150.244:999 | EC | 1110 | 8 | 121/165 |
| http://185.238.238.49:58080 | PL | 7801 | 8 | 57/163 |
| http://154.59.56.72:999 | VE | 2048 | 8 | 95/128 |
| socks5://69.55.49.177:38182 | US | 2076 | 8 | 23/24 |
| http://187.102.219.32:999 | AR | 1396 | 7 | 58/168 |
| http://186.96.111.214:999 | CO | 5654 | 7 | 77/158 |
| http://45.186.6.104:3128 | EC | 598 | 7 | 139/147 |
| http://195.226.213.251:8888 | UA | 3889 | 7 | 67/163 |
| http://165.154.162.73:8888 | US | 723 | 7 | 112/169 |
| socks5://45.61.129.165:9050 | US | 1395 | 7 | 128/169 |
| http://38.19.213.80:999 | CO | 4085 | 6 | 7/8 |
| http://190.0.246.213:4040 | CO | 584 | 6 | 124/134 |
| http://43.155.62.157:443 | HK | 1042 | 6 | 62/72 |
| http://45.198.11.183:9191 | ID | 4333 | 6 | 15/50 |
| http://160.22.207.95:8082 | ID | 3303 | 6 | 40/147 |
| http://189.51.168.165:999 | MX | 1805 | 6 | 75/81 |
| http://206.135.47.107:999 | MX | 5039 | 6 | 21/39 |
| http://154.59.56.74:999 | VE | 2197 | 6 | 89/132 |
| http://190.123.83.137:999 | ?? | 1115 | 6 | 6/6 |
| socks5://101.36.104.46:10808 | JP | 2123 | 6 | 145/169 |
| http://128.201.30.222:8666 | BR | 4099 | 5 | 8/15 |
| http://8.243.167.51:999 | CO | 4202 | 5 | 15/56 |
| http://45.65.137.218:999 | CO | 2474 | 5 | 57/134 |
| http://131.221.40.131:4040 | CO | 577 | 5 | 7/8 |
| http://177.234.217.83:999 | EC | 4017 | 5 | 12/16 |
| http://177.234.217.92:999 | EC | 3773 | 5 | 13/18 |
| http://37.187.109.70:10111 | FR | 7431 | 5 | 58/169 |
| http://103.133.26.119:8080 | ID | 2007 | 5 | 48/79 |
| http://103.155.196.83:8082 | ID | 2250 | 5 | 34/82 |
| http://103.158.210.80:8082 | ID | 2813 | 5 | 46/159 |
| http://160.19.146.221:2022 | ID | 1577 | 5 | 38/134 |
| http://160.22.45.114:8080 | ID | 4383 | 5 | 17/28 |
| http://163.61.55.243:8081 | ID | 1807 | 5 | 32/163 |
| http://202.47.185.153:8090 | ID | 3023 | 5 | 27/124 |
| http://52.195.147.51:3128 | JP | 3893 | 5 | 40/133 |
| http://140.238.32.108:3128 | JP | 2979 | 5 | 94/168 |
| http://38.210.179.30:999 | MX | 2881 | 5 | 25/101 |
| http://82.152.138.127:999 | MX | 357 | 5 | 45/131 |
| http://38.172.130.175:999 | PE | 4106 | 5 | 22/55 |
| http://83.171.113.43:3128 | RU | 2401 | 5 | 9/15 |
| http://49.229.100.235:8080 | TH | 1549 | 5 | 77/117 |
| http://209.62.196.68:8080 | US | 2872 | 5 | 22/112 |
| http://23.94.68.53:3128 | ?? | 583 | 5 | 5/5 |
| http://152.42.170.187:9090 | ?? | 1306 | 5 | 5/5 |
| http://171.100.254.137:8080 | ?? | 1654 | 5 | 5/5 |
| http://189.51.168.164:999 | ?? | 1396 | 5 | 5/5 |
| socks5://8.219.122.8:9999 | SG | 6205 | 5 | 25/59 |
| socks5://176.124.206.150:8443 | ?? | 1113 | 5 | 5/5 |
| http://181.209.107.154:999 | AR | 6271 | 4 | 9/33 |
| http://187.102.219.64:999 | AR | 1127 | 4 | 66/108 |
| http://103.89.27.32:8080 | BD | 3732 | 4 | 7/32 |
| http://185.191.239.248:3128 | CH | 836 | 4 | 120/168 |
| http://186.67.94.10:999 | CL | 2618 | 4 | 30/164 |
| http://102.244.78.61:8080 | CM | 6377 | 4 | 47/58 |
| http://102.244.78.61:8084 | CM | 4839 | 4 | 45/57 |
| http://114.244.221.178:8888 | CN | 2162 | 4 | 47/92 |
| http://123.119.25.143:8888 | CN | 2467 | 4 | 60/134 |
| http://38.95.88.126:999 | DO | 4076 | 4 | 22/120 |
| http://179.60.189.81:999 | EC | 1904 | 4 | 22/41 |
| http://41.33.245.139:1976 | EG | 2311 | 4 | 7/8 |
| http://188.164.201.197:666 | GR | 3217 | 4 | 24/53 |
| http://43.161.254.16:3128 | HK | 3842 | 4 | 6/9 |
| http://103.130.61.61:8081 | ID | 1892 | 4 | 138/169 |
| http://103.172.42.123:1111 | ID | 4428 | 4 | 29/167 |
| http://103.174.236.120:8080 | ID | 4590 | 4 | 10/15 |
| http://180.148.25.190:3128 | ID | 5608 | 4 | 13/27 |
| http://161.248.176.2:8080 | IN | 2424 | 4 | 23/98 |
| http://45.174.175.27:999 | MX | 736 | 4 | 35/131 |
| http://187.251.224.167:8081 | MX | 4197 | 4 | 41/129 |
| http://49.149.24.144:8082 | PH | 2311 | 4 | 5/8 |
| http://119.93.207.214:8082 | PH | 2977 | 4 | 36/161 |
| http://185.78.113.230:81 | RU | 1124 | 4 | 44/165 |
| http://128.199.116.219:9090 | SG | 1150 | 4 | 69/88 |
| http://61.91.162.126:8080 | TH | 1496 | 4 | 82/112 |
| http://103.10.231.189:8080 | TH | 1944 | 4 | 109/154 |
