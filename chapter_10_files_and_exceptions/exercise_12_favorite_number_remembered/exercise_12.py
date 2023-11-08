import json
from pathlib import Path


def run():
    file_name = "favorite_numbers.json"
    file = Path(file_name)
    new_numbers = []
    if file.is_file():
        try:
            favorite_numbers = json.loads(file.read_text())
        except ValueError:
            print("Can not read favorite numbers from file!")
        else:
            print("Your favorite numbers are:")
            [print(f"- {f}") for f in favorite_numbers]
            new_numbers = favorite_numbers
    text = input("Want to add a new favorite number? ")
    try:
        new_numbers.append(int(text))
    except ValueError:
        print("The provided value is not a valid number!")
    else:
        file.write_text(json.dumps(new_numbers))


run()
