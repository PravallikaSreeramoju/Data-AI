
cart = {}
expense_history = []


def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    qty = int(input("Enter quantity: "))

    if name in cart:
        cart[name]['qty'] += qty
    else:
        cart[name] = {'price': price, 'qty': qty}

    print("Item added successfully!\n")


def remove_item():
    name = input("Enter item name to remove: ")
    if name in cart:
        del cart[name]
        print("Item removed.\n")
    else:
        print("Item not found.\n")


def update_quantity():
    name = input("Enter item name: ")
    if name in cart:
        qty = int(input("Enter new quantity: "))
        cart[name]['qty'] = qty
        print("Quantity updated.\n")
    else:
        print("Item not found.\n")


def view_cart():
    if not cart:
        print("Cart is empty.\n")
        return

    print("\n--- Shopping Cart ---")
    total = 0
    for item, details in cart.items():
        item_total = details['price'] * details['qty']
        total += item_total
        print(f"{item} | Price: {details['price']} | Qty: {details['qty']} | Total: {item_total}")

    print("Cart Total:", total, "\n")


def checkout():
    if not cart:
        print("Cart is empty.\n")
        return

    total = sum(details['price'] * details['qty'] for details in cart.values())
    expense_history.append(total)
    cart.clear()

    print(f"Checkout successful! Amount paid: {total}\n")


def view_expenses():
    if not expense_history:
        print("No expenses recorded.\n")
        return

    print("\n--- Expense History ---")
    for i, amount in enumerate(expense_history, start=1):
        print(f"Purchase {i}: {amount}")

    print("Total Money Spent:", sum(expense_history), "\n")
