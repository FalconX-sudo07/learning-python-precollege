# from Classes import Car,ElectricCar
from Classes import Car as C
from Classes import ElectricCar as EC

# from Classes import Car
my_car = C('Audi','A4',2024)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 23
my_car.read_odometer()

# from Classes import ElectricCar
my_e_car = EC("nissan","leaf",2024)
print(my_e_car.get_descriptive_name())
my_e_car.battery.describe_battery()
my_e_car.battery.get_range()
