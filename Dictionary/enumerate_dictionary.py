# Program to display student details using enumerate with dictionary

students = {
    "Anjali": 95,
    "Rahul": 88,
    "Priya": 92,
    "Kiran": 85
}

print("===== STUDENT MARKS LIST =====\n")

for index, (name, marks) in enumerate(students.items(), start=1):
    print(f"{index}. {name} - {marks}")
