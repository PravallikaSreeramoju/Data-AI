class Employee:
  

    def display(self,*args):
        print(f"Name: {name}, Age: {age}, Phone No: {no}")
        print(f"{name} is  {work_type}.")
        print(f"Working hours: {hours} hours per day.")
     
n=int(input("Enter number of employees:"))
for i in range(n):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    no=int(input("Enter phone no:"))
    work_type=input("Enter work type:")
    hours=int(input("Enter working hours:"))
    e=Employee()
    e.display(name,age,no,hours,work_type)
    e.display(name,age,no)