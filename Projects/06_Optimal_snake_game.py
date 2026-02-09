import random, time, os, msvcrt
from collections import deque

WIDTH = 60
HEIGHT = 20
x = WIDTH//2
y = HEIGHT//2
gameOver = False
score = 0
direction = "STOP"
fruitX = random.randint(0,WIDTH-1)
fruitY = random.randint(0,HEIGHT-1)
tail = deque()

def setup():
    global gameOver, x, y, fruitX, fruitY, score, tail, direction
    x = WIDTH//2
    y = HEIGHT//2
    gameOver = False
    score = 0
    direction = "STOP"
    fruitX = random.randint(0,WIDTH-1)
    fruitY = random.randint(0,HEIGHT-1)
    tail = deque()

def Draw():
    os.system("cls")
    print("#"*(WIDTH+2))
    for i in range(HEIGHT-1):
        row = "#"+"".join("O" if (i,j) == (y,x) else 
                          "*" if (i,j)==(fruitY,fruitX) else
                          "o" if (i,j) in tail else
                          " " for j in range(WIDTH))+"#"
        print(row)
    print("#"*(WIDTH+2) + f"\nScore : {score}")

def Input():
    global direction, gameOver
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        direction = {"a":"LEFT", "d":"RIGHT", "w":"UP","s":"DOWN"}.get(key,direction)
        if key=='x':gameOver = True

def Logic():
    global x, y, fruitX, fruitY, score, gameOver, tail
    tail.appendleft((x,y))
    if len(tail)>score//10:tail.pop()
    x, y = (x-1 if direction == "LEFT" else x+1 if direction == "RIGHT" else x),(y-1 if direction == "UP" else y+1 if direction == "DOWN" else y)
    if x>=WIDTH or x<0 or y>=HEIGHT or y<0 or (x,y) in tail: gameOver = True
    if (x,y) == (fruitX, fruitY):
        score+=10
        fruitX, fruitY = random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)



if __name__=="__main__":
    setup()
    while not gameOver:
        Draw()
        Input()
        Logic()
        time.sleep(0.03)    # speed
