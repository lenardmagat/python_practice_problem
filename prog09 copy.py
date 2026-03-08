def char_index(string, parameter):
    index = 0
    for i in range(len(string), 0, -1):
        index += 1
        if string[i-1] == parameter:
            return print(index)
        
string = input("Enter any string: ")
char_index(string, "L")