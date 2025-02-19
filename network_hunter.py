import os
import socket
import platform
import requests
import subprocess

# ASCII Banner
def banner():
    print("="*50)
    print(" NETWORK HUNTER - SYSTEM & NETWORK TOOL")
    print("="*50)
    print("Author : lilscorfy")
    print("GitHub : https://github.com/lilscorfy")
    print("Status : ACTIVE")
    print("="*50)

# Get IP Address
def get_ip():
    try:
        return requests.get('https://api64.ipify.org').text
    except:
        return "Unable to fetch"

# Get System Information
def system_info():
    return f"""
OS       : {platform.system()} {platform.release()}
Machine  : {platform.machine()}
Python   : {platform.python_version()}
IP Addr  : {get_ip()}
"""

# Scan Local Network for Active Devices
def scan_network():
    print("\nScanning Network...\n")
    os.system("arp -a")  # Shows active devices

# Scan Open Ports on a Target
def scan_ports():
    target = input("Enter Target IP: ")
    for port in [21, 22, 25, 53, 80, 443, 3306, 8080]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if not sock.connect_ex((target, port)):
            print(f"[+] Port {port} is OPEN")
        sock.close()

# Check if Website is Online
def check_website():
    site = input("Enter Website (example.com): ")
    try:
        response = requests.get(f"http://{site}")
        print(f"[+] {site} is ONLINE - Status Code: {response.status_code}")
    except:
        print(f"[-] {site} is OFFLINE")

# Menu Options
def menu():
    while True:
        banner()
        print("[1] Show System Info")
        print("[2] Scan Active Devices on Network")
        print("[3] Scan Open Ports on Target")
        print("[4] Check if Website is Online")
        print("[5] Exit")

        choice = input("\nSelect an option: ")
        
        if choice == "1":
            print(system_info())
        elif choice == "2":
            scan_network()
        elif choice == "3":
            scan_ports()
        elif choice == "4":
            check_website()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

# Run the menu
if __name__ == "__main__":
    menu()
