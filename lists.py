bicycles = ["trek", "cannondale", "redline", "specialized"]  #list
print(bicycles)
print(bicycles[0])
print(bicycles[-1])  #first from last
print(bicycles[0].title())

bicycles[0]="Brompton"  #modyfying a list
print(bicycles)
bicycles.append("decathlon")
bicycles.insert(2,"firefox")    #in the new list, the position of firefox will be 2
print(bicycles)
del bicycles[-1]
print(bicycles)
bicycles.sort()
bicycles.reverse()
#or, it can be written as 
bicycles.sort(reverse=True)

print(bicycles)
people = []
people.append("siddhu")
people.append("suhas")
people.append("siddharth")
print(people)
print(len(people))
people.sort()
print(people)



magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
    

for magician in magicians:
    print(magician.title()," ","that was a great trick!")
    print("i cant wait to see your next trick! "+magician.title()+"\n")
    

animals=[]
animals.append("lion")
animals.append("cheetah")
animals.append("tiger")
animals.append("gorilla")
animals.insert(2,"puma")
print(animals)
for i in animals:
    print(i.title()+" ""is a dangerous animal") #here i is important, it is not animals
print(sorted(animals))

for value in range(1,5):
    print(value)
    
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

#orrrrrr
squares=[]
for value in range(1,11):
    squares.append(value**2)
     
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])          #only prints from [1] to [3] (before the index 4)

for player in players[:-3]:   
    print(player.title())  #blank can be anywhere either to left or right of :
    

my_foods = ['pizza', 'falafel', 'carrot cake']

friend=my_foods[:]
my_foods.append('roll')
friend.append('vada pav')
print(my_foods)
print(friend)

print("===========")
friend=my_foods
print(my_foods)
print(friend)
