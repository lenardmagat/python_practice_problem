#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_num = 0
for i in range(10):
    while True:
        try:
            number = float(input(f"Enter number {i + 1}: "))
            if(number % 2 != 0):
                odd_num += 1
            break
        except ValueError:
            print("Invalid input!")
            continue
print(f"the number of odds number is {odd_num}")