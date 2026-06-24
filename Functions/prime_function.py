# Program to check whether a number is prime using a function

def is_prime(n):

    # Numbers less than 2 are not prime
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
