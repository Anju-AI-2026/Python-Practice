# Program to manage a restaurant menu using a list

menu = []

while True:
    print("\n===== RESTAURANT MENU MANAGER =====")
    print("1. Add Food Item")
    print("2. Display Menu")
    print("3. Search Food Item")
    print("4. Remove Food Item")
    print("5. Count Menu Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        food_item = input("Enter food item: ")
        menu.append(food_item)
        print("Food item added successfully.")

    elif choice == 2:
        if len(menu) == 0:
            print("Menu is empty.")
        else:
            print("\nRestaurant Menu:")

            # Display all food items in the menu
            for index, food_item in enumerate(menu, start=1):
                print(f"{index}. {food_item}")

    elif choice == 3:
        food_item = input("Enter food item to search: ")

        if food_item in menu:
            print("Food item is available in the menu.")
        else:
            print("Food item not found.")

    elif choice == 4:
        food_item = input("Enter food item to remove: ")

        if food_item in menu:
            menu.remove(food_item)
            print("Food item removed successfully.")
        else:
            print("Food item not found.")

    elif choice == 5:
        print(f"Total menu items: {len(menu)}")

    elif choice == 6:
        print("Thank you for using the Restaurant Menu Manager.")
        break

    else:
        print("Invalid choice. Please try again.")
