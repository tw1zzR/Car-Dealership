from Entities.Cars import Car

class Crossover(Car):
    type = "CUV"

    def __init__(self, make, model, year, fuel_capacity, cost, front_wheel, rear_wheel):
        super().__init__(make, model, year, fuel_capacity, cost, front_wheel, rear_wheel, self.type)