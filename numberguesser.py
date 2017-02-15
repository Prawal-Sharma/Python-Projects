""" This program prompts the player to guess a number from 1 - 100 and provides
feedback for the user (if the number is too low or too high), program allows user to play 
again with a prompt"""
from random import randint

print " \t Welcome to Number Guesser"
print " \t Try to guess a number from 1 - 100, as you guess you will be notified \
   if your guess was too high or too low, at the end you will also be shown how   many \
times it took for you to arrive at the answer. Have fun!"



def game():
	number = randint(1,100)
	#print number, just for debugging 
	total = 1 
	guess = raw_input("Guess a number from 1 - 100 ")
	while int(guess) != number:
		if int(guess) > number:
			print "Too high"
			total += 1
			guess = raw_input("Guess again ")
		elif int(guess) < number:
			print "Too low"
			total += 1
			guess = raw_input("Guess again ")

	if int(guess) == number:
		print "You got it!"	
	if total == 1:
		print "It took you %d guess" % (total)
	else:
		print "It took you %d guesses" % (total)
	play_again()

def play_again():
	answer = raw_input("Wanna play again? ")
	if answer.lower() == "yes":
		game()
	elif answer.lower() == "no":
		print "Ok, thanks for playing"

game()
		
		
	

	