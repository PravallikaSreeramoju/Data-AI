bill_amnt=int(input("enter the bill ammount: "))
day=input("enter day: ")
gold_mem=input("are you a gold member: y/n? ")
res=bill_amnt
if day in ["saturday","sunday"] and bill_amnt>1000 and gold_mem=="y":
    res*=0.8
print(f"your final bill ammount: {res}")
