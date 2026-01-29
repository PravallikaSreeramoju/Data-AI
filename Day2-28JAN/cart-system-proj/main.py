import cart_functions as cart

while True:
    print("===== Shopping Cart Menu =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Quantity")
    print("4. View Cart")
    print("5. Checkout")
    print("6. View Expense History")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        cart.add_item()
    elif choice == '2':
        cart.remove_item()
    elif choice == '3':
        cart.update_quantity()
    elif choice == '4':
        cart.view_cart()
    elif choice == '5':
        cart.checkout()
    elif choice == '6':
        cart.view_expenses()
    elif choice == '7':
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Try again.\n")
