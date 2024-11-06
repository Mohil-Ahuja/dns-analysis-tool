# DNS Toolkit

A powerful tool for analyzing, editing, and simulating DNS packets. This toolkit allows you to perform various operations on DNS traffic, such as sniffing packets, analyzing DNS requests, modifying responses, visualizing DNS traffic, and even simulating DNS flood attacks.

## Features

1. **Sniff DNS Packets**: Capture DNS packets from the network to monitor DNS queries.
2. **Analyze DNS Packets**: Analyze captured DNS packets and get insights like the most queried domains.
3. **Edit and Replay DNS Packets**: Modify DNS response packets and replay them for testing.
4. **Visualize DNS Traffic**: Visualize DNS traffic patterns, such as the frequency of DNS queries to different domains.
5. **Simulate DNS Flood**: Simulate a DNS flood attack by sending numerous DNS requests to a target server.
6. **Extensible**: The toolkit is modular and can be extended with new DNS-related features.

## Requirements

- **Python 3.x**  
- **Scapy** library for packet manipulation and sniffing  
- **Matplotlib** for traffic visualization  
- **Tkinter** (Optional) for a GUI (if applicable)

Install the required dependencies using:

```bash
pip install scapy matplotlib

## Usage

1. **Sniff DNS Packets**:  
   Start the packet sniffer by specifying the network interface to monitor (e.g., `eth0`, `wlan0`).
   ```python
   Select an option: 1
   Enter interface to sniff (e.g., eth0): wlan0
   ```

2. **Analyze DNS Packets**:  
   Load a `.cap` file (packet capture file) to analyze DNS traffic.
   ```python
   Select an option: 2
   Enter path to .cap file: /path/to/file.cap
   ```

3. **Edit and Replay DNS Packets**:  
   Modify DNS response packets by changing IP addresses and replay the modified packets.
   ```python
   Select an option: 3
   Enter path to .cap file: /path/to/file.cap
   Enter new IP address for DNS response: 8.8.8.8
   ```

4. **Visualize DNS Traffic**:  
   Visualize the DNS traffic from a `.cap` file using Matplotlib.
   ```python
   Select an option: 4
   Enter path to .cap file: /path/to/file.cap
   ```

5. **Simulate DNS Flood**:  
   Simulate a DNS flood attack to target a DNS server with a specified number of DNS queries.
   ```python
   Select an option: 5
   Enter target DNS server IP: 8.8.8.8
   Enter domain to query: example.com
   ```

## Example Usage

Here is an example of sniffing DNS packets on the `wlan0` interface:

```bash
python main.py
```
- Choose option `1` to sniff DNS packets.
- Enter `wlan0` as the interface.

You will start receiving DNS queries from your network, such as:
```bash
Query: time.cloudflare.com.
Query: assets.msn.com.
Query: dns.google.
```

## How It Works

- **Packet Sniffing**: The tool captures DNS query packets on the specified interface using Scapy.
- **Packet Analysis**: The tool analyzes `.cap` files containing DNS traffic, counting the frequency of queried domains.
- **Packet Editing**: The tool allows modifying DNS responses by editing the IP address in the DNS response packet and then replaying the modified packets.
- **Flood Simulation**: The tool sends a large number of DNS queries to simulate a DNS flood attack to a specified DNS server.

## Contributing

If you'd like to contribute to the project, feel free to open issues or pull requests. Any improvements, bug fixes, or new features are welcome!

### How to Contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m "Your commit message"`).
5. Push your changes to your fork (`git push origin feature/your-feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
