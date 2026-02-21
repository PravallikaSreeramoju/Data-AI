def totalbill(*args):
    sum=0
    for num in args:
        sum+=num
    return sum

def profileGenerator(**kwargs):
    mylist=[]
    for key,value in kwargs.items():
        mylist.append(f"{key} : {value}")
    return mylist