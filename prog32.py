#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
def remove(string, parameter):
    for i in range(len(string)):
        if i == 0 and string[i] == parameter:
            continue
        else:
            print(string[i], end="")
    print()

user_input = input("Enter any strings: ")
remove(user_input, "p") #(string, char you want to remove)pract