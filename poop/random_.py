import random

x = random.randint(1,6)
y = random.random()

print(x)

mlist=["rock","papers","scissors"]
z=random.choice(mlist)
print(z)

cards=[1,2,3,4,5,6,7,8,9,"j","k","q","a"]
random.shuffle(cards)


print(cards)

ttt=["X","O"]
t=random.choice(ttt)
print(t)