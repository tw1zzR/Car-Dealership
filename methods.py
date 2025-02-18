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
    all_cars = len(list_of_cars)
    cars_all_count = {"Crossover": 0, "Pickup": 0, "Sportcar": 0}

    for car in list_of_cars:
        car_type = type(car).__name__
        if car_type in cars_all_count:
            cars_all_count[car_type] += 1

    # Show info
    print (f"→ Available {all_cars} cars:")
    for car_type, cars_count in cars_all_count.items():
        print(f"{cars_count} {car_type}s.", end=" ")
    print(f"\n{border}")