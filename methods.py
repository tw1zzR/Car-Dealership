from Entities.CarsInfo import CarsInfo
from variables import border


def GoodByeClient():
    print("\nHave a nice day! Good bye!")
    exit()

def display_list_of_cars(list_of_cars):
    for car in list_of_cars:
        object_carinfo = CarsInfo(car)
        car_stats = object_carinfo.get_car_info_as_string()

        print(border)
        for stat in car_stats:
            print(stat)
    print(border)