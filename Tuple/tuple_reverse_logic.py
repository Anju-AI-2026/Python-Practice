# Program to reverse a tuple without using slicing

numbers = (10, 20, 30, 40, 50)

reversed_tuple = ()

for i in range(len(numbers)-1, -1, -1):
    reversed_tuple += (numbers[i],)

print("Original Tuple:", numbers)
print("Reversed Tuple:", reversed_tuple)
