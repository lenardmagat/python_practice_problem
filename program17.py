#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
number = {}
duplicates = []
while True:
    user_number = input("Enter any number: ")
    try:
        user_number = float(user_number)
        if str(user_number) not in number:
            number[str(user_number)] = 1
        else:
            number[str(user_number)] += 1
    except ValueError:
        highest_duplicate = max(number.values())
        for key, value in number.items():
            if value == highest_duplicate:
                duplicates.append(key)
        print("Highest duplicates number: ", *duplicates)
        break
        