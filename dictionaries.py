alien = {'color':'green','points':5}
# 
print(str(alien['points']))
print("you have earned"+str(alien['points']))
# 
print(alien)
alien['x-position']=0
alien['y-position']=25
print(alien)
#  
print('colour of the alien is: '+alien['color']+'.')
# 
# 
# 
alien['color']='yellow'
print('new color is: '+str(alien['color'])+'.')


alien_game = {'x_pos':0,'y_pos':0,'speed':'medium'}
alien_game['speed']=str(input("enter desired speed: "))
if alien_game['speed']=='slow':
    x_increment=1
elif alien_game['speed']=='medium':
    x_increment=2
else:
    x_increment=3  

alien_game['x_pos']=alien_game['x_pos']+x_increment

print("New x-pos: "+str(alien_game['x_pos']))


del alien['points']     #vlaue is removed permanently
print(alien)


user = {'uname':'ksiddharth',
        'fname':'k',
        'lname':'siddharth'}

for key,value in user.items():
    print('\nKey: '+key)
    print('value: '+value)

favlang = {
    'jen':'python',
    'alan':'c#',
    'barry':'java',
    'phil':'django'
}
friends = ['jen','phil']
for name,fav in favlang.items():
    if name in friends:
        print("hello, " + name +"!"+"\nI see, your favourite language is, "+fav)
 #also can be written as:       
for name in favlang.keys():     #for keys
    print(name.title())

    if name in friends:
        print("hello "+name.title()+"!")
        
for name in sorted(favlang.keys()):
    print(name.title()+",thank you for taking the poll.")
    
for languages in favlang.values():
    print("\nfav languages of each1 "+str(languages.title()))
    



