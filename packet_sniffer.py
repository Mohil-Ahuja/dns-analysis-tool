
from scapy.all import sniff, DNS, DNSQR

def dns_sniffer(pkt):
    if pkt.haslayer(DNS) and pkt[DNS].qr == 0:  # DNS query
        print(f"Query: {pkt[DNSQR].qname.decode()}")

def start_sniffer(interface="eth0"):
    print(f"Starting DNS packet sniffer on {interface}...")
    sniff(filter="udp port 53", iface=interface, prn=dns_sniffer)
