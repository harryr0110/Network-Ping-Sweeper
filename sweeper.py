'''
    Plan:
        1. prompt user to enter subnet
        2. iterate through each IP ADDRESS on subnet and PING IT
           - if it RESPONDS, device active
           - if doesnt respond, device is offline
        3. track how long scan took (time library)
        4. display summary of how many active devices found
'''

import time
import ipaddress

#for pinging the ips
import subprocess

#prompt user for subnet
subnet = input("Enter subnet: ")

#strict=False makes it so it ignores the host part of ip address, more forgiving for input
network = ipaddress.ip_network(subnet, strict=False)

print(f"Scanning {subnet}...")
print("-" * 40)

#start timer
start_time = time.time()

active_ips = 0

#ipaddress module auto handles range of ips, no need to get range from user
for ip in network.hosts():
    result = subprocess.run(
        #ping, one ping packet, wait max 1 sec for response, ip address as string
        ["ping", "-c", "1", "-W", "1", str(ip)],
        #supresses ping output so screen isnt cluttered
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    #ping returns 0 if host reposts, anything else means no response
    if result.returncode == 0:
        print(f"{ip} is ACTIVE")
        active_ips += 1

#end timer
end_time = time.time()

#calculate elapsed time
elapsed = round(end_time - start_time, 2)

#display summary to user
print(f"Scan completed in {elapsed} seconds.")
print(f"{active_ips} hosts found.")
