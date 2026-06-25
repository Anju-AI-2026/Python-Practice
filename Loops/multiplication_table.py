# Program to print the multiplication table

# Asking the user for a number
number = int(input("Enter any number: "))

# Printing the table
for i in range(1, 11):
    print(number, "X", i, "=", number * i)
