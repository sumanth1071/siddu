import random
#to perform random operation on lists

while True:
#using while state creates an iteration 

	choices = ["rock","paper","scissors"]

	computer=random.choice(choices)
	#randomly selects objects from the choices list

	player=None
	#player value should put None due to different possibilities

	while player not in choices:
	#check whether the player entered correct input
	#till he enter correct input the statement prints infinite times
		player = input("rock, paper, or scissors?: ").lower()

	if player == computer:
		print("computer: ",computer)
		print("player: ",player)
		print("tie!")

	elif player == "rock":
		if computer == "scissors":
			print("computer: ",computer)
			print("player :",player)
			print("You Win")
		if computer == "paper":
			print("computer: ",computer)
			print("player :",player)
			print("You Lose")
	elif player == "paper":
		if computer == "scissors":
			print("computer: ",computer)
			print("player :",player)
			print("You Lose")
		if computer == "rock":
			print("computer: ",computer)
			print("player :",player)
			print("You Win :)")
	elif player == "scissors":
		if computer == "rock":
			print("computer: ",computer)
			print("player :",player)
			print("You Lose")
		if computer == "paper":
			print("computer: ",computer)
			print("player :",player)
			print("You Win :)")

	play_again = input("Play agian(yes/no)?: ").lower()

	if play_again != "yes":
	#if the player don't want to continue
	#the while loop breaks
		break

print("Bye!")
