from variables import *
from menu_variables import *
from methods import say_goodbye_and_exit, display_list_of_cars, show_car_types_count
from Entities.Dealerships.FirstDealership.CreateFirstDealership import first_dealership
from Entities.Dealerships.SecondDealership.CreateSecondDealership import second_dealership
from Entities.Dealerships.ThirdDealership.CreateThirdDealership import third_dealership
from Entities.Car.Crossovers import Crossover
from Entities.Car.Sportcars import Sportcar
from Entities.Car.Pickups import Pickup


try:
    print(border)

    while True:
        user_dealership_option = input(ask_which_dealership).upper()

        match user_dealership_option:
            case "Q":
                say_goodbye_and_exit()
            case "1":
                selected_dealership = first_dealership
            case "2":
                selected_dealership = second_dealership
            case "3":
                selected_dealership = third_dealership
            case _:
                print(f"{invalid_option}\n")
                continue
        break

    print(f"\n{dealership_border}")
    print(welcome)

    while True:
        selection = input(what_do_you_want_1).upper()

        match selection:
            case "Q":
                say_goodbye_and_exit()
            case "1":

                while True:
                    selection = input(what_are_you_interested_in_2).upper()

                    match selection:
                        case "Q":
                            say_goodbye_and_exit()
                        case "B":
                            break
                        case "1":

                            while True:
                                print("\nAvailable car makes:\n"
                                      f"{q_b_options}")

                                i = 1
                                for car in selected_dealership.brands:
                                    print(f" {i}. {car}")
                                    i += 1

                                option = input("Enter car make: ").upper()

                                if option in selected_dealership.brands:
                                    kind_of_car = option
                                else:
                                    print(invalid_option)
                                    continue

                                list_of_cars = list(selected_dealership.find_car_make(kind_of_car))

                                print()
                                display_list_of_cars(list_of_cars)

                        case "2":

                            while True:
                                option = input(choose_type_of_car_opt).upper()

                                match option:
                                    case "Q":
                                        say_goodbye_and_exit()
                                    case "B":
                                        break
                                    case "CROSSOVER" | "SPORTCAR" | "PICKUP":
                                        for car in selected_dealership.cars:
                                            if option == car.type:
                                                kind_of_car = globals()[option.capitalize()]
                                                break
                                    case _:
                                        print(invalid_option)
                                        continue

                                list_of_cars = list(selected_dealership.find_car_type(kind_of_car))

                                print()
                                display_list_of_cars(list_of_cars)

                        case "3":

                            while True:
                                model_option = input(looking_for_car_model).upper()
                                print()

                                match model_option:
                                    case "Q":
                                        say_goodbye_and_exit()
                                    case "B":
                                        break
                                    case _:
                                        list_of_cars = list(selected_dealership.find_car_model(model_option))

                                        if not list_of_cars:
                                            print(border)
                                            print(f"(!) Car model '{model_option}' is not in stock.")
                                            print(border)
                                            continue

                                        display_list_of_cars(list_of_cars)

                        case "4":
                            list_of_cars = list(selected_dealership.show_all_stock_cars())

                            print()
                            display_list_of_cars(list_of_cars)

                            show_car_types_count(list_of_cars)

                        case "5":

                            while True:
                                option = input(how_to_sort_opt).upper()

                                match option:
                                    case "Q":
                                        say_goodbye_and_exit()
                                    case "B":
                                        break
                                    case "1":
                                        descending_order = False
                                    case "2":
                                        descending_order = True
                                    case _:
                                        print(invalid_option)
                                        continue

                                list_of_cars = list(selected_dealership.sort_price(reverse_sort=descending_order))

                                print()
                                display_list_of_cars(list_of_cars)

                        case "6":

                            while True:
                                option = input(choose_benefits_output).upper()

                                match option:
                                    case "Q":
                                        say_goodbye_and_exit()
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
                print(f"\nDealership works at: {selected_dealership.work_time}")
            case "3":
                print(selected_dealership.about_us)
            case _:
                print(invalid_option)

except KeyboardInterrupt:
    print("\n\n\nThe program was interrupted by the user.")