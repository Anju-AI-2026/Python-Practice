# Program to check the strength of a password using a function

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif character in special_characters:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    elif len(password) >= 6 and (has_upper or has_lower) and has_digit:
        return "Medium Password"
    else:
        return "Weak Password"


user_password = input("Enter your password: ")

result = check_password_strength(user_password)

print("Password Strength:", result)
