
def read_number():
    try:
        return int(input("Please enter a number: "))
    except ValueError:
        print(f"Invalid number!")
        return None


def run():
    go_on = ""
    while go_on != "n":
        print("This calculator adds numbers provided by you!")
        one = read_number()
        if one:
            two = read_number()
            if two:
                print(f"Result: {one + two}")
        print("Do you want to continue? (Y/n)")
        go_on = input("Choice: ")


run()
