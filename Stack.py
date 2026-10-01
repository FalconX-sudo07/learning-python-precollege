cardStack = []
cardStack.append('5 of diamonds')
print(print(','.join(cardStack)))
cardStack.append('3 of clubs')
print(','.join(cardStack))
cardStack.append('ace of hearts')
print(','.join(cardStack))
cardStack.pop()
print(','.join(cardStack))
 
#pg 11, call stack
def a():
    spam = 'Ant'
    print('spam is '+spam)
    b()
    print('spam is '+spam)
    
def b():
    spam = 'Bobcat'
    print('spam is '+spam)
    c()
    print('spam is '+spam)

def c():
    spam = 'Coyote'
    print('spam is '+spam)
    
a()

