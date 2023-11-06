
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_server = 0

    def print_number_server(self):
        print(f"Today, we have served {self.number_server} guest/s so far.")

    def increment_number_served(self, guests):
        if guests > 0:
            self.number_server += guests
        else:
            print(f"Number of guests must be greater than 0 but was: {guests}")


my_restaurant = Restaurant(name="Luigi's", cuisine_type="Italian")
my_restaurant.print_number_server()
my_restaurant.number_server = 5
my_restaurant.print_number_server()
my_restaurant.increment_number_served(-1)
my_restaurant.increment_number_served(7)
my_restaurant.print_number_server()
