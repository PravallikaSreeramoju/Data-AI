import psutil #type:ignore

cpu=psutil.cpu_percent(interval=1)
memory=psutil.virtual_memory().percent

print(f"CPU Usage : {cpu} %")
print(f"Memory Usage : {memory} %")
