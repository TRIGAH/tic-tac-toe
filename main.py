import random

game_board = [['1','2','3'],['4','5','6'],['7','8','9',]]



def check_full_board(board):
    return all([all(board[i]) for i in  range(len(board)) ])

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

print(check_full_board(game_board))
print_board(game_board)

choose_row = random.choice(range(len(game_board)))
choose_row_position = random.choice(range(len(game_board[choose_row])))
game_board[choose_row][choose_row_position] = 'x'
print(game_board)