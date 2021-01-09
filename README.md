# Squid Pivoting Port Scanner (Authenticated)

Simple python squid pivot port scanner with authentication (all the others out there don't have auth)
to test for open ports on computers behind squid proxy.

usage: squid_scan.py [-h] [-t TARGET] [--creds CREDS] [--proxy PROXY]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP Address or Hostname
  --creds CREDS         Proxy username and password (username:password)
  --proxy PROXY         Define proxy address (xxx:3128)

  ![alt text](https://github.com/vsamiamv/squid_scan/blob/master/example.jpg?raw=true)
