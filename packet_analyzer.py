# packet_analyzer.py
from collections import Counter
from scapy.all import rdpcap, DNSQR

def analyze_dns(filename="dns.cap"):
    print(f"Analyzing DNS traffic from {filename}...")
    packets = rdpcap(filename)
    queries = [pkt[DNSQR].qname.decode() for pkt in packets if pkt.haslayer(DNSQR)]
    query_counts = Counter(queries)
    return query_counts
