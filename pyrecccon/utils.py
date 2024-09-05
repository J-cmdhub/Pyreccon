def print_report(subdomains, whois_data, geolocation, nmap_data):
    print("\n=== Scan Report ===")
    
    print("\nSubdomains:")
    for sub in subdomains:
        print(f"- {sub}")

    print("\nWHOIS Data:")
    for key, value in whois_data.items():
        print(f"{key}: {value}")

    print("\nGeolocation Data:")
    for key, value in geolocation.items():
        print(f"{key}: {value}")

    print("\nNmap Scan Data:")
    for protocol in nmap_data.all_protocols():
        ports = nmap_data[protocol].keys()
        print(f"{protocol}: {ports}")

    print("\n=== End of Report ===")
