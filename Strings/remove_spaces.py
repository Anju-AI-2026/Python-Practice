# Program to remove spaces from a string

text = input("Enter a string: ")

new_text = ""

# Create a new string without spaces
for character in text:
    if character != " ":
        new_text += character

print("\nString without spaces:")
print(new_text)
