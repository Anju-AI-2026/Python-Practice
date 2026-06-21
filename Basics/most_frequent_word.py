# Program to find the most frequently occurring word(s)

words = input("Enter some words: ").split()

word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Find the highest frequency
max_frequency = max(word_count.values())

print("Highest frequency:", max_frequency)
print("Most frequent word :")

# Print all words with the highest frequency
for word in word_count:
    if word_count[word] == max_frequency:
        print(word)
