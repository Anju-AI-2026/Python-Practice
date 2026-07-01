# Program to find maximum and minimum in a tuple

numbers = (45, 12, 89, 33, 67, 5)

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Tuple:", numbers)
print("Maximum:", max_value)
print("Minimum:", min_value)
