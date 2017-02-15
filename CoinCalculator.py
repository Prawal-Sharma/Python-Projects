# Coin Calculator - Prawal Sharma - Aug 1 
""" Program that takes weight of different coins and returns the number of coins and
how many coin holders will be needed. Program is able to take in grams or pounds and 
return total sum """
import math 

print "\t Welcome to Coin Calculator"

weight = raw_input("Are you inputting your weights in pounds or grams? ")

qs = [] 
ds = []
ns = []
ps = []


def quarter_counter():
	if weight == "pounds":
		q_weight = 0.01250021
	elif weight == "grams":
		q_weight = 5.670 
	input_quarters = raw_input("Weight of Quarters: ")
	number_of_quarters = float(input_quarters) / (q_weight)
	number_of_quarters = math.ceil(number_of_quarters)
	q_wrapper = number_of_quarters / 40
	q_wrapper = math.ceil(q_wrapper)
	qs.append(number_of_quarters)
	print "The number of quarters you have is %f" % (number_of_quarters)
	print "The number of coin wrappers you need -rounded up- is %f" % (q_wrapper)

def dime_counter():
	if weight == "pounds":
		d_weight = 0.0050000841
	elif weight == "grams":
		d_weight = 2.268
	input_dimes = raw_input("Weight of Dimes: ")
	number_of_dimes = float(input_dimes) / (d_weight)
	number_of_dimes = math.ceil(number_of_dimes)
	d_wrapper = number_of_dimes / 50
	d_wrapper = math.ceil(d_wrapper)
	ds.append(number_of_dimes)
	print "The number of dimes you have is %f" % (number_of_dimes)
	print "The number of coin wrappers you need -rounded up- is %f" % (d_wrapper)

def nickel_counter():
	if weight == "pounds":
		n_weight = 0.0110231
	elif weight == "grams":
		n_weight = 5.000
	input_nickels = raw_input("Weight of Nickels: ")
	number_of_nickels = float(input_nickels) / (n_weight)
	number_of_nickels = math.ceil(number_of_nickels)
	n_wrapper = number_of_nickels / 40
	n_wrapper = math.ceil(n_wrapper)
	ns.append(number_of_nickels)
	print "The number of nickels you have is %f" % (number_of_nickels)
	print "The number of coin wrappers you need -rounded up- is %f" % (n_wrapper)

def penny_counter():
	if weight == "pounds":
		p_weight = 0.00551156
	elif weight == "grams":
		p_weight = 2.500
	input_pennys = raw_input("Weight of Pennys: ")
	number_of_pennys = float(input_pennys) / (p_weight)
	number_of_pennys = math.ceil(number_of_pennys)
	p_wrapper = number_of_pennys / 50
	p_wrapper = math.ceil(p_wrapper)
	ps.append(number_of_pennys)
	print "The number of pennies you have is %f" % (number_of_pennys)
	print "The number of coin wrappers you need -rounded up- is %f" % (p_wrapper)

def total_coins():
	q_total_money = qs[0] * .25
	d_total_money = ds[0] * .10
	n_total_money = ns[0] * .05
	p_total_money = ps[0] * .01
	total_of_all = q_total_money + d_total_money + n_total_money + p_total_money
	print "In total you have %f dollars worth of coins" % (total_of_all)

def final():
	quarter_counter()
	dime_counter()
	nickel_counter()
	penny_counter()
	total_coins()
	try_again()

def try_again():
	answer = raw_input("Would you like to try again? ")
	if answer.lower() == "yes":
		final()
	elif answer.lower() == "no":
		print "Thanks for using our service, so you next time!"
	else:
		print "I'm sorry I didn't get that..."
		try_again()	

final()






