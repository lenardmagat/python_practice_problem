#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
def center(string, final_total_char, char_to_fill):
    try:
        spaces = (final_total_char - len(string))//2
    except TypeError:
        return print("Invalid input!")
    if spaces > 0:
        print(char_to_fill * spaces, end="")
        for i in range(len(string)):
            print(string[i], end="")
        print(char_to_fill * spaces)
        return
    return print(string)

string = input("Enter any string: ")
center(string, 15, "-")