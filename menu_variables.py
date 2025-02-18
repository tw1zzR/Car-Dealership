from Entities.Dealerships.FirstDealership.CreateFirstDealership import first_dealership
from Entities.Dealerships.SecondDealership.CreateSecondDealership import second_dealership
from Entities.Dealerships.ThirdDealership.CreateThirdDealership import third_dealership

q_b_options = "[q to quit]  [b to back]"

ask_which_dealership = ("Which dealership would you like to visit? [q to quit]\n"
                                       f" 1. {first_dealership.dealership_name}\n"
                                       f" 2. {second_dealership.dealership_name}\n"
                                       f" 3. {third_dealership.dealership_name}\n"
                                       "Select an option: ")

what_do_you_want_1 =  ("\nWhat do you want? [q to quit]\n"
                       " 1. Buy a car\n"
                       " 2. Work schedule\n"
                       " 3. About us\n"
                       "Select your option: ")

what_are_you_interested_in_2 = ("\nWhat are you interested in?\n"
                                      " [q to quit]   [b to back]\n"
                                      " ↓    ↓      ↓     ↓     ↓\n"
                                      " 1. Choose car make\n"
                                      " 2. Choose car type \n"
                                      " 3. Find a car model\n"
                                      " 4. All cars in stock\n"
                                      " 5. Sort cars by price\n"
                                      " 6. Car type's benefits\n"
                                      "Select: ")

choose_type_of_car_opt = (f"\nChoose type of car:\n"
                          f"{q_b_options}\n"
                          f" 1. Crossover\n"
                          f" 2. Sportcar\n"
                          f" 3. Pickup\n"
                          f"Select type: ")

looking_for_car_model = ("\nWhat model are you looking for?\n"
                           f"   {q_b_options}      \n"
                           "Enter a car model: ")

how_to_sort_opt = ("\nHow you want to sort?\n"
                  f"{q_b_options}\n"
                   " 1. Low to High ↓\n"
                   " 2. High to Low ↓\n"
                   "Select option: ")

# CASE 6
choose_benefits_output = ("\nChoose option:\n"
                         f"{q_b_options}\n"
                          " 1. Crossovers\n"
                          " 2. Sportcars\n"
                          " 3. Pickups\n"
                          "Select: ")