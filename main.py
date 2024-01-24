import random

game_board = [['','',''],['','',''],['','','']]
PLAYERS = ['X','O']
POSITION= ''

def check_full_board(board):
    return all([all(board[i]) for i in  range(len(board)) ])

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def generated_choices(board):
    choosen_player = random.choice(PLAYERS)
    choose_row = random.choice(range(len(board)))
    choose_row_position = random.choice(range(len(board[choose_row])))
    board[choose_row][choose_row_position] = 'X'

    choose_row_o = random.choice(range(len(board)))
    choose_row_position_o = random.choice(range(len(board[choose_row_o])))
    if board[choose_row_o][choose_row_position_o] == 'X':
        board[choose_row_o][choose_row_position_o] = 'O'
    else:
        board[choose_row_o][choose_row_position_o] = 'O'
   



def play_game(board):
    generated_choices(board)
    print_board(board)    

if check_full_board(game_board):
    print("Game Over")  
else:
    play_game(game_board)

