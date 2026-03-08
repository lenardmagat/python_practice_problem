#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
def char_index(string, parameter):
    index = 0
    for i in range(len(string), 0, -1):
        index += 1
        if string[i - 1] == parameter:
            return print(index)
        
string = input("Enter any string: ")
char_index(string, "L")