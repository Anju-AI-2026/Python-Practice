# Program to find the factorial of a number

N = int(input("Enter any number to find factorial: "))

i = 1
fact = 1

# Calculate factorial using a while loop
while i <= N:
    fact = fact * i
    i += 1

# Display the result
print("The factorial =", fact)
