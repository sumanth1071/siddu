"""
1.create dictionary of questions which includes
	key as question and value as answer
2.create options list using list of ist
3.create function new_game()
4.declare an empty list guesses[],
	correct_guesses=0,
	question_number=1
5.print questions from dictionary using for loop
6.print the options of list of every questions using for loop by indexing[-1]
	because the question_number is 1 so decrementing the value by 1 gets the 
	first value of the list
7.create a empty variable guess and input the values
8.append that value into the guesses list
9.now we have to print the correct answers 
10.before printing the answers we have to check the answers
11.define a fuction check_answers
	of parameters answer and guesses
12.inside the function check answer and guesses matches or not using 
	ifelse condition statement
13.if correct return as 1 else return 0
14.now inside the new_game function call the variable correct_guesses
13.using addition and assignment operator call the check_answers function
	of parameters (key from the dictonary using get method,input guess)
	till here we print one set of options for 1 questions
	in next next we print next set of options for next question
14.call variable question_number using increment and assignment operator(+=)
	and assign 1 to it
15.till now we have checked answers and printed they are correct or wrong
	now we have print the score of the player
16.now define function display_score of parameters correct_guesses and guesses
17.inside display_score print the values from the dictionary using for loop
18.in same function print the answers from the list guesses
19.now to print the score create variable score and get the score by
	score=int((correct_guesses/len(questions))*100)
20.now call display_score function in the new_game fucntion
	of parameters correct_guesses and guesses
21.now call the function 
	new_game() 
	now succesfully the quiz completed
21.now to play again we have to create function play_again
22.create a variable which takes input yes or no
23.now create a ifelse statement to check whether the player
	wants to play again or not by giving boolean values as return values
24.now call the play_again statement as a condtion in while loop
	now call the new_game function as a statement in while loop
	if the boolean value in the  play_again function returns false the
	while loop terminates
	and prints sayonara
"""
questions = {"who bought twitter in 2022? ":"A",
"what is most easiest programming language? ":"B",
"what is sumanth's favorite series? ":"C",
"what is sumanth's favorite anime? ":"B"}

options = [["A.elon musk","B.mark zuck","C.jeff bezos","D.me"],
["A.java","B.Python","C.c","D.C++"],
["A.la casa de papel","B.stranger things","C.breaking bad","D.You"],
["A.death note","B.naruto","C.demon slayer","D.haikyuu"]]
#--------------------------
def new_game():

	guesses=[]
	# for guesses by player
	correct_guesses=0
	question_num=1

	for key in questions:
	#prints the first value in dictionary
		print("#--------------------------")
		print(key)
		
		for i in options[question_num-1]:
		#getting the options from the list
			
			print(i)
			#print the values from the list
		
		guess = input("enter (A,B,C or D): ").upper()
		
		guesses.append(guess)
		#adds the answer given by the player to the list(guesses)

		correct_guesses += check_answer(questions.get(key),guess)
		question_num += 1
		#to get next options

	display_score(correct_guesses,guesses)
#--------------------------
def check_answer(answer,guess):
	if answer == guess:
		print("CORRECT!")
		return 1
	else:
		print("WRONG!")
		return 0
#--------------------------
def display_score(correct_guesses,guesses):
	print("#--------------------------")
	print("RESULTS: ")
	print("#--------------------------")
	print("ANSWERS: ",end="")
	for i in questions:
		print(questions.get(i),end=" ")
	print("")
	print("guesses: ",end=" ")
	for i in guesses:
		print(i,end=" ")
	print("")

	score = int((correct_guesses/len(questions))*100)
	print("Your score is "+str(score)+"%")
#--------------------------
def play_again():
	response = input("Do You Wanrt To Play Again? (Yes or No)").upper()
	if response == "YES":
		return True
	else:
		return False
#--------------------------


new_game()

while play_again():
	new_game()

print("sayonara")
