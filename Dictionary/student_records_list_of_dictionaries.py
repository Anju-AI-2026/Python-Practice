# Program to store and display student records using a list of dictionaries

student_records = []

# Continue taking student records until the user chooses to exit
while True:
    choice = int(input("\n1. Add Student\n2. Exit\nEnter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))

        # Create a dictionary for each student
        student = {
            "name": name,
            "marks": marks
        }

        # Add the student record to the list
        student_records.append(student)

    elif choice == 2:
        break

    else:
        print("Invalid choice. Please try again.")

# Display the name and marks of each student
print("\nStudent Records:")

# Iterate through the list and access each student record
for student in student_records:
    print(f"{student['name']} : {student['marks']}")
