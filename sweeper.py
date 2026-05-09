'''
    Plan:
        1. prompt user to enter subnet
        2. iterate through each IP ADDRESS on subnet and PING IT
           ***USING THREADS*** to ping multiple ips simultaneously 
           - if it RESPONDS, device active
           - if doesnt respond, device is offline
        3. track how long scan took (time library)
        4. display summary of how many active devices found
'''

import time
import ipaddress

#for pinging the ips
import subprocess

#for threading
import concurrent.futures

#moving ping logic into its own function
def ping_host(ip):
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
        return str(ip)
    return None

#prompt user for subnet
subnet = input("Enter subnet: ")

#strict=False makes it so it ignores the host part of ip address, more forgiving for input
network = ipaddress.ip_network(subnet, strict=False)

print(f"Scanning {subnet}...")
print("-" * 40)

#start timer
start_time = time.time()

#instead of just a forloop repeating ping function, executor.map handles it
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    #puts ping_host function return values into a list 
    results = list(executor.map(ping_host, network.hosts()))

    #if the return value isnt None, increment the counter for active hosts
    active_hosts = len([r for r in results if r is not None])
#end timer
end_time = time.time()

#calculate elapsed time
elapsed = round(end_time - start_time, 2)

#display summary to user
print(f"Scan completed in {elapsed} seconds.")
print(f"{active_hosts} hosts found.")
