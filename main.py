   
   
def check_board(board):
    return all(cell != ' ' for row in board for cell in row)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def win(board):
    
    # Check Rows
    for row in board:
        if all(cell == row[0] and cell != ' ' for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(3)):
            return True
        
    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(3)):
        return True

    if all(board[i][2 - i] == board[0][2] and board[i][2 - i] != ' ' for i in range(3)):
        return True

    return False     
  


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player

            if win(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_board(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.") 
 
if __name__ == "__main__":
    tic_tac_toe()


















