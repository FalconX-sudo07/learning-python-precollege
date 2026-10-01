class Dog():

    def __init__(self,name,age):
        self.name = name        #self is used inside a class to refer to the current object (instance) of that class. It lets each object keep track of its own data and ensures that methods operate on the correct instance. Without self, Python wouldn’t know which object’s attributes or methods you’re trying to access.
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        print(self.name.title()+" just rolled over!")


my_dog = Dog('willie',6)
print("My dog's name is, "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()


dawg = Dog('Lucy',3)
print("\n your dog's name is, "+dawg.name.title()+".")
print("your dog is "+str(dawg.age)+" years old.")
dawg.sit()
dawg.roll_over()




class Car():
    def __init__(self,make,model,year): #The __init__ method in Python classes is a special constructor method. It’s automatically called whenever you create a new object from the class, and its job is to initialize the object’s attributes with the values you provide.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def getname(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name
    
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it.")

    #Modifying an Attribute’s Value Through a Method
    def update_odometer(self,mileage):
        self.odometer_reading=mileage

        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('you cant roll back an odometer!')

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

    
my_new_car = Car('Audi','a4',2016)
print(my_new_car.getname())   #object.method()
my_new_car.read_odometer()
#Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(30)
my_new_car.read_odometer()
my_new_car.update_odometer(12030)
my_new_car.read_odometer
