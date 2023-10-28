diego = {'name': 'diego', 'kind_of_animal': 'cat', 'owner': 'silvia'}
jacky = {'name': 'jacky', 'kind_of_animal': 'cat', 'owner': 'birgit'}
oscar = {'name': 'oscar', 'kind_of_animal': 'dog', 'owner': 'annette'}

pets = [diego, jacky, oscar]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind_of_animal']} and belongs to {pet['owner'].title()}")
