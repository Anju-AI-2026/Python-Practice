# Program to finding common element in 2 list

List1=input("Enter some elements for list 1 :").split()
List2=input("Enter some elements for list 2 :").split()

# A empty list to store common elements
comm_element=[]

# Finding if the lists are empty or not
def find_comm_element():

    if (len(List1) == 0 or len(List2) == 0):
        print("List is empty")
    else:
        # Finding the common elements and storing them in empty list
        for i in range(len(List1)):
            if (List1[i] in List2):
                if (List1[i] not in comm_element):
                    comm_element.append(List1[i])

find_comm_element()
if (len(comm_element) == 0):
    print("There is no common elements")
else:
    print("The common element in both list is :", comm_element)
