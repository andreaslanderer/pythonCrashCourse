import json
from pathlib import Path


def run():
    file_name = "user.json"
    file = Path(file_name)
    if file.is_file():
        user = json.loads(file.read_text())
        response = input(f"Are you {user['user_id']}? (Y/n) ").lower()
        if response != "n":
            print("Welcome back! Here is your basic data:")
            print(f"User ID   : {user['user_id']}")
            print(f"First Name: {user['first_name']}")
            print(f"Last Name : {user['last_name']}")
        else:
            print("Please update your user data:")
            write_user_data(file)
            print("Thank you! Your user data has been successfully updated!")
    else:
        print("Please provide your user data:")
        write_user_data(file)
        print("Thank you! Your user data has been successfully persisted!")


def write_user_data(file):
    user = {
        'user_id': input("User ID   : "),
        'first_name': input("First Name: "),
        'last_name': input("Last Name : ")}
    file.write_text(json.dumps(user))


run()