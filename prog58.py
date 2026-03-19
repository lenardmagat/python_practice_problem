#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
for i in range(100):
    if (i + 1) % 2 != 0:
        print(f"{i + 1} is odd number")