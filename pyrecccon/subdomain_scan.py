import requests

def subdomain_scan(domain):
    subdomains = ["www", "mail", "ftp", "admin", "blog", "shop", "support", "dev", "staging", "test", "api", "static", "m", "webmail", "chat", "vpn", "database", "portal", "docs", "secure"]
    print(f"Starting subdomain scan on {domain}...")
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Discovered subdomain: {url}")
        except requests.ConnectionError:
            continue

