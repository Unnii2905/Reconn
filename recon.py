import whois
import dns.resolver
import socket
from ipwhois import IPWhois
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███╗   ██╗███╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗████╗  ██║████╗  ██║
██████╔╝█████╗  ██║     ██║   ██║██████╔╝██╔██╗ ██║██╔██╗ ██║
██╔═══╝ ██╔══╝  ██║     ██║   ██║██╔═══╝ ██║╚██╗██║██║╚██╗██║
██║     ███████╗╚██████╗╚██████╔╝██║     ██║ ╚████║██║ ╚████║
╚═╝     ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═══╝
              Offensive Reconnaissance Toolkit
""")

def whois_lookup(domain):
    print(Fore.YELLOW + "\n[1] WHOIS Lookup:")
    try:
        w = whois.whois(domain)
        print(Fore.GREEN + str(w))
    except Exception as e:
        print(Fore.RED + f"[WHOIS] Error: {e}")

def dns_lookup(domain):
    print(Fore.YELLOW + "\n[2] DNS Records:")

    
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '1.1.1.1']  

    for record_type in ['A', 'MX', 'NS', 'TXT']:
        try:
            answers = resolver.resolve(domain, record_type, lifetime=5)
            print(Fore.CYAN + f"  {record_type}:")
            for r in answers:
                print(Fore.GREEN + f"    {r.to_text()}")
        except Exception as e:
            print(Fore.RED + f"  {record_type}: Error - {e}")
def subdomain_bruteforce(domain, wordlist_path):
    print(Fore.YELLOW + "\n[3] Subdomain Bruteforce:")
    try:
        with open(wordlist_path, 'r') as file:
            words = [line.strip() for line in file]
    except:
        print(Fore.RED + "Wordlist not found.")
        return

    found = []
    for sub in words:
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            print(Fore.GREEN + f"  [+] Found: {subdomain}")
            found.append(subdomain)
        except:
            pass
    if not found:
        print(Fore.RED + "  No subdomains found.")

def ip_geolocation(ip):
    print(Fore.YELLOW + "\n[4] IP Geolocation:")
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        print(Fore.GREEN + f"  Country: {res.get('network', {}).get('country')}")
        print(Fore.GREEN + f"  ASN: {res.get('asn')}")
        print(Fore.GREEN + f"  Org: {res.get('asn_description')}")
    except Exception as e:
        print(Fore.RED + f"[GEO] Error: {e}")

if __name__ == "__main__":
    banner()
    target = input(Fore.CYAN + "Enter target domain: ").strip()

    try:
        ip = socket.gethostbyname(target)
        print(Fore.BLUE + f"\n[+] Resolved IP: {ip}")
    except:
        print(Fore.RED + "[ERROR] Could not resolve domain.")
        exit()

    whois_lookup(target)
    dns_lookup(target)
    subdomain_bruteforce(target, "subdomains.txt")
    ip_geolocation(ip)

