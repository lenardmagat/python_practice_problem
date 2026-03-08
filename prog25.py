#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
username = input("Enter you full name")
for i in range(len(username)):
    if i == 0 or username[i-1] == " ":
        print(username[i].capitalize(), end="")
    else:
        print(username[i].lower(), end= "")
print()