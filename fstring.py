#What is an f-string?
#f = formatted string literal
#Introduced in Python 3.6
#Lets you embed variables, expressions, and function calls directly inside a string using {}.



name = 'Siddharth'
age = 17
is_female = False
message = f"my name is {name} and i am {age} years old and female = {is_female}"
print(message)

    
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
