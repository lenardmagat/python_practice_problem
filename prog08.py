#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
def c_count(string, parameter):
    char_match = 0
    parameter_match = 0
    for i in range(len(string)):
        if string[i] == parameter[char_match]:
            char_match += 1
            if char_match == len(parameter):
                parameter_match += 1
                char_match = 0
        else:
            char_match = 0
    return print(parameter_match)

string = input("Enter any string: ")
paramter = "practice"
c_count(string, paramter)
