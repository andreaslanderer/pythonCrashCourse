
class Restaurant:

    def __init__(self, name, cuisine_type, open=False):
        self.name = name
        self.cuisine_type = cuisine_type
        self.open=open

    def describe(self):
        print(f"The {self.cuisine_type.title()} restaurant named {self.name.title()}")
        print(f"Open: {self.open}")
        print("---")

    def open_restaurant(self):
        self.open = True

    def close_restaurant(self):
        self.open = False


restaurants = [
    Restaurant("Onion Diner", "American"),
    Restaurant("Luigi", "Italian"),
    Restaurant("Paolo", "French")
]

[r.describe() for r in restaurants]
[r.open_restaurant() for r in restaurants]
[r.describe() for r in restaurants]
