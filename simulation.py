from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB )
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of raquetball between two")
    print("players called 'A' and 'B'. The abilities of each player")
    print("is indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInputs():
    a = eval(input("What is the probability that player A wins a serve? "))
    b = eval(input("What is the probability that player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames( n, probA, probB ):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simGame(probA, probB)
        if scoreA > scoreB :
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simGame(probA, probB ):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver( scoreA, scoreB ):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver( a, b ):
    return a == 15 or b == 15


def printSummary( winsA, winsB ):
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: %d (%0.1f%%)" % (winsA, float(winsA)/n*100) )
    print("Wins for B: %d (%0.1f%%)" % (winsB, float(winsB)/n*100) )



main()