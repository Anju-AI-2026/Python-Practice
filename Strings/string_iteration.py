# Program to iterate through a string

text = input("Enter a string: ")

print("\nCharacters in the string:")

# Display each character with its index
for index, character in enumerate(text):
    print(f"Index {index}: {character}")
