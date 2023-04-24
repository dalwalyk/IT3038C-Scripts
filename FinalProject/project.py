# Define a 3x3 board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Function to print the board
def print_board():
    for row in board:
        print(row)

# Function to check if there is a winner
def check_winner(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    player = 'X'
    while True:
        row = int(input("Enter the row number (0-2): "))
        col = int(input("Enter the column number (0-2): "))
        if board[row][col] == '-':
            board[row][col] = player
            print_board()
            if check_winner(player):
                print(player + " wins!")
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print("That cell is already taken. Try again.")

# Start the game
play_game()
