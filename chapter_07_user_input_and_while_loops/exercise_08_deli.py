sandwich_orders = ["blt", "club", "reuben", "grilled cheese", "submarine"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.title()} sandwich.")

for sandwich in finished_sandwiches:
    print(sandwich)