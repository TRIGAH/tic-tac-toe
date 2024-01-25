import random

game_board = [['','',''],['','',''],['','','']]


def generated_choices(board):
    if check_board(board) == False:    
        choose_row = random.choice(range(len(board)))
        choose_row_position = random.choice(range(len(board[choose_row])))
        board[choose_row][choose_row_position] = 'X'

        choose_row_o = random.choice(range(len(board)))
        choose_row_position_o = random.choice(range(len(board[choose_row_o])))
        if board[choose_row_o][choose_row_position_o] == 'X':
            board[choose_row_o][choose_row_position_o] = 'O'
        else:
            board[choose_row_o][choose_row_position_o] = 'O'
    else:
        print("Game Over")        
   
def check_board(board):
    return all([all(board[i]) for i in  range(len(board)) ])

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def win(board):
    # Check Rows
    # Hint --- If the item in a Row == 1st item in all the other Rows
    for row in board:
        if all( cell == row[0]  and cell != '' for cell in row ):
            return True
    
    # #Check Columns
    for i in range(3):
        if  all( col[i] == board[i+1][i]  and col[i] != '' for col in board ):
            return True
        
    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(3)):
        return True

    if all(board[i][2 - i] == board[0][2] and board[i][2 - i] != ' ' for i in range(3)):
        return True

    return False     

def move(board):
    while check_board(board) == False:
        move_x = input('Enter 1 to move: ')
        if move_x == '1':
            generated_choices(board)
            print_board(board)
    if win(board) == True and check_board(board) == True:
        print("WIN")
    else:
        print('Try Again')    

move(game_board)        
 
 
         


















    # Check columns
    # for col in range(3):
    #     if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(3)):
    #         return True
