def profileGenerator(**kwargs):
    mylist=[]
    for key,value in kwargs.items():
        mylist.append(f"{key} : {value}")
    return mylist


full_name=input("Enter your full name: ")
age=int(input("Enter your age: "))
gender=input("Enter your gender: ")
email=input("Enter your email id: ")
phn_num=input("Enter your phone number: ")
city=input("Enter your city: ")


print(profileGenerator(Full_Name=full_name.strip().title(),Age=age,Gender=gender,Email_ID=email.strip().title(),Phone_numer=phn_num,Location=city.strip().title()))