ages = [1, 3, 10, 18, 42, 66]

for age in ages:
    if age < 2:
        print("Your are a baby")
    elif age < 4:
        print("You are a toddler")
    elif age < 13:
        print("You are a kid")
    elif age < 20:
        print("You are a teenager")
    elif age < 65:
        print("You are an adult")
    else:
        print("Your are an elder")
