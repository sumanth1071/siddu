#slicing= creating a sub sting from another string
#using indexing[] and slice()
#[start:stop:steps]


name="sumanth banka"

l_name=name[8:]
f_name=name[0:8]
fl_name=name[::2]
rev_name=name[::-1]
# 	inclusive exclusive

print(f_name)
print(l_name)
print(fl_name)
print(rev_name)

#negative indexing

webs="http://google.com"
webs2="http://netflix.com"
slice=slice(7,-4)
print(webs[slice])
print(webs2[slice])