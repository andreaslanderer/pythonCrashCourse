
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"Restaurant: {self.name.title()}")
        print(f"\tCuisine Type: {self.cuisine_type.title()}")


class IceCreamStand(Restaurant):

    def __init__(self, name, *flavors):
        super().__init__(name=name, cuisine_type="Ice Cream Stand")
        self.flavors = flavors

    def describe(self):
        super().describe()
        print("\tIce Cream Flavors:")
        [print(f"\t- {f.title()}") for f in self.flavors]


stand_one = IceCreamStand("Alberto Ice Cream", "chocolate", "vanilla")
stand_one.describe()
