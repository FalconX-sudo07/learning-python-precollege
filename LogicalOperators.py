#and
age = 20
citizenship = True
if age>=18 and citizenship == True:
    print('eligible to vote! ')


age = 10
citizenship = False
if age>=18 and citizenship == True:
    print('not eligible to vote')


#or
age = 17
has_perms = True
if age>=18 or has_perms == True:
    print('you can go to the concert')


#not
#not False = True
#not True = False

its_sunny = False
if not its_sunny:
    print("it is sunny!")
    