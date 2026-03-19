#Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The difference of two number is %d" %(num1 - num2))
except ValueError:
    print("Invalid input!")
