# Program to store and display employee details using tuples

employees = []

number_of_employees = int(input("Enter the number of employees: "))

# Store employee records
for i in range(number_of_employees):
    employee_id = int(input("\nEnter employee ID: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))

    employee = (employee_id, name, salary)
    employees.append(employee)

print("\n===== EMPLOYEE DETAILS =====")

# Display all employee records
for employee in employees:
    print(f"ID: {employee[0]}")
    print(f"Name: {employee[1]}")
    print(f"Salary: ₹{employee[2]:.2f}")
    print("-" * 30)
