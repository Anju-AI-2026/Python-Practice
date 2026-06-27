# Asking user for the list element and printing 

# Taking a empty list
num=[]

# Asking the user for list element
n=int(input("Enter the limit to the numbers:"))

# Inserting the element in list
for i in range(1,n+1):
    x=int(input(f"Enter the {i} numbers:"))
    num.insert(i,x)

#Printing the list element
print("The sum of number is :", num)
