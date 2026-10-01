import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping')
    

with concurrent.futures.ThreadPoolExecutor() as excecuter:
    f1 = excecuter.submit(do_something,1)

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
