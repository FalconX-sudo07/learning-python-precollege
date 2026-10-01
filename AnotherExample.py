import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping')
    
#do_something()        #running on a single thread,output gives 2 seconds if we use the next line of code
#do_something()
#finish = time.perf_counter()
#print(f'Finished in {round(finish-start,2)} second(s)')

#  with multi threading,
# smth1 = threading.Thread(target=do_something)
# smth2 = threading.Thread(target=do_something)

# smth1.start()
# smth2.start()
# smth1.join()
# smth2.join()
# finish = time.perf_counter()
# print(f'Finished in {round(finish-start,2)} second(s)')

threads=[]
#even better!
for _ in range(10):
    t = threading.Thread(target=do_something, args = [3])
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
    
 
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')
