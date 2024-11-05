# packet_editor.py
from scapy.all import rdpcap, wrpcap, DNSRR

def modify_dns_response(filename="dns.cap", new_ip="1.2.3.4"):
    print(f"Modifying DNS responses in {filename}...")
    packets = rdpcap(filename)
    for pkt in packets:
        if pkt.haslayer(DNSRR):  # DNS response
            pkt[DNSRR].rdata = new_ip
    wrpcap("modified_dns.cap", packets)
    print("Modified packets saved to modified_dns.cap.")

def replay_packets(filename="modified_dns.cap"):
    print(f"Replaying packets from {filename}...")
    packets = rdpcap(filename)
    sendp(packets)
