# Program to demonstrate a simple calculator

# Asking input from the user
number1 = float(input("Enter the first number :"))
number2 = float(input("Enter the second number :"))

# Addition of numbers
sum = (number1 + number2)
print("The sum is :", sum)

# Subtraction of numbers
sub = (number1 - number2)
print("The subtraction is :", sub)

# Multiplication of numbers
multi = (number1 * number2)
print("The Multiplication is :", multi)

# Division of numbers
if (number2 != 0):
  div = (number1 / number2)
  print("The division is :", div)
else:
  print("Error : Can not divide by zero")
