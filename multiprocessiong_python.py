# ------------------------------
# mutliprocessing
# ------------------------------

# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL(global interpreter lock) used for threading
# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading  = better for io bound tasks (waiting around)


from multiprocessing import Process,cpu_count 
import time


def counter(num):
	count = 0
	while count < num:
		count += 1

def siddu():

	print("my macbook have "+str(cpu_count())+" cores")#to print no of cores a computer's cpu consists
	a=Process(target=counter,args=(100000,))
	b=Process(target=counter,args=(100000,))
	c=Process(target=counter,args=(100000,))
	d=Process(target=counter,args=(100000,))
	e=Process(target=counter,args=(100000,))
	f=Process(target=counter,args=(100000,))
	g=Process(target=counter,args=(100000,))
	h=Process(target=counter,args=(100000,))
	i=Process(target=counter,args=(100000,))
	j=Process(target=counter,args=(100000,))
	
	a.start()
	b.start()
	c.start()
	d.start()
	e.start()
	f.start()
	g.start()
	h.start()
	i.start()
	j.start()
	
	a.join()
	b.join()
	c.join()
	d.join()
	e.join()
	f.join()
	g.join()
	h.join()
	i.join()
	j.join()

	print("this process took ",time.perf_counter(),"seconds")

if __name__ == "__main__":
# the above statement should be mentioned to create others processes
	siddu()


