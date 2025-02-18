class CarInfo():

    def __init__(self, car):
        self.car = car

    def check_drive(self):
        if self.car.all_wheels:
            return f"Complete-Drive: {self.car.all_wheels}"
        elif self.car.front_wheel and not self.car.rear_wheel:
            return f"Front-Drive: {self.car.front_wheel}"
        elif self.car.rear_wheel and not self.car.front_wheel:
            return f"Rear-Drive: {self.car.rear_wheel}"

    def get_car_info_as_string(self):
        car_class_name = type(self.car).__name__
        return (f"{self.car.cost}$ | {self.car.make} {self.car.model} {self.car.year} [{car_class_name}]",
               f"Fuel Capacity: {self.car.fuel_capacity}",
               CarInfo.check_drive(self))


# class CarsInfo():
#
#     @classmethod
#     def check_drive(self, car):
#         if car.all_wheels:
#             return f"Complete-Drive: {car.all_wheels}"
#         elif car.front_wheel and not car.rear_wheel:
#             return f"Front-Drive: {car.front_wheel}"
#         elif car.rear_wheel and not car.front_wheel:
#             return f"Rear-Drive: {car.rear_wheel}"
#
#     @classmethod
#     def show_car_info(self, car):
#         return (f"{car.cost}$ | {car.make} {car.model} {car.year} [{car.type}]",
#                 f"Fuel Capacity: {self.car.fuel_capacity}",
#                 CarsInfo.check_drive(car))