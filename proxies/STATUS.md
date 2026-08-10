# Proxy status

Generated 2026-08-10T21:10:22Z by `harvest.py`.

- re-emitted from stored measurements; nothing was probed this run
- **263** entries in `all.txt` (a proxy is kept until it fails 3 runs running)
- **7000** endpoints on record
- retirement age: **12 days** with no successful request
- **density: 115/266 (43%)** — of a random sample of the shipped file, how many worked on a second pass

The test is the app's own: handshake, TLS with SNI, `Range: bytes=0-15`, HTTP 206
or 200, non-empty body, all inside eight seconds. A proxy that answers a generic
liveness check but refuses `CONNECT` — the commonest false positive there is —
fails here, which is the point.

Entries are **not** sorted by speed. The app draws 600 at random and shuffles first,
so ranking is discarded; what matters is the share of the file that works, and the
order is chosen to make the daily diff readable instead.

| protocol | entries |
|---|---|
| http | 160 |
| socks5 | 90 |
| socks4 | 13 |

## Sources

A source that has moved returns 404 and yields nothing, which in a log looks
exactly like a quiet day. Anything reading **0 usable** here is worth replacing.

| source | http | lines | usable | new this run | last yielded |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt | 206 | 5 | 5 | 3 | 2026-08-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt | 206 | 21 | 21 | 0 | 2026-08-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt | 206 | 59 | 59 | 31 | 2026-08-10 |
| https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt | 206 | 100 | 100 | 84 | 2026-08-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt | 206 | 117 | 117 | 91 | 2026-08-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt | 206 | 119 | 119 | 33 | 2026-08-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt | 206 | 133 | 133 | 61 | 2026-08-10 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt | 206 | 150 | 150 | 85 | 2026-08-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt | 206 | 168 | 168 | 0 | 2026-08-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt | 206 | 180 | 180 | 22 | 2026-08-10 |
| https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt | 206 | 211 | 211 | 63 | 2026-08-10 |
| https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt | 206 | 212 | 212 | 43 | 2026-08-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt | 206 | 247 | 247 | 103 | 2026-08-10 |
| https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt | 206 | 400 | 400 | 0 | 2026-08-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt | 206 | 405 | 405 | 162 | 2026-08-10 |
| https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt | 206 | 435 | 435 | 258 | 2026-08-10 |
| https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt | 206 | 528 | 528 | 0 | 2026-08-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt | 206 | 554 | 554 | 536 | 2026-08-10 |
| https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt | 206 | 630 | 630 | 449 | 2026-08-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt | 206 | 1603 | 1603 | 1131 | 2026-08-10 |
| https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt | 206 | 1801 | 1801 | 1628 | 2026-08-10 |
| https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt | 206 | 1837 | 1835 | 1 | 2026-08-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt | 206 | 1904 | 1903 | 176 | 2026-08-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt | 206 | 2412 | 2411 | 601 | 2026-08-10 |
| https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt | 206 | 2452 | 2452 | 1899 | 2026-08-10 |
| https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt | 206 | 2632 | 2630 | 2033 | 2026-08-10 |

## Longest-running entries

Consecutive successful runs is the only signal here that predicts tomorrow.

