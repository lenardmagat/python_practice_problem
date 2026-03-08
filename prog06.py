def add_space_beginning(string, total_length_string):
    space = total_length_string - len(string)
    if space > 0:
        print(" " * space, end="")
        print(string)
        return
    print(string)

string = input("Enter any string: ")
add_space_beginning(string, 10)