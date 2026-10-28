# Proxy status

Generated 2026-10-28T19:04:20Z by `harvest.py`.

- **1907** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4148** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39698** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 186/600 (31%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2804 |
| socks5 | 1340 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 1102 |
| ID | 947 |
| ?? | 249 |
| PH | 152 |
| MX | 123 |
| CO | 121 |
| US | 103 |
| RU | 86 |
| VE | 77 |
| BR | 74 |
| CN | 71 |
| TH | 70 |
| BD | 66 |
| EC | 66 |
| IN | 56 |
| AR | 49 |
| TR | 47 |
| DO | 44 |
| VN | 44 |
| SG | 39 |
| ZA | 31 |
| PK | 30 |
| JP | 29 |
| EG | 27 |
| PE | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 1 | 2026-10-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 79 | 79 | 20 | 2026-10-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 82 | 82 | 45 | 2026-10-28 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 122 | 122 | 58 | 2026-10-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-10-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 221 | 221 | 55 | 2026-10-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-10-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 323 | 323 | 6 | 2026-10-28 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 456 | 456 | 153 | 2026-10-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-10-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 737 | 737 | 307 | 2026-10-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1133 | 2026-10-28 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1640 | 1640 | 79 | 2026-10-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-10-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2488 | 2488 | 648 | 2026-10-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2974 | 2974 | 1930 | 2026-10-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3532 | 3532 | 1024 | 2026-10-28 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 79964 | 79964 | 65653 | 2026-10-28 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 86938 | 86937 | 3018 | 2026-10-28 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 1331 | 77 | 144/157 |
| http://149.130.173.58:9443 | CO | 743 | 68 | 68/68 |
| http://190.0.246.213:4040 | CO | 753 | 51 | 114/122 |
| http://103.237.102.191:11111 | DE | 1172 | 44 | 150/157 |
| http://45.186.6.104:3128 | EC | 911 | 38 | 128/135 |
| http://103.133.26.73:3128 | ID | 1212 | 33 | 53/135 |
| http://103.133.26.119:8080 | ID | 1554 | 33 | 37/67 |
| http://176.111.37.5:39811 | HK | 1113 | 28 | 138/157 |
| http://34.43.46.91:80 | US | 566 | 27 | 151/157 |
| http://4.144.146.21:80 | SG | 870 | 25 | 42/49 |
| http://190.0.246.210:4040 | CO | 826 | 24 | 143/156 |
| http://43.155.62.157:443 | HK | 1866 | 24 | 52/60 |
| http://102.244.78.61:8081 | CM | 1548 | 23 | 36/43 |
| http://186.5.94.206:999 | EC | 1115 | 22 | 110/119 |
| http://189.51.168.165:999 | MX | 614 | 21 | 64/69 |
| http://176.111.37.216:39811 | HK | 1301 | 20 | 129/157 |
| http://103.130.61.61:8081 | ID | 3218 | 19 | 127/157 |
| http://103.133.26.50:8080 | ID | 1159 | 17 | 36/58 |
| http://103.130.61.60:8081 | ID | 3511 | 13 | 13/13 |
| socks5://67.207.92.87:1088 | US | 833 | 12 | 98/156 |
| socks5://69.55.49.177:38182 | US | 1698 | 12 | 12/12 |
| socks5://101.36.104.46:10808 | JP | 1378 | 11 | 136/157 |
| http://89.167.124.218:8888 | DE | 1090 | 10 | 10/10 |
| http://45.65.224.74:999 | AR | 2169 | 9 | 17/22 |
| http://102.244.78.61:8085 | CM | 1430 | 9 | 36/47 |
| http://102.244.78.61:8087 | CM | 2658 | 9 | 35/47 |
| http://43.202.114.177:7428 | KR | 2428 | 8 | 31/71 |
| http://187.102.219.42:999 | AR | 1543 | 7 | 86/152 |
| http://159.223.41.216:9090 | SG | 853 | 7 | 84/117 |
| socks5://47.238.126.208:1080 | HK | 2416 | 7 | 33/62 |
| http://45.65.137.218:999 | CO | 5233 | 6 | 50/122 |
| http://190.12.150.244:999 | EC | 5918 | 6 | 111/153 |
| http://51.15.20.32:3129 | NL | 2631 | 6 | 17/21 |
| http://128.199.116.219:9090 | SG | 847 | 6 | 60/76 |
| http://34.43.46.91:443 | US | 653 | 6 | 146/157 |
| http://45.65.226.169:999 | AR | 5254 | 5 | 14/19 |
| http://123.200.8.170:10000 | BD | 2832 | 5 | 65/155 |
| http://190.7.138.78:8080 | CO | 1901 | 5 | 41/86 |
| http://177.234.221.197:999 | EC | 5010 | 5 | 31/62 |
| http://34.88.38.81:9443 | FI | 1095 | 5 | 84/122 |
| http://35.228.49.168:9443 | FI | 878 | 5 | 65/94 |
| http://198.244.254.77:3128 | GB | 6097 | 5 | 37/41 |
| http://103.194.47.53:8082 | ID | 7802 | 5 | 36/126 |
| http://140.238.32.108:3128 | JP | 3631 | 5 | 84/156 |
| http://200.94.38.45:2604 | MX | 4306 | 5 | 23/46 |
| http://154.59.56.72:999 | VE | 3985 | 5 | 84/116 |
| http://16.28.32.67:48907 | ZA | 2729 | 5 | 23/69 |
| socks5://213.199.47.140:1080 | FR | 1730 | 5 | 97/123 |
| socks5://103.100.158.115:10809 | JP | 727 | 5 | 36/45 |
| socks5://103.182.22.221:9000 | ?? | 4808 | 5 | 6/9 |
| http://45.65.226.173:999 | AR | 3988 | 4 | 8/18 |
| http://187.102.219.34:999 | AR | 1338 | 4 | 59/108 |
| http://13.239.253.213:3128 | AU | 3600 | 4 | 36/122 |
| http://158.172.153.36:999 | BO | 4441 | 4 | 21/136 |
| http://40.177.104.199:48086 | CA | 1414 | 4 | 34/124 |
| http://184.70.113.34:3128 | CA | 1625 | 4 | 38/155 |
| http://16.18.22.211:9090 | CH | 2351 | 4 | 36/117 |
| http://101.251.204.174:8080 | CN | 1806 | 4 | 78/143 |
| http://123.119.25.143:8888 | CN | 1201 | 4 | 53/122 |
| http://123.121.122.28:8888 | CN | 1138 | 4 | 63/106 |
| http://186.96.111.214:999 | CO | 5120 | 4 | 68/146 |
| http://45.71.186.214:999 | EC | 2247 | 4 | 43/103 |
| http://41.33.245.138:1981 | EG | 6496 | 4 | 40/87 |
| http://43.198.78.37:48065 | HK | 5311 | 4 | 19/113 |
| http://103.129.205.151:8080 | ID | 6949 | 4 | 8/18 |
| http://103.147.135.33:8082 | ID | 4721 | 4 | 34/103 |
| http://103.176.96.32:8082 | ID | 7957 | 4 | 33/150 |
| http://103.180.123.47:8080 | ID | 4816 | 4 | 17/63 |
| http://157.10.97.185:8080 | ID | 1214 | 4 | 17/70 |
| http://163.61.191.7:3128 | ID | 4636 | 4 | 6/13 |
| http://163.227.146.38:8080 | ID | 3370 | 4 | 38/157 |
| http://119.93.207.214:8082 | PH | 2622 | 4 | 30/149 |
| http://122.52.202.231:8080 | PH | 2176 | 4 | 7/15 |
| http://154.18.196.6:8083 | PH | 3092 | 4 | 30/150 |
| http://185.238.238.169:58080 | PL | 4499 | 4 | 37/79 |
| http://167.172.76.176:9090 | SG | 847 | 4 | 81/118 |
| http://43.251.205.146:8080 | TH | 6329 | 4 | 33/123 |
| http://171.101.72.82:8080 | TH | 4335 | 4 | 6/10 |
| http://190.94.212.216:999 | VE | 5111 | 4 | 9/15 |
| http://103.131.19.42:8181 | ?? | 4638 | 4 | 5/12 |
| http://177.234.217.83:999 | ?? | 5860 | 4 | 4/4 |
| http://177.234.217.84:999 | ?? | 6972 | 4 | 4/4 |
| socks5://101.36.104.239:10808 | JP | 2338 | 4 | 133/157 |
| socks5://193.218.118.128:1080 | UA | 1747 | 4 | 10/13 |
| socks5://20.121.179.183:3001 | ?? | 7013 | 4 | 4/4 |
| http://18.230.23.72:25761 | BR | 3091 | 3 | 35/117 |
| http://131.196.50.128:8080 | BR | 5830 | 3 | 17/80 |
| http://201.62.125.142:8080 | BR | 7838 | 3 | 9/61 |
| http://201.71.24.65:8082 | BR | 7340 | 3 | 26/146 |
| http://16.174.124.173:425 | CA | 3164 | 3 | 27/125 |
| http://112.65.132.181:3128 | CN | 3157 | 3 | 5/10 |
| http://114.244.221.178:8888 | CN | 1635 | 3 | 38/80 |
| http://123.119.179.34:8888 | CN | 5621 | 3 | 44/119 |
| http://123.119.179.161:8888 | CN | 6171 | 3 | 52/122 |
| http://221.221.163.120:8888 | CN | 1209 | 3 | 42/110 |
| http://45.65.138.48:999 | CO | 4299 | 3 | 68/157 |
| http://152.200.200.217:999 | CO | 6424 | 3 | 30/135 |
| http://181.79.57.57:8080 | CO | 7585 | 3 | 17/58 |
| http://38.50.165.125:999 | DO | 6805 | 3 | 34/132 |
| http://45.71.186.210:999 | EC | 1206 | 3 | 47/131 |
