# Program to reverse a string using a function

def reverse_string(text):
    return text[::-1]

# Taking input from user
user_string = input("Enter a string: ")

# Calling reverse_string function
reversed_string = reverse_string(user_string)

# Printing the reversed string
print("Reversed string:", reversed_string)
