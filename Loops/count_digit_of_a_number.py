# Program : Count digits
n = int(input("\nEnter any number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits:", count)
