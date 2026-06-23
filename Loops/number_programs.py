# Number Programs using Loops

# Program 1: Sum of first N natural numbers
n = int(input("Enter any number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "natural numbers is:", total)


# --------------------------------------------------

# Program 2: Sum of digits
n = int(input("\nEnter any number: "))
digit_sum = 0

while n > 0:
    digit_sum += n % 10
    n //= 10

print("Sum of digits:", digit_sum)


# --------------------------------------------------

# Program 3: Count digits
n = int(input("\nEnter any number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits:", count)
