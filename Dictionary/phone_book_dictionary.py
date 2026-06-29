# Program to create a simple phone book using a dictionary

phone_book = {}

number_of_contacts = int(input("Enter the number of contacts: "))

for i in range(number_of_contacts):
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")

    phone_book[name] = phone_number

print("\nPhone Book:")

for name, phone_number in phone_book.items():
    print(f"{name}: {phone_number}")

search_name = input("\nEnter the contact name to search: ")

if search_name in phone_book:
    print(f"{search_name}'s phone number: {phone_book[search_name]}")
else:
    print("Contact not found.")
