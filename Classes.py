#from file.py import Class Name -> Basic class import dialogue
# from file.py import Class1,Class2,Classx -> import multiple classes
#from file.py import Class Name as CN -> aliasing class name
class Dog():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title()+" is now sitting.")
        
    def roll_over(self):
        print(self.name.title()+" just rolled over!")
        

class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        lname = str(self.year)+' '+self.make+' '+self.model
        return lname.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        # self.odometer_reading = mileage  just basic
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cant roll back an odometer!')
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery:
    def __init__(self,battery_size=65):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}--KWh Battery")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 275
        print(f"This car can go about {range} Kms on a full charge")
    
mnc = Car('audi','a4',2016)

print(mnc.get_descriptive_name())

mnc.read_odometer()
mnc.odometer_reading = 23
mnc.read_odometer()
mnc.update_odometer(50)
mnc.read_odometer()

moc = Car('Innova','Crysta',2013)
print(moc.get_descriptive_name())

moc.update_odometer(23000)
moc.read_odometer()
moc.increment_odometer(100)
moc.read_odometer()



class ElectricCar(Car):     #ElectricCar is the child class
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        # self.battery_size = 30
        self.battery = Battery()    #Battery_size set on main class Battery
    def describe_battery(self):
        print(f"This car has a {self.battery_size}--KWh Battery.")
        
mec = ElectricCar('MG','Comet',2026)
print(mec.get_descriptive_name())

mec.battery.describe_battery()
mec.battery.get_range()

