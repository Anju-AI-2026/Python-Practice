# Program to simulate ATM PIN verification

correct_pin = "1234"
balance = 5000

pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:
    print("\nLogin Successful!")

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Available Balance: ₹{balance}")

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Updated Balance: ₹{balance}")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print(f"Please collect your cash.")
            print(f"Remaining Balance: ₹{balance}")
        else:
            print("Insufficient Balance.")

    else:
        print("Invalid Choice.")

else:
    print("Incorrect PIN.")
