from scapy.all import sniff, IP, TCP, UDP, Raw

def handle_packet(packet):
    print("-" * 50)

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP:      {src_ip}")
        print(f"Destination IP: {dst_ip}")

        if TCP in packet:
            print(f"Protocol:       TCP")
            print(f"Source Port:    {packet[TCP].sport}")
            print(f"Dest Port:      {packet[TCP].dport}")
        elif UDP in packet:
            print(f"Protocol:       UDP")
            print(f"Source Port:    {packet[UDP].sport}")
            print(f"Dest Port:      {packet[UDP].dport}")
        else:
            print(f"Protocol:       Other")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload (raw):  {payload[:50]}")  # first 50 bytes only
    else:
        print("Non-IP packet (e.g. ARP)")

print("Starting sniffer... press Ctrl+C to stop")
sniff(prn=handle_packet, count=20)
