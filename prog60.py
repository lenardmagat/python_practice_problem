#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    lower = min(num2, num1)
    higher = max(num2, num1)
    for i in range(lower + 1, higher):
        print(i)
except ValueError:
    print("Invalid input!")
    

