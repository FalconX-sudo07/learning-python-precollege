current_number = 1
while current_number<=5:
    print(current_number)
    # current_number=1     #the most subtle mistake, so use 
    current_number+=1
#using continue
current_no = 0
while current_no<10:
    current_no+=1
    if current_no % 2 ==0:
        continue           #the continue statement is used to ignore whatever is divisible by 2(since modulo 0), and print the rest
    print(current_no)

#method 1 to echo a mssg
prompt = '\n tell me something and i will repeat it'
prompt += '\nEnter quit to end the program!'


message = ""
while message != 'quit':            #!= means not equal to, can also use is not
# while message is not 'quit':
    message=input(prompt)
    # print(message)    #delete this if u dont want to print quit
#until here, this method doesnt work fully since quit doesnt break the code, it prints 'quit', soo...
    if message!='quit':
        print(message)

#method 2 also produces the same as method 1
prompt = '\n tell me something and i will repeat it'
prompt += '\nEnter quit to end the program!'
while True:
    message=input(prompt)
    if message=='quit':
        break
    print(message)
    
#method 3 is by using a flag
prompt = '\n tell me something and i will repeat it'
prompt += '\nEnter quit to end the program!'
active = True
while active:
    message = input(prompt)
    if message=='quit':
        active = False
    else:
        print(message)
        

unconfirmed_users = ['shyam','pinda','jassi','jameel']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("verifying user: "+current_user.title())
    confirmed_users.append(current_user)
    
    print("\n the following users have been confirmed: ")
    
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    

pets = ['dog','cat','gorilla','snake']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)


responses = {}
polling_active = True

while polling_active:
    name = input("what is your name?: ")
    response = input("which mountain would u like to climb?: ")

    responses[name]=response

    repeat = input("would u like to let another person enter the poll?: ")
    if repeat == 'no':
        polling_active = False
    
print('\n--- Poll Results ---')
for name,response in responses.items():
    print(name+" would you like to climb "+response)


