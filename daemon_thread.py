# daemon thread = a thread that runs in background for program to run
# your programs will not wait for daemon threads to complete before exit
# non-daemon threads cannot normally be killed,stay alive until the task is complete 
# usually used for background tasks, garbage collection ,waiting for input, long running processes
import threading
import time

def timer():
	print()
	count = 0
	while True:
		time.sleep(1)
		count += 1
		print("logged in for ",count," seconds")

x=threading.Thread(target=timer,daemon=True)
x.setDaemon(False) # used to change a object into daemon
x.start() #used to start a thread

print(x.isDaemon()) #check the object is daemon or not returns boolean

ans = input("do you want to exit? \n")
