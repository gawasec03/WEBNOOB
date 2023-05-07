# WEBNOOB
Made by ChatGPT The provided code can be described as a scanning tool for detecting Web Application Firewalls (WAFs) and Content Management Systems (CMSs) on a given domain and its subdomains. This tool can be useful for security researchers, developers, and system administrators who want to identify potential security measures and CMS platforms used by websites.

# How to Usage :

1. pip install requests
2. python webnoob.py "example.com" (for single domain)
3. python scan.py "example.com" -s <subdomains-file> (for subdomain)

# Help :

usage : webnoob.py [-h] [-s SUBDOMAINS] domain                                                                    
Detect WAF and CMS from domain and subdomains                                                                                                         
positional arguments :                                                                                                                                
  domain                The domain to scan                                                                                                           
                                                                                                                                                     
options :                                                                                                                                             
  -h, --help            show this help message and exit                                                                                              
  -s SUBDOMAINS, --subdomains SUBDOMAINS                                                                                                             
                        A file containing a list of subdomains
