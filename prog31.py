#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
user_input = input("Enter any string that starts on space: ")
for i in range(len(user_input)):
    if i == 0 and user_input[0] == " ":
        continue
    else:
        print(user_input[i], end= "")
print()