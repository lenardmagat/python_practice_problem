#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 != num2:
        print("Not Equal")
    else:
        print("Equal") 
except ValueError:
    print("Invalid input!")
