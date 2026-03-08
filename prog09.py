#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
def char_index(string, parameter):
    index = 0
    for i in range(len(string)):
        index += 1
        if string[i] == parameter:
            return print(index)
        
string = input("Enter any string: ")
char_index(string, "L")