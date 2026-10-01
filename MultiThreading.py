#multithreading = Used to perform multiple tasks concurrently (multitasking)
#                 Good for I/O bound tasks like reading files or fetching data from APIs
#                 threading.Thread(target=my_function)

import threading
import time

def walk_dog():
    time.sleep(8)
    print('you finish walking the dog')   
    
def take_out_trash():
    time.sleep(4)
    print('you take out the trash')
    
def get_mail():
    time.sleep(10)
    print('you get the mail')


# walk_dog()
# take_out_trash()      # all these run on the same thread
# get_mail()

#accomplishing all 3 tasks at the same time,runs code concurrently
chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()
#in the final output, the executed order is,
# you take out the trash
# you finish walking the dog
# you get the mail          here, the task which takes the least amount of time gets executed first

# print('chores r finished!')   this takes the least amount of time, and gets executed first, which is wrong... hence
chore1.join()
chore2.join()
chore3.join()
print('all chores are complete!')
