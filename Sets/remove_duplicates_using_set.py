# Program to remove duplicate elements from a list using a set

numbers = []

size = int(input("Enter the number of elements: "))

for i in range(size):
    number = int(input(f"Enter element {i + 1}: "))
    numbers.append(number)

unique_numbers = set(numbers)

print("\nOriginal List:", numbers)
print("Unique Elements:", unique_numbers)
