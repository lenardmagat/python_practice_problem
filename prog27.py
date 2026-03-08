#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
userinput = input("Enter anything you want to enter: ")
num_word = 0
for i in range(len(userinput)):
    if userinput[i] == " ":
        if userinput[i-1] != " ":
            num_word += 1
    elif i == len(userinput) - 1:
        num_word += 1
print(f"number of words: {num_word}")
