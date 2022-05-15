#dictionary = a changeable,unordered collection of unique key:value pairs
#fast because they use hashing,allow us to access a value qyickly

capitals= {"usa":"washington DC",
			"india":"new delhi",
			"china":"beijing",
			"russia":"moscow"}

capitals.update({"germany":"berlin"})
capitals.update({"usa":"los vegas"})
print(capitals["india"])
# print(capitals(["germany"])
print(capitals.get("germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.pop("germanys"))

for key,value in capitals.items():
	print(key,value)