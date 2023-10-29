user_polls = {}

poll_active = True
while poll_active:
    name = input("What is your name? ")
    location = input("Where would you like to travel to? ")
    end = input("Do you want to end the poll (yes/no)? ")
    user_polls[name] = location
    if end == "yes":
        poll_active = False
    else:
        print()

for user, location in user_polls.items():
    print(f"{user.title()} wants to travel to {location.title()}")