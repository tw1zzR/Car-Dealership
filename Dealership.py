from Cars import *

class Dealership:

    cars = [Crossover("BMW", "X5", 2019, 83, 56300, True, False),
            Sportcar("BMW", "M4", 2018, 59, 55000, False, True),
            Pickup("BMW", "X7 PICK-UP", 2021, 88, 45750, True, True),
            Crossover("AUDI", "Q7", 2020, 85, 60000, True, False),
            Sportcar("AUDI", "R8", 2023, 73, 72500, True, True),
            Pickup("AUDI", "ACTIVESPHERE", 2025, 0, 43200, False, True),
            Crossover("HONDA", "CR-V", 2022, 57, 51050, True, True),
            Sportcar("HONDA", "NSX", 2015, 59, 34600, False, True),
            Pickup("HONDA", "RIDGELINE", 2024, 73, 31900, True, False)
            ]

    def __init__(self):
        print("Initializing Dealership")


    def find_mark(self, brand):

        # BMW
        if brand == "BMW" or brand == "1":
            for car in self.cars:
                if car.make.startswith("B"):
                    print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
        # Audi
        elif brand == "AUDI" or brand == "2":
            for car in self.cars:
                if car.make.startswith("A"):
                    print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
        # Honda
        elif brand == "HONDA" or brand == "3":
            for car in self.cars:
                if car.make.startswith("H"):
                    print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
        else:
            print(f"{brand} is not in stock.")


    def find_type(self, type):
        quantity = 0

        # Crossovers
        if type.startswith("C") or type == "1":
            for car in self.cars:
                if isinstance(car, Crossover):
                    print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                    quantity += 1
            print(f"\nAvailable {quantity} crossovers. Which one interests you?\n")
        # Sportcars
        elif type.startswith("S") or type == "2":
            for car in self.cars:
                if isinstance(car, Sportcar):
                    print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                    quantity += 1
            print(f"\nAvailable {quantity} sportcars. Which one interests you?\n")
        # Pickups
        elif type.startswith("P") or type == "3":
            for car in self.cars:
                if isinstance(car, Pickup):
                    print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                    quantity += 1
            print(f"\nAvailable {quantity} pickups. Which one interests you?\n")
        else:
            print(f"{type} is not in stock.")

    def find_model(self, model):
        for car in self.cars:
            if model == car.model.split()[0]:
                print(f"{car.cost}$ - {car.make} {car.model} {car.year}")
                print(f"Fuel capacity: {car.fuel_capacity}")
                car.check_drive()
                # if car.all_wheels:
                #     print(f"Complete-Drive: {car.all_wheels}")
                # elif car.front_wheel and not car.rear_wheel:
                #     print(f"Front-Drive: {car.front_wheel}")
                # elif car.rear_wheel and not car.front_wheel:
                #     print(f"Rear-Drive: {car.rear_wheel}")








    def car_maker(self):
        print(f"Car make: {self.make}")

    def car_model(self):
        print(f"Model: {self.model}")

    def car_year(self):
        print(f"Year: {self.year}")

    def car_fuel(self):
        print(f"Fuel capacity: {self.fuel_capacity}")

    def drive(self):
        if self.all_wheels:
            print(f"Complete-Drive: {self.all_wheels}")
        elif self.front_wheel and not self.rear_wheel:
            print(f"Front-Drive: {self.front_wheel}")
        elif self.rear_wheel and not self.front_wheel:
            print(f"Rear-Drive: {self.rear_wheel}")