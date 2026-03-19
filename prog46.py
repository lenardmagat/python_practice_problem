#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The {num1} to the power of {num2} is equal to {num1 ** num2} ")
except ValueError:
    print("Invalid input!")
