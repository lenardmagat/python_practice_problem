#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The remainder is %s" %str((num1 / num2) - int(num1 / num2)))
except ValueError:
    print("Invalid input!")
