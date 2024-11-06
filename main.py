# main.py
import packet_sniffer
import packet_analyzer
import packet_editor
import dns_visualizer
import dns_attack_simulator

def main():
    while True:
        print("\nDNS Toolkit")
        print("1. Sniff DNS Packets")
        print("2. Analyze DNS Packets")
        print("3. Edit and Replay Packets")
        print("4. Visualize DNS Traffic")
        print("5. Simulate DNS Flood")
        print("6. Exit")

        choice = input("Select an option: ")
        
        if choice == '1':
            interface = input("Enter the network interface to sniff (e.g., 'Wi-Fi' on Windows, 'eth0' on Linux): ")
            packet_sniffer.start_sniffer(interface)
        elif choice == '2':
            filename = input("Enter path to .cap file: ")
            counts = packet_analyzer.analyze_dns(filename)
            print(counts)
        elif choice == '3':
            filename = input("Enter path to .cap file: ")
            new_ip = input("Enter new IP address for DNS response: ")
            packet_editor.modify_dns_response(filename, new_ip)
            replay = input("Replay packets? (y/n): ")
            if replay.lower() == 'y':
                packet_editor.replay_packets("modified_dns.cap")
        elif choice == '4':
            filename = input("Enter path to .cap file: ")
            counts = packet_analyzer.analyze_dns(filename)
            dns_visualizer.plot_top_queries(counts)
        elif choice == '5':
            target = input("Enter target DNS server IP: ")
            domain = input("Enter domain to query: ")
            requests_per_second = 1000  # Fixed to 1000 requests per second
            dns_attack_simulator.dns_flood(target, domain, requests_per_second)
        elif choice == '6':
            print("Exiting the toolkit.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
