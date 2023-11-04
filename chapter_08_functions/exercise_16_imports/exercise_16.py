
from cars import build_car

car = build_car(
    "Lamborghini",
    "Murciélago",
    power="580ps",
    transmission="6-speed manual",
    price="USD 250'000")

for key, value in car.items():
    print(f"{key.title()}: {value.title()}")
