#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
parameter = "p"
string = input("Enter any string: ")
if string[0] == parameter:
    print(f"the string is starts with parameter {parameter}")
else: print("the string is not stars with given parameter")

#or in function type and multiple char
def isstartwith(string, parameter):
    indices = 0
    match_char = 0
    for i in range(len(string)):
        indices +=1
        if string[i] == parameter[i]:
            match_char += 1
        if indices == len(parameter) or len(string) < len(parameter):
            if match_char == len(parameter): return True
            else: return False

print(isstartwith(string, "practice")) 