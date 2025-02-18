from Entities.Car.Crossovers import Crossover
from Entities.Car.Pickups import Pickup
from Entities.Car.Sportcars import Sportcar

third_dealership_cars = [Pickup("BMW", "X7", 2020, 88, 47000, True, True),
                         Sportcar("BMW", "M4", 2019, 59, 56500, False, True),
                         Sportcar("BMW", "M4", 2017, 54, 51000, True, True),
                         Sportcar("BMW", "I8", 2021, 30, 118000, True, True),
                         Sportcar("BMW", "M5", 2023, 6, 93000, True, True),
                         Sportcar("BMW", "Z4 M40I", 2021, 14, 67500, True, True),
                         Crossover("BMW", "X5", 2021, 83, 58000, True, False),
                         Pickup("AUDI", "ACTIVESPHERE", 2025, 0, 43200, False, True),
                         Sportcar("AUDI", "R8", 2021, 73, 70500, True, True),
                         Sportcar("AUDI", "TT RS", 2020, 40, 67000, True, True),
                         Sportcar("AUDI", "RS5", 2023, 18, 76500, True, True),
                         Sportcar("AUDI", "RS7", 2024, 4, 108000, True, True),
                         Crossover("AUDI", "Q7", 2019, 85, 59000, True, False),
                         Pickup("HONDA", "RIDGELINE", 2022, 73, 30500, True, False),
                         Pickup("HONDA", "TACTICAL", 2021, 15, 37500, False, True),
                         Sportcar("HONDA", "NSX", 2017, 59, 36000, False, True),
                         Sportcar("HONDA", "CIVIC TYPE R", 2022, 8, 44000, True, True),
                         Sportcar("HONDA", "S2000", 2011, 55, 34000, True, True),
                         Crossover("HONDA", "CR-V", 2020, 57, 49500, True, True),
                         Pickup("MERCEDES", "X-CLASS", 2020, 60, 46000, True, True),
                         Sportcar("MERCEDES", "AMG GT", 2023, 22, 128000, True, True),
                         Sportcar("MERCEDES", "SL 63 AMG", 2019, 28, 112000, True, True),
                         Sportcar("MERCEDES", "C63 AMG", 2021, 7, 96000, True, True),
                         Crossover("MERCEDES", "GLE", 2022, 10, 74000, True, False)]

dealership_name = "CarZone"

work_time = "10:00 - 19:00"

about_us = (f"\nWelcome to {dealership_name}, where performance meets elegance.\n"
             "Explore our handpicked collection of top-tier crossovers,\n"
             "thrilling sports cars, and tough pickups.\n"
             "Exceptional quality, personalized service, and the best deals await you!")