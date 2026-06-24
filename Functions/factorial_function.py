# Program to find the factorial of a number using recursion

def fact(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * fact(n - 1)


n = int(input("Enter a number to find its factorial: "))

print("The factorial of", n, "is:", fact(n))
