from variables import *
from methods import GoodByeClient
from Entities.Dealership import Dealership

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
                                print()

                                match option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case "1" | "BMW":
                                        tuple_brand_cars = dealership.find_car_make("BMW")
                                    case "2" | "AUDI":
                                        tuple_brand_cars = dealership.find_car_make("AUDI")
                                    case "3" | "HONDA":
                                        tuple_brand_cars = dealership.find_car_make("HONDA")
                                    case _:
                                        print(invalid_option)
                                        continue

                                # Display cars
                                for car in tuple_brand_cars:
                                    print(border)

                                    for car_stats in car:
                                        print(f"{car_stats}")
                                print(border)

                        case "2":

                            while True:
                                option = input(choose_type_of_car_opt).upper()
                                print()

                                match option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case "1" | "CROSSOVER":
                                        kind_of_car = "Crossover"
                                        tuple_type_cars = dealership.find_car_type(kind_of_car)
                                    case "2" | "SPORTCAR":
                                        kind_of_car = "Sportcar"
                                        tuple_type_cars = dealership.find_car_type(kind_of_car)
                                    case "3" | "PICKUP":
                                        kind_of_car = "Pickup"
                                        tuple_type_cars = dealership.find_car_type(kind_of_car)
                                    case _:
                                        print(invalid_option)
                                        continue

                                # Display cars
                                for car in tuple_type_cars:
                                    print(border)

                                    for car_stats in car:
                                        print(f"{car_stats}")
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
                                        tuple_model_cars = dealership.find_car_model(model_option)

                                        for car in tuple_model_cars:
                                            if car.startswith("(!)"):
                                                invalid_car_model = car
                                                print(invalid_car_model)
                                                break
                                            else:
                                                # Display cars
                                                for car in tuple_model_cars:
                                                    print(border)

                                                    for car_stats in car:
                                                        print(f"{car_stats}")
                                                print(border)

                        case "4":
                            tuple_of_stock_cars = dealership.all_stock_cars()

                            print()
                            # Display cars
                            for car in tuple_of_stock_cars:
                                for car_stats in car:
                                    print(f"{car_stats}")
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
                                        tuple_of_sorted_cars = dealership.sort_price()
                                    case "2":
                                        tuple_of_sorted_cars = dealership.sort_price(reverse_sort=True)
                                    case _:
                                        print(invalid_option)

                                print(f"\n{border}")
                                for car in tuple_of_sorted_cars:
                                    print(car)
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