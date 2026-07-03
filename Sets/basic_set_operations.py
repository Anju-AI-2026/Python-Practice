# Program to demonstrate basic set operations

numbers = {10, 20, 30, 40}

print("Original Set:", numbers)

# Add an element
numbers.add(50)
print("\nAfter adding an element:")
print(numbers)

# Remove an element
numbers.remove(20)
print("\nAfter removing an element:")
print(numbers)

# Search for an element
search_number = int(input("\nEnter an element to search: "))

if search_number in numbers:
    print(f"{search_number} is present in the set.")
else:
    print(f"{search_number} is not present in the set.")
