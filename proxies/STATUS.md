# Proxy status

Generated 2026-10-31T17:53:44Z by `harvest.py`.

- **3148** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5342** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33656** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 196/600 (33%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2827 |
| socks5 | 2511 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 2245 |
| ID | 794 |
| ?? | 581 |
| CO | 125 |
| PH | 119 |
| MX | 96 |
| US | 85 |
| TH | 82 |
| RU | 75 |
| VE | 69 |
| BR | 67 |
| CN | 61 |
| TR | 58 |
| BD | 55 |
| EC | 50 |
| IN | 50 |
| AR | 45 |
| DO | 43 |
| PK | 43 |
| ZA | 33 |
| PE | 30 |
| SG | 30 |
| SY | 27 |
| DE | 23 |
| KH | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 11 | 11 | 4 | 2026-10-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 110 | 110 | 26 | 2026-10-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 55 | 2026-10-31 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 72 | 2026-10-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 164 | 164 | 99 | 2026-10-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 164 | 164 | 53 | 2026-10-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-10-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 367 | 367 | 132 | 2026-10-31 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-31 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-31 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 453 | 2026-10-31 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 953 | 953 | 244 | 2026-10-31 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1114 | 1114 | 594 | 2026-10-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-10-31 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1588 | 2026-10-31 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1898 | 1898 | 0 | 2026-10-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2569 | 2569 | 645 | 2026-10-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3030 | 3030 | 1747 | 2026-10-31 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3279 | 3279 | 986 | 2026-10-31 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4895 | 4895 | 3683 | 2026-10-31 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10748 | 10747 | 2517 | 2026-10-31 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 2942 | 83 | 150/163 |
| http://149.130.173.58:9443 | CO | 619 | 74 | 74/74 |
| http://103.237.102.191:11111 | DE | 1068 | 50 | 156/163 |
| http://103.133.26.73:3128 | ID | 1257 | 39 | 59/141 |
| http://103.133.26.119:8080 | ID | 1557 | 39 | 43/73 |
| http://176.111.37.5:39811 | HK | 1694 | 34 | 144/163 |
| http://34.43.46.91:80 | US | 4707 | 33 | 157/163 |
| http://4.144.146.21:80 | SG | 903 | 31 | 48/55 |
| http://190.0.246.210:4040 | CO | 6351 | 30 | 149/162 |
| http://176.111.37.216:39811 | HK | 1679 | 26 | 135/163 |
| http://103.130.61.61:8081 | ID | 5217 | 25 | 133/163 |
| socks5://67.207.92.87:1088 | US | 839 | 18 | 104/162 |
| http://34.43.46.91:443 | US | 1161 | 12 | 152/163 |
| http://167.172.76.176:9090 | SG | 923 | 10 | 87/124 |
| socks5://101.36.104.239:10808 | JP | 1383 | 10 | 139/163 |
| socks5://193.218.118.128:1080 | UA | 3786 | 10 | 16/19 |
| http://130.110.103.245:3128 | SA | 1573 | 9 | 145/163 |
| socks5://49.13.22.249:10805 | DE | 5857 | 9 | 49/81 |
| socks5://45.61.188.134:44499 | US | 611 | 9 | 65/130 |
| socks5://193.25.215.182:22222 | US | 453 | 9 | 136/163 |
| http://185.238.236.226:58080 | PL | 1133 | 8 | 35/85 |
| socks5://45.149.92.160:1080 | HK | 1613 | 8 | 21/30 |
| http://123.121.134.192:8888 | CN | 2422 | 7 | 14/29 |
| http://103.172.42.161:1111 | ID | 6360 | 7 | 16/97 |
| socks5://88.201.248.85:1080 | RU | 5240 | 7 | 12/18 |
| http://15.229.149.81:3128 | BR | 5440 | 6 | 43/73 |
| http://35.183.78.223:35766 | CA | 1867 | 6 | 6/6 |
| http://177.234.217.85:999 | EC | 4044 | 6 | 9/18 |
| http://177.234.217.235:999 | EC | 4458 | 6 | 64/132 |
| http://38.103.250.205:8080 | ID | 7106 | 6 | 24/126 |
| http://103.133.26.72:8080 | ID | 1196 | 6 | 43/89 |
| http://103.168.254.198:8080 | ID | 1283 | 6 | 17/27 |
| http://128.199.121.61:9090 | SG | 906 | 6 | 66/83 |
| http://16.28.101.55:2080 | ZA | 2164 | 6 | 35/103 |
| http://38.211.68.83:999 | ?? | 5047 | 6 | 6/6 |
| socks5://212.77.75.25:1088 | IT | 1107 | 6 | 51/63 |
| socks5://43.155.143.227:1080 | ?? | 827 | 6 | 6/6 |
| http://190.124.252.129:6666 | BR | 5035 | 5 | 31/141 |
| http://36.213.79.159:1081 | CN | 1907 | 5 | 10/23 |
| http://114.249.219.180:8888 | CN | 3391 | 5 | 52/127 |
| http://123.121.209.108:8888 | CN | 2406 | 5 | 41/113 |
| http://81.19.210.10:80 | GB | 6356 | 5 | 16/24 |
| http://103.175.237.36:8080 | ID | 3812 | 5 | 32/139 |
| http://154.18.255.43:8080 | ID | 3750 | 5 | 16/68 |
| http://203.175.102.54:3125 | ID | 4600 | 5 | 20/123 |
| http://180.191.137.111:8082 | PH | 6311 | 5 | 34/147 |
| http://149.40.242.118:8080 | PK | 3204 | 5 | 8/27 |
| http://154.59.56.78:999 | VE | 3791 | 5 | 82/119 |
| http://45.189.57.114:3129 | ?? | 873 | 5 | 5/5 |
| http://104.194.146.9:80 | ?? | 1178 | 5 | 8/9 |
| http://191.5.126.28:8080 | ?? | 1585 | 5 | 6/8 |
| socks5://202.62.42.92:1080 | KH | 4549 | 5 | 33/145 |
| socks5://202.62.42.167:1080 | KH | 3542 | 5 | 42/160 |
| socks5://107.174.30.92:1080 | US | 6377 | 5 | 30/59 |
| http://187.102.219.64:999 | AR | 3544 | 4 | 61/102 |
| http://15.229.149.81:1080 | BR | 3137 | 4 | 28/65 |
| http://15.223.187.219:55865 | CA | 4181 | 4 | 26/77 |
| http://102.244.78.61:8080 | CM | 1396 | 4 | 42/52 |
| http://102.244.78.61:8083 | CM | 1403 | 4 | 42/51 |
| http://102.244.78.61:8084 | CM | 1390 | 4 | 40/51 |
| http://102.244.78.61:8085 | CM | 1415 | 4 | 41/53 |
| http://102.244.78.61:8086 | CM | 1399 | 4 | 41/51 |
| http://102.244.78.61:8087 | CM | 1417 | 4 | 40/53 |
| http://61.149.134.158:8888 | CN | 1226 | 4 | 49/128 |
| http://123.121.102.115:8888 | CN | 1189 | 4 | 26/123 |
| http://123.121.108.22:8888 | CN | 1337 | 4 | 10/14 |
| http://179.1.196.133:999 | CO | 5047 | 4 | 11/19 |
| http://181.78.195.137:999 | EC | 2236 | 4 | 56/163 |
| http://181.224.175.200:999 | EC | 1343 | 4 | 20/78 |
| http://8.215.25.3:2081 | ID | 1067 | 4 | 45/161 |
| http://103.97.141.85:8080 | ID | 3038 | 4 | 17/77 |
| http://103.151.22.66:8082 | ID | 2243 | 4 | 32/102 |
| http://108.137.124.195:8998 | ID | 3980 | 4 | 30/122 |
| http://110.76.144.119:8082 | ID | 1477 | 4 | 31/64 |
| http://163.227.135.146:8080 | ID | 1724 | 4 | 31/140 |
| http://202.47.162.58:8080 | ID | 2376 | 4 | 21/105 |
| http://89.46.219.133:80 | IR | 3830 | 4 | 8/22 |
| http://45.43.60.220:8080 | JP | 5210 | 4 | 88/162 |
| http://140.238.32.108:3128 | JP | 2701 | 4 | 89/162 |
| http://102.68.76.247:5566 | KE | 4459 | 4 | 39/116 |
| http://197.248.59.159:8082 | KE | 4033 | 4 | 13/82 |
| http://45.174.242.145:999 | MX | 4641 | 4 | 25/118 |
| http://69.171.214.160:999 | MX | 3660 | 4 | 17/66 |
| http://49.145.58.197:8082 | PH | 7792 | 4 | 22/37 |
| http://122.53.48.41:8080 | PH | 6945 | 4 | 22/85 |
| http://124.105.39.244:8081 | PH | 3714 | 4 | 5/13 |
| http://128.199.116.219:9090 | SG | 887 | 4 | 64/82 |
| http://159.223.41.216:9090 | SG | 893 | 4 | 88/123 |
| http://38.188.201.10:999 | VE | 4876 | 4 | 28/77 |
| http://163.227.149.137:3128 | ?? | 3212 | 4 | 6/7 |
| http://165.101.230.155:8080 | ?? | 4386 | 4 | 4/4 |
| http://181.129.16.218:8080 | ?? | 3032 | 4 | 4/4 |
| http://189.148.34.54:8080 | ?? | 593 | 4 | 4/4 |
| socks4://23.141.116.9:9000 | ?? | 1650 | 4 | 7/15 |
| socks5://5.75.133.113:10805 | DE | 1419 | 4 | 39/81 |
| socks5://37.18.73.60:5566 | RU | 2242 | 4 | 20/60 |
| socks5://42.115.72.145:1080 | ?? | 1598 | 4 | 4/4 |
| socks5://125.27.147.150:9999 | ?? | 1233 | 4 | 4/4 |
| socks5://195.201.246.53:1081 | ?? | 1421 | 4 | 5/6 |
| http://187.102.219.34:999 | AR | 2427 | 3 | 63/114 |
