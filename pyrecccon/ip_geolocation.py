import requests

def get_geolocation(ip):
    print(f"\n[INFO] Performing IP geolocation for {ip}")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        geolocation = response.json()
        return geolocation
    except Exception as e:
        print(f"[ERROR] Failed to get geolocation: {e}")
        return {}
