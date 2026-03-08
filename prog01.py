char = []
string = input("enter any characters that end in space character: ")
for i in string:
    if i == len(string) and i == " ":
        break
    char.append(i)
characters = [print(i, end= "") for i in char]