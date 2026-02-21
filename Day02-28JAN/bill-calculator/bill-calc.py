import totalandprof

full_name=input("Enter your full name: ")
phn_num=input("Enter your phone number: ")
masked_phn=phn_num[:2]+"******"+phn_num[-2]
city=input("Enter your city: ")
rest=input("Enter the resturant you've been to: ")
n=int(input("Enter no. of bills: "))
bills=[]
for i in range(0,n):
    bills.append(int(input(f"Enter your bill {i} amount: ")))
total_amount=totalandprof.totalbill(*bills)
mylist=totalandprof.profileGenerator(Full_Name=full_name.strip().title(),Phone_numer=masked_phn,Location=city.strip().title(),Resturant=rest.strip().title(),Total_amount=total_amount)

for i in mylist:
    print(i)