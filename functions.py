def greet_user(username):           #here username is an argument
    print("hello, "+username.title()+" !")
    
username = str(input("enter your username: "))
greet_user(username)


def describe_pet(animal_type,pet_name):
    print("\n i have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name)
    
t = int(input("how many people's pets do u want to register? "))
for i in range(t):
    animal_type = str(input("what kind is your animal?: "))
    pet_name = str(input("what is it's name?: "))

    describe_pet(animal_type,pet_name)
    # describe_pet(pet_name,animal_type)    #order matters in positional arguments
    
describe_pet(animal_type='hamster',pet_name='harry')  #keyword argument
#orrrr...
describe_pet('hamster','harry')


def descbook(title,author='rick riordan',genre = 'fiction'):  #this is setting a default value for genre
    print("\n i am reading a "+genre+' book')
    print("the book "+title.title()+" is written by "+author.title())
    
        # descbook(author = 'rick riordan')           #this is just calling it once
descbook('the lost titan')
descbook(title='the alchemist',author = 'paulo coelho',genre='drama')    #this alters the original function
#orrrr u can use...
descbook('the alchemist','paulo coelho','drama')



def desc_city(city,country):
    print("the city "+city.title()+" is in "+country.title())

city = str(input("enter the name of your city: "))
country = str(input("enter the name of the country u live in: "))
desc_city(city,country)
    
def make_shirt(size,message='i love python!'):
    print("the size of your shirt is "+size+" it reads "+message)

t = int(input("how many shirts do u want to buy:  "))    
for shirt in range(t):
    size = str(input('enter your shirt size: '))
    make_shirt(size)
    
    
    
    
    
    
#using return statement in here!!
def full_name(fname,lname,mname=None ):  #None signifies that it can be either empty or full or we can aLso use ' '
    if mname:
        full_name = fname + ' '+mname + ' '+lname    
    else:
        full_name = fname + ' '+ lname
    return(full_name.title())    #returns the output with each starting letter capitalized

print(full_name('jimmy','donaldson'))
print(full_name('john','hooker','lee'))


def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician = build_person('kalva','siddharth',14)
print(musician)


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

#to generate an infinity loop
while True:
    print('\n tell your name: ')
    fname = input('first: ')
    if fname == 'quit':
        break
    lname = input('last: ')
    if lname =='quit':
        break
    formatted_name = get_formatted_name(fname,lname)
    print("\nHello, "+formatted_name+" !")
    

def greet_usernames(names):
    for name in names:
        mssg = "hello, "+name.title()+" !"
        print(mssg)
        
usernames = []

t = int(input("enter number of ppl u want to greet: "))
for i in range(t):
    name = str(input("enter your name: "))
    usernames.append(name)
    
greet_usernames(usernames)    



