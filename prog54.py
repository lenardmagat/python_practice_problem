#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The quotient of two number is %d" %(num1 / num2))
except ValueError:
    print("Invalid input!")
