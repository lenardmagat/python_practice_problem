#Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.
num_char = 0
username = input("Enter your full name: ")
for i in range(len(username)):
    num_char += 1
print(f"The number of charcter in your name is: {num_char}")    