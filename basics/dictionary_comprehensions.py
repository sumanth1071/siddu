# dictionary comprehension = create dictionaries using an expression

# can replace loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if condition}
# dictionary = {key: expression (if/else) for (key,value) in iterable}
# dictionary = {key: funtion(value) for (key,value) in iterable}
# ---------------------------------------------------------------------------

cities_f = {"vijayawada":45,"guntur":40,"vizag":43,"godavari":35}
cities_c = {key: round((value-32)*(5/9)) for (key,value) in cities_f.items()}
print(cities_c)

# ---------------------------------------------------------------------------

weather = {"vijayawada":"sunny", "guntur":"cloudy","vizag":"cloudy","godavari":"rainy"}

cloudy_weather = {key: value for (key,value) in weather.items() if value == "cloudy"}
print(cloudy_weather)

# ---------------------------------------------------------------------------

cities = {"vijayawada":45,"guntur":40,"vizag":43,"godavari":35}
desc_cities = {key: ("warm" if value>=40 else "cold") for (key,value) in cities.items()}
print(desc_cities)

# --------------------------------------------------------------------
def check_temp(value):
	if value >= 45:
		return "hot"
	elif 45 >= value >= 40:
		return "warm"
	else:
		return "cold"

cities = {"vijayawada":45,"guntur":40,"vizag":43,"godavari":35}
con_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(con_cities)