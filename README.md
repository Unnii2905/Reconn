
RECONN is a simple and beginner-friendly Python-based reconnaissance tool for gathering basic DNS information about a domain. Ideal for cybersecurity students, ethical hackers, or CTF participants.

---

## Features

- DNS Record Lookup (`A`, `MX`, `NS`, `TXT`)
- WHOIS Information
- Reverse IP Lookup
- Basic Geolocation
- IP History Lookup
---


---

##  Installation

1. **Clone the repository:**

cd RECONN

2. Install the dependencies
  pip install -r requirements.txt

## Usage 
python3 recon.py

##The tool uses a file called subdomains.txt which contains a list of common subdomain prefixes (like www, mail, ftp, etc.).
You can edit this file to include any subdomains you'd like to scan for.
Format: One subdomain per line.
Example:
nginx
Copy code
www
mail
dev
ftp
The script appends each entry to the target domain during brute-force subdomain enumeration (e.g., dev.example.com).

##  License

This project is licensed under the [MIT License](LICENSE).
