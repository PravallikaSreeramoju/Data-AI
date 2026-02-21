errors_log=[]

with open("sample_logs.log","r") as log:
    lines=log.readlines()

    for line in lines:
        if "ERROR" in line:
            words=line.split("]")
            error1=words[2]
            errors_log.append(error1)

with open("ip_error_out.txt","w") as ip:
    for err in errors_log:
        ip.write(err)
    
print("errors extracted successfully.")

