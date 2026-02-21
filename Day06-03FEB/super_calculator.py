import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def power(a, b):
    return a ** b

def absolute(a):
    return abs(a)

def maximum(a, b):
    return max(a, b)

def minimum(a, b):
    return min(a, b)

def square_root(a):
    return math.sqrt(a)

