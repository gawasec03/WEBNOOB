import os
import requests
import wafw00f
import wappalyzer
import argparse

def main():
    if os.name == 'nt':
        os.system('clear')  # Use 'clear' command instead of 'cls' in Kali Linux
    banner = """\u001b[36m
       
░██╗░░░░░░░██╗███████╗██████╗░███╗░░██╗░█████╗░░█████╗░██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝██╔██╗██║██║░░██║██║░░██║██████╦╝
░░████╔═████║░██╔══╝░░██╔══██╗██║╚████║██║░░██║██║░░██║██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░╚███║╚█████╔╝╚█████╔╝██████╦╝
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░
    made by ChatGPT from: gawasec03
    
    """
    print(banner)

# Define command line arguments
parser = argparse.ArgumentParser(description="Detect WAF and CMS from domain and subdomains")
parser.add_argument("domain", help="The domain to scan")
parser.add_argument("-s", "--subdomains", help="A file containing a list of subdomains")
args = parser.parse_args()

# Set up wafw00f scanner
wafw00f_scanner = wafw00f.WafW00F()

# Set up wappalyzer scanner
wappalyzer_scanner = wappalyzer.Wappalyzer()

# Create a list of URLs to scan
urls = [args.domain]
if args.subdomains:
    with open(args.subdomains) as f:
        subdomains = f.read().splitlines()
    urls += [f"{subdomain}.{args.domain}" for subdomain in subdomains]

# Loop through URLs and perform scans
for url in urls:
    # Send a request to the URL to get the headers
    response = requests.head(f"https://{url}")

    # Detect WAF using wafw00f
    wafw00f_result = wafw00f_scanner.identify_waf(response.headers)
    if wafw00f_result:
        print(f"WAF detected on {url}: {wafw00f_result}")

    # Detect CMS using wappalyzer
    try:
        apps = wappalyzer_scanner.analyze_with_versions(response.headers, f"https://{url}")
        cms = [app["name"] for app in apps if "CMS" in app["categories"]]
