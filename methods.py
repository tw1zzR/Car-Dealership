from Entities.Car.Crossovers import Crossover
from Entities.Car.Pickups import Pickup
from Entities.Car.Sportcars import Sportcar
from Entities.CarInfo import CarInfo
from variables import border


def say_goodbye_and_exit():
    print("\nHave a nice day! Good bye!")
    exit()

def display_list_of_cars(list_of_cars):
    for car in list_of_cars:
        object_carinfo = CarInfo(car)
        car_stats = object_carinfo.get_car_info_as_string()

        print(border)
        for stat in car_stats:
            print(stat)
    print(border)

def show_car_types_count(list_of_cars):
    cars_all_count = len(list_of_cars)
    crossover_count = 0
    sportcar_count = 0
    pickup_count = 0

    for car in list_of_cars:
        if isinstance(car, Crossover):
            crossover_count += 1
        elif isinstance(car, Sportcar):
            sportcar_count += 1
        elif isinstance(car, Pickup):
            pickup_count += 1

    print (f"→ Available {cars_all_count} cars:\n"
           f"→ {crossover_count} Crossovers. "
           f"{sportcar_count} Sportcars. "
           f"{pickup_count} Pickups."
           f"\n{border}")