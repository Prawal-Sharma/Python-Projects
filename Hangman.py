#Hangman project - Prawal 
from random import randint

print "\n\t Welcome to hangman (without the actual hanging part...), you have as   \
\t many tries as the length of the word plus 5 \
to guess the answer, good luck!"

def begin():
	words = ["happy", "sad", "mad", "super", "dumb", "introduction", "computing", "apple", 
	"systems", "elementary", "japanese", "wireless", "network", "pokemon", "pencil", "circuit", 
	"course"]
	global word
	word = words[randint(0, len(words))-1]
	global test
	test = word
	word = list(word)
	# print word 
	global length_word
	length_word = len(word)
	global display

	
	display = []


	display.append(["_"]  * (length_word))

def print_display(display):
	for i in display:
		print " ".join(i)

def gamer():
	global length_word
	begin()
	global display 
	global word
	print_display(display)
	for turn in range(length_word + 5):
	
		guess = raw_input("Guess a letter ")
		for times in range(length_word):
			for i in word:
				if guess == i:
					display[0][word.index(i)] = i
					word[word.index(i)] = "!"
				elif guess.lower() == "quit":
					print "Thank you for playing"
					exit()
		print_display(display)
		if turn == 0:
			print "You have used %d turn" % (turn + 1)
		else:
			print "You have used %d turns" % (turn + 1)
	
		if "".join(word) == "!" * length_word:
			print "You win!! Wooooo"
			play_again()
	
		if turn == length_word + 4:
			print "You lost..."
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "
			
			print "The word was %s" % (test)
			play_again()
		

def play_again():
	answer = raw_input("Do you want to play again? ")
	if answer.lower() == "yes":
		gamer()
	elif answer.lower() != "no":
		print "I didn't get that"
		play_again()
	else:
		print "Thanks for playing"


		

gamer()
		

	







			





