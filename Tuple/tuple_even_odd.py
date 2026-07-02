# Program to separate even and odd numbers from a tuple

numbers = (12, 5, 8, 17, 20, 9, 14)

even_numbers = ()
odd_numbers = ()

for num in numbers:
    if num % 2 == 0:
        even_numbers += (num,)
    else:
        odd_numbers += (num,)

print("Original Tuple:", numbers)
print("Even Numbers :", even_numbers)
print("Odd Numbers  :", odd_numbers)
