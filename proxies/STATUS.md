# Proxy status

Generated 2026-11-13T20:31:49Z by `harvest.py`.

- **1464** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3507** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **34542** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 130/600 (22%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2822 |
| socks5 | 664 |
| socks4 | 21 |

| country | entries |
|---|---|
| ID | 734 |
| NL | 502 |
| ?? | 424 |
| US | 137 |
| PH | 125 |
| CO | 117 |
| MX | 117 |
| CN | 94 |
| BR | 78 |
| VE | 77 |
| TH | 73 |
| TR | 67 |
| BD | 64 |
| AR | 57 |
| IN | 57 |
| EC | 52 |
| RU | 47 |
| DO | 33 |
| DE | 32 |
| SG | 32 |
| VN | 31 |
| ZA | 31 |
| PE | 29 |
| PK | 29 |
| EG | 28 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 64 | 64 | 10 | 2026-11-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 87 | 87 | 32 | 2026-11-13 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-11-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 39 | 2026-11-13 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 65 | 2026-11-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 209 | 209 | 17 | 2026-11-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 321 | 321 | 199 | 2026-11-13 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 337 | 337 | 89 | 2026-11-13 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-13 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 526 | 2026-11-13 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 443 | 2026-11-13 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 740 | 740 | 122 | 2026-11-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1122 | 2026-11-13 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1715 | 1715 | 109 | 2026-11-13 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1578 | 2026-11-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2058 | 2058 | 397 | 2026-11-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2245 | 2245 | 645 | 2026-11-13 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2287 | 2287 | 1413 | 2026-11-13 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5332 | 5332 | 4090 | 2026-11-13 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 11043 | 11043 | 1849 | 2026-11-13 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://176.111.37.5:39811 | HK | 3587 | 60 | 170/189 |
| http://34.43.46.91:80 | US | 3268 | 59 | 183/189 |
| http://4.144.146.21:80 | SG | 1019 | 57 | 74/81 |
| http://176.111.37.216:39811 | HK | 3514 | 52 | 161/189 |
| http://130.110.103.245:3128 | SA | 3514 | 35 | 171/189 |
| http://45.189.57.114:3129 | EC | 2091 | 31 | 31/31 |
| http://49.229.100.235:8080 | TH | 1394 | 25 | 97/137 |
| http://171.100.254.137:8080 | TH | 1687 | 25 | 25/25 |
| http://45.186.6.104:3128 | EC | 1058 | 19 | 158/167 |
| http://38.180.18.103:3128 | BE | 3976 | 18 | 18/18 |
| http://190.71.72.85:2525 | CO | 1707 | 17 | 33/74 |
| http://102.244.78.61:8090 | CM | 2072 | 16 | 65/81 |
| socks5://121.46.226.221:10808 | CN | 2962 | 15 | 15/15 |
| http://43.155.62.157:443 | HK | 1312 | 12 | 79/92 |
| http://185.191.239.248:3128 | CH | 2874 | 10 | 138/188 |
| http://27.147.155.206:12051 | BD | 1870 | 9 | 9/9 |
| http://43.128.144.133:18080 | KR | 3004 | 9 | 9/9 |
| http://51.85.44.162:31819 | IL | 5853 | 8 | 26/41 |
| http://45.65.224.74:999 | AR | 4744 | 7 | 45/54 |
| http://140.238.32.108:3128 | JP | 4026 | 7 | 109/188 |
| http://144.124.251.24:10605 | NL | 703 | 7 | 76/121 |
| http://144.124.251.24:11266 | NL | 734 | 7 | 78/121 |
| http://16.51.5.77:16637 | AU | 6784 | 6 | 35/129 |
| http://111.196.24.150:8888 | CN | 3442 | 6 | 22/39 |
| http://123.121.122.125:8888 | CN | 1684 | 6 | 9/12 |
| http://43.99.60.244:8089 | HK | 959 | 6 | 73/139 |
| http://144.124.251.24:10566 | NL | 705 | 6 | 78/122 |
| http://202.62.57.235:8080 | KH | 2667 | 5 | 29/138 |
| http://128.199.116.219:9090 | SG | 972 | 5 | 84/108 |
| http://167.172.76.176:9090 | SG | 1142 | 5 | 109/150 |
| http://35.43.85.195:443 | ?? | 2865 | 5 | 5/5 |
| http://45.155.226.177:3128 | ?? | 1707 | 5 | 5/5 |
| http://85.132.108.42:3128 | AZ | 4100 | 4 | 6/7 |
| http://102.244.78.61:8085 | CM | 3013 | 4 | 62/79 |
| http://102.244.78.61:8088 | CM | 2129 | 4 | 61/77 |
| http://123.121.73.146:8888 | CN | 2361 | 4 | 7/11 |
| http://204.199.106.226:999 | CO | 2389 | 4 | 11/12 |
| http://15.217.107.97:9675 | ES | 1521 | 4 | 20/88 |
| http://198.244.254.77:3128 | GB | 4317 | 4 | 61/73 |
| http://38.199.88.1:999 | GT | 1747 | 4 | 6/9 |
| http://15.232.45.244:3127 | ID | 3360 | 4 | 42/149 |
| http://103.122.64.156:8080 | ID | 3887 | 4 | 31/131 |
| http://185.166.27.208:2020 | IQ | 5867 | 4 | 16/23 |
| http://52.195.147.51:3128 | JP | 3616 | 4 | 52/153 |
| http://43.202.114.177:7428 | KR | 5630 | 4 | 45/103 |
| http://192.81.249.2:999 | MX | 2675 | 4 | 5/7 |
| http://144.124.251.24:10230 | NL | 947 | 4 | 76/136 |
| http://144.124.251.24:10346 | NL | 804 | 4 | 72/121 |
| http://144.124.251.24:10829 | NL | 851 | 4 | 73/121 |
| http://144.124.251.24:11265 | NL | 948 | 4 | 79/137 |
| http://144.124.251.24:11491 | NL | 774 | 4 | 74/137 |
| http://119.93.207.214:8082 | PH | 4664 | 4 | 46/181 |
| http://180.191.121.186:8181 | PH | 7635 | 4 | 15/26 |
| http://185.140.103.1:8080 | PL | 5280 | 4 | 9/20 |
| http://185.238.238.169:58080 | PL | 5673 | 4 | 57/111 |
| http://192.203.0.198:999 | PR | 794 | 4 | 23/85 |
| http://128.199.121.61:9090 | SG | 1076 | 4 | 83/109 |
| http://98.94.14.234:36508 | US | 1063 | 4 | 45/149 |
| http://89.104.102.209:58080 | UZ | 5658 | 4 | 25/133 |
| http://38.63.98.32:999 | VE | 6136 | 4 | 28/77 |
| http://161.22.33.185:999 | VE | 6554 | 4 | 18/64 |
| http://52.128.238.98:18080 | ?? | 1052 | 4 | 4/4 |
| socks5://103.119.1.160:5555 | ?? | 1189 | 4 | 4/4 |
| http://16.26.208.68:1256 | AU | 2674 | 3 | 30/129 |
| http://203.76.220.126:16464 | BD | 6725 | 3 | 40/185 |
| http://177.55.68.68:8080 | BR | 6362 | 3 | 16/109 |
| http://102.244.78.61:8081 | CM | 2136 | 3 | 61/75 |
| http://102.244.78.61:8083 | CM | 2263 | 3 | 61/77 |
| http://102.244.78.61:8087 | CM | 2751 | 3 | 59/79 |
| http://101.251.204.174:8080 | CN | 1652 | 3 | 96/175 |
| http://221.221.164.42:8888 | CN | 1823 | 3 | 7/12 |
| http://38.19.41.227:999 | CO | 3397 | 3 | 7/20 |
| http://45.65.138.48:999 | CO | 3509 | 3 | 90/189 |
| http://46.232.249.209:40001 | DE | 1876 | 3 | 11/29 |
| http://63.180.203.233:37086 | DE | 2167 | 3 | 44/149 |
| http://45.185.163.111:999 | EC | 6570 | 3 | 7/9 |
| http://177.234.217.93:999 | EC | 4422 | 3 | 35/48 |
| http://177.234.217.235:999 | EC | 3934 | 3 | 79/158 |
| http://185.174.80.7:3128 | ES | 6053 | 3 | 36/158 |
| http://188.164.201.197:666 | GR | 4944 | 3 | 33/73 |
| http://179.49.113.230:999 | HN | 2252 | 3 | 30/120 |
| http://101.255.151.246:8080 | ID | 2583 | 3 | 8/14 |
| http://103.141.150.147:8080 | ID | 5303 | 3 | 19/70 |
| http://103.158.210.80:8082 | ID | 3133 | 3 | 56/179 |
| http://103.175.202.182:8090 | ID | 6570 | 3 | 20/101 |
| http://103.227.187.3:6090 | ID | 4413 | 3 | 22/99 |
| http://157.66.3.20:1111 | ID | 5353 | 3 | 23/95 |
| http://45.174.175.27:999 | MX | 3799 | 3 | 42/151 |
| http://189.51.168.165:999 | MX | 3435 | 3 | 93/101 |
| http://144.124.251.24:10412 | NL | 835 | 3 | 67/121 |
| http://144.124.251.24:10453 | NL | 746 | 3 | 77/126 |
| http://144.124.251.24:10601 | NL | 773 | 3 | 72/136 |
| http://144.124.251.24:10610 | NL | 727 | 3 | 72/121 |
| http://144.124.251.24:10631 | NL | 896 | 3 | 73/121 |
| http://144.124.251.24:10800 | NL | 874 | 3 | 74/121 |
| http://144.124.251.24:10818 | NL | 736 | 3 | 65/121 |
| http://112.208.174.83:8080 | PH | 7814 | 3 | 30/75 |
| http://157.20.142.34:9595 | PH | 6864 | 3 | 6/23 |
| http://92.86.207.198:8080 | RO | 7440 | 3 | 36/181 |
| http://82.138.122.43:80 | TR | 5527 | 3 | 39/153 |
