from pathlib import Path


def read_from_file(uri):
    path = Path(uri)
    try:
        return path.read_text().splitlines()
    except FileNotFoundError:
        return None


pets = {
    "cats": read_from_file("cats.txt"),
    "rabbits": read_from_file("rabbits.txt"),
    "dogs": read_from_file("dogs.txt"),
}

for pet_type, names in pets.items():
    if names:
        print(f"{pet_type.title()}:")
        [print(f"- {n}") for n in names]