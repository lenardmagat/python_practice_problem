#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
for i in range(100):
    if str((i+1))[-1] in ["5", "0"]:
        continue
    print(i + 1)