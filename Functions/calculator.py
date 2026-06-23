 python program using function
# Simple Calculator using Functions
# This program performs basic arithmetic operations using functions.

# Function to add two numbers
def add():
    return a + b


# Function to subtract two numbers
def subtract():
    return a - b


# Function to multiply two numbers
def multiply():
    return a * b


# Function to divide two numbers
def divide():
    return a / b


# Function to find the remainder
def remainder():
    return a % b


# Function to display the calculator menu
def show_menu():
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Show Menu")
    print("7. Exit")


# Get input numbers from the user
print("--- Enter the numbers to perform operations ---")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display the menu initially
show_menu()

# Keep running until the user chooses to exit
while True:

    choice = int(input("\nEnter your choice from the menu: "))

    if choice == 1:
        print("The addition of the numbers is:", add())

    elif choice == 2:
        print("The subtraction of the numbers is:", subtract())

    elif choice == 3:
        print("The multiplication of the numbers is:", multiply())

    elif choice == 4:
        # Check for division by zero
        if b == 0:
            print("Division by zero is not possible.")
        else:
            print("The division of the numbers is:", divide())

    elif choice == 5:
        # Check for division by zero while finding remainder
        if b == 0:
            print("Division by zero is not possible.")
        else:
            print("The remainder of the numbers is:", remainder())

    elif choice == 6:
        show_menu()

    elif choice == 7:
        print("Thank you for using the calculator!")
        break

    else:
        print("Please enter a valid choice.")

