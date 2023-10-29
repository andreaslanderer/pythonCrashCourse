sandwich_orders = [
    "pastrami",
    "blt",
    "club",
    "pastrami",
    "reuben",
    "grilled cheese",
    "pastrami",
    "submarine"
]

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    print(sandwich)
