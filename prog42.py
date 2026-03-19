#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 == num2:
        print("the two numbers is equal!")
    else:
        print("the two numbers does not equal!")
except ValueError:
    print("Invalid input!")
