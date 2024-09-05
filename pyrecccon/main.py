from domain_enum import enum_subdomains
from whois_lookup import whois_lookup
from ip_geolocation import get_geolocation
from nmap_scan import nmap_scan, network_crawl
from utils import print_report

def main():
    target = input("Enter the target (domain or IP): ")

    if '.' in target:
        print(f"\n[INFO] Target is a domain: {target}")
        subdomains = enum_subdomains(target)
        print(f"Subdomains found: {subdomains}")
    else:
        print(f"\n[INFO] Target is an IP: {target}")

    do_whois = input("\nDo you want to perform WHOIS lookup? (yes/no): ")
    if do_whois.lower() == 'yes':
        whois_data = whois_lookup(target)
        print(f"WHOIS Data: {whois_data}")

    do_geo = input("\nDo you want to perform IP Geolocation? (yes/no): ")
    if do_geo.lower() == 'yes':
        geolocation = get_geolocation(target)
        print(f"Geolocation: {geolocation}")

    do_nmap = input("\nDo you want to perform Nmap scan? (yes/no): ")
    if do_nmap.lower() == 'yes':
        nmap_data = nmap_scan(target)
        print(f"Nmap Scan Results: {nmap_data}")

    do_crawl = input("\nDo you want to perform Network Crawling? (yes/no): ")
    if do_crawl.lower() == 'yes':
        network_crawl(target)

    print_report(subdomains, whois_data, geolocation, nmap_data)

if __name__ == '__main__':
    main()
