
def build_car(manufacturer, model, **props):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in props.items():
        car[key] = value
    return car
