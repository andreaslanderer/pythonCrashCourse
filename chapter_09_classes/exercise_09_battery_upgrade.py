
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_into(self):
        print(f"{self.year} {self.make.title()} {self.model.title()}")


class ElectricCar(Car):

    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)
        self.battery = battery

    def print_into(self):
        super().print_into()
        self.battery.print_info()


class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def print_info(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


audi_a4 = Car("audi", "a4", 2022)
audi_a4.print_into()

tesla_model_s = ElectricCar("tesla", "model s", 2023, Battery())
tesla_model_s.print_into()
tesla_model_s.battery.upgrade_battery()
tesla_model_s.print_into()
