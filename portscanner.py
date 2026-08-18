import socket
import sys
from datetime import datetime

# Define the target host (you can change this to any domain/IP you own or test locally)
TARGET_HOST = "127.0.0.1"
# Define default ports to scan
PORTS_TO_SCAN = [21, 22, 80, 443, 8080]

def scan_port(ip, port):
    """
    Attempts to connect to a specific port on the target IP address.
    Returns True if open, False if closed or filtered.
    """
    try:
        # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)  # Timeout after 1 second
        
        # Connect to target IP and port
        result = s.connect_ex((ip, port))
        s.close()
        
        # connect_ex returns 0 if connection was successful
        if result == 0:
            return True
        return False
    except Exception as e:
        return False

def main():
    print("-" * 50)
    print(f"Scanning target: {TARGET_HOST}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)

    try:
        target_ip = socket.gethostbyname(TARGET_HOST)
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()

    open_ports = []
    
    for port in PORTS_TO_SCAN:
        if scan_port(target_ip, port):
            print(f"[+] Port {port}: OPEN")
            open_ports.append(port)
        else:
            print(f"[-] Port {port}: Closed/Filtered")

    print("-" * 50)
    print(f"Scan complete. Open ports: {open_ports}")

if __name__ == "__main__":
    main()
