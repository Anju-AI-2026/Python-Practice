# Program to calculate the electricity bill

units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

print(f"Electricity Bill: ₹{bill}")
