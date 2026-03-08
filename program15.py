#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
number_container = []
while True:
    user_number = input("Enter any number")
    try:
        user_number = float(user_number)
        number_container.append(user_number)
    except ValueError:
        number_container.sort()
        [print(i, end="") for i in number_container]
        print()
        print("Invalid input!")
        break