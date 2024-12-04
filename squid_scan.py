import requests
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP Address or Hostname")
    parser.add_argument("--creds", dest="creds", help="Proxy username and password (username:password)")
    parser.add_argument("--proxy", dest="proxy", help="Define proxy address (xxx:3128)")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target, use --help for info")
    elif not options.proxy:
        parser.error("[-] Please specify a proxy, use --help for info")
    elif not options.creds:
        parser.error("[-] Please specify creds, use --help for info")
    return options

def set_proxy(creds, proxy):
    proxies = {
        "http": "http://" + creds + "@" + proxy
    }
    return proxies

def scan_proxy(target):
    ports = set(range(1, 65536))
    proxies = set_proxy(options.creds, options.proxy)
    for i in sorted(ports):
        port = str(i)
        r = requests.get("http://" + target + ":" + port, proxies=proxies)
        if r.status_code == 200:
            status = "Connected"
            print("\r[+]Target Port " + port + " - " + status)
        else:
            pass #status = "Blocked or Unavailable"

options = get_arguments()
scan_proxy(options.target)
