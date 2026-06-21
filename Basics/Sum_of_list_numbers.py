#PYTHON

# Program to calculate the sum of numbers entered by the user

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total = sum(numbers)

print("The sum of the numbers is:", total)
