# Proxy status

Generated 2026-11-18T01:51:08Z by `harvest.py`.

- **1637** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3750** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **29880** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 127/600 (21%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2893 |
| socks5 | 837 |
| socks4 | 20 |

| country | entries |
|---|---|
| ID | 931 |
| NL | 581 |
| ?? | 203 |
| PH | 164 |
| CO | 133 |
| US | 131 |
| MX | 128 |
| TR | 94 |
| VE | 86 |
| BR | 85 |
| TH | 85 |
| RU | 81 |
| IN | 78 |
| BD | 75 |
| EC | 51 |
| DO | 50 |
| AR | 48 |
| VN | 44 |
| CN | 40 |
| EG | 37 |
| ZA | 34 |
| DE | 33 |
| PK | 33 |
| SG | 30 |
| KH | 25 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 2 | 2026-11-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 83 | 83 | 20 | 2026-11-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 85 | 85 | 30 | 2026-11-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 90 | 90 | 16 | 2026-11-18 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 33 | 2026-11-18 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 57 | 2026-11-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 203 | 203 | 29 | 2026-11-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-11-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 303 | 303 | 200 | 2026-11-18 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-18 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-11-18 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-11-18 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 709 | 709 | 102 | 2026-11-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1133 | 2026-11-18 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-18 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1853 | 1853 | 180 | 2026-11-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2208 | 2208 | 416 | 2026-11-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2262 | 2262 | 678 | 2026-11-18 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2587 | 2587 | 1504 | 2026-11-18 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5490 | 5490 | 4294 | 2026-11-18 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 12027 | 12027 | 2027 | 2026-11-18 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 3657 | 69 | 179/198 |
| http://130.110.103.245:3128 | SA | 1821 | 44 | 180/198 |
| http://38.180.18.103:3128 | BE | 1612 | 27 | 27/27 |
| http://27.147.155.206:12051 | BD | 2011 | 18 | 18/18 |
| http://177.234.217.235:999 | EC | 7142 | 12 | 88/167 |
| http://141.94.22.37:3128 | FR | 955 | 10 | 13/14 |
| http://188.166.178.163:3129 | SG | 2213 | 10 | 10/10 |
| socks5://37.18.73.60:5566 | RU | 1420 | 10 | 46/95 |
| socks5://188.166.178.163:1088 | SG | 2120 | 10 | 10/10 |
| http://45.65.138.48:999 | CO | 5201 | 8 | 98/198 |
| socks5://107.174.30.92:1080 | US | 305 | 8 | 54/94 |
| http://102.244.78.61:8083 | CM | 1873 | 7 | 69/86 |
| http://102.244.78.61:8084 | CM | 1290 | 7 | 67/86 |
| http://102.244.78.61:8086 | CM | 1422 | 7 | 68/86 |
| http://102.244.78.61:8089 | CM | 1519 | 7 | 70/86 |
| http://45.155.226.177:3128 | HK | 875 | 7 | 12/14 |
| http://211.188.50.146:80 | KR | 1478 | 7 | 7/7 |
| http://211.188.53.248:80 | KR | 5953 | 7 | 7/7 |
| http://211.188.55.218:80 | KR | 2438 | 7 | 7/7 |
| http://211.188.59.191:80 | KR | 1137 | 7 | 7/7 |
| http://102.244.78.61:8080 | CM | 1201 | 6 | 71/87 |
| http://102.244.78.61:8088 | CM | 1962 | 6 | 68/86 |
| socks5://101.36.104.46:10808 | JP | 4007 | 6 | 165/198 |
| http://102.244.78.61:8081 | CM | 1458 | 5 | 68/84 |
| http://102.244.78.61:8082 | CM | 1284 | 5 | 69/87 |
| http://102.244.78.61:8085 | CM | 1646 | 5 | 69/88 |
| http://102.244.78.61:8087 | CM | 1677 | 5 | 66/88 |
| http://102.244.78.61:8090 | CM | 1437 | 5 | 72/90 |
| http://177.234.217.82:999 | EC | 7094 | 5 | 32/95 |
| http://177.234.217.85:999 | EC | 2749 | 5 | 29/53 |
| http://177.234.217.89:999 | EC | 2048 | 5 | 13/23 |
| http://181.78.44.63:999 | HN | 1788 | 5 | 48/122 |
| http://43.165.169.48:80 | JP | 1143 | 5 | 10/15 |
| http://38.7.17.83:999 | MX | 3535 | 5 | 7/12 |
| http://82.152.138.127:999 | MX | 1047 | 5 | 71/160 |
| http://4.144.146.21:80 | SG | 1610 | 5 | 81/90 |
| http://167.99.74.174:9090 | SG | 1543 | 5 | 105/158 |
| http://216.152.149.246:80 | US | 5182 | 5 | 9/10 |
| http://15.229.149.81:3128 | BR | 3163 | 4 | 70/108 |
| http://185.191.239.248:3128 | CH | 1487 | 4 | 143/197 |
| http://123.121.101.115:8888 | CN | 2760 | 4 | 12/19 |
| http://38.19.41.208:999 | CO | 4380 | 4 | 32/163 |
| http://35.43.85.195:443 | ES | 968 | 4 | 11/14 |
| http://43.161.254.16:3128 | HK | 4788 | 4 | 32/38 |
| http://52.128.238.98:18080 | HK | 450 | 4 | 9/13 |
| http://31.58.57.74:1111 | ID | 4839 | 4 | 41/156 |
| http://103.156.75.89:1717 | ID | 3663 | 4 | 11/22 |
| http://103.172.42.177:1111 | ID | 4231 | 4 | 29/109 |
| http://103.238.232.50:8080 | ID | 5834 | 4 | 15/37 |
| http://38.194.246.34:999 | MX | 2462 | 4 | 112/189 |
| http://204.199.201.133:999 | MX | 5036 | 4 | 40/171 |
| http://206.135.56.50:8080 | MX | 7894 | 4 | 55/157 |
| http://185.238.236.226:58080 | PL | 4389 | 4 | 57/120 |
| http://128.199.121.61:9090 | SG | 1478 | 4 | 91/118 |
| http://216.152.152.44:80 | US | 1524 | 4 | 7/10 |
| socks4://5.78.181.0:9052 | ?? | 1363 | 4 | 4/4 |
| socks5://218.77.50.79:6666 | CN | 3683 | 4 | 27/91 |
| socks5://45.74.31.46:4089 | NL | 7722 | 4 | 5/16 |
| socks5://193.25.215.182:22222 | US | 1816 | 4 | 163/198 |
| http://77.242.21.133:8080 | AL | 4138 | 3 | 19/110 |
| http://85.132.108.42:3128 | AZ | 2939 | 3 | 12/16 |
| http://103.134.56.148:8080 | BD | 2782 | 3 | 41/140 |
| http://85.187.224.21:8080 | BG | 3214 | 3 | 22/111 |
| http://45.168.244.16:8080 | BR | 5352 | 3 | 13/37 |
| http://201.28.86.18:61804 | BR | 2086 | 3 | 15/19 |
| http://184.75.221.82:3118 | CA | 1239 | 3 | 141/163 |
| http://123.121.113.161:8888 | CN | 6166 | 3 | 15/23 |
| http://45.65.137.218:999 | CO | 2555 | 3 | 78/163 |
| http://161.18.226.135:8080 | CO | 1758 | 3 | 36/194 |
| http://157.230.28.51:1981 | DE | 4313 | 3 | 18/121 |
| http://177.234.217.44:999 | EC | 3771 | 3 | 38/98 |
| http://181.78.195.137:999 | EC | 2919 | 3 | 78/198 |
| http://41.33.89.100:1976 | EG | 4537 | 3 | 22/60 |
| http://197.164.101.14:1976 | EG | 1673 | 3 | 57/170 |
| http://185.174.80.7:3128 | ES | 5996 | 3 | 40/167 |
| http://45.170.34.154:999 | HN | 5786 | 3 | 11/28 |
| http://103.124.136.70:8080 | ID | 5641 | 3 | 8/21 |
| http://103.130.61.61:8081 | ID | 2665 | 3 | 163/198 |
| http://103.146.185.139:1111 | ID | 7131 | 3 | 16/95 |
| http://103.156.16.67:8080 | ID | 6261 | 3 | 12/38 |
| http://103.156.233.19:8080 | ID | 4709 | 3 | 6/25 |
| http://103.159.96.158:3127 | ID | 5577 | 3 | 45/182 |
| http://103.162.17.207:8080 | ID | 6624 | 3 | 19/105 |
| http://103.172.71.172:1111 | ID | 7675 | 3 | 23/122 |
| http://103.172.71.202:1111 | ID | 3781 | 3 | 31/180 |
| http://103.173.138.225:8080 | ID | 6519 | 3 | 17/31 |
| http://103.188.252.21:8080 | ID | 7244 | 3 | 8/27 |
| http://103.203.234.105:3127 | ID | 3887 | 3 | 8/27 |
| http://157.66.16.67:8758 | ID | 6023 | 3 | 6/28 |
| http://160.20.39.23:8090 | ID | 5513 | 3 | 40/173 |
| http://165.99.30.34:7777 | ID | 6943 | 3 | 12/35 |
| http://165.101.231.41:8080 | ID | 6802 | 3 | 8/28 |
| http://192.147.114.23:3127 | ID | 4525 | 3 | 38/132 |
| http://192.232.48.21:8181 | ID | 2846 | 3 | 18/104 |
| http://202.47.185.35:8080 | ID | 7130 | 3 | 35/169 |
| http://102.0.25.36:8080 | KE | 7490 | 3 | 26/182 |
| http://49.156.44.115:8080 | KH | 5965 | 3 | 56/164 |
| http://38.210.201.144:999 | MX | 2644 | 3 | 27/167 |
| http://187.251.130.143:8081 | MX | 2909 | 3 | 9/25 |
| http://206.135.74.172:999 | MX | 4443 | 3 | 5/25 |
