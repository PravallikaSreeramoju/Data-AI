import super_calculator as sc

print("\n----- SUPER CALCULATOR -----")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Floor Division")
print("6. Modulus")
print("7. Power")
print("8. Absolute")
print("9. Square Root")
print("0. Exit")

choice = int(input("Enter your choice: "))

if choice == 0:
    print("Calculator Closed 👋")

elif choice in [1, 2, 3, 4, 5, 6, 7]:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == 1:
        print("Result:", sc.add(a, b))
    elif choice == 2:
        print("Result:", sc.subtract(a, b))
    elif choice == 3:
        print("Result:", sc.multiply(a, b))
    elif choice == 4:
        print("Result:", sc.divide(a, b))
    elif choice == 5:
        print("Result:", sc.floor_divide(a, b))
    elif choice == 6:
        print("Result:", sc.modulus(a, b))
    elif choice == 7:
        print("Result:", sc.power(a, b))

elif choice in [8, 9, 10]:
    a = float(input("Enter number: "))
    if choice == 8:
        print("Result:", sc.absolute(a))
    elif choice == 9:
        print("Result:", sc.square_root(a))

else:
    print("Invalid choice")
