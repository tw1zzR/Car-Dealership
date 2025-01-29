

class CarInfo:

    def __init__(self, make, model, year, fuel_capacity, cost, front_wheel, rear_wheel, type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.cost = cost
        self.front_wheel = front_wheel
        self.rear_wheel = rear_wheel
        self.type = type

        if front_wheel and rear_wheel:
            self.all_wheels = True
        else:
            self.all_wheels = False

    # def car_maker(self):
    #     print(f"Car make: {self.make}")
    #
    # def car_model(self):
    #     print(f"Model: {self.model}")
    #
    # def car_year(self):
    #     print(f"Year: {self.year}")
    #
    # def car_fuel(self):
    #     print(f"Fuel capacity: {self.fuel_capacity}")
    #
    # def drive(self):
    #     if self.all_wheels:
    #         print(f"Complete-Drive: {self.all_wheels}")
    #     elif self.front_wheel and not self.rear_wheel:
    #         print(f"Front-Drive: {self.front_wheel}")
    #     elif self.rear_wheel and not self.front_wheel:
    #         print(f"Rear-Drive: {self.rear_wheel}")

class Crossover(CarInfo):
    type = "Crossover"

    def __init__(self, make, model, year, fuel_capacity, cost, front_wheel, rear_wheel):
        super().__init__(make, model, year, fuel_capacity, cost, front_wheel, rear_wheel, self.type)

class Sportcar(CarInfo):
    type = "Sportcar"

    def __init__(self, make, model, year, fuel_capacity, cost, front_wheel, rear_wheel):
        super().__init__(make, model, year, fuel_capacity, cost, front_wheel, rear_wheel, self.type)

class Pickup(CarInfo):
    type = "Pickup"

    def __init__(self, make, model, year, fuel_capacity, cost, front_wheel, rear_wheel):
        super().__init__(make, model, year, fuel_capacity, cost, front_wheel, rear_wheel, self.type)

