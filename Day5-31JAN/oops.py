# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")
    
        
# name=input("Enter name:")
# age=int(input("Enter age:"))
# s1=Student(name,age)
# s1.display()

# class Animal:
#     def speak(self):
#         print("Some genric sound") 
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
        
# for animal_class in [Dog(),Cat()]:
#     animal_class.speak()
    
# class Pycharm:
#     def execute(self):
#         print("Compiling + Running")
        
# class VSCode:
#     def execute(self):
#         print("Running+Linting")
        
# def code(editor):
#     editor.execute()
    
# code(Pycharm())
# code(VSCode())

# class Grandfather():
#     def wisdom(self):
#         print("grandfather shares wisdom")
        
# class Father(Grandfather):
#     def drive(self):
#         print("Father can drive")
    
# class son(Father):
#     def play(self):
#         print("son can play")
        
# s=son()
# s.wisdom()
# s.drive()
# s.play()

# class Mother():
#     def cook(self):
#         print("Mother can cook")   
        
# class Daughter(Mother):
#     def dance(self):
#         print("Daughter can dance")
        
# class Son(Mother):
#     def sing(self):
#         print("Son can play")
        
# s=Son()
# d=Daughter()
# s.cook()
# d.cook()

# class Father:
#     def drive(self):
#         print("Father can drive")

# class Mother:
#     def cook(self):
#         print("Mother can cook")  
        
# class Child(Father,Mother):
#     def play(self):
#         print("Child can play")
        
# c=Child()
# c.drive()
# c.cook()
# c.play()

# class A:
#     def method_a(self):
#         print("Method A")
        
# class B(A):
#     def method_b(self):
#         print("Method B")
        
# class C(A):
#     def method_c(self):
#         print("Method C")   
        
# class D(B,C):
#     def method_d(self):
#         print("Method D")

# d=D()
# d.method_a()

# from abc import ABC
# from abc import abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def no_of_wheels(self):
#         pass
    
# class car(vehicle):
#     def no_of_wheels(self):
#         print("4 wheels")
# c=car()
# c.no_of_wheels()

class Parent:
    def _int_(self):
        self.public_var="I am public"
        self.protected_var="I am protected"    
        self.private_var="I am private"
        
def access_from_same_class(self):
    print("Inside Parent class")
    print("public",self.public_var)
    print("protected",self.protected_var)
    print("private",self.private_var)
    
class Child(Parent):
    def access_from_child_class(self):
        print("Inside Child class(Subclass)")