from Entities.Dealership import *
from variables import *
from methods import GoodByeClient


try:
    dealership = Dealership()

    while True:
        print(dealership_border)
        selection = input(options).upper()
        print()

        if selection == "Q":
            GoodByeClient()

        if selection == "1":
            while True:
                selection = input("What are you interested in?\n [q to quit]  [b to back]\n 1. Choose mark\n 2. Choose type \n 3. Find a model\n 4. All cars in stock\n 5. Sort by price\n 6. Car type benefits\n").upper()

                match selection:
                    case "Q":
                        GoodByeClient()
                    case "B":
                        break
                    case "1":
                        option = input(f"Available marks - {CarInfo.brands}\nSelect mark: ").upper()
                        print()
                        dealership.find_mark(option)
                        print()
                    case "2":
                        option = input(f"Choose type of car - Crossovers, Sportcars, Pickups\nSelect type: ").upper()
                        print()
                        dealership.find_type(option)
                        print()
                    case "3":
                        option = input("What model are you looking for?").upper()
                        print()
                        dealership.find_model(option)
                        print()
                    case "4":
                        dealership.stock_cars()
                        print()
                    case "5":
                        option = input("\nHow you want to sort?\n 1. Low to High ↑\n 2. High to Low ↓\nSelect option: ").upper()
                        print()
                        print(border)
                        dealership.sort_price(option)
                        print(border)
                        print()
                    case "6":
                        print()
                    case _:
                        print(invalid_option)
                        print()
        elif selection == "2":
            print(f"Dealership works at: {work_time}\n")
        elif selection == "3":
            print(about_us)
        else:
            print(invalid_option)

except KeyboardInterrupt:
    print("\n\n\nThe program was interrupted by the user.")