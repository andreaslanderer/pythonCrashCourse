from pathlib import Path


def ask_for_guests():
    print("Please provide the name of the guests who attended the party.")
    print("Type 'q' to finish the program!")
    guests = []
    while True:
        name = input("Provide the next name: ")
        if name == 'q':
            return guests
        else:
            guests.append(name.title())


def persist_guest_book(guest_book, path_to_file):
    path = Path(path_to_file)
    content = "The following guests visited the party:\n"
    for guest in guest_book:
        content += f"- {guest}\n"
    path.write_text(content)


def main(path_to_file):
    guest_book = ask_for_guests()
    persist_guest_book(guest_book, path_to_file)


main("guest_book.txt")
