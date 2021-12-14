import socket
from IPy import IP
from datetime import datetime
import pyfiglet

def scan(target):
    converted_ip = check_ip(target)
    print("-" * 50)
    print('\n' + '[+] scan target ' + str(target))
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)
    for port in range(1,65535):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddress,port))
        try:
            banner = get_banner(sock)
            print("[+] Open Port " + str(port) + ':' + str(banner.decode().strip('\n')))
        except:
            print("[+] Open Port " + str(port))
    except:
        pass

acsii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(acsii_banner)
targets = input("[+] Enter The Target\s to scan(split mulitple targets with ,): ")
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
