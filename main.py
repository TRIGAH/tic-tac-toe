import random

game_board = [['','',''],['','',''],['','','',]]



def check_full_board(board):
    return all([all(board[i]) for i in  range(len(board)) ])

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def play_game(board):
    choose_row = random.choice(range(len(board)))
    choose_row_position = random.choice(range(len(board[choose_row])))
    board[choose_row][choose_row_position] = 'x'
    print_board(board)

if check_full_board(game_board):
    print("Game Over")  
else:
    play_game(game_board)

