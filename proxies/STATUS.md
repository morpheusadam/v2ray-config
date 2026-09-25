# Proxy status

Generated 2026-09-25T22:47:44Z by `harvest.py`.

- **2588** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4350** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **37933** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 168/600 (28%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| socks5 | 2296 |
| http | 2045 |
| socks4 | 9 |

| country | entries |
|---|---|
| NL | 2049 |
| ID | 446 |
| ?? | 445 |
| US | 153 |
| CN | 107 |
| RU | 76 |
| MX | 62 |
| CO | 57 |
| BR | 55 |
| IN | 54 |
| DE | 53 |
| VE | 47 |
| BD | 45 |
| PH | 43 |
| JP | 42 |
| SG | 34 |
| VN | 33 |
| EC | 31 |
| HK | 30 |
| DO | 28 |
| EG | 27 |
| FR | 27 |
| KH | 24 |
| AU | 21 |
| PK | 21 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 2 | 2026-09-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 25 | 25 | 10 | 2026-09-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 93 | 93 | 46 | 2026-09-25 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 80 | 2026-09-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 113 | 113 | 34 | 2026-09-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 128 | 128 | 30 | 2026-09-25 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 79 | 2026-09-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 152 | 152 | 63 | 2026-09-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-09-25 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 349 | 349 | 103 | 2026-09-25 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-25 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 528 | 2026-09-25 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 454 | 2026-09-25 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 820 | 820 | 191 | 2026-09-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1147 | 2026-09-25 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1589 | 2026-09-25 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1925 | 1921 | 390 | 2026-09-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2436 | 2435 | 709 | 2026-09-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2788 | 2786 | 2001 | 2026-09-25 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2893 | 2892 | 558 | 2026-09-25 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 21922 | 21922 | 11141 | 2026-09-25 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 28767 | 28766 | 2805 | 2026-09-25 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1170 | 79 | 92/93 |
| http://130.110.103.245:3128 | SA | 1587 | 79 | 91/93 |
| http://1.231.81.166:3128 | KR | 6917 | 58 | 90/93 |
| http://190.97.236.128:999 | VE | 867 | 50 | 81/83 |
| http://190.97.236.129:999 | VE | 869 | 50 | 81/83 |
| http://95.3.69.222:8080 | TR | 1521 | 48 | 90/93 |
| http://38.51.207.104:8080 | VE | 1800 | 26 | 33/34 |
| http://193.104.179.115:3128 | UZ | 1434 | 23 | 41/58 |
| http://190.0.246.213:4040 | CO | 762 | 22 | 51/58 |
| http://213.111.146.36:18080 | NL | 753 | 22 | 25/30 |
| http://153.51.201.35:999 | VE | 903 | 20 | 20/20 |
| http://144.124.251.24:10007 | NL | 821 | 17 | 24/42 |
| http://144.124.251.24:10008 | NL | 2702 | 17 | 20/24 |
| http://144.124.251.24:10104 | NL | 1092 | 17 | 20/25 |
| http://144.124.251.24:10176 | NL | 769 | 17 | 24/41 |
| http://144.124.251.24:10185 | NL | 928 | 17 | 21/25 |
| http://144.124.251.24:10216 | NL | 782 | 17 | 25/42 |
| http://144.124.251.24:10226 | NL | 852 | 17 | 19/24 |
| http://144.124.251.24:10333 | NL | 742 | 17 | 23/42 |
| http://144.124.251.24:10346 | NL | 817 | 17 | 21/25 |
| http://144.124.251.24:10366 | NL | 833 | 17 | 22/39 |
| http://144.124.251.24:10372 | NL | 1150 | 17 | 24/37 |
| http://144.124.251.24:10431 | NL | 813 | 17 | 26/41 |
| http://144.124.251.24:10453 | NL | 814 | 17 | 23/30 |
| http://144.124.251.24:10551 | NL | 874 | 17 | 25/41 |
| http://144.124.251.24:10574 | NL | 748 | 17 | 25/42 |
| http://144.124.251.24:10771 | NL | 836 | 17 | 20/25 |
| http://144.124.251.24:10953 | NL | 951 | 17 | 21/25 |
| http://144.124.251.24:11011 | NL | 928 | 17 | 21/25 |
| http://144.124.251.24:11265 | NL | 844 | 17 | 24/41 |
| http://144.124.251.24:11266 | NL | 822 | 17 | 21/25 |
| http://144.124.251.24:11274 | NL | 925 | 17 | 24/41 |
| http://144.124.251.24:11480 | NL | 772 | 17 | 19/25 |
| http://144.124.251.24:11491 | NL | 786 | 17 | 24/41 |
| socks5://83.147.217.103:1080 | US | 506 | 16 | 16/16 |
| http://144.124.251.24:10801 | NL | 1026 | 15 | 21/41 |
| socks5://213.199.47.140:1080 | FR | 1708 | 15 | 51/59 |
| socks5://185.87.255.54:1080 | GB | 1055 | 14 | 14/14 |
| socks5://101.36.104.239:10808 | JP | 1986 | 14 | 77/93 |
| http://190.0.246.211:4040 | CO | 1208 | 13 | 80/93 |
| http://144.124.251.24:10082 | NL | 868 | 13 | 23/41 |
| http://167.172.76.176:9090 | SG | 909 | 13 | 35/54 |
| socks5://103.75.118.84:1080 | JP | 873 | 13 | 67/88 |
| http://144.124.251.24:10261 | NL | 951 | 12 | 20/25 |
| http://128.199.116.219:9090 | SG | 892 | 12 | 12/12 |
| socks5://101.36.104.46:10808 | JP | 958 | 12 | 83/93 |
| http://213.32.70.99:3128 | FR | 1652 | 11 | 11/11 |
| http://154.59.56.76:999 | VE | 5002 | 11 | 42/53 |
| http://181.119.224.25:8080 | EC | 941 | 10 | 10/10 |
| http://197.224.185.3:3128 | MU | 2335 | 10 | 56/61 |
| http://144.124.251.24:10084 | NL | 1279 | 10 | 20/25 |
| http://144.124.251.24:10088 | NL | 925 | 10 | 19/25 |
| http://144.124.251.24:10412 | NL | 1057 | 10 | 20/25 |
| http://144.124.251.24:10471 | NL | 953 | 10 | 24/40 |
| http://144.124.251.24:10566 | NL | 758 | 10 | 21/26 |
| http://144.124.251.24:10605 | NL | 989 | 10 | 20/25 |
| http://144.124.251.24:10610 | NL | 1233 | 10 | 20/25 |
| http://144.124.251.24:10631 | NL | 983 | 10 | 20/25 |
| http://144.124.251.24:10658 | NL | 981 | 10 | 20/25 |
| http://144.124.251.24:10689 | NL | 795 | 10 | 21/29 |
| http://144.124.251.24:10800 | NL | 808 | 10 | 20/25 |
| http://144.124.251.24:10811 | NL | 1080 | 10 | 20/25 |
| http://144.124.251.24:10818 | NL | 1566 | 10 | 17/25 |
| http://144.124.251.24:11450 | NL | 1090 | 10 | 18/25 |
| http://34.43.46.91:80 | US | 1417 | 10 | 89/93 |
| http://190.0.246.210:4040 | CO | 1136 | 9 | 81/92 |
| http://103.237.102.191:11111 | DE | 1335 | 9 | 87/93 |
| http://35.78.212.217:32053 | JP | 2168 | 9 | 19/75 |
| http://154.59.56.73:999 | VE | 7326 | 9 | 52/65 |
| http://190.97.236.130:999 | VE | 7483 | 9 | 19/22 |
| http://200.229.65.172:3128 | BR | 1067 | 8 | 8/8 |
| http://38.7.195.50:999 | CL | 2861 | 8 | 27/52 |
| http://18.157.123.132:3128 | DE | 831 | 8 | 40/54 |
| http://3.216.199.128:3128 | US | 457 | 8 | 8/8 |
| socks5://109.205.182.143:1088 | FR | 1070 | 8 | 8/8 |
| socks5://107.167.18.122:443 | US | 107 | 8 | 43/45 |
| http://120.232.115.57:17981 | CN | 1246 | 7 | 14/18 |
| http://34.88.38.81:9443 | FI | 866 | 7 | 40/58 |
| http://35.228.49.168:9443 | FI | 896 | 7 | 21/30 |
| http://140.238.32.108:3128 | JP | 2749 | 7 | 44/92 |
| socks5://144.91.121.61:1088 | FR | 3037 | 7 | 79/93 |
| http://91.233.223.147:3128 | RU | 1254 | 6 | 20/67 |
| http://34.43.46.91:443 | US | 1823 | 6 | 87/93 |
| socks5://185.87.255.47:1080 | GB | 968 | 6 | 11/12 |
| socks5://103.88.234.239:40002 | MX | 594 | 6 | 12/16 |
| http://123.115.226.82:8888 | CN | 953 | 5 | 14/39 |
| http://123.121.132.32:8888 | CN | 1575 | 5 | 23/54 |
| http://125.33.195.27:8888 | CN | 1329 | 5 | 17/39 |
| http://222.128.171.2:8888 | CN | 1402 | 5 | 25/45 |
| http://134.199.191.115:3128 | DE | 5476 | 5 | 5/5 |
| http://189.51.168.165:999 | MX | 733 | 5 | 5/5 |
| http://144.124.251.24:10000 | NL | 951 | 5 | 24/39 |
| http://144.124.251.24:10187 | NL | 820 | 5 | 20/39 |
| http://144.124.251.24:10230 | NL | 808 | 5 | 23/40 |
| http://144.124.251.24:10829 | NL | 963 | 5 | 19/25 |
| http://144.124.251.24:11108 | NL | 808 | 5 | 21/40 |
| http://144.124.251.24:11124 | NL | 868 | 5 | 22/42 |
| http://144.124.251.24:11180 | NL | 1070 | 5 | 19/24 |
| socks5://141.148.206.170:1088 | IN | 1892 | 5 | 10/13 |
| socks5://23.239.30.204:1088 | US | 5331 | 5 | 5/5 |
