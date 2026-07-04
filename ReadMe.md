Task 1: Basic Network Sniffer 
For this task, I built a network packet sniffer in Python using the scapy library. The program captures live network traffic passing through my computer and displays key details for each packet: source IP, destination IP, protocol (TCP/UDP), port numbers, and raw payload data.
To capture packets on Windows, I installed Npcap, a packet-capture driver required alongside scapy since Windows doesn't allow raw packet access by default.
Running the sniffer while browsing the web revealed several real networking concepts in action:

DNS queries and answers — my computer looking up IP addresses for domain names before connecting to them.
The TCP three-way handshake — visible as SYN (S), SYN-ACK (SA), and ACK (A) packets, which is how two devices establish a reliable connection before exchanging data.
UDP traffic — used for faster, connectionless communication like DNS lookups.
Encrypted vs. unencrypted payloads — HTTPS traffic appeared as scrambled, unreadable bytes (because it's encrypted), while one unencrypted connection exposed a fully readable JSON payload in plain text. This was a useful real-world demonstration of why encryption (HTTPS/TLS) matters: any application sending data without it can have that data read by anyone capturing packets on the network.

Tools used: Python, scapy, Npcap
Key takeaway: This task showed firsthand how data moves across a network layer by layer (Ethernet → IP → TCP/UDP → payload), and why unencrypted protocols pose a security risk compared to encrypted ones.
