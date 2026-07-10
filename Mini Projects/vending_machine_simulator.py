# Mini Project: Vending Machine Simulator

while True:

    print("\n===== VENDING MACHINE =====")
    print("1. Chips       ₹20")
    print("2. Chocolate   ₹30")
    print("3. Juice       ₹40")
    print("4. Water       ₹15")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nYou selected Chips")
        print("Price : ₹20")
        item = "Chips"
        price = 20

    elif choice == "2":
        print("\nYou selected Chocolate")
        print("Price : ₹30")
        item ="Chocolate"
        price = 30

    elif choice == "3":
        print("\nYou selected Juice")
        print("Price : ₹40")
        item = "Juice"
        price = 40

    elif choice == "4":
        print("\nYou selected Water")
        print("Price : ₹15")
        item = "Water"
        price = 15

    elif choice == "5":
        print("Thank you for using the Vending Machine.")
        break

    else:
        print("Invalid choice. Please try again.")

    quantity = int(input("Enter quantity: "))

    total = price * quantity

    print("\n===== BILL =====")
    print("Item :", item)
    print("Price :", price)
    print("Quantity :", quantity)
    print("Total Bill : ₹", total)   
