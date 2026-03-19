#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 < num2:
        print("The smallest number is %d" %num1)
    else:
        print("The smallest number is %d" %num2) 
except ValueError:
    print("Invalid input!")
