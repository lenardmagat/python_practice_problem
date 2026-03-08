#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
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
        sum = 0
        for i in num_container:
            sum += i
        print(f"Averag of the number you input is: {sum/len(num_container):.2f}")
        break