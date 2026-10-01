# num = 10
# print("dividing numbers...")
# result = num/0
# print('answer is: ',result)

#[try:code that might throw an exception | except:code to handle exception]block
try:
    num = 10
    print("dividing numbers...")
    result = num/0
    print('answer is: ',result) 
except ZeroDivisionError:
    print("error bruhh,cant divide a number by 0")

#else:runs when no exception occurs
num = int(input('enter desired number: '))      #if we enter a string instead of an integer, we get a value error... so we fix this by
print('you entered'+num)

try:
    num = int(input('enter desired number: '))
    print('you entered'+num)

except ValueError:
    print('please enter only integer')
else:
    print('no errors occured')

#Finally
try:
    num = 10
    print("dividing numbers...")
    result = num/0
    print('answer is: ',result) 
except ZeroDivisionError:
    print("error bruhh,cant divide a number by 0")
finally:
    print('this will always excecute')
    