#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
string = input("Enter any string: ")
for i in range(len(string)):
    if string[i - 1 ]==  " " or i == 0:
        print(string[i].upper(), end="")
        continue
    print(string[i].lower(), end="")
print()
    