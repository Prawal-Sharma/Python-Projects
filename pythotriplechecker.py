print "\t \t Welcome to Pythogorean Triple Checker "

sides = []

def get_sides():
	for turn in range(3):
		side = raw_input("Side: ")
		sides.append(side)

def checker():
	get_sides()
	hypo = max(sides)
	sides.remove(hypo)
	a = sides[0]
	b = sides[1]
	
	
	if int(a) ** 2 + int(b) ** 2 == int(hypo) ** 2:
		print 'Success'
	else: 
		print ' Failure ' 
	play_again()

def play_again():
	inp = raw_input("Wanna try again? (yes or no) ")
	if inp.lower() == "yes":
		checker()
	elif inp.lower() == "no":
		print "See you next time"
	else: 
		print "What?"
		play_again()

checker()
