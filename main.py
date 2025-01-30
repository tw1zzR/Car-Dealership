from Dealership import *
from variables import *
from methods import GoodByeClient

dealership = Dealership()

while True:
    print(dealership_border)
    selection = input(options).upper()
    print()

    if selection == "Q":
        GoodByeClient()

    if selection == "1":
        while True:
            selection = input("What are you interested in?\n [q to quit]  [b to back]\n 1. Choose mark\n 2. Choose type \n 3. Find a model\n 4. All cars in stock\n 5.").upper()

            match selection:
                case "Q":
                    GoodByeClient()
                case "B":
                    break
                case "1":
                    option = input(f"Available marks - {CarInfo.brands}\n Select mark: ").upper()
                    print()
                    dealership.find_mark(option)
                    print()
                case "2":
                    option = input(f"Choose type of car - Crossovers, Sportcars, Pickups\n Select type: ").upper()
                    print()
                    dealership.find_type(option)
                    print()
                case _:
                    print(invalid_option)
    elif selection == "2":
        print(f"Dealership works at: {work_time}\n")
    elif selection == "3":
        print(about_us)
    else:
        print(invalid_option)