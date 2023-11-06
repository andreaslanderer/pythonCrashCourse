"""This module defines the Restaurant class"""


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"Restaurant Name: {self.name.title()}")
        print(f"Type of Cuisine: {self.cuisine_type.title()}")
        print("---")
