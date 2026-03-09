#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
letter = {
    "A" : "a",
    "B" : "b",
    "C" : "c",
    "D" : "d",
    "E" : "e",
    "F" : "f",
    "G" : "g",
    "H" : "h",
    "I" : "i",
    "J" : "j",
    "K" : "k",
    "L" : "l",
    "M" : "m",
    "N" : "n",
    "O" : "o",
    "P" : "p",
    "Q" : "q",
    "R" : "r",
    "S" : "s",
    "T" : "t",
    "U" : "u",
    "V" : "v",
    "W" : "w",
    "X" : "x",
    "Y" : "y",
    "Z" : "z"
         }
string = input("Enter any string: ")
for i in range(len(string)):
    if string[i].islower():
        print(string[i], end="") 
    else:
        print(letter.get(string[i]), end="")
print()
#or
for i in range(len(string)):
    print(string[i].casefold(), end="")
print()