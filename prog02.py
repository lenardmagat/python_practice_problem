string = input("Enter any characters: ")
for i in range(len(string)):
    if i == len(string) - 1 and string[i] == "e": # "e" is the parameter
        break
    print(string[i], end="")
    print()

#or function type
def remove_last(string, parameter):
    for i in range(len(string)):
        if i == len(string) - 1 and string[i] == parameter:
             return
        print(string[i], end="")

remove_last(string, "e")