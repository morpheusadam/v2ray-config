# Proxy status

Generated 2026-09-30T18:32:41Z by `harvest.py`.

- **1781** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4199** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39542** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 166/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2135 |
| http | 2060 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 1950 |
| ID | 552 |
| US | 129 |
| ?? | 107 |
| CN | 104 |
| RU | 85 |
| PH | 81 |
| CO | 73 |
| MX | 70 |
| IN | 66 |
| BR | 57 |
| VE | 53 |
| BD | 49 |
| EC | 47 |
| DE | 45 |
| TR | 45 |
| SG | 38 |
| VN | 36 |
| DO | 31 |
| PK | 31 |
| JP | 28 |
| FR | 27 |
| HK | 25 |
| AR | 24 |
| CA | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 1 | 2026-09-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 65 | 65 | 34 | 2026-09-30 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 79 | 2026-09-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 121 | 121 | 46 | 2026-09-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 78 | 2026-09-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 155 | 155 | 50 | 2026-09-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 259 | 259 | 139 | 2026-09-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 282 | 282 | 125 | 2026-09-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 325 | 325 | 141 | 2026-09-30 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 719 | 719 | 253 | 2026-09-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1132 | 2026-09-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1587 | 2026-09-30 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1973 | 1969 | 0 | 2026-09-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2804 | 2802 | 647 | 2026-09-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2983 | 2981 | 2142 | 2026-09-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3314 | 3312 | 702 | 2026-09-30 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 32996 | 32996 | 18330 | 2026-09-30 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 38962 | 38961 | 2672 | 2026-09-30 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 880 | 88 | 101/102 |
| http://95.3.69.222:8080 | TR | 1139 | 57 | 99/102 |
| http://190.0.246.213:4040 | CO | 614 | 31 | 60/67 |
| http://213.111.146.36:18080 | NL | 479 | 31 | 34/39 |
| http://190.0.246.211:4040 | CO | 800 | 22 | 89/102 |
| http://34.43.46.91:80 | US | 513 | 19 | 98/102 |
| http://190.0.246.210:4040 | CO | 715 | 18 | 90/101 |
| http://103.237.102.191:11111 | DE | 577 | 18 | 96/102 |
| http://18.157.123.132:3128 | DE | 523 | 17 | 49/63 |
| socks5://107.167.18.122:443 | US | 506 | 17 | 52/54 |
| socks5://144.91.121.61:1088 | FR | 5076 | 16 | 88/102 |
| http://34.43.46.91:443 | US | 494 | 15 | 96/102 |
| http://189.51.168.165:999 | MX | 676 | 14 | 14/14 |
| http://149.130.173.58:9443 | CO | 543 | 13 | 13/13 |
| http://43.173.120.13:8899 | US | 777 | 13 | 13/13 |
| http://185.195.71.218:18080 | CH | 1977 | 10 | 30/39 |
| http://103.119.19.218:3128 | CZ | 609 | 10 | 14/15 |
| http://186.5.94.206:999 | EC | 1041 | 10 | 61/64 |
| http://37.59.125.131:8888 | FR | 1057 | 10 | 81/102 |
| http://107.150.41.226:18080 | US | 447 | 10 | 38/39 |
| http://172.236.242.244:3128 | US | 429 | 10 | 10/10 |
| socks5://154.201.71.12:2080 | HK | 7723 | 9 | 10/11 |
| http://197.224.185.3:3128 | MU | 3083 | 8 | 64/70 |
| socks5://121.169.46.116:1090 | KR | 3919 | 8 | 69/102 |
| http://184.75.221.82:3118 | CA | 251 | 7 | 59/67 |
| http://144.76.61.252:3128 | DE | 6497 | 7 | 13/15 |
| http://45.186.6.104:3128 | EC | 844 | 7 | 75/80 |
| http://49.147.104.23:8082 | PH | 4553 | 7 | 7/7 |
| socks4://185.112.83.80:1080 | FI | 2454 | 7 | 7/7 |
| socks5://5.75.133.113:10801 | DE | 3059 | 7 | 40/68 |
| socks5://47.238.126.208:1080 | HK | 1378 | 7 | 7/7 |
| http://185.191.239.248:3128 | CH | 7764 | 6 | 72/101 |
| http://123.121.122.28:8888 | CN | 1898 | 6 | 31/51 |
| http://123.121.208.55:8888 | CN | 7620 | 6 | 21/55 |
| http://153.51.241.50:999 | MX | 6990 | 6 | 53/99 |
| http://49.229.100.235:8080 | TH | 1620 | 6 | 26/50 |
| http://61.91.162.126:8080 | TH | 1657 | 6 | 36/45 |
| http://103.10.231.189:8080 | TH | 1772 | 6 | 61/87 |
| socks5://101.36.104.239:10808 | JP | 1337 | 6 | 85/102 |
| http://221.221.154.122:8888 | CN | 6985 | 5 | 20/55 |
| http://129.212.171.38:3128 | DE | 528 | 5 | 5/5 |
| http://134.199.191.115:3128 | DE | 565 | 5 | 13/14 |
| http://34.88.38.81:9443 | FI | 833 | 5 | 45/67 |
| http://35.228.49.168:9443 | FI | 647 | 5 | 26/39 |
| http://43.155.62.157:443 | HK | 1187 | 5 | 5/5 |
| http://176.111.37.216:39811 | HK | 914 | 5 | 83/102 |
| http://202.154.19.50:3125 | ID | 5651 | 5 | 14/71 |
| http://136.114.233.244:3128 | US | 1410 | 5 | 6/7 |
| http://195.158.8.123:3128 | UZ | 3974 | 5 | 66/100 |
| http://190.97.229.118:999 | VE | 3839 | 5 | 49/92 |
| http://190.97.241.106:999 | VE | 5808 | 5 | 58/86 |
| http://113.161.93.6:8080 | VN | 3898 | 5 | 12/26 |
| socks5://109.123.251.109:1080 | FR | 1527 | 5 | 57/102 |
| socks5://193.25.215.182:22222 | US | 1353 | 5 | 91/102 |
| http://114.250.195.77:8888 | CN | 2202 | 4 | 25/67 |
| http://114.252.15.106:8888 | CN | 3398 | 4 | 31/55 |
| http://123.119.179.34:8888 | CN | 1884 | 4 | 24/64 |
| http://123.121.208.63:8888 | CN | 1962 | 4 | 24/48 |
| http://222.128.172.158:8888 | CN | 1705 | 4 | 30/67 |
| http://45.71.186.213:999 | EC | 4272 | 4 | 31/86 |
| http://177.234.217.43:999 | EC | 4595 | 4 | 23/75 |
| http://177.234.221.203:999 | EC | 1746 | 4 | 5/7 |
| http://90.161.220.67:3128 | ES | 7696 | 4 | 10/39 |
| http://103.113.26.7:8080 | ID | 4899 | 4 | 6/15 |
| http://35.78.252.142:56698 | JP | 3978 | 4 | 17/82 |
| http://185.238.236.226:58080 | PL | 2531 | 4 | 11/24 |
| http://56.228.13.15:443 | SE | 871 | 4 | 10/16 |
| http://47.81.56.193:8888 | TH | 2007 | 4 | 62/102 |
| http://69.87.216.54:7989 | US | 447 | 4 | 30/47 |
| http://38.172.160.16:999 | VE | 6698 | 4 | 31/53 |
| socks5://5.75.133.113:10807 | DE | 2190 | 4 | 10/17 |
| socks5://144.91.111.48:1088 | FR | 1642 | 4 | 65/102 |
| socks5://45.74.31.47:4769 | NL | 5789 | 4 | 4/4 |
| socks5://45.74.31.47:5223 | NL | 6369 | 4 | 4/4 |
| socks5://45.74.31.50:4726 | NL | 6617 | 4 | 4/4 |
| socks5://45.74.31.50:5349 | NL | 2343 | 4 | 4/4 |
| socks5://45.61.129.165:9050 | US | 2736 | 4 | 82/102 |
| socks5://67.207.92.87:1088 | US | 333 | 4 | 56/101 |
| socks5://129.153.11.56:1080 | US | 207 | 4 | 6/7 |
| socks5://160.187.0.89:1080 | VN | 1636 | 4 | 11/15 |
| http://114.246.203.194:8888 | CN | 1839 | 3 | 9/25 |
| http://123.115.226.82:8888 | CN | 1641 | 3 | 17/48 |
| http://123.121.121.123:8888 | CN | 1484 | 3 | 33/67 |
| http://123.121.211.160:8888 | CN | 1777 | 3 | 25/48 |
| http://179.1.182.19:999 | CO | 5895 | 3 | 11/72 |
| http://190.7.138.78:8080 | CO | 3148 | 3 | 16/31 |
| http://67.207.72.60:3128 | DE | 4041 | 3 | 12/17 |
| http://154.236.179.229:1981 | EG | 1786 | 3 | 10/20 |
| http://213.131.85.28:1981 | EG | 873 | 3 | 3/3 |
| http://37.59.138.176:8080 | ES | 2995 | 3 | 10/44 |
| http://102.164.255.155:8080 | GQ | 2042 | 3 | 12/60 |
| http://103.142.255.227:8080 | ID | 1688 | 3 | 3/3 |
| http://103.156.16.241:8081 | ID | 6226 | 3 | 9/22 |
| http://103.169.130.130:8080 | ID | 7548 | 3 | 5/15 |
| http://103.185.43.242:8080 | ID | 6758 | 3 | 4/15 |
| http://144.79.241.254:3128 | ID | 1541 | 3 | 3/3 |
| http://175.111.96.154:3128 | ID | 6976 | 3 | 6/15 |
| http://192.147.114.23:3127 | ID | 1631 | 3 | 11/36 |
| http://202.58.75.98:7777 | ID | 6855 | 3 | 5/25 |
| http://203.175.103.169:8080 | ID | 1578 | 3 | 5/15 |
