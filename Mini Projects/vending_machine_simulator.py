# Mini Project: Vending Machine Simulator

purchase_history = []
grand_total = 0

while True:

    # Display the vending machine menu
    print("\n===== VENDING MACHINE =====")
    print("1. Chips       ₹20")
    print("2. Chocolate   ₹30")
    print("3. Juice       ₹40")
    print("4. Water       ₹15")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Select item and price
    if choice == "1":
        print("\nYou selected Chips")
        print("Price : ₹20")
        item = "Chips"
        price = 20

    elif choice == "2":
        print("\nYou selected Chocolate")
        print("Price : ₹30")
        item = "Chocolate"
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

        print("\n========== PURCHASE SUMMARY ==========")

        if purchase_history:

            for purchase in purchase_history:
                print(f"{purchase['Item']} x{purchase['Quantity']} = ₹{purchase['Total']}")

            print("--------------------------------------")
            print("Grand Total : ₹", grand_total)

        else:
            print("No items purchased.")

        print("\nThank you for using the Vending Machine.")
        break

    else:
        print("Invalid choice. Please try again.")
        continue

    # Ask for quantity
    while True:

        quantity = input("Enter quantity: ")

        if quantity.isdigit():

            quantity = int(quantity)

            if quantity > 0:
                break

            else:
                print("Quantity should be greater than zero.")

        else:
            print("Quantity should contain numbers only.")

    total = price * quantity

    # Display the bill
    print("\n===== BILL =====")
    print("Item :", item)
    print("Price :", price)
    print("Quantity :", quantity)
    print("Total Bill : ₹", total)

    # Accept payment
    while True:

        amount = input("Enter payment amount: ₹")

        if amount.isdigit():

            amount = int(amount)

            if amount >= total:

                change = amount - total

                print("\nPayment Successful!")
                print("Total Bill : ₹", total)
                print("Change : ₹", change)

                grand_total += total

                purchase_history.append({
                    "Item": item,
                    "Quantity": quantity,
                    "Total": total
                })

                break

            else:
                print("Insufficient payment.")
                print(f"Please pay at least ₹{total}.")

        else:
            print("Payment amount should contain numbers only.")

    # Ask whether to continue shopping
    while True:

        again = input("\nDo you want to buy anything else? (Y/N): ").upper()

        if again == "Y":
            break

        elif again == "N":

            print("\n========== PURCHASE SUMMARY ==========")

            for purchase in purchase_history:
                print(f"{purchase['Item']} x{purchase['Quantity']} = ₹{purchase['Total']}")

            print("--------------------------------------")
            print("Grand Total : ₹", grand_total)

            print("\nThank you for using the Vending Machine.")
            exit()

        else:
            print("Please enter Y or N.")
