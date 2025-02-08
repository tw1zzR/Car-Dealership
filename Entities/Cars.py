class Car:

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