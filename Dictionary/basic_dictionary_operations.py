# Program to demonstrate basic dictionary operations

student = {
    "name": "Anjali",
    "age": 18,
    "branch": "CSE"
}

# Display the dictionary
print("Dictionary:", student)

# Add a new key-value pair
student["college"] = "ABC College"
print("\nAfter adding a new key-value pair:")
print(student)

# Update an existing value
student["age"] = 19
print("\nAfter updating age:")
print(student)

# Delete a key-value pair
del student["branch"]
print("\nAfter deleting branch:")
print(student)

# Search for a key
search_key = input("\nEnter the key to search: ")

if search_key in student:
    print(f"{search_key}:", student[search_key])
else:
    print("Key not found.")
