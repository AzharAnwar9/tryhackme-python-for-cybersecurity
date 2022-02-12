import sys
import socket
import pyfiglet


ascii_banner = pyfiglet.figlet_format("NETWORK SCANNER")
print(ascii_banner)

try:
    ip = sys.argv[1]
except:
    print("Please provide target IP address")
    print("Syntax : python3 net_scanner.py 10.10.10.10")
    sys.exit(0)

open_ports = list()

ports = range(1, 65535)

def scan_port(ip, port):
    result = 1
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        r = sock.connect_ex((ip, port))

        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

for port in ports:
    sys.stdout.flush()
    response = scan_port(ip, port)

    if response == 0 :
        print(port)
