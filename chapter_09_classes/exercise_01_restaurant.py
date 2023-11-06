class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = True

    def describe_restaurant(self):
        print(f"The {self.cuisine_type.title()} restaurant is called {self.restaurant_name.title()}.")

    def open_restaurant(self):
        if self.open:
            print("The restaurant is opened.")
        else:
            print("The restaurant is closed.")

    def open(self):
        self.open = True

    def close(self):
        self.open = False


my_restaurant = Restaurant("Luigi", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.close()
my_restaurant.open_restaurant()
