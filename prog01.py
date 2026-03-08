#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
char = []
string = input("enter any characters that end in space character: ")
for i in range(len(string)):
    if i == len(string)-1 and i == " ":
        break
    char.append(i)
characters = [print(i, end= "") for i in char]