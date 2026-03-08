parameter = "p"
string = input("Enter any string: ")
if string[0] == parameter:
    print(f"the string is starts with parameter {parameter}")
else: print("the string is not stars with given parameter")

#or in function type
def isstartwith(string, parameter):
    if string[0] == parameter:
        return True
    return False

print(isstartwith(string, "p")) 