import os
import requests
import argparse
import socket
import whois

def main():
    if os.name == 'nt':
        os.system('clear')  # Gunakan perintah 'clear' jika menjalankan di Kali Linux
    banner = """\u001b[36m

██╗    ██╗███████╗██████╗ ███╗   ██╗ ██████╗  ██████╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝██╔██╗ ██║██║   ██║██║   ██║██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██║╚██╗██║██║   ██║██║   ██║██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝                  
    Made from ChatGPT | by: gawasec03 (2023)

    """
    print(banner)

    # Define command line arguments
    parser = argparse.ArgumentParser(description="Detect WAF, CMS, and WHOIS information from domain and subdomains")
    parser.add_argument("domain", help="The domain to scan")
    parser.add_argument("-s", "--subdomains", help="A file containing a list of subdomains")
    args = parser.parse_args()

    # Create a list of URLs to scan
    urls = [args.domain]
    if args.subdomains:
        with open(args.subdomains) as f:
            subdomains = f.read().splitlines()
        urls += [f"{subdomain}.{args.domain}" for subdomain in subdomains]

    # Print number of subdomains
    num_subdomains = len(urls) - 1
    print(f"Number of subdomains processed: {num_subdomains}")

    # Loop through URLs and perform scans
    for url in urls:
        # Send a request to the URL to get the headers
        response = requests.head(f"https://{url}")

        # Detect WAF
        if "Server" in response.headers and "WAF" in response.headers["Server"]:
            print(f"\u001b[31mWAF detected on {url}: {response.headers['Server']}\u001b[0m")  # Warna huruf merah

        # Detect CMS
        if "X-Powered-By" in response.headers:
            print(f"\u001b[31mCMS detected on {url}: {response.headers['X-Powered-By']}\u001b[0m")  # Warna huruf merah
        elif "Server" in response.headers:
            print(f"\u001b[31mCMS detected on {url}: {response.headers['Server']}\u001b[0m")  # Warna huruf merah
        else:
            print(f"No CMS detected on {url}")

       # Get IP address
        try:
            ip = socket.gethostbyname(url)
            print(f"\u001b[32mIP address of {url}: {ip}\u001b[0m")  # Warna huruf hijau
        except socket.gaierror:
            print(f"\u001b[31mUnable to resolve IP address for {url}\u001b[0m")  # Warna huruf merah
    
        # Get WHOIS information
        try:
            w = whois.whois(url)
            print(f"\u001b[33mWHOIS information for {url}:\n{w}\u001b[0m")  # Warna huruf kuning
        except whois.parser.PywhoisError as e:
            print(f"\u001b[31mUnable to retrieve WHOIS information for {url}: {e}\u001b[0m")  # Warna huruf merah
        except Exception as e:
            print(f"\u001b[31mAn error occurred while retrieving WHOIS information for {url}: {e}\u001b[0m")  # Warna huruf merah      

if __name__ == "__main__":
    main()
