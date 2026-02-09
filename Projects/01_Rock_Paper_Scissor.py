'''
    Rock Paper Scissor
    1 for Rock
    0 for Paper
    -1 for Scissor
'''

import random
import os

yourDict = {'r':1, 'p':0, 's':-1}
reverseDict = {1:"Rock", 0:"Paper", -1:"Scissor"}
playerScore = 0
computerScore = 0
rounds = 3

os.system("cls")
print("\n----- Welcome to the Game -----")
print("\nRules : r = Rock, p = Paper and s = Scissor")
for i in range(1,rounds+1):
    print("\n=============================================")
    print(f"\nRound {i} of {rounds}")
    yourInput = input("\nEnter your choice : ")
    if yourInput not in yourDict:
        print("\nInvalid input! Please input 'r', 'p' or 's'.")
        continue
    computer = random.choice([1,0,-1])
    you = yourDict[yourInput]
    print(f"\n\nYou choose : {reverseDict[you]}\nCPU choose : {reverseDict[computer]}")
    if(computer == you):
        print("\nIt's a draw.")
    else:
        if(you==1 and computer==-1):
            print("\nYou win")
            playerScore+=1
        elif(you==1 and computer==0):
            print("\nCPU win")
            computerScore+=1
        elif(you==0 and computer==1):
            print("\nYou win")
            playerScore+=1
        elif(you==0 and computer==-1):
            print("\nCPU win")
            computerScore+=1
        elif(you==-1 and computer==0):
            print("\nYou win")
            playerScore+=1
        elif(you==-1 and computer==1):
            print("\nCPU win")
            computerScore+=1
        else:
            print("\nSomething went wrong!")

print("\n----- Final Score -----\n")
print(f"You : {playerScore}  |  CPU : {computerScore}")
if(playerScore>computerScore):
    print("\nCongratulations! You won the game.")
elif(playerScore<computerScore):
    print("\nCPU wins! Better luck next time.")
else:
    print("\nIt's a draw! Well played.")
print("\nThanks for playing....\n")