# Proxy status

Generated 2026-11-09T23:14:25Z by `harvest.py`.

- **1622** endpoints opened a TLS tunnel to `raw.githubusercontent.com` this run
- **5694** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **36021** endpoints on record
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
| http | 3576 |
| socks5 | 2101 |
| socks4 | 17 |

| country | entries |
|---|---|
| NL | 1881 |
| ID | 1051 |
| ?? | 603 |
| PH | 165 |
| CO | 151 |
| US | 136 |
| TH | 114 |
| MX | 113 |
| BR | 92 |
| TR | 90 |
| VE | 85 |
| IN | 84 |
| BD | 78 |
| CN | 71 |
| RU | 64 |
| DO | 63 |
| EC | 56 |
| AR | 55 |
| PK | 47 |
| VN | 42 |
| ZA | 39 |
| DE | 37 |
| EG | 34 |
| JP | 33 |
| PE | 33 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 7 | 7 | 2 | 2026-11-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-11-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 78 | 78 | 12 | 2026-11-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 92 | 92 | 38 | 2026-11-09 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 82 | 2026-11-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 120 | 120 | 20 | 2026-11-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 150 | 150 | 34 | 2026-11-09 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 64 | 2026-11-09 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 158 | 158 | 23 | 2026-11-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-11-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 104 | 2026-11-09 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-11-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 402 | 402 | 284 | 2026-11-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 161 | 2026-11-09 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-11-09 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 544 | 544 | 90 | 2026-11-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 527 | 2026-11-09 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 445 | 2026-11-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1127 | 2026-11-09 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1662 | 1662 | 0 | 2026-11-09 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1580 | 2026-11-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2232 | 2232 | 691 | 2026-11-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2330 | 2330 | 1380 | 2026-11-09 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 2785 | 2785 | 673 | 2026-11-09 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 5163 | 5163 | 3936 | 2026-11-09 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 10817 | 10817 | 1984 | 2026-11-09 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://103.133.26.73:3128 | ID | 1270 | 57 | 77/159 |
| http://176.111.37.5:39811 | HK | 1940 | 52 | 162/181 |
| http://34.43.46.91:80 | US | 1143 | 51 | 175/181 |
| http://4.144.146.21:80 | SG | 892 | 49 | 66/73 |
| http://176.111.37.216:39811 | HK | 3152 | 44 | 153/181 |
| http://34.43.46.91:443 | US | 534 | 30 | 170/181 |
| http://130.110.103.245:3128 | SA | 1716 | 27 | 163/181 |
| http://103.133.26.72:8080 | ID | 1223 | 24 | 61/107 |
| http://45.189.57.114:3129 | EC | 854 | 23 | 23/23 |
| http://190.123.83.137:999 | AR | 3671 | 18 | 18/18 |
| http://190.0.246.213:4040 | CO | 2292 | 18 | 136/146 |
| http://103.133.26.119:8080 | ID | 1639 | 17 | 60/91 |
| http://189.51.168.164:999 | MX | 3361 | 17 | 17/17 |
| http://49.229.100.235:8080 | TH | 1266 | 17 | 89/129 |
| http://171.100.254.137:8080 | TH | 1587 | 17 | 17/17 |
| http://43.161.254.16:3128 | HK | 1082 | 16 | 18/21 |
| http://103.130.61.61:8081 | ID | 2243 | 16 | 150/181 |
| http://184.75.221.82:3118 | CA | 1866 | 15 | 128/146 |
| http://103.133.26.50:8080 | ID | 1277 | 15 | 55/82 |
| http://102.244.78.61:8089 | CM | 1417 | 12 | 56/69 |
| http://45.186.6.104:3128 | EC | 841 | 11 | 150/159 |
| http://38.180.18.103:3128 | BE | 1420 | 10 | 10/10 |
| http://45.65.224.74:999 | AR | 1794 | 9 | 38/46 |
| http://190.71.72.85:2525 | CO | 804 | 9 | 25/66 |
| http://103.130.61.60:8081 | ID | 2745 | 9 | 27/37 |
| http://128.199.113.85:9090 | SG | 2042 | 9 | 11/12 |
| http://102.244.78.61:8090 | CM | 1455 | 8 | 57/73 |
| http://45.198.20.224:8080 | ID | 3512 | 7 | 23/99 |
| http://167.172.76.176:9090 | SG | 898 | 7 | 102/142 |
| socks5://121.46.226.221:10808 | ?? | 4803 | 7 | 7/7 |
| http://131.221.40.131:4040 | CO | 2533 | 6 | 18/20 |
| http://103.97.141.142:8080 | ID | 7319 | 6 | 11/17 |
| http://154.59.56.76:999 | VE | 2734 | 6 | 102/141 |
| http://118.69.182.184:8082 | VN | 5977 | 6 | 8/9 |
| http://114.130.153.122:58080 | BD | 4202 | 5 | 9/10 |
| http://15.229.149.81:1080 | BR | 2786 | 5 | 43/83 |
| http://123.121.140.72:8888 | CN | 7301 | 5 | 19/33 |
| http://177.234.217.44:999 | EC | 3700 | 5 | 28/81 |
| http://84.36.141.180:1981 | EG | 6091 | 5 | 32/132 |
| http://103.109.173.170:80 | ID | 5568 | 5 | 21/67 |
| http://103.122.64.156:8080 | ID | 4508 | 5 | 27/123 |
| http://103.231.236.133:8182 | ID | 3120 | 5 | 28/127 |
| http://49.149.24.144:8082 | PH | 3762 | 5 | 12/20 |
| http://104.248.151.93:9090 | SG | 898 | 5 | 60/82 |
| http://1.10.248.236:80 | TH | 1619 | 5 | 11/20 |
| http://1.20.178.212:80 | TH | 5813 | 5 | 20/45 |
| http://69.87.216.54:7989 | US | 45 | 5 | 65/126 |
| http://172.239.170.24:3128 | US | 1261 | 5 | 10/15 |
| http://90.156.160.234:3128 | UZ | 2834 | 5 | 28/69 |
| http://161.22.39.99:999 | VE | 7251 | 5 | 15/42 |
| http://190.115.15.100:8080 | ?? | 1992 | 5 | 5/5 |
| socks5://45.194.33.12:30002 | HK | 3314 | 5 | 11/25 |
| socks5://193.25.215.182:22222 | US | 730 | 5 | 153/181 |
| http://45.65.224.125:999 | AR | 4378 | 4 | 31/43 |
| http://103.145.45.237:8090 | BD | 4747 | 4 | 19/79 |
| http://56.112.93.245:32650 | CA | 4500 | 4 | 23/80 |
| http://102.244.78.61:8083 | CM | 1415 | 4 | 55/69 |
| http://102.244.78.61:8084 | CM | 1394 | 4 | 55/69 |
| http://102.244.78.61:8088 | CM | 1476 | 4 | 54/69 |
| http://123.121.108.22:8888 | CN | 1490 | 4 | 22/32 |
| http://123.121.132.234:8888 | CN | 1435 | 4 | 28/42 |
| http://103.237.102.191:11111 | DE | 1035 | 4 | 172/181 |
| http://181.188.203.112:999 | EC | 7161 | 4 | 62/173 |
| http://43.155.62.157:443 | HK | 816 | 4 | 71/84 |
| http://38.188.63.115:8081 | ID | 6804 | 4 | 22/105 |
| http://103.151.23.89:8082 | ID | 2534 | 4 | 28/79 |
| http://103.173.162.61:8080 | ID | 7686 | 4 | 18/78 |
| http://157.66.16.33:8787 | ID | 1937 | 4 | 8/12 |
| http://157.66.67.16:8080 | ID | 7140 | 4 | 18/101 |
| http://160.25.155.85:8080 | ID | 7950 | 4 | 10/27 |
| http://160.19.41.37:80 | IN | 6198 | 4 | 23/57 |
| http://188.72.42.241:47193 | IQ | 6049 | 4 | 13/32 |
| http://38.56.251.27:999 | MX | 7467 | 4 | 10/12 |
| http://38.194.246.34:999 | MX | 4390 | 4 | 101/172 |
| http://82.152.138.127:999 | MX | 4056 | 4 | 56/143 |
| http://189.51.168.165:999 | MX | 1524 | 4 | 86/93 |
| http://144.124.251.24:10216 | NL | 1073 | 4 | 77/130 |
| http://144.124.251.24:10574 | NL | 880 | 4 | 74/130 |
| http://144.124.251.24:10658 | NL | 906 | 4 | 67/113 |
| http://144.124.251.24:10811 | NL | 838 | 4 | 68/113 |
| http://200.121.48.195:999 | PE | 7874 | 4 | 26/113 |
| http://180.191.122.34:8082 | PH | 5432 | 4 | 7/10 |
| http://202.125.155.121:8080 | PK | 7636 | 4 | 7/15 |
| http://182.52.113.85:443 | TH | 7749 | 4 | 14/43 |
| http://176.88.166.201:8080 | TR | 5991 | 4 | 22/101 |
| http://165.154.162.73:8888 | US | 1865 | 4 | 123/181 |
| http://173.205.202.33:8181 | US | 7783 | 4 | 29/64 |
| http://38.172.160.16:999 | VE | 7857 | 4 | 82/132 |
| http://41.196.16.226:1976 | ?? | 2235 | 4 | 4/4 |
| http://123.121.121.123:8888 | ?? | 1549 | 4 | 4/4 |
| http://203.28.53.55:8090 | ?? | 3513 | 4 | 4/4 |
| http://204.199.106.226:999 | ?? | 932 | 4 | 4/4 |
| socks5://5.255.113.177:1080 | NL | 5058 | 4 | 30/79 |
| socks5://213.176.74.119:1080 | NL | 5113 | 4 | 15/60 |
| http://181.209.125.237:999 | AR | 2430 | 3 | 9/38 |
| http://3.26.199.107:1234 | AU | 2539 | 3 | 25/94 |
| http://103.204.211.103:443 | BD | 7824 | 3 | 12/27 |
| http://182.252.89.134:8080 | BD | 6553 | 3 | 14/40 |
| http://15.223.187.219:55865 | CA | 4530 | 3 | 35/95 |
| http://102.244.78.61:8080 | CM | 1406 | 3 | 58/70 |
