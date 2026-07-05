# Program to count different types of characters in a string

text = input("Enter a string: ")

letters = 0
digits = 0
spaces = 0
special_characters = 0

# Count different types of characters
for character in text:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1
    elif character.isspace():
        spaces += 1
    else:
        special_characters += 1

print("\n===== CHARACTER COUNT =====")
print("Letters           :", letters)
print("Digits            :", digits)
print("Spaces            :", spaces)
print("Special Characters:", special_characters)
