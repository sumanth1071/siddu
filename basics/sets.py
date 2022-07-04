#sets = unordered,unindexed,no duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl",'plate','cup',"knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)
# print(dishes.difference(utensils))
print(utensils.difference(dishes))
# for x in dinner_table:
	# print(x)

