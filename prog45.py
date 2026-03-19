#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The quotient of two numbers is %s" %str(num1 / num2))
except ValueError:
    print("Invalid input!")
