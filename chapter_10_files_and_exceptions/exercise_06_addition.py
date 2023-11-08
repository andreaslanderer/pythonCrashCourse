
def addition():
    print("This program adds to numbers that have been chosen by you.")
    print("Please provide two valid numbers!")
    try:
        number_one = int(input("Number 1: "))
        number_two = int(input("Number 2: "))
    except ValueError:
        print("The number provided was not valid!")
        return None
    else:
        return number_one + number_two


result = addition()
if result:
    print(f"Result: {result}")
