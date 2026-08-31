
# Function to perform the exception handling
def check_int():
    # Loop continuously until a valid integer is provided
    while True:
        try:
            # Attempt to convert user input to an integer
            number=int(input("Enter an Integer :"))
        except ValueError:
            # Handle cases where input is not a whole number
            print("This is not a Interger")
        else:
            # Confirm successful conversion and exit the loop
            print(f"The Interger number is :{number}") 
            return
        finally:
            # Code here runs every time, whether an error happened or not
            pass          

# Calling the check_int() function 
check_int()
