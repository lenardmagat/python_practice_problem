#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
number_container = []
num = 0
while True:
    user_number = input(f"Enter any number. number {num + 1}: ")
    num += 1
    try:
        user_number = float(user_number)
        number_container.append(user_number)
    except ValueError:
        print("Invlaid input!")
        highest_number = max(number_container)
        print(f"highest number is: {highest_number}")
        break
