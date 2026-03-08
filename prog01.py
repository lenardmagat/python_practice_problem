char = []
string = input("enter any characters that end in space character: ")
for i in range(len(string)):
    if i == len(string)-1 and i == " ":
        break
    char.append(i)
characters = [print(i, end= "") for i in char]