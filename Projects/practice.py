# Tic Tac Toe

import os
import random

BOARD_SIZE = 3
X, O = 'X', 'O'

class Score:
    def __init__(self):
        self.player = 0
        self.computer = 0
        self.draw = 0

score = Score()

def input_difficulty():
    while True:
        try:
            difficulty = int(input("\nEnter your difficulty level : \n\nHuman (Standard)\nGod (Impossible to win)\n\nEnter your choice : "))
            if difficulty in [1,2]:
                return difficulty
            print("\nIncorrect choice, choose 1 or 2")
        except ValueError:
            print("\nInvalid input! Enter 1 or 2")


def print_board(board):
    os.system("cls")
    print(f"\nSCORE :    Player X's : {score.player}    Computer : {score.computer}     Draw : {score.draw}")
    print("Tic Tac Toe\n")
    for i in range(BOARD_SIZE):
        print("  |".join(board[i]))
        if i < BOARD_SIZE - 1:
            print("---+---+---")


def check_win(board,player):
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or all(board[j][j]==player for j in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE-1-i] == player for i in range(BOARD_SIZE)):
        return True
    return False

def check_draw(board):
    return all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

def is_valid_move(board,row,col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == ' '

def player_move(board):
    while True:
        try:
            row, col = map(int, input("\nEnter row and col (1-3) for X : ").split())
            row, col = row - 1, col - 1
            if is_valid_move(board,row,col):
                board[row][col] = X
                return
            print("\nInvalid move! Try again...")
        except ValueError:
            print("\nEnter two numbers between 1 and 3")

def computer_move(board,difficulty):
    # 1. Win if possible
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j]== ' ':
                board[i][j] = O
                if check_win(board,X):
                    return
                board[i][j] = ' '

    # 2. Block player win
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == ' ':
                board[i][j] = X
                if check_win(board,X):
                    board[i][j] = O
                    return
                board[i][j] = ' '

    if difficulty == 2:
        # 3. Play centre if available
        if board[1][1] == ' ':
            board[1][1] = O
            return

        # 4. Play corners if available
        corners = [(0,0),(0,2),(2,0),(2,2)]
        random.shuffle(corners)
        for row, col in corners:
            if board[row][col] == ' ':
                board[row][col] = O
                return
    
    # 5. Play first available move
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == ' ':
                board[i][j] = O
                return
            
def play_game(difficulty):
    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = X if random.choice([True,False]) else O

    while True:
        print_board(board)
        if current_player == X:
            player_move(board)
            if check_win(board,X):
                score.player += 1
                print_board(board)
                print("\nCongratulation! you have won.")
                break
            current_player = O
        else:
            computer_move(board,difficulty)
            if check_win(board,O):
                score.computer += 1
                print_board(board)
                print("\nI won! But you played well...")
                break
            current_player = X
        
        if check_draw(board):
            score.draw += 1
            print_board(board)
            print("\nIt's a draw.")
            break




def main():
    difficulty = input_difficulty()
    while True:
        play_game(difficulty)
        replay = input("\nDo you want to play again? (y/n) : ").lower()
        if replay != 'y':
            print("\nBye Bye! Thanks for playing....")
        else:
            play_game(difficulty)

if __name__ == "__main__":
    main()