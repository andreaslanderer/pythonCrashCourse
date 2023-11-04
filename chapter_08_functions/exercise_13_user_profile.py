
def build_profile(first_name, last_name, **properties):
    properties['first_name'] = first_name
    properties['last_name'] = last_name
    for key, value in properties.items():
        print(f"{key.title()}: {value.title()}")


build_profile("andreas",
              "landerer",
              date_of_birth="11.02.1983",
              gender='male',
              profession='software architect')
