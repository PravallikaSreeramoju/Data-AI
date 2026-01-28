name=str(input("Enter Name: "))
email=str(input("Enter Email: "))
pw=str(input("Enter Password: "))
age=str(input("Enter Age: "))

if "@" not in email:
    print("Invalid Email!")
if len(pw)<6:
    print("Password is too short!")
if type(age) != int:
    print("Age must be a number")
if(any(char.isdigit() for char in name)):
    print("Name must not contain any numbers")
else:
    print("Form submitted successfully!")