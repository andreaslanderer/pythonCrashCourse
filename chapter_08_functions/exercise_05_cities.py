
def describe_city(city, country="Germany"):
    """This function prints a city and its corresponding country"""
    print(f"{city.title()} is located in {country}")


describe_city("Munich")
describe_city("Zurich", "Switzerland")
describe_city(country="Argentina", city="Buenos Aires")
