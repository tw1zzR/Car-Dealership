from Entities.CarCrossovers import Crossover
from Entities.CarSportcars import Sportcar
from Entities.CarPickups import Pickup
from Entities.CarsInfo import CarsInfo
from variables import border


class Dealership:

    cars = [Crossover("BMW", "X5", 2019, 83, 56300, True, False),
            Sportcar("BMW", "M4", 2018, 59, 55000, False, True),
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

        for car in self.cars:
            if car.make not in self.brands:
                self.brands.append(car.make)

    # Dealership abilities
    def find_car_make(self, brand):

        match brand:
            case "1": # BMW
                for car in self.cars:
                    if car.make == "BMW":
                        print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
            case "2": # AUDI
                for car in self.cars:
                    if car.make == "AUDI":
                        print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
            case "3": # HONDA
                for car in self.cars:
                    if car.make == "HONDA":
                        print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
            case _:
                print(f"{brand} is not in stock.")


    def find_type(self, type):
        quantity = 0

        match type:
            case "1": # Crossovers
                for car in self.cars:
                    if isinstance(car, Crossover):
                        print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                        quantity += 1
                print(f"\nAvailable {quantity} crossovers.")
            case "2": # Sportcars
                for car in self.cars:
                    if isinstance(car, Sportcar):
                        print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                        quantity += 1
                print(f"\nAvailable {quantity} sportcars.")
            case "3": # Pickups
                for car in self.cars:
                    if isinstance(car, Pickup):
                        print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                        quantity += 1
                print(f"\nAvailable {quantity} pickups.")
            case _:
                print(f"{type} is not in stock.")


    def find_model(self, model):
        found = False

        for car in self.cars:
            if model == car.model:
                print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                print(f"Fuel capacity: {car.fuel_capacity}")
                # Other stats
                print(CarsInfo.check_drive(car))
                found = True

        if not found:
            print(f"{model} is not in stock.")


    def stock_cars(self):
        for car in self.cars:
            print(border)
            print(f"{car.make} {car.model} {car.year}")
            print(f"Fuel capacity: {car.fuel_capacity}")
            # Other stats
            print(CarsInfo.check_drive(car))
            print(f"Cost: {car.cost}$")


    def sort_price(self, price):

        def cost_key(e):
            return e.cost

        match price:
            case "1": # High to Low
                self.cars.sort(key=cost_key)
            case "2": # Low to High
                self.cars.sort(reverse=True, key=cost_key)

        for car in self.cars:
            print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
