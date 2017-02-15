""" Class Practice, maybe game """
from random import randint 
class Enemy1():
	global health
	health = 100
	def health_add(self):
		global health
		health += 10
		print "Enemy1 drank a hp potion health is now " + str(health)
	
	def health_down(self):
		global health 
		health -= 10
		print "You attacked, Enemy1 health is now " + str(health)
		if health == 0:
			print "Enemy is now dead"
Enem = Enemy1()


print "You see an enemy, with 100 health"

for turn in range(10):
	number = randint(1,10)
	if number % 2 == 0:
		okay = "okay"
	else:
		okay = "no"
	print "Do you want to attack?"
	answer = raw_input("yes or no?: ")

	if answer.lower() == "yes":
		Enem.health_down()
		if okay == "okay":
			Enem.health_add()
		
		
	



		
		
	