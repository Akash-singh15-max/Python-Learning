import random
import time
import os
import msvcrt  # For Windows keyboard input handling

# Game settings
WIDTH = 60
HEIGHT = 20

game_over = False
x = WIDTH // 2
y = HEIGHT // 2
fruit_x = random.randint(0, WIDTH - 1)
fruit_y = random.randint(0, HEIGHT - 1)
score = 0
tail_x = []
tail_y = []
n_tail = 0

direction = "STOP"

def setup():
    global game_over, x, y, fruit_x, fruit_y, score, n_tail, tail_x, tail_y, direction
    game_over = False
    direction = "STOP"
    x = WIDTH // 2
    y = HEIGHT // 2
    fruit_x = random.randint(0, WIDTH - 1)
    fruit_y = random.randint(0, HEIGHT - 1)
    score = 0
    n_tail = 0
    tail_x = []
    tail_y = []

def draw():
    os.system("cls" if os.name == "nt" else "clear")
    
    # Top border
    print("#" * (WIDTH + 2))
    
    for i in range(HEIGHT - 1):
        for j in range(WIDTH):
            if j == 0:
                print("#", end="")
            
            if i == y and j == x:
                print("O", end="")
            elif i == fruit_y and j == fruit_x:
                print("*", end="")
            elif (j, i) in zip(tail_x, tail_y):
                print("o", end="")
            else:
                print(" ", end="")
            
            if j == WIDTH - 1:
                print("#", end="")
        print()
    
    # Bottom border
    print("#" * (WIDTH + 2))
    print(f"Score: {score}")

def input_handler():
    global direction, game_over
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8") 
        if key == 'a':
            direction = "LEFT"
        elif key == 'd':
            direction = "RIGHT"
        elif key == 'w':
            direction = "UP"
        elif key == 's':
            direction = "DOWN"
        elif key == 'x':
            game_over = True

def logic():
    global x, y, fruit_x, fruit_y, score, game_over, n_tail, tail_x, tail_y
    
    if n_tail > 0:
        tail_x.insert(0, x)
        tail_y.insert(0, y)
        if len(tail_x) > n_tail:
            tail_x.pop()
            tail_y.pop()
    
    if direction == "LEFT":
        x -= 1
    elif direction == "RIGHT":
        x += 1
    elif direction == "UP":
        y -= 1
    elif direction == "DOWN":
        y += 1
    
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
        game_over = True
    
    if (x, y) in zip(tail_x, tail_y):
        game_over = True
    
    if x == fruit_x and y == fruit_y:
        score += 10
        fruit_x = random.randint(0, WIDTH - 1)
        fruit_y = random.randint(0, HEIGHT - 1)
        n_tail += 1

def main():
    setup()
    while not game_over:
        draw()
        input_handler()
        logic()
        time.sleep(0.05)  # Faster game speed

if __name__ == "__main__":
    main()
