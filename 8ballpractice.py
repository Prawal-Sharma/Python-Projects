import random, time
from random import randint 

messages = ["That's a good question...", "Hell no", "No", 
"The future is bright", "The future is grim", "Maybe", "Yes, but with consequences"]


def asker():
	
	question = raw_input("Ask me anything ")
	time.sleep(1)
	print "Your question is " + '"'+ str(question) + '"' 
	time.sleep(1.5)
	print "Give me a second to think about this"
	time.sleep(2.5)
	print "okay"
	time.sleep(1.5)
	print messages[randint(0, len(messages)-1)]
	play_again()

def play_again():
	inp = raw_input("Would you like to play again? ")
	
	if inp.lower() == "yes":
		asker()
	elif inp.lower() == "no":
		print "Your loss"
		
	else:
		print "I have no idea what you just said.."
		play_again()

asker()


	