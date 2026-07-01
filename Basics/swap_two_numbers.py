# Program to swap two numbers without using a third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swapping logic
a = a + b
b = a - b
a = a - b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
