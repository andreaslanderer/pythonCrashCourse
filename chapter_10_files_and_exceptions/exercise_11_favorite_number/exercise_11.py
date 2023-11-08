import json
from pathlib import Path


def read_file(path):
    return Path(path)


def read_number(file):
    text = file.read_text("utf-8")
    number = json.loads(text)
    try:
        return int(number)
    except ValueError:
        print("Error: Persisted value is not a number!")
        return None


def run():
    file_name = "favorite_number.json"
    file = read_file(file_name)
    if file.is_file():
        number = read_number(file)
        print(f"I know your favorite number: {number}")
    text = input("What is your favorite number? ")
    try:
        text_as_int = int(text)
    except ValueError:
        print("Error: Provided value is not a number!")
    else:
        file.write_text(json.dumps(text_as_int))


run()
