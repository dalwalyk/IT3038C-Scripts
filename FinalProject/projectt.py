import pygame

# Initialize pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define font
FONT = pygame.font.Font(None, 36)

# Define game variables
board = [['', '', ''], ['', '', ''], ['', '', '']]
player = 'X'
game_over = False
winner = None

# Define functions
def draw_board():
    for row in range(3):
        for col in range(3):
            x = col * 133 + 33
            y = row * 133 + 33
            pygame.draw.rect(screen, WHITE, (x, y, 100, 100))
            text = FONT.render(board[row][col], True, BLACK)
            screen.blit(text, (x + 35, y + 35))

def draw_text(text, color, x, y):
    text = FONT.render(text, True, color)
    screen.blit(text, (x, y))

def check_winner():
    global game_over, winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            winner = board[row][0]
            game_over = True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            winner = board[0][col]
            game_over = True
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        game_over = True
    if all(all(row) for row in board) and not winner:
        game_over = True

def handle_click(row, col):
    global player, board
    if not game_over and board[row][col] == '':
        board[row][col] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // 133
            col = mouse_pos[0] // 133
            handle_click(row, col)
            check_winner()

    # Draw the board
    screen.fill(BLUE)
    draw_board()

    # Draw game over message
    if game_over:
        draw_text('Game Over', BLACK, 150, 10)
        if winner:
            draw_text(f'{winner} wins!', BLACK, 150, 50)
        else:
            draw_text('Tie Game!', BLACK, 150, 50)

    # Update the screen
    pygame.display.update()
