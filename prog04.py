string = input("enter any string: ")
lower = 0
for i in range(len(string)):
    if string[i].lower() == string[i]:
        lower += 1
if lower == len(string): print("all the characters are in lower case")
else: print("not all characters are in lower case")
    