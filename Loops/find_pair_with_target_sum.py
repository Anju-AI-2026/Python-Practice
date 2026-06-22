# Program to find a pair of numbers with the given target sum

numbers = [10, 2, 5, 4, 6, 7]
target = 17

seen = set()

for num in numbers:
    complement = target - num

    # Check if the required complement is already seen
    if complement in seen:
        print("Pair found:", complement, "and", num)
        break

    seen.add(num)
