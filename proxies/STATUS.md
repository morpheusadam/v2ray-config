# Proxy status

Generated 2026-11-01T23:03:42Z by `harvest.py`.

- **2318** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4877** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34475** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 117/600 (20%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2826 |
| socks5 | 2039 |
| socks4 | 12 |

| country | entries |
|---|---|
| NL | 1817 |
| ID | 731 |
| ?? | 683 |
| CO | 118 |
| PH | 115 |
| MX | 106 |
| US | 89 |
| BR | 75 |
| TH | 74 |
| VE | 74 |
| BD | 68 |
| RU | 58 |
| IN | 51 |
| DO | 50 |
| CN | 49 |
| EC | 49 |
| TR | 49 |
| AR | 41 |
| PE | 34 |
| SG | 32 |
| PK | 30 |
| JP | 28 |
| DE | 26 |
| KH | 24 |
| CA | 22 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 4 | 2026-11-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 55 | 2026-11-01 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 63 | 2026-11-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 255 | 255 | 69 | 2026-11-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 290 | 290 | 73 | 2026-11-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 397 | 397 | 244 | 2026-11-01 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 160 | 2026-11-01 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 530 | 2026-11-01 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 440 | 2026-11-01 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 655 | 655 | 226 | 2026-11-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 884 | 884 | 268 | 2026-11-01 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 1161 | 1161 | 593 | 2026-11-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1124 | 2026-11-01 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-11-01 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1805 | 1805 | 359 | 2026-11-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2339 | 2339 | 693 | 2026-11-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2755 | 2755 | 1683 | 2026-11-01 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3650 | 3650 | 1166 | 2026-11-01 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4928 | 4928 | 3701 | 2026-11-01 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11262 | 11261 | 2582 | 2026-11-01 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 3911 | 86 | 153/166 |
| http://149.130.173.58:9443 | CO | 625 | 77 | 77/77 |
| http://103.237.102.191:11111 | DE | 983 | 53 | 159/166 |
| http://103.133.26.73:3128 | ID | 1247 | 42 | 62/144 |
| http://176.111.37.5:39811 | HK | 1110 | 37 | 147/166 |
| http://34.43.46.91:80 | US | 545 | 36 | 160/166 |
| http://4.144.146.21:80 | SG | 952 | 34 | 51/58 |
| http://176.111.37.216:39811 | HK | 1218 | 29 | 138/166 |
| http://34.43.46.91:443 | US | 610 | 15 | 155/166 |
| http://167.172.76.176:9090 | SG | 925 | 13 | 90/127 |
| socks5://101.36.104.239:10808 | JP | 1329 | 13 | 142/166 |
| http://130.110.103.245:3128 | SA | 1519 | 12 | 148/166 |
| socks5://45.61.188.134:44499 | US | 539 | 12 | 68/133 |
| socks5://193.25.215.182:22222 | US | 428 | 12 | 139/166 |
| http://123.121.134.192:8888 | CN | 1900 | 10 | 17/32 |
| http://177.234.217.85:999 | EC | 1934 | 9 | 12/21 |
| http://103.133.26.72:8080 | ID | 1244 | 9 | 46/92 |
| http://81.19.210.10:80 | GB | 865 | 8 | 19/27 |
| http://154.59.56.78:999 | VE | 4545 | 8 | 85/122 |
| http://45.189.57.114:3129 | ?? | 884 | 8 | 8/8 |
| socks5://107.174.30.92:1080 | US | 5592 | 8 | 33/62 |
| http://15.229.149.81:1080 | BR | 2199 | 7 | 31/68 |
| http://102.244.78.61:8085 | CM | 1442 | 7 | 44/56 |
| http://102.244.78.61:8087 | CM | 1436 | 7 | 43/56 |
| http://45.43.60.220:8080 | JP | 1323 | 7 | 91/165 |
| http://102.68.76.247:5566 | KE | 4162 | 7 | 42/119 |
| http://159.223.41.216:9090 | SG | 900 | 7 | 91/126 |
| socks5://37.18.73.60:5566 | RU | 3703 | 7 | 23/63 |
| http://102.244.78.61:8090 | CM | 1423 | 6 | 44/58 |
| http://103.253.18.6:8080 | PK | 2782 | 6 | 16/76 |
| http://38.172.160.16:999 | VE | 3101 | 6 | 69/117 |
| http://200.59.191.27:999 | VE | 3554 | 6 | 110/161 |
| http://130.127.204.197:8080 | ?? | 405 | 6 | 6/6 |
| socks5://207.180.217.98:1088 | ?? | 2063 | 6 | 6/6 |
| http://45.65.224.74:999 | AR | 1312 | 5 | 24/31 |
| http://123.200.8.170:10000 | BD | 1884 | 5 | 72/164 |
| http://102.244.78.61:8082 | CM | 1437 | 5 | 44/55 |
| http://102.244.78.61:8089 | CM | 1450 | 5 | 42/54 |
| http://217.76.245.80:999 | DO | 6212 | 5 | 34/122 |
| http://190.12.150.244:999 | EC | 1776 | 5 | 118/162 |
| http://144.124.251.24:11011 | NL | 815 | 5 | 61/98 |
| http://185.238.238.49:58080 | PL | 7104 | 5 | 54/160 |
| http://185.238.238.113:58080 | PL | 1190 | 5 | 44/135 |
| http://154.59.56.72:999 | VE | 4980 | 5 | 92/125 |
| http://154.59.56.73:999 | VE | 2571 | 5 | 97/138 |
| socks5://213.199.47.140:1080 | FR | 7265 | 5 | 104/132 |
| socks5://69.55.49.177:38182 | US | 934 | 5 | 20/21 |
| socks5://82.180.146.251:10800 | ?? | 1468 | 5 | 5/5 |
| socks5://192.3.7.110:1080 | ?? | 761 | 5 | 5/5 |
| http://187.102.219.32:999 | AR | 3590 | 4 | 55/165 |
| http://181.191.14.5:8080 | BR | 5448 | 4 | 21/156 |
| http://186.96.111.214:999 | CO | 3243 | 4 | 74/155 |
| http://45.186.6.104:3128 | EC | 814 | 4 | 136/144 |
| http://177.234.217.82:999 | EC | 5898 | 4 | 14/63 |
| http://181.188.203.40:999 | EC | 4286 | 4 | 28/63 |
| http://197.164.101.13:1981 | EG | 1907 | 4 | 54/155 |
| http://102.164.252.150:8080 | GQ | 3869 | 4 | 48/125 |
| http://164.163.74.97:999 | HN | 5603 | 4 | 27/88 |
| http://168.228.44.66:999 | HN | 6998 | 4 | 16/78 |
| http://103.102.12.67:8080 | ID | 7067 | 4 | 10/21 |
| http://103.144.54.53:8082 | ID | 7355 | 4 | 14/48 |
| http://103.174.237.128:8080 | ID | 6718 | 4 | 12/29 |
| http://157.15.211.48:8080 | ID | 2808 | 4 | 19/78 |
| http://160.19.146.210:2022 | ID | 7984 | 4 | 23/109 |
| http://13.208.246.143:46557 | JP | 2869 | 4 | 32/126 |
| http://178.217.168.164:55443 | KG | 7486 | 4 | 33/146 |
| http://38.58.130.128:999 | MX | 6479 | 4 | 31/161 |
| http://144.124.251.24:10188 | NL | 782 | 4 | 4/4 |
| http://144.124.251.24:10366 | NL | 780 | 4 | 66/112 |
| http://144.124.251.24:10469 | NL | 839 | 4 | 4/4 |
| http://144.124.251.24:10812 | NL | 767 | 4 | 4/4 |
| http://112.208.174.83:8080 | PH | 2969 | 4 | 18/52 |
| http://119.93.64.216:8082 | PH | 5899 | 4 | 16/79 |
| http://104.248.151.93:9090 | SG | 898 | 4 | 49/67 |
| http://195.226.213.251:8888 | UA | 6310 | 4 | 64/160 |
| http://165.154.162.73:8888 | US | 519 | 4 | 109/166 |
| http://38.41.0.60:11201 | VE | 5832 | 4 | 32/92 |
| http://38.41.27.150:11201 | VE | 3476 | 4 | 23/81 |
| http://80.74.30.136:31286 | ?? | 892 | 4 | 5/6 |
| socks5://31.58.144.19:1080 | DE | 908 | 4 | 18/27 |
| socks5://121.169.46.116:1090 | KR | 1287 | 4 | 114/166 |
| socks5://175.107.30.110:1080 | PK | 7696 | 4 | 19/52 |
| socks5://45.61.129.165:9050 | US | 1825 | 4 | 125/166 |
| http://165.101.222.18:8080 | BD | 4632 | 3 | 15/67 |
| http://200.115.100.33:8080 | BR | 5604 | 3 | 25/138 |
| http://35.183.29.62:8051 | CA | 6315 | 3 | 4/6 |
| http://35.183.29.62:8181 | CA | 4358 | 3 | 33/134 |
| http://123.121.134.141:8888 | CN | 1581 | 3 | 16/27 |
| http://190.0.246.213:4040 | CO | 7033 | 3 | 121/131 |
| http://38.75.82.211:999 | DO | 4335 | 3 | 16/39 |
| http://177.234.211.195:999 | EC | 6890 | 3 | 8/55 |
| http://198.244.254.77:3128 | GB | 4582 | 3 | 43/50 |
| http://43.155.62.157:443 | HK | 788 | 3 | 59/69 |
| http://36.64.54.98:8080 | ID | 2388 | 3 | 25/78 |
| http://45.198.11.183:9191 | ID | 3298 | 3 | 12/47 |
| http://103.36.9.9:8181 | ID | 5593 | 3 | 22/89 |
| http://103.61.234.186:8180 | ID | 6530 | 3 | 69/163 |
| http://103.82.246.129:8181 | ID | 5214 | 3 | 11/44 |
| http://103.145.176.162:8080 | ID | 7514 | 3 | 27/144 |
| http://103.159.96.158:3127 | ID | 6484 | 3 | 35/150 |
