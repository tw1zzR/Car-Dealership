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
                            print()
                            dealership.find_mark(option)
                            print()
                        else:
                            print(invalid_option)

                    case "2":
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
                            print()
                            dealership.find_type(option)
                            print()
                        else:
                            print(invalid_option)
                    case "3":
                        option = input("\nWhat model are you looking for?\n"
                                       "   [q to quit]  [b to back]      \n"
                                       "Enter a car model: ").upper()
                        if option == "Q":
                            GoodByeClient()
                        elif option == "B":
                            break
                        else:
                            dealership.find_model(option)

                    case "4":
                        print()
                        dealership.stock_cars()
                        print(f"{border}")
                    case "5":
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
                            print(border)
                            dealership.sort_price(option)
                            print(border)
                        else:
                            dealership.sort_price(option)
                    case "6":
                        print()
                        option = input("Choose option:\n"
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