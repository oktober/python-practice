'''
Ask user to enter their name and age
Print out message telling them when they'll turn 100
'''

name = input("What's your name?: ")
age = int(input("What's your age?: "))
repeat = int(input("How many times do you want to hear this?: "))

turn_100 = 100 - age
message = "{0}, you'll turn 100 in {1} years".format(name, turn_100)

for x in range(repeat):
	print(message)