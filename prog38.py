#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
string = input("Enter any string: ")
for i in range(len(string)):
    if string[i].islower():
        print(string[i].capitalize(), end="")
    else:
        print(string[i].lower(), end="")
print()