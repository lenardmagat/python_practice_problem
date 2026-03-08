#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
num_container = []
num = 1
while True:
    user_num = input(f"Enter any number. number {num}: ")
    num += 1
    try:
        user_num = float(user_num)
        num_container.append(user_num)
    except ValueError:
        print("Invalid input!")
        num_container.sort(reverse=True)
        for i in num_container:
            print(i, end= " ")
        break