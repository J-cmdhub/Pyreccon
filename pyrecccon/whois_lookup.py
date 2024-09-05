import whois

def whois_lookup(target):
    print(f"\n[INFO] Performing WHOIS lookup for {target}")
    try:
        domain_whois = whois.whois(target)
        return domain_whois
    except Exception as e:
        print(f"[ERROR] WHOIS lookup failed: {e}")
        return {}
