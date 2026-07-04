# Program to manage student attendance using loops

present_count = 0
absent_count = 0

number_of_students = int(input("Enter the number of students: "))

# Record attendance for each student
for i in range(number_of_students):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ")
    attendance = input("Present or Absent (P/A): ").upper()

    if attendance == "P":
        present_count += 1
        print(f"{name} is Present.")
    elif attendance == "A":
        absent_count += 1
        print(f"{name} is Absent.")
    else:
        print("Invalid attendance status.")

print("\n===== ATTENDANCE REPORT =====")
print(f"Total Students : {number_of_students}")
print(f"Present        : {present_count}")
print(f"Absent         : {absent_count}")
