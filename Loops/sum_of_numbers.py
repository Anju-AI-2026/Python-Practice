# Program to find the sum of N numbers entered by the user

numbers = []  # List to store the numbers entered by the user

limit = int(input("Enter the number of elements: "))

# Read numbers from the user and store them in the list
for i in range(limit):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)
total = sum(numbers)

# Display the result
print("The sum of the numbers is:", total)
