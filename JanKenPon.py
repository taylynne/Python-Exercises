# Practise Python
# Project Rock Paper Scissors, exercise 08
# First 3 chili exercise!
# 3 June 2018

import sys


def rockPaperScissors(x, y):
    if x == y:
        print("A tie! Just draw some straws to see who wins... or play again!")
    elif x == "Rock":
        if y == "Scissors":
            print(p1 + " wins!")
        elif y == "Paper":
            print(p2 + " wins!")
    elif x == "Scissors":
        if y == "Rock":
            print(p2 + " wins!")
        elif y == "Paper":
            print(p1 + " wins!")
    elif x == "Paper":
        if y == "Rock":
            print(p1 + " wins!")
        elif y == "Scissors":
            print(p2 + " wins!")
    else:
        print("Please select from rock paper or scissors next time.")


def play(x, y):
    x = input(p1 + ", Rock, Paper, or Scissors? ").capitalize()
    y = input(p2 + ", Rock, Paper, or Scissors? ").capitalize()
    rockPaperScissors(x, y)


print("Hello! This is going to be a simple game of rock, paper scissors.")
print("Try not to cheat and look at your opponent's answer now ;)")

p1 = input("Who is the first player? ")
p2 = input("And who is the second player? ")

play(p1, p2)

while True:
    again = input("Do you want to play again? yes or no ").capitalize()
    if again == "Yes":
        play(p1, p2)
    else:
        print("We'll see you next time!")
        sys.exit()
