#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
for i in range(101):
    if str(i)[-1] == "0":
        continue
    print(i)