# Program: Password Strength Checker

while True:
    print("\n===== PASSWORD STRENGTH CHECKER =====")
    print("1. Check Password Strength")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        password = input("Enter your password: ")

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        # Check every character in the password
        for char in password:

            if char.isupper():
                has_upper = True

            elif char.islower():
                has_lower = True

            elif char.isdigit():
                has_digit = True

            else:
                has_special = True

        print("\n===== PASSWORD REPORT =====")

        print(f"Length               : {len(password)}")

        if has_upper:
            print("Uppercase Letter     : Yes")
        else:
            print("Uppercase Letter     : No")

        if has_lower:
            print("Lowercase Letter     : Yes")
        else:
            print("Lowercase Letter     : No")

        if has_digit:
            print("Number               : Yes")
        else:
            print("Number               : No")

        if has_special:
            print("Special Character    : Yes")
        else:
            print("Special Character    : No")

        score = 0

        if len(password) >= 8:
            score += 1

        if has_upper:
            score += 1

        if has_lower:
            score += 1

        if has_digit:
            score += 1

        if has_special:
            score += 1

        print("\n===== RESULT =====")

        if score <= 2:
            print("Password Strength : Weak 🔴")

        elif score == 3 or score == 4:
            print("Password Strength : Medium 🟡")

        else:
            print("Password Strength : Strong 🟢")

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
