import os
import requests
import argparse
import socket

def main():
    if os.name == 'nt':
        os.system('clear')  # Gunakan perintah 'clear' jika menjalankan di Kali Linux
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
            print(f"\u001b[31mIP address of {url}: {ip}\u001b[0m")  # Warna huruf merah
        except socket.gaierror:
            print(f"\u001b[31mUnable to resolve IP address for {url}\u001b[0m")  # Warna huruf merah

if __name__ == "__main__":
    main()
