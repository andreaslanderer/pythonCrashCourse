
def make_car(manufacturer, model, **properties):
    properties['manufacturer'] = manufacturer
    properties['model'] = model
    return properties


cars = [
    make_car("Audi", "A4"),
    make_car("Lamborghini", "Gallardo", price=130_000),
    make_car("Tesla", "Model 3", price=50_000, range=330)
]

for car in cars:
    for key, value in car.items():
        print(f"{key.title()}: {value}")
    print("---")
