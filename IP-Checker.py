#One will need to have NMAP, Whois, and NSLOOKUP installed, on the system that is running the below program.
import subprocess

def whois_lookup(ip_address):
    result = subprocess.run(['whois', ip_address], capture_output=True, text=True)
    print(result.stdout)

def nslookup(ip_address):
    result = subprocess.run(['nslookup', ip_address], capture_output=True, text=True)
    print(result.stdout)

def nmap_https_cert(ip_address):
    result = subprocess.run(['nmap', '--script', 'ssl-cert', '-Pn', '443', ip_address], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")

    print("\nWHOIS Lookup:")
    whois_lookup(ip_address)

    print("\nNSlookup:")
    nslookup(ip_address)

    print("\nNmap HTTPS Certificate Information:")
    nmap_https_cert(ip_address)
