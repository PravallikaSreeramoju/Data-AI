import shutil

total, used, free =shutil.disk_usage("C:/")

print(f"Total disk: {total//(1024**3)} GB")
print(f"Used disk: {used//(1024**3)} GB")
print(f"Free disk: {free//(1024**3)} GB")

