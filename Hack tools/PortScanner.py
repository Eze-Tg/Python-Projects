import socket
from IPy import IP


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((ipaddress, port))
        print(f'''[+] Port {str(port)} is open''')
    except:
        print(f'''[-] Port {str(port)} is Closed''')

ipaddress = input('[+] Enter Target to scan: ')

for port in range(75,85):
    scan_port(ipaddress, port)