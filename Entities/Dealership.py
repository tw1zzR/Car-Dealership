from Entities.CarCrossovers import Crossover
from Entities.CarSportcars import Sportcar
from Entities.CarPickups import Pickup
from Entities.CarsInfo import CarsInfo
from variables import border, invalid_option


class Dealership:

    cars = [Crossover("BMW", "X5", 2019, 83, 56300, True, False),
            Sportcar("BMW", "M4", 2018, 59, 55000, False, True),
            Sportcar("BMW", "M4", 2016, 54, 52400, True, True),
            Pickup("BMW", "X7", 2021, 88, 45750, True, True),
            Crossover("AUDI", "Q7", 2020, 85, 60000, True, False),
            Sportcar("AUDI", "R8", 2023, 73, 72500, True, True),
            Pickup("AUDI", "ACTIVESPHERE", 2025, 0, 43200, False, True),
            Crossover("HONDA", "CR-V", 2022, 57, 51050, True, True),
            Sportcar("HONDA", "NSX", 2015, 59, 34600, False, True),
            Pickup("HONDA", "RIDGELINE", 2024, 73, 31900, True, False)]

    brands = []

    def __init__(self):
        self.dealership_name = "9LPUK-XY9LPUK"

        # Brands appending
        for car in self.cars:
            if car.make not in self.brands:
                self.brands.append(car.make)

    # Dealership abilities
    def find_car_make(self, brand):

        for car in self.cars:
            if car.make == brand:
                yield (f"{car.cost}$ | {car.make} {car.model} {car.year}",
                       f"Fuel Capacity: {car.fuel_capacity}",
                       CarsInfo.check_drive(car))


    def find_car_type(self, type):
        class_type = globals()[type]

        for car in self.cars:
            if isinstance(car, class_type):
                yield (f"{car.cost}$ | {car.make} {car.model} {car.year}",
                       f"Fuel Capacity: {car.fuel_capacity}",
                       CarsInfo.check_drive(car))
            else:
                continue


    def find_car_model(self, model):
        found = False

        for car in self.cars:
            if model == car.model:
                found = True
                yield (f"{car.cost}$ | {car.make} {car.model} {car.year}",
                       f"Fuel Capacity: {car.fuel_capacity}",
                       CarsInfo.check_drive(car))
            else:
                continue
        if not found:
            yield f"(!) Car model '{model}' is not in stock."


    def all_stock_cars(self):

        for car in self.cars:
            print(border)
            yield (f"{car.cost}$ | {car.make} {car.model} {car.year}",
                   f"Fuel Capacity: {car.fuel_capacity}",
                   CarsInfo.check_drive(car))


    def sort_price(self, reverse_sort=False):

        def cost_key(e):
            return e.cost

        sorted_cars = sorted(self.cars, key=cost_key, reverse=reverse_sort)

        for car in sorted_cars:
            yield f"{car.cost}$ | {car.make} {car.model} {car.year}"