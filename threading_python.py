# thread = a flow of execution , like a seperate order of execution

# each thread takes a turn running to achieve concurrency

# GIL = gloabal interpreter lock
# allows only one thread to hold the control of python interpreter


# cpu bound = program/tasks spends most of its time waiting for internal events(CPU intensive)
# use multiprocessing



# io bound = program/tasks spends most of its time waiting for external events(user input,web scarping)
# use multithreading

import threading
import time

def eat_breakfast():
	time.sleep(3)
	print("you ate eat_breakfast")

def drink_coffee():
	time.sleep(4)
	print("you drank caffine")

def study():
	time.sleep(5)
	print("you finished studyng")





x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffee,args=())
y.start()

z = threading.Thread(target=study,args=())
z.start()

# to achieve synchronous threading 
# hold the main thread till every thread joined
x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()



print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())






