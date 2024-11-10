#!/usr/bin/python3

import argparse
import logging
import random
import time
from scapy.all import IP, ICMP, sr1, send
from ipaddress import ip_network
import string

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def random_payload(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size)).encode()

def ping_sweep(network, min_delay, max_delay, timeout, size, timestamp):
    ip_list = ip_network(network, strict=False).hosts()
    print(f"Starting ping sweep on network: {network}")

    for ip in ip_list:
        packet = IP(dst=str(ip), ttl=random.randint(64, 128), id=random.randint(1, 65535))/ICMP(type=13 if timestamp else 8)/random_payload(size)

        response = sr1(packet, timeout=timeout, verbose=0)

        if response:
            print(f"Host {ip} is up")

        time.sleep(random.uniform(min_delay, max_delay)) 

def main():
    parser = argparse.ArgumentParser(description="Ping Sweep")
    parser.add_argument("network", help="Network address with CIDR notation (e.g., 192.168.1.0/24)")
    parser.add_argument("-M", "--max_delay", default=0, help="Maximum delay in seconds (default 0)")
    parser.add_argument("-m", "--min_delay", default=0, help="Minimum delay in seconds (default 0)")
    parser.add_argument("-t", "--timeout", default=0.3, help="Timeout in seconds (default 0.3)")
    parser.add_argument("-s", "--size", default=60, help="Size of the payload (default 60)")
    parser.add_argument("-ts", "--timestamp", action="store_true", help="Use ICMP timestamp type")

    args = parser.parse_args()

    try:
        ping_sweep(
            args.network, 
            float(args.min_delay), 
            float(args.max_delay), 
            float(args.timeout), 
            int(args.size),
            args.timestamp
            )
    except ValueError as e:
        print(f"Invalid network address: {e}")

if __name__ == "__main__":
    main()
