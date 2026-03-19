#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = input("Enter the first number: ")
num2= input("Enter the second number: ")
try:
    num1, num2 = float(num1), float(num2)
    if num1 > num2:
        print("the largest number is %d" %num1)
    else:
        print("the largest number is %d" %num2)
except ValueError:
    print("Invalid input!")
    