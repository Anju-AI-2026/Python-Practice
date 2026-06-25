# Program to find the biggest of three number

# Asking for the input number
first_num=int(input("Enter the first number :"))
second_num=int(input("Enter the second number :"))
third_num=int(input("Enter the third number :"))

# Finding the largest number
if (first_num >= second_num and first_num >= third_num):
    print("The first number is bigger :" ,first_num)
elif(second_num >= first_num and second_num >= third_num):
    print("The second number is bigger :" ,second_num)
else:
    print("The third number is bigger :" ,third_num)       
