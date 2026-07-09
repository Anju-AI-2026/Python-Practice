# Program: Password Character Checker

password = input("Enter your password: ")

has_upper = False
has_lower = False

for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

print("\n===== PASSWORD REPORT =====")

print(f"Password Length : {len(password)}")

print(f"Contains Uppercase : {has_upper}")
print(f"Contains Lowercase : {has_lower}")
