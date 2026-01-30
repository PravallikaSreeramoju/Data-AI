import re

def pass_check(password):
    if len(password) < 7:
        print("Password too short")
    elif not re.search(r'[A-Z]', password):
        print("Need at least one uppercase letter")
    elif not re.search(r'[a-z]', password):
        print("Need at least one lowercase letter")
    elif not re.search(r'\d', password):
        print("Need at least one digit")
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Need at least one special character")
    else:
        print("Strong password")

password = input("Enter the password: ")
pass_check(password)