import json
from pathlib import Path


def run():
    file_name = "user.json"
    file = Path(file_name)
    if file.is_file():
        user = json.loads(file.read_text())
        print(f"Welcome back! Here is your basic user information:")
        print(f"- User ID   : {user['user_id']}")
        print(f"- First Name: {user['first_name']}")
        print(f"- Last  Name: {user['last_name']}")
    else:
        print(f"It seems this is the first time you are using this program!")
        print(f"Let's start recording your basic data!")
        user = {
            'user_id': input("Please provide your unique user id: "),
            'first_name': input("Please provide your first name: "),
            'last_name': input("Please provide your last name: ")
        }
        file.write_text(json.dumps(user))
        print("Thank you! We successfully persisted your basic data!")


run()
