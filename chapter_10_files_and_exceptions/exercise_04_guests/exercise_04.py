from pathlib import Path


def persist_guest_list(guest_list, path_to_file):
    path = Path(path_to_file)
    guest_string = ""
    for guest in guest_list:
        guest_string += f"{guest}\n"
    path.write_text(guest_string)


guests = []

print(f"This program assists you to create a new guest list for your next party.")
print(f"At any time, press 'q' to exit the program!")

while True:
    name = input("Enter a name to be added to your guest list: ")
    if name == "q":
        break
    else:
        guests.append(name.title())
        print(f"Thank you. {name.title()} has been added to the guest list.")

persist_guest_list(guest_list=guests, path_to_file="guest_list.txt")
