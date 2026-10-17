# Proxy status

Generated 2026-10-17T16:28:04Z by `harvest.py`.

- **2738** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **3998** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **38448** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 145/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2260 |
| http | 1733 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 2045 |
| ID | 479 |
| US | 92 |
| RU | 84 |
| CO | 77 |
| MX | 76 |
| PH | 76 |
| CN | 70 |
| ?? | 66 |
| BD | 61 |
| IN | 51 |
| VE | 51 |
| VN | 48 |
| BR | 43 |
| EC | 40 |
| SG | 35 |
| AR | 33 |
| DE | 33 |
| TH | 32 |
| TR | 32 |
| DO | 28 |
| JP | 28 |
| KH | 24 |
| PK | 24 |
| EG | 23 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 6 | 6 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 84 | 84 | 2 | 2026-10-17 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-10-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 120 | 120 | 55 | 2026-10-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 144 | 144 | 59 | 2026-10-17 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 77 | 2026-10-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 209 | 209 | 60 | 2026-10-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-17 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 299 | 299 | 111 | 2026-10-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 303 | 303 | 121 | 2026-10-17 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-17 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-10-17 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 452 | 2026-10-17 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 753 | 753 | 524 | 2026-10-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1138 | 2026-10-17 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1596 | 2026-10-17 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1947 | 1943 | 316 | 2026-10-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 1975 | 1973 | 750 | 2026-10-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2411 | 2409 | 1652 | 2026-10-17 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3053 | 3051 | 1522 | 2026-10-17 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 66448 | 66448 | 51832 | 2026-10-17 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 73271 | 73270 | 2536 | 2026-10-17 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 847 | 55 | 122/135 |
| http://149.130.173.58:9443 | CO | 551 | 46 | 46/46 |
| http://190.0.246.213:4040 | CO | 550 | 29 | 92/100 |
| http://197.224.185.3:3128 | MU | 1829 | 27 | 96/103 |
| http://103.237.102.191:11111 | DE | 1446 | 22 | 128/135 |
| http://203.252.142.217:80 | KR | 959 | 17 | 17/17 |
| http://45.186.6.104:3128 | EC | 2662 | 16 | 106/113 |
| socks5://101.36.104.46:10808 | JP | 1853 | 16 | 119/135 |
| http://3.211.120.181:443 | US | 160 | 15 | 29/46 |
| http://165.154.162.73:8888 | US | 3001 | 15 | 88/135 |
| http://102.244.78.61:8083 | CM | 1254 | 14 | 20/23 |
| http://103.130.61.61:8081 | ID | 1697 | 14 | 106/135 |
| http://102.244.78.61:8088 | CM | 1274 | 12 | 19/23 |
| http://5.129.254.5:8888 | RU | 1064 | 12 | 79/90 |
| http://5.129.254.49:8888 | RU | 1066 | 12 | 80/90 |
| http://5.129.254.51:8888 | RU | 1069 | 12 | 80/90 |
| http://5.129.254.60:8888 | RU | 1050 | 12 | 79/89 |
| http://5.129.254.70:8888 | RU | 1065 | 12 | 80/90 |
| http://5.129.254.129:8888 | RU | 1083 | 12 | 85/96 |
| http://5.129.254.154:8888 | RU | 1057 | 12 | 76/86 |
| http://5.129.254.215:8888 | RU | 1069 | 12 | 29/32 |
| http://5.129.254.243:8888 | RU | 1044 | 12 | 29/31 |
| http://103.133.26.50:8080 | ID | 1461 | 11 | 15/36 |
| http://103.133.26.72:8080 | ID | 1497 | 11 | 16/61 |
| http://103.133.26.73:3128 | ID | 1499 | 11 | 31/113 |
| http://103.133.26.119:8080 | ID | 1705 | 11 | 15/45 |
| socks5://67.207.92.87:1088 | US | 2060 | 11 | 79/134 |
| http://147.45.164.178:8888 | RU | 1018 | 9 | 9/9 |
| http://128.199.121.61:9090 | SG | 1082 | 7 | 45/55 |
| socks5://171.25.158.95:1080 | SE | 2928 | 7 | 42/50 |
| socks5://47.87.97.94:1080 | TH | 2026 | 7 | 10/11 |
| http://102.244.78.61:8082 | CM | 1286 | 6 | 19/24 |
| http://102.244.78.61:8086 | CM | 1236 | 6 | 18/23 |
| http://102.244.78.61:8089 | CM | 1270 | 6 | 17/23 |
| http://205.237.105.49:3129 | FR | 606 | 6 | 6/6 |
| http://198.244.254.77:3128 | GB | 3226 | 6 | 17/19 |
| http://176.111.37.5:39811 | HK | 1883 | 6 | 116/135 |
| http://34.43.46.91:443 | US | 2720 | 6 | 126/135 |
| http://38.7.195.53:999 | CL | 4484 | 5 | 47/134 |
| http://41.128.77.76:1976 | EG | 3044 | 5 | 40/101 |
| http://45.125.64.215:443 | HK | 2192 | 5 | 5/5 |
| http://176.111.37.216:39811 | HK | 984 | 5 | 108/135 |
| http://140.238.32.108:3128 | JP | 2155 | 5 | 68/134 |
| http://189.51.168.165:999 | MX | 2193 | 5 | 43/47 |
| http://34.43.46.91:80 | US | 2934 | 5 | 129/135 |
| http://154.59.56.73:999 | VE | 2870 | 5 | 79/107 |
| socks5://47.238.126.208:1080 | HK | 1860 | 5 | 23/40 |
| socks5://101.36.104.239:10808 | JP | 1428 | 5 | 114/135 |
| http://102.244.78.61:8080 | CM | 1256 | 4 | 19/24 |
| http://102.244.78.61:8084 | CM | 1276 | 4 | 18/23 |
| http://221.221.157.102:8888 | CN | 6599 | 4 | 36/87 |
| http://217.12.215.163:10808 | DE | 3183 | 4 | 19/117 |
| http://177.234.217.237:999 | EC | 2228 | 4 | 50/108 |
| http://181.78.194.249:999 | EC | 3126 | 4 | 42/118 |
| http://41.65.103.168:8080 | EG | 2393 | 4 | 11/23 |
| http://45.245.208.180:8080 | EG | 1055 | 4 | 7/8 |
| http://80.65.211.149:8888 | FR | 4746 | 4 | 7/14 |
| http://152.67.191.232:6800 | IN | 1147 | 4 | 4/4 |
| http://187.251.224.167:80 | MX | 4710 | 4 | 37/131 |
| http://49.229.100.235:8080 | TH | 1426 | 4 | 52/83 |
| http://61.91.162.126:8080 | TH | 1496 | 4 | 61/78 |
| http://103.10.231.189:8080 | TH | 1824 | 4 | 87/120 |
| socks5://94.183.170.105:1080 | EE | 7386 | 4 | 4/4 |
| socks5://43.245.199.34:1080 | HK | 1264 | 4 | 4/4 |
| http://45.65.226.40:999 | AR | 4204 | 3 | 4/11 |
| http://114.246.197.252:8888 | CN | 2567 | 3 | 15/54 |
| http://221.221.159.97:8888 | CN | 7935 | 3 | 41/88 |
| http://221.221.163.25:8888 | CN | 1737 | 3 | 33/89 |
| http://181.119.86.180:999 | CO | 5897 | 3 | 3/3 |
| http://177.234.217.45:999 | EC | 4102 | 3 | 23/66 |
| http://177.234.221.197:999 | EC | 6905 | 3 | 20/40 |
| http://177.234.221.201:999 | EC | 2802 | 3 | 13/38 |
| http://41.196.16.226:1976 | EG | 3405 | 3 | 3/3 |
| http://206.135.47.108:999 | MX | 7841 | 3 | 3/3 |
| http://206.135.47.110:999 | MX | 4421 | 3 | 5/6 |
| http://185.238.238.29:58080 | PL | 971 | 3 | 48/127 |
| http://46.161.49.174:10809 | RU | 1025 | 3 | 3/3 |
| http://109.225.40.145:58080 | RU | 3687 | 3 | 3/3 |
| http://4.144.146.21:80 | SG | 1111 | 3 | 20/27 |
| http://146.190.80.158:9090 | SG | 1083 | 3 | 44/61 |
| http://167.172.76.176:9090 | SG | 1100 | 3 | 66/96 |
| http://195.226.213.254:8888 | UA | 4474 | 3 | 47/133 |
| http://154.59.56.76:999 | VE | 2992 | 3 | 72/95 |
| http://200.59.191.27:999 | VE | 3092 | 3 | 86/130 |
| socks5://62.83.34.101:1080 | AT | 976 | 3 | 3/3 |
| socks5://103.239.201.50:58765 | PH | 4718 | 3 | 36/120 |
| socks5://149.40.242.118:1080 | PK | 3459 | 3 | 3/3 |
| socks5://87.236.23.100:1080 | RU | 1317 | 3 | 6/13 |
| socks5://52.128.241.106:1080 | US | 478 | 3 | 8/17 |
| socks5://113.22.224.63:1083 | VN | 1929 | 3 | 3/3 |
| http://186.22.246.60:3128 | AR | 6327 | 2 | 19/93 |
| http://186.38.100.130:999 | AR | 3800 | 2 | 6/10 |
| http://190.15.194.72:8080 | AR | 6083 | 2 | 4/5 |
| http://27.147.153.179:9249 | BD | 7798 | 2 | 2/2 |
| http://103.118.85.144:6321 | BD | 5156 | 2 | 7/41 |
| http://45.174.176.161:8087 | BR | 6959 | 2 | 5/14 |
| http://168.227.239.66:10000 | BR | 853 | 2 | 2/2 |
| http://38.7.195.52:999 | CL | 6006 | 2 | 53/117 |
| http://120.232.115.170:17981 | CN | 1791 | 2 | 95/134 |
| http://123.121.98.109:8888 | CN | 3630 | 2 | 2/2 |
