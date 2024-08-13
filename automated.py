#!/usr/bin/env python3

import os
import threading

def send_to_host(host_name, ip):
    """Sends traffic to a specific host in the Mininet environment.""" 
    os.system(f"mx {host_name} python3 send.py {ip} 250")

# List of target host names and target IP
target_host_names = ["h2", "h3", "h4"]
target_ip = "10.0.1.1"

# Create and start threads for each host
threads = []
for host_name in target_host_names:
    thread = threading.Thread(target=send_to_host, args=(host_name, target_ip))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All traffic sent successfully!")