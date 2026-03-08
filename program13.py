#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
number_container = []
while True:
    user_number = input("Enter any number: ")
    try:
        user_number = float(user_number)
        if user_number not in number_container:
            number_container.append(user_number)
            print(f"{user_number} is Unique number")
        else: print(f"{user_number} is Duplicate")
    except ValueError:
        print("Invalid input!")
        break