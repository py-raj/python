# Import 'random' to generate a random number
import random

# 'try...catch' block to accept the range of numbers from the user
try:
	print('''
----Welcome To Number Guessing Game----

Please enter the range of random number.''')
	minNum = abs(int(input("Min: ")))
	maxNum = abs(int(input("Max: ")))
	rand_num = random.randint(minNum, maxNum)
except:
	print("Something went wrong, please try again!")

# Initializing the variables
# print(rand_num) --for testing purpose only--
number = 0
attempt = 0

# A function to accept the number from user
def getNum():
	global number
	global attempt
	number = int(input(f"{attempt}. Enter a number: "))

# A function which asks user if he wants to play again or not
def askPlayAgain():
	global attempt
	playAgainInput = input("\nDo you wanna play again? : ")
	print("\n")
	if (playAgainInput.upper() == 'Y'):
		attempt = 0
		guessNum()
	else:
		print("Thanks for playing.")

# A main function that handles the game
def guessNum():
	global attempt
	global number
	attempt = attempt + 1
	getNum()	#call
	# Handling the attempts
	if (attempt <= 2):
		# Comparing the 'user input' and the 'generated random number'
		if (number == rand_num):
			print(f"Congratulations, you guessed the number.\nNumber is: {number}.")
		elif (number > maxNum) :
			print(f"please enter the number in range of {minNum} to {maxNum}")
			guessNum()
		elif (number < minNum):
			print(f"please enter the number in range of {minNum} to {maxNum}")
			guessNum()
		else:
			print("Nope, please try again!\n")
			guessNum()	#call
	else:
		print("You lost.")
		askPlayAgain()	#call

guessNum()	#call