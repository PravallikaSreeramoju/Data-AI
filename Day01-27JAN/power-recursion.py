def pow(a,b):
    if(b==0):
        return 1
    elif(b==1):
        return a
    return a*pow(a,b-1)

a,b=5,3
print(pow(a,b))