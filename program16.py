#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
num_container = []
duplicate = set()
for i in range(10):
    while True:
        user_number = input(f"Enter number {i}: ")
        try:
            user_number = float(user_number)
            if user_number not in num_container:
                num_container.append(user_number)
                break
            duplicate.add(user_number)
            break
        except ValueError:
            print("Invalid input!")
            continue
for i in duplicate:
    print(i, end=" ")