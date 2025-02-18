from Entities.Car.Crossovers import Crossover
from Entities.Car.Pickups import Pickup
from Entities.Car.Sportcars import Sportcar

first_dealership_cars = [Crossover("BMW", "X5", 2019, 83, 56300, True, False),
                         Sportcar("BMW", "M4", 2018, 59, 55000, False, True),
                         Sportcar("BMW", "M4", 2016, 54, 52400, True, True),
                         Pickup("BMW", "X7", 2021, 88, 45750, True, True),
                         Crossover("AUDI", "Q7", 2020, 85, 60000, True, False),
                         Sportcar("AUDI", "R8", 2023, 73, 72500, True, True),
                         Pickup("AUDI", "ACTIVESPHERE", 2025, 0, 43200, False, True),
                         Crossover("HONDA", "CR-V", 2022, 57, 51050, True, True),
                         Sportcar("HONDA", "NSX", 2015, 59, 34600, False, True),
                         Pickup("HONDA", "RIDGELINE", 2024, 73, 31900, True, False)]

dealership_name = "AutoHub"

work_time = "9:00 - 19:00"

about_us = (f"\nWelcome to {dealership_name} car dealership,\n"
            "your ultimate destination for premium crossovers,\n"
            "high-performance sports cars, and powerful pickups.\n"
            "We offer top brands, expert service, and the best deals to match your driving passion.")