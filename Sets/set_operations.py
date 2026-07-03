# Program to perform basic set operations

set1 = set()
set2 = set()

size1 = int(input("Enter the number of elements in Set 1: "))

print("\nEnter elements for Set 1:")
for i in range(size1):
    set1.add(int(input()))

size2 = int(input("\nEnter the number of elements in Set 2: "))

print("\nEnter elements for Set 2:")
for i in range(size2):
    set2.add(int(input()))

print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (Set 1 - Set 2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
