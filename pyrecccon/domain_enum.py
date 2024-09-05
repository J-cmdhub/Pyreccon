import subprocess

def enum_subdomains(domain):
    print(f"\n[INFO] Enumerating subdomains for {domain}")
    try:
        result = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)
        subdomains = result.stdout.splitlines()
        return subdomains if subdomains else "No subdomains found."
    except Exception as e:
        print(f"[ERROR] Error during subdomain enumeration: {e}")
        return []
