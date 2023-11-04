
def make_sandwich(*toppings):
    """Create a custom sandwich with as many items as the client wants"""
    if toppings:
        print("Creating a custom sandwich with:")
        for topping in toppings:
            print(f"- {topping.title()}")
    else:
        print("Creating a sandwich without toppings")


make_sandwich()
make_sandwich("salami")
make_sandwich("salami", "cheese", "onions", "egg")
