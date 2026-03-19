#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The product of two numbers is %d" %(num2 * num1))
except ValueError:
    print("Invalid input!")
