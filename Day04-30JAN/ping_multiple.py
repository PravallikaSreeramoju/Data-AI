import os
hosts=["8.8.8.8","localhost","google.com"]

for host in hosts:
    print(f"Pinging {host}")
    os.system(f"ping -n 2 {host}")