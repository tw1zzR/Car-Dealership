from create_lists_of_cars import first_dealership_cars, second_dealership_cars, third_dealership_cars
from Entities.Dealership import Dealership


first_dealership = Dealership(first_dealership_cars)

second_dealership = Dealership(second_dealership_cars)

third_dealership = Dealership(third_dealership_cars)


print(first_dealership.cars)
print(second_dealership.brands)