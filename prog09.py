def char_index(string, parameter):
    index = 0
    for i in range(len(string)):
        index += 1
        if string[i] == parameter:
            return print(index)
        
string = input("Enter any string: ")
char_index(string, "L")