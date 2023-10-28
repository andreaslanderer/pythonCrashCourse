favorite_numbers = {
    'andreas': [7, 23],
    'iris': [24],
    'julius': [7, 13]
}

for name, numbers in favorite_numbers.items():
    print(f"Name: {name.title()}")
    [print(f"{n}") for n in numbers]
    print()
