#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
string = input("Enter any string: ")
for i in range(len(string)):
    print(string[i].capitalize(), end="")
    print()