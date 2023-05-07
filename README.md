# WEBNOOB
Made by ChatGPT designed to perform scanning of websites for the detection of Web Application Firewalls (WAFs) and Content Management Systems (CMSs). It utilizes the wafw00f and wappalyzer libraries to conduct the scans.

# How to Usage :

* Install the required dependencies by running the following command :

1. pip install wafw00f wappalyzer requests
2. Once the dependencies are installed, you can run the script with the appropriate command-line arguments. Here are a few examples :

- To scan a single domain : "python3 webnoob.py <example.com>"
- To scan a domain with a list of subdomains : "python3 webnoob.py <example.com> -s subdomains.txt
- Note: Replace subdomains.txt with the actual file containing your list of subdomains.

3. The script will start scanning the specified domain and subdomains. It will print any detected WAFs or CMSs for each URL.
