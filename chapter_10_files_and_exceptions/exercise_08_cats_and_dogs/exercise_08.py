from pathlib import Path


def get_names_from_file(uri):
    try:
        path = Path(uri)
        return path.read_text().splitlines()
    except FileNotFoundError:
        print(f"File '{uri}' does not exist!")
        return None


def main():
    cats = get_names_from_file("cats.txt")
    rabbits = get_names_from_file("rabbits.txt")
    dogs = get_names_from_file("dogs.txt")

    if cats:
        print("Cats:")
        [print(f"- {c}") for c in cats]
    if rabbits:
        print("Rabbits:")
        [print(f"- {r}") for r in rabbits]
    if dogs:
        print("Dogs:")
        [print(f"- {d}") for d in dogs]


main()
