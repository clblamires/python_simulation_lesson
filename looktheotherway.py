# look the other way
# choose a direction, left or right, and the computer randomly selects a direction
# if you're looking the opposite direction as the computer, you win and gain +1 points
# if you look the same direction, you lose 1 point

# simulate the game by choosing two random numbers, one for the "player"
# and one for the computer. Choose the number of games to simulate and get the win vs lose rate
# score can never go below zero points

from random import random
from math import floor

gamesToSimulate = 5000
score           = 0
wins            = 0
losses          = 0


for i in range(gamesToSimulate):
    player   = floor( random() * 2 )
    computer = floor( random() * 2 )
    if player == computer:
        losses = losses + 1
        score = score - 1
        if score < 0:
            score = 0
    else:
        wins = wins + 1
        score = score + 1

print("Wins: " , wins)
print("Losses: ", losses)
print("Final Score: ", score)