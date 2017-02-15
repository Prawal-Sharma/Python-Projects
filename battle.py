from random import randint 
name = raw_input("What's your name? ")

age = raw_input("how old are you? ")


print "Oh, so your name is %s and you are %s years old!" % (name, age)

print "If you want to go further type 'yes' or 'no'"

answer = raw_input()


if answer.lower() == 'yes':
	print "That's good to hear, let the journy begin"
else: 
	print "Sorry to hear that, maybe next time..."

print "The first step in this quest is a guessing game...I will give you 2 turns to guess a random number from 1 to 3"

number = randint(1,3)
print number

for turn in range(2):
	guess = int(raw_input("Guess: "))
	
	if guess == number:
		print "Impressive, your intiution is quite good!"
		task = True 
		break
	else:
		if turn == 1:
			print "Sorry, better luck next time"
			task = False
		else: 
			print "Try again"
			task = False

if task == True:
	print "I'm very glad you made it past the first step, we have much more to do!"


	
		

	

	
	

