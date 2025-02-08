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
                            i = 1
                            print("\nAvailable car makes:")
                            for car in dealership.brands:
                                print(f" {i}. {car}")
                                i += 1
                            option = input("Select car make: ").upper()
                            print()

                            i = 1
                            match option:
                                case "Q":
                                    GoodByeClient()
                                case "B":
                                    break
                                case "1" | "BMW":
                                    list_brand_cars = dealership.find_car_make("BMW")
                                case "2" | "AUDI":
                                    list_brand_cars = dealership.find_car_make("BMW")
                                case "3" | "HONDA":
                                    list_brand_cars = dealership.find_car_make("BMW")
                                case _:
                                    print(invalid_option)
                                    continue

                            for car in list_brand_cars:
                                print(f"{i}) {car}")
                                i += 1

                        case "2":

                            while True:
                                option = input(choose_type_of_car_opt).upper()
                                print()

                                i = 1
                                match option:
                                    case "Q":
                                        GoodByeClient()
                                    case "B":
                                        break
                                    case "1" | "CROSSOVER":
                                        kind_of_car = "Crossover"
                                        list_type_cars = dealership.find_car_type(kind_of_car)
                                    case "2" | "SPORTCAR":
                                        kind_of_car = "Sportcar"
                                        list_type_cars = dealership.find_car_type(kind_of_car)
                                    case "3" | "PICKUP":
                                        kind_of_car = "Pickup"
                                        list_type_cars = dealership.find_car_type(kind_of_car)
                                    case _:
                                        print(invalid_option)
                                        continue

                                for car in list_type_cars:
                                    print(f"{i}) {car}")
                                    i += 1

                        case "3":

                            while True:
                                model_option = input("\nWhat model are you looking for?\n"
                                               f"   {q_b_options}      \n"
                                               "Enter a car model: ").upper()
                                if model_option == "Q":
                                    GoodByeClient()
                                elif model_option == "B":
                                    break
                                else:
                                    found = False
                                    for car in dealership.cars:
                                        if model_option == car.model:
                                            found = True

                                            print(f"\n{border}")
                                            dealership.find_model(model_option)
                                            print(border)
                                    if not found:
                                        print(f"\n{model_option} not found in the list of available vehicles.")

                        case "4":
                            print()
                            dealership.stock_cars()
                            print(border)

                        case "5":

                            while True:
                                option = input(how_to_sort_opt).upper()

                                if option == "Q":
                                    GoodByeClient()
                                elif option == "B":
                                    break
                                elif option == "1" or option == "2":
                                    print(f"\n{border}")
                                    dealership.sort_price(option)
                                    print(border)
                                else:
                                    print(invalid_option)

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