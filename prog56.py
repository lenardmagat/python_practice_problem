#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
num1 = 0
sum = 0
for i in range(10):
    while True:
        try:
            number = float(input(f"Enter the number {i+1}:"))
            if i == 0:
                num1 = number
                break
            sum += number
            break
        except ValueError:
            print("Invalid error")
print(f"The result is {num1 - sum}")