| proxy | country | ms | streak | successes/checks |
|---|---|---|---|---|
| http://1.231.81.166:3128 | ?? | 1801 | 1 | 1/1 |
| http://2.78.60.10:3129 | ?? | 2679 | 1 | 1/1 |
| http://3.121.130.230:48716 | ?? | 3319 | 1 | 1/1 |
| http://3.127.27.51:11726 | ?? | 3645 | 1 | 1/1 |
| http://5.200.72.62:3128 | ?? | 2356 | 1 | 1/1 |
| http://8.138.217.152:21001 | ?? | 2524 | 1 | 1/1 |
| http://8.211.170.91:14680 | ?? | 2848 | 1 | 1/1 |
| http://13.41.196.179:9002 | ?? | 3544 | 1 | 1/1 |
| http://13.48.13.125:11726 | ?? | 4485 | 1 | 1/1 |
| http://13.60.163.108:39409 | ?? | 2857 | 1 | 1/1 |
| http://14.139.235.82:3128 | ?? | 2387 | 1 | 1/1 |
| http://18.141.223.48:3129 | ?? | 1383 | 1 | 1/1 |
| http://18.170.25.193:53656 | ?? | 7240 | 1 | 1/1 |
| http://27.185.218.213:17981 | ?? | 2007 | 1 | 1/1 |
| http://27.254.99.183:8118 | ?? | 2530 | 1 | 1/1 |
| http://34.43.46.91:443 | ?? | 1948 | 1 | 1/1 |
| http://34.43.46.91:80 | ?? | 1333 | 1 | 1/1 |
| http://34.215.116.246:3128 | ?? | 1285 | 1 | 1/1 |
| http://36.92.104.123:8000 | ?? | 4414 | 1 | 1/1 |
| http://37.59.125.131:8888 | ?? | 1196 | 1 | 1/1 |
| http://37.187.109.70:10111 | ?? | 3122 | 1 | 1/1 |
| http://38.51.216.56:999 | ?? | 7571 | 1 | 1/1 |
| http://38.75.82.221:999 | ?? | 5133 | 1 | 1/1 |
| http://38.76.9.0:999 | ?? | 3019 | 1 | 1/1 |
| http://38.194.250.174:999 | ?? | 4298 | 1 | 1/1 |
| http://40.177.99.164:31822 | ?? | 6820 | 1 | 1/1 |
| http://43.99.100.108:3128 | ?? | 1929 | 1 | 1/1 |
| http://43.133.128.153:16012 | ?? | 7155 | 1 | 1/1 |
| http://43.153.82.179:8888 | ?? | 5314 | 1 | 1/1 |
| http://45.65.138.48:999 | ?? | 3873 | 1 | 1/1 |
| http://45.144.53.63:5001 | ?? | 1421 | 1 | 1/1 |
| http://45.153.4.154:3128 | ?? | 1413 | 1 | 1/1 |
| http://45.155.226.177:3128 | ?? | 1398 | 1 | 1/1 |
| http://45.174.108.143:999 | ?? | 4647 | 1 | 1/1 |
| http://45.174.168.3:999 | ?? | 4209 | 1 | 1/1 |
| http://47.76.220.47:33128 | ?? | 1546 | 1 | 1/1 |
| http://47.81.56.193:8888 | ?? | 1713 | 1 | 1/1 |
| http://47.84.84.1:3128 | ?? | 4896 | 1 | 1/1 |
| http://49.144.19.84:8181 | ?? | 7153 | 1 | 1/1 |
| http://51.16.42.227:33527 | ?? | 4854 | 1 | 1/1 |
| http://51.16.42.227:38531 | ?? | 3830 | 1 | 1/1 |
| http://51.44.97.6:2025 | ?? | 3147 | 1 | 1/1 |
| http://56.68.116.64:47651 | ?? | 2755 | 1 | 1/1 |
| http://58.186.168.155:2033 | ?? | 3649 | 1 | 1/1 |
| http://58.186.168.155:2103 | ?? | 6964 | 1 | 1/1 |
| http://63.179.134.206:56179 | ?? | 5410 | 1 | 1/1 |
| http://64.112.184.210:3128 | ?? | 2948 | 1 | 1/1 |
| http://67.220.95.36:8202 | ?? | 1157 | 1 | 1/1 |
| http://74.208.117.247:3128 | ?? | 1409 | 1 | 1/1 |
| http://78.109.34.192:8080 | ?? | 4624 | 1 | 1/1 |
| http://79.137.192.65:30081 | ?? | 2571 | 1 | 1/1 |
| http://82.102.11.164:3460 | ?? | 1165 | 1 | 1/1 |
| http://85.208.200.185:8081 | ?? | 6949 | 1 | 1/1 |
| http://86.53.163.185:10002 | ?? | 4363 | 1 | 1/1 |
| http://87.251.77.29:3128 | ?? | 475 | 1 | 1/1 |
| http://88.210.11.216:8989 | ?? | 3865 | 1 | 1/1 |
| http://89.251.21.4:8080 | ?? | 6652 | 1 | 1/1 |
| http://91.228.133.191:8888 | ?? | 1971 | 1 | 1/1 |
| http://92.51.21.96:8081 | ?? | 5351 | 1 | 1/1 |
| http://95.3.69.222:8080 | ?? | 2211 | 1 | 1/1 |
| http://95.211.64.139:8888 | ?? | 1294 | 1 | 1/1 |
| http://95.211.64.139:8889 | ?? | 728 | 1 | 1/1 |
| http://95.211.174.135:3128 | ?? | 805 | 1 | 1/1 |
| http://98.154.21.253:4228 | ?? | 3306 | 1 | 1/1 |
| http://101.206.186.99:8080 | ?? | 7179 | 1 | 1/1 |
| http://101.255.164.214:8090 | ?? | 7320 | 1 | 1/1 |
| http://102.209.18.248:8080 | ?? | 5668 | 1 | 1/1 |
| http://103.19.78.243:1080 | ?? | 4078 | 1 | 1/1 |
| http://103.77.173.125:9486 | ?? | 1769 | 1 | 1/1 |
| http://103.82.126.243:8080 | ?? | 3093 | 1 | 1/1 |
| http://103.106.79.253:2233 | ?? | 3688 | 1 | 1/1 |
| http://103.130.61.61:8081 | ?? | 1842 | 1 | 1/1 |
| http://103.132.52.20:8080 | ?? | 3801 | 1 | 1/1 |
| http://103.133.24.123:8080 | ?? | 4764 | 1 | 1/1 |
| http://103.135.48.30:8089 | ?? | 4018 | 1 | 1/1 |
| http://103.155.196.46:8080 | ?? | 4037 | 1 | 1/1 |
| http://103.156.75.246:8181 | ?? | 4704 | 1 | 1/1 |
| http://103.161.69.252:2698 | ?? | 4834 | 1 | 1/1 |
| http://103.171.255.242:8086 | ?? | 5630 | 1 | 1/1 |
| http://103.172.42.143:1111 | ?? | 5959 | 1 | 1/1 |
| http://103.172.71.140:8989 | ?? | 5178 | 1 | 1/1 |
| http://103.173.138.236:1111 | ?? | 5993 | 1 | 1/1 |
| http://103.174.123.5:8089 | ?? | 4614 | 1 | 1/1 |
| http://103.178.176.14:8080 | ?? | 7955 | 1 | 1/1 |
| http://103.179.252.153:8181 | ?? | 4571 | 1 | 1/1 |
| http://103.189.249.145:1111 | ?? | 7012 | 1 | 1/1 |
| http://103.237.102.191:11111 | ?? | 1857 | 1 | 1/1 |
| http://103.247.15.103:9090 | ?? | 6800 | 1 | 1/1 |
| http://109.94.1.23:4050 | ?? | 2486 | 1 | 1/1 |
| http://110.76.147.26:1111 | ?? | 4544 | 1 | 1/1 |
| http://111.230.27.213:3128 | ?? | 7617 | 1 | 1/1 |
| http://113.160.132.26:8080 | ?? | 2457 | 1 | 1/1 |
| http://114.236.137.41:21000 | ?? | 3026 | 1 | 1/1 |
| http://115.127.181.114:6969 | ?? | 4524 | 1 | 1/1 |
| http://116.196.150.180:17981 | ?? | 2015 | 1 | 1/1 |
| http://117.236.124.166:3128 | ?? | 4827 | 1 | 1/1 |
| http://119.188.131.55:17981 | ?? | 4536 | 1 | 1/1 |
| http://122.54.132.131:8080 | ?? | 4575 | 1 | 1/1 |
| http://122.246.3.210:17981 | ?? | 4810 | 1 | 1/1 |
| http://124.106.83.244:8083 | ?? | 5021 | 1 | 1/1 |
