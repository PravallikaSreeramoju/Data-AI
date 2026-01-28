def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

a=int(input())
op=str(input())
b=int(input())

if(op== '+'):
    print(add(a,b))
elif(op=='-'):
    print(sub(a,b))
elif(op=='*'):
    print(mul(a,b))
elif(op=='/'):
    print(div(a,b))
elif(op=='%'):
    print(mod(a,b))