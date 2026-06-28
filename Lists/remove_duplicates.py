# Python program to remove duplicates from list

# Asking user to enter the elements and inserting them into list1
list1=[]
number = int(input("Enter the limit to the numbers :"))
for i in range(1,number+1):
    x=int(input(f"Enter the {i} element :"))
    list1.insert(i,x)

# Taking a empty list to insert nnon duplicate element
list2=[]

# Checking and removing duplicate value
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])

# Printing the upgraded list        
print("List with no duplicate elements :\n",list2)
