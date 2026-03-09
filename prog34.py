#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
def check_upper(string):
    for i in range(len(string)):
        if not string[i].islower():
            continue
        else:
            return False
    return True

string = input("Enter any string: ")
print(check_upper(string))
