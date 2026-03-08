#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
username = input("Enter you full name: ")
for i in range(len(username)):
    if i == 0 or username[i-1] == " ":
        print(username[i].lower(), end="")
    else:
        print(username[i].upper(), end= "")
print()