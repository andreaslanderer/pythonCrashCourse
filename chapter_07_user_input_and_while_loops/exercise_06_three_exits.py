number = 1
while number <= 5:
    print(number)
    number += 1

active = True
while active:
    number = int(input("Enter '0' to exit the program: "))
    if number == 0:
        active = False
    else:
        print("Program continues.")
