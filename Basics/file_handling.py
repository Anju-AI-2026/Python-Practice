# 1. Write to a file
with open("note.txt", "w") as file:
    file.write("Hello World")

# 2. Read from a file
with open("note.txt", "r") as file:
    print(file.read())
