#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
string = input("Enter any string: ")
is_beginning_space = True
for i in range(len(string)):
    if is_beginning_space and string[i] == " ":
        continue
    is_beginning_space = False
    print(string[i], end= "")
print()