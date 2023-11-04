
def city_country(city, country):
    """Return a formatted string: (City, Country)"""
    return f"{city.title()}, {country.title()}"


print(city_country("buenos aires", "argentina"))
print(city_country("barcelona", "spain"))
print(city_country("berlin", "germany"))
