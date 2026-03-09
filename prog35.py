#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
def ends_with(string, parameter):
    matches = 0
    for i in range((len(string) - len(parameter)), len(string), 1):
        if string[i] == parameter[matches]:
            matches += 1
            continue 
        else:
            return False
    return True

string = input("Enter any string: ")
print(ends_with(string, "practice"))