
def city_country(city, country, population=''):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
        return result
    else:
        return result
