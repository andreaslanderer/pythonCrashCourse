cities = {
    'buenos_aires': {
        'country': 'argentina',
        'population': 15_490_000
    },
    'new york': {
        'country': 'united states of america',
        'population': 8_468_000
    },
    'stockholm': {
        'country': 'sweden',
        'population': 975_500
    }
}

for city, details in cities.items():
    print(city.title())
    print(f"\tCountry   : {details['country'].title()}")
    print(f"\tPopulation: {details['population']}")
