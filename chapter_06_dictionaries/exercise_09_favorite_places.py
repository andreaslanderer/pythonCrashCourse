favorite_places = {
    'andreas': ['barcelona', 'zurich'],
    'franziska': ['san diego', 'munich'],
    'iris': ['munich', 'berlin'],
    'julius': ['schwenningen']
}

for name, places in favorite_places.items():
    print(f"{name.title()}")
    [print(f"\t{place.title()}") for place in places]
