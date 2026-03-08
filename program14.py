#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
number_container = []
while True:
    user_number = input("Enter any number")
    try:
        user_number = float(user_number)
        number_container.append(user_number)
    except ValueError:
        if len(number_container) >0:
            print(f"minimum number you enter is: {min(number_container)}")
            print("Invalid input!")
            break
        else: 
            print("Invalid input!")
            break
            