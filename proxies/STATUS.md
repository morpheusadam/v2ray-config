# Proxy status

Generated 2026-10-28T23:30:25Z by `harvest.py`.

- **2296** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4638** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39861** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 160/600 (27%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2791 |
| socks5 | 1843 |
| socks4 | 4 |

| country | entries |
|---|---|
| NL | 1650 |
| ID | 906 |
| ?? | 233 |
| PH | 149 |
| CO | 122 |
| US | 106 |
| MX | 105 |
| RU | 82 |
| VE | 81 |
| TH | 76 |
| BR | 71 |
| CN | 71 |
| BD | 65 |
| EC | 63 |
| TR | 60 |
| IN | 54 |
| VN | 47 |
| AR | 44 |
| DO | 41 |
| SG | 36 |
| PE | 31 |
| ZA | 31 |
| EG | 28 |
| JP | 28 |
| PK | 26 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 1 | 2026-10-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 54 | 54 | 13 | 2026-10-28 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 106 | 106 | 49 | 2026-10-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 130 | 130 | 89 | 2026-10-28 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 68 | 2026-10-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 155 | 155 | 4 | 2026-10-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-28 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 286 | 286 | 76 | 2026-10-28 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 477 | 477 | 252 | 2026-10-28 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 517 | 517 | 175 | 2026-10-28 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-28 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 455 | 2026-10-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1139 | 2026-10-28 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1642 | 1642 | 96 | 2026-10-28 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1592 | 2026-10-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2488 | 2488 | 648 | 2026-10-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2974 | 2974 | 1912 | 2026-10-28 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3532 | 3532 | 993 | 2026-10-28 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 79997 | 79997 | 65826 | 2026-10-28 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 86877 | 86876 | 2929 | 2026-10-28 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 866 | 78 | 145/158 |
| http://149.130.173.58:9443 | CO | 1477 | 69 | 69/69 |
| http://190.0.246.213:4040 | CO | 494 | 52 | 115/123 |
| http://103.237.102.191:11111 | DE | 856 | 45 | 151/158 |
| http://45.186.6.104:3128 | EC | 2611 | 39 | 129/136 |
| http://103.133.26.73:3128 | ID | 1601 | 34 | 54/136 |
| http://103.133.26.119:8080 | ID | 1883 | 34 | 38/68 |
| http://176.111.37.5:39811 | HK | 804 | 29 | 139/158 |
| http://34.43.46.91:80 | US | 485 | 28 | 152/158 |
| http://4.144.146.21:80 | SG | 1147 | 26 | 43/50 |
| http://190.0.246.210:4040 | CO | 621 | 25 | 144/157 |
| http://43.155.62.157:443 | HK | 1239 | 25 | 53/61 |
| http://102.244.78.61:8081 | CM | 1190 | 24 | 37/44 |
| http://186.5.94.206:999 | EC | 769 | 23 | 111/120 |
| http://189.51.168.165:999 | MX | 358 | 22 | 65/70 |
| http://176.111.37.216:39811 | HK | 1846 | 21 | 130/158 |
| http://103.130.61.61:8081 | ID | 2613 | 20 | 128/158 |
| http://103.133.26.50:8080 | ID | 1502 | 18 | 37/59 |
| socks5://67.207.92.87:1088 | US | 334 | 13 | 99/157 |
| socks5://69.55.49.177:38182 | US | 153 | 13 | 13/13 |
| socks5://101.36.104.46:10808 | JP | 1587 | 12 | 137/158 |
| http://89.167.124.218:8888 | DE | 840 | 11 | 11/11 |
| http://102.244.78.61:8085 | CM | 1190 | 10 | 37/48 |
| http://102.244.78.61:8087 | CM | 1210 | 10 | 36/48 |
| http://43.202.114.177:7428 | KR | 2993 | 9 | 32/72 |
| http://187.102.219.42:999 | AR | 6477 | 8 | 87/153 |
| socks5://47.238.126.208:1080 | HK | 1235 | 8 | 34/63 |
| http://51.15.20.32:3129 | NL | 532 | 7 | 18/22 |
| http://34.43.46.91:443 | US | 638 | 7 | 147/158 |
| http://45.65.226.169:999 | AR | 3520 | 6 | 15/20 |
| http://123.200.8.170:10000 | BD | 7131 | 6 | 66/156 |
| http://190.7.138.78:8080 | CO | 4952 | 6 | 42/87 |
| http://34.88.38.81:9443 | FI | 762 | 6 | 85/123 |
| http://35.228.49.168:9443 | FI | 579 | 6 | 66/95 |
| http://103.194.47.53:8082 | ID | 3144 | 6 | 37/127 |
| http://140.238.32.108:3128 | JP | 5976 | 6 | 85/157 |
| http://200.94.38.45:2604 | MX | 7542 | 6 | 24/47 |
| http://154.59.56.72:999 | VE | 5933 | 6 | 85/117 |
| socks5://213.199.47.140:1080 | FR | 6829 | 6 | 98/124 |
| socks5://103.100.158.115:10809 | JP | 3548 | 6 | 37/46 |
| socks5://103.182.22.221:9000 | ?? | 5332 | 6 | 7/10 |
| http://45.65.226.173:999 | AR | 2844 | 5 | 9/19 |
| http://187.102.219.34:999 | AR | 1085 | 5 | 60/109 |
| http://40.177.104.199:48086 | CA | 2224 | 5 | 35/125 |
| http://184.70.113.34:3128 | CA | 3783 | 5 | 39/156 |
| http://16.18.22.211:9090 | CH | 4461 | 5 | 37/118 |
| http://101.251.204.174:8080 | CN | 2038 | 5 | 79/144 |
| http://123.119.25.143:8888 | CN | 7781 | 5 | 54/123 |
| http://123.121.122.28:8888 | CN | 1745 | 5 | 64/107 |
| http://45.71.186.214:999 | EC | 2109 | 5 | 44/104 |
| http://119.93.207.214:8082 | PH | 4290 | 5 | 31/150 |
| http://167.172.76.176:9090 | SG | 1144 | 5 | 82/119 |
| http://103.131.19.42:8181 | ?? | 5403 | 5 | 6/13 |
| socks5://101.36.104.239:10808 | JP | 1261 | 5 | 134/158 |
| socks5://193.218.118.128:1080 | UA | 7457 | 5 | 11/14 |
| http://18.230.23.72:25761 | BR | 2947 | 4 | 36/118 |
| http://131.196.50.128:8080 | BR | 1887 | 4 | 18/81 |
| http://16.174.124.173:425 | CA | 1874 | 4 | 28/126 |
| http://114.244.221.178:8888 | CN | 1405 | 4 | 39/81 |
| http://123.119.179.34:8888 | CN | 3818 | 4 | 45/120 |
| http://221.221.163.120:8888 | CN | 4049 | 4 | 43/111 |
| http://45.71.186.210:999 | EC | 5396 | 4 | 48/132 |
| http://177.234.221.202:999 | EC | 2351 | 4 | 35/62 |
| http://45.245.208.180:8080 | EG | 2297 | 4 | 24/31 |
| http://188.164.201.197:666 | GR | 5332 | 4 | 16/42 |
| http://181.119.103.237:999 | GT | 2187 | 4 | 24/139 |
| http://36.64.54.98:8080 | ID | 5485 | 4 | 22/70 |
| http://45.198.20.223:8080 | ID | 4289 | 4 | 15/92 |
| http://103.35.216.34:8080 | ID | 6596 | 4 | 17/77 |
| http://103.38.101.194:1111 | ID | 5820 | 4 | 36/152 |
| http://103.46.186.126:8080 | ID | 6472 | 4 | 11/24 |
| http://103.50.25.40:8080 | ID | 3441 | 4 | 28/140 |
| http://103.55.22.236:8080 | ID | 4514 | 4 | 21/147 |
| http://103.122.0.52:8181 | ID | 7686 | 4 | 20/70 |
| http://103.156.57.135:9988 | ID | 7828 | 4 | 26/98 |
| http://103.172.35.40:8080 | ID | 3435 | 4 | 17/70 |
| http://103.175.237.232:8080 | ID | 5677 | 4 | 18/78 |
| http://103.176.96.84:8082 | ID | 4021 | 4 | 24/96 |
| http://108.137.124.195:8998 | ID | 2306 | 4 | 26/117 |
| http://121.101.133.96:8080 | ID | 5591 | 4 | 17/66 |
| http://160.25.119.29:8080 | ID | 5075 | 4 | 27/97 |
| http://202.73.27.115:8080 | ID | 3446 | 4 | 13/31 |
| http://51.16.4.39:1461 | IL | 3081 | 4 | 34/142 |
| http://138.186.201.77:8083 | MX | 3561 | 4 | 27/79 |
| http://200.94.38.42:2604 | MX | 7385 | 4 | 25/51 |
| http://191.44.71.208:8080 | NL | 5809 | 4 | 17/37 |
| http://130.110.103.245:3128 | SA | 1269 | 4 | 140/158 |
| http://104.129.203.85:9480 | US | 2089 | 4 | 11/34 |
| http://165.154.162.73:8888 | US | 579 | 4 | 103/158 |
| http://154.59.56.74:999 | VE | 4973 | 4 | 79/121 |
| http://154.59.56.76:999 | VE | 5478 | 4 | 85/118 |
| http://16.28.101.55:10015 | ZA | 2093 | 4 | 4/4 |
| http://49.149.195.243:8081 | ?? | 7097 | 4 | 4/4 |
| http://181.119.86.132:999 | ?? | 4159 | 4 | 4/4 |
| socks5://49.13.22.249:10805 | DE | 6824 | 4 | 44/76 |
| socks5://121.169.46.116:1090 | KR | 2566 | 4 | 108/158 |
| socks5://45.61.129.165:9050 | US | 1742 | 4 | 118/158 |
| socks5://45.61.188.134:44499 | US | 261 | 4 | 60/125 |
| socks5://193.25.215.182:22222 | US | 760 | 4 | 131/158 |
| socks5://103.100.235.25:1080 | ?? | 3938 | 4 | 5/6 |
