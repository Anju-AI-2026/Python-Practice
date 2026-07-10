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

    while True :
        quantity = input("Enter quantity: ")
        if (quantity.isdigit()):
            quantity = int(quantity)
            total = price * quantity

            print("\n===== BILL =====")
            print("Item :", item)
            print("Price :", price)
            print("Quantity :", quantity)
            print("\nTotal Bill : ₹", total)  

            amount = int(input("Enter payment amount: ₹"))

            if amount >= total:

                change = amount - total

                print("\nPayment Successful!")
                print("Total Bill : ₹", total)
                print("Change : ₹", change)
                return

            else:

                print("\nInsufficient payment.")
                print("Please pay ₹", total)
        else:
            print("Quantity should be numbers only")  
