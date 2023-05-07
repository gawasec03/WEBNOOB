# WEBNOOB
Made by ChatGPT designed to perform scanning of websites for the detection of Web Application Firewalls (WAFs) and Content Management Systems (CMSs). It utilizes the wafw00f and wappalyzer libraries to conduct the scans.

# How to Usage :

1. Install the required dependencies by running the following command:

a. pip install wafw00f wappalyzer requests
b. Once the dependencies are installed, you can run the script with the appropriate command-line arguments. Here are a few examples:

1) To scan a single domain: "python3 webnoob.py <example.com>"
2) To scan a domain with a list of subdomains: "python3 webnoob.py <example.com> -s subdomains.txt
3) Note: Replace subdomains.txt with the actual file containing your list of subdomains.

2. The script will start scanning the specified domain and subdomains. It will print any detected WAFs or CMSs for each URL.
