from pathlib import Path


def run():
    running = True
    path = Path("alice.txt")
    try:
        content_lines = path.read_text("utf-8").splitlines()
    except FileNotFoundError:
        print("The file does not exist!")
    else:
        while running:
            print("This program tells you how often a word appears in 'Alice in Wonderland'.")
            print("Press 'q' to stop the program!")
            word = input("Which word are you looking for for? ")
            if word == "q":
                running = False
            else:
                count = 0
                for line in content_lines:
                    count += line.lower().count(word.lower())
                print(f"The word '{word}' appears {count} times.")


run()
