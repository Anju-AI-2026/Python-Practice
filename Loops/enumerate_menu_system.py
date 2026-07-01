# Program to display a numbered menu using enumerate

menu_items = ["Add Student", "View Students", "Search Student", "Delete Student", "Exit"]

print("===== STUDENT MANAGEMENT MENU =====")

for index, item in enumerate(menu_items, start=1):
    print(f"{index}. {item}")

choice = int(input("\nEnter your choice: "))

if 1 <= choice <= len(menu_items):
    print(f"\nYou selected: {menu_items[choice - 1]}")
else:
    print("\nInvalid choice.")
