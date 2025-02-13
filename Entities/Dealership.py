from Entities.Car.Crossovers import Crossover
from Entities.Car.Sportcars import Sportcar
from Entities.Car.Pickups import Pickup
from Entities.CarsInfo import CarsInfo
from variables import border


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

    brands = sorted(set(car.make for car in cars), key=lambda car: len(car))

    def __init__(self):
        self.dealership_name = "9LPUK-XY9LPUK"

    # Dealership abilities
    def find_car_make(self, brand):
        for car in self.cars:
            if car.make == brand:
                yield car

    def find_car_type(self, type):
        class_type = globals()[type]

        for car in self.cars:
            if isinstance(car, class_type):
                yield car

    def find_car_model(self, model):
        for car in self.cars:
            if model == car.model:
                yield car

    def show_all_stock_cars(self):
        for car in self.cars:
            print(border)
            yield car

    def sort_price(self, reverse_sort=False):
        sorted_cars = sorted(self.cars, key=lambda car: car.cost, reverse=reverse_sort)

        for car in sorted_cars:
            yield car