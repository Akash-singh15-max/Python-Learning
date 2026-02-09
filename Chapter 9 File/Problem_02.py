# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the
# Hiscore whenever the game() function breaks the Hi-score.

# game = random number 
import random

def game():
    print("You are playing the game:")
    score = random.randint(1,50)
    # fetch the highscore
    with open("highscore.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0
    
    print(f"Your score: {score}")
    if(score>highscore):
        # write the high score to the file
        with open("highscore.txt","w") as f:    
            f.write(str(score))
    
    return score
game()