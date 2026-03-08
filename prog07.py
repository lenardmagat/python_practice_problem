#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
def add_zero_beginning(string, total_length_string):
    space = total_length_string - len(string)
    if space > 0:
        print("0" * space, end="")
        print(string)
        return
    print(string)

string = input("Enter any string: ")
add_zero_beginning(string, 10)