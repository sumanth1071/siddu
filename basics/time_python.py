import time

# epoch = The "epoch" serves as a reference point from which time is measured.
		# when computer thinks the time began (reference point)

print(time.ctime(0)) #convert a time in seconds since epoch to a readble string


print(time.time()) #return cuurent seconds since epoch

print(time.ctime(time.time())) #gives current time uisng ctime and time funtions

time_object = time.localtime() #local time (unreadable)
time_object = time.gmtime() #UTC time
print(time_object)

# using strftime(string_format_time) function 
# strftime(function,tiem_object)
local_time=time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time)

# using strptime(string_parse_time) function
# string -> time
# strptime(time_object,function)
time_string = "20 april 2022"
time_object = time.strptime(time_string,"%d %B %Y")
print(time_object)

# using asctime convert a tuple into struct_time by given format
# (year,month,day,hours,minutes,secs,#day of the week,#day of the year,dst)
time_tuple = (2022,7,10,20,2,20,0,100,0)
time_string = time.asctime(time_tuple)
print(time_string)


# using mktime(mark_time)
# gives the seconds from epoch to the time mentioned in the tuple
# (year,month,day,hours,minutes,secs,#day of the week,#day of the year,dst)
time_tuple = (2022,7,10,20,2,20,0,100,0)
time_string = time.mktime(time_tuple)
print(time_string)

