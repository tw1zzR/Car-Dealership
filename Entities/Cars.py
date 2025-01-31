

class CarInfo:
    brands = []

    def __init__(self, make, model, year, fuel_capacity, cost, front_wheel, rear_wheel, type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.cost = cost
        self.front_wheel = front_wheel
        self.rear_wheel = rear_wheel
        self.type = type

        if self.make not in self.brands:
            self.brands.append(self.make)

        if front_wheel and rear_wheel:
            self.all_wheels = True
        else:
            self.all_wheels = False

    def check_drive(self):
        if self.all_wheels:
            print(f"Complete-Drive: {self.all_wheels}")
        elif self.front_wheel and not self.rear_wheel:
            print(f"Front-Drive: {self.front_wheel}")
        elif self.rear_wheel and not self.front_wheel:
            print(f"Rear-Drive: {self.rear_wheel}")

    def display_info(self):
        print(f"Car: {self.make} {self.model}")
        print(f"Year: {self.year}")
        print(f"Type: {self.type}")
        print(f"Fuel capacity: {self.fuel_capacity}")
        CarInfo.check_drive(self)
        print(f"Cost: {self.cost}$")


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

