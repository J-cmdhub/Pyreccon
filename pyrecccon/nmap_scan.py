import nmap
import matplotlib.pyplot as plt

def nmap_scan(target):
    print(f"\n[INFO] Performing Nmap scan for {target}")
    nm = nmap.PortScanner()
    try:
        nm.scan(target, '1-65535')
        return nm[target]
    except Exception as e:
        print(f"[ERROR] Nmap scan failed: {e}")
        return {}

def network_crawl(target):
    print(f"\n[INFO] Crawling the network from {target}")
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=f'{target}/24', arguments='-sn')
        hosts = nm.all_hosts()

        nodes = []
        edges = []
        for host in hosts:
            nodes.append(host)
            for proto in nm[host].all_protocols():
                for port in nm[host][proto].keys():
                    edges.append((host, port))

        draw_network(nodes, edges)
    except Exception as e:
        print(f"[ERROR] Network crawling failed: {e}")

def draw_network(nodes, edges):
    plt.figure(figsize=(8, 6))
    plt.scatter(range(len(nodes)), [1] * len(nodes), s=100)
    for edge in edges:
        plt.plot(edge, [1, 1], 'ro-')
    plt.title("Network Map")
    plt.show()
