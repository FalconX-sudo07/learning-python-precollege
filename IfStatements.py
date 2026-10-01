cars = ['audi','bmw','mercedes','suzuki']
for car in cars:
    if car == 'bmw':            #an '=' sign is to assign a value for the operator
                                #a '==' sign is to check whether the value is it or not
        print(car.upper())
        
    else:
        print(car.title())

car = "Audi"
car.lower()=="audi"


answer = "hello"
if answer != "hello":
    print("the answer is incorrect!")
else:
    print("the correct answer")
    

requested_food = ['pizza','pasta','biriyani','donuts']

'donuts' in requested_food
'macaroons' in requested_food


banned_users = ['david','alvarez','messi']
user = str(input("enter the person u want to view: "))
if user !=banned_users:
    print("the user is not banned")
else:
    print("user is banned")
    
    
age = int(input("enter your age: "))
# if age<4:
    # print("your age is: " +age+ " hence your allowed in the park")
# elif age<10 and age>=4:
    # print("your age is: " +age+ " hence you are allowed to use only a few items")
# else:
    # print("your age is: " +age+ " hence you are not allowed in the park!") 
#in the above u cannot concatenate a string and an integer,hence it should be:

if age<4:

     print("your age is: " +str(age)+ " hence your allowed in the park")

elif age<10 and age>=4:

     print("your age is: " +str(age)+ " hence you are allowed to use only a few items")

else:

     print("your age is: " +str(age)+ " hence you are not allowed in the park!") 



requested_vips = []
number = int(input("enter the number of vip's u want to have: "))
# for t in number:            #u can't use for t in number, since number is an integer,instead use:
for t in range(number):
    vips = str(input("enter the name of the vip: "))
    requested_vips.append(vips)

# print("the vip's are" +" "+ requested_vips) #u cant concatenate a list to a string, hence use:
    
print("the vip's are" +" "+ str(requested_vips))

available = ['Pepperoni','Sausage','Mushrooms','Extra Cheese','Onions','Black Olives','Green Peppers','Bacon']

requested = []
t = int(input("enter the number of toppings u want: "))
for topping in range(t):
    topping = str(input("enter what u want: "))
    requested.append(topping.title())
    
for topping in requested:
    if topping in available:
        print("adding "+topping+".")
    else:
        print("sorry, "+topping+" is not available")

