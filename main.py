from Entities.Cars import CarInfo
from variables import *
from methods import GoodByeClient
from create_dealership import dealership


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
                                i = 1

                                print("\nAvailable marks:\n"
                                      f" {q_b_options}")
                                for car in CarInfo.brands:
                                    print(f"{i}. {car}")
                                    i += 1
                                option = input("Select mark: ").upper()

                                if option == "Q":
                                    GoodByeClient()
                                elif option == "B":
                                    break
                                elif option == "1" or option == "2" or option == "3":

                                    # ???????????????????????????
                                    dealership.confirm_deal()

                                    # while True:
                                    #     print(f"\n{border}")
                                    #     dealership.find_mark(option)
                                    #     print(f"{border}\n")
                                    #
                                    #     model_option = input(which_one_interests_you).upper()
                                    #
                                    #     if model_option == "Q":
                                    #         GoodByeClient()
                                    #     elif model_option == "B":
                                    #         break
                                    #     else:
                                    #         found = False
                                    #         for car in dealership.cars:
                                    #             if model_option == car.model:
                                    #                 while True:
                                    #                     print(f"\n{border}")
                                    #                     car.display_info()
                                    #                     print(f"{border}")
                                    #
                                    #                     found = True
                                    #                     buy_option = input(buy_this_car_question).upper()
                                    #
                                    #                     if buy_option == "Q":
                                    #                         GoodByeClient()
                                    #                     elif buy_option == "B":
                                    #                         break
                                    #                     elif buy_option == "Y":
                                    #                         print(f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}.\nDeal amount - {car.cost}$")
                                    #                         GoodByeClient()
                                    #                     elif buy_option == "N":
                                    #                         break
                                    #                     else:
                                    #                         print(invalid_option)
                                    #         if not found:
                                    #             print(f"\n{model_option} not found in the list of available vehicles.")
                                else:
                                    print(invalid_option)

                        case "2":

                            while True:
                                option = input(choose_type_of_car_opt).upper()

                                if option == "Q":
                                    GoodByeClient()
                                elif option == "B":
                                    break
                                elif option == "1" or option == "2" or option == "3":

                                    while True:
                                        print(f"\n{border}")
                                        dealership.find_type(option)
                                        print(border)

                                        model_option = input(which_one_interests_you).upper()

                                        if model_option == "Q":
                                            GoodByeClient()
                                        if model_option == "B":
                                            break
                                        else:
                                            found = False
                                            for car in dealership.cars:
                                                if model_option == car.model:
                                                    while True:
                                                        print(f"\n{border}")
                                                        car.display_info()
                                                        print(f"{border}")

                                                        found = True
                                                        buy_option = input(buy_this_car_question).upper()

                                                        if buy_option == "Q":
                                                            GoodByeClient()
                                                        elif buy_option == "B":
                                                            break
                                                        elif buy_option == "Y":
                                                            print(f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}.\nDeal amount - {car.cost}$")
                                                            GoodByeClient()
                                                        elif buy_option == "N":
                                                            break
                                                        else:
                                                            print(invalid_option)
                                            if not found:
                                                print(f"\n{model_option} not found in the list of available vehicles.")
                                else:
                                    print(invalid_option)

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
                                            while True:
                                                print(f"\n{border}")
                                                dealership.find_model(model_option)
                                                print(border)

                                                found = True
                                                option = input("\nHave you been looking for this car? (y/n)\n"
                                                                     f"         {q_b_options}          \n"
                                                                     "Enter a model: ").upper()

                                                if option == "Q":
                                                    GoodByeClient()
                                                if option == "B":
                                                    break
                                                elif option == "Y":

                                                    while True:
                                                        print(f"\n{border}")
                                                        car.display_info()
                                                        print(f"{border}")

                                                        buy_option = input(buy_this_car_question).upper()

                                                        if buy_option == "Q":
                                                            GoodByeClient()
                                                        elif buy_option == "B":
                                                            break
                                                        elif buy_option == "Y":
                                                            print(f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}.\nDeal amount - {car.cost}$")
                                                            GoodByeClient()
                                                        elif buy_option == "N":
                                                            break
                                                        else:
                                                            print(invalid_option)
                                                elif model_option == "N":
                                                    break
                                                else:
                                                    print(invalid_option)
                                    if not found:
                                        print(f"\n{model_option} not found in the list of available vehicles.")

                        case "4":

                            while True:
                                print()
                                dealership.stock_cars()
                                print(border)

                                model_option = input(which_one_interests_you).upper()

                                if model_option == "Q":
                                    GoodByeClient()
                                elif model_option == "B":
                                    break
                                else:
                                    found = False
                                    for car in dealership.cars:
                                        if model_option == car.model:
                                            while True:
                                                print(f"\n{border}")
                                                car.display_info()
                                                print(border)

                                                found = True
                                                buy_option = input(buy_this_car_question).upper()

                                                if buy_option == "Q":
                                                    GoodByeClient()
                                                elif buy_option == "B":
                                                    break
                                                elif buy_option == "Y":
                                                    print(f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}.\nDeal amount - {car.cost}$")
                                                    GoodByeClient()
                                                elif buy_option == "N":
                                                    break
                                                else:
                                                    print(invalid_option)
                                    if not found:
                                        print(f"\n{model_option} not found in the list of available vehicles.")

                        case "5":

                            while True:
                                option = input(how_to_sort_opt).upper()

                                if option == "Q":
                                    GoodByeClient()
                                elif option == "B":
                                    break
                                elif option == "1" or option == "2":

                                    while True:
                                        print(f"\n{border}")
                                        dealership.sort_price(option)
                                        print(border)

                                        model_option = input(which_one_interests_you).upper()

                                        if model_option == "Q":
                                            GoodByeClient()
                                        elif model_option == "B":
                                            break
                                        else:
                                            found = False
                                            for car in dealership.cars:
                                                if model_option == car.model:
                                                    while True:
                                                        print(f"\n{border}")
                                                        car.display_info()
                                                        print(border)

                                                        found = True
                                                        buy_option = input(buy_this_car_question).upper()

                                                        if buy_option == "Q":
                                                            GoodByeClient()
                                                        elif buy_option == "B":
                                                            break
                                                        elif buy_option == "Y":
                                                            print(f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}.\nDeal amount - {car.cost}$")
                                                            GoodByeClient()
                                                        elif buy_option == "N":
                                                            break
                                                        else:
                                                            print(invalid_option)
                                            if not found:
                                                print(f"\n{model_option} not found in the list of available vehicles.")
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