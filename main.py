from Dealership import *
from variables import *
from methods import GoodByeClient



while True:
    print(dealership_border)
    selection = input(options).lower()
    print()

    if selection == "q":
        GoodByeClient()

    if selection == "1":
        while True:
            selection = input("What are you interested in?\n [q to quit]  [b to back]\n").lower()

            match selection:
                case "q":
                    GoodByeClient()
                case "b":
                    break
                case _:
                    print(invalid_option)

    elif selection == "2":
        print(f"Dealership works at: {work_time}\n")
    elif selection == "3":
        print(about_us)
    else:
        print(invalid_option)