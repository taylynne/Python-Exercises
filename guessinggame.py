# Practise Python
# Project Guessing Game One, exercise 9
# 8 June 2018
# I think I've done this before with the lrn 2 automate w/ python stuff,
# so it'll be good review... If I can recall exactly what I've done.

import random

def guessingGame(x):
	num = random.randint(1,10)
	while True:
		if x == num:
			print("Awesome! That's the number I was thinking of.")
			break
		elif x > num:
			print("Unfortunately, the number I'm thinking of is smaller...")
			x = int(input("Try again. "))
		elif x < num:
			print("It seems the number I am thinking of is larger!")
			x = int(input("Try again. "))

print("Let's play a small game!  Try to guess the number I'm thinking of, between 1 and 10.")
guess = int(input("What number am I thinking of? \n"))

guessingGame(guess)


# come back to this to update how to keep track of the number of guesses, and do other "extras"

