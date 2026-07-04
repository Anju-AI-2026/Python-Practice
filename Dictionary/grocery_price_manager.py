# Program to manage grocery items and their prices using a dictionary

grocery_items = {}

while True:
    print("\n===== GROCERY PRICE MANAGER =====")
    print("1. Add Grocery Item")
    print("2. Display Price List")
    print("3. Search Grocery Item")
    print("4. Update Price")
    print("5. Remove Grocery Item")
    print("6. Count Grocery Items")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter grocery item: ")
        price = float(input("Enter price: ₹"))

        grocery_items[item] = price
        print("Grocery item added successfully.")

    elif choice == 2:
        if len(grocery_items) == 0:
            print("No grocery items available.")
        else:
            print("\n===== PRICE LIST =====")

            # Display all grocery items and their prices
            for item, price in grocery_items.items():
                print(f"{item:<20} ₹{price:.2f}")

    elif choice == 3:
        item = input("Enter grocery item to search: ")

        if item in grocery_items:
            print(f"{item} costs ₹{grocery_items[item]:.2f}")
        else:
            print("Grocery item not found.")

    elif choice == 4:
        item = input("Enter grocery item to update: ")

        if item in grocery_items:
            new_price = float(input("Enter new price: ₹"))
            grocery_items[item] = new_price
            print("Price updated successfully.")
        else:
            print("Grocery item not found.")

    elif choice == 5:
        item = input("Enter grocery item to remove: ")

        if item in grocery_items:
            del grocery_items[item]
            print("Grocery item removed successfully.")
        else:
            print("Grocery item not found.")

    elif choice == 6:
        print(f"Total grocery items: {len(grocery_items)}")

    elif choice == 7:
        print("Thank you for using the Grocery Price Manager.")
        break

    else:
        print("Invalid choice. Please try again.")
