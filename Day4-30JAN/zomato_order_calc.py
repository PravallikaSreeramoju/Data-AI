print("Welcome to Zomato Order Calculator")
PRICE_PER_ITEM = {
    1 : 500,
    2 : 150,
    3 : 350,
    4 : 100,
    5 : 250
}
items_options={
        "1" : " Biryani",
        "2" : "Noodles",
        "3" : "Chicken starters",
        "4" : "momos",
        "5" : "icecream"
    }
for key,value in items_options.items():
    print(f" {key} : {value}")
try:
    n=int(input("What would you like to order? : "))
    items = int(input("How many items would you like to order? "))
    if items < 0:
        print("Number of items cannot be negative.")
    elif items == 0:
        print("You must order at least one item.")
    else:
        total_cost = items * PRICE_PER_ITEM[n]
        average_cost = total_cost / items
        print("Order Summary")
        print("Items ordered:", items)
        print("Total cost:", total_cost)
        print("Average cost per item:", average_cost)
except ValueError:
    print("Please enter a valid integer value.")
except Exception as e:
    print("Unexpected error occurred:", e)
finally:
    print("Thank you for using Zomato. Have a great day!")

