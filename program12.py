#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers = set()
for i in range(5):
    try:
        user_number = float(input(f"Enter any number, number {i + 1}: "))
        numbers.add(user_number)
    except ValueError:
        print("invalid input")
numbers = list(numbers)
no_duplicate = [print(i, end= " ") for i in numbers]
    