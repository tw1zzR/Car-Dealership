from Entities.Dealership import *
from variables import *
from methods import GoodByeClient


try:
    dealership = Dealership()

    print(dealership_border)
    print(welcome)

    while True:
        selection = input(options).upper()

        if selection == "Q":
            GoodByeClient()

        if selection == "1":

            while True:
                selection = input("\nWhat are you interested in?\n"
                                  " [q to quit]  [b to back]\n"
                                  "   ↓   ↓   ↓  ↓   ↓   ↓   \n"
                                  " 1. Choose mark\n"
                                  " 2. Choose type \n"
                                  " 3. Find a model\n"
                                  " 4. All cars in stock\n"
                                  " 5. Sort by price\n"
                                  " 6. Car type benefits\n"
                                  "Select: ").upper()

                match selection:
                    case "Q":
                        GoodByeClient()
                    case "B":
                        break
                    case "1":
                        while True:
                            i = 1

                            print("\nAvailable marks:\n"
                                  " [q to quit]  [b to back]")
                            for car in CarInfo.brands:
                                print(f"{i}. {car}")
                                i += 1
                            option = input("Select mark: ").upper()

                            if option == "Q":
                                GoodByeClient()
                            elif option == "B":
                                break
                            elif option == "1" or option == "2" or option == "3":

                                while True:
                                    print(f"\n{border}")
                                    dealership.find_mark(option)
                                    print(f"{border}\n")

                                    found = False
                                    model_option = input("Which one interests you?\n"
                                                   "[q to quit]  [b to back]\n"
                                                   "Enter a model: "
                                                   ).upper()
                                    if model_option == "Q":
                                        GoodByeClient()
                                    elif model_option == "B":
                                        break
                                    for car in dealership.cars:
                                        if model_option == car.model:
                                            found = True
                                            while True:
                                                print(f"\n{border}")
                                                car.display_info()
                                                print(f"{border}")

                                                buy_option = input("\nDo you want to buy this auto? (y/n)\n"
                                                               "      [q to quit]  [b to back]       \n"
                                                               "Enter your choice: ").upper()

                                                if buy_option == "Q":
                                                    GoodByeClient()
                                                elif buy_option == "B":
                                                    break
                                                elif buy_option == "Y":
                                                    print(f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}. Deal amount - {car.cost}$")
                                                    GoodByeClient()
                                                elif buy_option == "N":
                                                    break
                                                else:
                                                    print(invalid_option)
                                    if not found:
                                        print(invalid_option)


                            else:
                                print(invalid_option)

                    case "2":

                        while True:
                            option = input(f"\nChoose type of car:\n"
                                           "[q to quit]  [b to back]\n"
                                           f" 1. Crossovers\n"
                                           f" 2. Sportcars\n"
                                           f" 3. Pickups\n"
                                           f"Select type: ").upper()
                            if option == "Q":
                                GoodByeClient()
                            elif option == "B":
                                break
                            elif option == "1" or option == "2" or option == "3":

                                while True:
                                    print(f"\n{border}")
                                    dealership.find_type(option)
                                    print(border)


                                    found = False
                                    model_option = input("\nWhich one interests you?\n"
                                                         "  [q to quit]  [b to back]\n]"
                                                         "Enter a model: ").upper()

                                    if model_option == "Q":
                                        GoodByeClient()
                                    if model_option == "B":
                                        break
                                    else:

                                        for car in dealership.cars:
                                            if model_option == car.model:
                                                found = True
                                                while True:
                                                    print(f"\n{border}")
                                                    car.display_info()
                                                    print(f"{border}")

                                                    buy_option = input("\nDo you want to buy this auto? (y/n)\n"
                                                                       "      [q to quit]  [b to back]       \n"
                                                                       "Enter your choice: ").upper()

                                                    if buy_option == "Q":
                                                        GoodByeClient()
                                                    elif buy_option == "B":
                                                        break
                                                    elif buy_option == "Y":
                                                        print(
                                                            f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}. Deal amount - {car.cost}$")
                                                        GoodByeClient()
                                                    elif buy_option == "N":
                                                        break
                                                    else:
                                                        print(invalid_option)
                                        if not found:
                                            print(invalid_option)

                            else:
                                print(invalid_option)

                    case "3":

                        while True:
                            option = input("\nWhat model are you looking for?\n"
                                           "   [q to quit]  [b to back]      \n"
                                           "Enter a car model: ").upper()
                            if option == "Q":
                                GoodByeClient()
                            elif option == "B":
                                break
                            else:
                                found = False
                                for car in dealership.cars:
                                    if option == car.model:
                                        while True:
                                            print(f"\n{border}")
                                            dealership.find_model(option)
                                            print(border)

                                            found = True

                                            # while True:
                                            model_option = input("\nHave you been looking for this car? (y/n)\n"
                                                                 "         [q to quit]  [b to back]          \n"
                                                                 "Enter a model: ").upper()
                                            if model_option == "Q":
                                                GoodByeClient()
                                            if model_option == "B":
                                                break
                                            elif model_option == "Y":

                                                while True:
                                                    print(f"\n{border}")
                                                    car.display_info()
                                                    print(f"{border}")

                                                    buy_option = input("\nDo you want to buy this auto? (y/n)\n"
                                                                       "      [q to quit]  [b to back]       \n"
                                                                       "Enter your choice: ").upper()

                                                    if buy_option == "Q":
                                                        GoodByeClient()
                                                    elif buy_option == "B":
                                                        break
                                                    elif buy_option == "Y":
                                                        print(
                                                            f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}. Deal amount - {car.cost}$")
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
                                    print(f"\n{option} not found in the list of available vehicles.")

                    case "4":

                        while True:
                            print()
                            dealership.stock_cars()
                            print(f"{border}")

                            model_option = input("\nWhich one interests you?\n"
                                                 "  [q to quit]  [b to back]\n"
                                                 "Enter a model: ").upper()
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


                                            buy_option = input("\nDo you want to buy this auto? (y/n)\n"
                                                               "      [q to quit]  [b to back]       \n"
                                                               "Enter your choice: ").upper()

                                            if buy_option == "Q":
                                                GoodByeClient()
                                            elif buy_option == "B":
                                                break
                                            elif buy_option == "Y":
                                                print(
                                                    f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}. Deal amount - {car.cost}$")
                                                GoodByeClient()
                                            elif buy_option == "N":
                                                break
                                            else:
                                                print(invalid_option)

                    case "5":

                        while True:
                            option = input("\nHow you want to sort?\n"
                                           "[q to quit]  [b to back]\n"
                                           " 1. Low to High ↑\n"
                                           " 2. High to Low ↓\n"
                                           "Select option: ").upper()
                            if option == "Q":
                                GoodByeClient()
                            elif option == "B":
                                break
                            elif option == "1" or option == "2":

                                while True:
                                    print(f"\n{border}")
                                    dealership.sort_price(option)
                                    print(border)

                                    model_option = input("\nWhich one interests you?\n"
                                                         "  [q to quit]  [b to back]\n"
                                                         "Enter a model: ").upper()
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

                                                    buy_option = input("\nDo you want to buy this auto? (y/n)\n"
                                                                       "      [q to quit]  [b to back]       \n"
                                                                       "Enter your choice: ").upper()

                                                    if buy_option == "Q":
                                                        GoodByeClient()
                                                    elif buy_option == "B":
                                                        break
                                                    elif buy_option == "Y":
                                                        print(
                                                            f"\nCongratulations! You have purchased a car {car.make} {car.model} {car.year}. Deal amount - {car.cost}$")
                                                        GoodByeClient()
                                                    elif buy_option == "N":
                                                        break
                                                    else:
                                                        print(invalid_option)
                                        if not found:
                                            print(invalid_option)
                            else:
                                print(invalid_option)

                    case "6":

                        while True:
                            option = input("\nChoose option:\n"
                                           "[q to quit]  [b to back]\n"
                                           " 1. Crossovers\n"
                                           " 2. Sportcars\n"
                                           " 3. Pickups\n"
                                           "Select: ").upper()
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

        elif selection == "2":
            print(f"\nDealership works at: {work_time}")
        elif selection == "3":
            print(about_us)
        else:
            print(invalid_option)

except KeyboardInterrupt:
    print("\n\n\nThe program was interrupted by the user.")