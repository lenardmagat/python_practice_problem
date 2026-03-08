def c_count(string, parameter):
    parameter_match = 0
    for i in range(len(string)):
        if string[i] == parameter:
            parameter_match += 1
    return print(parameter_match)

string = input("Enter any string")
c_count(string, "L")
