# Program to identify vowels in a string and count them

text = input("Enter a string: ")

vowel_count = 0

#Counting th vowel in the word
for character in text:
    if character in "aeiouAEIOU":
        print(character, "is a vowel")
        vowel_count += 1
    else:
        print(character, "is not a vowel")

# Display the total number of vowels in the string
print("Total number of vowels:", vowel_count)
