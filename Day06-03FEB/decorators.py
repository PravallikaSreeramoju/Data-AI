# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before calling the function.")
#         result = func(*args, **kwargs)
#         print("After calling the function.")
#         return result
#     return wrapper

# @my_decorator
# def add(a,b):
#     return a + b

# print(add(2,3))

# def employee_decorator(func):
#     def wrapper(name, position="Developer", salary=50000):
#         func(name)
#         print(f"Employee designation: {position}")
#         print(f"salary: {salary}")
#     return wrapper

# @employee_decorator
# def employee_info(name):
#     print(f"Employee name: {name}")
    
# employee_info("Alice Smith")

# def logger_decorator(func):
#     def wrapper(name, email, password):
#         func(name, email, password)
#         if name=="admin" and password=="admin123":
#             print("registered successfully!")
#         else:
#             print("User is not registered.")
#     return wrapper

# @logger_decorator
# def register_user(name, email, password):
#     name=input("Enter your name: ")
#     email=input("Enter your email: ")
#     password=input("Enter your password: ")
   
    
# register_user("","","")


# def registration_required(func):
#     def wrapper(*args, **kwargs):
#         is_registered=False
#         if is_registered:
#             return func(*args, **kwargs)
#         else:
#             print("User is not registered. Please register to access this function.")
#     return wrapper

# @registration_required
# def view_profile():
#     print("Viewing user profile...")
    
# view_profile()

class Person:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
p=Person('anjali')
print(p.name) 

i=1
while i<=5:
    print(i)
    i+=1