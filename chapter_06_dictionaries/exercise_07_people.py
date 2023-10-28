andreas = {'first_name': 'andreas', 'last_name': 'landerer', 'city': 'zurich'}
franziska = {'first_name': 'franziska', 'last_name': 'schneider', 'city': 'san diego'}
iris = {'first_name': 'iris', 'last_name': 'landerer', 'city': 'munich'}
julius = {'first_name': 'julius', 'last_name': 'schneider', 'city': 'freiburg'}

people = [andreas, franziska, iris, julius]

for person in people:
    print(f"First Name: {person['first_name'].title()}")
    print(f"Last Name : {person['last_name'].title()}")
    print(f"City      : {person['city'].title()}\n")
