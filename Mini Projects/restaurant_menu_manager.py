# Mini Project: Restaurant Menu Manager

menu = []

while True:
    print("\n===== RESTAURANT MENU MANAGER =====")
    print("1. Add Food Item")
    print("2. Display Menu")
    print("3. Search Food Item")
    print("4. Remove Food Item")
    print("5. Count Food Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        food = input("Enter food item: ")
        menu.append(food)
        print("Food item added successfully.")

    elif choice == 2:
        if len(menu) == 0:
            print("Menu is empty.")
        else:
            print("\n===== MENU =====")

            # Display all food items
            for index, food in enumerate(menu, start=1):
                print(f"{index}. {food}")

    elif choice == 3:
        food = input("Enter food item to search: ")

        if food in menu:
            print("Food item is available.")
        else:
            print("Food item not found.")

    elif choice == 4:
        food = input("Enter food item to remove: ")

        if food in menu:
            menu.remove(food)
            print("Food item removed successfully.")
        else:
            print("Food item not found.")

    elif choice == 5:
        print(f"Total Food Items: {len(menu)}")

    elif choice == 6:
        print("Thank you for using Restaurant Menu Manager.")
        break

    else:
        print("Invalid choice.")
