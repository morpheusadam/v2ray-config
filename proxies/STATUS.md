# Proxy status

Generated 2026-09-27T17:34:55Z by `harvest.py`.

- **2047** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **4414** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **39622** endpoints on record
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
| socks5 | 2556 |
| http | 1848 |
| socks4 | 10 |

| country | entries |
|---|---|
| NL | 2334 |
| ID | 472 |
| ?? | 344 |
| CN | 121 |
| US | 121 |
| CO | 71 |
| RU | 71 |
| PH | 67 |
| MX | 65 |
| DE | 53 |
| IN | 45 |
| BD | 44 |
| BR | 43 |
| VE | 42 |
| EC | 34 |
| EG | 29 |
| VN | 28 |
| DO | 25 |
| SG | 24 |
| TR | 24 |
| PK | 23 |
| AR | 21 |
| FR | 20 |
| JP | 18 |
| TH | 18 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 4 | 4 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 29 | 29 | 9 | 2026-09-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 64 | 64 | 17 | 2026-09-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 97 | 97 | 44 | 2026-09-27 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 81 | 2026-09-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 110 | 110 | 38 | 2026-09-27 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 82 | 2026-09-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 198 | 198 | 67 | 2026-09-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 105 | 2026-09-27 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 353 | 353 | 158 | 2026-09-27 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-09-27 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-09-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-09-27 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 451 | 2026-09-27 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 1027 | 1027 | 527 | 2026-09-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1129 | 2026-09-27 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1586 | 2026-09-27 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1929 | 1925 | 1 | 2026-09-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2463 | 2461 | 1880 | 2026-09-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2711 | 2709 | 670 | 2026-09-27 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 3025 | 3023 | 528 | 2026-09-27 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 25895 | 25895 | 13131 | 2026-09-27 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 31848 | 31847 | 3098 | 2026-09-27 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://95.211.174.135:3128 | NL | 1263 | 82 | 95/96 |
| http://190.97.236.128:999 | VE | 798 | 53 | 84/86 |
| http://190.97.236.129:999 | VE | 856 | 53 | 84/86 |
| http://95.3.69.222:8080 | TR | 1396 | 51 | 93/96 |
| http://38.51.207.104:8080 | VE | 850 | 29 | 36/37 |
| http://190.0.246.213:4040 | CO | 597 | 25 | 54/61 |
| http://213.111.146.36:18080 | NL | 706 | 25 | 28/33 |
| http://153.51.201.35:999 | VE | 794 | 23 | 23/23 |
| http://144.124.251.24:10007 | NL | 730 | 20 | 27/45 |
| http://144.124.251.24:10008 | NL | 750 | 20 | 23/27 |
| http://144.124.251.24:10104 | NL | 749 | 20 | 23/28 |
| http://144.124.251.24:10176 | NL | 736 | 20 | 27/44 |
| http://144.124.251.24:10185 | NL | 719 | 20 | 24/28 |
| http://144.124.251.24:10216 | NL | 765 | 20 | 28/45 |
| http://144.124.251.24:10226 | NL | 727 | 20 | 22/27 |
| http://144.124.251.24:10333 | NL | 740 | 20 | 26/45 |
| http://144.124.251.24:10346 | NL | 724 | 20 | 24/28 |
| http://144.124.251.24:10366 | NL | 838 | 20 | 25/42 |
| http://144.124.251.24:10372 | NL | 855 | 20 | 27/40 |
| http://144.124.251.24:10431 | NL | 745 | 20 | 29/44 |
| http://144.124.251.24:10453 | NL | 724 | 20 | 26/33 |
| http://144.124.251.24:10551 | NL | 733 | 20 | 28/44 |
| http://144.124.251.24:10574 | NL | 875 | 20 | 28/45 |
| http://144.124.251.24:10771 | NL | 799 | 20 | 23/28 |
| http://144.124.251.24:10953 | NL | 712 | 20 | 24/28 |
| http://144.124.251.24:11011 | NL | 750 | 20 | 24/28 |
| http://144.124.251.24:11265 | NL | 708 | 20 | 27/44 |
| http://144.124.251.24:11266 | NL | 779 | 20 | 24/28 |
| http://144.124.251.24:11274 | NL | 730 | 20 | 27/44 |
| http://144.124.251.24:11480 | NL | 759 | 20 | 22/28 |
| http://144.124.251.24:11491 | NL | 714 | 20 | 27/44 |
| socks5://83.147.217.103:1080 | US | 527 | 19 | 19/19 |
| http://144.124.251.24:10801 | NL | 1135 | 18 | 24/44 |
| socks5://185.87.255.54:1080 | GB | 1511 | 17 | 17/17 |
| http://190.0.246.211:4040 | CO | 1085 | 16 | 83/96 |
| http://167.172.76.176:9090 | SG | 977 | 16 | 38/57 |
| http://144.124.251.24:10261 | NL | 771 | 15 | 23/28 |
| http://154.59.56.76:999 | VE | 4464 | 14 | 45/56 |
| http://144.124.251.24:10084 | NL | 5991 | 13 | 23/28 |
| http://144.124.251.24:10088 | NL | 846 | 13 | 22/28 |
| http://144.124.251.24:10412 | NL | 738 | 13 | 23/28 |
| http://144.124.251.24:10471 | NL | 781 | 13 | 27/43 |
| http://144.124.251.24:10566 | NL | 746 | 13 | 24/29 |
| http://144.124.251.24:10605 | NL | 973 | 13 | 23/28 |
| http://144.124.251.24:10610 | NL | 1185 | 13 | 23/28 |
| http://144.124.251.24:10631 | NL | 775 | 13 | 23/28 |
| http://144.124.251.24:10658 | NL | 749 | 13 | 23/28 |
| http://144.124.251.24:10689 | NL | 706 | 13 | 24/32 |
| http://144.124.251.24:10800 | NL | 745 | 13 | 23/28 |
| http://144.124.251.24:10811 | NL | 797 | 13 | 23/28 |
| http://144.124.251.24:10818 | NL | 719 | 13 | 20/28 |
| http://144.124.251.24:11450 | NL | 741 | 13 | 21/28 |
| http://34.43.46.91:80 | US | 508 | 13 | 92/96 |
| http://190.0.246.210:4040 | CO | 732 | 12 | 84/95 |
| http://103.237.102.191:11111 | DE | 847 | 12 | 90/96 |
| http://154.59.56.73:999 | VE | 6358 | 12 | 55/68 |
| http://190.97.236.130:999 | VE | 830 | 12 | 22/25 |
| http://200.229.65.172:3128 | BR | 1988 | 11 | 11/11 |
| http://18.157.123.132:3128 | DE | 733 | 11 | 43/57 |
| http://3.216.199.128:3128 | US | 322 | 11 | 11/11 |
| socks5://109.205.182.143:1088 | FR | 2102 | 11 | 11/11 |
| socks5://107.167.18.122:443 | US | 99 | 11 | 46/48 |
| socks5://144.91.121.61:1088 | FR | 2498 | 10 | 82/96 |
| http://34.43.46.91:443 | US | 460 | 9 | 90/96 |
| http://123.121.132.32:8888 | CN | 6233 | 8 | 26/57 |
| http://134.199.191.115:3128 | DE | 6712 | 8 | 8/8 |
| http://189.51.168.165:999 | MX | 512 | 8 | 8/8 |
| http://144.124.251.24:10000 | NL | 921 | 8 | 27/42 |
| http://144.124.251.24:10187 | NL | 779 | 8 | 23/42 |
| http://144.124.251.24:10230 | NL | 725 | 8 | 26/43 |
| http://144.124.251.24:10829 | NL | 919 | 8 | 22/28 |
| http://144.124.251.24:11108 | NL | 711 | 8 | 24/43 |
| http://144.124.251.24:11124 | NL | 769 | 8 | 25/45 |
| http://144.124.251.24:11180 | NL | 725 | 8 | 22/27 |
| socks5://23.239.30.204:1088 | US | 5207 | 8 | 8/8 |
| http://101.251.204.174:8080 | CN | 1830 | 7 | 44/82 |
| http://149.130.173.58:9443 | CO | 549 | 7 | 7/7 |
| http://43.173.120.13:8899 | US | 317 | 7 | 7/7 |
| http://161.22.39.58:999 | VE | 786 | 7 | 7/7 |
| http://201.71.2.25:999 | VE | 3755 | 7 | 35/83 |
| socks5://45.61.129.165:9050 | US | 4340 | 7 | 77/96 |
| http://144.124.251.24:10485 | NL | 842 | 6 | 20/28 |
| http://128.199.121.61:9090 | SG | 978 | 6 | 14/16 |
| http://3.212.18.54:3128 | ?? | 316 | 6 | 6/6 |
| socks5://43.167.166.56:1080 | JP | 1731 | 6 | 7/8 |
| socks5://171.25.158.95:1080 | SE | 1375 | 6 | 7/11 |
| http://168.194.34.196:9001 | AR | 2467 | 5 | 29/94 |
| http://36.137.204.11:8002 | CN | 2823 | 5 | 8/12 |
| http://47.121.139.13:3128 | CN | 3183 | 5 | 47/95 |
| http://190.12.150.244:999 | EC | 7421 | 5 | 63/92 |
| http://154.59.56.78:999 | VE | 2725 | 5 | 33/52 |
| http://200.59.191.27:999 | VE | 5500 | 5 | 60/91 |
| socks5://160.187.0.89:1080 | VN | 1385 | 5 | 6/9 |
| http://185.195.71.218:18080 | CH | 4237 | 4 | 24/33 |
| http://47.97.114.99:13357 | CN | 4172 | 4 | 8/25 |
| http://114.252.12.37:8888 | CN | 7328 | 4 | 7/48 |
| http://120.232.115.170:17981 | CN | 3522 | 4 | 70/95 |
| http://200.10.31.45:8081 | CO | 1844 | 4 | 41/93 |
| http://31.31.74.185:9898 | CZ | 873 | 4 | 15/17 |
| http://103.119.19.218:3128 | CZ | 817 | 4 | 8/9 |
