#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even = 0
for i in range(10):
    while True:
        try:
            number = float(input(f"Enter the number {i + 1}: "))
            if number % 2 == 0:
                even += 1
                break
            break
        except ValueError:
            print("Invalid input!")
            continue
print(f"number of even is {even}")