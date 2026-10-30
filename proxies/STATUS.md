# Proxy status

Generated 2026-10-30T18:44:53Z by `harvest.py`.

- **2870** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5347** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **33454** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 189/600 (32%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2714 |
| http | 2631 |
| socks4 | 2 |

| country | entries |
|---|---|
| NL | 2377 |
| ID | 809 |
| ?? | 529 |
| PH | 119 |
| CO | 109 |
| MX | 104 |
| US | 87 |
| RU | 75 |
| VE | 65 |
| CN | 62 |
| TH | 61 |
| TR | 54 |
| BR | 53 |
| BD | 52 |
| EC | 49 |
| DO | 43 |
| AR | 40 |
| IN | 40 |
| SG | 35 |
| PK | 34 |
| PE | 31 |
| EG | 28 |
| JP | 26 |
| KH | 26 |
| VN | 24 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 10 | 10 | 4 | 2026-10-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-10-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 103 | 103 | 48 | 2026-10-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 105 | 105 | 24 | 2026-10-30 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 62 | 2026-10-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 176 | 176 | 43 | 2026-10-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 208 | 208 | 125 | 2026-10-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-30 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 314 | 314 | 94 | 2026-10-30 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-10-30 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-30 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 448 | 2026-10-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 740 | 740 | 217 | 2026-10-30 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 945 | 945 | 354 | 2026-10-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1126 | 2026-10-30 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1646 | 1646 | 108 | 2026-10-30 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1594 | 2026-10-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2521 | 2521 | 657 | 2026-10-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 3065 | 3065 | 1959 | 2026-10-30 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 4331 | 4331 | 1392 | 2026-10-30 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 4862 | 4862 | 3711 | 2026-10-30 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10871 | 10870 | 2557 | 2026-10-30 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 976 | 81 | 148/161 |
| http://149.130.173.58:9443 | CO | 692 | 72 | 72/72 |
| http://103.237.102.191:11111 | DE | 875 | 48 | 154/161 |
| http://45.186.6.104:3128 | EC | 931 | 42 | 132/139 |
| http://103.133.26.73:3128 | ID | 1244 | 37 | 57/139 |
| http://103.133.26.119:8080 | ID | 1571 | 37 | 41/71 |
| http://176.111.37.5:39811 | HK | 1228 | 32 | 142/161 |
| http://34.43.46.91:80 | US | 566 | 31 | 155/161 |
| http://4.144.146.21:80 | SG | 951 | 29 | 46/53 |
| http://190.0.246.210:4040 | CO | 835 | 28 | 147/160 |
| http://186.5.94.206:999 | EC | 7799 | 26 | 114/123 |
| http://189.51.168.165:999 | MX | 658 | 25 | 68/73 |
| http://176.111.37.216:39811 | HK | 1131 | 24 | 133/161 |
| http://103.130.61.61:8081 | ID | 1849 | 23 | 131/161 |
| http://103.133.26.50:8080 | ID | 1206 | 21 | 40/62 |
| socks5://67.207.92.87:1088 | US | 654 | 16 | 102/160 |
| socks5://47.238.126.208:1080 | HK | 1271 | 11 | 37/66 |
| http://51.15.20.32:3129 | NL | 6385 | 10 | 21/25 |
| http://34.43.46.91:443 | US | 613 | 10 | 150/161 |
| http://34.88.38.81:9443 | FI | 1032 | 9 | 88/126 |
| http://35.228.49.168:9443 | FI | 887 | 9 | 69/98 |
| socks5://103.100.158.115:10809 | JP | 1122 | 9 | 40/49 |
| http://101.251.204.174:8080 | CN | 1769 | 8 | 82/147 |
| http://167.172.76.176:9090 | SG | 859 | 8 | 85/122 |
| socks5://101.36.104.239:10808 | JP | 1245 | 8 | 137/161 |
| socks5://193.218.118.128:1080 | UA | 2566 | 8 | 14/17 |
| http://51.16.4.39:1461 | IL | 2225 | 7 | 37/145 |
| http://130.110.103.245:3128 | SA | 1487 | 7 | 143/161 |
| http://154.59.56.74:999 | VE | 3889 | 7 | 82/124 |
| socks5://49.13.22.249:10805 | DE | 4052 | 7 | 47/79 |
| socks5://45.61.129.165:9050 | US | 1413 | 7 | 121/161 |
| socks5://45.61.188.134:44499 | US | 591 | 7 | 63/128 |
| socks5://193.25.215.182:22222 | US | 1871 | 7 | 134/161 |
| http://185.238.236.226:58080 | PL | 5354 | 6 | 33/83 |
| http://188.132.221.186:8080 | TR | 5486 | 6 | 22/99 |
| socks5://45.149.92.160:1080 | HK | 1038 | 6 | 19/28 |
| socks5://45.74.31.47:5304 | NL | 3520 | 6 | 8/23 |
| http://45.65.226.174:999 | AR | 5857 | 5 | 12/22 |
| http://123.121.134.192:8888 | CN | 4315 | 5 | 12/27 |
| http://177.234.217.92:999 | EC | 1847 | 5 | 7/10 |
| http://18.175.170.244:51141 | GB | 2071 | 5 | 6/9 |
| http://103.172.42.161:1111 | ID | 4272 | 5 | 14/95 |
| http://103.208.103.30:8080 | ID | 2299 | 5 | 8/16 |
| socks5://124.248.177.44:1080 | KH | 4136 | 5 | 36/150 |
| socks5://45.74.31.46:7333 | NL | 3100 | 5 | 5/5 |
| socks5://88.201.248.85:1080 | RU | 5643 | 5 | 10/16 |
| http://15.229.149.81:3128 | BR | 2836 | 4 | 41/71 |
| http://35.183.78.223:35766 | CA | 1632 | 4 | 4/4 |
| http://114.249.232.222:8888 | CN | 1639 | 4 | 48/126 |
| http://177.234.217.85:999 | EC | 4093 | 4 | 7/16 |
| http://177.234.217.235:999 | EC | 5753 | 4 | 62/130 |
| http://38.103.250.205:8080 | ID | 1164 | 4 | 22/124 |
| http://103.133.26.72:8080 | ID | 2512 | 4 | 41/87 |
| http://103.168.254.198:8080 | ID | 3344 | 4 | 15/25 |
| http://187.102.211.202:3128 | PE | 4356 | 4 | 25/71 |
| http://160.250.6.18:8082 | PH | 3161 | 4 | 22/74 |
| http://128.199.121.61:9090 | SG | 871 | 4 | 64/81 |
| http://64.118.155.2:22222 | US | 349 | 4 | 12/15 |
| http://16.28.101.55:2080 | ZA | 3220 | 4 | 33/101 |
| http://1.10.248.235:80 | ?? | 2018 | 4 | 4/4 |
| http://1.20.101.25:80 | ?? | 2628 | 4 | 4/4 |
| http://38.211.68.83:999 | ?? | 3677 | 4 | 4/4 |
| http://157.15.112.14:8082 | ?? | 1314 | 4 | 4/4 |
| http://157.66.36.129:8080 | ?? | 1186 | 4 | 5/6 |
| http://160.191.180.95:8089 | ?? | 6817 | 4 | 4/4 |
| http://187.245.220.100:999 | ?? | 3361 | 4 | 4/4 |
| socks5://148.251.68.232:8888 | DE | 2253 | 4 | 23/40 |
| socks5://212.77.75.25:1088 | IT | 1147 | 4 | 49/61 |
| socks5://183.106.215.208:1080 | KR | 885 | 4 | 14/47 |
| socks5://45.74.31.40:10306 | NL | 5755 | 4 | 4/4 |
| socks5://45.74.31.40:9999 | NL | 7507 | 4 | 7/23 |
| socks5://45.74.31.41:8130 | NL | 3114 | 4 | 7/29 |
| socks5://45.74.31.41:8257 | NL | 2393 | 4 | 4/4 |
| socks5://45.74.31.42:6461 | NL | 4865 | 4 | 9/38 |
| socks5://45.74.31.42:6642 | NL | 7615 | 4 | 4/4 |
| socks5://45.74.31.46:6550 | NL | 5930 | 4 | 4/4 |
| socks5://45.74.31.46:7049 | NL | 3985 | 4 | 5/7 |
| socks5://45.74.31.46:7692 | NL | 3830 | 4 | 9/35 |
| socks5://45.74.31.46:9109 | NL | 4870 | 4 | 8/24 |
| socks5://45.74.31.46:9307 | NL | 6129 | 4 | 4/4 |
| socks5://45.74.31.47:8063 | NL | 3274 | 4 | 5/22 |
| socks5://45.74.31.47:9539 | NL | 2517 | 4 | 8/32 |
| socks5://185.9.73.44:1080 | RU | 3928 | 4 | 12/34 |
| socks5://43.155.143.227:1080 | ?? | 787 | 4 | 4/4 |
| http://103.60.173.173:8080 | BD | 4592 | 3 | 16/116 |
| http://103.118.85.144:6321 | BD | 3896 | 3 | 11/67 |
| http://190.124.252.129:6666 | BR | 7094 | 3 | 29/139 |
| http://36.213.79.159:1081 | CN | 2392 | 3 | 8/21 |
| http://114.246.203.194:8888 | CN | 1465 | 3 | 34/84 |
| http://114.249.219.180:8888 | CN | 3806 | 3 | 50/125 |
| http://120.232.115.57:17981 | CN | 1102 | 3 | 53/86 |
| http://123.121.114.234:8888 | CN | 1594 | 3 | 39/120 |
| http://123.121.209.108:8888 | CN | 1676 | 3 | 39/111 |
| http://38.19.43.185:999 | CO | 2642 | 3 | 22/74 |
| http://45.179.200.65:999 | CO | 5983 | 3 | 25/118 |
| http://181.48.159.22:3128 | CO | 1972 | 3 | 11/45 |
| http://181.78.19.82:999 | CO | 5225 | 3 | 27/105 |
| http://63.180.203.233:1976 | DE | 3354 | 3 | 21/73 |
| http://38.75.82.216:999 | DO | 4448 | 3 | 31/130 |
| http://181.78.195.136:999 | EC | 3778 | 3 | 13/17 |
