#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
def just(string, max_char):
    try:
        len_space = max_char - len(string)
    except TypeError:
        return print("Invalid input!")
    if len_space >= 0:
        for i in range(len(string)):
            print(string[i], end="")
        print(" " * len_space, end="")
        print("|") #mark
        return
    else:
        return print("Invalid input!")
    
string = input("Enter any string: ")
just(string, "q")
