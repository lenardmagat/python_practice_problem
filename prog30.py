#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
username = input("Enter your full name: ")
for i in range(len(username)):
    if username[i] == " ":
        print("_", end="")
    else:
        print(username[i].lower(), end="")
print()