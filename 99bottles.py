question = raw_input("How many bottles of beer are on the wall? ")
numbers = range(int(question) + 1)
numbers = numbers[::-1]

for i in numbers:
	if i > 2: 
		print str(i) + " bottles of beer on the wall " + str(i) + " bottles of beer", 
		print "take on down pass it around " + str(i-1) + " bottles of beer on the wall \n"
	
	elif i == 2:
		print str(i) + " bottles of beer on the wall " + str(i) + " bottles of beer", 
		print "take one down pass it around " + str(i-1) + " bottle of beer on the wall \n"
	elif i == 1:
		print str(i) + " bottle of beer on the wall " + str(i) + " bottle of beer", 
		print "take one down pass it around, no more bottles of beer on the wall"
	
	
