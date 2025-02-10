from Entities.Cars import Car

class CarsInfo(Car):

    def __init__(self):
        super().__init__()

    def check_drive(self):
        if self.all_wheels:
            return f"Complete-Drive: {self.all_wheels}"
        elif self.front_wheel and not self.rear_wheel:
            return f"Front-Drive: {self.front_wheel}"
        elif self.rear_wheel and not self.front_wheel:
            return f"Rear-Drive: {self.rear_wheel}"

    # def show_car_info(self, car):
    #     return (f"{car.cost}$ | {car.make} {car.model} {car.year} [{car.type}]",
    #            f"Fuel Capacity: {car.fuel_capacity}",
    #            CarsInfo.check_drive(car))
    #
    # class CarsInfo(Car):
    #     def __init__(self, car):
    #         super().__init__()
    #         self.car = car
    #
    #     def check_drive(self):
    #         if self.all_wheels:
    #             return f"Complete-Drive: {self.all_wheels}"
    #         elif self.front_wheel and not self.rear_wheel:
    #             return f"Front-Drive: {self.front_wheel}"
    #         elif self.rear_wheel and not self.front_wheel:
    #             return f"Rear-Drive: {self.rear_wheel}"
    #
    #     def show_car_info(self):
    #         return (f"{self.cost}$ | {self.make} {self.model} {self.year} [{self.type}]",
    #                 f"Fuel Capacity: {self.fuel_capacity}",
    #                 CarsInfo.check_drive(self))