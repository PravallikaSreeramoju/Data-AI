username=input("Enter username: ")
password=input("Enter password: ")
for i in range(0,3):
    reenter=input("Re-enter password: ")
    if reenter==password:
        print("login successful.")
        break
    elif i==2 and reenter!=password:
        print("Your account is locked.")
    else:
        print("Login failed.")