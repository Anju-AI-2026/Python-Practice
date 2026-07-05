# Program to count vowels and consonants in a string

text = input("Enter a string: ")

vowels = 0
consonants = 0

# Count vowels and consonants
for character in text.lower():
    if character.isalpha():
        if character in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("\n===== RESULT =====")
print("Vowels     :", vowels)
print("Consonants :", consonants)
