#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

user_input = input("Enter a number between 0-1000: ")
if not user_input.isdigit():
    print("Invalid input")
elif 0 <= float(user_input) <= 1000:
    number_len = len(user_input)
    print("0" * (6 - number_len), end="")
    print(user_input)
else:
    print("between 0-1000 only!")