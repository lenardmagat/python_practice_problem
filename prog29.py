#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
username = input("Enter your full name: ")
for i in range(len(username)):
    if username[i] == " ":
        continue
    if i == 0 or username[i-1] == " ":
        print(username[i].upper(), end="")
    else:
        print(username[i].lower(), end="")
print()