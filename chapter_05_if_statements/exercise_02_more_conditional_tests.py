magicNumber = 42

if magicNumber > 40 and magicNumber < 50:
    print(f"40 < {magicNumber} < 50")

if magicNumber == 0 or magicNumber == 42:
    print(f"{magicNumber} is either 0 or 42")

if 42 in [0, 13, 42]:
    print(f"{magicNumber} is in the list")

if 42 not in range(42):
    print(f"{magicNumber} is not in the range")