# Program to find the longest word in a sentence

words = input("Enter a sentence: ").split()

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
