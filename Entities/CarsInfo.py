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

    # Detailed info about car. Used in confirm deal, not needed
    # def display_info(self):
    #     print(f"Car: {self.make} {self.model}")
    #     print(f"Year: {self.year}")
    #     print(f"Type: {self.type}")
    #     print(f"Fuel capacity: {self.fuel_capacity}")
    #     Car.check_drive(self)
    #     print(f"Cost: {self.cost}$")