# Proxy status

Generated 2026-10-14T18:09:46Z by `harvest.py`.

- **1694** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4068** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **40000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 142/600 (24%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 2558 |
| socks5 | 1505 |
| socks4 | 5 |

| country | entries |
|---|---|
| NL | 1260 |
| ID | 770 |
| MX | 148 |
| PH | 146 |
| US | 127 |
| CO | 122 |
| RU | 108 |
| CN | 85 |
| VE | 82 |
| BD | 77 |
| BR | 74 |
| IN | 67 |
| VN | 66 |
| TR | 65 |
| EC | 55 |
| DO | 45 |
| SG | 42 |
| DE | 40 |
| TH | 37 |
| AR | 35 |
| JP | 33 |
| PK | 31 |
| ZA | 31 |
| PE | 29 |
| EG | 27 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 8 | 8 | 2 | 2026-10-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 83 | 83 | 39 | 2026-10-14 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-10-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 123 | 123 | 48 | 2026-10-14 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 80 | 2026-10-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 244 | 244 | 74 | 2026-10-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-10-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 282 | 282 | 95 | 2026-10-14 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 401 | 401 | 150 | 2026-10-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 176 | 2026-10-14 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-10-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 529 | 2026-10-14 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-10-14 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 835 | 835 | 648 | 2026-10-14 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 986 | 986 | 454 | 2026-10-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1143 | 2026-10-14 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1595 | 2026-10-14 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1960 | 1956 | 304 | 2026-10-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2066 | 2064 | 718 | 2026-10-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2457 | 2455 | 1676 | 2026-10-14 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2482 | 2480 | 933 | 2026-10-14 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 58328 | 58328 | 43644 | 2026-10-14 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 64228 | 64227 | 2055 | 2026-10-14 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://190.0.246.211:4040 | CO | 3485 | 49 | 116/129 |
| http://149.130.173.58:9443 | CO | 534 | 40 | 40/40 |
| http://190.0.246.213:4040 | CO | 5259 | 23 | 86/94 |
| http://144.124.251.24:10366 | NL | 767 | 23 | 52/75 |
| http://197.224.185.3:3128 | MU | 5460 | 21 | 90/97 |
| http://103.237.102.191:11111 | DE | 1681 | 16 | 122/129 |
| http://186.5.94.206:999 | EC | 2339 | 14 | 84/91 |
| http://203.252.142.217:80 | KR | 1022 | 11 | 11/11 |
| http://104.248.151.93:9090 | SG | 1049 | 11 | 27/30 |
| http://146.190.80.158:9090 | SG | 1041 | 11 | 39/55 |
| http://45.186.6.104:3128 | EC | 714 | 10 | 100/107 |
| http://144.124.251.24:10605 | NL | 774 | 10 | 50/61 |
| socks5://101.36.104.46:10808 | JP | 3689 | 10 | 113/129 |
| http://187.102.219.64:999 | AR | 7901 | 9 | 41/68 |
| http://144.124.251.24:10000 | NL | 737 | 9 | 53/75 |
| http://3.211.120.181:443 | US | 283 | 9 | 23/40 |
| http://165.154.162.73:8888 | US | 2457 | 9 | 82/129 |
| http://102.244.78.61:8083 | CM | 2326 | 8 | 14/17 |
| http://103.130.61.61:8081 | ID | 5023 | 8 | 100/129 |
| http://144.124.251.24:10261 | NL | 773 | 8 | 50/61 |
| http://144.124.251.24:10628 | NL | 694 | 8 | 48/61 |
| http://144.124.251.24:10771 | NL | 809 | 8 | 50/61 |
| http://144.124.251.24:11180 | NL | 774 | 8 | 49/60 |
| http://101.206.186.99:8080 | CN | 4574 | 7 | 55/129 |
| http://144.124.251.24:10811 | NL | 1042 | 7 | 49/61 |
| http://34.196.85.244:3128 | US | 308 | 7 | 7/7 |
| http://102.244.78.61:8080 | CM | 1350 | 6 | 14/18 |
| http://102.244.78.61:8088 | CM | 1487 | 6 | 13/17 |
| http://144.124.251.24:10187 | NL | 927 | 6 | 49/75 |
| http://144.124.251.24:10412 | NL | 885 | 6 | 48/61 |
| http://144.124.251.24:11265 | NL | 984 | 6 | 54/77 |
| http://5.129.254.5:8888 | RU | 1349 | 6 | 73/84 |
| http://5.129.254.49:8888 | RU | 1351 | 6 | 74/84 |
| http://5.129.254.51:8888 | RU | 1317 | 6 | 74/84 |
| http://5.129.254.60:8888 | RU | 3025 | 6 | 73/83 |
| http://5.129.254.70:8888 | RU | 1403 | 6 | 74/84 |
| http://5.129.254.129:8888 | RU | 1142 | 6 | 79/90 |
| http://5.129.254.154:8888 | RU | 2682 | 6 | 70/80 |
| http://5.129.254.215:8888 | RU | 1585 | 6 | 23/26 |
| http://5.129.254.243:8888 | RU | 1378 | 6 | 23/25 |
| socks5://110.38.233.122:1080 | PK | 2120 | 6 | 8/9 |
| socks5://116.101.14.169:1089 | VN | 2055 | 6 | 6/6 |
| http://38.7.195.49:999 | CL | 3655 | 5 | 46/103 |
| http://41.65.55.27:1981 | EG | 7244 | 5 | 24/69 |
| http://34.88.38.81:9443 | FI | 817 | 5 | 64/94 |
| http://35.228.49.168:9443 | FI | 736 | 5 | 45/66 |
| http://43.155.62.157:443 | HK | 3050 | 5 | 27/32 |
| http://103.133.26.50:8080 | ID | 1451 | 5 | 9/30 |
| http://103.133.26.72:8080 | ID | 2019 | 5 | 10/55 |
| http://103.133.26.73:3128 | ID | 1676 | 5 | 25/107 |
| http://103.133.26.119:8080 | ID | 1790 | 5 | 9/39 |
| http://144.124.251.24:10084 | NL | 778 | 5 | 48/61 |
| http://144.124.251.24:10176 | NL | 1001 | 5 | 53/77 |
| http://144.124.251.24:10185 | NL | 824 | 5 | 50/61 |
| http://144.124.251.24:10299 | NL | 800 | 5 | 48/61 |
| http://144.124.251.24:10566 | NL | 769 | 5 | 49/62 |
| http://144.124.251.24:10801 | NL | 757 | 5 | 48/77 |
| http://144.124.251.24:11491 | NL | 733 | 5 | 53/77 |
| http://66.210.33.34:8080 | US | 6618 | 5 | 10/37 |
| http://104.129.203.85:9480 | US | 476 | 5 | 5/5 |
| socks5://213.199.47.140:1080 | FR | 1353 | 5 | 75/95 |
| socks5://123.58.219.171:10808 | HK | 3027 | 5 | 101/129 |
| socks5://212.77.75.25:1088 | IT | 2460 | 5 | 26/29 |
| socks5://67.207.92.87:1088 | US | 1407 | 5 | 73/128 |
| socks5://193.25.215.182:22222 | US | 967 | 5 | 108/129 |
| http://138.117.14.237:9090 | AR | 7799 | 4 | 17/67 |
| http://186.38.100.130:999 | AR | 5771 | 4 | 4/4 |
| http://185.222.94.66:808 | AZ | 2537 | 4 | 8/26 |
| http://184.75.221.82:3118 | CA | 262 | 4 | 82/94 |
| http://177.234.217.88:999 | EC | 2995 | 4 | 46/121 |
| http://177.234.217.236:999 | EC | 4812 | 4 | 37/102 |
| http://181.119.107.80:3128 | GT | 6482 | 4 | 25/94 |
| http://45.198.11.164:9191 | ID | 2476 | 4 | 8/23 |
| http://122.176.158.103:80 | IN | 7082 | 4 | 7/15 |
| http://49.156.44.115:8080 | KH | 3232 | 4 | 27/95 |
| http://187.251.224.167:8081 | MX | 5423 | 4 | 19/89 |
| http://144.124.251.24:10008 | NL | 733 | 4 | 49/60 |
| http://144.124.251.24:10104 | NL | 739 | 4 | 46/61 |
| http://144.124.251.24:10346 | NL | 708 | 4 | 48/61 |
| http://144.124.251.24:10453 | NL | 1689 | 4 | 50/66 |
| http://144.124.251.24:10610 | NL | 1013 | 4 | 46/61 |
| http://144.124.251.24:10658 | NL | 842 | 4 | 46/61 |
| http://144.124.251.24:10818 | NL | 733 | 4 | 44/61 |
| http://144.124.251.24:10953 | NL | 1054 | 4 | 48/61 |
| http://144.124.251.24:11108 | NL | 769 | 4 | 51/76 |
| http://144.124.251.24:11450 | NL | 871 | 4 | 45/61 |
| http://144.124.251.24:11480 | NL | 751 | 4 | 47/61 |
| http://134.185.85.16:3128 | SG | 1266 | 4 | 4/4 |
| http://108.61.29.163:10001 | US | 1280 | 4 | 15/23 |
| http://173.205.202.33:8181 | US | 4743 | 4 | 7/12 |
| http://38.51.220.64:999 | VE | 5053 | 4 | 17/106 |
| socks5://45.74.31.46:5759 | NL | 6854 | 4 | 5/23 |
| socks5://138.2.216.186:1080 | US | 1691 | 4 | 32/123 |
| http://187.102.219.32:999 | AR | 6701 | 3 | 38/128 |
| http://187.102.219.34:999 | AR | 1206 | 3 | 42/80 |
| http://187.102.219.42:999 | AR | 7720 | 3 | 67/124 |
| http://103.122.142.174:8080 | BD | 7860 | 3 | 6/30 |
| http://165.101.222.18:8080 | BD | 7096 | 3 | 7/30 |
| http://18.228.228.159:3822 | BR | 2224 | 3 | 12/39 |
| http://168.195.168.182:8080 | BR | 2201 | 3 | 29/124 |
