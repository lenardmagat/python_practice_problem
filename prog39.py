#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
string = input("Enter any string: ")
for i in range(len(string)):
    if i == 0:
        print(string[i].upper(), end="")
        continue
    print(string[i].lower(), end="")
print()