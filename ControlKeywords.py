#Break
#stops loop even if the continous loop is not satisfied yet

movies = ['inception','the matrix','interstellar','titanic']
for movie in movies:
    print('now watching, '+movie)
    if movie == 'interstellar':
        print('stopping the grind ')
        break


#Continue
#skip rest of code in the loop and move to the other iteration

dishes = ['pizza','pasta','spicey curry','noodles','spicey noodles']
for dish in dishes:
    if 'spicey' in dish:        #pasta doesnt have spicey in it so it just skips this loop, and moves to the next dish available
        print('skipping',dish)
        continue
    print('eating dish',dish)



#Pass
#acts like a placeholder

tasks = ['clean the room','skip','go to basketball','practice python']
for task in tasks:
    if task =='skip':
        pass
    else:
        print('doing task',task)    
