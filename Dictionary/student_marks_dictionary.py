# Program to store and manage student marks using a dictionary

student_marks = {}

number_of_students = int(input("Enter the number of students: "))

# Taking student names and marks as input
for i in range(number_of_students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    student_marks[name] = marks

# Display all students and their marks
print("\nStudent Marks:")
for name, marks in student_marks.items():
    print(f"{name}: {marks}")

# Search for a student's marks
search_name = input("\nEnter the student name to search: ")

if search_name in student_marks:
    print(f"{search_name}'s marks: {student_marks[search_name]}")
else:
    print("Student not found.")

# Find the student with the highest marks
highest_student = max(student_marks, key=student_marks.get)

print("\nStudent with the highest marks:")
print(f"{highest_student}: {student_marks[highest_student]}")
