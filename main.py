from variables import *
from menu_variables import *
from methods import GoodByeClient, display_cars
from Entities.Dealership import Dealership
from Entities.CarsInfo import CarsInfo

dealership = Dealership()

try:
    print(dealership_border)
    print(welcome)

    while True:
        selection = input(what_do_you_want_1).upper()

        match selection:
            case "Q":
                GoodByeClient()

            case "1":

                while True:
                    selection = input(what_are_you_interested_in_2).upper()

                    match selection:
                        case "Q":
                            GoodByeClient()
                        case "B":
                            break
                        case "1":

                            while True:
                                print("\nAvailable car makes:\n"
                                      f"{q_b_options}")

                                i = 1
                                for car in dealership.brands:
                                    print(f" {i}. {car}")
                                    i += 1

                                option = input("Select car make: ").upper()

                                match option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case "1" | "BMW":
                                        kind_of_car = "BMW"
                                    case "2" | "AUDI":
                                        kind_of_car = "AUDI"
                                    case "3" | "HONDA":
                                        kind_of_car = "HONDA"
                                    case _:
                                        print(invalid_option)
                                        continue

                                list_of_cars = list(dealership.find_car_make(kind_of_car))

                                print()
                                # Display cars
                                display_cars(list_of_cars)
                                # for car in list_of_cars:
                                #     object_carinfo = CarsInfo(car)
                                #     car_stats = object_carinfo.get_car_info_as_string()
                                #
                                #     print(border)
                                #     for stat in car_stats:
                                #         print(stat)
                                # print(border)

                        case "2":

                            while True:
                                option = input(choose_type_of_car_opt).upper()

                                match option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case "1" | "CROSSOVER":
                                        kind_of_car = "Crossover"
                                    case "2" | "SPORTCAR":
                                        kind_of_car = "Sportcar"
                                    case "3" | "PICKUP":
                                        kind_of_car = "Pickup"
                                    case _:
                                        print(invalid_option)
                                        continue

                                list_type_cars = list(dealership.find_car_type(kind_of_car))

                                print()
                                # Display cars
                                for car in list_type_cars:
                                    object_carinfo = CarsInfo(car)
                                    car_stats = object_carinfo.get_car_info_as_string()

                                    print(border)
                                    for stat in car_stats:
                                        print(stat)
                                print(border)

                        case "3":

                            while True:
                                model_option = input(looking_for_car_model).upper()
                                print()

                                match model_option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case _:
                                        list_model_cars = list(dealership.find_car_model(model_option))

                                        print(border)
                                        if not list_model_cars:
                                            print(f"(!) Car model '{model_option}' is not in stock.")
                                            print(border)
                                            continue

                                        # Display cars
                                        for car in list_model_cars:
                                            object_carinfo = CarsInfo(car)
                                            car_stats = object_carinfo.get_car_info_as_string()

                                            for stat in car_stats:
                                                print(stat)
                                            print(border)

                        case "4":
                            list_of_stock_cars = list(dealership.show_all_stock_cars())

                            print(f"\n{border}")
                            # Display cars
                            for car in list_of_stock_cars:
                                object_carinfo = CarsInfo(car)
                                car_stats = object_carinfo.get_car_info_as_string()

                                for stat in car_stats:
                                    print(stat)
                                print(border)

                        case "5":

                            while True:
                                option = input(how_to_sort_opt).upper()

                                match option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case "1":
                                        descending_order = False
                                    case "2":
                                        descending_order = True
                                    case _:
                                        print(invalid_option)
                                        continue

                                list_of_sorted_cars = list(dealership.sort_price(reverse_sort=descending_order))

                                print(f"\n{border}")
                                # Display cars
                                for car in list_of_sorted_cars:
                                    object_carinfo = CarsInfo(car)
                                    car_stats = object_carinfo.get_car_info_as_string()

                                    for stat in car_stats:
                                        print(stat)
                                    print(border)

                        case "6":

                            while True:
                                option = input(choose_benefits_output).upper()

                                match option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case "1":
                                        print(crossover_benefits)
                                    case "2":
                                        print(sportcar_benefits)
                                    case "3":
                                        print(pickup_benefits)
                                    case _:
                                        print(invalid_option)
                        case _:
                            print(invalid_option)

            case "2":
                print(f"\nDealership works at: {work_time}")
            case "3":
                print(about_us)
            case _:
                print(invalid_option)

except KeyboardInterrupt:
    print("\n\n\nThe program was interrupted by the user.")