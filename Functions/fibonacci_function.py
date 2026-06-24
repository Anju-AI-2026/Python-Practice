def fib(n):
    #Base case
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input("Enter the number of terms in the Fibonacci series: "))

print("Fibonacci series:")

#Printing fibonacci series
for i in range(n):
    print(fib(i), end=" ")

print()  # Move the cursor to the next line
