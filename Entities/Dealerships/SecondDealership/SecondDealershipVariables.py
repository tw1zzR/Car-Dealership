from Entities.Car.Crossovers import Crossover
from Entities.Car.Pickups import Pickup
from Entities.Car.Sportcars import Sportcar

second_dealership_cars = [Crossover("BMW", "X5", 2020, 83, 59250, True, False),
                         Sportcar("BMW", "M4", 2016, 55, 52400, True, True),
                         Pickup("BMW", "X7", 2022, 87, 48750, True, True),
                         Crossover("AUDI", "Q7", 2019, 84, 58000, True, False),
                         Sportcar("AUDI", "R8", 2023, 93, 80500, True, True),
                         Pickup("AUDI", "ACTIVESPHERE", 2024, 0, 40200, False, True),
                         Crossover("HONDA", "CR-V", 2022, 57, 51550, True, True),
                         Sportcar("HONDA", "NSX", 2013, 62, 31600, False, True),
                         Pickup("HONDA", "RIDGELINE", 2025, 73, 36900, True, False),
                         Pickup("MERCEDES-BENZ", "X-CLASS", 2017, 81, 66500, True, True)]

dealership_name = "DriveWorld"

work_time = "8:00 - 16:00"

about_us = (f"\nAt {dealership_name}, we bring you the finest selection of luxury SUVs,\n"
             "cutting-edge sports cars, and rugged pickups.\n"
             "With unbeatable prices, expert guidance, and a seamless buying experience,\n"
             "your dream ride is just a visit away!")