class Dealership:

    def __init__(self, dealership_name, list_of_cars):
        self.dealership_name = dealership_name
        self.cars = list_of_cars
        self.brands = sorted(set(car.make for car in self.cars), key=lambda car: len(car))

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
            yield car

    def sort_price(self, reverse_sort=False):
        sorted_cars = sorted(self.cars, key=lambda car: car.cost, reverse=reverse_sort)

        for car in sorted_cars:
            yield car